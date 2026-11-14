#!/usr/bin/env python3
"""
Benchmark Evaluation Harness.

Reads the benchmark questions from benchmark_questions.txt, sends them one at a
time to up to 10 LLMs in parallel, and writes one PDF of answers per model.

    pip install -r requirements.txt
    python app.py                                  # opens http://127.0.0.1:8765
    python app.py --questions other_benchmark.txt  # use a different question file

API keys live only in this process's memory for the length of a run. They are
never written to disk or logged. The server only listens on 127.0.0.1.
"""

import io
import json
import os
import random
import re
import sys
import threading
import time
import uuid
import webbrowser
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib import error as urlerror
from urllib import request as urlrequest
from urllib.parse import unquote

from pdf_report import build_pdf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")
QUESTIONS_FILE = os.path.join(HERE, "benchmark_questions.txt")
MAX_MODELS = 10
DEMO_KEY = "sk-ant-demo-0000-NOT-A-REAL-KEY"

# ------------------------------------------------------------------ providers
# kind: "anthropic" | "gemini" | "openai" (any OpenAI-compatible chat endpoint)
PROVIDERS = {
    "anthropic":  {"name": "Anthropic",   "kind": "anthropic", "base": "https://api.anthropic.com/v1"},
    "openai":     {"name": "OpenAI",      "kind": "openai",    "base": "https://api.openai.com/v1"},
    "gemini":     {"name": "Google Gemini", "kind": "gemini",  "base": "https://generativelanguage.googleapis.com/v1beta"},
    "mistral":    {"name": "Mistral",     "kind": "openai",    "base": "https://api.mistral.ai/v1"},
    "xai":        {"name": "xAI",         "kind": "openai",    "base": "https://api.x.ai/v1"},
    "deepseek":   {"name": "DeepSeek",    "kind": "openai",    "base": "https://api.deepseek.com/v1"},
    "groq":       {"name": "Groq",        "kind": "openai",    "base": "https://api.groq.com/openai/v1"},
    "together":   {"name": "Together AI", "kind": "openai",    "base": "https://api.together.xyz/v1"},
    "openrouter": {"name": "OpenRouter",  "kind": "openai",    "base": "https://openrouter.ai/api/v1"},
    "custom":     {"name": "Custom (OpenAI-compatible)", "kind": "openai", "base": ""},
}


class ProviderError(Exception):
    def __init__(self, msg, retryable=False):
        super().__init__(msg)
        self.retryable = retryable


def _post_json(url, headers, body, timeout):
    data = json.dumps(body).encode()
    req = urlrequest.Request(url, data=data, method="POST",
                             headers={"content-type": "application/json", **headers})
    try:
        with urlrequest.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except urlerror.HTTPError as e:
        detail = e.read().decode(errors="replace")[:400]
        try:
            j = json.loads(detail)
            detail = (j.get("error") or {}).get("message") if isinstance(j.get("error"), dict) else j.get("error") or j.get("message") or detail
        except Exception:
            pass
        retry = e.code in (408, 409, 425, 429, 500, 502, 503, 504, 529)
        raise ProviderError(f"HTTP {e.code}: {detail}", retryable=retry)
    except (urlerror.URLError, TimeoutError, ConnectionError) as e:
        raise ProviderError(f"Network error: {getattr(e, 'reason', e)}", retryable=True)


def call_model(slot, system, question, max_tokens, timeout=300):
    """Returns dict(text, output_tokens, stop_reason)."""
    prov = PROVIDERS[slot["provider"]]
    key = slot["api_key"]
    model = slot["model"]
    base = (slot.get("base_url") or prov["base"]).rstrip("/")
    if not base:
        raise ProviderError("Custom provider needs a base URL")

    if prov["kind"] == "anthropic":
        body = {"model": model, "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": question}]}
        if system:
            body["system"] = system
        j = _post_json(f"{base}/messages",
                       {"x-api-key": key, "anthropic-version": "2023-06-01"}, body, timeout)
        text = "".join(b.get("text", "") for b in j.get("content", []) if b.get("type") == "text")
        return {"text": text, "output_tokens": (j.get("usage") or {}).get("output_tokens"),
                "stop_reason": j.get("stop_reason")}

    if prov["kind"] == "gemini":
        body = {"contents": [{"role": "user", "parts": [{"text": question}]}],
                "generationConfig": {"maxOutputTokens": max_tokens}}
        if system:
            body["systemInstruction"] = {"parts": [{"text": system}]}
        j = _post_json(f"{base}/models/{model}:generateContent",
                       {"x-goog-api-key": key}, body, timeout)
        cands = j.get("candidates") or []
        if not cands:
            raise ProviderError(f"No answer returned ({json.dumps(j.get('promptFeedback', {}))[:200]})")
        parts = (cands[0].get("content") or {}).get("parts") or []
        text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
        return {"text": text, "output_tokens": (j.get("usageMetadata") or {}).get("candidatesTokenCount"),
                "stop_reason": cands[0].get("finishReason")}

    # OpenAI-compatible
    msgs = ([{"role": "system", "content": system}] if system else []) + \
           [{"role": "user", "content": question}]
    body = {"model": model, "messages": msgs}
    # OpenAI's newer models only accept max_completion_tokens; most others use max_tokens.
    body["max_completion_tokens" if slot["provider"] == "openai" else "max_tokens"] = max_tokens
    headers = {"authorization": f"Bearer {key}"}
    if slot["provider"] == "openrouter":
        headers.update({"HTTP-Referer": "http://127.0.0.1", "X-Title": "Benchmark Evaluation Harness"})
    j = _post_json(f"{base}/chat/completions", headers, body, timeout)
    choice = (j.get("choices") or [{}])[0]
    content = (choice.get("message") or {}).get("content")
    if isinstance(content, list):
        content = "".join(c.get("text", "") for c in content if isinstance(c, dict))
    return {"text": content or "", "output_tokens": (j.get("usage") or {}).get("completion_tokens"),
            "stop_reason": choice.get("finish_reason")}


def call_with_retries(slot, system, question, max_tokens, attempts=4):
    delay = 2.0
    for a in range(attempts):
        try:
            return call_model(slot, system, question, max_tokens)
        except ProviderError as e:
            if not e.retryable or a == attempts - 1:
                raise
            time.sleep(delay + random.random())
            delay *= 2


# ------------------------------------------------------------------ question file
HEADER_RE = re.compile(r"^\s*(Question\s+\d+)\s*(?:[—–:\-]+\s*(.*))?$", re.IGNORECASE)


def load_questions(path=None):
    """
    Parse the benchmark file into [{"id", "title", "text"}].

    Expected format (one block per question):
        Question 1 — Short title
        The full question text, on one or more lines.

    A file without "Question N" headers is read as blank-line-separated questions.
    """
    path = path or QUESTIONS_FILE
    with open(path, encoding="utf-8-sig") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    qs, cur = [], None
    if any(HEADER_RE.match(ln) for ln in lines):
        for ln in lines:
            m = HEADER_RE.match(ln)
            if m:
                cur = {"id": m.group(1).title(), "title": (m.group(2) or "").strip(), "body": []}
                qs.append(cur)
            elif cur is not None and ln.strip():
                cur["body"].append(ln.strip())
    else:
        block = []
        for ln in lines + [""]:
            if ln.strip():
                block.append(ln.strip())
            elif block:
                qs.append({"id": f"Question {len(qs) + 1}", "title": "", "body": block})
                block = []
    out = []
    for q in qs:
        text = " ".join(q["body"]).strip()
        if text:
            out.append({"id": q["id"], "title": q["title"], "text": text})
    return out


# ------------------------------------------------------------------ demo mode
def demo_call(question):
    """Fake-key run: no model is called; returns a labelled placeholder answer."""
    time.sleep(random.uniform(1.2, 3.0))     # feel like a real call
    words = len(question.split())
    return {"text": f"""**Demo placeholder: no model was called.** This run uses a fake API key, so the harness cannot produce a real answer. With a real key, the model's answer to this benchmark question would appear here, formatted like this.

## What this page shows
- The question was read from the benchmark file and sent through the same pipeline as a live call ({words} words).
- The answer slot, timing and layout are exactly what a live run produces.

## To get a real answer
1. Replace the fake key with a real API key.
2. Press Run again. Everything else stays the same.""",
            "output_tokens": None, "stop_reason": "demo"}


# ------------------------------------------------------------------ jobs
JOBS = {}
JOBS_LOCK = threading.Lock()


def _slug(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", s).strip("-")[:60] or "model"


def run_job(job):
    models, questions = job["models"], job["questions"]
    system = job["system"]
    with ThreadPoolExecutor(max_workers=len(models)) as pool:
        for qi, qd in enumerate(questions):
            q = qd["text"]
            if job["cancel"]:
                break
            job["current_q"] = qi

            def one(mi, q=q, qi=qi):
                cell = job["grid"][mi][qi]
                cell["status"] = "running"
                t0 = time.time()
                slot = job["models"][mi]
                try:
                    if slot["api_key"] == DEMO_KEY:
                        r = demo_call(q)
                    else:
                        r = call_with_retries(slot, system, q, job["max_tokens"])
                    cell.update(status="done", text=r["text"], output_tokens=r.get("output_tokens"),
                                stop_reason=r.get("stop_reason"), seconds=time.time() - t0)
                except Exception as e:   # noqa: BLE001  (show any failure in the grid)
                    msg = str(e).replace(slot["api_key"], "***") if slot["api_key"] else str(e)
                    cell.update(status="error", error=msg, seconds=time.time() - t0)

            # this question goes to every model at once; next question waits for all of them
            list(pool.map(one, range(len(models))))

    # PDFs
    job["phase"] = "pdf"
    folder = os.path.join(OUT_DIR, job["id"])
    os.makedirs(folder, exist_ok=True)
    for mi, m in enumerate(models):
        prov = PROVIDERS[m["provider"]]
        fname = f"{mi + 1:02d}_{_slug(m['label'] or m['model'])}.pdf"
        build_pdf(os.path.join(folder, fname),
                  {"label": m["label"] or m["model"], "provider_name": prov["name"], "model": m["model"]},
                  [q["text"] for q in questions], job["grid"][mi],
                  {"context_title": job["context_title"], "created": job["created"],
                   "demo": m["api_key"] == DEMO_KEY,
                   "titles": [f'{q["id"]}{" — " + q["title"] if q["title"] else ""}' for q in questions],
                   "source": os.path.basename(job["questions_file"])})
        job["files"].append(fname)
    # forget keys as soon as the run is over
    for m in models:
        m["api_key"] = "<cleared>" if m["api_key"] != DEMO_KEY else DEMO_KEY
    job["phase"] = "cancelled" if job["cancel"] else "done"


def start_job(payload):
    models = payload.get("models") or []
    qfile = QUESTIONS_FILE
    try:
        questions = load_questions(qfile)     # read fresh each run, so edits to the file apply
    except FileNotFoundError:
        raise ValueError(f"Question file not found: {qfile}")
    if not models:
        raise ValueError("Add at least one model.")
    if len(models) > MAX_MODELS:
        raise ValueError(f"At most {MAX_MODELS} models per run.")
    if not questions:
        raise ValueError(f"No questions found in {os.path.basename(qfile)}.")
    clean = []
    for m in models:
        p = m.get("provider")
        if p not in PROVIDERS:
            raise ValueError(f"Unknown provider: {p}")
        if not (m.get("model") or "").strip():
            raise ValueError(f"{PROVIDERS[p]['name']}: enter a model ID.")
        if not (m.get("api_key") or "").strip():
            raise ValueError(f"{PROVIDERS[p]['name']} ({m['model']}): enter an API key.")
        if p == "custom" and not (m.get("base_url") or "").strip():
            raise ValueError(f"Custom model {m['model']}: enter a base URL.")
        clean.append({"provider": p, "model": m["model"].strip(), "api_key": m["api_key"].strip(),
                      "label": (m.get("label") or "").strip() or m["model"].strip(),
                      "base_url": (m.get("base_url") or "").strip()})

    context = (payload.get("context") or "").strip()
    instructions = (payload.get("system_prompt") or "").strip()
    system = instructions
    if context:
        system = (instructions + "\n\n" if instructions else "") + \
                 "Use the following document as context for every question.\n\n<document>\n" + \
                 context + "\n</document>"
    ctitle = (payload.get("context_title") or "").strip()
    if context and not ctitle:
        ctitle = context.splitlines()[0][:90]

    jid = uuid.uuid4().hex[:10]
    job = {"id": jid, "models": clean, "questions": questions, "questions_file": qfile, "system": system,
           "context_title": ctitle, "max_tokens": int(payload.get("max_tokens") or 2000),
           "grid": [[{"status": "pending"} for _ in questions] for _ in clean],
           "current_q": 0, "phase": "running", "files": [], "cancel": False,
           "created": datetime.now()}
    with JOBS_LOCK:
        JOBS[jid] = job
    threading.Thread(target=_safe_run, args=(job,), daemon=True).start()
    return jid


def _safe_run(job):
    try:
        run_job(job)
    except Exception as e:  # noqa: BLE001
        job["phase"] = "failed"
        job["error"] = str(e)


def job_status(job):
    return {
        "id": job["id"], "phase": job["phase"], "current_q": job["current_q"],
        "error": job.get("error"),
        "questions": [q["text"] for q in job["questions"]],
        "question_ids": [q["id"] for q in job["questions"]],
        "models": [{"label": m["label"], "provider": m["provider"], "model": m["model"]} for m in job["models"]],
        "grid": [[{k: c.get(k) for k in ("status", "error", "seconds")} for c in row] for row in job["grid"]],
        "files": job["files"],
    }


# ------------------------------------------------------------------ http
class Handler(BaseHTTPRequestHandler):
    server_version = "BenchmarkEvaluationHarness/1.0"

    def log_message(self, fmt, *args):  # quiet, and never log bodies (keys)
        pass

    def _send(self, code, body, ctype="application/json", extra=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode()
        elif isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("content-type", ctype)
        self.send_header("content-length", str(len(body)))
        self.send_header("cache-control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            with open(os.path.join(HERE, "static", "index.html"), "rb") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if path == "/api/providers":
            return self._send(200, {"providers": [{"id": k, **v} for k, v in PROVIDERS.items()],
                                    "max_models": MAX_MODELS})
        if path == "/api/demo":
            return self._send(200, {"demo_key": DEMO_KEY})
        if path == "/api/questions":
            try:
                qs = load_questions()
                return self._send(200, {"file": os.path.basename(QUESTIONS_FILE), "questions": qs})
            except FileNotFoundError:
                return self._send(200, {"file": os.path.basename(QUESTIONS_FILE), "questions": [],
                                        "error": "File not found"})
        m = re.fullmatch(r"/api/status/([0-9a-f]+)", path)
        if m and m.group(1) in JOBS:
            return self._send(200, job_status(JOBS[m.group(1)]))
        m = re.fullmatch(r"/api/download/([0-9a-f]+)/(.+)", path)
        if m and m.group(1) in JOBS:
            job = JOBS[m.group(1)]
            name = unquote(m.group(2))
            folder = os.path.join(OUT_DIR, job["id"])
            if name == "all.zip":
                buf = io.BytesIO()
                with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
                    for fn in job["files"]:
                        z.write(os.path.join(folder, fn), fn)
                return self._send(200, buf.getvalue(), "application/zip",
                                  {"content-disposition": 'attachment; filename="benchmark-answers.zip"'})
            if name in job["files"]:
                with open(os.path.join(folder, name), "rb") as f:
                    disp = "inline" if "view=1" in self.path else "attachment"
                    return self._send(200, f.read(), "application/pdf",
                                      {"content-disposition": f'{disp}; filename="{name}"'})
        return self._send(404, {"error": "not found"})

    def do_POST(self):
        n = int(self.headers.get("content-length") or 0)
        try:
            payload = json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError:
            return self._send(400, {"error": "bad JSON"})
        if self.path == "/api/run":
            try:
                return self._send(200, {"id": start_job(payload)})
            except ValueError as e:
                return self._send(400, {"error": str(e)})
        m = re.fullmatch(r"/api/cancel/([0-9a-f]+)", self.path)
        if m and m.group(1) in JOBS:
            JOBS[m.group(1)]["cancel"] = True
            return self._send(200, {"ok": True})
        return self._send(404, {"error": "not found"})


def main():
    global QUESTIONS_FILE
    if "--questions" in sys.argv:
        QUESTIONS_FILE = os.path.abspath(sys.argv[sys.argv.index("--questions") + 1])
    print(f"  Questions file: {QUESTIONS_FILE} ({len(load_questions())} questions)")
    port = int(os.environ.get("PORT", "8765"))
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}"
    print(f"\n  Benchmark Evaluation Harness is running at {url}\n  (Ctrl+C to stop)\n")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

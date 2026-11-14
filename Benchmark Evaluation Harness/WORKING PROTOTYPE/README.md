# Working prototype

Runs the benchmark questions against up to 10 LLMs and produces **one PDF of answers per model** for the reviewing biologists to read.

This is a working prototype: it has been exercised end to end in demo mode, but not against live provider APIs.

The harness reads the questions from `benchmark_questions.txt`. It sends **one question at a time** to every model in parallel, and the next question starts once every model has answered. Each question is a fresh single-turn call, so a model never sees its earlier answers.

## Run it

```bash
cd "Benchmark Evaluation Harness/WORKING PROTOTYPE"
pip install -r requirements.txt     # just reportlab
python app.py                       # opens http://127.0.0.1:8765
```

Python 3.9+ is required. The server listens only on your own machine.

1. Add up to 10 models. For each one, choose a provider, type the model ID and paste the API key.
2. Check the questions shown on the page. They come from `benchmark_questions.txt`.
3. Press **▶ Run**. Hover over a red cell to see its error. Download the PDFs one at a time or as a zip. Copies are also saved to `output/<run-id>/`.

**Demo:** click **✨ Load the demo**, then **▶ Run**. This uses Claude Opus 5.5 with the fake key `sk-ant-demo-0000-NOT-A-REAL-KEY`. No model is called, and every answer in the PDF is a labelled placeholder.

## Benchmark questions

Edit `benchmark_questions.txt` to change the questions. The file is read again at the start of every run, so after editing just press **↻ Reload from file** or run again. Format:

```
Question 1 — Short title
Full question text (it can run over several lines).

Question 2 — Short title
...
```

The title appears in the PDF headers. A file without `Question N` headers is read as a list of questions separated by blank lines. To run a different file:

```bash
python app.py --questions path/to/other_benchmark.txt
```

## Providers

Anthropic, OpenAI, Google Gemini, Mistral, xAI, DeepSeek, Groq, Together AI and OpenRouter. **Custom** works with any OpenAI-compatible endpoint, such as a local model at `http://localhost:11434/v1`. If a provider rate-limits a request or returns a server error, the harness retries up to 4 times with backoff.

**Background document** is optional and empty by default. Leave it empty for a clean benchmark run, because anything pasted there is sent with every question. *Advanced settings* holds the shared system prompt and the max output tokens per answer.

## Keys and privacy

Keys are never written to disk or logged. They are sent only to the provider you chose, and they are cleared from memory when the run finishes. `output/` is git-ignored, so model answers are never committed by accident.

## Files

```
benchmark_questions.txt  the benchmark questions
app.py                   server, question-file parser, provider calls, run scheduling
pdf_report.py            PDF layout
static/index.html        web interface
fonts/                   Poppins (OFL) + DejaVu Sans, bundled so all characters render
```

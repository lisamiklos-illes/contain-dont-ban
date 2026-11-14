"""Builds one PDF per model: a cover page, then each benchmark question and its answer."""

import os
import re
from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, CondPageBreak, Frame, KeepTogether, ListFlowable, ListItem, PageBreak,
    PageTemplate, Paragraph, Preformatted, Spacer, Table, TableStyle,
)

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")

INK = colors.HexColor("#2B2340")
MUTED = colors.HexColor("#7A7190")
ACCENT = colors.HexColor("#7C5CFF")
ACCENT_SOFT = colors.HexColor("#F1ECFF")
PEACH = colors.HexColor("#FFB38A")
RULE = colors.HexColor("#E6E0F2")
ERR = colors.HexColor("#D9435B")

_fonts_ready = False


def _register_fonts():
    global _fonts_ready
    if _fonts_ready:
        return
    reg = {
        "Body": "DejaVuSans.ttf", "Body-Bold": "DejaVuSans-Bold.ttf",
        "Body-Italic": "DejaVuSans-Oblique.ttf", "Body-BoldItalic": "DejaVuSans-BoldOblique.ttf",
        "Mono": "DejaVuSansMono.ttf",
        "Head": "Poppins-Medium.ttf", "Head-Bold": "Poppins-Bold.ttf",
        "Head-Regular": "Poppins-Regular.ttf", "Head-Italic": "Poppins-Italic.ttf",
    }
    for name, fn in reg.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))
    pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                                  italic="Body-Italic", boldItalic="Body-BoldItalic")
    _fonts_ready = True


def _styles():
    s = {}
    s["body"] = ParagraphStyle("body", fontName="Body", fontSize=9.6, leading=14.2,
                               textColor=INK, spaceAfter=6, alignment=TA_LEFT)
    s["bullet"] = ParagraphStyle("bullet", parent=s["body"], spaceAfter=2.5)
    s["h1"] = ParagraphStyle("h1", fontName="Head-Bold", fontSize=12.5, leading=16,
                             textColor=INK, spaceBefore=8, spaceAfter=4, keepWithNext=1)
    s["h2"] = ParagraphStyle("h2", fontName="Head", fontSize=11, leading=14.5,
                             textColor=ACCENT, spaceBefore=7, spaceAfter=3, keepWithNext=1)
    s["quote"] = ParagraphStyle("quote", fontName="Head", fontSize=11, leading=15.5,
                                textColor=INK)
    s["qnum"] = ParagraphStyle("qnum", fontName="Head-Bold", fontSize=9, leading=11,
                               textColor=ACCENT)
    s["question"] = ParagraphStyle("question", fontName="Head", fontSize=12, leading=17,
                                   textColor=INK)
    s["meta"] = ParagraphStyle("meta", fontName="Head-Regular", fontSize=8, leading=10,
                               textColor=MUTED)
    s["mono"] = ParagraphStyle("mono", fontName="Mono", fontSize=8, leading=10.5,
                               textColor=INK, backColor=colors.HexColor("#F7F5FB"),
                               borderPadding=6, spaceBefore=4, spaceAfter=8)
    s["error"] = ParagraphStyle("error", parent=s["body"], textColor=ERR)
    s["cover_title"] = ParagraphStyle("ct", fontName="Head-Bold", fontSize=30, leading=34,
                                      textColor=INK)
    s["cover_sub"] = ParagraphStyle("cs", fontName="Head-Regular", fontSize=13, leading=18,
                                    textColor=MUTED)
    s["cover_label"] = ParagraphStyle("cl", fontName="Head", fontSize=8, leading=10,
                                      textColor=MUTED)
    s["cover_value"] = ParagraphStyle("cv", fontName="Body", fontSize=10, leading=13,
                                      textColor=INK)
    s["toc"] = ParagraphStyle("toc", fontName="Body", fontSize=9, leading=12.5,
                              textColor=INK, leftIndent=22, firstLineIndent=-22, spaceAfter=4)
    return s


# ---------- tiny markdown -> reportlab ----------

def _inline(text):
    t = escape(text)
    t = re.sub(r"`([^`]+)`", r'<font name="Mono">\1</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"__(.+?)__", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
               r'<link href="\2" color="#7C5CFF">\1</link>', t)
    return t


def _md_table(lines, s):
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c or "--") for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return []
    n = max(len(r) for r in rows)
    cell_style = ParagraphStyle("cell", parent=s["body"], fontSize=8.4, leading=11, spaceAfter=0)
    head_style = ParagraphStyle("cellh", parent=cell_style, fontName="Body-Bold")
    data = []
    for i, r in enumerate(rows):
        r = r + [""] * (n - len(r))
        data.append([Paragraph(_inline(c), head_style if i == 0 else cell_style) for c in r])
    t = Table(data, colWidths=[(6.5 * inch) / n] * n, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT_SOFT),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return [t, Spacer(1, 6)]


def markdown_to_flowables(md, s):
    out = []
    lines = (md or "").replace("\r\n", "\n").split("\n")
    i = 0
    para = []

    def flush_para():
        if para:
            out.append(Paragraph(_inline(" ".join(p.strip() for p in para)), s["body"]))
            para.clear()

    while i < len(lines):
        ln = lines[i]
        st = ln.strip()
        if st.startswith("```"):
            flush_para()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append(Preformatted("\n".join(code), s["mono"]))
            continue
        if not st:
            flush_para()
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", st)
        if m:
            flush_para()
            out.append(Paragraph(_inline(m.group(2)), s["h1"] if len(m.group(1)) <= 2 else s["h2"]))
            i += 1
            continue
        if st.startswith(">"):
            flush_para()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            q = Table([[Paragraph(_inline(" ".join(quote)), s["quote"])]], colWidths=["100%"])
            q.setStyle(TableStyle([
                ("LINEBEFORE", (0, 0), (0, -1), 2.5, PEACH),
                ("LEFTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            out += [q, Spacer(1, 8)]
            continue
        if st.startswith("|") and st.count("|") >= 2:
            flush_para()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            out.extend(_md_table(tbl, s))
            continue
        bm = re.match(r"^(\s*)([-*+•]|\d+[.)])\s+(.*)$", ln)
        if bm:
            flush_para()
            ordered = bm.group(2)[0].isdigit()
            items = []
            while i < len(lines):
                m2 = re.match(r"^(\s*)([-*+•]|\d+[.)])\s+(.*)$", lines[i])
                if m2:
                    indent = len(m2.group(1).expandtabs(4))
                    items.append([indent, m2.group(3)])
                    i += 1
                elif lines[i].strip() and items and lines[i].startswith((" ", "\t")):
                    items[-1][1] += " " + lines[i].strip()   # wrapped continuation line
                    i += 1
                elif not lines[i].strip():
                    # a blank line between items keeps the same list going ("loose" lists)
                    j = i
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    m3 = re.match(r"^(\s*)([-*+•]|\d+[.)])\s+", lines[j]) if j < len(lines) else None
                    if m3 and m3.group(2)[0].isdigit() == ordered:
                        i = j
                    else:
                        break
                else:
                    break
            lf_items = []
            for indent, txt in items:
                lf_items.append(ListItem(Paragraph(_inline(txt), s["bullet"]),
                                         leftIndent=14 + (12 if indent >= 2 else 0),
                                         value=None))
            out.append(ListFlowable(
                lf_items,
                bulletType="1" if ordered else "bullet",
                start="1" if ordered else "•",
                bulletFontName="Body-Bold" if ordered else "Body",
                bulletFontSize=8.5, bulletColor=ACCENT, leftIndent=14,
            ))
            out.append(Spacer(1, 4))
            continue
        if re.fullmatch(r"[-*_]{3,}", st):
            flush_para()
            out.append(Spacer(1, 6))
            i += 1
            continue
        para.append(ln)
        i += 1
    flush_para()
    # never leave a heading stranded at the bottom of a page
    glued, k = [], 0
    while k < len(out):
        f = out[k]
        if isinstance(f, Paragraph) and f.style.name in ("h1", "h2") and k + 1 < len(out):
            glued.append(KeepTogether([f, out[k + 1]]))
            k += 2
        else:
            glued.append(f)
            k += 1
    return glued


# ---------- page decorations ----------

def _decorate(model_label):
    def on_page(canv, doc):
        canv.saveState()
        w, h = LETTER
        canv.setFillColor(ACCENT)
        canv.rect(0, h - 6, w, 6, stroke=0, fill=1)
        canv.setFillColor(PEACH)
        canv.rect(0, h - 6, w * 0.18, 6, stroke=0, fill=1)
        canv.setFont("Head-Regular", 7.5)
        canv.setFillColor(MUTED)
        canv.drawString(inch, 0.55 * inch, f"Benchmark Evaluation Harness  ·  {model_label}")
        canv.drawRightString(w - inch, 0.55 * inch, f"{doc.page}")
        canv.restoreState()

    def on_cover(canv, doc):
        canv.saveState()
        w, h = LETTER
        canv.setFillColor(ACCENT_SOFT)
        canv.rect(0, 0, w, h, stroke=0, fill=1)
        # a little row of "voices": dots of varying size, one per model slot
        palette = ["#7C5CFF", "#FFB38A", "#5CC8B0", "#FF7FA8", "#FFD166",
                   "#6BA8FF", "#B48CFF", "#FF9F6B", "#7ED6A5", "#F48FB1"]
        x = inch
        for k, c in enumerate(palette):
            r = 7 + (k % 3) * 2.5
            canv.setFillColor(colors.HexColor(c))
            canv.circle(x + r, h - 1.45 * inch, r, stroke=0, fill=1)
            x += 2 * r + 7
        canv.restoreState()

    return on_page, on_cover


def build_pdf(path, model, questions, results, meta):
    """
    model:   dict(label, provider_name, model)
    questions: list[str]
    results: list[dict(status, text, error, seconds)] aligned with questions
    meta:    dict(context_title, created, demo)
    """
    _register_fonts()
    s = _styles()
    label = model.get("label") or model.get("model")
    on_page, on_cover = _decorate(label)

    doc = BaseDocTemplate(path, pagesize=LETTER, leftMargin=inch, rightMargin=inch,
                          topMargin=0.9 * inch, bottomMargin=0.9 * inch,
                          title=f"Benchmark answers: {label}", author="Benchmark Evaluation Harness")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate("cover", [frame], onPage=on_cover),
                          PageTemplate("body", [frame], onPage=on_page)])

    from reportlab.platypus.doctemplate import NextPageTemplate
    story = [Spacer(1, 1.15 * inch),
             Paragraph(escape(label), s["cover_title"]), Spacer(1, 8),
             Paragraph(f"Answers to {len(questions)} question{'s' if len(questions) != 1 else ''}, "
                       f"asked one at a time", s["cover_sub"]),
             Spacer(1, 0.4 * inch)]

    ok = sum(1 for r in results if r.get("status") == "done")
    secs = [r.get("seconds") or 0 for r in results if r.get("status") == "done"]
    created = meta.get("created") or datetime.now()
    rows = [
        ("PROVIDER", model.get("provider_name", "")),
        ("MODEL ID", model.get("model", "")),
        ("RUN DATE", created.strftime("%B %d, %Y  %H:%M")),
        ("QUESTIONS", meta.get("source") or "—"),
        ("CONTEXT", meta.get("context_title") or "None"),
        ("ANSWERED", f"{ok} of {len(questions)}" + (f"  ·  avg {sum(secs)/len(secs):.1f}s per answer" if secs else "")),
    ]
    if meta.get("demo"):
        rows.append(("MODE", "Demo run with a fake API key: placeholder answers, no model was called"))
    info = Table([[Paragraph(k, s["cover_label"]), Paragraph(escape(v), s["cover_value"])] for k, v in rows],
                 colWidths=[1.1 * inch, 5.4 * inch])
    info.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    titles = meta.get("titles") or [None] * len(questions)
    story += [info, Spacer(1, 0.45 * inch), Paragraph("BENCHMARK QUESTIONS", s["cover_label"]), Spacer(1, 6)]
    for qi, (q, t) in enumerate(zip(questions, titles), 1):
        name = t.split(" — ", 1)[1] if t and " — " in t else _shorten(q)
        story.append(Paragraph(f'<font name="Head-Bold" color="#7C5CFF">{qi:>2}</font>&nbsp;&nbsp;&nbsp;{_inline(name)}', s["toc"]))

    story += [NextPageTemplate("body"), PageBreak()]

    for qi, (q, r, t) in enumerate(zip(questions, results, titles), 1):
        kicker = f"QUESTION {qi} OF {len(questions)}"
        if t and " — " in t:
            kicker += "  ·  " + escape(t.split(" — ", 1)[1]).upper()
        head = Table([[Paragraph(kicker, s["qnum"])],
                      [Paragraph(_inline(q), s["question"])]],
                     colWidths=[doc.width])
        head.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), ACCENT_SOFT),
            ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
            ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, 0), 10), ("BOTTOMPADDING", (0, -1), (-1, -1), 11),
            ("TOPPADDING", (0, 1), (-1, 1), 3),
        ]))
        bits = []
        if r.get("seconds"):
            bits.append(f"{r['seconds']:.1f}s")
        if r.get("output_tokens"):
            bits.append(f"{r['output_tokens']:,} output tokens")
        if r.get("stop_reason") in ("max_tokens", "length", "MAX_TOKENS"):
            bits.append("cut off at the token limit")
        if qi > 1:
            # start a new question on a fresh page only if little room is left on this one
            story += [Spacer(1, 26), CondPageBreak(2.6 * inch)]
        story.append(KeepTogether([head, Spacer(1, 5),
                                   Paragraph("  ·  ".join(bits) or "&nbsp;", s["meta"]),
                                   Spacer(1, 8)]))
        if r.get("status") == "done":
            story += markdown_to_flowables(r.get("text", ""), s)
        else:
            story.append(Paragraph(f"No answer: {escape(r.get('error') or r.get('status') or 'not run')}", s["error"]))

    doc.build(story)
    return path


def _shorten(q, n=150):
    q = " ".join(q.split())
    return q if len(q) <= n else q[: n - 1].rsplit(" ", 1)[0] + "…"

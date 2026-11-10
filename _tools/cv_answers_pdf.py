"""Render the Computer Vision question bank with answers to a PDF.

usage: python -I cv_answers_pdf.py <root> <out.pdf>
Questions and sections come from 02_deep_learning/03_cnn_computer_vision_part*.md (by ID);
answers from _answers/computer_vision/answers_*.md, where each answer starts with '### <ID>'.
Answer markdown subset: paragraphs, '- ' bullets (two-space indent = nested), '1. ' numbered items,
**bold**, `code`, and '|' tables.
"""
import glob, os, re, sys
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT, OUT = sys.argv[1], sys.argv[2]
F = "C:/Windows/Fonts/"
pdfmetrics.registerFont(TTFont("Body", F + "segoeui.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", F + "segoeuib.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", F + "segoeuii.ttf"))
pdfmetrics.registerFont(TTFont("Body-BoldItalic", F + "segoeuiz.ttf"))
pdfmetrics.registerFont(TTFont("Math", F + "cambria.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("Mono", F + "consola.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic", boldItalic="Body-BoldItalic")
FALLBACK = set("∇∗∝∪⋆⌊⌋")  # glyphs Segoe UI lacks; rendered with Cambria

INK, ACCENT, MUTED, RULE = colors.HexColor("#1f2933"), colors.HexColor("#1d4ed8"), colors.HexColor("#52606d"), colors.HexColor("#cbd2d9")
S = {
    "title": ParagraphStyle("title", fontName="Body-Bold", fontSize=26, leading=32, textColor=INK, alignment=TA_CENTER),
    "subtitle": ParagraphStyle("subtitle", fontName="Body", fontSize=12, leading=17, textColor=MUTED, alignment=TA_CENTER),
    "h1": ParagraphStyle("h1", fontName="Body-Bold", fontSize=16, leading=21, textColor=ACCENT, spaceBefore=4, spaceAfter=8),
    "q": ParagraphStyle("q", fontName="Body-Bold", fontSize=10.5, leading=14.5, textColor=INK, spaceBefore=10, spaceAfter=4),
    "p": ParagraphStyle("p", fontName="Body", fontSize=9.5, leading=13.8, textColor=INK, spaceAfter=3),
    "li": ParagraphStyle("li", fontName="Body", fontSize=9.5, leading=13.8, textColor=INK, leftIndent=14, bulletIndent=4, bulletFontName="Body", spaceAfter=1.5),
    "li2": ParagraphStyle("li2", fontName="Body", fontSize=9.5, leading=13.8, textColor=INK, leftIndent=28, bulletIndent=18, bulletFontName="Body", spaceAfter=1.5),
    "cell": ParagraphStyle("cell", fontName="Body", fontSize=8.5, leading=11.5, textColor=INK),
    "toctitle": ParagraphStyle("toctitle", fontName="Body-Bold", fontSize=16, leading=21, textColor=ACCENT, spaceAfter=8),
    "toc1": ParagraphStyle("toc1", fontName="Body", fontSize=10.5, leading=16, textColor=INK, leftIndent=6),
    "small": ParagraphStyle("small", fontName="Body", fontSize=9, leading=13, textColor=MUTED),
}


def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r'<font name="Mono">\1</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return "".join(f'<font name="Math">{c}</font>' if c in FALLBACK else c for c in t)


# questions and sections, in corpus order
qs, order = {}, []
for f in sorted(glob.glob(os.path.join(ROOT, "02_deep_learning", "03_cnn_computer_vision_part*.md"))):
    sec = None
    for ln in open(f, encoding="utf-8"):
        if ln.startswith("## "):
            sec = ln[3:].strip()
        m = re.match(r"^- \[(DL03-\d{3})\] (.+)$", ln.rstrip("\n"))
        if m:
            qs[m.group(1)] = (sec, m.group(2))
            order.append(m.group(1))

answers, cur = {}, None
for f in sorted(glob.glob(os.path.join(ROOT, "_answers", "computer_vision", "answers_*.md"))):
    for ln in open(f, encoding="utf-8"):
        m = re.match(r"^### (DL03-\d{3})\s*$", ln)
        if m:
            cur = m.group(1)
            answers[cur] = []
        elif cur:
            answers[cur].append(ln.rstrip("\n"))
missing = [q for q in order if q not in answers]
if missing:
    sys.exit(f"missing answers: {missing}")


def render_answer(lines):
    out, para, table = [], [], []

    def flush_para():
        if para:
            out.append(Paragraph(inline(" ".join(para)), S["p"]))
            para.clear()

    def flush_table():
        if not table:
            return
        rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in table]
        rows = [r for r in rows if not all(set(c) <= set("-: ") for c in r)]  # drop |---| separator rows
        data = [[Paragraph(inline(c), S["cell"]) for c in r] for r in rows]
        t = Table(data, repeatRows=1, hAlign="LEFT", colWidths=[(A4[0] - 40 * mm) / len(rows[0])] * len(rows[0]))
        t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, RULE), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eef2ff")),
                               ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
        out.append(Spacer(1, 3))
        out.append(t)
        out.append(Spacer(1, 3))
        table.clear()

    for ln in lines:
        s = ln.strip()
        if s.startswith("|"):
            flush_para()
            table.append(s)
            continue
        flush_table()
        if not s:
            flush_para()
            continue
        m_b = re.match(r"^(\s*)- (.+)$", ln)
        m_n = re.match(r"^(\s*)(\d+)\. (.+)$", ln)
        if m_b or m_n:
            flush_para()
            ind = len((m_b or m_n).group(1))
            style = S["li2"] if ind >= 2 else S["li"]
            if m_b:
                out.append(Paragraph(inline(m_b.group(2)), style, bulletText="•" if ind < 2 else "–"))
            else:
                out.append(Paragraph(inline(m_n.group(3)), style, bulletText=f"{m_n.group(2)}."))
        elif ln.startswith("  ") and out and not para:
            # continuation paragraph inside a list item
            out.append(Paragraph(inline(s), S["li2"]))
        else:
            para.append(s)
    flush_para()
    flush_table()
    return out


class Doc(BaseDocTemplate):
    def afterFlowable(self, fl):
        if isinstance(fl, Paragraph) and fl.style.name == "h1":
            key = "sec-" + re.sub(r"\W+", "-", fl.getPlainText()).lower()  # stable across multiBuild passes
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(fl.getPlainText(), key, level=0)
            self.notify("TOCEntry", (0, fl.getPlainText(), self.page, key))


def on_page(c, d):
    c.saveState()
    c.setFont("Body", 8)
    c.setFillColor(MUTED)
    c.drawString(20 * mm, 12 * mm, "Computer Vision interview questions and answers")
    c.drawRightString(A4[0] - 20 * mm, 12 * mm, str(d.page))
    c.setStrokeColor(RULE)
    c.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)
    c.restoreState()


doc = Doc(OUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=20 * mm,
          title="Computer Vision Interview Q&A", author="ITW_QUES", subject="DL03 questions with answers")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])

story = [Spacer(1, 60 * mm), Paragraph("Computer Vision", S["title"]), Spacer(1, 4 * mm),
         Paragraph("Interview questions with answers", S["subtitle"]), Spacer(1, 10 * mm),
         Paragraph(f"{len(order)} questions (DL03-001 to DL03-{len(order):03d}) from the ITW_QUES corpus, "
                   "grouped by topic. Question IDs match the RAG files in 02_deep_learning.", S["subtitle"]),
         PageBreak(), Paragraph("Contents", S["toctitle"])]
toc = TableOfContents()
toc.levelStyles = [S["toc1"]]
story += [toc, PageBreak()]

prev_sec = None
for qid in order:
    sec, qtext = qs[qid]
    if sec != prev_sec:
        if prev_sec is not None:
            story.append(Spacer(1, 6))
        story.append(Paragraph(inline(sec), S["h1"]))
        prev_sec = sec
    body = render_answer(answers[qid])
    head = Paragraph(f'<font color="#1d4ed8">{qid}</font>&nbsp;&nbsp;{inline(qtext)}', S["q"])
    story.append(KeepTogether([head] + body[:2]))
    story += body[2:]

doc.multiBuild(story)
print("written", OUT, "questions", len(order))

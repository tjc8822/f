#!/usr/bin/env python3
"""Build a Chinese-language Markdown report into a PDF using ReportLab.

Spec:
  - WQY Zen Hei TTC (falls back to WQY Micro Hei TTC if Zen Hei not present)
  - wordWrap='CJK', TA_LEFT
  - Teal #01696F headings
  - Bullet character: U+25B6 (BLACK RIGHT-POINTING TRIANGLE) — never the dot
  - Hyperlinks underlined in teal
"""

import os
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    PageBreak,
)

# ----------------------------------------------------------------------------
# Font setup
# ----------------------------------------------------------------------------
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
]

CN_FONT = "WQY"
font_path = next((p for p in FONT_CANDIDATES if os.path.exists(p)), None)
if font_path is None:
    sys.exit(f"No CJK font found. Looked for: {FONT_CANDIDATES}")
pdfmetrics.registerFont(TTFont(CN_FONT, font_path, subfontIndex=0))

TEAL = colors.HexColor("#01696F")
DARK_TEXT = colors.HexColor("#1a1a1a")
MUTED = colors.HexColor("#444444")

# Bullet glyph the spec requires
BULLET = "\u25B6"  # ▶


# ----------------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------------
base_styles = getSampleStyleSheet()


def make_style(name, **kw):
    defaults = dict(
        fontName=CN_FONT,
        fontSize=10.5,
        leading=16,
        textColor=DARK_TEXT,
        alignment=TA_LEFT,
        wordWrap="CJK",
        spaceBefore=0,
        spaceAfter=4,
    )
    defaults.update(kw)
    return ParagraphStyle(name=name, **defaults)


STYLE_TITLE = make_style("Title", fontSize=20, leading=28, textColor=TEAL,
                         spaceBefore=4, spaceAfter=12)
STYLE_H1 = make_style("H1", fontSize=16, leading=22, textColor=TEAL,
                      spaceBefore=14, spaceAfter=8)
STYLE_H2 = make_style("H2", fontSize=13.5, leading=20, textColor=TEAL,
                      spaceBefore=10, spaceAfter=6)
STYLE_H3 = make_style("H3", fontSize=12, leading=18, textColor=TEAL,
                      spaceBefore=8, spaceAfter=4)
STYLE_BODY = make_style("Body", fontSize=10.5, leading=16,
                        spaceAfter=4)
STYLE_BULLET = make_style("Bullet", fontSize=10.5, leading=16,
                          leftIndent=14, firstLineIndent=-14,
                          spaceAfter=3)
STYLE_HEADER_META = make_style("Meta", fontSize=10, leading=14,
                               textColor=MUTED, spaceAfter=2)
STYLE_QUOTE = make_style("Quote", fontSize=10, leading=15,
                         textColor=MUTED, leftIndent=14, spaceAfter=6)


# ----------------------------------------------------------------------------
# Markdown -> ReportLab inline conversion
# ----------------------------------------------------------------------------
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITAL_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
CODE_RE = re.compile(r"`([^`]+)`")


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_inline(text: str) -> str:
    """Convert markdown inline syntax to ReportLab mini-html."""
    parts = []
    pos = 0
    for m in LINK_RE.finditer(text):
        parts.append(escape_xml(text[pos : m.start()]))
        label = escape_xml(m.group(1))
        href = m.group(2).strip()
        parts.append(
            f'<link href="{href}" color="#01696F">'
            f'<u>{label}</u></link>'
        )
        pos = m.end()
    parts.append(escape_xml(text[pos:]))
    out = "".join(parts)
    out = BOLD_RE.sub(r"<b>\1</b>", out)
    out = ITAL_RE.sub(r"<i>\1</i>", out)
    out = CODE_RE.sub(r"<font face='Courier'>\1</font>", out)
    return out


# ----------------------------------------------------------------------------
# Document builder
# ----------------------------------------------------------------------------
def build_pdf(md_path: Path, pdf_path: Path) -> None:
    src = md_path.read_text(encoding="utf-8")
    lines = src.splitlines()

    story = []
    skip_blank = False

    def add_para(text, style):
        if not text.strip():
            return
        # Replace any stray ● with ▶ defensively.
        text = text.replace("\u25CF", BULLET).replace("●", BULLET)
        story.append(Paragraph(text, style))

    in_blockquote = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            if not skip_blank:
                story.append(Spacer(1, 4))
            skip_blank = True
            i += 1
            continue
        skip_blank = False

        if stripped.startswith("---"):
            # horizontal rule
            story.append(Spacer(1, 6))
            story.append(
                Paragraph(
                    '<para backColor="#01696F" textColor="#01696F">_</para>',
                    make_style("hr", fontSize=1, leading=1, spaceBefore=0,
                               spaceAfter=4),
                )
            )
            story.append(Spacer(1, 4))
            i += 1
            continue

        # Headings
        if stripped.startswith("# "):
            content = stripped[2:].strip()
            if "本周全球及中国一级市场科技重磅事件周报" in content and not story:
                add_para(render_inline(content), STYLE_TITLE)
            else:
                add_para(render_inline(content), STYLE_H1)
            i += 1
            continue
        if stripped.startswith("## "):
            add_para(render_inline(stripped[3:].strip()), STYLE_H2)
            i += 1
            continue
        if stripped.startswith("### "):
            add_para(render_inline(stripped[4:].strip()), STYLE_H3)
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            content = stripped.lstrip(">").strip()
            add_para(render_inline(content), STYLE_QUOTE)
            i += 1
            continue

        # Bullets — recognize ▶ already in source, or "- "/"* " variants.
        bullet_match = None
        if stripped.startswith("▶"):
            bullet_match = stripped[1:].strip()
        elif stripped.startswith("- ") or stripped.startswith("* "):
            bullet_match = stripped[2:].strip()

        if bullet_match is not None:
            add_para(
                f'<font color="#01696F">{BULLET}</font>&nbsp;'
                + render_inline(bullet_match),
                STYLE_BULLET,
            )
            i += 1
            continue

        # Default body
        add_para(render_inline(stripped), STYLE_BODY)
        i += 1

    # ---- Build doc ----
    doc = BaseDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="本周全球及中国一级市场科技重磅事件周报",
        author="Weekly Tech/VC Intelligence",
    )

    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="normal",
    )

    def _page_footer(canvas, doc_):
        canvas.saveState()
        canvas.setFont(CN_FONT, 8)
        canvas.setFillColor(MUTED)
        canvas.drawCentredString(
            A4[0] / 2, 1 * cm,
            f"一级市场周报 v4 · 第 {doc_.page} 页",
        )
        canvas.restoreState()

    doc.addPageTemplates(
        PageTemplate(id="default", frames=[frame], onPage=_page_footer)
    )
    doc.build(story)


def main() -> None:
    if len(sys.argv) >= 3:
        md_path = Path(sys.argv[1])
        pdf_path = Path(sys.argv[2])
    else:
        md_path = Path("Weekly_Tech_VC_Report_2026-05-09.md")
        pdf_path = Path("Weekly_Tech_VC_Report_2026-05-09.pdf")

    if not md_path.exists():
        sys.exit(f"Source markdown not found: {md_path}")

    build_pdf(md_path, pdf_path)
    print(f"Wrote {pdf_path} ({pdf_path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()

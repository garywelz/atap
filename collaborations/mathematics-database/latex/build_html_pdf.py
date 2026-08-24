"""Build latex/paper.pdf from proof-graphs.md using local mmdc + Chrome.

Used when pandoc/pdflatex are not installed. Output path matches the
journal pipeline so the file can be deposited to Zenodo.
"""

from __future__ import annotations

import html
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "proof-graphs.md"
ZENODO = ROOT.parent / "zenodo_build"
MMDC = ROOT / "node_modules" / ".bin" / ("mmdc.cmd" if os.name == "nt" else "mmdc")
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
PUPPETEER = ZENODO / "puppeteer.json"
MERMAID_CONFIG = ZENODO / "mermaid-config.json"
MERMAID_CSS = ZENODO / "mermaid-figures.css"


def run_mmdc() -> Path:
    if not MMDC.exists():
        raise SystemExit(f"mmdc not found at {MMDC}; run npm install in latex/")
    paper_md = ROOT / "paper.md"
    paper_md.write_text(SOURCE.read_text(encoding="utf-8"), encoding="utf-8")
    out_md = ROOT / "paper-fig.md"
    env = os.environ.copy()
    env["PUPPETEER_EXECUTABLE_PATH"] = str(CHROME)
    cmd = [
        str(MMDC),
        "-i",
        str(paper_md),
        "-o",
        str(out_md),
        "-e",
        "png",
        "-b",
        "white",
        "-p",
        str(PUPPETEER),
        "-c",
        str(MERMAID_CONFIG),
        "-C",
        str(MERMAID_CSS),
        "-s",
        "2",
        "-w",
        "1400",
        "-f",
    ]
    print("==> Render Mermaid figures")
    subprocess.run(cmd, check=True, cwd=ROOT, env=env)
    figures = ROOT / "figures"
    figures.mkdir(exist_ok=True)
    for png in ROOT.glob("paper-fig-*.png"):
        num = png.name[len("paper-fig-") : -len(".png")]
        dest = figures / f"fig{num}.png"
        dest.write_bytes(png.read_bytes())
        png.unlink()
    return out_md


def inline_format(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[\^([^\]]+)\]", r'<sup class="fn"><a href="#fn-\1">\1</a></sup>', text)
    return text


def md_to_html(text: str) -> str:
    text = re.sub(
        r"!\[diagram\]\(\./paper-fig-(\d+)\.png\)",
        r'<p class="figure"><img src="figures/fig\1.png" alt="Figure \1"></p>',
        text,
    )
    text = re.sub(
        r"!\[([^\]]*)\]\(figures/fig(\d+)\.(?:png|pdf)\)",
        r'<p class="figure"><img src="figures/fig\2.png" alt="\1"></p>',
        text,
    )
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    in_table = False
    table_rows: list[str] = []
    in_code = False
    code_lines: list[str] = []
    in_ul = False

    def close_lists() -> None:
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not table_rows:
            return
        out.append("<table>")
        for idx, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if idx == 1 and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
                continue
            tag = "th" if idx == 0 else "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline_format(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("</table>")
        table_rows = []
        in_table = False

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            close_lists()
            flush_table()
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        if line.startswith("|"):
            close_lists()
            in_table = True
            table_rows.append(line)
            i += 1
            continue
        if in_table:
            flush_table()
        if re.match(r"^#{1,6} ", line):
            close_lists()
            hashes, title = line.split(" ", 1)
            level = min(len(hashes), 6)
            out.append(f"<h{level}>{inline_format(title)}</h{level}>")
            i += 1
            continue
        if line.strip() == "---":
            close_lists()
            out.append("<hr>")
            i += 1
            continue
        if re.match(r"^[-*] ", line):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_format(line[2:])}</li>")
            i += 1
            continue
        close_lists()
        if not line.strip():
            i += 1
            continue
        out.append(f"<p>{inline_format(line)}</p>")
        i += 1

    close_lists()
    flush_table()
    return "\n".join(out)


def write_html(body: str) -> Path:
    html_path = ROOT / "paper.html"
    html_path.write_text(
        f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Proof Graphs</title>
<style>
  @page {{ size: letter; margin: 18mm; }}
  body {{
    font-family: "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
    font-size: 11pt;
    line-height: 1.35;
    color: #111;
    max-width: 180mm;
    margin: 0 auto;
  }}
  h1 {{ font-size: 18pt; line-height: 1.25; margin: 0 0 12pt; }}
  h2 {{ font-size: 14pt; margin: 18pt 0 8pt; }}
  h3 {{ font-size: 12pt; margin: 14pt 0 6pt; }}
  p {{ margin: 0 0 8pt; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 10pt 0; }}
  th, td {{ border: 1px solid #444; padding: 3px 6px; text-align: left; }}
  th {{ background: #f3f3f3; }}
  code, pre {{ font-family: Consolas, "Courier New", monospace; font-size: 9pt; }}
  pre {{ background: #f7f7f7; padding: 8px; overflow: hidden; }}
  img {{ max-width: 100%; height: auto; }}
  .figure {{ text-align: center; margin: 12pt 0; }}
  a {{ color: #114; }}
</style>
</head>
<body>
{body}
</body>
</html>
""",
        encoding="utf-8",
    )
    return html_path


def chrome_pdf(html_path: Path) -> Path:
    pdf_path = ROOT / "paper.pdf"
    if pdf_path.exists():
        pdf_path.unlink()
    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--print-to-pdf-no-header",
        html_path.resolve().as_uri(),
    ]
    print("==> Chrome print-to-pdf")
    subprocess.run(cmd, check=True)
    if not pdf_path.exists():
        raise SystemExit("Chrome did not write paper.pdf")
    print(f"==> Done: {pdf_path} ({pdf_path.stat().st_size} bytes)")
    return pdf_path


def main() -> None:
    fig_md = run_mmdc()
    print("==> Convert markdown to HTML")
    body = md_to_html(fig_md.read_text(encoding="utf-8"))
    html_path = write_html(body)
    chrome_pdf(html_path)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.exit(exc.returncode)

"""Convert a research Markdown file into a standalone, printable HTML page in NEXUS brand style.

Usage: python md_to_html.py <input.md> [output.html]
"""
import os
import sys

import markdown

CSS = """
body{margin:0;background:#fff;color:#000;font-family:'General Sans','Segoe UI',Arial,sans-serif;font-size:16px;line-height:1.6}
main{max-width:1100px;margin:0 auto;padding:40px 24px 80px}
h1,h2,h3{font-family:'Neutral Face','Arial Black',Arial,sans-serif;line-height:1.15}
h1{font-size:2.4rem;text-transform:uppercase;border-bottom:6px solid #DFFF13;padding-bottom:12px}
h2{font-size:1.6rem;margin-top:56px;padding:10px 14px;background:#000;color:#fff}
h3{font-size:1.2rem;margin-top:32px;border-left:6px solid #DFFF13;padding-left:10px}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:14px}
th{background:#000;color:#fff;text-align:left}
th,td{border:1px solid #D1D1D1;padding:8px;vertical-align:top}
tr:nth-child(even) td{background:#f6f6f6}
code{background:#f1f1f1;padding:1px 4px;border-radius:3px;font-size:13px}
pre{background:#111;color:#eee;padding:14px;overflow:auto;border-radius:4px}
pre code{background:none;color:inherit}
blockquote{margin:16px 0;padding:12px 16px;background:#f6f6f6;border-left:6px solid #DFFF13}
hr{border:0;border-top:1px solid #D1D1D1;margin:40px 0}
@media print{h2{break-before:page}table,pre{break-inside:avoid}}
"""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".html"
    with open(src, encoding="utf-8") as f:
        text = f.read()
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "toc"])
    title = next((l.lstrip("# ").strip() for l in text.splitlines() if l.startswith("# ")), "NEXUS")
    html = (
        f'<!doctype html>\n<html lang="en-GB"><head><meta charset="utf-8">'
        f'<meta name="viewport" content="width=device-width, initial-scale=1">'
        f"<title>{title}</title><style>{CSS}</style></head><body><main>{body}</main></body></html>"
    )
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {out} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()

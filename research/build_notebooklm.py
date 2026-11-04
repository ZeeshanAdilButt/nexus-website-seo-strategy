"""Combine the NEXUS research documents into one source file for NotebookLM.

NotebookLM works best with a single, well-headed text source, so this joins
Mark's facts (07) and 01-04 in reading order with a short orientation header.

Usage: python build_notebooklm.py
Output: research/NEXUS-NotebookLM-Source.md
"""
import os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCES = [
    ("07-NEXUS-Mark-Facts.md", "Mark's facts: the client's decisions and rules (source of truth)"),
    ("04-NEXUS-SEO-Guide.md", "The NEXUS SEO Guide (business, audit, strategy, tools, other systems)"),
    ("01-NEXUS-Research-Findings.md", "Research findings and fact base"),
    ("02-NEXUS-Website-SEO-Strategy-Plan.md", "Website and SEO strategy plan"),
    ("03-Client-Pack-What-To-Send.md", "Client pack: message, questions and access list"),
]
OUT = os.path.join(HERE, "NEXUS-NotebookLM-Source.md")

HEADER = f"""# NEXUS: Complete Website, SEO and Tools Knowledge Base

Compiled {date.today():%d %B %Y} for NotebookLM. This single file contains five documents about NEXUS Creative HQ Ltd
(company no. 12667243), a London company that helps technology businesses land, grow and scale in the UK, with China
as its flagship corridor. It covers: what the business does and sells, its audiences, the current website audit,
how AI assistants describe NEXUS today, the SEO/AEO/GEO strategy, each SEO tool explained, NEXUS's other tools
(Ticket Tailor, Intercom "Ask Fin", Mailchimp, Ghost, Typeform, Zoho, Nexudus, email and DNS), open questions
for the client, and the launch plan for 12 November 2026 ahead of the Global Innovator Awards on 16 November 2026.

Status labels used throughout: Verified = checked against a primary source; Client-stated = from client documents;
Conflict = sources disagree; Gap or To confirm = not yet known.

Contents:
""" + "\n".join(f"{i + 1}. {title}" for i, (_, title) in enumerate(SOURCES)) + "\n"


def main():
    parts = [HEADER]
    for i, (name, title) in enumerate(SOURCES, start=1):
        with open(os.path.join(HERE, name), encoding="utf-8") as f:
            body = f.read().strip()
        parts.append(f"\n\n---\n\n# DOCUMENT {i}: {title}\n\n_Source file: {name}_\n\n{body}\n")
    text = "".join(parts)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {OUT} ({len(text):,} chars, {text.count(chr(10)):,} lines)")


if __name__ == "__main__":
    main()

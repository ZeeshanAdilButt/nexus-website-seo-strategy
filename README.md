# NEXUS website, SEO and AI-search strategy

Research and planning for the rebuild of [nexuscreativehq.com](https://nexuscreativehq.com). NEXUS helps technology businesses land, grow and scale in the UK, with China as its flagship corridor. Launch target: Thursday 12 November 2026, before the Global Innovator Awards on Monday 16 November 2026.

## Start here

| Document | What it is |
|---|---|
| [`research/04-NEXUS-SEO-Guide.md`](research/04-NEXUS-SEO-Guide.md) | The main guide: the business explained, site audit, SEO/AEO/GEO strategy, each tool explained, playbooks, and NEXUS's other systems |
| [`research/02-NEXUS-Website-SEO-Strategy-Plan.md`](research/02-NEXUS-Website-SEO-Strategy-Plan.md) | Strategy plan: goals, positioning, audiences, keyword map, KPIs, timeline |
| [`research/01-NEXUS-Research-Findings.md`](research/01-NEXUS-Research-Findings.md) | Fact base, with each fact marked verified, client-stated, conflicting or missing |
| [`research/03-Client-Pack-What-To-Send.md`](research/03-Client-Pack-What-To-Send.md) | Message, questions and access list for the client |
| [`research/05-Claude-Design-Prompt-Pack.md`](research/05-Claude-Design-Prompt-Pack.md) | Prompts for designing pages and the deck in Claude Design |
| [`research/NEXUS-NotebookLM-Source.md`](research/NEXUS-NotebookLM-Source.md) | All four documents in one file, for NotebookLM |

Each document also has an `.html` copy styled in the NEXUS brand; download and open it in a browser, or print it to PDF.

## What else is here

- `NEXUS Website Brief Developer.docx`, `NEXUS Website Tool Guide.pdf`, `questions.txt`, `seo finding.txt`, `undersatding of seo resource.docx`, `seo lady draft.html`: the original client and team inputs.
- `NEXUS Brand Assets/`, `Partner Logos/` (and their `.zip` files): brand and partner logo files.
- `research/live-site/`, `research/olostep-pages/`, `research/raw/`: crawl of the current site and saved research answers.
- `research/local-docs/`: plain-text copies of the brief, case studies and prototype pages.

## Scripts (Python 3)

- `research/olostep.py`: Olostep API helper (`map`, `scrape`, `answer`). Reads `OLOSTEP_API_KEY` from your environment; no key is stored in this repo.
- `research/md_to_html.py <file.md>`: makes a branded HTML copy of a document.
- `research/build_notebooklm.py`: rebuilds the combined NotebookLM file.

Research compiled 31 October 2026. Partner names, logos, statistics and case studies are subject to NEXUS's approval before any public use on the website.

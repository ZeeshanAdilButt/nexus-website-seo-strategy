# NEXUS website: start here

Updated 5 November 2026.

## Where we are
- **The job.** Rebuild [nexuscreativehq.com](https://nexuscreativehq.com) to Mark's Developer Brief. NEXUS helps technology businesses land, grow and scale in the UK, with China as its flagship corridor. The target is to go live on Thursday 12 November 2026, before the Global Innovator Awards on Monday 16 November.
- **The facts.** Mark's documents are the facts. Everything he has stated is in [07 Mark's facts](knowledge-base/07-NEXUS-Mark-Facts.md). Where anything else differs, Mark's version is what we build, and the difference goes to him as a question.
- **Our response.** The proposal and design options are dated 5 November. They are kept on this computer only (see "Kept local" below), with a check against Mark's brief beside them.
- **The build.** Hasaan's 24-page brand build is the current site, on an unlisted review link. Our Claude Design canvas holds the v3.1 pages. Both are covered in [design/README.md](design/README.md).

## The folder

| Folder | What's in it |
|---|---|
| `emails-and-meetings/` | **Everything exchanged with NEXUS, in date order.** Each name starts with its date. Mark's brief and assets are here |
| `knowledge-base/` | **What we know.** Mark's facts, our research findings, the SEO specialist's inputs, the crawl of the current site, saved research answers |
| `plan/` | **What we propose and how we'd do it.** Strategy, the SEO guide, the design plan and prompts, the tool guide |
| `design/` | Hasaan's site code, the Claude Design canvas source, design critiques and screenshots |
| `scripts/` | Python helpers: HTML copies, the NotebookLM file, Olostep research, the site crawl |
| `_archive/` | Superseded drafts and duplicate files, kept for the record |

Each Markdown document also has an `.html` copy in the NEXUS style. Open it in a browser, or print it to PDF.

## Timeline: emails and meetings

| Date | File | What happened |
|---|---|---|
| 25 Oct 2026 | [2026-10-31-mark-brief-and-assets/](emails-and-meetings/2026-10-31-mark-brief-and-assets/) | Mark saves the Developer Brief (date from the Word file) |
| 31 Oct 2026 | the same folder | We have the brief, his prototype copy, the case studies, the Brand Guidelines 2025, the brand assets and the partner logos. `text-copies/` has plain-text versions |
| 31 Oct 2026 | [2026-10-31-questions-for-mark.txt](emails-and-meetings/2026-10-31-questions-for-mark.txt) | Our six SEO questions for Mark |
| 31 Oct 2026 | [2026-10-31-03-Client-Pack-What-To-Send.md](emails-and-meetings/2026-10-31-03-Client-Pack-What-To-Send.md) | Message, questions and access list for NEXUS |
| 5 Nov 2026 | `2026-11-05-proposal/` (kept local) | Our proposal and design options, plus `00-check-against-mark.md` |

The 31 October dates come from file dates. Correct them if the real dates differ.

## Knowledge base: what we know

| File | What it gives you |
|---|---|
| [07-NEXUS-Mark-Facts.md](knowledge-base/07-NEXUS-Mark-Facts.md) | **Read first.** Mark's brief, prototype, case studies and guidelines, fact by fact, covering every section of the brief: decisions, sitemap, page specs, offers, proof, brand, forms, search, technical targets, phases (including what the Phase 0 proposal must contain), components, acceptance tests, handover. It also lists what Mark still has to confirm (§13), conflicts inside his own documents (§14), and where our work goes beyond him (§15) |
| [01-NEXUS-Research-Findings.md](knowledge-base/01-NEXUS-Research-Findings.md) | Our fact base from public sources and the crawl. Each fact is marked verified, client-stated, conflicting or missing |
| [NEXUS-NotebookLM-Source.md](knowledge-base/NEXUS-NotebookLM-Source.md) | 07, 04, 01, 02 and 03 in one file, for NotebookLM |
| `seo-specialist/` | The SEO specialist's audit (`seo finding.txt`), business-understanding doc and homepage draft |
| `current-site/` | Our crawl of the live site: page inventory, image status, external links, robots.txt, sitemap, saved pages |
| `research-answers/` | Saved Olostep answers (AI visibility, competitors, keywords, market) and the site map |

## Plan: what we propose

| File | What it gives you |
|---|---|
| [04-NEXUS-SEO-Guide.md](plan/04-NEXUS-SEO-Guide.md) | The main guide: the business, site audit, SEO, AEO and GEO strategy, every tool explained, playbooks, NEXUS's other systems |
| [02-NEXUS-Website-SEO-Strategy-Plan.md](plan/02-NEXUS-Website-SEO-Strategy-Plan.md) | Goals, positioning, audiences, keyword map, KPIs, timeline |
| [06-NEXUS-Landing-Page-Design-Plan.md](plan/06-NEXUS-Landing-Page-Design-Plan.md) | Which pages to design first, the design direction, considerations, business case |
| [05-Claude-Design-Prompt-Pack.md](plan/05-Claude-Design-Prompt-Pack.md) | Prompts for designing pages in Claude Design |
| `NEXUS Website Tool Guide.pdf` | The ten free tools we recommend, what each costs and when it comes in |

## Read in this order
1. [07 Mark's facts](knowledge-base/07-NEXUS-Mark-Facts.md)
2. [design/README.md](design/README.md), then the live review site
3. The 5 November proposal and its check (local)
4. [04 SEO guide](plan/04-NEXUS-SEO-Guide.md)
5. [02 strategy plan](plan/02-NEXUS-Website-SEO-Strategy-Plan.md)
6. [01 research findings](knowledge-base/01-NEXUS-Research-Findings.md)

The numbers in file names (01 to 08) are the IDs the documents use to point at each other, for example "07 §14". `03` lives in `emails-and-meetings/` and `08` in `_archive/`.

## Kept local (not on GitHub)

This repository is **public**. These folders are listed in `.gitignore` and stay on this computer:
- `emails-and-meetings/2026-11-05-proposal/`: our proposal, design options and the check
- `reference docs/`: the GIA project's questions, brief, quote, invoices and support summary
- `responses/`: drafts in progress

Mark's case study document is marked "Private & Confidential", and its text is in `emails-and-meetings/2026-10-31-mark-brief-and-assets/text-copies/`. Decide whether the repository should be private.

## Rules when working on NEXUS
- Mark's documents win. Use his prototype copy word for word, and mark anything missing as `[Placeholder: …]`.
- Never write substitute claims, statistics, testimonials, prices, emails, addresses or response times.
- No case study mentions visa or endorsement status. The UKES role stays on its own page, with no sales action.
- Name the Alibaba Entrepreneurs Fund and the Swiss Bluefaer Innovation Centre as text only, and show partner logos only once each partner confirms in writing.
- Our ideas go to Mark as decisions with a default. Never build them in as if they were agreed.
- Every sentence needs a reason. No filler and no AI phrasing.

## Scripts (Python 3)
- `scripts/md_to_html.py <file.md>`: makes the styled HTML copy of a document.
- `scripts/build_notebooklm.py`: rebuilds `knowledge-base/NEXUS-NotebookLM-Source.md`.
- `scripts/olostep.py`: the Olostep helper (`map`, `scrape`, `answer`). It reads `OLOSTEP_API_KEY` from your environment, and saves to `knowledge-base/research-answers/`.
- `scripts/crawl_public.py`: re-crawls the live site into `knowledge-base/current-site/`.

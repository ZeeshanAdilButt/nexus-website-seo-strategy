---
name: website-intake-and-facts
description: Starts a website project. Asks the intake questions, sets up the workspace, and turns the owner's documents into a fact-by-fact facts doc with conflicts flagged. Use at the start of any client or personal website project.
---

You start website projects. Your job is to find out what's true before anyone designs, writes or builds anything.

## 1. Ask the intake questions

Ask only what you can't find in the files, in one short message, grouped. Suggest a default for each.

**The project**
- Is this for a client or for the user's own site? Who owns the accounts (client-owned, or the user's personal accounts)?
- What is the site for, and what action counts as success (an enquiry, a sale, a sign-up, a booking)?
- Is there a deadline, or an event it must go live before?

**What already exists**
- What documents exist: a brief, a prototype, brand guidelines, case studies, copy, photos? Where are they?
- Is there a design already? It could be a Claude Design canvas, Figma, a designer's site, or a prototype. Get the link.
- Has research already been done (an SEO audit, a crawl, keywords, competitors)? Where is it?
- What's the current site URL, and what platform runs it?

**Audience and data**
- Where do most visitors come from (countries or regions)? Is any target country restrictive (for example mainland China)?
- Will the site collect personal data (forms, sign-ups)? Which privacy law applies (UK GDPR, EU GDPR, US state laws, other)?

**People and running it**
- Who edits the site after launch? Can they use a GitHub login?
- Which domain is it on, and where is its DNS? Is there an email address on that domain to send or receive from?
- Is there a budget limit for monthly running costs?
- Is the project repo public or private?

## 2. Set up the workspace

```text
00-START-HERE.md       where things stand, folders, a dated timeline, reading order, rules
README.md              a short landing page pointing to 00-START-HERE.md
emails-and-meetings/   everything exchanged, in date order (YYYY-MM-DD-NN-name). The owner's originals plus text-copies/
knowledge-base/        facts doc, research, crawls, one folder per specialist (named after the person)
plan/                  numbered plan docs (01, 02, ...), which other docs cite as IDs
design/                design source, reviews, screenshots
proposals/             LOCAL ONLY (gitignored): YYYY-MM-DD/ for each send, plus not-sent/
scripts/               helpers (Markdown to HTML, crawl, research)
_archive/              superseded and duplicate files
```

- **If the repo is public,** put `proposals/`, any reference quotes and invoices, and drafts in progress in `.gitignore`.
- **Moving files:** use `git mv`, then run a link checker over every relative Markdown link.
- **Commits:** small, with real messages.

## 3. Write the facts doc

Read every document in full, including the originals:
- For Word files, read `word/document.xml`, `docProps/core.xml` (author, dates) and `word/_rels` (links), and diff them against any text copy to prove nothing is missing.
- For PDFs, extract the text and the links.

Write `knowledge-base/<NN>-<PROJECT>-Facts.md` with these sections:
1. Who they are, in their words
2. Decisions already made, with their labels (Approved, To confirm, Optional)
3. Sitemap, header, footer and navigation
4. Page specs: exact H1s, section order, copy
5. Offers and price lines
6. Proof supplied: stats, partners, case studies, team
7. What can and cannot be said
8. Brand rules
9. Forms and tracking
10. Their SEO titles and descriptions
11. Technical targets: speed, accessibility, regions, security
12. Phases, and what a first proposal must contain
13. Still to confirm
14. **Conflicts inside their own documents**
15. **Where our work goes beyond them**
16. The documents themselves: author, dates, links
17. Components
18. Acceptance tests
19. Handover

Close the doc with a pre-flight checklist for any page.

Also list every place their brief asks us to "tell us", "confirm", "give us" or "price separately". The proposal must answer each one.

## Hand over

Hand over the project profile (the answers to step 1), the workspace, the facts doc, and the conflicts to raise with the owner. Stop for the user's go-ahead.

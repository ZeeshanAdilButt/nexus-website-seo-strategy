---
name: website-proposal-and-quote
description: Writes the documents a client receives before a build. Three separate documents: the plan (proposal), the important questions only, and a lean quote in the style of the user's previous quotes, with 50% upfront. Later questions and Phase 2 pricing stay unsent. Every claim is checked against the facts doc.
---

You turn the facts, research, stack and design into documents a client can say yes to.

## Ask first

- Is there a precedent quote or proposal for this client or a similar project? Use its layout, rate, payment terms and validity.
- What is the user's hourly rate, and which discount, if any, can be offered (as a goodwill line, never argued)?
- Who is on the team, and what does each person cost? For example, a fixed fee for a senior specialist.

## What goes out, and in what order

All of it goes in `proposals/YYYY-MM-DD/`, which is gitignored if the repo is public.

1. **The message:** short, to paste into email or WhatsApp, with the review link and the design link. The client-messages agent writes it.
2. **The proposal: the plan only, no questions.**
   - Open like a person: what this is, and why it matters to them now.
   - Sections:
     - before and after (screenshots, an audit table)
     - how search and AI see them today
     - SEO and AI strategy (one search topic per page; your recommendations as their decisions, with their wording as the default)
     - page structure with links
     - design: the recommended direction, with the others "on the side"
     - how we build it: stack, editing, regions, component inventory
     - keeping their search value: redirects
     - content and the blog
     - security and support, including any confirmations they asked for
     - scope
     - timeline: "delivered by" one date, or "about N working days after your go-ahead"
3. **Questions (one page).**
   - Only what blocks the build now, each with our suggested answer.
   - Then the materials and access needed, with dates.
   - Drop any question their documents already answer, or that we can find out ourselves.
4. **The quote, in the precedent's style:**
   - scope
   - work already done (not charged)
   - why this fee, compared with the precedent
   - a fee breakdown by workstream: development, hosting and launch, testing, iterations, SEO and backlink preservation, content migration, with hours, rate and fee
   - any discount as one "goodwill discount" line
   - payment: 50% on acceptance, 50% at launch
   - timeline, terms (revisions, fixes, accounts, third-party costs, not included, validity), and the next step

**Kept in `not-sent/`:**
- later questions, each with what we do in the meantime
- Phase 2 and optional pricing, which becomes a separate quote later
- the after-launch list
- the fix list for the designer
- the source for every document
- superseded versions

## Question discipline (for the Questions document)

Before each question, run the three-question test:
1. Can we find this out ourselves later, with access?
2. Did they already answer it, in their documents or messages?
3. Does it change the scope or the estimate now?

Keep the question only if the answers are no, no and yes. Everything else is parked in `not-sent/`, labelled Proposal, Build or Discovery, with what we do in the meantime.

Also:
- In an early message, don't ask about access dates, timing or who decides.
- Don't ask how long a task takes when we'll automate it anyway.
- Never ask for "a short reply". Their input helps us head in the right direction.
- Always give our suggested answer, so a quick yes is enough.

## Closing the deal

- **Help first, sell second.** Value shown with their own data (a crawl, a speed test, a typo in their price list) beats value claimed.
- **Name what we build,** in plain words they can picture, and say plainly that it's what we'd build.
- **Be humble, never cocky.** Offer choices and let them pick, credit their work, and admit we might be missing something. Point out errors in their data gently, and only when it helps them.
- **Never cap their choices.** Ask "which areas would you like us to go deeper into?", not "pick two or three".
- **Keep every promise** from earlier messages and minutes, and say so ("as promised").
- **Before the scope is agreed,** show ideas and components, not full designs, unless the user decides a full review site is part of the pitch. Timelines and prices wait for the scope, unless the client's brief asks for a fixed quote.

## Rules

- **Propose only what they asked for.** Never cap what they asked for: if the brief says "migrate our articles", all of them are in the fee.
- **No outcome promises:** no enquiry numbers, rankings or "90-day" targets. The owner's own targets can stay, framed as targets.
- **Don't explain their business back to them,** and don't quote their brief at them.
- **Free fixes on what we build are ongoing.** New features, changes and security patching go under a retainer or a separate quote. Say so in one clear line.
- **Hosting is paid by the owner directly,** in their name. State the cost plainly (for example "about $5 a month").

## Before anything goes out

- **Check every figure programmatically:** hours sum, fees sum, discount, payment split, and each research number against its proof.
- **Scan for banned items:** em or en dashes, semicolons, "placeholder", old prices, removed limits, promises.
- **Render the PDFs.**
  - Write HTML with print CSS: A4, `@page` margin boxes for a running header and "Page X of Y", serif headings, a readable body size, quiet table headers.
  - Print with `msedge --headless=new --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf=out.pdf file:///page.html`.
  - Check thumbnails with PyMuPDF, and fix orphaned headings and near-empty pages.
- **Give the user a reading guide:** which files to send, in what order, and what to attach.

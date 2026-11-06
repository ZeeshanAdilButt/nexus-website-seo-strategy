---
name: website-research
description: Researches a current website and its market with proof for every number. Covers the crawl, SEO data, AI visibility, competitors, keywords, a fresh-visit speed test and the content audit. Use when research is missing. If research exists, check it and fill only the gaps.
---

You research where a website stands today, and you prove every number.

## First, check what already exists

- **Read any existing research:** a specialist's audit, a Screaming Frog crawl, Ahrefs or Semrush exports, earlier findings.
- **List what it covers and what it doesn't.** Redo nothing that's already proven. Re-check only numbers that have no source.
- **Credit every number to its source and date:** "Ahrefs, as supplied 27 October" or "our crawl, 6 November".

## Research checklist (fill the gaps)

1. **Crawl the current site.**
   - Build a page inventory: status codes, titles, meta descriptions, canonicals, H1s, robots, the sitemap, broken pages and images, and duplicate addresses (for example "#!" copies).
   - Record the host rule (http/https, www or not) and redirects.
   - Save it in `knowledge-base/current-site/` (inventory CSV and JSON).
2. **Authority and search.** Domain rating, referring domains, the terms it ranks for and organic visits, from the owner's or specialist's tool exports. If you have no export, ask for one rather than guessing.
3. **AI visibility.** Ask answer engines a fixed prompt set:
   - "What is <brand>?"
   - "Who runs <brand>?"
   - "Best <category> organisations for <audience> in <market>"
   - "<brand> vs <competitor>"

   Record how they describe the brand, what they get wrong, and who they name instead. Save the raw answers.
4. **Competitors and keywords.**
   - Find who the brand is compared with or loses to.
   - Test the owner's favourite phrases for real search volume. If a phrase has none, it can lead the story but not the search targets.
   - Note the phrases buyers actually type.
5. **Speed test on a fresh visit, with proof.**
   - Run headless Edge or Chrome through the DevTools protocol, with a new profile and the cache disabled, on a fast connection and on Lighthouse's slow 4G (150 ms latency, 1.6 Mbps down, 750 kbps up).
   - Record first contentful paint, LCP, the load event, request count and image count.
   - Save the script and its raw output in the proofs folder, and note where you ran it from.
   - Try PageSpeed Insights if its quota allows.
   - Never repeat a speed number that has no file behind it.
6. **Content audit.**
   - Find how the owner publishes today (a built-in blog, Ghost, WordPress, LinkedIn-style posts).
   - Count the posts and dates (check `sitemap-posts.xml` and the generator meta tag) and where they live.
   - Note duplicates, off-topic posts and missing dates.
7. **Tools in use.** Registrar and DNS host, email provider (MX, SPF, DMARC), forms, CRM, analytics, booking and ticketing, and any third-party subdomains.
8. **Restricted regions** (if relevant). Note which services on the current site are blocked there (for example Google Fonts, Maps, reCAPTCHA and YouTube in mainland China).

## Output

- **`knowledge-base/<NN>-Research-Findings.md`.** Mark each fact Verified, Owner-stated, Conflict or Gap, with its source.
- **A before-and-after audit table** that the proposal can reuse: current state against new site.
- **`proofs/README.md`:** each claim, its evidence, and the file path.

Hand over the findings, plus any numbers you could not prove (so nobody uses them).

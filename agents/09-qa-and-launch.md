---
name: website-qa-and-launch
description: Tests the staging site against the owner's acceptance criteria (layout, brand, forms, SEO, speed, accessibility, regions, security, redirects, CMS), runs the launch and builds the handover pack. Every check leaves evidence.
---

You prove the site works before it goes live, then launch it and hand it over.

## Test on staging (keep evidence for each)

| Area | Passes when | How |
|---|---|---|
| Layout | Every page follows the agreed section order and copy at 360, 768, 1280 and 1440px, with no sideways scroll | Screenshots at each width |
| Brand | Colours, logo, type and buttons follow the guidelines, and accent colours are never used as backgrounds | Review against the facts doc |
| Copy | H1s, statistics, names and case studies match what the owner approved, and placeholders are marked | Diff against the facts doc |
| Forms | Each form validates, stores the entry, sends the notification in under 5 minutes and the acknowledgement, and records its source fields. The export works, and the webhook posts to a test URL | One test submission per form |
| SEO | Unique titles and descriptions, one H1, correct canonicals, a valid sitemap, and structured data with no errors | Crawl, plus the Rich Results and Schema validators |
| Speed | LCP target met for real users (aim 500ms to 1.5s), CLS under 0.1 | Fresh-visit script with output saved, plus Lighthouse |
| Accessibility | Lighthouse 95+ on every template, no critical axe errors, full keyboard use, 200% zoom works | axe, Lighthouse, a screen reader check |
| Regions | Key pages load within the target from each priority region, including restricted countries | Third-party speed tests from those locations |
| Security | Supported versions, a clean vulnerability scan and dependency audit, headers present, 2FA on, one restore tested | Scan reports and a header check |
| Privacy | Analytics blocked until consent, a privacy link on every form, opt-ins never pre-ticked | Cookie audit |
| Redirects | Every old address returns one 301 to a live page | Crawl of the old address list |
| CMS | An owner's editor can edit a statistic, replace a placeholder, add an event and publish an article without help | A live session |

## Launch

1. Switch the domain and DNS, keeping the host rule (https, and www or not, as before).
2. Run the redirect crawl.
3. Submit the sitemap to Google Search Console and Bing, and request indexing for the key pages.
4. Watch errors, 404s and form delivery on day one.
5. For the first month, check broken links weekly and fix any defects in our work free.

## Hand over

- Credentials through a password manager, never by email. Our access reduced to the agreed level.
- An editing guide or recorded walkthrough, plus one live training session.
- Technical docs: platform, component inventory and versions, integrations, form field schema, webhook, redirect map, analytics events.
- A security summary: patch levels, scan results, the patching commitment (if a support agreement exists).
- All the test evidence and the test log, filed in the dated proposals or launch folder.

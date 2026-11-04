# Review: Hasaan Wayne's two drafts against Mark's documents

| | |
|---|---|
| Date | 4 November 2026 |
| Scope | Draft one (`Hasaanwayne/nexus-website-draft-one` at `2deb844`) and the colour redesign (`Hasaanwayne/nexus-website-draft` at `ee092d2`): Home, International companies, Institutions, Asia corridor |
| Measured against | [`research/07-NEXUS-Mark-Facts.md`](../../07-NEXUS-Mark-Facts.md) and Mark's source files in `research/local-docs/` |
| Method | Read the HTML, CSS and JS from shallow clones, plus the screenshots in this folder. No code was run. Contrast was spot-checked by hex value only (no axe or Lighthouse run). The lower parts of pages were read in the code, not seen in screenshots |
| Not in scope | Hosting, performance, the live sites' behaviour |

## Summary

Neither draft is ready to be the base of the build as it stands. The audience pages in draft one track Mark's prototype copy closely, and the colour redesign has the stronger engineering (landmarks, JSON-LD, Mark's titles on two pages). The homepages in both have moved away from Mark: a new H1, a fourth audience, case studies hidden behind placeholders the brief does not ask for, and details taken from outside Mark's documents.

**Fix first:**
1. Restore Mark's Home H1, buttons, three audiences and four statistics.
2. Use the seven case studies and the Alibaba Entrepreneurs Fund and Swiss Bluefaer names as the brief allows. Replace every detail that is not in Mark's documents with a `[Placeholder: …]`.
3. Colour redesign only: drop the paintings, the porcelain ground and the scroll motion. All three break written brand rules.
4. Add canonicals, fix the nav breakpoint to 1100px, use the 1200px content width, and use the Neutral Face Bold and General Sans files.

## Findings

P0 = contradicts an Approved rule or states something Mark has not approved. P1 = a missing or misplaced required part. P2 = a technical or polish gap.

| # | P | Draft | What it does | What Mark says |
|---|---|---|---|---|
| 1 | P0 | Both | Home H1 is "UK–China market entry." (draft one `index.html:103`, colour `index.html:65`). The second button is "For science parks and zones". Home titles differ from the brief's table | H1 "Land, grow and scale technology businesses in the UK."; buttons Find your route, Talk to our team; titles as brief §10 |
| 2 | P0 | Both | Details not in Mark's documents (listed below this table) | "Do not write substitute claims, statistics, testimonials or case studies" |
| 3 | P0 | Both | Case studies shown as "[Aerospace client]", "[Robotics client]"; Volatus as "[acquirer]"; Alibaba Entrepreneurs Fund and Swiss Bluefaer as "[… name pending approval]" | All seven case studies are Ready. Alibaba and Swiss Bluefaer are shown "by name only", with placeholder wording and no logo |
| 4 | P0 | Both | "Four ways in" adds "UK companies looking at Asia" | "Three ways in. One team behind them." |
| 5 | P0 | Colour | Public-domain and CC BY-SA paintings on every page, replacing the Tianjin signing photo | "Real NEXUS photography … No stock"; meanwhile use placeholders |
| 6 | P0 | Colour | Porcelain `#F6F7F2` section ground (`assets/css/site.css:16`); Studio Grey defined but unused | "Use no other colours"; backgrounds "black, white or Studio Grey" |
| 7 | P0 | Colour | Scroll reveals, count-up figures, an image shutter and an animated crossing graphic (`site.css:352-372`, `site.js:102-135`). Reduced motion is respected | "Hover and focus states only" |
| 8 | P1 | Both | "Supplier and security cleared" swapped for a CBBC "Member" tile; draft one shortens the stat labels | The four statistics, worded as approved |
| 9 | P1 | Both | Home lacks Partner network, the team (colour has a placeholder only), the three contact tiles (a form instead), the session series and the logo row | Brief 4.2 section order |
| 10 | P1 | Both | Asia corridor adds "Two directions" and FAQs and has no logo row. Anchors: colour uses `#request` for `#start`; draft one's Asia page uses `#start` for `#delegations` | Brief 4.4 sections; anchors `#start`, `#delegations` |
| 11 | P1 | Both | No UK scale-ups, Results, Events, Insights, About, Partner, Endorsing role, Contact or legal pages. Links fall back to home anchors | Phase 1 sitemap |
| 12 | P1 | Both | Nav omits Events and adds Results; draft one also omits Partner with NEXUS. Collapse at 640px (draft one `index.html:25`) and 1180px (colour `site.css:115`) | Seven items plus Partner with NEXUS and Talk to us; collapse below 1100px |
| 13 | P1 | Both | Draft one uses Outfit, DM Sans and DM Mono; colour uses General Sans for body but Outfit for headlines. Both self-host fonts | Neutral Face Bold headlines, General Sans body, self-hosted |
| 14 | P1 | Both | Content width 1320px (draft one) and 1440px (colour); colour section spacing 88 to 136px; draft one header buttons 46px | 1200px max, 64 to 112px between sections, buttons at least 48px |
| 15 | P2 | Both | No canonical on any page. Draft one: no JSON-LD, no Open Graph, no `<main>`, no skip link, form fields without `name`, "Mainland China" pre-selected | Self-referencing canonical; one H1, landmarks, labelled fields |
| 16 | P2 | Both | Draft one footer lacks the Explore and Contact columns, social links, Cookies and Accessibility; colour footer lacks Cookies and "About and team" | Footer columns and legal links as brief §3 |

**Details in finding 2.** Each comes from outside Mark's documents, or contradicts them:

| Detail | Where | Status |
|---|---|---|
| Registered office "Kings Parade, Lower Coombe Street, Croydon CR0 1AA" | Every footer | Matches Companies House (doc `01`), but Mark lists the registered office as To confirm and the prototype shows "[Registered office to be confirmed]" |
| "SBREC, 80 Basinghall Street" | Draft one `index.html:381`; colour `index.html:269` and JSON-LD | From the live site, not from Mark |
| GIA at "The Dorchester, London" and "Ten categories, one hundred finalists" | Draft one `index.html:303`; colour `index.html:222` | From the GIA site; Mark's prototype says "[Venue to be confirmed]" |
| Working-hours overlap "09:00–10:00 London" | Draft one `index.html:376-379`; colour `index.html:265-267` | Not in Mark's documents |
| "Figures reported by NEXUS, November 2026" | Draft one `index.html:145`; colour `index.html:116` | Not in Mark's documents |
| Three new insight titles; the report called "Our annual guide" | Home insights | Mark's prototype names three articles; the report is a placeholder |
| "Partners on the ground in … Hong Kong" | Draft one `index.html:346`; colour `index.html:248`, `international-companies.html:200` | The Hong Kong partner is in discussion; Mark says "partners on the ground in China" |
| "NEXUS runs delegations to Hong Kong" | Both Asia pages, colour FAQPage JSON-LD | 2027 delegation details are a placeholder |
| One CC BY-SA painting described as public domain | Colour `asia-corridor.html:206, 329` and the repo README | Licence claim is inaccurate |

**Already in line with Mark:**
- No case study mentions visa status. UKES is kept separate.
- Each page has one H1, with headings in order.
- Yellow is used as an accent only.
- Consent is never pre-ticked, and every input has a label.
- Every page has noindex, plus `Disallow: /` in robots.txt, as client-review copies should.

## Carry forward into the build

- Draft one's audience-page copy and structure: the challenge quote, offer cards with "on application" price lines, fit and not-fit, steps, FAQs, and forms with "What happens next".
- The UKES wording in both drafts.
- Accessible mobile menu in both: `aria-expanded`, `aria-controls`, Escape to close. Pill buttons, 3px focus rings, reduced-motion guards.
- From the colour draft:
  - skip link and `<main>`
  - BreadcrumbList, Service and FAQPage JSON-LD (minus the unconfirmed address)
  - Mark's titles and meta on Institutions and Asia corridor
  - a `marketing_consent` field
  - GIA ticket links with UTM tags
  - the `#routes`, `#about`, `#contact` and `#delegations` anchors
  - clearly highlighted placeholders
- Draft forms that state nothing has been sent, self-hosted fonts and no third-party scripts.

## Checklist for the next revision

- [ ] Home H1, eyebrow, intro and buttons are Mark's words
- [ ] Three audiences, four statistics, seven named case studies
- [ ] Alibaba Entrepreneurs Fund and Swiss Bluefaer named as text, with placeholder wording and no logo
- [ ] Every address, venue, count and time not in `07` replaced with a `[Placeholder: …]`
- [ ] No paintings, no porcelain, no scroll or load animation
- [ ] Nav: seven items, Partner with NEXUS, Talk to us; Menu below 1100px
- [ ] 1200px content width; 64 to 112px section spacing; buttons at least 48px
- [ ] Neutral Face Bold and General Sans self-hosted
- [ ] Self-referencing canonical on every page
- [ ] Anchors `#routes`, `#how`, `#start`, `#delegations`, `#about`, `#contact`

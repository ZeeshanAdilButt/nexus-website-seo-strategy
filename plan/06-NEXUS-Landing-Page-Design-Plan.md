# NEXUS: Landing page design plan (Claude Design)

> **Mark's documents win.** Where this document differs from Mark's brief or prototype copy, follow [`07-NEXUS-Mark-Facts.md`](../knowledge-base/07-NEXUS-Mark-Facts.md). Its section 15 lists our proposals that still need Mark's decision.

| | |
|---|---|
| Date | 1 November 2026 |
| Scope | Which pages to design first in Claude Design, how they should look and read, and why, for both search and the client's revenue |
| Audience | Project lead (internal); sections 3 and 4 can be shared with NEXUS |
| Builds on | `02` Strategy Plan, `04` SEO Guide, `05` Claude Design Prompt Pack, the Developer Brief §4.2 |
| Not in scope | Build platform, hosting, CMS choice, full sitemap (already approved in the brief) |

---

## 1. Executive summary

Design **two pages**, in this order: the **Homepage** as a corridor-first router, then **`/international-companies`** as the flagship SEO landing page. Every other page reuses their components.

The homepage tells Google, AI engines and visitors one thing in five seconds: NEXUS is the UK–China bridge for technology companies. The international page is where search intent and revenue meet: "UK market entry from China" has buyers, weak competitors, and leads to the paid Market-Entry Diagnostic.

**Do in order:**
1. Set up the NEXUS design system in Claude Design (prompt pack `05`, Step 1).
2. Design hero Variants A and B; run the Lyssna 5-second test; pick the winner.
3. Design the Homepage (prompt in §3.3).
4. Design `/international-companies` (prompt pack `05`, prompt B, plus the changes in §3.4).
5. Export as standalone HTML, run the checklist in §6, then **Handoff to Claude Code** for the real build.

**Your call (needs the client):** if NEXUS answers question 3 in `emails-and-meetings/2026-10-31-questions-for-mark.txt` with "institutions bring the most revenue", swap step 4 to `/institutions`. Same template, different copy.

---

## 2. The call: why these two pages

| Option | Search value | Client value | Verdict |
|---|---|---|---|
| **Homepage** | Brand + entity page; carries most of the 884 linking domains after the 301s | First impression for every partner, judge and GIA guest | **Design first** |
| **`/international-companies`** | Highest-intent cluster: "UK market entry for tech companies", "UK soft landing", "expand to UK from China" | Leads to the paid diagnostic (direct revenue) | **Design second (flagship)** |
| `/institutions` | Low search volume, high deal value | Biggest contracts, few buyers | Swap in if the client says so |
| `/asia-corridor` | Strong for AI answers ("who connects Tianjin with the UK?") | Differentiator, but not a conversion page | Phase 1, after the template exists |
| `/events` (GIA) | Short-lived spike to 16 Nov | Ticket sales already run on the GIA site | Announcement bar only |

**Reason in one line:** the site has authority (DR 34, 884 domains) but almost no relevance (2 ranking keywords). The homepage fixes relevance; the international page converts it into enquiries.

---

## 3. The design

### 3.1 Design direction ("make it stand out, stay on brand")

| Element | Direction |
|---|---|
| Base | Pitch Black dominant. White and Studio Grey sections for rhythm. **Yellow is accent only** (buttons, underlines, tags, numbers). |
| Type | Neutral Face Bold, uppercase, very large (clamp to 96px desktop / 44px mobile). General Sans body, 17px. |
| Signature visual | A **corridor line**: London on the left, Tianjin, Shanghai and Hong Kong on the right, joined by a thin yellow line. Built in SVG with real text labels, so it is crawlable and fast. This replaces a stock "globe". |
| Brand graphics | The NEXUS **X** (`NEXUS Brand Graphics/`) as a large cropped outline behind the hero and section breaks. The **scribble** marks to underline one key word per section. |
| Proof | Big-number strip (100+, 16, 1,400+). Numbers in yellow on black, labels in white. |
| Photography | Real photos only (Tianjin signing, S-Tron, GIA). Clear `[Placeholder: …]` boxes until supplied. No stock, no AI images. |
| Motion | One effect: the corridor line draws in on load. Off when `prefers-reduced-motion` is set. |
| Feel | Confident and editorial, closer to a consultancy annual report than a startup template. |

### 3.2 Hero (shared by both variants)

```text
Eyebrow : THE UK–CHINA INNOVATION CORRIDOR
H1 (A)  : LAND, GROW AND SCALE TECHNOLOGY BUSINESSES IN THE UK.
H1 (B)  : LAND, GROW AND SCALE IN THE UK. / FROM CHINA AND BEYOND.   (line 2 in yellow)
Intro   : NEXUS is the operational bridge between the UK and China for technology
          companies, science parks and innovation zones: one accountable team in
          the UK, with partners on the ground in China.
Buttons : [Find your route] yellow   [Talk to our team] outline
Visual  : corridor line + [Placeholder: Tianjin signing photograph]
```

**Build default: Variant A, Mark's H1.** Variant B is our proposal for Mark to decide: it puts "China" in the H1, which Google weights most and AI engines quote. Test both with Lyssna, then put the result to Mark.

### 3.3 Homepage: section order

Follows the brief §4.2, with three changes marked **Change**.

| # | Section | Job for search / AI | Job for the client |
|---|---|---|---|
| 1 | Announcement bar (GIA, 16 Nov) | Fresh event signal | Ticket and visibility push |
| 2 | Hero (Variant A; B only if Mark approves) | H1 + 160-character intro carry "UK–China" | Five-second clarity |
| 3 | Proof strip: 3 stats + 4 logos | Citable numbers | Trust before scrolling |
| 4 | Who we work with: three route cards + one text link "UK company going to China? →" | One internal link per audience page | Visitor self-selects. **Change:** adds the outbound route |
| 5 | **Asia corridor** (5 partner cards, Hong Kong line) | Named partners and places, which AI engines repeat | The differentiator. **Change:** moved up from #6, above "How we work" |
| 6 | How we work (5 steps) | Process answers "how does it work?" | Lowers perceived risk |
| 7 | Results (3 case study cards) | Proof for every claim | Shows outcomes, not promises |
| 8 | Events: NEXUS Sessions + GIA | Event schema | Sponsor and ticket path |
| 9 | Partner network chips | Topical terms (R&D tax, IP, banking) | Sponsor pipeline |
| 10 | Team (portraits, founder quote) | Names the CEO (AI engines currently cannot) | Human trust |
| 11 | Insights (3 cards + China 2027 report) | Freshness, internal links | Lead magnet. **Change:** replace the three old creative-tech articles with corridor content |
| 12 | Common questions (5 FAQs) | FAQPage schema, direct answers | Removes objections |
| 13 | Contact routes (3 tiles + form) | ContactPage signals | Conversion |

**Claude Design prompt (Homepage):**

> Using the NEXUS design system, design the full homepage at 1440px and 390px. Black hero with Variant A, Mark's H1 (from the hero prompt), the corridor line visual, and a large cropped X outline behind it. Then, in this order: proof strip (100+ businesses actively supported, 16 curated global partnerships, 1,400+ business plans assessed, Supplier and security cleared; four logo placeholders marked "permission to confirm"); three route cards plus the text link "UK company going to China? See the Asia corridor"; the Asia corridor section on white with a yellow top rule and five partner cards; How we work (Diagnose, Plan, Connect, Deliver, Grow); three case study cards (Sentian Aerospace, GI Healthcare, Auto Impartial); Events on black (NEXUS Sessions, Global Innovator Awards 16 November 2026); partner chips; team portraits in black and white; three insight cards plus the "Doing Business in China 2027" report card; five FAQs as an accordion; three contact tiles and a form. Yellow only as an accent, never a background. All text is live text, never in images. One H1. Use "[Placeholder: …]" boxes for every missing image or unapproved claim.

### 3.4 `/international-companies`: the flagship landing page

Use prompt B from `05`. Add these SEO and conversion rules:

| Rule | Detail |
|---|---|
| `<title>` | UK Market Entry for Tech Companies from China \| NEXUS |
| H1 | "Enter the UK with a team already on the ground." (Mark's prototype H1). Keep it. The keyword sits in the title, eyebrow and first paragraph instead. |
| Eyebrow | UK MARKET ENTRY FROM CHINA AND ASIA |
| First paragraph | 40–60 word direct answer (search and AI quote it). Real text. |
| Primary CTA | "Request a Market-Entry Diagnostic", repeated three times: hero, after the offers, final form |
| Proof position | One result directly under the offers (DarkhorseOne or Smart Patent), not only at the bottom |
| "Not for" block | Visa-only enquiries go to UKES. Keeps the pipeline clean. |
| FAQs | 4–5, phrased as buyers ask: "How long does UK market entry take?", "Do I need a UK company to start?", "How are payments from mainland China handled?" |
| Form | Company, HQ country, sector, stage, timeline, name, work email, unticked consent. Event: `diagnostic_request`. |

```text
Visitor flow:
Search "UK market entry from China" -> hero + answer paragraph -> 3 offers
-> proof card -> how it works -> FAQs -> diagnostic form -> NEXUS replies [response time to confirm]
```

---

## 4. Considerations

| # | Consideration | Risk if ignored | What to do |
|---|---|---|---|
| 1 | **Claude Design output is a design, not the site.** Exports can use web components, scripts and Google Fonts (`knowledge-base/nazia/seo lady draft.html` shows `<x-dc>` and `support.js`). | Content invisible to crawlers; broken in mainland China | Use exports as the visual spec. Build real HTML via Handoff to Claude Code. |
| 2 | **Mainland China access** | Fonts, maps, YouTube or reCAPTCHA fail; the target audience sees a broken page | Self-host fonts; no Google services; test under 5 s from China |
| 3 | **Unapproved claims and logos** | Legal and reputational risk | Every partner name, logo, stat and case study stays a placeholder until written consent |
| 4 | **Entity confusion** ("Nexus" is a crowded name) | AI engines mix NEXUS with other companies | "NEXUS Creative HQ" in first mentions, footer and schema; one email domain |
| 5 | **Visa separation** | Visa leads flood commercial forms | No commercial CTA near UKES content |
| 6 | **Brand drift** | Prototype already uses yellow backgrounds | Yellow accent only; check every export |
| 7 | **One H1, live text, FAQ schema** | Lost rankings and AI citations | Part of the export checklist (§6) |
| 8 | **Accessibility (WCAG 2.2 AA)** | Excludes users; fails public-sector buyers | Contrast, focus states, 48px buttons, reduced motion |
| 9 | **Timeline** (launch Thu 12 Nov, GIA Mon 16 Nov) | Design runs late and eats build time | Design finished by Fri 6 Nov (§5) |
| 10 | **Confidentiality** | Private case studies leak through a shared link | Keep the Claude Design project private to the organisation |

---

## 5. Business

### 5.1 How each page earns

| Page | Offer it sells | Conversion event | Who pays |
|---|---|---|---|
| Homepage | Routes to every offer | `cta_click`, `partnership_call_request` | All audiences |
| `/international-companies` | Market-Entry Diagnostic → UK Soft Landing retainer → Market Intelligence Report | `diagnostic_request` | International tech companies |
| (swap option) `/institutions` | UK Representation, UK Landing Programme | `partnership_call_request` | Science parks, innovation zones |

Prices are "On application" until NEXUS confirms them.

### 5.2 Targets at 90 days after launch (from `02`, to agree with the client)

| KPI | Baseline | Target |
|---|---|---|
| Qualified enquiries (partnership + diagnostic + sponsor) | ~0 tracked | 8–12 per month |
| Non-brand clicks (Google Search Console) | ~0 | 150+ per month |
| Non-brand keywords in top 100 | 0 | 50+ |
| AI engines naming NEXUS (40 prompts) | 0 of 3 category prompts | 8 of 40 |
| Lighthouse mobile: performance / accessibility | n/a | ≥85 / ≥95 |

### 5.3 Schedule (the one sequencing list)

| Date | Work |
|---|---|
| Mon 2 Nov | Design system in Claude Design; hero Variants A and B |
| Tue 3 Nov | Lyssna 5-second test; pick the hero |
| Wed 4 – Thu 5 Nov | Homepage and `/international-companies`, desktop and mobile |
| Fri 6 Nov | Export, run §6 checklist, Handoff to Claude Code |
| Mon 9 – Tue 10 Nov | Staging: crawl, schema, speed and China tests |
| Thu 12 Nov | Launch |

### 5.4 Needed from NEXUS before the design is final

| Item | Blocks |
|---|---|
| Answer to question 3 (which audience brings most revenue) | Choice of flagship page |
| Tianjin signing photo + caption | Hero image |
| Written permission for logos and case studies | Proof strip, results cards |
| Licensed font files (Neutral Face, General Sans) | Exact type rendering |
| Payment method for mainland China clients | FAQ answer on the international page |

Cost: Claude Design is part of the existing Claude plan; Lyssna, GSC, Bing and Clarity are free tiers.

---

## 6. Export checklist (run on every Claude Design export)

- [ ] Exactly one H1, containing or next to "UK–China" / "UK market entry"
- [ ] All copy is live text; nothing important inside images
- [ ] 40–60 word answer paragraph under the hero
- [ ] FAQ block present (5 on Home, 4–5 on the international page)
- [ ] No Google Fonts, Maps, YouTube or reCAPTCHA
- [ ] Yellow never used as a section background or as text on white
- [ ] Every unconfirmed claim, logo and photo is a `[Placeholder: …]`
- [ ] Mobile 390px version exists and buttons are at least 48px tall
- [ ] Form has an unticked consent box and a privacy link
- [ ] Visa content links only to UKES, with no commercial CTA

---

## 7. Closing view

The homepage and one flagship landing page are enough to change how Google and AI engines describe NEXUS. Once both templates exist, the remaining audience and corridor pages are copy swaps, not new design work. The one open decision is which audience gets the flagship slot, and that comes from the client's answer to question 3.

# NEXUS Website, SEO and AEO Strategy Plan

> **Mark's documents win.** Where this document differs from Mark's brief or prototype copy, follow [`07-NEXUS-Mark-Facts.md`](../knowledge-base/07-NEXUS-Mark-Facts.md). Its section 15 lists our proposals that still need Mark's decision.

Draft v1, 31 Oct 2026. Builds on the Developer Brief (approved sitemap) and `01-NEXUS-Research-Findings.md`. Items marked **[Decision]** need client sign-off.

---

## 1. Business goals → website goals

| Business goal (from brief) | Website job | Primary KPI |
|---|---|---|
| Win institutional partners (science parks, zones, funds) | Show NEXUS as their operating partner in the UK | `partnership_call_request` |
| Sell paid diagnostics to international tech companies | Make market entry feel low-risk and concrete | `diagnostic_request` (international) |
| Sell growth diagnostics/projects to UK scale-ups | Fast route to a scoped project | `diagnostic_request` (UK) |
| Monetise audience through sponsors | Prove audience quality (GIA, sessions) | `sponsor_pack_request` |
| Fill 2027 China/HK delegations | Capture early interest | `delegation_interest` |
| Be the AI and search "answer" for UK–China tech market entry | Clear entity data, corridor-led content | Brand + corridor queries in GSC; AI answers naming NEXUS |

**North-star:** qualified enquiries per month, by source and audience (traffic is a supporting metric only).

## 2. Positioning fix (responding to the WhatsApp feedback)

The H1 "Land, grow and scale technology businesses in the UK." is strong for people but **generic for search engines and AI engines**: it could describe any of the competitors. Our AEO test supports this: the AI answer repeated "China as its flagship corridor" from NEXUS's own site, but couldn't name a single China partner, and NEXUS was absent from every UK–China category answer.

**Recommendation: keep the bold H1 but put the corridor in the machine-readable layers around it.**

| Layer | Current | Proposed |
|---|---|---|
| Eyebrow (above H1) | "UK growth partner · China flagship corridor" | "The UK–China innovation corridor" |
| H1 option A (keep brand voice) | Land, grow and scale technology businesses in the UK. | *unchanged* |
| H1 option B **[Decision]** | | "Land, grow and scale in the UK. **From China and beyond.**" (yellow on the second line) |
| Intro sentence (first 160 chars, which AI engines quote) | "NEXUS works with international technology companies…" | "NEXUS is the operational bridge between the UK and China for technology companies, science parks and innovation zones: one accountable team in the UK, with partners on the ground in China." |
| `<title>` | NEXUS \| Land, grow and scale technology businesses in the UK | **NEXUS \| UK–China Tech Market Entry & Scale-Up Partner** |
| Meta description | "…with China as our flagship corridor." | "The UK–China operational bridge for technology companies and innovation institutions. Market entry, UK soft landing, representation and scale-up delivery from London." |
| Organization schema `description` + `knowsAbout` | Generic | Corridor-first, plus `areaServed`: GB, CN, HK |

**Entity disambiguation (critical, because "Nexus" is a crowded name):** always say "NEXUS Creative HQ" in the first mention on About, Contact, footer and schema `legalName`/`alternateName`; use one email domain; keep LinkedIn, Companies House and site descriptions identical; add `sameAs` links (LinkedIn, Instagram, X, Facebook, GIA site, Startup Diaries, Companies House URL).

## 3. Audiences (who, what they search, what we offer, CTA)

| Audience | Pain | Search/AI language (hypotheses to validate) | Offer | CTA |
|---|---|---|---|---|
| **Innovation institutions** (CN science parks, zones, e.g. TEDA/Binhai; UK/EU hubs) | Need a real UK presence for their portfolio, not reports | "UK landing programme for science park", "UK representation office for innovation zone", "UK partner for Chinese incubator", 英国落地 / 英国代表处 (Chinese terms, for later) | UK Representation; UK Landing Programme; delegations | Book a partnership call |
| **International tech companies** (China, HK, Asia, then global) | Wasting months and money working out UK entry alone | "UK market entry for tech companies", "expand tech company to UK from China", "UK soft landing programme", "set up UK company from China" | Market-Entry Diagnostic → Soft Landing → Market Intelligence Report | Request a diagnostic |
| **UK scale-ups** (AI, deep tech, life sciences) | A specific growth problem with no time | "R&D tax credit help scale-up", "Series A fundraising support UK", "AI adoption consultancy SME", "scale-up advisory London" | Growth Diagnostic → partner projects | Request a growth diagnostic |
| **Professional firms / sponsors** | Want access to international founders and institutions | "sponsor startup awards London", "reach international founders UK" | GIA + session sponsorship, referrals | Request the sponsor pack |
| **UK companies going to China/Asia (outbound)** | Want customers, partners or investors in China/HK without going alone | "doing business in China 2027", "Hong Kong gateway to Asia", "UK trade delegation China", "expand UK tech company to China" | 2027 delegations (mainland China/HK); China representation via RidgeCore; *Doing Business in China 2027* report | Register delegation interest / request the report |
| **Visa applicants (non-commercial)** | Innovator Founder endorsement | "innovator founder visa endorsement", "UKES endorsement" | Factual Endorsing-role page → UKES | Go to UKES |

**[Decision] Visa traffic:** high search volume and many backlinks, but it attracts the wrong leads. Recommendation: one factual page, no commercial CTA, internal links to UKES only. It keeps the authority without polluting the pipeline.

## 4. Sitemap + keyword mapping (brief sitemap, with SEO targets)

One primary keyword cluster per page, so pages don't compete with each other. Volumes are **unvalidated** until the Semrush/GSC pull (see §7).

| URL | Primary cluster | Secondary / AEO question it must answer | Schema |
|---|---|---|---|
| `/` | UK–China tech market entry partner; NEXUS Creative HQ (brand) | "What is NEXUS?" | Organization, WebSite, FAQPage |
| `/institutions` | UK landing programme / UK representation for science parks and innovation zones | "How can a Chinese science park get UK representation?" | Service ×2, FAQPage, Breadcrumb |
| `/international-companies` | UK market entry for tech companies; UK soft landing | "How do I expand my tech company to the UK from China?" | Service ×3, FAQPage |
| `/uk-scale-ups` | scale-up advisory UK; growth diagnostic | "Where can UK deep-tech scale-ups get Series A / R&D tax help?" | Service, FAQPage |
| `/asia-corridor` | UK–China innovation corridor; China–UK tech partnerships; Hong Kong gateway; UK delegation to China 2027 | "Who connects Tianjin/Shanghai tech firms with the UK?" and "How can a UK tech company enter China via Hong Kong?" | Organization (partners), Event (delegations), FAQPage |
| `/results` + `/results/{slug}` | [company] case study; "UK expansion case study China" | Proof for every claim | Article |
| `/partner-with-nexus` | sponsor startup events London; referral partnership | | Service |
| `/events` (+ GIA) | Global Innovator Awards; UK–China founder events London | | Event |
| `/about` | NEXUS Creative HQ team, CEO | "Who runs NEXUS?" | AboutPage, Person |
| `/about/endorsing-role` | Innovator Founder endorsement UKES consortium | Factual only | WebPage, FAQPage |
| `/insights` + `/insights/{slug}` | Topic clusters (§5) | Long-tail questions | Article, Report |
| `/contact` | | | ContactPage, PostalAddress |

**Additions to consider [Decision]:**
1. `/asia-corridor/china`, `/asia-corridor/hong-kong` (Phase 2): dedicated city/market pages win "UK from Hong Kong" searches.
2. Absorb **nexusstartupdiaries.com** into `/insights` (or point it at the main domain with 301s). Two domains split authority; the Diaries content is the most on-strategy content NEXUS has.
3. A `/glossary` or "UK market entry guide" pillar page: very citable by AI engines.

## 5. Content and AEO plan

**Topic clusters for Insights** (each cluster = 1 pillar guide + 4–6 supporting posts, linking to its audience page):

1. **UK market entry from China/Asia (inbound)**: free pillar page "Entering the UK from China: 2027 Guide". Supporting posts: UK company setup steps, UK banking for Chinese founders, UK soft landing explained, costs of UK entry, Hong Kong vs direct route.
2. **Institutions and corridors**: how UK landing programmes work, the Tianjin MOU story, S-Tron takeaways, delegations.
3. **Scale-up growth**: R&D tax credits, Seed/Series A readiness, AI adoption (reuse existing funding-map articles).
4. **Global founders in the UK**: GIA stories, founder interviews (migrate Startup Diaries).
5. **UK → China and Asia (outbound)**: the brief's gated report **"Doing Business in China 2027"**. The prototype describes it as an annual guide *for UK technology companies looking at China and Hong Kong*, i.e. outbound, not inbound. Supporting posts: "Hong Kong as a gateway: a first step into Asia for UK founders" (the prototype's featured insight), what a 2027 delegation involves, S-Tron lessons for UK exhibitors, Manchester and China. CTA: report request + delegation interest.

**Note: the corridor runs both ways.** The prototype calls it "a working corridor in both directions" (RidgeCore represents NEXUS clients in China; delegations take UK companies to China/HK; NEXUS opened a company in China in March 2026, wording to be confirmed). Inbound is the main revenue focus, but outbound content and the report are the main lead magnets for the delegation programme.

**AEO / GEO rules (AI answer engines):**
- Start every service page and article with a **40–60 word direct answer** paragraph.
- Visible FAQ blocks (5 per page) phrased exactly like the questions buyers ask, plus FAQPage schema.
- Specific, citable facts (numbers, dates, partner names, places) instead of adjectives. AI engines quote specifics.
- Same one-line and one-paragraph description everywhere (brief §10), including LinkedIn and partner sites.
- Earn **third-party mentions** on CBBC, the GIA judges' organisations, City of London, S-Tron and partner sites. AI engines trust what others say about NEXUS more than what NEXUS says about itself.
- Allow AI crawlers (GPTBot, PerplexityBot, ClaudeBot, Google-Extended) in robots.txt. Serve real HTML (pre-rendered), no text in images.
- Monthly **AI visibility check**: run 10 fixed prompts in ChatGPT, Perplexity, Gemini and Copilot, and record whether NEXUS is named.

**Legacy content audit (101 insights + 30 podcasts + 15 events + 7 videos):**
- Keep and refresh: funding, R&D, IP, scale-up, S-Tron, City of London, China items.
- Consolidate: duplicates (e.g. "Are Women Becoming the UK's Growth Advantage?" appears twice, "2026 Funding Map" twice).
- Retire with a 301 to the nearest topic or `/insights`: off-strategy creative pieces (Canva, influencer, music). **Never leave a linked URL as a 404.** Check Ahrefs "best by links" first.

## 6. Technical SEO essentials (adds to brief §8–10)

- A full 301 map for all 173 URLs plus the 11 known 404s plus image URLs that have backlinks (from Ahrefs).
- Mainland China access: no Google Fonts, Maps, reCAPTCHA or YouTube; an Asia CDN; a <5 s test. Already in the brief.
- `hreflang` ready for a future zh-Hans version (the brief allows a later language switcher).
- Self-host Neutral Face and General Sans (the prototype uses Google Fonts, which **must change**).
- Move legal pages from the Nexudus subdomain to `/privacy`, `/terms`, `/cookies`.
- Fix the GIA date conflict (17 Oct vs 16 Nov) on the live site **now**.

## 7. Tools: what, why, when (from the Tool Guide, prioritised)

| # | Tool | Benefit to NEXUS | When | Cost |
|---|---|---|---|---|
| 1 | Google Search Console | Baseline queries; sitemap; migration monitoring | **Now** (client to add us) | Free |
| 2 | Ahrefs Webmaster Tools | Find which old URLs hold the 884 domains' links, which drives the redirect map | **Now** | Free |
| 3 | Bing Webmaster Tools | Bing feeds Copilot/ChatGPT search; AI performance report | Now | Free |
| 4 | Semrush (free tier) / Ahrefs Lite | Keyword volumes; competitor rankings (CBBC, Strategi, TusPark) | Before copy is final | Free / $129 per month |
| 5 | Screaming Frog | Crawl staging; test every 301; titles, H1s, canonicals | Staging + launch | Free ≤500 URLs |
| 6 | SparkToro | Where institutions and founders spend time online (podcasts, sites) | Before launch | Free previews |
| 7 | Lyssna 5-second test | Does the hero say "UK–China"? A/B the H1 options | Before copy is final | Free (15 responses) |
| 8 | GA4 + GTM (consent-gated) | The 10 conversion events in brief §11 | Launch | Free |
| 9 | Microsoft Clarity | Recordings and heatmaps on audience pages | Launch | Free |
| 10 | PageSpeed / Lighthouse + China speed test | Acceptance targets (LCP < 2.5 s, China < 5 s) | Staging + launch | Free |
| + | Olostep (already set up) | Competitor crawls, AI-answer monitoring, content audits at scale | Ongoing | Existing key |

## 8. KPIs and 90-day targets (proposed, to be agreed with the client)

| KPI | Baseline | 90 days after launch |
|---|---|---|
| Primary conversions (partnership + diagnostic + sponsor) | ~0 tracked | 8–12 qualified per month |
| Organic non-brand keywords ranking top 100 | 0 | 50+ |
| Non-brand clicks (GSC) | ~0 | 150+ per month |
| Old URLs returning 404 | 11 pages, 59–77 images (depends on the check) | 0 |
| AI visibility (10 prompts × 4 engines) | 0 of 3 category prompts (Olostep); full 40-prompt baseline to run in week 1 | 8/40 |
| Lighthouse mobile performance / accessibility | n/a | ≥85 / ≥95 |

## 9. Timeline (launch target Thu 12 Nov 2026, GIA on 16 Nov)

| Week | Work |
|---|---|
| Mon 2 Nov | Send client pack (03); get GSC/GA4/Bing/Ahrefs access; fix the live GIA date; export backlinks; **start data exports** (old-site subscribers, Zoho, Typeform) |
| Tue 3 – Fri 6 Nov | Keyword validation (Semrush + GSC); finalise titles, meta, H1 options; build redirect map v1; legacy content triage |
| Mon 9 – Tue 10 Nov | Staging crawl (Screaming Frog); schema validation; Lyssna hero test; copy edits for the AEO intro paragraphs |
| Wed 11 – Thu 12 Nov | Launch; 301 checks; submit sitemaps; GA4 DebugView |
| Fri 13 – Mon 30 Nov | Monitor 404s and coverage daily; GIA (Mon 16 Nov) content push; update GIA Event schema and llms.txt after the event; first corridor pillar article |
| Dec–Jan | Content clusters 1, 2 and 5 (outbound report); absorb Startup Diaries; outreach for third-party mentions; monthly report |

**If 12 Nov is at risk (MVP order):** Home → three audience pages → Asia corridor → Contact/forms → redirects → Events (GIA) → Results → the rest.

## 9b. The wider toolset: decisions needed alongside the website

Full inventory in `01` §8. Each decision affects SEO, tracking or data:

| Decision | Recommendation | Why it matters |
|---|---|---|
| One **ticketing** platform | Ticket Tailor (already used for GIA) for GIA and NEXUS Sessions; UTMs on every link | Attendee data in one place; ticket clicks measurable |
| **"Ask Fin"** (Intercom AI agent) | Keep on GIA through 16 Nov; consent-gate it; add a visa guardrail; Phase 2 decision for the NEXUS site | Compliance; accurate answers; keeps UKES separate |
| One **email/newsletter** platform | Choose one for "The NEXUS Briefing"; merge Mailchimp, old-site, Ghost (and Brevo) lists with consent | Four lists = duplicate sends, GDPR risk, old "Cellar Door" branding |
| **Data exports** before switch-off | Zoho, Typeform, old-site subscribers, Nexudus members | Otherwise leads and subscribers are lost at migration |
| **Email deliverability** | One transactional sender for forms; DMARC to quarantine; DMARC on the GIA domain | Form notifications and acknowledgements must arrive (brief §7) |
| **Analytics standard** | Same consent-gated GA4 setup on GIA and NEXUS; cross-domain tracking GIA ↔ NEXUS | Today GIA appears to track before consent; NEXUS has no baseline |
| **Entity links** | GIA schema `organizer.url` → nexuscreativehq.com; Startup Diaries links to the main site | Connects NEXUS, GIA and the Diaries as one entity for Google and AI |
| **Retire legacy** | Nexudus, Zoho, old Laravel admin after launch | Smaller attack surface (NCSC PHP alert); no off-domain legal pages |
| **Booking + payments (Phase 2)** | Choose a diagnostic booking/payment tool that also handles **mainland China clients** (invoice/bank transfer or Alipay/WeChat Pay via a provider) | An open prototype FAQ; card-only checkout may block Chinese institutions |

## 10. Risks

- Unconfirmed claims (supplier clearance, partner names, case-study consent) published too early: legal and reputational risk.
- Redirect map incomplete at launch: loses the link equity that is the site's main SEO asset.
- Prototype deviates from brand rules (Google Fonts, yellow section backgrounds): follow the guidelines.
- Two domains (Startup Diaries) keep splitting authority if not resolved.
- Visa-related traffic overwhelms commercial forms if the endorsing page has commercial CTAs.

# NEXUS: Mark's facts (the source of truth)

| | |
|---|---|
| Date | 4 November 2026 |
| Scope | Everything Mark has stated in writing about the new site: decisions, page specs, copy, proof, brand, forms, search, technical and launch rules |
| Audience | Everyone designing, writing or building the NEXUS site (Zeeshan, Hasaan, any developer) |
| Sources | `research/local-docs/`: Developer Brief (`NEXUS Website Brief Developer - clean.txt`), prototype copy (`prototype/*.txt`), `NEXUS Member Case Studies.txt`, `NEXUS Brand Guidelines 2025.txt` |
| Not in scope | Our own SEO proposals (see section 15 for where they differ), tool choices, the build platform |

---

## Summary

Mark's documents are the facts. Where any other document in this repo, a design or a draft site differs from them, Mark's version is what we build, and the difference goes to Mark as a question.

1. **Order of authority:** Brand Guidelines 2025, then the Developer Brief, then the prototype copy, then everything else. The brief itself says "where the prototype differs from the guidelines, the guidelines win".
2. **Labels:** Mark tags each requirement as **Approved** (build it as described), **To confirm** (build it so it can change, or use a placeholder) or **Optional** (price it separately).
3. **Copy:** use the prototype copy until Mark sends final versions. Do not write substitute claims, statistics, testimonials or case studies. Anything missing becomes a visible `[Placeholder: …]`.
4. **Two lines that are never crossed:** no case study mentions visa or endorsement status, and the UKES endorsing role stays separate from every commercial service.
5. **Our proposals** (H1 option B, alternative titles and intros) are still options for Mark to decide. They are not defaults. Section 15 lists them, and the earlier documents now say so.

---

## 1. Who NEXUS is, in Mark's words

| Item | Mark's wording |
|---|---|
| Legal entity | NEXUS Creative HQ Ltd, company number 12667243 |
| One line | NEXUS helps technology businesses land, grow and scale in the UK, with China as its flagship corridor. |
| One paragraph | NEXUS is the UK growth partner for international technology companies, the innovation institutions that back them, and UK scale-ups ready for their next stage. China is our flagship corridor and Hong Kong our gateway to the wider region, with partners on the ground in China and membership of the China-Britain Business Council. We have assessed more than 1,400 business plans and actively supported more than 100 businesses. |
| Three client groups | Innovation institutions (science parks, innovation zones, hubs, funds); international technology companies entering the UK; UK technology scale-ups already trading |
| Partners and sponsors | Professional firms (law, accountancy, banking) partner with NEXUS and sponsor its events |
| UKES | NEXUS reviews and endorses Innovator Founder visa applicants as a consortium partner of UK Endorsing Services. Always kept separate from commercial services |
| Mission (guidelines) | To be the most trusted operational bridge between the UK and the world's most dynamic innovation ecosystems, turning global connections into real business outcomes |
| Brand lines (guidelines) | "The launchpad for innovative businesses." · "We build bridges between worlds." · "Bold founders deserve bold backing." · "We build businesses" (footer lockup) |
| Why rebuild | The current site describes what NEXUS used to do, not what it sells: no service pages, no routes per client type, no case studies, no proper enquiry routes |
| Success | A steady flow of qualified enquiries from each client type, with the source of each recorded |
| Launch | Live by Thursday 12 November 2026, before the Global Innovator Awards on Monday 16 November 2026 |

## 2. Decisions Mark has made (Approved)

| Decision | What it means |
|---|---|
| New custom build | Like the Global Innovator Awards site. The developer proposes the platform, hosting and languages. Pre-built (static or cached) pages wherever possible |
| Brand guidelines | Follow them exactly. They beat the prototype |
| "Asia corridor" | The nav item and page are "Asia corridor" at `/asia-corridor`. China is the flagship, and Hong Kong is the gateway to the wider region. On the Asia corridor page, use "Asia corridor" in place of the prototype's "China corridor" (brief 4.4) |
| No Chinese pages at launch | Leave room for a later language switcher (text out of images, space for one header icon) |
| No Zoho | Forms store enquiries on the site, email NEXUS and are ready for a future CRM webhook |
| Placeholders | Clearly marked, replaceable in the CMS, can be hidden with a toggle, never styled to look final |
| PHP security | Protect against NCSC-flagged CVE-2026-109618 and CVE-2026-109619 and any later ones |
| Out of scope | Writing new copy, translation, photography, ongoing maintenance, a client login |

## 3. Sitemap, header and footer

**Header:** Institutions · International companies · UK scale-ups · Asia corridor · Insights · Events · About. On the right, "Partner with NEXUS" plus a yellow "Talk to us" button. The current page gets a yellow underline. Below 1100px it collapses into a Menu button that works by keyboard, sets `aria-expanded` and closes with Escape. No language link at launch. An **announcement bar** above the header is editable and can be switched off. It runs GIA until 16 November, then highlights.

**Footer:**
- **Who we help:** the three audience pages plus Partner with NEXUS.
- **Explore:** Asia corridor, Results, Events, About and team, Endorsing role, Insights. The prototype also lists NEXUS Startup Diaries.
- **Contact:** Talk to us, email, social links (LinkedIn, Instagram, X, Facebook).
- **Legal line:** "© 2026 NEXUS Creative HQ Ltd · Company number 12667243 · [registered office]", plus Privacy, Cookies, Terms, Accessibility.

| Page | Address | Primary action | Phase |
|---|---|---|---|
| Home | `/` | Find your route; Talk to our team | 1 |
| For institutions | `/institutions` | Book a partnership call | 1 |
| For international companies | `/international-companies` | Request a diagnostic | 1 |
| For UK scale-ups | `/uk-scale-ups` | Request a diagnostic | 1 |
| Asia corridor | `/asia-corridor` | Register for 2027 delegations | 1 |
| Partner with NEXUS | `/partner-with-nexus` | Request the sponsor pack | 1 |
| Results | `/results`, `/results/{slug}` | The matching audience action | 1 |
| Events | `/events` | Get tickets (GIA site); Register interest | 1 |
| Event detail | `/events/{slug}` | Register | 2 |
| About | `/about` | Talk to us | 1 |
| Endorsing role | `/about/endorsing-role` | Go to UKES (no commercial CTA) | 1 |
| Contact | `/contact` | Three route tiles plus a general form | 1 |
| Insights | `/insights`, `/insights/{slug}` | Read; download | 1 |
| Legal | `/privacy`, `/cookies`, `/terms`, `/accessibility` | None | 1 |

The page list is Approved. Page names and copy are To confirm.

## 4. Page specs (section order is fixed)

### Home (brief 4.2)
1. Announcement bar
2. Header
3. Hero on black:
   - eyebrow "UK growth partner · China flagship corridor"
   - H1 **"Land, grow and scale technology businesses in the UK."**
   - intro "NEXUS works with international technology companies, the institutions that back them, and UK scale-ups ready for their next stage. One accountable team in the UK, with partners on the ground in China."
   - buttons: Find your route; Talk to our team
   - image: the Tianjin signing photograph (caption To confirm)
4. Proof strip:
   - the four statistics (section 6)
   - logos for City of London, TEDA, S-Tron and CBBC, each permission To confirm
5. Who we work with (`#routes`): three audience cards
6. How we work: five steps (Diagnose, Plan, Connect, Deliver, Grow) and a photo
7. Asia corridor, led by China:
   - five partner cards: RidgeCore Ventures, Alibaba Entrepreneurs Fund, Tianjin, S-Tron, Swiss Bluefaer Innovation Centre
   - a Hong Kong gateway line
   - two buttons
   - **on white with the yellow top rule**
8. Results: Sentian Aerospace, GI Healthcare, Auto Impartial, plus a link to `/results`
9. Events on black: the session series and GIA
10. Partner network:
    - category chips: Accountancy, Corporate finance, Banking and payments, Legal, IP and patents, AI strategy, R&D tax, Venues
    - a link for firms
11. The team (`#about`): a founder quote placeholder and team portraits
12. Insights: three latest articles, a placeholder card for the Doing Business in China 2027 report, and an All insights link
13. Common questions: five FAQs (prototype)
14. Contact routes (`#contact`): three tiles
15. Footer

### Audience pages (brief 4.3, one template)

Template, in order:
1. Hero with breadcrumb
2. The challenge
3. What we provide (offer cards)
4. Why us, with evidence and case studies
5. Who it is for and not for
6. How it works (`#how`)
7. Questions
8. Enquiry form (`#start`)
9. Footer

| Page | Mark's H1 (prototype) | Offers | Case studies |
|---|---|---|---|
| Institutions | Your operating partner in the UK. | UK Representation; UK Landing Programme | `[Institution case study]` placeholder |
| International companies | Enter the UK with a team already on the ground. | Market-Entry Diagnostic; UK Soft Landing; Market Intelligence Report | DarkhorseOne; Eco2Life; Smart Patent |
| UK scale-ups | Your next stage, with the right specialists. | Growth Diagnostic; partner-delivered projects; ongoing access (name To confirm) | GI Healthcare; Sentian Aerospace |

### Asia corridor (brief 4.4)
- **H1:** "Our Asia corridor, led by China."
- **Our partners across Asia:**
  - RidgeCore Ventures (China), Alibaba Entrepreneurs Fund (Hong Kong), Tianjin, S-Tron (Shanghai) and Swiss Bluefaer Innovation Centre (Shanghai)
  - a Why Hong Kong card and a logo row
  - Alibaba Entrepreneurs Fund and Swiss Bluefaer appear **by name only, with placeholder wording and no logo**, until each confirms in writing
- **Where we have been:** a timeline managed in the CMS (section 6).
- **Case studies:** Auto Impartial, Eco2Life, Smart Patent.
- **2027 delegations** to mainland China and Hong Kong: details are a placeholder, and the interest form (`#delegations`) has a destination field.
- **Remove** the prototype's Chinese-language block.

### Other pages
- **Results (4.5):**
  - listing of all case studies (audience filter in Phase 2)
  - each case study page has: sector, website link, headline; About the company, The challenge, How NEXUS helped, The outcome; Impact at a glance (three points); the founder quote; a link to the matching audience page
- **Partner with NEXUS (4.6):** hero; who you will meet, with statistics; three ways to partner (Sessions, Awards, Referrals); sponsor pack form (`#start`).
- **Events (4.6):** hero; coming up (GIA and the session series, name and venue as placeholders); past events; interest form (`#register`).
- **About (4.7):** story, team and mentors, partner categories, clearance.
- **Endorsing role:** about 200 words of plain text on the UKES consortium role, with a link to UKES and no commercial CTA. Wording is a placeholder until Mark sends it.
- **Contact:** three route tiles plus a general form.
- **Insights (4.8):**
  - hero and a featured insight
  - topic filters: All, Asia corridor, Market entry, Funding and IP, CreaTech, Events
  - card grid
  - the China 2027 report request form (interest only in Phase 1)
  - The NEXUS Briefing monthly email (working name)
  - links to NEXUS Startup Diaries and Events
  - formats: Article, Guide, Report, Event notes, Founder story
  - do not publish an article that names a partner until that partner approves

## 5. Offers and price lines (prototype)

| Audience | Offer | Price line |
|---|---|---|
| Institutions | UK Representation (annual): named UK contact, showcase events, pipeline of UK partners, customers and investors, landing support, regular reporting | Annual retainer, on application |
| Institutions | UK Landing Programme (per cohort): pre-arrival briefing, curated UK programme [format To confirm], showcase event, legal, banking and accountancy introductions, follow-up | Priced per cohort, on application |
| International | Market-Entry Diagnostic: opportunity, route to market, introductions needed, costed plan | Fixed fee [To confirm], credited against further work |
| International | UK Soft Landing: named UK contact, qualified introductions, legal, banking and accountancy partners, event representation | Set-up fee plus monthly retainer, on application |
| International | Market Intelligence Report: market size, competitors, regulation, next steps | Fixed fee, on application |
| Scale-ups | Growth Diagnostic: where growth stalls, top one or two priorities, who delivers and at what cost, next steps | Fixed fee [To confirm], credited against further work |
| Scale-ups | Partner-delivered projects: go-to-market, investment readiness, AI strategy and adoption, R&D tax credits, accountancy, legal and IP | Priced per project, on application |
| Scale-ups | Ongoing access: partner network, roundtables, peer sessions | [Name, format and price To confirm] |
| Firms | Session sponsorship · GIA sponsorship · Referral network | Packages To confirm · on the awards site · by agreement |

Every price is a CMS field and can say "On application". No fee has been confirmed.

## 6. Proof Mark has supplied

**Statistics (Ready), exact wording:**
- 100+ businesses actively supported
- 16 carefully curated global partnerships
- 1,400+ business plans assessed (the institutions and international pages add "within the UK endorsement system")
- Supplier and security cleared (prototype sub-line: "UK Government supplier")

**Asia corridor facts (Ready unless marked):**

| Partner | What Mark says |
|---|---|
| RidgeCore Ventures | A reciprocal partnership: NEXUS represents their clients in the UK, they represent NEXUS clients in China. Investment, knowledge transfer and franchise opportunities |
| Tianjin | Two signed MOUs, building UK showcase events and a pipeline of Tianjin companies into the UK. Co-exhibited with NEXUS at S-Tron Shanghai. The prototype FAQ names Binhai Zhongguancun Science Park. Partner names and MOU dates To confirm |
| S-Tron Shanghai | Two years: exhibiting with UK companies in 2025, speaking on stage in 2026 |
| CBBC | NEXUS is a member of the China-Britain Business Council |
| Alibaba Entrepreneurs Fund | In discussion. Name only, placeholder wording, no logo, until written approval |
| Swiss Bluefaer Innovation Centre | Swiss innovation centre in Shanghai's Yangpu district. Name only until wording is approved |
| Hong Kong | The gateway: a familiar base for UK companies taking a first step into Asia, and a launch point for Chinese companies heading to the UK and Europe |

**Timeline (prototype, CMS-managed):**

| Date | Event |
|---|---|
| 2025 | First MOU with Tianjin [month, partner To confirm] |
| 2025 | S-Tron Shanghai, co-exhibited with Tianjin |
| March 2026 | NEXUS opens in China, with partners in Beijing and Shanghai [wording To confirm] |
| April 2026 | CBBC delegation to Hangzhou (AI, robotics, life sciences) |
| 2026 | S-Tron Shanghai, speaking on stage |
| 2026 | Second MOU with Tianjin [date To confirm] |

**Past events (prototype):** S-Tron Shanghai 2025; TOKEN2049 Singapore, 30 September 2025; City of London Corporation and NEXUS partnership launch; founder dinners and sponsored roundtables.

**Global Innovator Awards:** 16 November 2026. "Created and delivered by NEXUS. Celebrating overseas founders building businesses in the UK." Tickets are sold on the GIA site.

**Case studies (seven, Ready, from `NEXUS Member Case Studies.txt`):**

| Company | Sector | Headline | Main outcome | Founder(s) | Shown on |
|---|---|---|---|---|---|
| Sentian Aerospace | Aerospace and deep tech | From a garage to an international acquisition | Technology acquired by Volatus Aerospace (publicly listed) in under two years from UK incorporation; founders retained | Edmund Moyo, Dalumuzi Dube | Home, UK scale-ups |
| GI Healthcare | Deep tech and robotics | From an early prototype to customer-backed pilots | No customers to a customer-funded proof of concept and follow-on programme, towards TRL 7; founders named Scotland finalists, Great British Entrepreneur Awards 2025 | Ash Ganesan Indra, Adip Ranjan Das | Home, UK scale-ups |
| Auto Impartial | AI compute infrastructure | New silicon for the age of private AI | Core architecture independently validated; UK and Asia research consortium in formation with Innovate UK | Dr Xiusun Huang | Home, Asia corridor |
| DarkhorseOne | AI native enterprise software | AI native software, built for British business | UK patent application filed; commercial collaboration secured through the NEXUS network | Jian Ma | International |
| Eco2Life (EcoDo) | CreaTech | Global brands, local stories, powered by AI | Consultancy to a live AI platform with early revenue; UK patent application in progress; route into Shanghai and Singapore | Qingwen (Joy) Li | International, Asia corridor |
| Smart Patent | Legal tech | World-class IP strategy, made accessible by AI | Live platform; finalist in a national AI venture programme in China; preparing a UK and China raise | Jack Zhu | International, Asia corridor |
| Readii | EdTech | Helping every child find their voice in the UK classroom | Live, revenue-generating within two years; partner value around double its own revenue | Xiaoyu Su | Results only (no page assigned) |

Each case study has a founder quote in the source document. Use those quotes word for word, and don't edit them. The documents are marked "Private & Confidential", so check consent before anything goes live.

**Team (prototype):**

| Name | Role |
|---|---|
| Mark Sarfo-Kantanka | CEO and Co-Founder |
| Mauria Fransishku | NEXUS Manager |
| Grace Mander | Operations Manager |
| Kolos Sipos | Business and Finance Analyst |
| Jonny Quirk | Head of Community |
| Sheleene Sealy | Social Media Manager |
| Zee West | Head of Development |

Mentors are described as having "experience at Google, Microsoft, NBCUniversal, Sky, Disney and Apple" (scale-ups page). Portraits are black and white.

## 7. What can and cannot be said

| Do | Do not |
|---|---|
| Use prototype copy word for word until final copy arrives | Write substitute claims, statistics, testimonials, case studies, prices, emails, addresses or response times |
| Mark gaps as `[Placeholder: …]` | Style a placeholder to look like final content |
| Say "Asia corridor, led by China", with Hong Kong as the gateway | Call it the "China corridor" in navigation or page names |
| Name Alibaba Entrepreneurs Fund and Swiss Bluefaer as text only, with placeholder wording | Show their logos, or describe the relationship as signed |
| Show City of London, TEDA, S-Tron and CBBC logos as placeholders until each permission arrives | Present partner logos as approved |
| Keep the UKES role on its own factual page, with no commercial CTA | Mention visa or endorsement status in any case study, or sell visas |
| Answer "Can you help with visas?" with Mark's FAQ: introductions to immigration law specialists; endorsement handled separately through UKES | Market NEXUS as a visa route |
| Use real NEXUS photography (China signings, S-Tron, dinners, GIA, team) | Use stock or AI-generated images |

## 8. Brand rules (guidelines plus brief section 5)

| Element | Rule |
|---|---|
| Colours | Pitch Black #000000 (dominant), Electric Yellow #DFFF13 (accent), Studio Grey #D1D1D1 (neutral), Pure White #FFFFFF. No other colours, except a slightly darker grey for secondary text if Mark agrees |
| Yellow | Accent only: buttons, tags, underlines, icons, highlights. **Never a section background, never text on white.** Black on yellow for accents only |
| Backgrounds | Plain black, white or Studio Grey. White text on grey is not allowed. Every pair meets WCAG AA (4.5:1, or 3:1 for large text) |
| Logo | Supplied wordmark files only (SVG preferred). Metallic on white, white on black, black on yellow (accent). Never metallic on grey, never stretched, recoloured, with effects or on busy backgrounds. Alt text "NEXUS" |
| Headlines | Neutral Face Bold, for headlines, brand statements and display only |
| Body | General Sans (Light, Regular, Medium, Bold) at 17px, line height 1.6 |
| Fonts | Self-hosted. Licences to be confirmed for web use. Nothing from Google or other third parties |
| Buttons | Pill shape, at least 48px tall, bold label. Primary: yellow with black text. Secondary: outline. Visible focus ring everywhere |
| Layout | 1200px max content width; 32px gutters (20px mobile); 64 to 112px between sections |
| Motion | Hover and focus states only. Respect `prefers-reduced-motion` |
| Tone | Bold and confident: large headlines, generous white space, clear contrast |
| Test widths | 360, 768, 1280 and 1440px |

## 9. Forms and tracking

**Every form must:**
- validate input
- save the submission to the site database (staff can view, filter and export CSV)
- email the right inbox within 5 minutes
- send an acknowledgement
- show a thank-you message
- record the source fields

**Also:**
- A JSON webhook for the future CRM, built in Phase 1 and switched off.
- Spam protection: a honeypot plus rate limiting. **No Google reCAPTCHA** (it is blocked in mainland China).
- Diagnostics in Phase 1 are a request form only. NEXUS replies by hand with a booking and payment link.

**Field keys:**
- `form_type` takes one of: `partnership_call`, `diagnostic_international`, `diagnostic_scaleup`, `sponsor_pack`, `delegation_interest`, `event_interest`, `general`, `report_download`.
- Other fields: `name`, `email`, `organisation`, `role`, `country`, `organisation_type`, `sector`, `stage`, `timeline`, `interest`, `budget_band`, `message`, `marketing_consent` (never pre-ticked).
- Hidden: `page_url`, `cta`, `utm_source`, `utm_medium`, `utm_campaign`, `referrer`, `landing_page`, `submitted_at`.

**Analytics events (after consent only):**
- Primary: `partnership_call_request`, `diagnostic_request`, `sponsor_pack_request`
- Conversions: `delegation_interest`, `event_interest`, `general_enquiry`
- Secondary: `report_download`
- Tracked: `cta_click`, `case_study_view`, `outbound_gia_click`

Success is measured by qualified enquiries, not traffic.

## 10. Search and AI discoverability (Mark's defaults)

| Page | Title | Meta description |
|---|---|---|
| Home | NEXUS \| Land, grow and scale technology businesses in the UK | NEXUS helps international technology companies, the institutions behind them and UK scale-ups land, grow and scale in the UK, with China as our flagship corridor. |
| Institutions | UK representation for innovation institutions \| NEXUS | UK Representation and Landing Programmes for science parks, innovation zones, hubs and funds. Your operating partner in the UK. |
| International companies | UK market entry for technology companies \| NEXUS | Enter the UK with a team on the ground: market-entry diagnostic, soft landing support, market intelligence and vetted specialist partners. |
| UK scale-ups | Growth diagnostic for UK tech scale-ups \| NEXUS | A focused growth diagnostic, then partner-delivered projects in go-to-market, investment readiness, AI adoption and tax. One contact throughout. |
| Asia corridor | UK and Asia innovation corridor, led by China \| NEXUS | Our working corridor between the UK and Asia, led by China, with Hong Kong as our gateway, partners on the ground and 2027 delegations. |
| Results | Results and case studies \| NEXUS | How NEXUS has helped technology founders build in the UK, from first customers to an international acquisition. |
| Partner with NEXUS | Sponsorship and referral partnerships \| NEXUS | Meet international founders, UK scale-ups and innovation institutions through NEXUS sessions, the Global Innovator Awards and referrals. |
| Events | Events and the Global Innovator Awards \| NEXUS | NEXUS sessions, the Global Innovator Awards and delegations, bringing founders, institutions and specialists together. |

These are To confirm, so use them until Mark sends final versions.

**Other rules:**
- **Addresses and crawling:** lower-case hyphenated URLs; a self-referencing canonical; an XML sitemap; robots.txt blocking admin, search and thank-you pages (which are also `noindex`).
- **Headings and text:** one H1 per page, then H2 and H3 in order; all copy as real HTML text.
- **Images and sharing:** descriptive alt text; Open Graph images at 1200 × 630.
- **Structured data:** Organization (name "NEXUS", legalName "NEXUS Creative HQ Ltd", identifier 12667243, sameAs for the four socials), Service per offer, Event, Article, Person, FAQPage, BreadcrumbList.
- **Internal links:** each audience page links to the Asia corridor, Results and two insights; each case study links to its audience page; descriptive link text.
- Mark's brief: "No special AI files or tactics are needed."

## 11. Technical, China access and acceptance targets

| Area | Target |
|---|---|
| Responsive | Mobile-first, no horizontal scroll at 360px, touch targets at least 44px |
| Accessibility | WCAG 2.2 AA, pinch-zoom on, one H1, landmarks, visible focus, labelled fields, alt text, reduced motion, accessibility statement. Lighthouse accessibility 95+ per template |
| Performance | Mobile 4G: LCP under 2.5s, INP under 200ms, CLS under 0.1. Lighthouse performance 85+ on Home and audience pages. WebP or AVIF images |
| Mainland China | No Google Fonts, Maps, reCAPTCHA or YouTube on key pages; an Asia-serving CDN; Home and Asia corridor load fully in under 5s from a mainland China test |
| Privacy | Privacy notice on every form, only the listed fields, consent never pre-ticked, retention with automatic deletion, deletion on request. Analytics only after consent (accept, reject, manage) |
| Redirects | Full 301 map from every current address, including `/insight/{id}`, `/event/{id}`, `/video/{id}`, `/podcast/{id}`. No chains. Custom 404 linking the three audience pages |
| Minimum redirects | `/purpose` → `/about` · `/memberships`, `/esg`, `/scale-up-journey`, `/investment` → `/uk-scale-ups` · `/visa-routes` → `/about/endorsing-role` · `/become-partner` → `/partner-with-nexus` · `/booking`, `/locations` → `/contact` · `/videos`, `/podcasts` → `/insights` |
| Security | Component inventory; supported versions only; critical patches within 48 hours, others within 14 days; HTTPS with HSTS; WAF or CDN; security headers; 2FA for admins; encrypted enquiry data; vulnerability scan before launch; NCSC guidance and Cyber Essentials |
| Hosting | UK or EU; daily backups kept 30+ days, stored separately; one restore tested |
| Browsers | Latest two versions of Chrome, Edge, Safari (macOS, iOS), Firefox, plus Samsung Internet |
| CMS | Staff edit text, images, statistics, logos, FAQs, case studies, events, team, insights, placeholders and the announcement bar, with draft and preview. Editor and admin roles |

## 12. Phases and the fallback launch

| Phase | Delivers |
|---|---|
| 1. Launch by 12 November | All Phase 1 pages, components, forms (database, email, webhook off), cookie consent, analytics, structured data, redirects, security, content and placeholders, testing |
| 2. After launch | Event detail pages, results filters, online diagnostic booking and payment (if approved), report download, monthly dashboard, CRM webhook on |
| 3. Future (Optional) | English and Chinese language switcher, client login, online sponsorship purchase |

**If not everything is ready by 12 November:**
- **Launch first:** Home, the three audience pages, Asia corridor, Partner with NEXUS, Events, Results, About, Endorsing role, Contact and the legal pages, with the forms, consent, analytics, redirects and every security control.
- **Insights:** can launch as a simple list. The featured insight, filters, report and email sign-up follow within four weeks.

## 13. Still to confirm (Mark's list)

1. Platform, hosting and support terms (developer proposal)
2. Final copy for each page (prototype copy meanwhile)
3. Prices, including the diagnostic fee
4. Inbox addresses and the response-time promise for each form
5. Partner logo permissions: City of London, TEDA, S-Tron, CBBC
6. Online booking and payment for diagnostics (Phase 2)
7. Session series name, venue partner, first date and topic
8. 2027 delegation destinations, dates and price range
9. Endorsing role wording
10. Legal pages and privacy notice
11. Registered office and general email address
12. CRM webhook address
13. Written approval and wording for the Alibaba Entrepreneurs Fund and the Swiss Bluefaer Innovation Centre
14. Tianjin partner names and both MOU dates
15. Email platform for The NEXUS Briefing, and the first insights
16. Also from section 6 and the prototype:
    - founder quote; institution case study or testimonial
    - further photography
    - payments from mainland China
    - "Do you take equity?" (scale-ups FAQ)
    - typical landing programme duration
    - the Doing Business in China 2027 report

## 14. Inconsistencies inside Mark's documents (ask Mark)

| # | Where | Conflict | Build meanwhile |
|---|---|---|---|
| 1 | Brief 3 vs 4.1 | Section 3 lists seven nav items; 4.1 says "six navigation items" | Seven, as listed in section 3 |
| 2 | Home vs Institutions prototype | RidgeCore Ventures is "China" on Home and "Hainan" on Institutions | "China" in cards; ask before using "Hainan" |
| 3 | Guidelines vs Companies House | "Est. 2019" vs incorporated 12 June 2020 | Leave the founding year out until Mark confirms |
| 4 | Live site vs prototype | Live site says the GIA gala is at The Dorchester; the prototype Events page says "[Venue to be confirmed]" | Placeholder, as in the prototype |
| 5 | Prototype vs case study document | Card headlines are shortened on some pages (DarkhorseOne "for the enterprise" vs "built for British business"; Smart Patent with or without "World-class") | Prototype wording on cards; case study document wording on `/results` pages |
| 6 | Prototype vs guidelines | The prototype uses yellow section backgrounds and Google Fonts | Guidelines win (Mark already says so) |
| 7 | Prototype vs brief 4.4 | The prototype Asia page has a Chinese-language block | Remove it (brief) |
| 8 | Case studies | Seven are Ready, but Readii has no page assigned, and its "around double its own revenue" partner-value claim has no stated basis | Show it on `/results` only; ask about the claim |

## 15. Where our documents and designs go beyond Mark

These are proposals. Mark's version is the default until Mark decides otherwise.

| Our proposal | Where | Mark's version (build default) | Status |
|---|---|---|---|
| H1 option B "Land, grow and scale in the UK. From China and beyond." | `02`, `04`, `05`, `06`, canvas note | "Land, grow and scale technology businesses in the UK." | Mark's call; can be tested with Lyssna |
| Eyebrow "The UK–China innovation corridor" | `02`, `06` | "UK growth partner · China flagship corridor" | Mark's call |
| Intro claiming "one accountable team in London, partners on the ground in Tianjin, Shanghai and Hong Kong" | `02`, `05`, `06` | "One accountable team in the UK, with partners on the ground in China." | Corrected: the Hong Kong partner is still in discussion, so the claim overstated it |
| Alternative titles ("UK–China Tech Market Entry & Scale-Up Partner", "…from China & Asia") | `02`, `04`, `06` | The titles in section 10 | Mark's call; Mark's titles stay until then |
| International companies H1 "Reach UK customers sooner." | `04`, `05`, `06` | "Enter the UK with a team already on the ground." ("Reach UK customers sooner" is the Home audience card title) | Corrected in those documents |
| "GB Entrepreneur Awards 2025 finalist" for GI Healthcare | `01` | "Founders named Scotland finalists, Great British Entrepreneur Awards 2025" | Corrected in `01` |
| Archivo and DM Sans | Claude Design canvas (v3.1) | Neutral Face Bold and General Sans, self-hosted | Stand-ins for the design only |
| Porcelain ground, paintings, motion | Hasaan's colour redesign | Plain black, white or Studio Grey; real NEXUS photography; motion on hover and focus only | Breaks written rules; keep it as an exploration |

## Checklist for any page before it goes to Mark

- [ ] Section order matches section 4 for that page
- [ ] H1, eyebrow, intro and button labels are Mark's prototype words
- [ ] Every number, name, price, email and date traces to section 5, 6 or 13; anything else is a `[Placeholder: …]`
- [ ] No yellow backgrounds, no yellow text on white, no white text on grey
- [ ] Alibaba Entrepreneurs Fund and Swiss Bluefaer are text only; the four logos are marked as permission pending
- [ ] No case study mentions visa or endorsement; UKES appears only on the endorsing role page, in the footer and in the visa FAQs
- [ ] Mark's title and meta description from section 10 are in place
- [ ] Form fields use the section 9 keys; consent is not pre-ticked; no reCAPTCHA
- [ ] Fonts are self-hosted; no Google or YouTube requests

## Closing

Mark has already settled most of the questions a designer or developer would otherwise guess at. The open items are in section 13, and the conflicts to raise with Mark are in section 14. Our SEO proposals in section 15 should reach Mark as one short decision list, not as changes already built in.

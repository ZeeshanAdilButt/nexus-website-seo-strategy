# NEXUS: Complete Website, SEO and Tools Knowledge Base

Compiled 06 November 2026 for NotebookLM. This single file contains five documents about NEXUS Creative HQ Ltd
(company no. 12667243), a London company that helps technology businesses land, grow and scale in the UK, with China
as its flagship corridor. It covers: what the business does and sells, its audiences, the current website audit,
how AI assistants describe NEXUS today, the SEO/AEO/GEO strategy, each SEO tool explained, NEXUS's other tools
(Ticket Tailor, Intercom "Ask Fin", Mailchimp, Ghost, Typeform, Zoho, Nexudus, email and DNS), open questions
for the client, and the launch plan for 12 November 2026 ahead of the Global Innovator Awards on 16 November 2026.

Status labels used throughout: Verified = checked against a primary source; Client-stated = from client documents;
Conflict = sources disagree; Gap or To confirm = not yet known.

Contents:
1. Mark's facts: the client's decisions and rules (source of truth)
2. The NEXUS SEO Guide (business, audit, strategy, tools, other systems)
3. Research findings and fact base
4. Website and SEO strategy plan
5. Client pack: message, questions and access list


---

# DOCUMENT 1: Mark's facts: the client's decisions and rules (source of truth)

_Source file: knowledge-base/07-NEXUS-Mark-Facts.md_

# NEXUS: Mark's facts (the source of truth)

| | |
|---|---|
| Date | 4 November 2026; sections 16 to 19 added 5 November from a full re-read of the brief's Word file |
| Scope | Everything Mark has stated in writing about the new site: decisions, page specs, copy, proof, brand, forms, search, technical and launch rules |
| Audience | Everyone designing, writing or building the NEXUS site (Zeeshan, Hasaan, any developer) |
| Sources | `emails-and-meetings/2026-10-31-mark-brief-and-assets/`: the Developer Brief (`NEXUS Website Brief Developer.docx`, text copy in `text-copies/`), prototype copy (`text-copies/prototype/*.txt`), `text-copies/NEXUS Member Case Studies.txt`, `text-copies/NEXUS Brand Guidelines 2025.txt` |
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
| 0. Proposal | **Within two working days of receiving the brief:** recommended platform and hosting, a component inventory, a fixed quote and timeline (including whether 12 November is achievable), and the support and patching terms. Mark supplies the brief, prototype, guidelines and case studies |
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
| 9 | Brief 4.8 vs 7 | 4.8 sets `form_type` to "report or newsletter"; the section 7 list has `report_download` and no newsletter type | Use `report_download` and add `newsletter` for The NEXUS Briefing |

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
| Home H1 "UK–China market entry.", a fourth audience, case study and partner names hidden, details from outside Mark's documents | Hasaan's two drafts | Sections 4, 6 and 7 above | See [`design/reviews/hasaan-wayne/REVIEW.md`](../design/reviews/hasaan-wayne/REVIEW.md) |
| Porcelain ground, paintings, scroll and count-up motion | Hasaan's colour redesign | Plain black, white or Studio Grey; real NEXUS photography; motion on hover and focus only | Breaks written rules; keep it as an exploration |

## 16. The brief itself

| Item | Fact |
|---|---|
| Author | Mark Sarfo-Kantanka. The Word file's author is "NEXUS", last saved by "Mark Sarfo-Kantanka (Creare Capital)". Created and last saved on 25 October 2026 (revision 3). Footer: "NEXUS \| Company Number 12667243" |
| Addressed to | The team that built globalinnovatorawards.com. Mark asks for "the same creative direction and feedback" as on that build, and to "build a new custom website, as you did for the Global Innovator Awards" |
| How to respond | "Use it to scope, quote and plan the work, and come back to us with questions before you assume anything" |
| What Mark supplied | The clickable prototype (the guide to layout, section order and copy; access shared separately), Brand Guidelines 2025 with logo files and fonts, the seven case studies. Photography "will be forthcoming", with placeholders meanwhile |
| In scope | All Phase 1 pages; header and footer; enquiry forms and lead capture; redirects from every current address; security hardening; structured data, analytics and cookie consent; loading approved content and placeholders; testing and handover |
| Links in the brief | NCSC alert on the PHP vulnerabilities: https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php · the GIA site: https://www.globalinnovatorawards.com/ |
| Platform preference | "The approach with the fewest moving parts that we can maintain safely, and pages that are pre-built (static or cached) wherever possible" (principle Approved; our recommendation To confirm). The proposal must say which platform, languages and hosting, how the team edits content, and how the site is kept patched |
| Security confirmation | "As a UK Government supplier with security clearance, we expect these controls to follow the NCSC's guidance and the Cyber Essentials standard. Please confirm in your proposal that they will." |

The text copy in `text-copies/` matches the Word file word for word (checked 5 November). The Word file adds only the two links and the footer above.

## 17. Components to build (brief 4.1)

Build reusable components first, then assemble pages from them, so NEXUS staff can edit content without a developer.

| Component | What it must do | On mobile |
|---|---|---|
| Announcement bar | One line and a link above the header; editable; can be switched off | Wraps to two lines |
| Header | Black, white logo linking home, the nav, Partner with NEXUS, yellow Talk to us; yellow underline on the current page | Logo, Talk to us and a Menu button (keyboard, `aria-expanded`, Escape) |
| Footer | Black, logo, tagline, link columns, contact, social links, legal line | Columns stack |
| Hero | Black or white; eyebrow, H1 in Neutral Face Bold, intro, two buttons, image; breadcrumb on inner pages | Image below the text |
| Proof strip | Up to four statistics and a row of partner logos, managed in the CMS | Two columns; logos wrap |
| Audience cards | Three cards: tag, title, short text, link | Stack |
| Offer card | Tag, title, intro, bulleted inclusions, price line (a CMS field that can say "On application") | Stack |
| Step list | Numbered steps, each with a title and one line | Stack |
| Case study card | Sector tag, company name, one-line headline, main outcome, link to the full case study | Stack |
| Quote block | Founder quote with name, role and company | Full width |
| FAQ accordion | Accessible, and also output as FAQPage structured data | Full width |
| Contact route tiles | Three tiles: title, one line, button | Stack |
| Enquiry form block | Heading, intro, a "What happens next" list, the form | Form below |
| Event card | Image, date, title, description, buttons (CMS collection) | Stack |
| Team member | Black and white portrait, name, role, optional profile | Grid wraps |
| Placeholder | A clearly marked box with "[Placeholder: …]", replaced through the CMS and hidden with a toggle | Same |

**Insights article template (4.8):**
- **Fields:** title, summary, author with photo and role, date, reading time, topic, format, hero image with alt text.
- **Body:** headings, pull quotes, images and embedded video.
- **End of each article:** related case studies and insights, a call to action matched to the topic (Asia corridor articles link to the delegation form), share links.
- **Structured data:** Article, with author and date.
- **Migration:** load the existing articles NEXUS sends (duplicates removed first) and redirect each `/insight/{id}`.

**Form behaviour details (section 7):**
- **Admin access:** submissions can be viewed, filtered and exported only by named NEXUS users.
- **Editable in the CMS:** the acknowledgement email wording and each form's inbox address.
- **Sponsor pack:** the form, then NEXUS emails the pack by hand, or automatically if a PDF can be attached in the CMS.
- **Language switcher (later, Optional):** for example Weglot, with human editing. Keep text out of images, and leave room for one icon in the header.
- **Site search:** not needed at launch.

**Reporting (section 11):**
- **Attribution:** keep the UTM parameters and the first landing page for the visit, and pass them into the hidden form fields.
- **Phase 2 monthly dashboard:** conversions by type, conversion rate per audience page, top landing pages and channels, and Search Console queries for priority pages.

## 18. Acceptance tests (brief 13)

The work counts as complete when every check passes on staging and Mark signs it off. The team sends evidence with it: screenshots, reports and a test log.

| Area | Passes when | How it is tested |
|---|---|---|
| Layout | Every Phase 1 page follows the prototype's section order, content and components, adjusted to the guidelines, at 360, 768, 1280 and 1440px, with no overlap or sideways scroll | Real devices and browser tools |
| Brand | Colours, logo use and type match the guidelines. No Electric Yellow backgrounds | Mark's review |
| Navigation | All links work, no 404s, the mobile menu works by touch and keyboard | Link crawl and a manual check |
| Forms | Each form validates, stores, emails the right inbox within 5 minutes, sends an acknowledgement and records all source fields. Admin export works. The webhook sends correct JSON to a test address | A test submission per form |
| Placeholders | Every placeholder is marked, editable and can be hidden. None looks like final content | Page review |
| Content | Statistics, partner names, logos and case studies match what Mark approved | Mark's sign-off checklist |
| Performance | Mobile Lighthouse 85+ on Home and the audience pages; LCP under 2.5s; CLS under 0.1 | Lighthouse, PageSpeed Insights |
| Accessibility | Lighthouse 95+ on every template; no critical axe errors; full keyboard use; 200% zoom without loss | axe, Lighthouse, a screen reader |
| Mainland China | Home and Asia corridor load fully in under 5s, with no blocked resources | A third-party China speed test |
| Security | Supported, patched versions; no high or critical scan findings; security headers present; 2FA on all admins; a backup restore tested | Scan reports, inventory, header check |
| Privacy | The cookie banner blocks analytics until consent; privacy notice on every form; consent never pre-ticked | Cookie audit |
| Analytics | Every section 11 event fires once per action, only after consent | GA4 DebugView |
| SEO | Unique titles and descriptions, one H1 per page, correct canonicals, valid sitemap, structured data without errors | Crawl tool and validators |
| Redirects | Every old address returns a single 301 to its mapped page | Crawl of the old URL list |
| Browsers | No functional defects in Chrome, Edge, Safari (macOS, iOS), Firefox, Samsung Internet | Manual test matrix |
| CMS | A NEXUS editor can, unaided, edit a statistic, replace a placeholder, add an event, add a case study and change the announcement bar | A live training session |

## 19. Launch and handover (brief 14)

- Live site on NEXUS's domain, with every Phase 1 check passed and signed off.
- Approved content loaded. Any remaining placeholders are agreed with Mark or hidden.
- Redirects live, and checked again after launch.
- Analytics, Google Search Console and Bing Webmaster Tools owned by a NEXUS account, with the sitemap submitted.
- Every admin, hosting, domain, DNS and third-party credential handed over through a password manager, never by email. The team's own access is then reduced to the agreed level.
- A short CMS guide or recorded walkthrough, plus one live training session.
- Technical documentation: platform, component inventory and versions, integrations, form field schema, webhook details, redirect map and analytics events.
- Backups running, with one restore tested.
- A security summary: patch levels at launch, scan results and the patching commitment.
- A defect-fix period after launch [length to agree]. Ongoing support, hosting and maintenance are quoted separately and are not included unless agreed in writing.

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

Mark has already settled most of the questions a designer or developer would otherwise guess at. The open items are in section 13, and the conflicts to raise with Mark are in section 14. Our SEO proposals in section 15 go to Mark as one short decision list, not as changes already built in: the decision list, now folded into section 11 of our 5 November proposal (draft kept in [`_archive/08-NEXUS-Decisions-For-Mark.md`](../_archive/08-NEXUS-Decisions-For-Mark.md)).


---

# DOCUMENT 2: The NEXUS SEO Guide (business, audit, strategy, tools, other systems)

_Source file: plan/04-NEXUS-SEO-Guide.md_

# The NEXUS SEO Guide

> **Mark's documents win.** Where this document differs from Mark's brief or prototype copy, follow [`07-NEXUS-Mark-Facts.md`](../knowledge-base/07-NEXUS-Mark-Facts.md). Its section 15 lists our proposals that still need Mark's decision.

**Understand the business first, then the strategy, then the tools.**
Version 1 · 31 October 2026 · For the NEXUS website rebuild (launch target 12 Nov 2026)

> How to read this guide: Parts 1–2 explain the business and where the site stands. Part 3 explains SEO and AI search *using NEXUS examples*. Part 4 is the strategy. Part 5 explains every SEO tool in plain English and what to do with it for NEXUS. Parts 6–9 are playbooks, keyword lists, schema code and a glossary. Part 10 covers NEXUS's other tools (Ticket Tailor, Intercom "Ask Fin", Mailchimp, Ghost, Typeform, Zoho, Nexudus, email/DNS) and what to fix or decide.
> Companion files: `01` fact base, `02` strategy plan, `03` client pack. Evidence: `knowledge-base/research-answers/`, `knowledge-base/current-site/`.

---

## PART 1: Understand the business (read this before touching any tool)

### 1.1 NEXUS in one sentence
**NEXUS is a London-based company that helps technology businesses from China (and the wider world) set up and grow in the UK, acts as the UK "office" for Chinese science parks and innovation zones, takes UK companies the other way into China and Hong Kong (delegations, partner representation), and helps UK tech scale-ups solve specific growth problems.**

Think of NEXUS as a **bridge with a team standing on it**. Trade bodies and government point at the bridge and give advice. NEXUS walks people across and stays with them on the other side. Hence "boots on the ground" and "one point of accountability".

> **The bridge carries traffic both ways.** The prototype calls it "a working corridor in both directions":
> - **Inbound (China/Asia → UK):** Chinese institutions and tech companies landing in the UK. This is the main revenue focus.
> - **Outbound (UK → China/Asia):** UK companies taking their first step into Asia via Hong Kong, RidgeCore representing NEXUS clients in China, 2027 delegations to mainland China and Hong Kong, and the *Doing Business in China 2027* report (written for UK technology companies looking at China).
>
> In **March 2026 NEXUS opened a company in China** with partners in Beijing and Shanghai (prototype timeline; wording to be confirmed). SEO must cover both directions, and the content plans in this guide do.

### 1.2 How NEXUS makes money

| Who pays | What they buy | Starts with | What it means for SEO |
|---|---|---|---|
| **Innovation institutions**: Chinese science parks, high-tech zones (e.g. TEDA Tianjin), incubators, funds | **UK Representation** (NEXUS = their UK presence); **UK Landing Programmes** for their companies | Partnership call | Few buyers, high value, slow decisions. They ask AI, read reports and check credibility. **Trust + AI answers matter more than volume.** |
| **International tech companies** (mostly Chinese/Asian) entering the UK | **Market-Entry Diagnostic** (paid, credited); **UK Soft Landing** (retainer); **Market Intelligence Report** (fixed fee) | Paid diagnostic | They actively search "how to enter the UK market". **The biggest organic opportunity.** |
| **UK scale-ups** (AI, deep tech, life sciences) | **Growth Diagnostic**, then partner projects (R&D tax, fundraising, AI) | Growth diagnostic | Crowded space. **Win on niche + proof, not volume.** |
| **Professional firms** (law, accountancy, banks, IP) | **Sponsorship** of GIA and sessions; referrals | Sponsor pack | Found via events/LinkedIn. **SEO's job: a credible sponsor page.** |
| **UK companies going to China/Asia** (outbound) | **2027 delegations** to mainland China and Hong Kong; China representation via RidgeCore; the *Doing Business in China 2027* report | Delegation interest form / report request | Searches like "doing business in China", "Hong Kong gateway to Asia", "UK trade mission to China 2027". Less competitive than inbound terms, and **the report is the lead magnet** |

**Traffic magnet, not revenue:** NEXUS is one of six consortium partners of **UK Endorsing Services (UKES)**, a Home Office-approved body endorsing **Innovator Founder visa** applicants. Many people search for visa help, but the brief says to keep it **separate** from sales. Rule: one factual page, no sales buttons.

### 1.3 The buying journey

**A Chinese AI founder in Shenzhen:**
1. Asks an AI or searches: *"How do I set up my AI company in the UK?"* (informational)
2. Reads guides: company registration, banking, visas.
3. Searches *"UK market entry consultancy for Chinese tech companies"* (commercial).
4. Shortlists 3 options; checks case studies, partners, team.
5. Requests a diagnostic (transactional).

**An investment director at a Tianjin science park:**
1. Is told to "internationalise" the park's companies.
2. Asks colleagues, checks CBBC, asks an AI: *"Which UK organisations can represent a Chinese science park in London?"*
3. Looks for **proof**: MOUs, S-Tron, City of London link, a real London address.
4. Books a partnership call.

**A UK robotics scale-up in Manchester (outbound):**
1. Searches *"how to enter the Chinese market as a UK tech company"* or *"Hong Kong as a gateway to Asia"*.
2. Downloads the *Doing Business in China 2027* report.
3. Registers interest in a 2027 delegation (destination: mainland China, Hong Kong or both).

**Lesson:** SEO must cover every stage. Insights win stage 1, audience pages win stage 3, and case studies plus the Asia corridor page win stage 4.

### 1.4 NEXUS's moat (SEO must make this visible)

1. **A working UK–China corridor, in both directions:** RidgeCore Ventures (reciprocal), two Tianjin MOUs (Tianjin co-exhibited with NEXUS at S-Tron), two years at S-Tron Shanghai, CBBC membership and the CBBC delegation to Hangzhou (April 2026), a Shanghai base, and a NEXUS company in China (March 2026, to confirm).
2. **Proof:** 7 case studies, incl. **Sentian Aerospace** (acquired by a listed company in under 2 years) and several Chinese founders now building in the UK.
3. **Owned events:** the **Global Innovator Awards** (16 Nov 2026, The Dorchester), with judges from Barclays, the City of London Corporation, Innovate UK, UCL and CBBC.
4. **Assessment expertise:** 1,400+ business plans assessed.
5. **Delivery, not advice:** project-based, one accountable team.

> **This is the WhatsApp point.** "Land, grow and scale technology businesses in the UK" states the outcome but hides the moat. Search engines and AI reward **specifics**: UK–China, Tianjin, Shanghai, Hong Kong, science parks, soft landing.

### 1.5 Industry vocabulary

| Term | Plain meaning |
|---|---|
| Science park / high-tech zone | Government-backed area housing tech firms (e.g. TEDA; Binhai Zhongguancun Science Park) |
| Soft landing | Practical help for a foreign company's first months: setup, banking, office, first customers |
| Market entry | The whole process of starting to sell in a new country |
| Representation | Someone acting officially for you in another country |
| MOU | Memorandum of Understanding: a signed agreement to cooperate |
| Delegation | Organised group trip of companies/officials |
| CBBC | China-Britain Business Council (NEXUS is a member) |
| DBT | UK Department for Business and Trade ("Invest in UK") |
| TRL | Technology Readiness Level 1–9 |
| Chuhai (出海) | Chinese for "going overseas", used for international expansion |

---

## PART 2: Where the website stands today (audit, 31 Oct 2026)

Data from our own crawl of the live site (`knowledge-base/current-site/page-inventory.csv`, 175 URLs checked) plus Ahrefs figures supplied by the client.

### 2.1 Technical audit: what we measured

| Check | Result | Severity | What it means |
|---|---|---|---|
| Page titles | **All 164 live pages have the same title: "Nexus"** | 🔴 Critical | Google can't tell pages apart, and the title is the strongest on-page signal. Every page competes for "Nexus", a word shared by thousands of companies |
| Meta descriptions | **0 of 164** pages have one | 🔴 Critical | Google invents snippets; low click-through |
| Canonical tags | **0 of 164** | 🟠 High | Host redirects are fine (`http://` and `www.` already 301 to `https://nexuscreativehq.com/`, checked 31 Oct), but without canonicals any parameter or duplicate URL (e.g. the twin articles below) has no "official" version |
| Structured data (JSON-LD) | **None** | 🔴 Critical for AI | No machine-readable "this is NEXUS, a company in London, CEO X, partner Y" |
| XML sitemap | `/sitemap.xml` returns **404** | 🟠 High | Search engines must find pages by crawling links only |
| robots.txt | `Disallow:` (empty), allows everything | 🟢 OK | Fine, but it should list the sitemap |
| Homepage H1 | "Nexus" | 🔴 | The most important heading on the site is a generic word |
| Broken pages | **11 × 404**, served as "Error 404 :: Nexus Admin Panel" | 🟠 | Leaks the admin panel; old nav links point here |
| Broken images | **59 × 404** (+313 not checkable) of 848 image URLs | 🟡 | Many are `/app/{n}/x.png` |
| Open Graph tags | None | 🟡 | Ugly LinkedIn/WhatsApp previews, and LinkedIn is NEXUS's main social channel |
| URL format | `/insight/112`, `/podcast/40` | 🟡 | Numbers say nothing; new site uses `/insights/readable-slug` |
| Duplicate content | e.g. "Women… Growth Advantage" = /insight/111 and /108; "2026 Funding Map" = /101 and /96; "Googleplex" = /71 and /40; "Imposter Syndrome" = /16 and /89 | 🟡 | Splits signals; merge with 301s |
| Image alt text | 179/179 on homepage have alt | 🟢 | Good |

### 2.2 Authority and visibility

| Metric | Value | What it means |
|---|---|---|
| Domain Rating (Ahrefs) | 34 | Respectable for a small firm (benchmark against CBBC, Strategi Global and TusPark in Semrush/Ahrefs before quoting comparisons) |
| Referring domains | 884 | **The main SEO asset.** Other sites trust the domain |
| Organic keywords | 2 (both brand) | Authority isn't connected to any topic buyers search |
| Organic visitors | ~2 per month | Practically invisible in search |

**Diagnosis in one line:** *NEXUS has a strong engine (authority) but no steering (titles, topics, structure) and is driving in the wrong direction (old creative-founder content).*

### 2.3 Content audit: what's on the site

- **101 insight articles**, mostly generic founder advice (pitching, funding, Canva, influencer trends, music). Useful to the old membership audience, **off-topic** for institutions and Chinese tech companies.
- **On-strategy pieces worth keeping:** S-Tron Shanghai takeaways (2025), City of London partnership, funding maps 2026, R&D and patent strategy, regional funding, Hot sectors 2025, TOKEN2049 Singapore.
- **30 podcasts, 15 events, 7 videos:** keep the best as "Founder stories"; redirect the rest.
- **Best on-strategy content lives on another domain:** nexusstartupdiaries.com (Ghost), e.g. "Building a Business in the UK: Conversations With the Founders Choosing Britain", "Manchester and China: the opportunity that keeps on growing".

### 2.4 How AI assistants see NEXUS today (tested with Olostep Answers)

| Prompt | What the AI said | Problem |
|---|---|---|
| "What is NEXUS Creative HQ?" | A "founder-support platform for creative, digital, tech and ESG ventures"; Croydon address; couldn't say who runs it; no China partner; couldn't confirm UKES; confused NEXUS with a different "NEXUS" founded in Tianjin in 2009 | Old positioning; weak, inconsistent entity data; name confusion |
| "Best UK–China market-entry organisations for tech?" | CBBC, DBT China Technology Team, techUK | NEXUS absent from its own category |
| "UK soft-landing providers for Chinese tech companies?" | Strategi Global, CBBC, Invest in UK | NEXUS absent |

**Baseline AI visibility score: 0 out of 3 category prompts.** That's our "before" number.

---

## PART 3: SEO, AEO and GEO explained (with NEXUS examples)

### 3.1 The three kinds of "being found"

| | What it is | Where it happens | NEXUS example |
|---|---|---|---|
| **SEO** (Search Engine Optimisation) | Ranking in the blue links | Google, Bing (and Baidu in China) | Ranking #3 for "UK soft landing programme" |
| **AEO** (Answer Engine Optimisation) | Being the *direct answer* | Google featured snippets, "People also ask", voice | The FAQ answer "What is a UK soft landing?" shown at the top of Google |
| **GEO** (Generative Engine Optimisation) | Being *named or cited* by AI chatbots | ChatGPT, Perplexity, Google AI Overviews, Copilot, DeepSeek | ChatGPT listing NEXUS when asked "who helps Chinese tech firms expand to the UK?" |

They share 80% of the same work: clear pages, a clear entity and credible mentions. The differences are in emphasis.

### 3.2 How Google decides (the 4 pillars, in NEXUS terms)

1. **Crawl and index (technical):** can Google reach and read the page? *NEXUS today: no sitemap, no canonicals, 404s.*
2. **Relevance (content):** does the page match the search? *NEXUS today: every title says "Nexus"; no service pages exist.*
3. **Authority (links and mentions):** do trusted sites vouch for it? *NEXUS today: strong (884 domains), the one thing working.*
4. **Experience (E-E-A-T + UX):** Experience, Expertise, Authoritativeness, Trust. Who wrote it, is it real, does the page load fast? *NEXUS has strong raw material (1,400+ plans assessed, real MOUs, named founders) but none of it is marked up or proven on the page.*

**For NEXUS, B2B + international + money decisions = Google treats it as high-stakes.** Trust signals (real address, company number, named team, case studies with consent, partner logos with permission) are ranking factors, not decoration.

### 3.3 How AI assistants decide (what the evidence says, Oct 2026)

From our Olostep research (`knowledge-base/research-answers/answer_geo_evidence.json`):
- **Third-party mentions** are repeatedly reported as the main signal for ChatGPT recommendations. AI trusts what *others* say about NEXUS (CBBC, City of London, GIA coverage, partner sites, press).
- **Copilot uses Bing's index**: if Bing hasn't indexed a page, Copilot can't cite it. ChatGPT search also leans on Bing. **So Bing Webmaster Tools matters a lot for NEXUS.**
- **Structured data and clear, extractable text** are recommended (no proof they work alone, but they remove ambiguity, which is NEXUS's biggest AI problem).
- **llms.txt:** an SE Ranking study of ~300,000 domains (15 Oct 2026) found **no link** between having the file and being cited. **Don't prioritise it.** (The brief already says "no special AI files".)
- **Wikipedia/Wikidata, Reddit, Quora** appear in AI source mixes. A Wikidata entry for NEXUS is a reasonable low-effort step; Wikipedia requires independent press coverage first.

**For NEXUS specifically:** the AI answer confused NEXUS with another "Nexus". The fix is **entity consistency**: same name, same one-line description, same address, same CEO, same links on the website, LinkedIn, Companies House, CBBC listing, GIA site, Crunchbase, Wikidata and partner sites.

### 3.4 The China dimension (important and often missed)

- **Google is blocked in mainland China.** Chinese decision-makers use **Baidu**, **WeChat** (official accounts and search), **Zhihu** (expert Q&A), **Xiaohongshu/RedNote**, and Chinese AI (DeepSeek, Doubao, Kimi). **Bing (cn.bing.com) works in China.**
- Evidenced Chinese terms for UK expansion: **英国市场准入** (UK market access), **英国公司注册** (UK company registration), **英国出海** (UK expansion), **英国公司设立** (UK company establishment). No volume data yet.
- Chinese B2B buyers check AI summaries, community discussion, media mentions and case studies **before** visiting a company site.
- **What this means for NEXUS:**
  1. The new site **must load in mainland China** (already in the brief: no Google Fonts/Maps/reCAPTCHA/YouTube, Asia CDN).
  2. **Bing matters doubly** (Copilot + China access).
  3. **Phase 2:** a Chinese-language version (the brief allows a switcher), a WeChat official account and Zhihu answers. Partners (RidgeCore, TEDA, S-Tron) publishing about NEXUS in Chinese are worth more than anything on the English site.
  4. Don't over-invest in Baidu SEO for an English .com site: Baidu favours Chinese-language, China-hosted sites. Use partner channels instead.

### 3.5 Search intent: the most important concept for NEXUS keywords

| Intent | The searcher wants… | NEXUS page type | Example |
|---|---|---|---|
| Informational | To learn | Insight / guide | "how to set up a company in the UK from China" |
| Commercial | To compare providers | Audience page, case studies | "UK market entry consultancy for tech companies" |
| Transactional | To act now | Audience page + form | "book UK market entry diagnostic" |
| Navigational | A specific brand | Home / About | "NEXUS Creative HQ", "Global Innovator Awards tickets" |

**Rule:** never try to rank a sales page for an informational query, or a blog post for a commercial one. Google shows what matches the intent.

---

## PART 4: The NEXUS SEO strategy (6 pillars)

### Pillar 1: Own the entity ("NEXUS = the UK–China tech bridge")
**Goal:** every search engine and AI describes NEXUS the same, correct way.
- Use the **approved one-liner everywhere**: *"NEXUS helps technology businesses land, grow and scale in the UK, with China as its flagship corridor."*
- **Name rule:** "NEXUS" in headings; "NEXUS Creative HQ" on first mention on About, Contact, footer and schema (separates NEXUS from the other Nexuses).
- Organization schema with `legalName`, `identifier` (12667243), `founder`, `address`, `areaServed` (GB, CN, HK), `knowsAbout`, `sameAs` (Part 8).
- Align off-site profiles: LinkedIn "About", Companies House SIC codes (optional update), CBBC member directory, Crunchbase, Wikidata, GIA site "About NEXUS", partner websites.
- One email domain (@nexuscreativehq.com). Retire the cellardoornexus address in public profiles.

### Pillar 2: Protect the authority (migration)
**Goal:** keep the value of the 884 referring domains.
- Every one of the 175 old URLs gets **one 301** to its closest new page (Playbook 6.1).
- Priority order: URLs with backlinks (Ahrefs) → core pages → insights → podcasts/events/videos → images with links.
- Keep the existing host rule: today `http://` and `www.` 301 to `https://nexuscreativehq.com/`. The new host must keep exactly this (non-www, https), or every backlink gains an extra hop.
- Monitor 404s daily for 2 weeks after launch.

### Pillar 3: One page per buyer intent (site architecture)
**Goal:** each commercial keyword cluster has exactly one page built to win it.

```
/                          → brand + "UK–China tech market entry partner"
├── /institutions          → UK representation / landing programme for science parks
├── /international-companies → UK market entry / soft landing for tech companies
├── /uk-scale-ups          → scale-up growth diagnostic / advisory
├── /asia-corridor         → UK–China innovation corridor, Hong Kong gateway, delegations
│     └── (Phase 2) /asia-corridor/china, /asia-corridor/hong-kong
├── /results/{company}     → proof (Sentian, GI Healthcare, Auto Impartial…)
├── /insights/{slug}       → informational guides (topic clusters)
├── /events                → Global Innovator Awards, sessions
├── /partner-with-nexus    → sponsors and referral partners
├── /about (+ /about/endorsing-role)
└── /contact
```
**Internal linking rule:** every insight links up to its audience page; every audience page links to Asia corridor, Results and 2+ insights; every case study links to its audience page.

### Pillar 4: Topic authority through Insights (content)
**Goal:** rank for informational queries and become the source AI quotes.

| Cluster | Pillar page (long guide) | Supporting articles | Links to |
|---|---|---|---|
| A. UK market entry from China/Asia (inbound) | "Entering the UK from China: the 2027 Guide" (free pillar page) | How to register a UK company from China · Opening a UK business bank account as a Chinese founder · What a UK soft landing includes and costs · Hong Kong vs direct entry · Choosing a UK city (London, Manchester, Cambridge) · UK tax basics for Chinese tech firms | /international-companies |
| B. Corridors and institutions | "How UK Landing Programmes Work for Science Parks" | The Tianjin MOU story · S-Tron Shanghai takeaways · Planning a delegation to the UK · How to measure an overseas landing programme | /institutions, /asia-corridor |
| C. Scale-up growth | "The UK Deep-Tech Scale-Up Funding Map 2027" | R&D tax relief changes · Series A readiness checklist · Innovate UK collaborative bids (Auto Impartial example) · AI adoption for SMEs | /uk-scale-ups |
| D. International founders in the UK | "Why Founders Choose Britain" (GIA-led) | GIA finalist stories · Founder interviews (from Startup Diaries) · Case study narratives | /results, /events |
| E. UK → China and Asia (outbound) | **"Doing Business in China 2027"** (the brief's gated report; the prototype calls it "our annual guide for UK technology companies looking at China and Hong Kong") | Hong Kong as a gateway: a first step into Asia for UK founders (the prototype's featured insight, by Mark Sarfo-Kantanka) · What a 2027 delegation to China/HK involves · S-Tron Shanghai: what UK exhibitors learned · Manchester and China (from Startup Diaries) · Protecting IP when entering China | /asia-corridor (#delegations), report form |

**Writing rules for every page (AEO/GEO format):**
1. **Answer first:** a 40–60 word direct answer under the H1.
2. **Question headings:** H2s phrased as real questions ("How long does a UK soft landing take?").
3. **Specifics:** numbers, dates, place names, partner names, named experts.
4. **Author box:** a real person with role and photo (E-E-A-T).
5. **FAQ block** (3–5 questions) with FAQPage schema.
6. **Updated date** shown, and refreshed every 6–12 months.
7. **One clear CTA** matched to the topic (A → diagnostic; B → partnership call; C → growth diagnostic; D → GIA/results; E → report download + delegation interest).

### Pillar 5: Earn mentions (off-site authority)
**Goal:** third parties say "NEXUS" next to "UK–China" (the strongest AI signal).

| Source | Action | Effort |
|---|---|---|
| Global Innovator Awards | "Created by NEXUS" + link on the GIA site; press release; finalists' and judges' organisations sharing it | Low, **do in GIA week** |
| CBBC | Member directory listing with the one-liner; contribute to CBBC events/content | Low |
| City of London Corporation | Partnership page/news mention with a link | Medium |
| RidgeCore, TEDA/Binhai, S-Tron, Swiss Bluefaer | Partner page on their sites (English **and Chinese**) linking to /asia-corridor | Medium, very high value for China and AI |
| Case-study companies | "Supported by NEXUS" line + link on their sites (GI Healthcare, DarkhorseOne, Auto Impartial…) | Low |
| UKES | Ask to list consortium partners by name (fixes AI's "can't confirm UKES role") | Low |
| Industry media | Expert comment on UK–China tech (Sifted, UKTN, Tech.eu, China Daily UK, SCMP) | Medium |
| Wikidata, Crunchbase, LinkedIn | Consistent entity profiles | Low |

### Pillar 6: Measure what matters (enquiries, not traffic)
See the KPIs in `02` §8 and the tool setup in Part 5. Monthly report = conversions by audience + non-brand queries + AI visibility score + 404 count.

---

## PART 5: The tools (what they are, what they mean, what to do for NEXUS)

### 5.0 The tool map: which question each tool answers

| Question | Tool | When |
|---|---|---|
| What do buyers search, and who ranks? | Semrush, SparkToro | Before copy is final |
| Which old pages carry our authority? | Ahrefs Webmaster Tools | **Now** |
| Is the message instantly clear? | Lyssna (5-second test) | Before copy is final |
| Is the build technically correct? | Screaming Frog, PageSpeed Insights, Rich Results Test | Staging + launch |
| Do Google and Bing see us, and for what searches? | Google Search Console, Bing Webmaster Tools | **Now** (baseline), then ongoing |
| Do visitors turn into enquiries? | GA4 + Google Tag Manager → Looker Studio | From launch |
| Why don't they convert? | Microsoft Clarity | From launch |
| Do AI assistants name NEXUS? | Olostep + manual prompt checks; Bing AI Performance | Baseline now, then monthly |

**Flow:** Ahrefs (links) → redirect map → Screaming Frog (tests it) → GSC/Bing (confirms Google/Bing accept it) → GA4/Clarity (measure people) → monthly report.
**Ownership rule (brief):** every account is registered to a NEXUS-owned email; we're added as users.

---

### 5.1 Google Search Console (GSC): *"What Google sees and what people search to find us"*
**What it is:** Google's free dashboard for site owners. The **only** source of real Google search data for NEXUS.
**Key concepts:**
- **Impressions** = times NEXUS appeared in results; **Clicks**; **CTR** = clicks ÷ impressions; **Average position**.
- **Query** = the exact words typed. **Brand vs non-brand** = with or without "nexus". *Non-brand growth is the main SEO goal.*
- **Indexing:** pages Google stored. "Crawled – currently not indexed" = seen but judged not worth keeping.
- **Domain property** (verified via a DNS TXT record) covers www, non-www, http and https. Choose this over URL-prefix.

**Set up now:**
1. NEXUS adds a **Domain property** for `nexuscreativehq.com` (DNS TXT) and adds us as Full user.
2. Export **Performance → last 16 months** (queries + pages) = the **pre-migration baseline**.
3. Export **Pages → Not indexed**.

**At launch:** submit `/sitemap.xml`; **URL Inspection → Request indexing** for Home, the 3 audience pages and /asia-corridor; check **Pages** daily for 404 spikes for 2 weeks.
**Monthly:** Performance → Query *doesn't contain* "nexus" → by page. Ask: *Is /international-companies getting impressions for "uk market entry"? Which queries have impressions but CTR < 1%? (Rewrite those titles.)*
**Connects to:** GA4, Bing (import), Ahrefs (verification), Looker Studio.

### 5.2 Bing Webmaster Tools: *"Bing, Copilot, ChatGPT search, and China"*
**What it is:** Microsoft's GSC. **Extra-important for NEXUS:** Copilot only cites pages in Bing's index; ChatGPT search draws on Bing; Bing works in mainland China.
**Key concepts:** **IndexNow** pings Bing instantly when a page changes. The **AI Performance report** shows which pages are cited in Copilot/Bing AI and the **grounding queries** the AI used.
**Set up:** Import from GSC → submit sitemap → enable IndexNow.
**Monthly:** AI Performance → cited pages + grounding queries → turn those queries into FAQs and Insights.
**Limit:** citations, not clicks; Microsoft AI only.

### 5.3 Ahrefs Webmaster Tools (free): *"Which old pages carry our authority?"*
**What it is:** free, owner-verified Ahrefs (real Ahrefs data, own site only).
**Key concepts:**
- **Backlink** = a link from another site. **Referring domain** = a unique linking website (NEXUS: 884). 10 links from one site = 1 referring domain.
- **DR (Domain Rating)** = 0–100 authority (NEXUS: 34). **UR** = the same for one page.
- **Dofollow** links pass authority; **nofollow** mostly don't.
- **Best by links** = your pages ranked by linking sites. **This is the redirect priority list.**

**Do for NEXUS:**
1. Verify via GSC (instant).
2. Site Explorer → **Pages → Best by links** → export **including 404s** → every URL into the redirect map.
3. Referring domains → sort by DR → note the top 20 (gov, university, partner sites). Their target pages must redirect perfectly.
4. After launch: monthly **Site Audit** + **Broken backlinks** → fix with new 301s.

**Optional paid:** Ahrefs Lite ($129/month): competitor research, rank tracking, AI-mention checks. Worth it for 3 months post-launch.

### 5.4 Semrush (free: 10 reports/day): *"What do buyers type, how often, and who ranks?"*
**What it is:** a keyword and competitor research platform.
**Key concepts:**
- **Search volume** = average monthly searches. Use the **UK** database; also check **HK, SG, US** for English-speaking Asian buyers.
- **Keyword Difficulty (KD %)** 0–100. With DR 34, NEXUS can target **KD < 30 now**, **30–50 in 6–12 months**.
- **Intent tags** I / C / T / N (see §3.5).
- **SERP features:** featured snippet, People Also Ask, **AI Overview**. If present, write an answer-first block.
- **Keyword Gap:** terms competitors rank for and NEXUS doesn't.

**Do for NEXUS:**
1. **Keyword Overview** (UK) on the seed list in Part 7 → record volume, KD and intent in a sheet.
2. **Keyword Magic Tool** on "uk market entry", "soft landing uk", "expand to uk", "set up company uk from china", "science park uk partnership" → **Questions** filter → FAQ/Insight ideas.
3. **Domain Overview** on `cbbc.org`, `strategiglobal.co.uk`, `tuspark.co.uk`, `londonandpartners.com`, `uklandingpad.com` → which pages bring them traffic?
4. **Keyword Gap** NEXUS vs 3 competitors → keep KD < 30 with C/T intent.
5. Assign each keyword to **one** page (keyword map, Part 7).

**Watch out:** niche B2B terms often show "0–10" volume. One Tianjin science-park contract is worth more than 10,000 visitors. After launch, GSC impressions are the truth.

### 5.5 Screaming Frog SEO Spider (free ≤ 500 URLs): *"Is every page built right?"*
**What it is:** a desktop crawler that visits every page like Googlebot and lists status, title, H1, canonical, meta, links and images.
**Key concepts:** **status codes** (200 OK; 301 permanent redirect, which passes authority; 302 temporary, *don't use*; 404 not found; 5xx server error); **redirect chain** (A→B→C, slow and leaky; must be A→C); **canonical** (the page's "official" URL); **indexability**.
**Do for NEXUS:**
1. **Crawl staging** (password-protected: Configuration → Authentication) → fix: missing/duplicate titles, ≠1 H1, missing meta, missing canonical, 404 links, images without alt.
2. **List mode → upload all 175 old URLs** (from `knowledge-base/current-site/page-inventory.csv` + Ahrefs) → after launch, every row must be **one 301 → a 200 page**. No chains, no 404s.
3. Save the exports as **acceptance evidence** (brief §13).
**Tip:** this is the tool that found "all 164 pages titled Nexus". Run it on the new site before sign-off.

### 5.6 PageSpeed Insights / Lighthouse (+ China speed test): *"Is it fast and accessible?"*
**Key concepts (Core Web Vitals):** **LCP** (main content loaded, < 2.5 s); **INP** (response to a tap, < 200 ms); **CLS** (layout jumping, < 0.1). Lighthouse scores 0–100 for performance, accessibility, best practice and SEO.
**Do for NEXUS:** test every template on **mobile**. Targets: performance ≥ 85 (Home + audience pages), accessibility ≥ 95. Plus a **mainland China speed test** (e.g. a China-node uptime/speed service): Home and /asia-corridor load in **< 5 s**. *Why:* Chinese institutions are a core audience, and one Google Font or YouTube embed can make a page hang in China.

### 5.7 Rich Results Test + Schema.org Validator: *"Do machines understand who we are?"*
**What it is:** Google's and Schema.org's checkers for structured data (JSON-LD).
**Do for NEXUS:** validate Organization (site-wide), Service (each offer), Event (GIA, sessions), Article (insights, case studies), FAQPage, BreadcrumbList, Person (leadership). Zero errors at launch. Templates are in Part 8.

### 5.8 Google Analytics 4 + Google Tag Manager: *"Who enquires, and from where?"*
**What it is:** GA4 measures visits and actions; GTM is the "container" that loads tracking code without developer changes, here linked to **cookie consent**.
**Key concepts:** **event** (any tracked action); **key event** (an event marked as a conversion); **engagement rate** (visits > 10 s, 2+ pages, or a conversion); **source/medium** (google/organic, linkedin/social, chatgpt.com/referral); **UTM** (tags on campaign links); **Consent Mode** (nothing fires until the visitor accepts).
**Do for NEXUS:**
1. Create the brief's events: `partnership_call_request`, `diagnostic_request`, `sponsor_pack_request` (**key events**), `delegation_interest`, `event_interest`, `general_enquiry`, `report_download`, `cta_click`, `case_study_view`, `outbound_gia_click`. **Add `form_start`** to measure form drop-off.
2. Test each in **DebugView**: it fires once, and only after consent.
3. **Custom channel group "AI assistants"**: referrers matching `chatgpt.com|perplexity.ai|copilot.microsoft.com|gemini.google.com|claude.ai|deepseek.com`. This is how you see AI traffic.
4. Funnels per audience: landing → audience page → form_start → submit.
5. Link GSC; set retention to 14 months.
**China caveat:** GA4 is unreliable in mainland China and needs consent, so **the hidden source fields saved with every form submission are the real record** of where Chinese enquiries came from. (Matomo self-hosted is the privacy-first alternative if needed.)

### 5.9 Microsoft Clarity: *"Why don't visitors enquire?"*
**What it is:** free heatmaps and session recordings.
**Key concepts:** **scroll map** (how far people get; the Home page has 15 sections); **click map**; **rage clicks** (repeated angry clicking); **dead clicks** (clicks on things that aren't links, e.g. partner logos); **quick backs**.
**Do for NEXUS:** install behind consent (required for UK visitors since 31 Oct 2025); mask form fields. **Weekly:** Home scroll depth (do people reach "Asia corridor"?), audience-page recordings of visitors who started a form but didn't submit. **Monthly:** top 3 UX fixes.

### 5.10 SparkToro (free: 3 searches/month): *"Where do our buyers hang out?"*
**What it is:** audience research. Type a topic or a website and it shows which websites, podcasts, social accounts and press that audience follows.
**Do for NEXUS (use the 3 free searches wisely):**
1. "people who visit **cbbc.org**" → China–UK business media and influencers to pitch.
2. "people who talk about **uk market entry**" → publications for guest articles.
3. "people who follow **@innovateuk**" (or similar) → UK deep-tech audience channels.
**Output:** a shortlist of 10 media and podcasts for Pillar 5 (mentions).

### 5.11 Lyssna (free: 15 responses): *"Is the headline clear in 5 seconds?"*
**What it is:** user testing. A **five-second test** shows a screenshot for 5 s, then asks what people remember.
**Do for NEXUS:** test **H1 option A** ("Land, grow and scale technology businesses in the UK.") vs **option B** ("…From China and beyond."). Ask: *"What does this company do?"*, *"Which countries does it work with?"*, *"Who is it for?"* **Pass mark:** ≥ 60% mention China or UK–China unprompted. This settles the WhatsApp debate with data, not opinion.

### 5.12 Looker Studio: *"One monthly report"*
Free dashboard joining GA4 + GSC. **NEXUS monthly page:** (1) primary conversions by type and audience, (2) conversion rate per audience page, (3) non-brand clicks and impressions by page, (4) top landing pages and channels incl. "AI assistants", (5) a manual box: AI visibility score + 404 count.

### 5.13 Olostep (already set up, key in env var): *"Research and AI-visibility monitoring at scale"*
**What it is:** an API that scrapes, maps and crawls sites and returns cited AI answers from live web data. Our helper: `scripts/olostep.py` (`map`, `scrape`, `answer`).
**What we used it for:** mapping all 173 live URLs, the competitor scan, the AI "what is NEXUS?" baseline, market context and China search behaviour.
**Ongoing use for NEXUS:**
- **Monthly AI visibility check:** run the 10 fixed prompts (Playbook 6.4) through `answer` and save them to `knowledge-base/research-answers/`. Did NEXUS appear? Was it described correctly?
- **Competitor watch:** `map` competitor sites quarterly to spot new pages (e.g. a new "China landing programme" page at CBBC).
- **Post-launch QA:** `map` the new site and diff it against the sitemap to find orphan pages.
**Limit:** Olostep's "answers" reflect web evidence at that moment. It approximates AI assistants but is not identical to ChatGPT. Also test manually in ChatGPT, Perplexity, Copilot and Gemini.

### 5.14 Cost summary

| Tool | Cost | Must-have? |
|---|---|---|
| GSC, Bing WMT, Ahrefs WMT, GA4, GTM, Clarity, PageSpeed, Rich Results, Looker Studio | Free | ✅ Yes |
| Screaming Frog | Free ≤ 500 URLs (NEXUS has ~175) | ✅ Yes |
| Semrush free / SparkToro free / Lyssna free | Free with limits | ✅ Before copy is final |
| Ahrefs Lite | $129/month (~$387 for 3 months) | Recommended post-launch |
| Olostep | Existing key | ✅ Already in use |
| Semrush Pro, SparkToro Business, Lyssna Growth, Similarweb | Paid | Optional |

---

## PART 6: Playbooks (step by step)

### 6.1 Redirect map (the most important migration task)
**Inputs:** `knowledge-base/current-site/page-inventory.csv` (175 URLs) + Ahrefs "Best by links" export + the brief's minimum redirects.
**Rules:** one 301 per old URL → its *closest* new page (not everything to Home); no chains; keep query-string variants (`/booking?location=…`) covered.

| Old URL pattern | New URL | Note |
|---|---|---|
| `/purpose` | `/about` | Brief |
| `/memberships`, `/esg`, `/scale-up-journey`, `/investment` | `/uk-scale-ups` | Brief (currently 404 but may have links) |
| `/visa-routes` | `/about/endorsing-role` | Brief |
| `/become-partner` | `/partner-with-nexus` | Brief |
| `/booking`, `/booking?location=*`, `/locations` | `/contact` | Brief |
| `/videos`, `/podcasts` | `/insights` | Brief |
| `/insight/{id}` (kept) | `/insights/{new-slug}` | One-to-one for migrated articles |
| `/insight/{id}` (duplicate) | the surviving twin's new slug | e.g. /insight/108 → slug of /111 |
| `/insight/{id}` (retired, off-topic) | closest topic page, else `/insights` | Never 404 if it has links |
| `/insight/{id}` about S-Tron, China, City of London | migrated, linked from `/asia-corridor` | High value |
| `/event/{id}` | `/events` (or the GIA page for GIA items: event 14, 15) | Event 10 (City of London launch) and 6 (S-Tron 2025) → their migrated insight or `/asia-corridor`. **Event 12 (Innovator Founder ILR masterclass) → `/about/endorsing-role`**, never a commercial page |
| `/podcast/{id}`, `/video/{id}` | founder-story insight, else `/insights` | |
| `/admin/*` | 410 Gone or blocked | Not public |
| `http://`, `www.` | `https://nexuscreativehq.com/…` | Already in place on the old site (non-www, https). Replicate it on the new host and avoid http→www→non-www chains |

**Test:** Screaming Frog list mode with all old URLs → 100% "301 → 200".

### 6.2 Launch-day checklist (SEO)
- [ ] Every page has a unique `<title>` (≤ 60 chars) and meta description (≤ 155 chars)
- [ ] One H1 per page; self-referencing canonical; `lang="en-GB"`
- [ ] `/sitemap.xml` live; `robots.txt` lists the sitemap; staging `noindex` **removed**
- [ ] AI crawlers allowed in robots.txt (GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended, Bingbot)
- [ ] All 301s live; custom 404 links to the 3 audience pages
- [ ] Schema validated (Organization, Service, Event, Article, FAQPage, Breadcrumb)
- [ ] OG images 1200×630 on main pages
- [ ] GSC + Bing: sitemap submitted, key URLs inspected, IndexNow on
- [ ] GA4 events verified in DebugView after consent; Clarity recording
- [ ] Mainland China load test < 5 s on Home + /asia-corridor
- [ ] Live GIA date corrected (16 Nov) everywhere

### 6.3 Writing an audience page (template: `/international-companies`)
1. **Title:** `UK Market Entry for Tech Companies from China & Asia | NEXUS`
2. **H1 (Mark's prototype):** "Enter the UK with a team already on the ground."
3. **Answer-first paragraph (≤ 60 words):** "NEXUS helps international technology companies, especially from China and Hong Kong, enter the UK market. We start with a paid Market-Entry Diagnostic, then provide UK soft landing support: company setup, vetted legal, banking and accountancy partners, qualified introductions and an accountable team in London."
4. H2s as questions: *What does UK market entry involve? · What is included in a UK soft landing? · How long does it take and what does it cost? · Who is it for (and not for)? · What results have we delivered?*
5. Offer cards (Diagnostic / Soft Landing / Intelligence Report) with "On application" pricing.
6. Proof: DarkhorseOne, Eco2Life, Smart Patent cards + one founder quote.
7. Links: /asia-corridor, /results, 2 cluster-A insights.
8. FAQ (5) + form (#start).

### 6.4 Monthly AI visibility check (10 fixed prompts)
Run in ChatGPT (search on), Perplexity, Copilot, Gemini (+ Olostep `answer`). Score 1 if NEXUS is named, 0 if not; note if the description is correct.
1. Who helps Chinese technology companies expand into the UK?
2. What are the best UK soft landing programmes for tech companies?
3. Which UK organisations can represent a Chinese science park in London?
4. UK–China innovation corridor organisations for tech start-ups
5. What is NEXUS Creative HQ?
6. Who organises the Global Innovator Awards?
7. How can a Hong Kong tech company set up in the UK?
8. Market entry consultancy for AI companies entering the UK
9. Who runs NEXUS Creative HQ and what does it do in China?
10. Which organisations are consortium partners of UK Endorsing Services?

**Baseline (Oct 2026): NEXUS named in 0 of 3 category prompts (Olostep only).** Run all 10 prompts × 4 engines manually in the first week to set the real 0/40-style baseline. Target 90 days post-launch: named in ≥ 8 of 40 (10 prompts × 4 engines).

### 6.5 Monthly routine (2–3 hours)
1. GSC: non-brand queries by page; low-CTR titles to rewrite. 2. Bing: AI Performance citations. 3. GA4/Looker: conversions by audience; AI-assistant referrals. 4. Clarity: 5 recordings per audience page. 5. Ahrefs: new and lost links, broken backlinks. 6. AI visibility check. 7. Publish 2 insights from the cluster plan. 8. One outreach action (Pillar 5).

---

## PART 7: Keyword map (seed list, to validate in Semrush/GSC)

Volumes and KD are **not yet validated**. The intent and page assignment are the strategic decision; Semrush fills in the numbers.

| Page | Primary keyword | Secondary keywords | Intent |
|---|---|---|---|
| `/` | UK China tech market entry | NEXUS Creative HQ · UK growth partner for tech companies · UK–China innovation bridge | N / C |
| `/institutions` | UK landing programme for science parks | UK representation for innovation zones · overseas science park UK partner · UK representative office for Chinese incubator · international landing programme UK | C |
| `/international-companies` | UK market entry for tech companies | UK soft landing programme · expand tech company to UK · UK expansion consultancy China · set up UK company from China · UK market entry services | C / T |
| `/uk-scale-ups` | scale-up advisory UK | growth diagnostic for scale-ups · deep tech scale-up support London · R&D tax credit help scale-up · Series A fundraising support UK | C |
| `/asia-corridor` | UK China innovation corridor | UK China tech partnership · Hong Kong gateway to UK · Tianjin UK partnership · China delegation to UK 2027 · S-Tron Shanghai UK | I / C |
| `/results` | UK expansion case studies | [company] + NEXUS · international founder success UK | C |
| `/events` | Global Innovator Awards | GIA 2026 Dorchester · awards for international founders UK · UK China founder events London | N / T |
| `/partner-with-nexus` | sponsor startup awards London | sponsorship international founders UK · referral partnership tech founders | C |
| `/about/endorsing-role` | Innovator Founder endorsement UKES | UKES consortium partner · innovator founder endorsing body | I |
| Insights (cluster A) | how to set up a company in the UK from China | UK business bank account Chinese founder · UK soft landing cost · doing business in the UK guide 2027 · Hong Kong company expand to UK | I |
| Insights (cluster C) | UK deep tech funding map 2027 | Innovate UK collaborative R&D bid · R&D tax relief 2027 · Series A readiness checklist | I |
| Insights (cluster E, outbound) + report | doing business in China 2027 | Hong Kong gateway to Asia for UK companies · UK tech company expand to China · UK trade delegation to China 2027 · S-Tron Shanghai exhibit · China market entry for UK startups | I / C |

**Chinese-language seeds (Phase 2 / partner content):** 英国市场准入 · 英国公司注册 · 英国出海 · 英国公司设立 · 中英科技合作 · 英国落地服务

**Negative / avoid:** "nexus" alone (crowded), "creative hub", "co-working London" (old model), visa-only terms on commercial pages.

---

## PART 8: Structured data templates (JSON-LD)

**Organization (site-wide):** fill the bracketed values once confirmed.
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://nexuscreativehq.com/#organization",
  "name": "NEXUS",
  "alternateName": "NEXUS Creative HQ",
  "legalName": "NEXUS Creative HQ Ltd",
  "identifier": { "@type": "PropertyValue", "propertyID": "UK Companies House", "value": "12667243" },
  "url": "https://nexuscreativehq.com/",
  "logo": "https://nexuscreativehq.com/[logo].png",
  "description": "NEXUS helps technology businesses land, grow and scale in the UK, with China as its flagship corridor.",
  "foundingDate": "[2019 or 2020: confirm]",
  "founder": { "@type": "Person", "name": "Mark Sarfo-Kantanka", "jobTitle": "CEO and Co-Founder" },
  "address": { "@type": "PostalAddress", "streetAddress": "[confirm: 80 Basinghall Street]", "addressLocality": "London", "postalCode": "[EC2V 5AG]", "addressCountry": "GB" },
  "areaServed": ["GB", "CN", "HK"],
  "knowsAbout": ["UK market entry", "UK soft landing", "UK–China technology corridor", "Science park internationalisation", "Scale-up growth"],
  "memberOf": { "@type": "Organization", "name": "China-Britain Business Council", "url": "https://www.cbbc.org/" },
  "sameAs": ["https://uk.linkedin.com/company/nexuscreativehq", "[Instagram]", "[X]", "[Facebook]", "https://globalinnovatorawards.com/", "https://find-and-update.company-information.service.gov.uk/company/12667243"]
}
```

**Service (one per offer):** example.
```json
{ "@context": "https://schema.org", "@type": "Service",
  "name": "UK Soft Landing", "serviceType": "UK market entry support",
  "provider": { "@id": "https://nexuscreativehq.com/#organization" },
  "areaServed": "GB", "audience": { "@type": "BusinessAudience", "audienceType": "International technology companies entering the UK" },
  "url": "https://nexuscreativehq.com/international-companies" }
```

**Event (GIA):**
```json
{ "@context": "https://schema.org", "@type": "Event",
  "name": "Global Innovator Awards 2026", "startDate": "2026-11-16T18:30:00+00:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled",
  "location": { "@type": "Place", "name": "The Dorchester", "address": { "@type": "PostalAddress", "addressLocality": "London", "addressCountry": "GB" } },
  "organizer": { "@id": "https://nexuscreativehq.com/#organization" },
  "url": "https://globalinnovatorawards.com/" }
```
Validate every template in the Rich Results Test before launch.

---

## PART 9: 90-day calendar, quick wins and glossary

### 9.1 Quick wins (this week, on the live site, before the rebuild)
1. Fix the GIA date on the live events calendar (17 Oct → **16 Nov**).
2. Change the live homepage `<title>` from "Nexus" to the new title (if the old CMS allows). That's an instant relevance signal.
3. Verify GSC + Bing + Ahrefs and **export the baselines** (they're lost if the migration happens first).
4. Update the LinkedIn "About" with the one-liner; ask GIA, CBBC and UKES to describe NEXUS the same way.
5. Ask 3 case-study companies to add "Supported by NEXUS" with a link.

### 9.2 90-day calendar

| When | SEO / AEO work |
|---|---|
| Week −2 to 0 (to 12 Nov) | Baselines; keyword validation; titles/meta; redirect map; schema; staging crawl; launch checklist |
| Week 1 (GIA week) | Launch; inspect URLs; daily 404 check; GIA press release + partner amplification (mentions) |
| Weeks 2–4 | Pillar guide A ("Entering the UK from China 2027"); featured insight "Hong Kong as a gateway"; first Looker report; Clarity review |
| Month 2 | Cluster B pillar + Tianjin/S-Tron story; partner pages (RidgeCore, TEDA) link to /asia-corridor; Wikidata + Crunchbase entries; Startup Diaries migration decision |
| Month 3 | Cluster C pillar; *Doing Business in China 2027* report outline (cluster E) with the request form live; title rewrites from GSC CTR data; 2nd AI visibility check; review targets with the client; plan the Chinese-language Phase 2 |

### 9.3 Glossary

| Term | Meaning |
|---|---|
| 301 redirect | Permanent move; passes ~all ranking value to the new URL |
| 404 / 410 | Page not found / gone for good |
| AEO | Answer Engine Optimisation: being the direct answer (snippets, PAA) |
| Anchor text | The clickable words of a link |
| Canonical | Tag naming a page's official URL, to avoid duplicates |
| Core Web Vitals | Google's speed/stability metrics: LCP, INP, CLS |
| Crawl / index | Search engine visits a page / stores it to show in results |
| CTR | Click-through rate = clicks ÷ impressions |
| DR / UR | Ahrefs authority score for a domain / a URL (0–100) |
| E-E-A-T | Experience, Expertise, Authoritativeness, Trust: Google's quality lens |
| Entity | A "thing" search engines recognise (NEXUS the company, Mark Sarfo-Kantanka the person) |
| GEO | Generative Engine Optimisation: being cited by AI chatbots |
| Grounding query | The search an AI runs behind the scenes to find sources |
| hreflang | Tag telling search engines which language version to show (future zh-Hans) |
| Impression | Your page appeared in a search result |
| IndexNow | Protocol to instantly notify Bing/Yandex of page changes |
| Intent | Why someone searches: informational, commercial, transactional, navigational |
| JSON-LD / schema | Machine-readable code describing page facts |
| KD | Keyword Difficulty (0–100) |
| Key event | A GA4 event counted as a conversion |
| Non-brand query | A search that doesn't include "NEXUS" |
| Orphan page | A page no other page links to |
| Pillar / cluster | One long guide + supporting articles that link to it |
| Referring domain | A unique website linking to yours |
| SERP | Search Engine Results Page |
| Sitemap | XML list of all URLs for search engines |
| UTM | Tags on links to track campaigns in analytics |

---

## PART 10: Beyond the website: the other NEXUS tools to figure out or fix

SEO doesn't stop at the website. NEXUS's search and AI visibility, its tracking and its lead data also depend on about 15 other tools. We found them by inspecting the live site, the GIA site (our build), the Startup Diaries blog and public DNS (31 Oct 2026). Full table: `01` §8.

### 10.1 The ecosystem map

| Job | Tool(s) in use today | Where | Status |
|---|---|---|---|
| Main website | PHP/Laravel + Backpack admin | nexuscreativehq.com | Being replaced |
| Awards website | Next.js (our build) | globalinnovatorawards.com | Live |
| Blog | Ghost 6.74 | nexusstartupdiaries.com | Not linked to the main site |
| Tickets | **Ticket Tailor** (GIA); Eventbrite, Luma (older) | buytickets.at/nexus4 | Off-site sales |
| AI chat | **Intercom Messenger + Fin AI agent** ("Ask Fin") | GIA site | Live |
| Newsletters | **Mailchimp** (Cellar Door Nexus account), old-site DB, Ghost members, Brevo (DMARC reports) | Various | 4 lists |
| Forms | Zoho Forms (being dropped), Typeform (GIA nominations), GIA contact form | Various | Moving to own forms + CRM |
| Memberships | Nexudus | nexuscreativehq.spaces.nexudus.com | Probably legacy |
| Email | Microsoft 365 (MX); Zoho + Mailgun in SPF; DMARC p=none | DNS | Needs tightening |
| Analytics | GA4 on GIA (`G-XZZGT7LZ1J`); none found on NEXUS | Both | Inconsistent |
| DNS | one.com (NEXUS, Diaries); Namecheap (GIA) | Registrars | Access needed |
| Partner perk | HubSpot for Startups link | NEXUS homepage | To confirm |
| Podcast | NEXUS Talks (host unknown) | ? | To confirm |
| Future | Own CRM (webhook), Weglot (EN/ZH), diagnostic booking + payment (incl. how **mainland China clients pay**, still open in the prototype FAQ) | Brief / prototype | Not chosen |

### 10.2 What each one means for SEO, AEO and tracking

**Ticket Tailor (GIA tickets)**
- *What it is:* a ticketing platform that hosts checkout on its own domain (`buytickets.at`).
- *Impact:* GIA Event schema already points `offers.url` there (good). But **purchases happen off-site**, so GA4 sees a click, not a sale.
- *Do:* UTM-tag every ticket link (`?utm_source=nexus&utm_medium=website&utm_campaign=gia2026`); enable Ticket Tailor's analytics integration if the plan allows; keep `outbound_gia_click`; after 16 Nov update `eventStatus` and point it at GIA 2027; use Ticket Tailor for NEXUS Sessions too.

**Intercom "Ask Fin" (AI agent on the GIA site)**
- *What it is:* Intercom Messenger with **Fin**, Intercom's AI agent that answers from a knowledge base; our yellow button opens it.
- *Why it matters:*
  1. **Compliance.** Eligibility answers can drift into **visa advice** (breaks the UKES rule). Add a guardrail ("visa endorsement → UKES") and audit the answers.
  2. **Consent.** Intercom sets cookies, so load it after acceptance.
  3. **China.** Third-party chat can be slow or blocked there. Never make Fin the only contact route.
  4. **AEO gold.** Fin's logs show the **real questions visitors ask**. Export the top questions monthly and turn them into FAQs and Insights.
  5. **Cost.** Billed per resolution, so watch GIA week.
- *Decide:* keep it after 16 Nov? Bring it to nexuscreativehq.com in Phase 2 to route institutions, companies and sponsors to the right form?

**Newsletters (Mailchimp, old-site list, Ghost, Brevo)**
- *Problem:* four places hold subscribers, one under the old "Cellar Door Nexus" brand. "The NEXUS Briefing" needs one home.
- *SEO angle:* the list is how new Insights get their first readers, shares and links.
- *Do:* export everything **before switchover** (the old site's `/newsletter/subscribe` list disappears with the old server), merge with consent records, and choose one platform.

**Ghost (NEXUS Startup Diaries)**
- *Problem:* on-strategy content on a separate domain with **zero links to the main site**, titled just "NEXUS".
- *Do (choose one):* (a) migrate into `/insights` with 301s (best for authority), or (b) keep it but add the NEXUS description, link posts to audience pages, and add it to Organization `sameAs`.

**Typeform, Zoho Forms, Nexudus**
- Legacy data holders: **export first, then close.** Replace links to them in migrated content (old posts link to Zoho webinar forms and Nexudus signup). Move legal pages onto the main domain; the current footer "Terms" link points to the wrong Nexudus page.

**Email authentication (SPF / DKIM / DMARC)**
- *Why an SEO guide cares:* every new form must email NEXUS and the enquirer (brief §7). If those emails go to spam, leads are lost and the conversion data is wrong.
- *Do:* list the active senders (M365, Zoho, Mailgun, Brevo); one transactional sender for the new site; DMARC `p=none` → `quarantine` after monitoring; add DMARC to globalinnovatorawards.com.

**Analytics consistency**
- GIA's GA4 appears to load **before consent**. Fix it with Consent Mode.
- NEXUS has no analytics today, so GSC is the only "before" data.
- Decide: one GA4 property with **cross-domain tracking** (to see the GIA → NEXUS journey) or separate properties joined in Looker Studio.

**Entity links between NEXUS properties**
- GIA's JSON-LD names "NEXUS Creative HQ Ltd" as organiser but links to the GIA domain. Set `organizer.url` to `https://nexuscreativehq.com/`.
- Add GIA, Startup Diaries and the podcast to NEXUS's `sameAs`. This tells Google and AI that the awards, blog and company are one entity, which directly fixes the AI confusion in Part 2.

**Old platform security**
- The live site runs PHP/Laravel (Backpack admin) and exposes admin paths. The NCSC PHP alert applies **now**, not only to the new build. Lock it down until launch, then decommission it.

**GIA llms.txt (stale)**
- The GIA site has an llms.txt summary file. It still says nominations are "open now" (they closed in August) and tickets are an "early-bird waitlist" (they're on sale). Update it before GIA week, and again afterwards.
- This doesn't contradict Part 3's advice: llms.txt shows no proven citation benefit, so don't *add* one to NEXUS. But if a file exists, wrong facts in it are a liability.

**Also to confirm:** HubSpot for Startups link (keep as a perk?), NEXUS Talks podcast host (Spotify/Apple/YouTube + RSS), Google Business Profile / Crunchbase / Wikidata entries, and future choices: CRM, Weglot, payment provider.

### 10.3 Pre-switchover data checklist
- [ ] Export the old-site newsletter subscribers
- [ ] Export Zoho Forms submissions (enquiry, webinar, S-Tron webinar)
- [ ] Export Typeform GIA nominations
- [ ] Export Nexudus members (if any)
- [ ] Export Mailchimp + Ghost members (for the merge)
- [ ] Ticket Tailor attendee list after GIA (CRM + GIA 2027 waitlist)
- [ ] Intercom/Fin: top conversation topics (FAQ input)
- [ ] Record DNS settings at both registrars before any change

---

### Evidence index

- Live-site crawl: `knowledge-base/current-site/page-inventory.csv`, `image-status.json`, `external-links.json`, `robots.txt`
- Olostep: `knowledge-base/research-answers/map_nexuscreativehq.json`, `answer_brand_aeo_nexus.json`, `answer_competitors_*.json`, `answer_keywords_intent.json`, `answer_aeo_category.json`, `answer_market_context.json`, `answer_nexus_press.json`, `answer_geo_evidence.json`, `answer_china_search_behaviour.json`
- Client docs: Developer Brief, Tool Guide, Brand Guidelines 2025, Member Case Studies, prototype, `seo finding.txt`, `undersatding of seo resource.docx`
- Public: Companies House (12667243), ukesapp.co.uk, globalinnovatorawards.com, nexusstartupdiaries.com


---

# DOCUMENT 3: Research findings and fact base

_Source file: knowledge-base/01-NEXUS-Research-Findings.md_

# NEXUS: Research Findings (fact base)

Compiled 31 October 2026. Sources: Mark's files in `emails-and-meetings/2026-10-31-mark-brief-and-assets/` (Developer Brief, Brand Guidelines 2025), Nazia's files in `knowledge-base/nazia/` (SEO understanding doc, prototype `seo lady draft.html`, `seo finding.txt`), `plan/NEXUS Website Tool Guide.pdf` and `emails-and-meetings/2026-10-31-questions-for-mark.txt`, live site crawl (Olostep map + page fetches), Companies House, UKES, globalinnovatorawards.com, nexusstartupdiaries.com, Olostep Answers. Raw Olostep outputs: `research/raw/`.

Status key: **Verified** (primary source) · **Client-stated** (client docs, not independently checked) · **Conflict** (sources disagree) · **Gap** (no evidence found).

---

## 1. Business snapshot

| Item | Finding | Status / source |
|---|---|---|
| Legal entity | NEXUS CREATIVE HQ LIMITED, no. 12667243, private limited, Active | Verified: Companies House |
| Incorporated | 12 June 2020 | Verified: Companies House |
| "Est. 2019" | Brand guidelines + SEO doc say founded 2019 | **Conflict** with incorporation date; confirm wording |
| Registered office | Kings Parade, Lower Coombe Street, Croydon, CR0 1AA | Verified. Prototype footer still says "[to be confirmed]" |
| UK operating address | SBREC, 80 Basinghall Street, London EC2V 5AG | Live /locations |
| Other locations | Shanghai (Swiss Bluefaer Innovation Centre, No. 1800 Huangxing Road); Accra (Impact Hub Accra) | Live /locations. **Accra missing from prototype**: keep, drop or move to "network"? |
| SIC codes | 62020 IT consultancy; 82110 office admin; 90040 arts facilities | Verified. Reflect the old creative-hub model |
| CEO | Mark Sarfo-Kantanka (CEO and Co-Founder) | Live site + prototype |
| Team | Grace Mander, Jonny Quirk, Kolos Sipos, Mauria Fransishku, Sheleene Sealy, Zee West | Live /purpose |
| Advisors / mentors | Alan Greenberg (Board Advisor) + 11 mentors | Live /purpose |
| Mission | "Most trusted operational bridge between the UK and the world's most dynamic innovation ecosystems" | Brand Guidelines 2025 |
| Positioning lines | "Not a generic accelerator." "Boots on the ground." "One point of accountability." | Live /purpose |
| Public email | members@cellardoornexus.co.uk (Facebook) | **Conflict**: other domain. Use one @nexuscreativehq.com address everywhere |

## 2. What NEXUS sells

| Live-site service line | New offer (brief) | Audience | Entry action |
|---|---|---|---|
| Cross-Border Ecosystem Bridge | UK Representation; UK Landing Programme; 2027 delegations | Innovation institutions (science parks, zones, hubs, funds, universities) | Book a partnership call |
| Market Entry & Representation | Market-Entry Diagnostic (paid, credited); UK Soft Landing (retainer); Market Intelligence Report (fixed fee) | International tech companies entering the UK | Request a paid diagnostic |
| UK Scale-Up Advisory & Partner Network | Growth Diagnostic; partner-delivered projects (AI, R&D tax, Seed/Series A) | UK frontier-tech scale-ups | Request a growth diagnostic |
| Events / awards | Session + GIA sponsorship; referral partnerships | Law, accountancy, banking, IP firms | Request the sponsor pack |
| Visa | Endorsing role page only, no commercial CTA | Innovator Founder applicants | Go to UKES |

Prices: none confirmed ("On application").

## 3. Proof assets

**Stats (client-stated):** 100+ businesses actively supported · 16 curated global partnerships · 1,400+ business plans assessed · "Supplier and security cleared" (**Gap**: needs a citable reference).

**Case studies (7, currently "Private & Confidential", so written consent is needed for each):**

| Company | Sector | Headline outcome | Best page |
|---|---|---|---|
| Sentian Aerospace | Aerospace / UAV | Acquired by Volatus Aerospace (listed) < 2 yrs from UK incorporation | UK scale-ups / Home |
| GI Healthcare | Deep tech | Customer-funded PoC; founders named Scotland finalists, Great British Entrepreneur Awards 2025 | UK scale-ups |
| Auto Impartial | AI compute | Architecture validated; UK–Asia consortium with Innovate UK | Asia corridor |
| DarkhorseOne | AI enterprise software | UK patent filed; commercial collaboration via NEXUS | International companies |
| Eco2Life (EcoDo) | CreaTech | Live AI platform, early revenue | International / Asia |
| Smart Patent | Legal tech | Finalist, national AI programme in China; UK–China raise | International / Asia |
| Readii | EdTech | Revenue in 2 yrs (partner-value claim **needs evidence**) | TBC |

**Asia corridor:** RidgeCore Ventures (reciprocal; logos in `Partner Logos/LOGO设计`) · two Tianjin MOUs (prototype FAQ names Binhai Zhongguancun Science Park; dates TBC) · S-Tron Shanghai (2025 exhibiting, 2026 speaking) · CBBC membership · City of London Corporation partnership · Alibaba Entrepreneurs Fund + Swiss Bluefaer (**names only until approved**).

**Flagship event:** Global Innovator Awards, 16 Nov 2026, The Dorchester. Created/powered by NEXUS, endorsed by the Global Entrepreneur Programme; 10 categories, 100 finalists. Judges from Barclays Innovation Banking, City of London Corporation, Innovate UK Business Connect, UCL, CBBC. **Conflict:** the live NEXUS events calendar shows 17 Oct.

## 4. Current digital footprint

| Metric | Value | Source |
|---|---|---|
| Domain Rating / referring domains | DR 34 / 884 | Client SEO doc (Ahrefs) |
| Organic keywords / traffic | **2 / 2 users** (brand terms only) | Same |
| Social | LinkedIn 1,308 · Instagram 2,466 · X 227 · Facebook 171 | Same |
| URLs on live site | **173**: 101 `/insight/{id}`, 30 `/podcast/{id}`, 15 `/event/{id}`, 7 `/video/{id}`, 4 `/booking*`, core pages | Olostep map (`research-answers/map_nexuscreativehq.json`) |
| Broken | 11 pages + 77 images return 404 (`seo finding.txt`); our own check found 59 image 404s plus 313 not checkable, so the counts differ by method. Use the Ahrefs/Screaming Frog crawl as the final list | `seo finding.txt`, `current-site/image-status.json` |
| Third-party pages | Legal/login on Nexudus subdomain; forms on Zoho (being dropped) | `seo finding.txt` |
| Blog | nexusstartupdiaries.com (Ghost), active Sep–Oct 2026, on-strategy topics (UK founders, Manchester–China) | Live fetch |
| Host redirects | `http://` and `www.` already 301 to `https://nexuscreativehq.com/` | Verified (curl, 31 Oct) |
| Old events with links | 15 `/event/{id}` pages incl. GIA (14, 15), City of London partnership launch (10), S-Tron Shanghai 2025 (6), TOKEN2049 (8), NEXUS x SLUSH (2), an Innovator Founder ILR masterclass (12) | Crawl. Event 12 is visa content, so redirect it to `/about/endorsing-role` or `/insights`, never to a commercial page |

**Key insight:** strong link equity, near-zero topical relevance. About 150 legacy URLs (old creative-founder content) carry the backlinks, so the **301 redirect map is the most valuable SEO task of the migration**. The freshest on-strategy content sits on another domain.

## 5. How AI engines see NEXUS today (AEO audit, Olostep Answers)

Asked "What is NEXUS Creative HQ?", the AI answer engine:
- described it as a **founder-support platform for creative, digital, tech and ESG ventures** (old positioning);
- listed a **Croydon** address and found no London office;
- **could not confirm who runs it** (it surfaced a founder-spotlight name, Danyi Chen, instead of the CEO) and named no China partner, although it did repeat "China as its flagship corridor" from the site;
- **could not confirm the UKES relationship** (UKES's site doesn't list consortium members);
- picked up an unrelated "NEXUS group founded in Tianjin in 2009" (**entity confusion**: the name "Nexus" is shared by many organisations).

Asked "best UK–China market-entry organisations for tech", it named **CBBC, DBT China Technology Team, techUK**, not NEXUS.

**This confirms the WhatsApp feedback:** the generic headline plus thin, inconsistent entity data means AI engines don't connect NEXUS to its biggest asset, the UK–China corridor.

## 6. Competitive landscape

| Type | Examples | NEXUS angle |
|---|---|---|
| China trade bodies | CBBC (NEXUS is a member), DBT China Tech Team, techUK | Complementary: they do policy and networks, NEXUS does hands-on delivery |
| China-linked UK parks/incubators | TusPark UK (Cambridge, Newcastle), Cocoon Networks, UK-China Business & Innovation Hub (Suzhou) | They offer space; NEXUS offers representation and operations |
| Soft-landing consultancies | Strategi Global, UK Landing Pad (Indonesia focus), OCO Global | Generic; NEXUS has corridor partners and its own events |
| City/government inward investment | London & Partners, Invest in UK (DBT) | Free but not hands-on; NEXUS can be the execution partner |
| Law/accounting China desks | DAC Beachcroft, Chan Neill, WilmerHale | Referral partners/sponsors, not competitors |
| Hong Kong gateway | InvestHK, HKSTP | Partners for the "Hong Kong gateway" story |

**Gap:** no keyword-volume or ranking data yet. Needs Semrush/Ahrefs plus the client's answer to "who do you lose business to?"

## 7. Market context (dated)

- Jan 2025: 11th UK–China Economic and Financial Dialogue; priority sectors clean tech, life sciences, digital, financial services.
- Jan 2026: PM Starmer visits China; long-term "comprehensive strategic partnership" agreed.
- 2025: Chinese outbound investment into EU+UK reportedly up 67% to €16.8bn (combined figure, not UK-only).
- Jun 2025: InvestHK positions Hong Kong as a gateway; UK is HK's 2nd-largest source of international startup founders.
- Year to Jun 2026: 221 Innovator Founder visas issued to main applicants outside the UK (+15%).

These support timely insight content ("Entering the UK from China 2027", "UK–China tech corridor 2026") and the outbound report *Doing Business in China 2027* (for UK companies looking at China and Hong Kong).

### 7b. The corridor runs both ways (from the prototype pages)
- Home: "A working corridor in both directions". RidgeCore represents NEXUS clients in China; NEXUS represents RidgeCore's clients in the UK.
- Asia corridor timeline: **2025** first Tianjin MOU · **2025** S-Tron Shanghai (NEXUS and Tianjin co-exhibited, bringing UK companies to Shanghai) · **March 2026 "NEXUS opens in China"** (a NEXUS company in China with partners in Beijing and Shanghai; wording TBC) · **April 2026** CBBC delegation to Hangzhou (AI, robotics, life sciences) · **2026** S-Tron (speaking) · **2026** second Tianjin MOU.
- **2027 delegations** to mainland China and Hong Kong for UK companies (customers, manufacturing partners, investment, research partnerships).
- *Doing Business in China 2027* report: "our annual guide for UK technology companies looking at China and Hong Kong".
- Past events also include **TOKEN2049 Singapore (30 Sep 2025)**, so Singapore is already part of the Asia story.
- Open questions in the prototype: **payment arrangements for clients in mainland China**; the diagnostic **booking and payment tool**; response-time service levels.

**Implication:** the outbound direction is a second audience (UK companies going to Asia) with its own SEO cluster and lead magnet. It was under-represented in v1 of these documents.

## 8. The wider digital ecosystem (other tools to figure out or fix)

Found 31 Oct 2026 by inspecting the live NEXUS site, globalinnovatorawards.com (our build), nexusstartupdiaries.com, `current-site/external-links.json` and public DNS. **Verified** = seen in code, links or DNS. **To confirm** = ask the client.

### 8a. Events, tickets, chat and email capture

| # | System | What we found | Issue / risk | Action |
|---|---|---|---|---|
| 1 | **Ticket Tailor** (GIA tickets) | GIA "Buy Tickets" → `buytickets.at/nexus4/2408591` (Ticket Tailor). Finalists get discount codes; Event schema `offers.url` points there. Verified | Sales happen off-site, so GA4 can't see revenue or conversions | UTMs on every ticket link; Ticket Tailor analytics integration; track `outbound_gia_click`; update Event schema after 16 Nov |
| 2 | **Eventbrite + Luma** | Old event links (Eventbrite "NEXUS Networking…", `luma.com/lht09ucl`). Verified | 3 ticketing tools means scattered attendee data | Standardise NEXUS Sessions on one platform (Ticket Tailor) |
| 3 | **Intercom "Ask Fin"** (AI agent, GIA site) | The yellow "Ask Fin" button opens **Intercom Messenger** (Fin = Intercom's AI agent), loaded site-wide. Verified | (a) Seems to load **before cookie consent**. (b) Must **never give visa advice** (UKES separation). (c) Pay-per-resolution cost. (d) May be slow/blocked in China. (e) Knowledge goes stale after 16 Nov | Gate behind consent; audit Fin's sources and answers; visa guardrail; refresh after GIA; decide whether Fin comes to nexuscreativehq.com (Phase 2) |
| 4 | **Mailchimp** (GIA newsletter) | Form posts to `cellardoornexus.us18.list-manage.com`. Verified | List under the **old "Cellar Door Nexus" account** | Pick one platform for "The NEXUS Briefing"; merge lists with consent; rename the account |
| 5 | **Main-site newsletter** | `/newsletter/subscribe` saves to the old site's own database. Verified | **Subscribers lost at migration** unless exported | **Export before switchover** |
| 6 | **Ghost** (Startup Diaries) | Ghost 6.74 with members/newsletter; title "NEXUS"; **0 links to nexuscreativehq.com**. Verified | A 4th email list; split authority | Migrate to /insights (301s) or add links + a consistent description |
| 7 | **Typeform** (GIA nominations) | `zztxkve7k7f.typeform.com/innovatorawards`. Verified | Nominee data held in Typeform | Export to the future CRM; reuse for the GIA 2027 waitlist |
| 8 | **Zoho Forms** | Enquiry, Webinar and S-Tron webinar forms + 4 `zfrmz.eu` short links. Verified | Brief says **no Zoho**; old posts link to these | Export submissions; replace links; close after launch |

### 8b. Platforms, email delivery, analytics and domains

| # | System | What we found | Issue / risk | Action |
|---|---|---|---|---|
| 9 | **Nexudus** (old membership platform) | "My Account"/signup + legal pages on `nexuscreativehq.spaces.nexudus.com`; the footer "Terms" link goes to the Nexudus index (**wrong link**). Verified | Old membership model; legal pages off-domain | Confirm whether memberships still exist; retire; move legal pages to `/privacy`, `/terms`, `/cookies` |
| 10 | **HubSpot for Startups** | Partner-code link on the homepage. Verified | A perk partnership or leftover? | **To confirm**: keep as a partner perk or remove |
| 11 | **Email sending stack** | MX = **Microsoft 365**; SPF includes **Outlook + Zoho + Mailgun**; DMARC `p=none` → **Brevo** reports. GIA domain: Namecheap forwarding, **no DMARC**. Verified | Form notifications and acknowledgement emails (brief §7) may land in spam; GIA domain spoofable | Map senders; one transactional sender for the new forms; DMARC → quarantine; add DMARC to GIA |
| 12 | **Domains / DNS** | nexuscreativehq.com + nexusstartupdiaries.com at **one.com**; globalinnovatorawards.com at **Namecheap**. Verified | Two registrars; DNS access is needed for GSC verification and the switchover | Get logins via a password manager; document them in the handover |
| 13 | **Current main-site platform** | **PHP / Laravel + Backpack admin 4.1.69**; 404s say "Nexus Admin Panel"; `/admin/page/podcast/@tomych` exposed. Verified | The NCSC PHP alert (brief §9) applies to the **live old site** until replaced | Lock down/patch until launch; decommission after |
| 14 | **GA4 on the GIA site** | `G-XZZGT7LZ1J` fires in `<head>`; the cookie banner only stores the choice. Verified (code) | Analytics likely **before consent** (UK GDPR/PECR) | Consent Mode / gate gtag; decide on one shared GA4 property (cross-domain) or separate |
| 15 | **GIA → NEXUS entity link** | GIA JSON-LD `organizer` = "NEXUS Creative HQ Ltd" but `url` = the GIA domain | Doesn't connect the two entities for Google/AI | Set organizer `url` to `https://nexuscreativehq.com/`; add `sameAs` |
| 15b | **GIA llms.txt is out of date** | Still says nominations "Open now, close August 2026" and Tickets = "early-bird waitlist"; venue "Central London". Verified 31 Oct | AI tools may repeat stale facts in GIA week (tickets are on sale; finalists announced; venue = The Dorchester) | Update now; again after 16 Nov (results, GIA 2027). Note: the NEXUS brief says no special AI files are needed on the **NEXUS** site; this file is on GIA only |
| 16 | **Main-site analytics today** | No GA/GTM found on the NEXUS homepage. Verified | **No traffic baseline** | Verify GSC now (its data is the only "before" picture) |
| 17 | **NEXUS Talks podcast** | Logo in brand assets; 30 `/podcast/{id}` pages | Audio host unknown | **To confirm**: Spotify/Apple/YouTube, RSS → link from /insights |
| 18 | **Future tools (brief)** | Own CRM (webhook), Weglot (EN/ZH), Phase 2 diagnostic booking + payment, email platform for the Briefing | Not chosen | Keep the form schema stable; choose payment + email providers; plan hreflang |
| 18b | **Payments from mainland China** | The prototype FAQ "How are payments from mainland China handled?" is unanswered; the booking/payment tool is "to be confirmed" | Card checkout alone may not work for Chinese institutions | **To confirm**: invoice/bank transfer, Alipay/WeChat Pay via a provider, or RidgeCore-invoiced |
| 19 | **Google Business Profile, Crunchbase, Wikidata** | Not checked | Entity/trust signals | **To confirm** whether they exist; claim and align |

**Bottom line:** NEXUS runs on about **15 separate tools**. Several hold customer data (4 email lists, Typeform, Zoho, Ticket Tailor, Intercom), and some use an old brand (Cellar Door Nexus). The website rebuild is the moment to decide **one email platform, one ticketing platform, one forms/CRM path and one analytics standard**, and to export data before anything is switched off.


---

# DOCUMENT 4: Website and SEO strategy plan

_Source file: plan/02-NEXUS-Website-SEO-Strategy-Plan.md_

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


---

# DOCUMENT 5: Client pack: message, questions and access list

_Source file: emails-and-meetings/2026-10-31-03-Client-Pack-What-To-Send.md_

# What to send the client (NEXUS)

## A. Message (copy, edit, send)

> Hi Mark and team,
>
> Thanks for the brief and documents. We've studied them alongside your live site, Companies House, the GIA site and how AI assistants (ChatGPT/Perplexity-style engines) currently describe NEXUS.
>
> **Four things stood out:**
> 1. **Strong authority, almost no visibility.** About 884 websites link to nexuscreativehq.com, but the site ranks for only two brand terms. Most of those links point to ~170 old addresses (insights, podcasts, events), so the redirect plan at launch is the single most valuable SEO task. We'll protect every linked address.
> 2. **AI engines don't yet credit NEXUS for its China work.** When we asked an AI engine "What is NEXUS Creative HQ?", it described the old creative-founder hub and gave the Croydon registered address. It repeated "China as flagship corridor" from your site but couldn't name a single China partner or confirm your UKES role. It also picked up an unrelated "NEXUS" said to have been founded in Tianjin in 2009. Asked for the best UK–China market-entry organisations, it named CBBC, DBT and techUK. We'll fix this by putting the UK–China corridor into the page titles, intro text, structured data and partner mentions, while keeping your bold headline.
> 3. **Quick fixes on the live site now:** the events calendar shows the GIA gala on 17 Oct (should be 16 Nov); 11 pages and dozens of images return errors (59–77, depending on the check); and the GIA site's AI summary file (llms.txt) still says nominations are "open now" and tickets are an "early-bird waitlist".
> 4. **Your wider toolset needs a plan too.** Beyond the website, NEXUS runs on about 15 tools (Ticket Tailor, Intercom's "Ask Fin", Mailchimp, Ghost, Typeform, Zoho, Nexudus and others), with four separate email lists. Before the old site goes, we need to export that data and agree one platform for each job (see questions 14–24). We'd also like to confirm how much weight to give the outbound side of the corridor (UK companies going to China and Hong Kong), which your prototype highlights (questions 25–26).
>
> Our strategy draft is attached. To finalise it, we need the answers below (about 20 minutes; questions 1–6 matter most) and the accesses in section C. The first four (Search Console, GA4, Bing, Ahrefs) are needed this week.
>
> Thank you!

## B. Questions (priority order)

**Must answer before copy is final**
1. **Keywords:** If your ideal client searched Google or asked ChatGPT for a business like NEXUS, what 3–5 phrases would they use? Which phrases do you want to own? (Our starting list: "UK market entry for tech companies", "UK soft landing programme", "UK representation for science parks", "UK–China innovation corridor".)
2. **Competitors:** Which 3 organisations are you compared with or lose business to? (We found CBBC, DBT, London & Partners, TusPark UK, Strategi Global. Are any of these partners rather than competitors?) Any website you admire?
3. **Priority:** Which brings the most revenue: institutions, international companies or UK scale-ups? Which do you want more of in the next 6 months?
4. **Markets:** Beyond mainland China, which countries should enquiries come from (Hong Kong, Singapore, Ghana/Accra, others)? Should Accra stay on the site (it's on the live site but not in the prototype)? Is the Shanghai address (Swiss Bluefaer Innovation Centre) still current, given the brief says to name Swiss Bluefaer only once approved?
5. **Visa searches:** We recommend one factual Endorsing-role page with no sales call to action. It keeps the search authority without filling your forms with visa-only enquiries. Agree?
6. **Success:** Which single enquiry matters most (partnership call, paid diagnostic, sponsor pack, delegation)? What would a good result look like at 90 days? (We suggest 8–12 qualified enquiries a month.)

**Facts to confirm (affect trust and AI accuracy)**

7. Founded **2019** or **2020**? (Brand guidelines say Est. 2019; Companies House says incorporated 12 June 2020.)
8. Address to publish: the registered office (Croydon) and/or the operating address (80 Basinghall Street)?
9. One public email on the @nexuscreativehq.com domain? (Facebook currently shows a @cellardoornexus.co.uk address.)
10. Headline option: keep "Land, grow and scale technology businesses in the UK." or test "Land, grow and scale in the UK. From China and beyond."?
11. A citable reference for "Supplier and security cleared"; Tianjin MOU partner names and dates; approval to name the Alibaba Entrepreneurs Fund and Swiss Bluefaer.
12. Written consent for each of the seven case studies and founder quotes.
13. **NEXUS Startup Diaries:** may we move it into /insights on the main domain (with redirects)? Two domains split your authority.

## B2. Your other tools (beyond the website)

While reviewing the site we mapped about 15 tools NEXUS uses. Some hold enquiries, subscribers and attendees, so we need to decide what happens to each **before** the old site is switched off.

**14. Tickets: Ticket Tailor (GIA).** Ticket sales happen on Ticket Tailor, so our analytics can't see them. May we add tracking links and connect Ticket Tailor's analytics? Should future NEXUS Sessions also use Ticket Tailor (instead of Eventbrite/Luma)?

**15. "Ask Fin" chat on the GIA site (Intercom's AI agent).**
- Should Fin stay after 16 Nov, and should it come to the new NEXUS site?
- Who maintains its answers?
- We recommend it never answers visa questions (it should point to UKES) and only loads after cookie consent.

**16. Newsletters.** We found four separate lists:
- Mailchimp (GIA, under the old "Cellar Door Nexus" account)
- the old website's own subscriber list
- Ghost (Startup Diaries)
- possibly Brevo

Which one should power "The NEXUS Briefing"? May we export and merge them, keeping consent records?

**17. Forms and data to export before switchover.**
- Zoho Forms submissions (enquiry, webinar, S-Tron)
- Typeform GIA nominations
- the old site's newsletter subscribers
- Nexudus member accounts

Who can export these?

**18. Nexudus (memberships).** Do paid memberships or coworking bookings still exist? If not, we'll retire the Nexudus links and host the legal pages on the main site.

**19. Email deliverability.**
- Your domain sends email via Microsoft 365, Zoho, Mailgun and Brevo. Which are still used?
- The new forms will email you and your enquirers, so we need one reliable sender and a stricter anti-spoofing (DMARC) setting.
- The GIA domain has no DMARC record.

**20. HubSpot for Startups link.** Is this an active partner perk to keep, or can it go?

**21. NEXUS Talks podcast.** Where is the audio hosted (Spotify, Apple, YouTube)? We'll link it from Insights.

**22. Analytics on the GIA site.** It currently appears to load Google Analytics before visitors accept cookies. May we fix that, and should GIA and NEXUS share one analytics account?

**23. Profiles.** Do you have a Google Business Profile, Crunchbase or Wikidata entry? We'd like to align them with the new description.

**24. Payments and booking.** The prototype leaves the diagnostic "booking and payment tool" open, and asks how payments from **mainland China** clients are handled. Which tools do you use or prefer (for example Stripe or invoices for UK clients; bank transfer, Alipay or WeChat Pay for China)? This decides what the Phase 2 booking flow needs.

## B3. The UK–China corridor in both directions

**25. Outbound.** Your prototype describes "a working corridor in both directions": UK companies going to China and Hong Kong through 2027 delegations, RidgeCore representation and the *Doing Business in China 2027* report. How important is outbound business compared with inbound (China → UK) over the next 12 months? This decides how much content we plan for each direction.

**26. "NEXUS opens in China" (March 2026).** May we name the China entity and its Beijing and Shanghai partners on the site? Facts like this make AI assistants connect NEXUS with China.

## C. Access needed (owned by a NEXUS account, us added as users)

- [ ] Google Search Console (Owner or Full) for nexuscreativehq.com
- [ ] GA4 (Editor)
- [ ] Bing Webmaster Tools (can import from GSC)
- [ ] Ahrefs Webmaster Tools (free, verified via GSC) to export "best by links"
- [ ] Optional: Ghost admin for nexusstartupdiaries.com
- [ ] DNS: one.com (nexuscreativehq.com, nexusstartupdiaries.com) and Namecheap (globalinnovatorawards.com), via a password manager
- [ ] Ticket Tailor (reporting/analytics settings)
- [ ] Intercom (Fin content and settings), read access at minimum
- [ ] Mailchimp and the old-site admin, for subscriber exports
- [ ] Zoho Forms and Typeform, for submission exports

## D. Attachments

1. `02-NEXUS-Website-SEO-Strategy-Plan.md` (export to PDF): the strategy
2. `01-NEXUS-Research-Findings.md`: fact base (internal; share selectively)
3. `NEXUS Website Tool Guide.pdf`: already prepared
4. `04-NEXUS-SEO-Guide.html` (print to PDF): the full SEO guide (business explained, audit, strategy, tools, playbooks, other systems). Share Parts 1–4 and Part 10 with the client; Parts 5–9 are the working manual for our team

**Before sending:**
- Don't attach `01` as is: it contains internal notes (Ahrefs figures, competitor views, security observations such as the exposed admin path). Share a trimmed version or keep it internal.
- Send security findings (old PHP admin, exposed paths, DMARC) privately to the named technical contact, not in a widely forwarded email.

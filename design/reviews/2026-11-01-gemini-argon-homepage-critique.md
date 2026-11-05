### 1. Blunt Critique: Why the Client Isn’t Enjoying It

#### Top 6 Design Problems (in [Main.dc.html](../design-canvas/Main.dc.html))
1. **Wrong Typefaces Kill the Brand’s DNA:** [NEXUS Brand Guidelines 2025.txt](../local-docs/NEXUS%20Brand%20Guidelines%202025.txt#L91-L129) mandate **Neutral Face Bold** (a tall, condensed grotesque) and **General Sans**. The prototype loads Google Fonts `Archivo` stretched to `font-stretch: 125%` and `Manrope` ([Main.dc.html](../design-canvas/Main.dc.html#L11-L15)). Wide-stretched Archivo feels squat and sporty, destroying the sharp, architectural authority of Neutral Face.
2. **Generic SaaS Bento-Boxes Instead of Institutional Gravity:** Every section relies on `18px–22px` rounded cards, pill tags, and thin borders ([main-1.png](preview/main-1.png)). It looks like a mid-market Web3 template rather than a City of London (`80 Basinghall Street`) operational partner signing MOUs with Chinese science parks.
3. **Wireframe Scars Masquerading as Design:** Exposed dashed boxes (`[Placeholder: Tianjin signing photograph]`, `permission to confirm`, and seven blank grey portrait boxes in [main-3.png](preview/main-3.png)) make the site look broken. If you have no photography yet, design a typographic/data-first system—never ship empty picture frames.
4. **Exhausting Zebra-Striping & Monotonous Pacing:** Pitch Black (`#000000`) is meant to be *dominant* ([NEXUS Brand Guidelines 2025.txt](../local-docs/NEXUS%20Brand%20Guidelines%202025.txt#L160-L163)). Instead, 11 sections alternate Black → Grey → White → Black → White → Black → Grey → White → Black, each with identical `104px` vertical padding.
5. **Timid Hero Right Column & Off-Brand Scribble:** In [main-0.png](preview/main-0.png), the right column stacks a cramped mini-diagram over an empty dashed box while the X mark (`stroke="#242424"`) disappears behind it. Meanwhile, a hand-drawn yellow underline scribble (`/_blob/7955e6...`) clashes with the geometric identity.
6. **Flat Visual Hierarchy:** A 5-card partner row, 5-column process strip (`01–05`), 6-dot timeline, 7-person team grid, and 4-card insights row ([main-2.png](preview/main-2.png), [main-3.png](preview/main-3.png)) give every element equal weight. Nothing commands attention.

#### Top 5 SEO + AEO Problems
1. **80% of Audience Copy & Query Matches Hidden in JS State:** In [`Component.renderVals`](../design-canvas/Main.dc.html#L491-L510), five audience propositions share one stateful tab (`{{cur}}`), using a `<span>` instead of an `<h3>`. Search/AI crawlers only index the default tab ("I am entering the UK"), missing core queries (`UK landing programme for science park`, `UK representation office`, `scale-up growth diagnostic`).
2. **Zero-Signal H2 Headings:** H2s like *"Start where you are. Who are you?"*, *"What we have delivered."*, *"The right people in the right room."*, and *"Straight answers."* contain zero entity or service keywords for passage retrieval.
3. **Weak Entity Disambiguation & Missing Schema:** `<title>` is `NEXUS homepage` ([Main.dc.html](../design-canvas/Main.dc.html#L5)), `<meta name="description">` and JSON-LD (`Organization`, `WebSite`, `FAQPage`) are absent, and the legal disambiguator **"NEXUS Creative HQ"** (crucial to separate from the 2009 Tianjin Nexus group noted in [01-NEXUS-Research-Findings.md](../01-NEXUS-Research-Findings.md#L82)) is omitted from the Hero and first-160-char AEO intro.
4. **Google Fonts Break Mainland China Performance:** Fetching `fonts.googleapis.com` ([Main.dc.html](../design-canvas/Main.dc.html#L11)) violates the mainland China `<5s` load rule in [02-NEXUS-Website-SEO-Strategy-Plan.md](../02-NEXUS-Website-SEO-Strategy-Plan.md#L104-L106).
5. **Dead-End Anchor Links (`#top`, `#events`, `#insights`):** Instead of funneling the domain’s DR 34 / 884 referring domains to canonical hubs (`/institutions`, `/international-companies`, `/uk-scale-ups`, `/asia-corridor`, `/results`, `/events`, `/about/endorsing-role`, `/insights`), cards link to page anchors.

---

### 2. Agency Creative Concept: *“The Sovereign Aperture”*

Instead of treating the NEXUS **X** as "two lines crossing," we deconstruct its left and right chevrons (`>` and `<`) into an architectural **aperture and lock-gate** between two sovereign operating zones: `LONDON [51.51°N · EC2V 5AG · GMT]` `>` `<` `[UTC+8 · TIANJIN · SHANGHAI · HONG KONG]`. Designed for zero photography, the visual language draws from Swiss central-bank ledgers, diplomatic treaties, and flight-deck telemetry: exposed `1px solid #262626` structural hairlines, monumental condensed **Neutral Face Bold** display type on 80% Pitch Black (`#000000`), live dual-timezone coordinates, and precision vector "Contract Plates" (replacing missing photos with typographic MOU seals, city coordinates, and patent/acquisition specs). The X-aperture frames every bidirectional exchange—inbound Chinese technology companies and science park cohorts locking into London, and outbound UK scale-ups deploying into Asia—triggered by razor-thin strikes of Electric Yellow (`#DFFF13`).

---

### 3. New Homepage Specification (8 Sections)

> **Head Metadata & Schema:** `<title>NEXUS Creative HQ | UK–China Tech Market Entry & Scale-Up Partner</title>` with `Organization` (`legalName: "NEXUS Creative HQ Limited"`, `companyNumber: "12667243"`, `areaServed: ["GB","CN","HK"]`, `sameAs`), `WebSite`, and `FAQPage` JSON-LD.

1. **Top Utility Telemetry & Header**
   - **Purpose:** Immediate institutional credibility, dual-timezone presence, and flagship event urgency.
   - **Copy (Eyebrow Bar):** `LONDON [GMT] · SHANGHAI / HK [UTC+8] — GLOBAL INNOVATOR AWARDS · 16 NOV 2026 · THE DORCHESTER, LONDON → GET TICKETS`
   - **Layout & Distinction:** Full-bleed `#000000` bar with `1px solid #262626` hairlines; crisp navigation linking to all 7 sitemap hubs plus a sharp-edged `#DFFF13` CTA button (`Talk to us`).
2. **Hero: The Corridor Lock**
   - **Purpose:** Nail the 5-second UK–China positioning test and feed AI answer engines a citable 50-word opening definition.
   - **Copy:**
     - *Eyebrow:* `THE UK–CHINA INNOVATION CORRIDOR`
     - *H1:* `LAND, GROW AND SCALE IN THE UK. FROM CHINA AND BEYOND.` *(Second sentence in `#DFFF13`)*
     - *AEO Lead Paragraph:* **"NEXUS Creative HQ is the London-based operational bridge between the UK and China for technology companies, science parks and innovation zones—combining one accountable team at 80 Basinghall Street, London with on-the-ground partners in Tianjin, Shanghai and Hong Kong."**
   - **Layout & Distinction:** 7:5 asymmetric architectural grid on `#000000`. Right column replaces the weak diagram and missing photo with a precision **Bi-Directional Telemetry Ledger**: live London ↔ Tianjin/Shanghai/HK nodes framed by the two halves of the X-aperture (`>` `<`), displaying verified metrics (`100+ businesses supported`, `16 global partnerships`, `1,400+ business plans assessed`, `[placeholder: UK Government supplier clearance ref]`).
3. **Audience Matrix: Four Commercial Routes (All Crawlably Rendered)**
   - **Purpose:** Route all 4 revenue audiences into dedicated funnels while exposing 100% of keyword-rich copy in the DOM for SEO/AEO.
   - **Copy (H2):** `UK MARKET ENTRY, INSTITUTIONAL REPRESENTATION AND SCALE-UP DELIVERY.`
   - **Layout & Distinction:** 4-column architectural Hairline Matrix on `#000000` (no hidden JS tabs). Each column has a semantic `<h3>`, deliverable list, entry product, and crawlable link:
     - `01 / Innovation Institutions` (`/institutions`): UK Representation (annual) & UK Landing Programme (per cohort) → *Book a partnership call*.
     - `02 / International Tech Companies` (`/international-companies`): Market-Entry Diagnostic (paid, credited), UK Soft Landing, Market Intelligence Report → *Request a diagnostic*.
     - `03 / UK Frontier-Tech Scale-Ups` (`/uk-scale-ups`): Growth Diagnostic & specialist delivery (AI, R&D tax, IP, Series A) via 1 accountable team → *Request a growth diagnostic*.
     - `04 / UK to China & Asia Outbound` (`/asia-corridor`): 2027 mainland China/HK delegations, China representation via RidgeCore Ventures, *Doing Business in China 2027* report → *Register delegation interest*.
4. **The Bidirectional Corridor & Active Mandates**
   - **Purpose:** Prove on-the-ground China/Asia execution with named entities for AI engines.
   - **Copy (H2):** `A WORKING UK–CHINA CORRIDOR IN BOTH DIRECTIONS.`
   - **Layout & Distinction:** High-contrast Pure White (`#FFFFFF`) ledger section with a `2px solid #000000` technical grid. Top half shows 3 verified partner dossier plates (`RidgeCore Ventures` reciprocal UK↔China representation; `Tianjin` two signed MOUs incl. `[placeholder: Binhai Zhongguancun Science Park date]`; `S-Tron Shanghai` 2025 exhibiting / 2026 speaking) plus `[placeholder: Alibaba Entrepreneurs Fund, HK]` and `[placeholder: Swiss Bluefaer Innovation Centre, No. 1800 Huangxing Road, Shanghai]`. Bottom half is a sharp horizontal 2025–2027 milestone track (`2025 Tianjin MOU` → `2025 S-Tron` → `Mar 2026 [placeholder: NEXUS China entity wording]` → `Apr 2026 CBBC Hangzhou delegation` → `2026 2nd Tianjin MOU` → `2027 Mainland China & HK Delegations`).
5. **Verified Outcomes & Case Dossiers**
   - **Purpose:** Substantiate claims with concrete technical and commercial proof—without needing product photos.
   - **Copy (H2):** `PROVEN OUTCOMES ACROSS UK–ASIA TECH EXPANSION AND SCALE-UP GROWTH.`
   - **Layout & Distinction:** 3-column "Dossier Spec Sheet" on `#000000` linking to `/results`. Instead of empty grey image boxes, each card features a giant typographic metric/outcome header in `#DFFF13`, sector tag, and verified result (`[placeholder: client written consent]`):
     - **Sentian Aerospace** (*Aerospace / UAV*): `< 2 YRS TO ACQUISITION` — Acquired by listed Volatus Aerospace from UK incorporation.
     - **Auto Impartial** (*AI Compute*): `UK–ASIA CONSORTIUM` — Core silicon validated; consortium forming with Innovate UK.
     - **DarkhorseOne / Smart Patent / GI Healthcare** (*AI & Deep Tech*): UK patent filed & commercial collaboration (`DarkhorseOne`); China national AI programme finalist (`Smart Patent`); customer-funded PoC & GB Entrepreneur Awards 2025 finalist (`GI Healthcare`).
6. **Execution Model & Specialist Network**
   - **Purpose:** Contrast NEXUS ("boots on the ground, one point of accountability") against generic accelerators and trade bodies, and convert professional-firm sponsors.
   - **Copy (H2):** `ONE ACCOUNTABLE LONDON TEAM. VETTED SPECIALISTS ON DEMAND.`
   - **Layout & Distinction:** Studio Grey (`#D1D1D1`) split architectural block. Left side: 5-step horizontal lock (`01 Diagnose → 02 Plan → 03 Connect → 04 Deliver → 05 Grow`) led by CEO Mark Sarfo-Kantanka’s London team. Right side: The 8 specialist practices (`Accountancy`, `Corporate finance`, `Banking & payments`, `Legal`, `IP & patents`, `AI strategy`, `R&D tax`, `Venues`) with CTA to `/partner-with-nexus` (*Request the sponsor pack*).
7. **Flagship Convening & Corridor Intelligence**
   - **Purpose:** Drive GIA tickets/sponsorship and capture leads for the 2027 China report.
   - **Copy (H2):** `GLOBAL INNOVATOR AWARDS AND UK–CHINA CORRIDOR INTELLIGENCE.`
   - **Layout & Distinction:** Asymmetric 2-column `#000000` showcase. Left: Monumental feature card for **Global Innovator Awards** (`16 Nov 2026 · The Dorchester, London · Endorsed by GEP · 10 categories, 100 finalists · Judges from Barclays Innovation Banking, City of London Corporation, Innovate UK Business Connect, UCL, CBBC`) + **NEXUS Sessions** (`[placeholder: venue partner & launch date]`). Right: Editorial index linking to `/insights` (*Entering the UK from China: 2027 Guide*, *Hong Kong as a Gateway for UK Founders*, *2027 UK Delegation Guide*) + embedded lead capture for the **Doing Business in China 2027** report (`[placeholder: publication date]`).
8. **AEO Direct-Answer FAQ & Route Conversion Terminal**
   - **Purpose:** Win AI/featured snippets for high-intent queries, isolate non-commercial visa traffic, and capture enquiries.
   - **Copy (H2):** `FREQUENTLY ASKED QUESTIONS ON UK–CHINA MARKET ENTRY AND NEXUS CREATIVE HQ.`
   - **Layout & Distinction:** Split screen on `#000000` above the legal footer (`SBREC, 80 Basinghall Street, London EC2V 5AG` + Companies House `12667243`). Left: 5 semantic `<details>` accordions (all rendered in HTML for crawlers) answering *What is NEXUS Creative HQ?*, *How does a Chinese tech company or science park enter the UK?*, *How do UK companies reach China/HK?*, *How does pricing work?*, and *Innovator Founder visa endorsement* (strictly factual, routing to `/about/endorsing-role` and UKES with zero commercial CTA). Right: Streamlined enquiry form + direct route triggers.

---

### 4. Typography, Rhythm & 3 Signature Accessible Interactions

#### Typography & Rhythm Rules
- **Self-Hosted WOFF2 Only (Zero Google Fonts):** Serve `NeutralFace-Bold.woff2` and `GeneralSans-Regular/Medium/Bold.woff2` from the origin/Asia CDN for `<5s` China load.
- **Typographic Scale:**
  - **H1 Display:** `Neutral Face Bold`, uppercase, `clamp(48px, 6.5vw, 96px)`, `line-height: 0.94`, `letter-spacing: -0.02em`.
  - **H2 Section Headers:** `Neutral Face Bold`, uppercase, `clamp(32px, 4.2vw, 56px)`, `line-height: 0.98`, `letter-spacing: -0.015em`.
  - **Data / Telemetry Labels:** `General Sans Bold`, uppercase, `12px`, `letter-spacing: 0.14em`, tabular numerals (`font-variant-numeric: tabular-nums`).
  - **Body Copy:** `General Sans Regular`, `18px` (`1.6` line-height, max `62ch` measure).
- **Color & Rhythm Ratio:** **75% Pitch Black (`#000000`)**, **15% Pure White (`#FFFFFF`)**, **10% Studio Grey (`#D1D1D1`)**. Electric Yellow (`#DFFF13`) is strictly a `2px` border, badge, word highlight, or primary button fill with `#000000` text—never a section background. Replace rounded `20px` bubbles with sharp `0px–4px` architectural corners and exposed `1px solid #262626` grid lines.

#### 3 Signature Accessible Interactions
1. **The X-Aperture Corridor Switcher (Hero):** Hovering or keyboard-focusing any city node (`London`, `Tianjin`, `Shanghai`, `Hong Kong`) slides the SVG `>` `<` chevron brackets to lock onto that coordinate, revealing the verified local mandate (`80 Basinghall St`, `2 Signed MOUs`, `S-Tron 2025/2026`, `Gateway to Asia`). Fully navigable via `Tab`/`Arrow` keys; respects `prefers-reduced-motion: reduce` (instant state swap).
2. **4-Column Route Spotlight (Audience Matrix):** All 4 audience columns remain visible and crawlable in HTML. On `:hover` or `:focus-within`, the active column expands slightly (`flex: 1.25`), illuminates its top border in `3px solid #DFFF13`, and reveals its primary CTA pill in Electric Yellow while dimming sibling columns to `opacity: 0.65`.
3. **Interactive Milestone Scrubbing (Corridor Timeline):** Stepping through the `2025 → 2027` timeline nodes via pointer or keyboard focus draws a progressive `#DFFF13` vector line across the track and highlights the corresponding partner dossier card above it via `aria-controls`.

---

### 5. What to Cut Immediately
1. **Cut the Team Section & 7 Empty Grey Portrait Boxes (`#about`):** A wall of blank grey rectangles and an unapproved `[Founder quote...]` placeholder destroys executive trust. Move team bios to `/about` once photography and quotes are signed off.
2. **Cut the Hand-Drawn Yellow Underline Scribble (`/_blob/7955e6...`) in the Hero:** It contradicts the brutalist, geometric precision of Neutral Face Bold and the X mark.
3. **Cut the Dashed Photo Placeholders (`Hero` & `Results`):** Never show `[Placeholder: ... image]` boxes. Use typographic outcome metrics (`< 2 YRS`, `100+`, `1,400+`) and vector dossier plates instead.
4. **Cut the Standalone "Choose Your Route" 3-Card Row Above the Contact Form:** It duplicates the Audience Matrix higher up the page; fold the route selector directly into the Contact Terminal.
5. **Cut Redundant `[permission to confirm]` Dashed Badges in the Proof Strip:** Only render verified text credentials now (`CBBC Member`, `S-Tron Shanghai 2025 · 2026`, `Two Signed Tianjin MOUs`, `City of London Corporation partnership`) and add logo marks as written approvals arrive.

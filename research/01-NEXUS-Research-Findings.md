# NEXUS: Research Findings (fact base)

Compiled 31 October 2026. Sources: root project files (Developer Brief, SEO understanding doc, Tool Guide, Brand Guidelines 2025, prototype `seo lady draft.html`, `seo finding.txt`, `questions.txt`), live site crawl (Olostep map + page fetches), Companies House, UKES, globalinnovatorawards.com, nexusstartupdiaries.com, Olostep Answers. Raw Olostep outputs: `research/raw/`.

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
| GI Healthcare | Deep tech | Customer-funded PoC; GB Entrepreneur Awards 2025 finalist | UK scale-ups |
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
| URLs on live site | **173**: 101 `/insight/{id}`, 30 `/podcast/{id}`, 15 `/event/{id}`, 7 `/video/{id}`, 4 `/booking*`, core pages | Olostep map (`raw/map_nexuscreativehq.json`) |
| Broken | 11 pages + 77 images return 404 (`seo finding.txt`); our own check found 59 image 404s plus 313 not checkable, so the counts differ by method. Use the Ahrefs/Screaming Frog crawl as the final list | `seo finding.txt`, `live-site/image-status.json` |
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

Found 31 Oct 2026 by inspecting the live NEXUS site, globalinnovatorawards.com (our build), nexusstartupdiaries.com, `live-site/external-links.json` and public DNS. **Verified** = seen in code, links or DNS. **To confirm** = ask the client.

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

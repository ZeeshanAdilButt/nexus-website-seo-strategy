# NEXUS: what we are building

| | |
|---|---|
| Date | 5 November 2026 |
| For | Us (Zeeshan, Hasaan, the senior SEO specialist). Not for Mark |
| Status | Proposed to Mark on 5 November. The build starts on his go-ahead |
| Facts | Mark's brief and prototype, digested in [`07`](../knowledge-base/07-NEXUS-Mark-Facts.md). Where this page and `07` differ, `07` wins |
| Fee and terms | Local only: `proposals/2026-11-05/` |

## In one line

Phase 1 of the new nexuscreativehq.com: 24 pre-built pages, a content editor, nine enquiry forms with a small backend, the full redirect map and the security controls in Mark's brief. On Cloudflare, live by **Thursday 12 November 2026**.

## Key dates

| Date | What happens |
|---|---|
| Fri 6 Nov | Mark's go-ahead, deposit and the six answers |
| Mon 9 Nov | Content lock: his articles, texts, fonts, logo permissions and access |
| Tue 10 Nov | Staging shared with Mark. China speed test. Security scan |
| Wed 11 Nov | His feedback applied, full test pass, sign-off |
| Thu 12 Nov | Live |
| By 10 Dec | Insights extras: featured insight, topic filters, report form, The NEXUS Briefing sign-up |

## Pages (24)

| Page | Address | Main action |
|---|---|---|
| Home | `/` | Find your route · Talk to our team |
| For institutions | `/institutions` | Book a partnership call |
| For international companies | `/international-companies` | Request a diagnostic |
| For UK scale-ups | `/uk-scale-ups` | Request a diagnostic |
| Asia corridor | `/asia-corridor` | Register for 2027 delegations |
| Partner with NEXUS | `/partner-with-nexus` | Request the sponsor pack |
| Results, plus 7 case studies | `/results`, `/results/{slug}` | The matching audience action |
| Events | `/events` | Get tickets (GIA site) · Register interest |
| Insights | `/insights`, `/insights/{slug}` | Read · request the report |
| About | `/about` | Talk to us |
| Endorsing role | `/about/endorsing-role` | Go to UKES (ukesapp.co.uk). No sales action |
| Contact | `/contact` | Three route tiles and a general form |
| Privacy, Cookies, Terms, Accessibility | `/privacy` and so on | None |
| Page not found | `404` | Links to the three audience pages |

Section order, copy and components follow `07` §4. Headlines are Mark's prototype wording, word for word.

## How it is built

```text
Editor (Decap CMS at /admin, behind Cloudflare Access with 2FA)
  -> saves content to the GitHub repo (NEXUS org)
  -> Workers Builds runs Astro -> pre-built HTML
  -> served by Cloudflare Workers static assets, worldwide

Visitor submits a form
  -> one Cloudflare Worker: validate, honeypot, rate limit
  -> D1 (EU) stores it with the source fields
  -> Email Service: notify the NEXUS inbox (within 5 min) + acknowledge the sender
  -> webhook to the CRM (built, switched off)
```

| Part | Choice | Notes |
|---|---|---|
| Hosting | Cloudflare Workers + static assets | Workers Paid plan, about $5 a month, paid by NEXUS |
| Pages | Astro, building static HTML | No PHP, WordPress or plugins |
| Backend | One Worker in TypeScript | The only server code |
| Database | Cloudflare D1, EU jurisdiction | 30-day point-in-time restore, plus a daily copy to R2 |
| Images | Uploaded through the editor into the repo | Resized to WebP or AVIF by Astro at build time |
| Backup copies | Cloudflare R2, EU jurisdiction | A daily copy of the database |
| Email | Cloudflare Email Service | Microsoft 365 as the fallback |
| Editor | Decap CMS, with a small GitHub sign-in Worker | Roles enforced in GitHub. Each editor needs a free GitHub login. How it works: [`10`](10-NEXUS-Astro-and-Decap-101.md) |
| Admin login | Cloudflare Access | Two-factor for every admin. Not linked from the site |
| Analytics | GA4, only after consent | Search Console and Bing under NEXUS accounts |
| Fonts | Neutral Face Bold and General Sans, self-hosted | A stand-in headline face until Mark sends the web files |
| Accounts | All in NEXUS's name | We are members, not owners |

## Running costs (paid by NEXUS, checked 6 November 2026)

There's no separate server for the blog or the editor. Everything runs on one Cloudflare plan.

| Part | Where it runs | Cost |
|---|---|---|
| Pages, the blog, images | Cloudflare Workers static assets | Included. Requests for static files are free and unlimited |
| Editor (Decap CMS) | The editor's browser. Content is saved as files in the NEXUS GitHub repo | Free (GitHub free organisation) |
| Editor sign-in | A small Worker on the same Cloudflare account | Included |
| Rebuild after each publish | Workers Builds | Included: 6,000 build minutes a month. One build takes about a minute or two |
| Enquiries database | Cloudflare D1 (EU) | Included: 5 GB storage, 25 billion rows read and 50 million written a month |
| Emails | Cloudflare Email Service | Included: 3,000 a month. Alerts to NEXUS's own verified addresses are free |
| Admin two-factor | Cloudflare Access | Free plan |
| Backup copies | Cloudflare R2 (EU) | Within the free allowance at this size |
| **Total** | | **About $5 a month** (the Workers Paid plan), plus the domain renewal NEXUS already pays |

## What the editor manages

The following are all editable, with draft, preview and publish:
- text on every page
- statistics, partner logos and FAQs
- case studies, events, team members and insights
- placeholders, each of which can be hidden
- the announcement bar

## Forms (9)

| Form | `form_type` | On |
|---|---|---|
| Partnership call | `partnership_call` | Institutions |
| International diagnostic | `diagnostic_international` | International companies |
| Growth diagnostic | `diagnostic_scaleup` | UK scale-ups |
| Sponsor pack | `sponsor_pack` | Partner with NEXUS |
| 2027 delegations | `delegation_interest` | Asia corridor (with a destination field) |
| Event interest | `event_interest` | Events |
| General enquiry | `general` | Contact |
| Report request | `report_download` | Insights and Home |
| The NEXUS Briefing | `newsletter` | Insights |

**Every form:**
- validates its fields
- stores the submission
- emails the right inbox within 5 minutes
- sends an acknowledgement
- shows a thank-you message
- records the source fields: page, CTA, UTM tags, referrer, landing page and time
- never pre-ticks consent
- has no reCAPTCHA

Field keys are in `07` §9. Named NEXUS users can view, filter and export submissions to CSV.

## Search, AI and redirects

- **On every page:** Mark's titles and descriptions (`07` §10), one H1, self-referencing canonicals, share images (1200 × 630) and alt text.
- **Structured data:** Organization, Service, Event, Article, Person, FAQPage and BreadcrumbList.
- **Indexing:** an XML sitemap and robots.txt, submitted to Google and Bing.
- **Blocked services:** no Google Fonts, Maps, reCAPTCHA or YouTube on key pages, because they're blocked in mainland China.
- **Redirects:**
  - one-step 301s for all 175 current addresses, including the 11 broken ones
  - Mark's minimum list is in `07` §11
  - the "#!" duplicates disappear with the old site
- **Migration review:** the senior SEO specialist checks keyword targets, titles, the redirect map against Ahrefs backlinks, a pre-launch audit, and indexing in the two weeks after launch.
- **Pending:** the homepage title naming the China corridor, if Mark agrees (Questions, item 2).

## Content at launch

- **Copy:** Mark's prototype copy and case-study wording, word for word.
- **Placeholders:** anything missing is a visible `[Placeholder: …]` that can be hidden in the editor.
- **Case studies:** all seven named and quoted once Mark confirms consent. Readii appears on Results only.
- **Partners:** the Alibaba Entrepreneurs Fund and the Swiss Bluefaer Innovation Centre appear by name only, with no logo. The four partner logos stay marked until each permission arrives.
- **Insights:** all the existing articles Mark sends (duplicates removed), each on its own page with a redirect. Today the team posts them as LinkedIn-style posts with slides through the old site's admin. New ones are written in the editor using one article template.
- **Startup Diaries:** stays on its own Ghost site for now.

## Design

- **Brand:** Mark's brand rules (`07` §8): black, Electric Yellow as an accent only, white, and Studio Grey for lines. Pill buttons at least 48px, a 1200px content width, motion on hover and focus only.
- **Our changes to Hasaan's build, needed before the review link goes to Mark:**
  - no grey section grounds
  - the announcement bar on black, with a yellow "Get tickets"
  - five headlines back to Mark's wording

  The details are in `proposals/not-sent/`.
- **Homepage:** the photo-led design (Option A), with the Tianjin signing photo in the hero. The other directions stay in Figma.

## Security and launch

- **Protection:** HTTPS with HSTS, a firewall, security headers (CSP, X-Content-Type-Options, frame-ancestors, Referrer-Policy), and rate limits on the forms and the admin login.
- **Data:** encrypted in transit and at rest, with access logged.
- **Before launch:**
  - vulnerability scan and dependency audit, with high and critical findings fixed
  - component inventory with versions
  - one restore tested
  - test evidence and a test log against the acceptance checks in `07` §18
- **Handover:**
  - credentials through a password manager
  - an editing guide and one training session
  - technical docs: platform, inventory, integrations, form fields, webhook, redirect map and analytics events
- **After launch:** 30 days of free defect fixes. Ongoing support only if Mark agrees it in writing.
- **Security contact:** Zeeshan.

## Not building now

- **Phase 2, quoted separately:**
  - event detail pages with registration
  - results filters
  - online diagnostic booking and payment
  - the gated report download
  - the monthly dashboard
  - connecting the CRM
- **Optional:** the English and Chinese language switcher, site search, and moving Startup Diaries into Insights.
- **Out of scope:**
  - new copywriting, translation or photography
  - a client login
  - ongoing maintenance unless agreed
  - the Cloudflare China Network, which needs an Enterprise plan and an ICP licence

## Who does what

| Person | Owns |
|---|---|
| Zeeshan | Lead, platform, backend and forms, security, launch, the relationship with Mark. Admin on GitHub, Cloudflare and the editor during the build, alongside one NEXUS admin who owns the accounts. Access drops to the agreed level at handover |
| Hasaan | Design and front end: components, templates, the review site |
| Senior SEO specialist | Migration review: keywords, titles, redirects against backlinks, pre-launch audit, indexing check |

## Open before we can finish

**Mark's six answers:**
- go-ahead
- the homepage title
- case-study consent
- form inboxes and the reply time
- registered office
- editors

**His materials:**
- articles
- endorsing role text
- legal texts
- the Neutral Face web fonts
- logo permissions

**Access:**
- one.com
- the old site's admin
- Search Console
- Bing
- GA4
- Zoho
- Nexudus

Everything that can wait is listed in `proposals/not-sent/`.

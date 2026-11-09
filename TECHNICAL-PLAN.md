# NEXUS website: technical plan

For Hasaan and Zeeshan, and for any Claude session working on the build. Updated 9 November 2026.

**The facts are Mark's.** Every headline, section order, form field and title comes from [Mark's facts](knowledge-base/07-NEXUS-Mark-Facts.md). If this plan and that file differ, the facts file wins. Ask Zeeshan rather than guess.

## What we're building

This is Phase 1 of the new nexuscreativehq.com:
- 24 pre-built pages
- an editor the NEXUS team uses without a developer
- nine enquiry forms with a small backend
- one-step 301 redirects for all 175 current addresses
- the security controls in Mark's brief

It goes live about five working days after Mark's go-ahead and content. A page still waiting on content stays hidden until it arrives.

## Stack

| Part | Choice |
|---|---|
| Hosting | Cloudflare Workers + static assets, deployed by Workers Builds on every push to `main` |
| Pages | Astro 7, pre-rendered to static HTML. No PHP, no WordPress, no plugins |
| Editor | Decap CMS 3.17.x at `/admin`, saving to the GitHub repo. Sign-in through the [sveltia-cms-auth](https://github.com/sveltia/sveltia-cms-auth) Worker |
| Forms backend | One TypeScript Worker route, `/api/enquiry`, using the `@astrojs/cloudflare` adapter. Every other page stays pre-rendered |
| Database | D1, EU jurisdiction. Daily copy to R2 (EU) |
| Email | Cloudflare Email Service: notify NEXUS within 5 minutes and acknowledge the sender. Microsoft 365 as the fallback |
| Admin 2FA | Cloudflare Access in front of the enquiries admin. GitHub org 2FA for editors |
| Accounts | All in NEXUS's name: its GitHub organisation and Cloudflare account. We're members, not owners |

More detail, with links to learn each part: [plan/10 Astro and Decap 101](plan/10-NEXUS-Astro-and-Decap-101.md). The full build brief: [plan/09 What we are building](plan/09-NEXUS-What-We-Are-Building.md).

## Repo layout (the new build repo in the NEXUS org)

```text
astro.config.mjs        site: https://nexuscreativehq.com, cloudflare adapter
wrangler.jsonc          assets -> ./dist, D1 + R2 bindings, EU jurisdiction
src/
  layouts/              Base (head, SEO, JSON-LD), Page, Article
  components/           Header, Footer, AnnouncementBar, Hero, OfferCard, CaseCard,
                        StatRow, LogoWall, FAQ, RouteTiles, FormBlock, Placeholder
  content/              collections: caseStudies, events, insights, team, faqs, stats, settings
  content.config.ts     a schema per collection, so a missing field fails the build
  pages/                the 24 pages, plus api/enquiry.ts
public/
  admin/                index.html + config.yml (Decap)
  uploads/              editor image uploads
  fonts/                self-hosted Neutral Face Bold, General Sans
  _redirects            the 175 old addresses -> new ones, single 301s
```

Decap collections map one to one onto `src/content/`. Turn on `publish_mode: editorial_workflow` for drafts.

## Who does what

| Hasaan: design and front end | Zeeshan: platform and back end |
|---|---|
| Turn the review site into Astro layouts and components | GitHub org, Cloudflare account, Workers Builds |
| Pages built to Mark's section order (facts §4) and brand rules (§8) | Decap sign-in Worker and the editor/admin role split |
| Decap fields for every editable block | Forms Worker, D1 table, emails, CSV export, CRM webhook (built, switched off) |
| Responsive, accessible, fast: hover and focus motion only | `_redirects`, sitemap, robots, JSON-LD, consent and GA4 |
| Placeholders that can be hidden from the editor | Security headers, rate limits, scan, restore test, launch |

## Do these on day 1, before any template work

1. **Editor sign-in end to end.** Deploy the auth Worker, create the GitHub OAuth app (callback `<worker-url>/callback`), set `base_url` in `config.yml`, and sign in for real.
2. **Roles.** Decap has none, so GitHub enforces them:
   - editors have Write
   - admins have Maintain
   - `main` needs one approving review, and admins can bypass it
   - org-wide 2FA is on

   Check that an editor's draft can't publish without an approval. If that fails, tell Mark straight away.
3. **One deploy.** A push to `main` builds and goes live on the `workers.dev` URL.

## Before anything goes to Mark: fixes to the current review site

- **No grey section grounds.** Light sections go white, with cards outlined in Studio Grey.
- **The announcement bar** goes on black, with a yellow "Get tickets".
- **Headlines back to Mark's wording, word for word:**

| Page | Mark's headline |
|---|---|
| International companies | Enter the UK with a team already on the ground. |
| UK scale-ups | Your next stage, with the right specialists. (Remove the duplicate bold lede) |
| Partner with NEXUS | Meet the founders and institutions you want as clients. (Remove the duplicate bold lede) |
| Insights | What we are seeing across the UK and Asia. |
| Events | Events |
| About | One accountable team in the UK. |

Case-study and partner names stay as placeholders until Mark confirms consent. Readii appears on Results only. The Alibaba Entrepreneurs Fund and the Swiss Bluefaer Innovation Centre appear by name only, with no logo.

## Rules for every page

- **Headings:** one H1, Mark's wording. Mark's title and description (facts §10). A self-referencing canonical. A 1200 × 630 share image. Alt text on every image.
- **No services blocked in mainland China:** no Google Fonts, Maps, reCAPTCHA or YouTube. Fonts are self-hosted.
- **Brand:**
  - black, white, Electric Yellow as an accent only, and Studio Grey for lines
  - pill buttons at least 48px tall
  - a 1200px content width
- **Forms:**
  - field keys from facts §9
  - consent never pre-ticked
  - a honeypot plus rate limiting, no CAPTCHA
  - the source fields recorded: page, CTA, UTM tags, referrer, landing page and time
- **Images:** go through Astro's image pipeline, output as WebP or AVIF.

## Build order (working days after the go-ahead)

| Day | Work |
|---|---|
| 1 | Accounts, repo, Workers Builds, editor sign-in and the role test. Hasaan starts the layouts and components |
| 2 | All 24 pages as Astro pages, collections and Decap fields. The forms Worker, D1 and emails |
| 3 | Mark's content and articles loaded. `_redirects`, JSON-LD, sitemap, consent and GA4 |
| 4 | Staging shared with Mark. China speed test, security scan |
| 5 | Mark's feedback, the acceptance tests (facts §18), a restore test. Switch the domain, check every redirect, submit the sitemap |

## Done means

- Every acceptance test in facts §18 passes, with evidence saved.
- Lighthouse runs on a fresh profile, with numbers we can prove.
- Every old address returns a single 301 to its new page.
- An editor can draft, an admin can publish, and the site rebuilds in about two minutes.
- Each of the nine forms stores its submission, emails NEXUS and acknowledges the sender.

## For a Claude session on this repo

Read [CLAUDE.md](CLAUDE.md) first. The specialist agents are in [`agents/`](agents/). Copy them into `~/.claude/agents/` to use them, starting with `07-build.md` for this work.

---
name: website-build
description: Builds the agreed website on the chosen stack (default Cloudflare Workers + Astro + Decap CMS + D1 + Email Service). Tests the day-1 traps first, builds the pages to the facts doc and the design, then the forms backend, SEO, redirects and security, all on staging.
---

You build the site exactly as the facts doc and the approved design describe.

## Before building

Read three things: the facts doc (copy, H1s, section order, forms, SEO titles), the stack recommendation (data location, ownership, email) and the approved design.

Then confirm the accounts:
- **A client project:** everything in the client's name, with you as a member.
- **The user's own site:** the user's personal accounts.

## Day 1: test the traps before any templates

1. **Repo and pipeline.** Create the repo in the right owner's GitHub, with an Astro starter. Connect Cloudflare Workers Builds:
   - build: `npx astro build`
   - deploy: `npx wrangler deploy`, or the `cf` equivalent if the project uses `cf`
   - `assets.directory` set to `./dist`
2. **CMS sign-in.**
   - Deploy `sveltia-cms-auth` as a Worker.
   - Create a GitHub OAuth app with the callback set to `<worker>/callback`.
   - Set `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET` and `ALLOWED_DOMAINS`.
   - Set `base_url` under `backend` in `public/admin/config.yml`.
   - Sign in end to end.
3. **Roles.**
   - Editors get Write, and admins get Maintain or Admin.
   - Protect `main` so it needs one approving review, with admins allowed to bypass.
   - Turn on `publish_mode: editorial_workflow` and require 2FA in the org.
   - Test: an editor's draft can't publish until an admin approves. If it doesn't behave, tell the user at once.
4. **Email.**
   - Onboard the domain (its DNS must be on Cloudflare).
   - Verify the destination addresses.
   - Send a test from the Worker binding.
5. **Data.** Create D1 and R2 in the agreed jurisdiction or location. It can't be changed later.

## Build order

1. **Layouts and components from the design:** header (with a keyboard menu that sets `aria-expanded` and closes on Escape), footer, hero, cards, forms, FAQ and placeholder blocks.
2. **Content collections** with schemas (case studies, events, articles, team, FAQs, statistics, settings), and Decap collections mapped to the same files.
3. **Pages** in the owner's section order, with the H1s and copy word for word.
4. **The forms Worker.**
   - Behaviour: validation, a honeypot, rate limiting (no reCAPTCHA where it's blocked), storage in D1 with source fields (page, CTA, UTM tags, referrer, landing page, time), a notification and an acknowledgement, a thank-you message, and a JSON webhook that stays off until needed.
   - The admin view, filter and CSV export sit behind Cloudflare Access.
5. **SEO.**
   - Titles and descriptions from the facts doc.
   - Canonicals, sitemap, robots.txt and Open Graph images.
   - JSON-LD: Organization, Service, Event, Article, Person, FAQPage, BreadcrumbList.
6. **Redirects:** `_redirects` with a single 301 for every old address (up to 2,000 static lines), and a custom 404 page linking to the key pages.
7. **Consent and analytics:** accept, reject and manage options, with analytics loading only after consent.
8. **Performance.** Aim for 500ms to 1.5s on a first visit for real users. Expect Google's mobile lab test to read nearer 2s.
   - Serve the hero image as AVIF or WebP, sized per breakpoint and preloaded.
   - Self-host the fonts, cut down to the characters actually used.
   - Use almost no JavaScript.
   - Load no third-party scripts before consent.
9. **Security:**
   - HTTPS with HSTS, a firewall
   - headers: CSP, X-Content-Type-Options, frame-ancestors, Referrer-Policy
   - rate limits on forms and admin
   - a component inventory with versions
   - supported versions only

## Rules

- **Never change the owner's copy or H1s.** Raise a question instead.
- **Keep commercial and personal data** out of the repo and the logs.
- **Commit in small steps,** with no AI attribution.
- **Pull before reorganising.** Collaborators push too.

# Astro and Decap CMS: a 101 for the NEXUS build

| | |
|---|---|
| Date | 5 November 2026 (versions and links checked that day) |
| For | Us, before and during the build |
| Goes with | [`09` what we are building](09-NEXUS-What-We-Are-Building.md) |

## The idea in one picture

```text
NEXUS editor  ->  Decap CMS at /admin  ->  saves files to GitHub (NEXUS org)
                                                |
                                  Cloudflare Workers Builds sees the change
                                                |
                                     Astro builds every page as HTML
                                                |
                       Cloudflare serves the HTML worldwide (no PHP, no database behind pages)

Visitor sends a form  ->  one small Worker  ->  D1 database (EU) + email to NEXUS
```

## Astro: the page builder

**What it is.** A free, open-source tool that turns templates plus content into finished HTML pages. It runs when the site is built, not on the live site, so visitors only ever get plain, fast pages. Current major version: Astro 7.

**What we use it for:**
- **Layouts and components.** Hasaan's 24 pages split into reusable pieces: header, footer, hero, offer card, case-study card, FAQ, form block.
- **Content collections.** Case studies, events, insights, team, FAQs and statistics stored as Markdown or JSON files in `src/content/`. Astro checks each file against a schema, so a missing field fails the build instead of the live site.
- **SEO.** Titles, descriptions, canonicals, JSON-LD and the sitemap are generated for every page.
- **One server route.** `/api/enquiry` handles the forms. Every other page is pre-built.

**How it reaches Cloudflare.** We connect the GitHub repo in the Cloudflare dashboard, which is Workers Builds. The build command is `npx astro build`. The deploy command is `npx wrangler deploy`. The `wrangler.jsonc` file points `assets` at `./dist`. The forms route needs `npx astro add cloudflare` (the `@astrojs/cloudflare` adapter). Pages stay pre-rendered.

**Learn it:**
- [Getting started](https://docs.astro.build/en/getting-started/)
- [The official tutorial](https://docs.astro.build/en/tutorial/0-introduction/) (a few hours, the best first step)
- [Content collections](https://docs.astro.build/en/guides/content-collections/)
- [Deploy to Cloudflare](https://docs.astro.build/en/guides/deploy/cloudflare/)

## Decap CMS: the editing screen

**What it is.** A free, open-source editing screen, formerly Netlify CMS. It's one HTML page at `/admin` plus a `config.yml` file. Editors fill in forms, and Decap saves their changes as files in the GitHub repo. There's no database and no server of its own. It is actively maintained: version 3.17.3 was released on 26 October 2026.

**What we use it for:**
- One collection per content type. Each one maps to the same files Astro reads in `src/content/`.
- Editors change text, statistics, logos, FAQs, case studies, events, team members, insights, placeholders and the announcement bar.
- Image uploads go into the repo (for example `public/uploads/`). Astro then resizes them at build time.

**Drafts and publishing (editorial workflow):** set `publish_mode: editorial_workflow` in `config.yml`.

```text
Save draft         -> Decap creates a branch and a pull request on GitHub
Edit draft         -> another commit on that branch
Approve + publish  -> Decap merges the pull request -> Cloudflare rebuilds -> live in about two minutes
```

**Learn it:**
- [Introduction](https://decapcms.org/docs/intro/)
- [Basic steps](https://decapcms.org/docs/basic-steps/)
- [Configuration options](https://decapcms.org/docs/configuration-options/)
- [Editorial workflow](https://decapcms.org/docs/editorial-workflows/)
- [GitHub backend](https://decapcms.org/docs/github-backend/)
- [Astro's own Decap guide](https://docs.astro.build/en/guides/cms/decap-cms/)

## Two things that would get us in trouble, and the fix

### 1. GitHub login needs a small auth server

Decap's GitHub login needs an OAuth server, and only Netlify provides one built in. We are on Cloudflare, so we deploy one ourselves.

**The fix:**
1. Deploy [sveltia-cms-auth](https://github.com/sveltia/sveltia-cms-auth). It's a tiny Cloudflare Worker, it is compatible with Decap, and it was last updated in October 2026.
2. Create a GitHub OAuth app, with the callback set to `<worker-url>/callback`.
3. Add `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` to the Worker.
4. Set `ALLOWED_DOMAINS` to nexuscreativehq.com.
5. In `config.yml`, add `base_url: <worker-url>` under `backend`.

**Do this on day 1**, before any template work, and test a full sign-in.

### 2. "Editors draft, admins publish" is not built into Decap

Decap has no roles. The proposal promises two roles, so we enforce them in GitHub. **Test this on day 1 as well.**

| Who | GitHub permission | What happens |
|---|---|---|
| Editor | Write | Can save drafts (branches and pull requests). Publishing is blocked until an admin approves |
| Admin | Maintain or Admin | Can approve and publish. Allowed to bypass the review rule. **Zeeshan during the build, plus one NEXUS admin who owns the GitHub organisation and Cloudflare account.** At handover, Zeeshan's access drops to the agreed level (brief §14) |

To set this up:
- Protect `main` with "require a pull request with one approving review", and let admins bypass it ([protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)).
- Require two-factor authentication for everyone in the NEXUS GitHub organisation ([how](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization)). This meets the brief's two-factor rule for editors.
- Put [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) in front of the enquiries admin (where staff view and export form submissions), with a two-factor code. Only named NEXUS users see enquiries. We use test submissions during the build and don't keep access to live enquiry data after handover.

If the role split doesn't behave in testing, **we tell Mark straight away**. The fallback is admins only, plus a draft review by email. We don't wait until launch week.

## Build order (to hit 12 November)

1. **Fri 6:**
   - the NEXUS GitHub org and Cloudflare account
   - the repo with an Astro 7 starter
   - Workers Builds connected
   - the auth Worker and Decap sign-in working
   - the role split tested
2. **Sat 7 and Sun 8:**
   - Hasaan's pages as Astro layouts and components, with Mark's headlines
   - content collections, with Decap collections mapped to them
   - the forms Worker, the D1 table and emails
3. **Mon 9:**
   - Mark's content and articles loaded
   - the `_redirects` file with all 175 addresses
   - JSON-LD, sitemap, consent and GA4
4. **Tue 10:** staging shared, the China speed test, the security scan.
5. **Wed 11:** feedback, full testing, a restore test, sign-off.
6. **Thu 12:** switch the domain, check the redirects, submit the sitemap.

## Other references

- [Workers Builds: deploy on every push](https://developers.cloudflare.com/workers/ci-cd/builds/)
- [Workers static assets](https://developers.cloudflare.com/workers/static-assets/)
- [D1 database](https://developers.cloudflare.com/d1/)
- [Sveltia CMS](https://github.com/sveltia/sveltia-cms): a modern, actively developed alternative to Decap that reads the same `config.yml`. Keep it as a fallback, not the plan.

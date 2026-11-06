---
name: website-tech-stack
description: Chooses and explains the website stack (hosting, framework, CMS, forms backend, data location, email, accounts, running costs) from the project's real needs. Asks where users are, who owns the accounts and who edits. Default is Cloudflare + Astro + Decap CMS.
---

You choose the tech stack and explain it in plain words. Recommend one stack with reasons. Don't ask the owner to choose between options they can't judge.

## Ask first (only what intake didn't answer)

1. **Where are most visitors?** This decides data location and the CDN.
2. **Does the site collect personal data,** and under which law (UK or EU GDPR, US state law, other)?
3. **Who owns the accounts?** The client (an organisation in their name, with us as members) or the user (a personal site or product, on the user's own accounts)?
4. **Who edits after launch,** and can they use a GitHub login?
5. **What does the site need?** Forms, a blog, an enquiries admin, logins, payments, search, multiple languages?
6. **Which domain is it on, and where is its DNS?** Does mail on that domain need sending, receiving or both?
7. **Is any target country restrictive?** For example mainland China.
8. **Is there a monthly budget limit?**

## Default stack (marketing sites with a small backend)

```text
Editor signs in at /admin (Decap CMS, GitHub sign-in, 2FA)
  -> content saved as files in a GitHub repo (history, undo)
  -> Cloudflare Workers Builds runs Astro on every publish (about 1 to 2 minutes)
  -> pre-built HTML served from Cloudflare's network, close to each visitor
Form submitted -> one Cloudflare Worker -> D1 database + Email Service -> optional CRM webhook
```

| Piece | Role | Why | Running cost (check before quoting) |
|---|---|---|---|
| Cloudflare Workers + static assets | Hosting and CDN | Fast worldwide, free static requests, firewall and DDoS protection, no server to patch | About $5/month on Workers Paid. A small personal site can start on Free |
| Workers Builds | Deploys on every push | No manual deploys | Paid: 6,000 build minutes a month. Free: 3,000 |
| Astro | Builds the pages | Plain HTML for search and AI readers. Content collections check every field at build time | Free |
| Decap CMS | The editing screen at `/admin` | Free, git-based, no server or database, drafts and preview | Free |
| sveltia-cms-auth (a Worker) | GitHub sign-in for Decap | Decap needs an OAuth server when not on Netlify | Included |
| GitHub (organisation or personal) | Code, content, roles, 2FA | Branch protection gives "editors draft, admins publish". The org can require 2FA | Free |
| D1 | Form submissions | SQL, point-in-time restore for 30 days | Paid includes 5 GB, 25 billion reads, 50 million writes a month |
| R2 | Backups and large files | A separate copy of the data | Small sites stay in the free allowance |
| Email Service | Notifications and acknowledgements | Sends from the site's own domain | Sending to verified addresses is free. Arbitrary recipients need Paid (3,000 a month included) |
| Cloudflare Access | 2FA in front of private admin pages | "2FA for every admin" without building logins | Free plan |
| Analytics | GA4 after consent, or Cloudflare Web Analytics | Consent first | Free |

## Adapt to the answers

**Data location** (D1 and R2 can be pinned when you create them):

| Most users or law | Choice |
|---|---|
| EU, or EU or UK GDPR | `jurisdiction=eu` on D1 and R2. Data stays in the EU. Pages are still served worldwide |
| US | `jurisdiction=us`, or a location hint near the users |
| Global, no residency rule | Let D1 pick automatically, or set a location hint (`weur`, `enam`, `apac` and so on) near where most submissions come from |
| FedRAMP needs | `jurisdiction=fedramp` |

Jurisdiction can only be set when the database is created, so decide before building.

**Ownership:**
- **Client project:** the Cloudflare account, GitHub organisation, analytics, Search Console, domain and DNS all in the client's name. We are members, and at handover our access drops to the agreed level. Only named client users see live personal data.
- **The user's own site:** use the user's personal Cloudflare account and personal GitHub (or their own organisation). Same stack, fewer roles.

**Editors:**
- **Can use GitHub:** Decap.
- **Can't use GitHub:** a hosted CMS with email logins (Sanity, TinaCMS), at extra monthly cost.
- **Already writing in Ghost:** Ghost headless (Astro pulls posts through the Content API, and a webhook triggers rebuilds). Offer this as an option. The costs are the Ghost subscription and two editors.

**Restrictive country (mainland China):**
- No Google Fonts, Maps, reCAPTCHA or YouTube on key pages.
- Keep pages light and test from inside the country.
- Cloudflare's in-country network needs Enterprise plus an ICP licence. Say plainly what can't be guaranteed without one.

**When not to use this stack:**
- **A tiny brochure or event site, where the owner wants to edit visually and needs no backend:** a no-code builder such as Framer.
- **A heavy app with logins, payments and complex data:** a full-stack framework on Workers (Astro server routes, or a dedicated app framework), plus a proper auth provider.

## Email on the site's own domain

The domain's DNS must be on Cloudflare to use Email Service. Onboarding adds the MX, SPF, DKIM and DMARC records.

| Goal | How | Cost |
|---|---|---|
| Receive `hello@domain` in a personal inbox (for example Gmail) | **Email Routing:** a rule from `hello@domain` to a verified destination address | Free |
| Website form alerts to the owner's own inbox, sent from `hello@domain` or `noreply@domain` | The form Worker sends through the Email Service binding to the verified destination address | Free on any plan |
| Acknowledgements to anyone (the person who filled in the form) | Email Sending from `hello@domain` | Workers Paid, 3,000 a month included |
| Day-to-day mail sent from `hello@domain` (replying as hello@) | A mailbox provider for that domain (Google Workspace, Zoho Mail, Fastmail), or Gmail "Send mail as" through an SMTP service | Provider pricing. Email Service also offers SMTP, but it's built for transactional mail, so check the terms before using it for personal mail |

## Output

- **A one-page recommendation:** the stack with reasons, data location, ownership, editing, email, running costs, and what it can't do.
- **A component inventory** (component, role, who keeps it current) and the set-up order.
- **Day-1 traps to test before building:**
  1. Decap sign-in through the auth Worker.
  2. The role split through GitHub branch protection (editors get Write, admins Maintain, `main` needs one approval with admins allowed to bypass).
  3. The email domain onboarded and verified.

Re-check prices and limits on the provider's pricing pages before quoting. They change.

---
name: website-tools-setup
description: Sets up and checks the tools and accounts a website project needs (Cloudflare and DNS, GitHub, Google Search Console, Bing Webmaster Tools, analytics, Ahrefs Webmaster Tools, PageSpeed, email routing, uptime monitoring). Does as much as possible in the user's connected Chrome through the Claude extension, hands over only sign-ins, account creation and secrets, and skips anything already set up.
---

You get every tool and account ready, doing as much of the work as you're allowed to, so the user only steps in where they must.

## How you work

1. **Check first, and don't bother the user with anything already done.** Before asking for anything, look for it:
   - `gh api user` and `gh api orgs/<org>`
   - `cf` or `npx wrangler whoami`, and the zone list
   - `nslookup -type=TXT <domain>` (finds google-site-verification records and others)
   - `curl -s https://<domain>/robots.txt` and `/sitemap.xml`
   - the site's HTML for analytics tags
   - the project's `tools-and-access.md` file

   Mark each tool **Ready**, **Partly set up** or **Missing**.
2. **Use the connected Chrome browser** through the Claude in Chrome extension.
   - Load its tools in one ToolSearch call (`tabs_context_mcp`, `navigate`, `read_page`, `find`, `computer`, `form_input`).
   - Do everything you can: open the right pages, fill in non-secret fields (property names, site URLs, time zones), click through set-up steps, and read back the IDs and verification values.
3. **Hand over only what the user must do,** then continue when they say "done". Say exactly what to do. For example: "Sign in with the client's Google account in this tab, then tell me".
   - **Sign-ins and two-factor codes:** the user signs in, in the open tab.
   - **Creating new accounts, entering passwords, payment details:** always the user.
   - **Accepting terms, granting OAuth access, creating resources that cost money, changing account settings:** ask first, then click only after a clear yes.
4. **Secrets never go through chat, the browser or a committed file.** When a key or secret is needed (API tokens, OAuth client secrets, SMTP passwords):
   - Write a small script that asks for it in the terminal, with hidden input, and stores it where it belongs:
     - `npx wrangler secret put NAME`, or the `cf` equivalent, for Workers
     - `gh secret set NAME` for GitHub Actions
     - `.dev.vars` for local development, and only if it's gitignored
   - Tell the user which page to copy the value from, and to run the script in their own terminal.
   - Afterwards, confirm the secret exists by name (for example `wrangler secret list`), never by reading its value.
   - If it already exists, skip it.
5. **Record everything that isn't secret** in a local `tools-and-access.md`: account owner, property IDs, measurement IDs, verification method, who has access, date. Keep it gitignored if it names client accounts.

## Tool checklist

| Tool | What it's for | You do | The user does | Done when |
|---|---|---|---|---|
| **Domain DNS on Cloudflare** | Hosting, email, verification records | Add the zone, read the two nameservers, open the registrar's DNS page | Sign in at the registrar and change the nameservers | `cf` shows the zone active, and `nslookup` returns Cloudflare NS |
| **Cloudflare account** (client-owned or the user's own) | Hosting, D1, R2, Email, Access | Check the plan. Open Billing to upgrade to Workers Paid if needed, with a yes first | Create the account if missing. Approve the payment | `whoami` shows the right account |
| **GitHub organisation or account** | Code, content, CMS roles | Create the repo. Set branch protection and the org 2FA requirement through `gh`. Invite members | Create the org if missing. Accept invites | `gh api` shows protection and members |
| **Google Search Console** | Indexing, search queries, sitemap | Open a Domain property, read the TXT value, add the TXT record through `cf` (with a yes) or show the user. Verify, submit the sitemap, add users | Sign in with the owner's Google account | Property verified, sitemap "Success" |
| **Bing Webmaster Tools** | Bing, and the AI answers that use it | Use "Import from Google Search Console" and submit the sitemap | Sign in | Site verified, sitemap submitted |
| **Google Analytics 4** (or Cloudflare Web Analytics) | Conversions after consent | Create the property and web stream, copy the Measurement ID (not secret) into the site config, mark the key events | Sign in. Accept the terms when asked | Events show in DebugView after consent |
| **Ahrefs Webmaster Tools** | Backlinks, broken links, site audit | Connect it through Search Console | Sign in | Site verified, first crawl started |
| **PageSpeed Insights** | Lab speed checks | Run tests. If the daily anonymous quota runs out, create an API key through the secret script | Create the API key in Google Cloud if needed | Results saved as proof |
| **Screaming Frog** (desktop) | Crawls and redirect checks | Give the list of URLs and settings | Install it, run the crawl and export the results | CSV exports in `knowledge-base/` |
| **Email Routing and Sending** | `hello@domain` forwarding, form emails | Onboard the domain, add the destination addresses | Click the verification link Cloudflare emails to each destination | Test email received |
| **Cloudflare Access** | 2FA in front of private admin pages | Create the Access application and policy (named users) | Approve the identity provider sign-in | A test login is blocked without 2FA |
| **Uptime monitoring** (for example a free uptime service, or Cloudflare health checks) | Alerts if the site goes down | Set the checks and alert email | Sign up if it's a new service | A test alert received |
| **Cookie consent** | Lawful analytics | Build the banner into the site (accept, reject, manage) | Approve the wording | Analytics blocked until accept |

## Rules

- **Never type a password, API key, token or payment detail into any page.**
- **Never create an account for the user.** Open the sign-up page and hand over.
- **Ask before every outward-facing action:** sending invites, accepting terms, submitting forms that create resources, DNS changes on a live domain, and anything that costs money.
- **For a client project,** every account is in the client's name. We get member or user access, never ownership.
- **Leave proof:** screenshots of the verified states, and the final `tools-and-access.md`.

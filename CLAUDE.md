# NEXUS website: notes for Claude

This repo holds the research, facts, plans and designs for rebuilding nexuscreativehq.com for NEXUS Creative HQ Ltd (client: Mark Sarfo-Kantanka). The build code itself will live in a separate repo in NEXUS's GitHub organisation.

## Read these first, in this order

1. [TECHNICAL-PLAN.md](TECHNICAL-PLAN.md): the stack, who does what, day-1 checks, build order, what done means
2. [knowledge-base/07-NEXUS-Mark-Facts.md](knowledge-base/07-NEXUS-Mark-Facts.md): Mark's facts. **These win over everything else**
3. [plan/09-NEXUS-What-We-Are-Building.md](plan/09-NEXUS-What-We-Are-Building.md): pages, forms, SEO, security, handover
4. [plan/10-NEXUS-Astro-and-Decap-101.md](plan/10-NEXUS-Astro-and-Decap-101.md): how Astro, Decap and Cloudflare fit, and the two traps
5. [design/README.md](design/README.md): Hasaan's review build and the design canvas
6. [00-START-HERE.md](00-START-HERE.md): the whole folder map and timeline

## Rules

- **Mark's documents are the facts.** Headlines, section order and copy are his wording, word for word. Never invent names, numbers, claims, emails or prices. Anything missing is a placeholder that can be hidden.
- **This repo is public.** Fees, quotes, proposals and client messages never get committed. They live in the gitignored `proposals/`, `responses/` and `reference docs/` folders.
- **No services blocked in mainland China** (Google Fonts, Maps, reCAPTCHA, YouTube).
- **Accounts stay in NEXUS's name.** Never type passwords or secrets into chat or commit them. Set secrets with `wrangler secret put` or the dashboard.
- **Git:** small commits with real messages. No AI attribution in commits, pull requests or READMEs.
- **Writing:** plain English. No em or en dashes, no semicolons.

## Agents

[`agents/`](agents/) has ten specialist agents, from intake to launch. Copy them into `~/.claude/agents/` (or `.claude/agents/` in the build repo). For the build, use `07-build.md`, then `08-content-migration.md` and `09-qa-and-launch.md`. [MASTER-WEBSITE-PROJECT-PROMPT.md](MASTER-WEBSITE-PROJECT-PROMPT.md) explains how they work together.

# Website project agents

Ten specialist agents for building client or personal websites, plus the master prompt that runs them in order: [`../MASTER-WEBSITE-PROJECT-PROMPT.md`](../MASTER-WEBSITE-PROJECT-PROMPT.md). They are generic. Each one asks what it needs to know before acting, and skips work that's already done.

## The agents

| # | Agent | Use it when | It hands over |
|---|---|---|---|
| 01 | [intake-and-facts](01-intake-and-facts.md) | A new project starts | The project profile, the workspace, and a facts doc from the owner's documents |
| 02 | [research](02-research.md) | You need to know where the current site and market stand. Skip it, or fill gaps only, if research already exists | Research findings, with a proof for every number |
| 03 | [tech-stack](03-tech-stack.md) | Choosing hosting, framework, CMS, data location, email and accounts | A stack recommendation with reasons, running costs and set-up steps |
| 04 | [design](04-design.md) | No design yet, or an existing design needs checking or improving | Designs and screenshots, checked against the facts |
| 05 | [proposal-and-quote](05-proposal-and-quote.md) | A client needs a plan and a price | Separate documents: plan, questions, quote. Later items kept unsent |
| 06 | [client-messages](06-client-messages.md) | Anything a client or partner will read | A human-sounding message, fact-checked, saved with its history |
| 07 | [build](07-build.md) | The design and stack are agreed | A working site on staging, built to the facts |
| 08 | [content-migration](08-content-migration.md) | Old articles or pages need new homes | Content moved, with a 301 for every old address |
| 09 | [qa-and-launch](09-qa-and-launch.md) | Before staging review, launch and handover | Test evidence, the launch and the handover pack |
| 10 | [tools-setup](10-tools-setup.md) | Any time an account or tool is needed: DNS, Cloudflare, GitHub, Search Console, Bing, analytics, Ahrefs, PageSpeed, email, monitoring | Tools ready and verified, using your connected Chrome. You only sign in, create accounts and paste secrets into a terminal prompt |

## How to use them

- **As Claude Code subagents:** copy the files you want into `~/.claude/agents/` (for every project) or into `<project>/.claude/agents/` (one project). Each file has `name` and `description` frontmatter, so Claude Code can call it.
- **As prompts:** paste a file's body into a fresh Claude Code session for that one job.
- **Run in order** with the master prompt. It runs intake first, then routes to the agents the project needs.

## Rules every agent follows

1. **The owner's documents are the facts.** If anything conflicts with them, ask. Never invent claims, numbers, names or prices.
2. **Every number needs a proof** you can point to (a file, a script output, a source and date).
3. **Propose only what was asked for.** Extras become decisions with a default. Never cap something the owner asked for.
4. **Ask before acting** on anything outward-facing: sending, publishing, pushing to someone else's repo, account changes.
5. **Do as much as possible in your connected Chrome** (through the Claude extension). Hand over only sign-ins, account creation, passwords and payments. Secrets go through a terminal prompt, never chat. Skip anything already set up.
6. **Commercial files stay out of public repos.** Prices, quotes and messages go in gitignored folders.
7. **No AI-sounding writing.** No em or en dashes, no semicolons, no filler words.
8. **No AI attribution** in commits, pull requests or READMEs.

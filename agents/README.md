# Agents: moved

The website project agents now live with the client project agents in one private repo:
**[ZeeshanAdilButt/client-project-agents](https://github.com/ZeeshanAdilButt/client-project-agents)**. Each of the fourteen agents has its own folder, with its templates and scripts beside it.

| Agent | What it does |
|---|---|
| project-orchestrator | Start here. Intake, the project folder, routing |
| research-analyst | Business research, and the facts doc from the client's brief |
| seo-analyst | The current site, search and AI visibility, speed with proof |
| call-prep | Meeting briefs and minutes |
| solution-architect | The stack, data location, account ownership, phases |
| design-director | Claude Design, checks of existing designs, clips |
| client-writer | Every client message, drafted first, then humanised with Codex |
| proposal-builder | Plan, questions and quote as separate PDFs |
| email-setup | Domain mail, sending, deliverability |
| tools-setup | Accounts and tools through your connected Chrome |
| web-builder | The build: B2B back end or a marketing site |
| content-migration | Old content to new addresses with 301s |
| quality-auditor | Independent checks before anything is sent |
| launch-qa | Site tests, launch, handover |

Install them with `scripts/install.sh` (or `install.ps1`) from that repo. They are already installed in `~/.claude/agents` on this machine.

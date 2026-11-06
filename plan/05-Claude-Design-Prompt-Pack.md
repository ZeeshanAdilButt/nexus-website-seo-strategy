# NEXUS: Claude Design prompt pack

> **Mark's documents win.** Where this document differs from Mark's brief or prototype copy, follow [`07-NEXUS-Mark-Facts.md`](../knowledge-base/07-NEXUS-Mark-Facts.md). Its section 15 lists our proposals that still need Mark's decision.

**Why a prompt pack:** Cline (this agent) can't operate Claude Design directly. You run these prompts in Claude Design (claude.ai, the Design tab, or `/design` inside Claude Code), export the results into `design/exports/`, and Cline then checks them against the SEO plan.

**Exports available:** PDF, PPTX, standalone HTML / HTML bundle, Google Slides, partner tools (e.g. Canva, Vercel), and **Handoff to Claude Code** for the build.

> **Likely origin of the existing drafts:** `knowledge-base/nazia/seo lady draft.html` (with `<x-dc>`, `DCLogic`, `support.js`) and "NEXUS Website Redesign Prototype-2" (a "Loading… Unpacking…" shell) look like Claude Design exports. If you have the original project, **re-export it as PDF or standalone HTML**. That's the easiest way for us to finally read Prototype-2.

---

## Step 1: Design system (do this once)

Upload, or create in Settings → Design Systems:

| Upload | From |
|---|---|
| Brand guidelines | `NEXUS Brand Assets\NEXUS Brand Guidelines\NEXUS Brand Guidelines 2025.pdf` |
| Logos | `NEXUS Brand Assets\PNG\` (white-on-black, metallic-on-white) |
| Brand graphics | `NEXUS Brand Assets\NEXUS Brand Graphics\` (X shapes) |
| Fonts | Neutral Face Bold, General Sans (licensed files from NEXUS) |
| Copy source | `emails-and-meetings/2026-10-31-mark-brief-and-assets/text-copies/prototype/*.txt` + the Developer Brief |

**Prompt:**
> Create a design system for NEXUS from the uploaded brand guidelines.
> - **Colours:** Pitch Black #000000 (dominant), Electric Yellow #DFFF13 (accent only, never a section background, never text on white), Studio Grey #D1D1D1, Pure White #FFFFFF.
> - **Type:** headlines in Neutral Face Bold, uppercase; body in General Sans, 17px, line height 1.6.
> - **Buttons:** pill shape, at least 48px tall. Primary is yellow with black text; secondary is outline.
> - **Layout:** 1200px max width, 32px gutters (20px on mobile), 64–112px between sections.
> - **Logo:** white on black or metallic on white only.
> - **Tone:** direct and confident; provocative headlines, substantive body copy.
> - **Images:** no stock or AI-generated photos. Use labelled boxes "[Placeholder: …]".
> - **Accessibility:** WCAG 2.2 AA contrast; visible focus states; respect reduced motion.

---

## Step 2: Prompts

### A. Homepage hero: two variants (for the Lyssna 5-second test)
> Using the NEXUS design system, create two hero variants on black, each at 1440px desktop and 390px mobile.
>
> **Shared elements**
> - Eyebrow: "The UK–China innovation corridor"
> - Intro: "NEXUS is the operational bridge between the UK and China for technology companies, science parks and innovation zones: one accountable team in the UK, with partners on the ground in China."
> - Buttons: "Find your route" (yellow) and "Talk to our team" (outline)
> - Image: "[Placeholder: Tianjin signing photograph]"
>
> **Headlines**
> - Variant A H1: "Land, grow and scale technology businesses in the UK."
> - Variant B H1: "Land, grow and scale in the UK.", with a second line "From China and beyond." in yellow.
>
> **Under each hero, a proof strip**
> - Stats: 100+ businesses actively supported · 16 curated global partnerships · 1,400+ business plans assessed · Supplier and security cleared
> - Four logo placeholders: City of London, TEDA, S-Tron, CBBC, each marked "permission to confirm"

### B. Audience page template: `/international-companies`
> Create the "For international companies" page.
> - **Header:** breadcrumb Home / For international companies; H1 "Enter the UK with a team already on the ground."
> - **Answer-first paragraph** (about 50 words, real text, for search and AI): NEXUS helps international technology companies, especially from China and Hong Kong, enter the UK. It starts with a paid Market-Entry Diagnostic, followed by UK Soft Landing support.
>
> **Sections, in order**
> 1. The challenge
> 2. What we provide: three offer cards (Market-Entry Diagnostic, UK Soft Landing, Market Intelligence Report), each with the price line "On application"
> 3. Why us: 1,400+ plans assessed; RidgeCore represents clients in China; one accountable team
> 4. Case study cards: DarkhorseOne, Eco2Life, Smart Patent
> 5. Who this is for, and not for. Not for visa-only enquiries, which go to UK Endorsing Services.
> 6. How it works: Diagnose, Plan, Land, Grow
> 7. Four FAQs as an accordion
> 8. Enquiry form: company, HQ country, sector, stage, timeline, name, work email, an unticked marketing-consent box and a privacy link

### C. Asia corridor page (both directions)
> Create the "Asia corridor" page.
> - **H1:** "Our Asia corridor, led by China."
> - **Intro:** the corridor works in both directions: Chinese companies and institutions landing in the UK, and UK companies entering China via Hong Kong.
> - **Partner cards:**
>   - RidgeCore Ventures (reciprocal representation)
>   - Tianjin (two MOUs)
>   - S-Tron Shanghai (exhibiting in 2025, speaking in 2026)
>   - Alibaba Entrepreneurs Fund and Swiss Bluefaer: name only, marked "[wording to be approved]", no logos
> - **"Why Hong Kong" card.**
> - **Vertical timeline:**
>   - 2025: first Tianjin MOU
>   - 2025: S-Tron Shanghai
>   - March 2026: NEXUS opens in China [to confirm]
>   - April 2026: CBBC delegation to Hangzhou
>   - 2026: speaking at S-Tron
>   - 2026: second Tianjin MOU
> - **2027 delegations section** with an interest form. Destination field: Mainland China / Hong Kong / Both / Not sure.
> - **Case studies:** Auto Impartial, Eco2Life, Smart Patent.
> - Do **not** include a Chinese-language block.

### D. Client strategy deck (10 slides, PPTX/PDF)
> Upload `02-NEXUS-Website-SEO-Strategy-Plan.md` and `04-NEXUS-SEO-Guide.md`, and use them to create a 10-slide deck in the NEXUS design system:
> 1. Title: "Making NEXUS the answer for UK–China tech"
> 2. Where we are: 884 linking domains, 2 ranking keywords, every page titled "Nexus"
> 3. How AI describes NEXUS today
> 4. The positioning fix (hero A and B)
> 5. Five audiences, including outbound UK → China
> 6. Site map with one keyword cluster per page
> 7. Content clusters A–E
> 8. Your wider toolset (Ticket Tailor, Ask Fin, Mailchimp, Ghost, Typeform, Zoho, Nexudus) and the decisions needed
> 9. Timeline: launch Thursday 12 November, GIA Monday 16 November
> 10. What we need from you: the top questions and the accesses
>
> Style: big numbers, one idea per slide, black backgrounds with yellow used only as an accent.

### E. One-pager: the NEXUS tool ecosystem
> From `01-NEXUS-Research-Findings.md` section 8, create a single A4 diagram of NEXUS's systems, grouped by job: Website, Awards site, Blog, Tickets, AI chat, Newsletters, Forms, Memberships, Email, Analytics, DNS. Tag each system with one status: Keep / Merge / Export then retire / Decide.

---

## Step 3: Bring it back and check
1. Export pages as **standalone HTML**, and the deck and one-pager as **PPTX/PDF**. Save them in `design/exports/`.
2. Ask Cline to check the exports:
   - one H1 per page
   - copy is real text, not images
   - an answer-first paragraph and FAQs are present
   - no Google Fonts, YouTube or reCAPTCHA (these break in mainland China)
   - brand rules followed: yellow never used as a background
   - placeholders are kept, with no invented claims
3. For the build: **Handoff to Claude Code**, or give the HTML to the developer together with the brief.

**Confidentiality:** the case studies are marked "Private & Confidential", and `01` contains security notes. Keep the Claude Design project private to your organisation, and don't share public links until NEXUS approves.

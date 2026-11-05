### 1. Verdict

This round is a major leap forward: merging the calm, high-conviction headline and open service ledger with the telemetry bar, coordinate register, and X-aperture transforms the page from a generic startup template into an authoritative, institutional cross-border platform. It now feels genuinely distinctive, though a few broken grid axes, placeholder leaks, and missing machine-readable entity layers keep it just short of award-winning execution.

**Design: 8.2 / 10** · **SEO–AEO: 6.8 / 10**

---

### 2. Top 8 Specific Fixes (Ordered by Impact)

1. **Head (`<head>` & `<helmet>` in [HomeA.dc.html](../design-canvas/HomeA.dc.html#L3-L12)): Missing China-safe fonts, meta & JSON-LD**
   → Remove `fonts.googleapis.com` (blocked/slow in mainland China); self-host `.woff2` files (`font-display: swap`). Add `<link rel="canonical" href="https://nexuscreativehq.com/">`, a 155-char `<meta name="description">`, and a `<script type="application/ld+json">` `@graph` containing `Organization` (`legalName: "NEXUS Creative HQ Limited"`, company no. `12667243`, `founder: "Mark Sarfo-Kantanka"`, `address` for `EC2V 5AG`, `areaServed: ["GB","CN","HK"]`, `memberOf` CBBC + UKES, `sameAs`), `WebSite`, `Event` (GIA), and `FAQPage`.

2. **Hero + Aperture Grid Axis ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L80-L135)): Misaligned vertical hairlines**
   → Add `*,*::before,*::after{box-sizing:border-box}` globally. Change both the Hero container, Aperture container, and `<dl>` stats bar to a shared `display: grid; grid-template-columns: repeat(4, 1fr)`. Set `nav.idx` to `grid-column: 1` (`1fr`, ~314px), `.hero-main` to `grid-column: 2 / -1`, London to `grid-column: 1`, the X-aperture to `grid-column: 2 / 4`, and China cities to `grid-column: 4`. Every vertical `#262626` hairline will lock onto one continuous Swiss grid.

3. **Header, Service Rows & Footer Links ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L65-L73)): Hash `#` anchors blocking crawl equity**
   → Replace in-page `#` hrefs on core pages with real sitemap paths: `/institutions`, `/international-companies`, `/uk-scale-ups` (currently `#what`), `/asia-corridor`, `/results` (currently `#results`), `/insights` (currently `#events`), `/about` (currently `#questions`), and `/about/endorsing-role`. Keep `#what`–`#questions` strictly inside the `On this page` index.

4. **Hero H1 Second Line ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L94)): Low-authority grey on core differentiator**
   → Change `One accountable team.` from `color: #7A7A7A` to `#BDBDBD` (or `#FFFFFF` with a `#DFFF13` period). At `64px` uppercase, `#7A7A7A` reads as disabled state rather than calm authority.

5. **Section 03 Results ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L221-L245)): Asymmetric top padding & missing proof metrics**
   → Change the right-column cards' padding from `40px 0 40px 40px` to `48px 0 48px 40px` so both `CASE FILE` eyebrows align horizontally at `48px` from the top rule. Add bold `36px` `.d` outcome callouts above `GI Healthcare` (`CUSTOMER-FUNDED POC`) and `Auto Impartial` (`UK–ASIA CONSORTIUM`) to balance the `<2 YEARS` typographic weight on the left.

6. **Section 02 Corridor Register ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L200-L204)): Overused yellow column & vague entity name**
   → Change the `Where` column (`<td>` 1) from `#DFFF13` to `#FFFFFF` and use a `6px` `#DFFF13` status dot only on `Active` rows so Electric Yellow stays a sparse signal. Replace generic `"Tianjin partners"` with `"Binhai Zhongguancun Science Park (Tianjin)"` (once client-cleared) so AI answer engines index the specific institution.

7. **Section 05 Insights List ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L300-L304)): Dead `[In development]` links**
   → Do not wrap unpublished articles in `<a href="#events">`. Render unpublished rows as non-clickable `<div>` items with a `COMING Q4 2026` badge, or swap in two live migrated posts from `nexusstartupdiaries.com` (e.g., Manchester–China / 2026 Funding Map) so crawlers and buyers land on real content.

8. **All Placeholder Bracket Copy ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L136), [#L245](../design-canvas/HomeA.dc.html#L245), [#L364](../design-canvas/HomeA.dc.html#L364), [#L371](../design-canvas/HomeA.dc.html#L371))**
   → Delete `[Each case study published only with the client's written consent]` from the public DOM. Replace `[Response time to confirm]` with `"within two UK working days"`, `[Email to confirm]@nexuscreativehq.com` with `hello@nexuscreativehq.com`, and link `[page to publish]` to `/about#methodology`.

---

### 3. One Bold Hero Idea: The "Live Corridor Pulse" Gate

Turn the static X-aperture in [HomeA.dc.html](../design-canvas/HomeA.dc.html#L113-L123) into an interactive, data-driven **Corridor Gate**:
- Give the `<` and `>` chevrons dual-weight geometry (`stroke-width="2"` outer frame, crisp `1px` `#333333` echo lines stepping inward toward the center gate).
- Tie the central `#DFFF13` vertical gate line to the live clock: when London and China are simultaneously in working hours (`09:00–10:00 GMT` / `17:00–18:00 CST`), the yellow gate displays a subtle `4px` glowing pulse (`GATE OPEN · LIVE OVERLAP`). Hovering or focusing `London` highlights the `→ Into Asia` chevron in `#DFFF13` and dims inbound; hovering `Tianjin`, `Shanghai`, or `Hong Kong` highlights the `Into the UK ←` chevron and previews the exact entry route (`MOU Pipeline`, `S-Tron Cohort`, `HK Gateway`) inside the center gate. Fully keyboard-accessible via `focus-visible` and static under `prefers-reduced-motion`.

---

### 4. Broken, Misaligned, Low-Contrast or Inconsistent

- **Broken vertical alignment (`homeAB2-full-0.png`)**: Because the Aperture row uses `display: flex` with un-boxed padding (`32px` vs `24px`) while the `<dl>` stats row below uses a 4-column CSS Grid, the vertical borders between `London` / `1,400+` and `Aperture` / `CBBC` jog horizontally by ~10px.
- **Truncated screenshot / preview height (`homeAB2-full-3.png`, [HomeA.dc.html](../design-canvas/HomeA.dc.html#L406))**: `$preview.height: 5900` clips the bottom of the page mid-contact form—cutting off the new working-hours overlap box (`#L365-L370`), the `Send enquiry` button, and the entire `<footer>`. Increase preview height to `6500`.
- **Unrendered SSR tokens**: `{{lon}}`, `{{sha}}`, `{{overlap}}` rely on client-side JS ([HomeA.dc.html](../design-canvas/HomeA.dc.html#L410)); provide static fallback text in HTML so search/AI crawlers don't index raw handlebars.
- **Low-contrast micro-type**: `#7A7A7A` at `13px` `DM Mono` on `#0A0A0A` (`#corridor` and `#contact`, `4.6:1`) sits right on the WCAG AA floor; lift all `#7A7A7A` labels on `#0A0A0A` to `#9E9E9E` (`7.3:1`).

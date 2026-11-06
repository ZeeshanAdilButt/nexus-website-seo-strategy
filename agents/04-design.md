---
name: website-design
description: Gets a beautiful, on-brief design for a website. It first asks what design already exists (Claude Design canvas, Figma, a designer's build, a prototype). If none exists, it designs in Claude Design, gets outside critiques from Codex and Gemini, and checks every page against the facts.
---

You make sure the site looks excellent and says exactly what the owner wrote.

## Ask first

- **Is there a design already?** Claude Design canvas link, Figma file, a designer's working site, a prototype, or nothing.
- **Brand assets:** guidelines, logo files (SVG), fonts and licences, colours, photography, graphic elements.
- **Sites the owner likes,** and why: structure, feel, typography. Use them for structure only, never to copy a look.
- **Is the copy final,** or are we placing their prototype copy word for word?

## If a design exists

- Get the link and screenshot every page at 1440px (and at phone width in the browser pane).
- **Check it against the facts doc, page by page:** the H1s and copy word for word, the section order, brand colours and their rules (accent colours that must never fill a background), fonts, button sizes, motion rules, and placeholders that should be visible.
- **List every gap** as a fix list for the designer: what it says now, what the facts say, and the file or line. Also list what to keep.
- Suggest taste improvements as options (for example "replace grey section grounds with white and outlined cards"). Show them before and after.

## If no design exists: Claude Design

1. **Brand intake.** Turn the guidelines into tokens: colours with their usage rules, type scale, spacing, buttons, motion.
2. **Explore 2 or 3 genuinely different directions** for the homepage hero and one inner page, all using the owner's real copy. Avoid generic AI looks: purple gradients, everything centred, the same rounded card everywhere, emoji icons.
3. **Get outside critiques** of the screenshots:
   - `codex exec --sandbox read-only --skip-git-repo-check -i a.png -i b.png - < critique.txt`
   - `agy --model <gemini-model> --mode plan --add-dir <dir> --settings '{"permissions":{"allow":["read_file","list_dir","view_file"]}}' -p="..."`

   Ask for specific fixes: sizes, spacing, hierarchy, contrast, image use, what looks generic. Keep what both agree on. Reject anything that breaks the facts.
4. **Build the chosen direction** across all the key pages, in the owner's section order. Keep placeholders visible and clearly marked, never styled as final.
5. **Run a second critique round,** then polish: spacing rhythm, type scale, image crops, alignment and the mobile layout.
6. **Publish the canvas** with one artboard per page. Read the live `canvas.json` before each republish. Keep the canvas source in `design/canvas/`.

## Quality bar (what "beautiful" means here)

- **Hierarchy you can read at a glance:** one idea per section, generous white space, and a type scale with clear steps.
- **Real photography** over icons and stock. Images cropped to purpose.
- **The brand used with restraint:** an accent colour as an accent, plain section grounds, consistent buttons (at least 48px tall).
- **Motion only where it helps** (hover and focus states) and `prefers-reduced-motion` respected.
- **Accessible:** contrast that meets WCAG AA, visible focus, readable at 200% zoom.
- **Mobile first:** no sideways scrolling at 360px, and full-width buttons.

## Output

- Screenshots of every page.
- The canvas or Figma link.
- The fix list for any existing build.
- One recommended direction with a sentence on why. The other directions stay available "on the side".

---
name: website-content-migration
description: Moves existing articles and pages from an old site or blog platform to the new site, with clean addresses and a single 301 from every old address. Uses the owner's export where possible, otherwise fetches and converts each page, and checks every redirect.
---

You move old content to its new home without losing a single link.

## Ask first

- Will the owner send an export (with duplicates removed), or do we fetch it from the live site?
- Which content moves: all of it, or only what the owner chooses? Never cap what they asked for.
- Is there a second platform (for example a Ghost blog)? Does it move now, or stay linked and move later as an option?

## Steps

1. **Inventory.** List every old address: articles, podcasts, videos, events, core pages and broken pages. Note duplicates and off-topic items for the owner to decide on.
2. **Get the content.** Use the owner's export first. Otherwise fetch each page and extract the title, body, images, date and author:
   - for Ghost, use the Content API or the JSON export
   - for WordPress, use the REST API or a WXR export
3. **Convert each item** to Markdown with frontmatter: `title`, `summary`, `author`, `date`, `topic`, `format`, `image`, `image_alt`. Give it a readable slug made from the title, lowercase, hyphenated and stripped of emoji.
4. **Images.** Download them, convert to WebP or AVIF, resize, give them descriptive alt text, and rewrite their paths.
5. **Redirects.** Add one line per old address to `_redirects`:
   ```text
   /insight/100 /insights/why-most-pitches-fail-and-what-makes-a-startup-truly-investable 301
   ```
   Off-topic or merged items redirect to the closest topic page, never to a chain.
6. **Check after deploy.** Request every old address and confirm one 301 that lands on a 200 page. Log the results as proof.
7. **Gaps.** Report anything missing, such as publish dates the old pages don't show. Fill gaps from the owner's export. Never invent dates.

## Output

The content files, the images, `_redirects`, a redirect check log, and a list of the owner's decisions (duplicates, off-topic items, missing data).

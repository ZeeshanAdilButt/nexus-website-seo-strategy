---
name: website-client-messages
description: Writes every message a client or partner reads (WhatsApp, email, follow-ups, replies to price or deadline questions). It drafts from the facts first, then uses Codex only to make the wording more human, then re-checks the facts and saves the history with proofs.
---

You write messages that sound like the user wrote them, after months of working with the client.

## Process (always, in this order)

1. **Read the context.** The client's latest message (save it as `From <client>.txt`), what we have already sent, and the facts doc.
2. **Write the full draft yourself.** Use only facts you can prove. Keep the order simple:
   1. answer their worry first
   2. then the value, in concrete facts
   3. then the ask or the price
   4. then the support promise
3. **Hand it to Codex to make it human:**
   ```text
   codex exec --sandbox read-only --skip-git-repo-check -o out.txt - < prompt.txt
   ```
   The prompt gives the context, lists every fact that must not change, says "add no facts or promises", and sets the style rules below.
4. **Check Codex's version against your draft,** fact by fact. Fix anything it added or changed.
5. **Save it** in `proposals/YYYY-MM-DD/`. Once it's sent, rename it `Reply (sent).txt` and keep the attachments beside it. Map every claim to its evidence in `proofs/README.md`.

## Style

- **Channel:** WhatsApp, short paragraphs. Email, a subject line and short paragraphs.
- **Opening:** "Hi <name>," and then straight to the point. No thank-you openers such as "thanks for replying, I really appreciate it".
- **Follow-ups:** start directly. Never "one more thing" or "I forgot to mention".
- **Value, said positively.** For example: "a site that works for <client> rather than one you keep working on". No fear, no pressure, and no phrases like "far less to think about".
- **Price:** don't argue it. A discount is "a goodwill discount". Never itemise small extras the client asked for.
- **Under pressure** (travel, deadlines): take the pressure off first. For example: "we can launch with any pages waiting on your content hidden, then switch them on when they're ready."
- **Never say "placeholders" to a client.** Don't mention hosting or extras unless they asked.
- **No banned writing:** no em or en dashes, no semicolons, no emojis unless the user uses them, and no AI phrasing ("absolutely", "rest assured", "seamless", "leverage", "happy to help", "just wanted to").
- **Numbers:** only measured or sourced ones. When unsure, say less (for example "over 10 seconds on a fresh visit" rather than an unproven exact figure).

## Output

- The message, ready to paste, plus a list of what to attach.
- The proofs map.
- One line on anything the user should know before sending (for example "the speed test was run from abroad, so UK visitors may see slightly faster times").

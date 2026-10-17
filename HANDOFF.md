# HANDOFF.md

## Branch
dragginmaster/merge-links-column — merge eBay link + Proof columns into one.

## What I did
- index.html: merged the "eBay link" and "Proof" table columns into a single
  "Listing & proof" column (Don's call, 2026-10-17). The column holds:
  "View sold listing" link, eBay ID (tap-to-copy, as before), and a
  "Screenshot" text link that opens the full-size archived screenshot in a
  new tab (same destination the old thumbnail click opened).
- The old 130px thumbnail column is gone. A missing screenshot now shows a
  visible red "⚠ no screenshot" flag instead of the dashed placeholder box —
  a comp without proof must still look wrong at a glance (hard rule).
- Table min-width 880px -> 760px; the full table should now fit a laptop
  viewport with no horizontal scroll.
- Removed dead code: proofPlaceholder(), .proof / img.proofimg CSS.
- sw.js v31 -> v32 (index.html is in the shell cache).

## What's left
- Don reviews the Cloudflare preview; merge to main on his say-so.
  (Merge = auto-deploy to production.)

## Decisions
- Screenshot link probes the shot URL with `new Image()` and only renders
  the link on load; on error it renders the "no screenshot" flag. Same
  request count as the old thumbnails, no broken-image tabs.
- Kept the change desktop-safe: mobile only tightens padding, unaffected.

## Blockers
- None.

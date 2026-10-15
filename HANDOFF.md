# HANDOFF.md

## Branch
feat/guide-table-ref-id — Don's call: show the eBay listing ID under "View sold listing" in the main guide table (closes #15).

## What I did
- index.html: each "View sold listing ↗" cell now has the listing ID beneath it in small mono type (.lid CSS), tap-to-copy via clipboard API. The guide table is per-comp rows, so one row = one ID, no ambiguity.
- sw.js: v23 -> v24 (index.html changed, it's in the shell cache).

## What's left
- Nothing. Merge to main when ready; production auto-deploys on merge.

## Decisions made
- Placed under the link cell rather than the model-name column: the ID identifies the linked listing, so it sits directly beneath it. Kept the modal sale-row IDs too (harmless, useful in the chart view).

## Blockers
- None.

## How to verify
- Preview guide tab: every "View sold listing ↗" has the numeric ID under it; tap copies.

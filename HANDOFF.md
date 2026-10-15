# HANDOFF.md

## Branch
feat/comp-ref-ids — Don's call: every comp gets a reference ID (the eBay listing ID) so he and users can point at a specific comp.

## What I did
- build-price-list.py: new 4th column "Listing ID" (small mono, tap-to-copy via clipboard API); regenerated price-list.html — 351 comps, 140 tiers.
- index.html: trend modal sale rows now show the listing ID as a small muted second line under the date, tap-to-copy (.sid CSS).
- draggin-feedback.html: optional "Comp listing ID" field, visible only when the feedback kind is "Wrong or missing comp" (tiny show/hide toggle).
- sw.js: v20 -> v21 (index.html, price-list.html, draggin-feedback.html are all in the SW shell cache).

## What's left
- Nothing. Merge to main when ready; production auto-deploys on merge.

## Decisions made
- Used the eBay listing ID as the reference — already unique, permanent, and in comps.json. No second ID system.
- Price list got a real column; the trend modal got a stacked line under the date (its rows are a 3-part flex with no room for a column).
- Feedback field only appears for the "comp" kind so the form stays clean for other feedback.

## Blockers
- None.

## How to verify
- Preview: https://feat-comp-ref-ids.dragginmasters-trains.pages.dev/price-list.html — check the Listing ID column, tap one to copy.
- Preview index.html: open any 5/5 trend, check the sale rows show IDs under the dates.
- Preview draggin-feedback.html: pick "Wrong or missing comp" — the listing ID field appears.

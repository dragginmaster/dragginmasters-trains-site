# HANDOFF.md

## Branch
feat/comp-ref-ids — Don's call: every comp gets a reference ID (the eBay listing ID) so he and users can point at a specific comp. (Rebased onto main after cinder/price-list-351.)

## What I did
- build-price-list.py: new 4th column "Listing ID" (small mono, tap-to-copy via clipboard API). Kept Cinder's OG/Twitter meta-tag emission from hunt #8 — both features live in the builder now.
- price-list.html: regenerated via build-price-list.py (351 comps, 140 tiers) with both the OG tags and the Listing ID column.
- index.html: trend modal sale rows now show the listing ID as a small muted second line under the date, tap-to-copy (.sid CSS). Cinder's restored OG/Twitter tags + canonical kept.
- draggin-feedback.html: optional "Comp listing ID" field, visible only when the feedback kind is "Wrong or missing comp" (tiny show/hide toggle).
- sw.js: v21 -> v22 (index.html, price-list.html, draggin-feedback.html are all in the SW shell cache).

## What's left
- Nothing. Merge to main when ready; production auto-deploys on merge.

## Decisions made
- Used the eBay listing ID as the reference — already unique, permanent, and in comps.json. No second ID system.
- Price list got a real column; the trend modal got a stacked line under the date (its rows are a 3-part flex with no room for a column).
- Feedback field only appears for the "comp" kind so the form stays clean for other feedback.
- price-list.html was conflicted after the rebase (both branches regenerated it) — resolved by regenerating from the merged builder, not by hand-merging HTML.

## Blockers
- None.

## How to verify
- Preview: https://feat-comp-ref-ids.dragginmasters-trains.pages.dev/price-list.html — Listing ID column present, tap one to copy; view-source shows og:title tags.
- Preview index.html: open any 5/5 trend, sale rows show IDs under the dates.
- Preview draggin-feedback.html: pick "Wrong or missing comp" — the listing ID field appears.

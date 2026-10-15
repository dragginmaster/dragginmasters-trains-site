# HANDOFF.md

## Branch
regen/drop-pulled-comp — regen after data PR #10 pulled bad comp 298717342120.

## What I did
- Fresh-synced data repo (399 comps, bad comp gone) and site main, then python3 build-price-list.py.
- price-list.html: 399 comps / 180 tiers; Listing ID column and print button intact.
- sw.js v25 -> v26 (price-list.html is in the shell cache).

## What's left
- Nothing. Merge to main; production auto-deploys.

## Blockers
- None.

## How to verify
- price-list.html has 399 rows and no 298717342120.

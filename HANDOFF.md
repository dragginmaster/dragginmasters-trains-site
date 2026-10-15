# HANDOFF.md

## Branch
regen/pull-10-comps — regen after data PR #11 pulled 10 best-offer comps.

## What I did
- Fresh-synced data (389 comps) and site main, then python3 build-price-list.py.
- price-list.html: 389 comps / 179 tiers; all 10 pulled IDs verified absent.
- sw.js v26 -> v27 (price-list.html is in the shell cache).

## What's left
- Nothing. Merge to main; production auto-deploys.

## Blockers
- None.

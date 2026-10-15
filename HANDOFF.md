# HANDOFF.md

## Branch
cinder/nscale-comps-9-site — Hunt #9: push the price guide from 351 to 400 comps.

## What I did
- price-list.html: regenerated via build-price-list.py (400 comps, 181 tiers). OG/Twitter tags present.
- sw.js: v24 -> v25 (price-list.html changed, it's in the shell cache).

## What's left
- Nothing. Merge to main when ready; production auto-deploys on merge.

## Decisions made
- Data PR #9 (dragginmasters-comps-data) merged first: 49 net-new N-scale comps, plus DCC-ready corrections for 800769438778 (InterMountain SD45-2) and 117413421683 (Atlas C630).

## Blockers
- None.

## How to verify
- Production guide should show 400 comps after deploy.

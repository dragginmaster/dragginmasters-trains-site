# HANDOFF.md

## Branch
cinder/road-cleanup-site — road-name housekeeping + Notes column.

## What I did
- Data repo: normalized all 432 comp road fields (384 distinct values -> 84).
  Road column now holds the road name only; road numbers and paint-scheme
  details moved into notes. 3 comps with undeterminable road names left for
  Don's review page (168648585326, 236966716655, 398125182899). COMPS.md
  updated with the road-name-only rule.
- Site: build-price-list.py now emits a Notes column (was Sold date / Road
  name / Price / Listing ID). price-list.html regenerated: 432 comps / 195 tiers.
- sw.js v30 -> v31 (price-list.html is in the shell cache).

## What's left
- Merge to main; production auto-deploys. Verify live count reads 432.

## Blockers
- None.

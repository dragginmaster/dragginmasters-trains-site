# HANDOFF.md

## Branch
cinder/price-list-312 — regenerate price-list.html for 12 new N-scale comps (hunt #6)

## What I did
- `price-list.html`: regenerated with `python3 build-price-list.py` — now 312 comps / 137 tiers (was 300/132). OG tags intact (build script emits them).
- `sw.js`: bumped `CACHE` from `dragginmasters-v17` to `dragginmasters-v18`.
- Data repo: PR #6 merged — comps.json 300 → 312, plus 12 new + 2 refreshed proof JPGs under `shots/`.

## The 12 new comps (all proof screenshots personally read)
New models:
1. Atlas U23B DC Used D&H Bicentennial #1776 — $130.00, 2026-10-10 (800780813034)
2. Kato C30-7 DC Used NS #8050 — $60.00, 2026-10-14 (198708465925); sold the morning it was banked
3. Bachmann DD40AX DC Used UP "The Centennial" — $110.00, 2026-09-28 (407243968057)
4. Life-Like GP20 DCC Used UP #474 — $99.95, 2026-10-09 (257767897372); CONFLICT FLAGGED: title "DCC" vs specifics "Analog", banked as DCC per title
5. Life-Like SW9 DC New ACL #666 — $75.00, 2026-10-11 (227552441420)
Thin-tier fills:
6. Atlas GP38-2 DC Used Santa Fe #2370 — $64.00, 2026-09-12 (128071405950); Kato mechanism
7. Kato F40PH DC Used Amtrak #346 — $75.00, 2026-08-23 (227473154917)
8. Kato AC4400CW DC Used BNSF #5615 — $79.95, 2026-09-14 (820101401679)
9. Bachmann GP40 DC Used B&O Chessie #4115 — $29.99, 2026-10-07 (127822510429); ANOMALY FLAGGED: seller-disclosed wear (damaged ladders, missing truck arm/couplers), tested running
10. Atlas RS-3 DC New D&H #4082 — $65.00, 2026-09-13 (307077961601); New: Other
11. Atlas VO-1000 DC Used Detroit Terminal #102 — $109.95, 2026-10-10 (820221977104); best offer accepted
12. Kato Mikado 2-8-2 DC Used Pennsylvania — $107.00, 2026-08-17 (137589622260); USRA Heavy, no road number stated

## Hunt notes
- 6 already-banked duplicate listings were caught and dropped during the hunt (the browser kept surfacing them); final hunt used a full 310-ID exclusion list, which worked.
- 2 listings failed final sold-proof verification and were rejected (ended-by-seller, multi-quantity BIN).

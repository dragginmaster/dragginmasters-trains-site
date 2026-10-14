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

---

# HANDOFF.md — Hunt #7

## Branch
cinder/price-list-325 — regenerate price-list.html for 13 new N-scale comps (hunt #7)

## What I did
- `price-list.html`: regenerated with `python3 build-price-list.py` — now 325 comps / 141 tiers (was 312/137). OG tags intact (build script emits them).
- `sw.js`: bumped `CACHE` from `dragginmasters-v18` to `dragginmasters-v19`.
- Data repo: PR #7 merged — comps.json 312 → 325, plus 13 new proof JPGs under `shots/`.

## The 13 new comps (all proof screenshots personally read)
New models (first in guide):
1. Con-Cor U50 DC Used SP #9852 — $142.50, 2026-10-13 (206605880294); runs
2. Model Power FA2 DC Used Southern #810 — $39.99, 2026-09-29 (820161326352); tested, runs forward and reverse
3. Life-Like SW1200 DC New GN #16 — $69.00, 2026-10-06 (287610486107); best offer accepted
New tiers:
4. Atlas S-4 DCC+Sound New ATSF #1517 — $220.00, 2026-10-13 (117458817346); CONFLICT FLAGGED: title "DCC sound" vs specifics "Analog", banked as DCC+Sound per title
5. Atlas C424 DCC+Sound New Conrail #2486 — $289.99, 2026-09-24 (158155198477); Phase 1, ex-Erie Lackawanna
6. Atlas GP30 DCC-ready New PRR #2219 — $150.00, 2026-08-09 (127993528443); Master Line Silver Series, NOS
7. Atlas H15-44 DCC-ready New FM Demo #1502 — $255.00, 2026-08-02 (287485737789); 14-bid auction
8. Atlas RS-1 DC New Green Mountain #405 — $114.99, 2026-10-07 (800767720557); tested
Thin-tier fills:
9. Atlas U23B DC Used WP #2252 — $77.00, 2026-08-14 (137597120697); runs slow
10. Bachmann DD40AX DC Used #6926 — $125.00, 2026-08-04 (236966716655); no road name stated
11. Kato C30-7 DC Used CSX #7012 — $100.00, 2026-10-06 (287620835086); weathered, tested
12. Kato PA-1 DC Used SP Black Widow — $42.00, 2026-10-06 (198676599432); title lists "Kato | Con Cor", silver paint overspray noted
13. InterMountain F7 DC Used M&StL #407 — $99.00, 2026-07-18 (236946269840); ANOMALY FLAGGED: no coupler hoses, front coupler needs help; runs and lights

## Hunt notes
- Bachmann FT target dropped: Bachmann never made an N-scale FT (HO only); replaced with Model Power FA2 + Life-Like SW1200.
- Kato E8 candidate 307200771495 was already banked (as "Kato E8A"); caught by the dupe check and dropped.
- Two replacement candidates (GS-4 327391529045, GG1 920033629089) were also already banked — the exclusion list given to the browser was stale; final hunt used a 2-ID focused exclusion and worked.

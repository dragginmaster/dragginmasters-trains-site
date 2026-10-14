# HANDOFF.md

## Branch
cinder/nscale-price-list-5 — regenerate price-list.html for 24 new N-scale comps (hunt #5)

## What I did
- `price-list.html`: regenerated with `python3 build-price-list.py` — now 300 comps / 132 tiers (was 276/121). OG tags intact (build script emits them).
- `sw.js`: bumped `CACHE` from `dragginmasters-v16` to `dragginmasters-v17`.
- Data repo: PR #5 merged — comps.json 276 → 300, plus 24 new + 5 replacement proof JPGs under `shots/`.

## The 24 new comps (all proof screenshots personally read)
Wave 1:
1. Atlas C424 DCC+Sound New Erie Lackawanna #2408 — $208.75, 2026-07-23 (236952144463); Master Gold/LokSound; photo shows #2406, title says #2408
2. Atlas Dash 8-40B DCC-ready New LMX #8554 — $149.99, 2026-09-26 (147427551416); best offer accepted
3. Atlas SD60 DCC+Sound New NS GoRail — $150.00, 2026-08-11 (336737087997); listed New (Other), open box
4. Atlas H15-44 DCC-ready Used Rio Grande #151 — $70.00, 2026-10-10 (198683938978)
5. Bachmann EMD GP7 DCC Used CNJ #1523 — $100.00, 2026-09-03 (358891815090)
Wave 2:
6. Atlas GP-9 DCC-ready New SP #5629 — $100.00, 2026-10-01 (178523408222); listed New (Other)
7. Bachmann GP38-2 DCC-ready New Milwaukee Road #355 — $52.00, 2026-09-22 (168690862919); 61753, Next18 plug
8. Atlas GP7 Ph.1 DCC-ready New NYC #5609 — $70.00, 2026-09-22 (147575976754); listed New (Other)
9. Atlas SD60 DCC-ready New BNSF #1452 — $90.00, 2026-10-13 (178367409187); SD60M, best offer accepted, listed New (Other)
10. Kato SD40-2 DCC Used AT&SF #5077 — $105.58, 2026-10-03 (336795569436); TSC decoder
11. Kato SD40-2 DCC-ready New CF&E #3487 — $170.00, 2026-09-05 (287378742651); title "DC / DCC Ready" → DCC-ready
12. Kato SD45 DCC Used SP #7514 — $97.00, 2026-10-07 (128111713455); TCS decoder, 1 bid
Wave 3:
13. Bachmann H16-44 DC Used N&W #147 — $60.00, 2026-09-15 (298677392743); 61455, new model tier
14. Life-Like GP38-2 DC Used UP — $54.88, 2026-10-03 (860005483377); Proto N 920-75034, new model tier
15. Fox Valley GP60 DCC Used SP #9726 — $164.95, 2026-09-05 (820087384365); CONFLICT FLAGGED: title "DCC Equipped" vs specifics "Analog", banked as DCC; new model tier
16. Atlas GP30 DCC-ready New NKP #904 — $78.89, 2026-09-19 (237064732640); CONFLICT FLAGGED: title "DCC Ready" vs specifics "Analog"; new model tier
17. Atlas RS-1 DC Used Santa Fe #2396 — $29.00, 2026-10-13 (800773417942); 4402, 4 bids, new model tier
18. Kato SD70M DCC Used UP #4841 — $79.00, 2026-10-12 (168785886036); 176-7506 flared radiators, new model tier
19. Bachmann GP40 DC Used Santa Fe #3500 — $49.95, 2026-10-05 (287607646855); new model tier
20. Kato C44-9W DCC+Sound Used SP — $120.00, 2026-08-25 (800499209310); thin tier x2
21. Atlas/Kato ALCO RS-11 DC Used Maine Central #802 — $119.99, 2026-10-09 (128031705491); 42604, thin tier x2
22. Bachmann SD45 DCC+Sound Used Rio Grande #5336 — $129.99, 2026-09-26 (800705764983); 66453, best offer accepted; new tier
23. Atlas (Kato-made) U25B DC Used Conrail #2627 — $46.53, 2026-09-03 (198599287784); Phase IIa, 2 bids, thin tier x2
24. Bachmann SD45 DCC-ready New UP — $63.99, 2026-07-25 (158113044745); Spectrum 82763, thin tier x2

## Decisions made
- Atlas C425, Bachmann FA2, InterMountain GP10: no N-scale versions exist — replaced with Atlas GP30, Atlas RS-1, Kato SD70M, Bachmann GP40.
- Dropped: 3 already-banked duplicates (Bachmann SD45 327294027089, Atlas/Kato U25B 407235668463, + wave-1 GP-9/GP38-2/FA-1), 2 failed-verification listings (Spectrum SD45 298604870829, etc.).
- Title/specifics control conflicts (Fox Valley GP60, Atlas GP30): banked per title, conflict flagged in note.
- comps.json (117KB) exceeded GitHub MCP push_files argv limit (~120KB) — pushed via browser upload flow instead.

## What's left
- Push site branch `cinder/nscale-price-list-5` (approval), open site PR, merge.
- Verify production shows 300 comps; sync local main; delete local + remote feature branches.

## How to verify
- comps.json count → 300; `grep -c "300 comps" price-list.html` → 1.
- Production: https://dragginmasterstrains.com/price-list → guide shows 300 comps after both PRs merge.

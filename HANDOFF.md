# HANDOFF.md

## Branch
cinder/nscale-price-list-4 — regenerate price-list.html for 10 new N-scale comps (hunt #4)

## What I did
- `price-list.html`: regenerated with `python3 build-price-list.py` — now 276 comps / 121 tiers (was 266/116). OG tags intact (build script now emits them).
- `sw.js`: bumped `CACHE` from `dragginmasters-v15` to `dragginmasters-v16`.
- Data repo branch `cinder/nscale-comps-4`: comps.json 266 → 276, plus 10 proof JPGs under `shots/`. Committed locally; nothing pushed yet.

## The 10 new comps (all proof screenshots personally read)
1. Atlas Dash 8-40B DC New CSX #5933 — $75.00, 2026-09-02 (128051438913); auction, 1 bid
2. Atlas GP38-2 DCC-ready New GMTX #2346 — $133.00, 2026-09-06 (287567784870); title "DC / (DCC-Sound Ready)", banked as DCC-ready per decoder-ready rule
3. Bachmann 2-8-0 Consolidation DC Used Santa Fe #4821 — $33.50, 2026-10-13 (920002708787)
4. Bachmann Spectrum GE 44 Ton Switcher DCC New PRR — $109.00, 2026-10-12 (147620113321)
5. Atlas S-2 DCC+Sound Used ATSF #2357 — $139.99, 2026-08-02 (318643709298); factory DCC and Sound, LNIB
6. Kato F3 DC Used Burlington Northern #710 — $81.00, 2026-10-13 (800781055422); F3A 176-1201, new model tier
7. Kato E8 DC Used Southern Railway #2925 — $60.00, 2026-10-13 (920033682742); new model tier
8. Kato GS-4 DC New Southern Pacific 4449 Daylight — $290.00, 2026-10-13 (327391529045); auction, 4 bids; new model tier
9. Atlas VO-1000 DC New Santa Fe — $71.00, 2026-09-05 (257710675037); test run only, auction 11 bids; new model tier
10. InterMountain F7 DC Used Great Northern #307B — $71.00, 2026-10-05 (267798470776); F7B unit, control unspecified (standard analog), auction 14 bids; new model tier

## Decisions made
- Hunt #4 ran in two browser sessions (first environment retired mid-hunt after 4 targets; resumed cleanly).
- GP38-2 GMTX: "DCC-Sound Ready" in title → DCC-ready per the decoder-ready conflict rule (joins existing DCC-ready tier, now x3).
- InterMountain F7B: control unspecified → DC with note (standard analog).
- Hunts bank directly per COMPS.md hard rules — no triage round.

## What's left
- Push data branch `cinder/nscale-comps-4` (comps.json via MCP push — approval; 10 JPGs via browser upload).
- Open data PR, merge it FIRST.
- Push site branch `cinder/nscale-price-list-4`, open site PR, verify Cloudflare preview, merge.
- Verify production shows 276 comps; sync local main; delete local + remote feature branches.

## How to verify
- comps.json count → 276; `grep -c "276 comps" price-list.html` → 1.
- Production: https://dragginmasterstrains.com/ → guide shows 276 comps after both PRs merge.

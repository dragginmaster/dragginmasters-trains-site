# HANDOFF.md

## Branch
cinder/nscale-price-list-3 — regenerate price-list.html for 10 new N-scale comps (hunt #3)

## What I did
- `price-list.html`: regenerated with `python3 build-price-list.py` — now 266 comps / 116 tiers (was 256/111).
- `sw.js`: bumped `CACHE` from `dragginmasters-v13` to `dragginmasters-v14` (mandatory per AGENTS.md).
- Data repo branch `cinder/nscale-comps-3` (in `~/workspace/projects/dragginmasters-comps-data`): comps.json 256 → 266, plus 10 proof JPGs under `shots/`. Committed locally as 91d0f7c; nothing pushed yet.

## The 10 new comps (all proof screenshots personally read)
1. Kato GG1 DC Used PRR #4913 — $85.00, 2026-10-12 (920033629089)
2. Kato AC4400CW DC Used BNSF #5624 — $99.99, 2026-10-03 (127866624088)
3. Atlas RS-3 DC New Norfolk and Western #307 — $39.99, 2026-10-10 (117429710264); banked as DC, note: stock Atlas 4202 is analog DC
4. Kato SD70ACu DCC+Sound New CP #6644 — $279.00, 2026-09-15 (236964435390)
5. Kato F40PH DCC-ready New Amtrak #405 — $101.95, 2026-08-09 (127903503138); title says DC, specifics say DCC-ready; multi-quantity (5 sold)
6. Atlas Dash 8-40B DCC-ready New LMX #8565 — $89.99, 2026-08-09 (287499397854); title "DC Analog Decoder Ready", banked as DCC-ready per decoder-ready rule
7. Bachmann EMD F7 DCC Used Norfolk Southern #4270 — $49.99, 2026-07-21 (127974531820); specifics Control System=Analog but Features="DCC fitted", banked as DCC
8. Kato P42 Genesis DCC+Sound New Amtrak #203 Lifesaver — $330.65, 2026-08-05 (177764581918); multi-quantity (2 sold)
9. InterMountain SD40-2 DC Used CSX #8833 — $129.95, 2026-10-05 (820206533549); best offer accepted
10. Kato Mikado 2-8-2 DC New Southern Pacific #3303 — $140.00, 2026-10-09 (267807926054)

## Decisions made
- IM SD40-2 eBay 198504789559 ($160.69 BN #6332) was already banked — dropped as duplicate, replaced with CSX #8833 (820206533549).
- Kato P42 eBay 336756125101 and Kato Mikado eBay 189020855993 were already banked — dropped as duplicates, replaced.
- Duplicate handling: the P42 and Mikado dupes were never appended; the IM SD40-2 dupe was caught before banking. shots/189020855993.jpg was restored from main after an overwrite during dupe processing.
- Hunts bank directly per COMPS.md hard rules — no triage round ("triage pages are for audits, not hunts").

## What's left
- Push data branch `cinder/nscale-comps-3` to GitHub (text via MCP push — approval card; 10 JPGs via browser upload to github.com, binary-safe).
- Open data PR, merge it FIRST (guide reads comps.json from the data repo).
- Push site branch `cinder/nscale-price-list-3`, open site PR, verify Cloudflare preview, merge.
- Verify production shows 266 comps; sync local main; delete local + remote feature branches.

## How to verify
- `python3 -c "import json; d=json.load(open('comps.json')); print(len(d['comps']))"` in data repo → 266.
- `grep -c "266 comps" price-list.html` → 1.
- Production: https://dragginmasterstrains.com/ → guide shows 266 comps after both PRs merge.

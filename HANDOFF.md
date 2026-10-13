# HANDOFF.md

## Branch
cinder/nscale-price-list — regenerate price-list.html for the 10 new N-scale comps

## What I did
- `price-list.html`: regenerated with `python3 build-price-list.py` — now 256 comps / 108 tiers (was 236). New tiers: Kato Big Boy 4-8-8-4 (DC + DCC), Kato E7A A-A Set (DC, factory 106-0440 2-unit set — own tier per Don), Kato SD40-2 (DCC-ready + DCC), Kato C44-9W (DCC+Sound), Atlas SD60 (DCC-ready + DCC+Sound), Atlas S-2 (DCC+Sound), Athearn F59PHI (DCC+Sound).
- `sw.js`: bumped `CACHE` from `dragginmasters-v11` to `dragginmasters-v12` (mandatory per AGENTS.md).
- Fixed a stale path: `build-price-list.py` reads `~/workspace/dragginmasters-comps-data/comps.json`, which doesn't exist — added a symlink `~/workspace/dragginmasters-comps-data -> ~/workspace/projects/dragginmasters-comps-data` so the documented command works.

## What's left
- Push branch + open PR with the Cloudflare preview URL; merge after Don reviews the preview.
- Data repo PR (dragginmaster/dragginmasters-comps-data, branch `cinder/nscale-new-comps`): comps.json + 10 screenshots still need to reach GitHub — the MCP push path can't carry binary files, so this goes up via a browser upload to github.com (Don signs in via takeover). The site loads comps.json at runtime from the data repo's raw URL, so the new tiers appear in the live app only after the data PR merges.

## Decisions made
- PA-1 gold-bonnet outlier ($320.99) dropped from the standard tier per Don; E7A factory A-A sets banked as their own tier per Don; the $380 E7A comp failed the verification gate (listing ended by seller, sale unproven — hard rule 1) and was replaced with the $299.99 factory set (verified sold Oct 4).
- SD40-2 $99.49 banked as DCC-ready with a note (title says DC, description confirms decoder-ready lighting board) per Don's call.
- Hunts now bank directly per hard rules — Don: "triage pages are for audits, not hunts."

## Blockers
- Data-repo binary upload needs Don's GitHub sign-in in the browser (one takeover).

## How to verify
- `grep -c "Big Boy 4-8-8-4" price-list.html` → 2; page lede says "256 comps".
- Preview: `https://cinder-nscale-price-list.dragginmasters-trains.pages.dev/price-list.html` — new tiers listed with sold prices and dates.

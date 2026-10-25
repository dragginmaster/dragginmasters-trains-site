# HANDOFF.md

## Branch
cinder/stale-rescue-oct25 — price-list regen for the Oct 25 stale-rescue hunt (guide 757 → 759).

## What I did
- Data repo (branch cinder/stale-rescue-oct25, separate PR): banked 2 verified
  N-scale comps that revive the two tiers due to flip STALE on Oct 25:
  Atlas C628 DC (ALCO demonstrator #628-3, $108.50, sold Oct 1) and Kato GS-4
  DCC-ready (Southern Pacific #4449, Kato 126-0301, $265.00, sold Oct 23).
  Each verified page-by-page on eBay with its proof screenshot read by Cinder
  before banking. Guide 757 → 759 comps (N 421 → 423, HO unchanged 336).
- This repo: re-ran build-price-list.py against the updated data repo —
  price-list.html now carries 759 comps / 424 tiers.
- sw.js v46 -> v47 (main had advanced past the expected v42; bumped from the
  actual current version).
- 3 judgment-call listings were NOT banked; they are on a small audit form
  for Don's rulings.

## What's left
- Don reviews the Cloudflare preview; merge to main on his say-so.
  (Merge = auto-deploy to production.)
- Don's audit rulings come back via the form; any "Bank it" cards get banked
  in a follow-up branch.

## Decisions
- The GS-4's DCC-ready control rests on the Kato item number 126-0301 in the
  title and box label (that SKU is the factory decoder-ready version) — the
  same basis as the tier's existing comp (137550791136, filed by Don's own
  workflow with the SKU in the note).

## Blockers
- None.

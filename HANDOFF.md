# HANDOFF.md

## Branch
cinder/ho-hunt-25 — price-list regen for the Oct 22 HO comp hunt (guide 596 → 621).

## What I did
- Data repo (branch cinder/ho-hunt-25, separate PR): banked 25 verified HO
  comps from eBay sold listings, every one screenshot-verified against the
  sold page (no best-offer sales, no struck-through prices). Guide goes
  596 → 621 comps; HO 175 → 200. 23 tiers touched (Atlas RS-3/GP38/U23B/U28C,
  Kato SD40/SD40-2 DCC-ready, Proto 2000 GP30/GP38-2/GP18/E7A/E8/0-8-0,
  blue-box GP9/SD9/F7A/F7A+F7B, Spectrum steam, BLI 2-8-0, Stewart F3B,
  Trainman GP38-2, Bachmann GP30).
- This repo: re-ran build-price-list.py against the updated data repo —
  price-list.html now carries 621 comps / 311 tiers.
- sw.js v41 -> v42.
- 24 judgment-call listings were NOT banked; they went to an audit form for
  Don's rulings (bank/ trash per card). One verified spare (Proto 2000 GP30
  B&O #6921, $49) is held in the hunt folder, unbanked.

## What's left
- Don reviews the Cloudflare preview; merge to main on his say-so.
  (Merge = auto-deploy to production.)
- Don's audit rulings come back via the form; any "Bank it" cards get banked
  in a follow-up branch.

## Decisions
- A Bachmann SD40-2 (CSX #8211, $79.99) that the browser pass called firm
  was demoted to the audit pile after screenshot review: the page shows
  "or Best Offer" and never proves the full price was paid. Per COMPS.md
  Rule 5 / "when in doubt, skip", it is Don's call, not the hunt's.
- A Bachmann SD40-2 graded C-2 "Restoration Required / needs reassembly"
  also went to audit instead of banking.

## Blockers
- None.

# HANDOFF.md

One per branch. Update this file on your branch BEFORE opening the PR, so the
reviewer (human or AI) can see the full picture without reading every commit.

## Branch
cinder/price-list-351 — Hunt #8: regenerate price list for 351 comps.

## What I did
- build-price-list.py: added Open Graph/Twitter Card meta tags to the generated
  price-list.html head (they were stripped by an earlier regen; now the builder
  emits them so future regens can't wipe them).
- price-list.html: regenerated via build-price-list.py (351 comps, 140 tiers).
- index.html: restored OG/Twitter Card tags + canonical link (were stripped
  from main at some point after PR #6; restored from cinder/og-tags-restore).
- sw.js: bumped CACHE v20 -> v21 (site files changed).

## What's left
- Nothing. Merge to main when ready; production auto-deploys on merge.

## Decisions made
- Fixed the builder script, not just the generated HTML — otherwise the next
  comp-banking regen wipes the OG tags again.
- Tier count went 141 -> 140: the phantom "Bachmann SD45 DCC-ready"
  (non-Spectrum) tier was removed after its only data point (158113044745)
  was verified as actually a Spectrum 82763; it now sits in the
  Bachmann Spectrum SD45 DCC-ready tier.

## Blockers
- None.

## How to verify
- Preview URL: https://cinder-price-list-351.dragginmasters-trains.pages.dev/price-list
- Header should read "351 comps below, updated 2026-10-15."
- View-source on / and /price-list.html should show og:title meta tags.

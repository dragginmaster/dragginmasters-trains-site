# HANDOFF.md

One per branch. Update this file on your branch BEFORE opening the PR, so the
reviewer (human or AI) can see the full picture without reading every commit.

## Branch
fix/print-price-list — Don reported the footer "Full price list (printable)" link doesn't actually print.

## What I did
- build-price-list.py: added a "Print this list" button (window.print()) under the topnav, plus @media print CSS (hides nav/button, white background, light table headers instead of ink-eating navy, tier cards avoid page breaks, smaller type).
- price-list.html: regenerated via build-price-list.py (256 comps, 111 tiers). The button and CSS live in the builder so future regens keep them.

## What's left
- Nothing. Merge to main when ready; production auto-deploys on merge.

## Decisions made
- Fixed the builder script, not the generated HTML — otherwise the next comp-banking regen wipes the fix.
- Print CSS swaps the navy table headers for light gray: navy headers print as solid black bars and eat ink.
- No sw.js bump needed: price-list.html is not in the SW SHELL cache (it's a plain static page), so no stale-cache risk.

## Blockers
- None.

## How to verify
- Preview URL: https://fix-print-price-list.dragginmasters-trains.pages.dev/price-list.html
- Click "Print this list" — the browser print dialog should open with a clean white page, no nav, no button.

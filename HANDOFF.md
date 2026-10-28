# HANDOFF.md

## Main — pushed direct by Cinder on Don's "Push it" (Oct 28)
Bank-82 publish: the last of the pool-harvest audit set lands on production.

## What I did
- Data repo (main, direct pushes, no PR — Don's Plan B pattern):
  - comps.json: banked 82 of the 91 audit-BANK items (commit 6c0aed7).
    Guide 1,090 -> 1,172 (all HO). Every field page-confirmed from the
    sold-listing screenshots; road numbers filed under the painted number
    where title and photo disagreed (notes carry the corrections).
  - 9 of the 91 were held out of the bank because a required field is not
    determinable from the page (control: 158298389991, 189033081602,
    307205956508, 336809030760; condition: 128096322097, 206589022683,
    227535743764, 297016224739; both: 237113217754). Don ruled all 9
    TRASH; recorded in handled-ids.json with reasons (commit d9ebb07:
    banked 416 -> 498, rejected 432 -> 441).
  - All 82 proof shots uploaded to shots/ on main (4 commits:
    c8f8c6e, 06eedab, 7f6ad31, d73148c; verified 82/82 present,
    sizes matching). The full 91 shots also sit on branch
    cinder/pool-harvest from the morning's upload round.
- This repo: re-ran build-price-list.py against data main at 1,172 —
  price-list.html now carries 1,172 comps / 653 tiers.
- sw.js v64 -> v65.

## What's left
- Nothing pending on this publish. Production verification: price-list
  serves "1172 comps below, updated 2026-10-28".

## Decisions
- 800730754280 (Genesis SD70M UP): title said "BRAND NEW" but the eBay
  condition field read Used — filed Used, same call as 198596606064 in
  the same set; road #4454 restored from the audit checker's box-label
  read and noted in the comp.
- Bare seller grades wrapped to guide style: "Used (C-8 Like New)",
  "Used (C-7 Excellent)", "New (seller grade C-9)".

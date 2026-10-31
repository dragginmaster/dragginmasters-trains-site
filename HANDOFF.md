# HANDOFF.md

## Main — pushed direct by Cinder on Don's "Go" (Oct 31)
Oct 30 hunt publish: 150 new comps land on production.

## What I did
- Data repo (main, direct push, no PR — Don's pattern):
  - comps.json: +150 comps from the Oct 30 hunt (commit 8baf646).
    Guide 1,172 -> 1,322 (N and HO mix; trend-tier fills plus new
    tiers). Every field verified from the sold-listing page and its
    proof screenshot; "best offer accepted" listings never banked.
  - All 150 proof shots uploaded to shots/ on main via the web
    upload flow (commits follow this entry).
  - 7 judgment calls held out of the count and sent to Don on an
    audit form (Oct 30 hunt audit): a Bachmann Spectrum 4-8-4 tier
    question, a New-vs-Used conflict, a DC-vs-"DCC fitted" conflict,
    a "Sold As Is" GP18, and three illustrated-lid-box Athearns.
- This repo: re-ran build-price-list.py against data main at 1,322 —
  price-list.html now carries 1,322 comps / 655 tiers.
- sw.js v65 -> v66.

## What's left
- Don's rulings on the 7 audit items; banked ones publish with the
  next hunt.
- Production verification: price-list serves "1322 comps below,
  updated 2026-10-30".

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

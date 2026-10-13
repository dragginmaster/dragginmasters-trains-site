# HANDOFF.md

## Branch
cinder/og-tags-restore — restore Open Graph/Twitter Card tags so Facebook shares render pretty previews

## What I did
- `index.html`: re-added the canonical link + 8 og:/twitter: meta tags (og:title, og:description, og:type, og:url, og:image, twitter:card=summary_large_image, twitter:title, twitter:description), all absolute URLs. og:image is `https://dragginmasterstrains.com/icon-512.png`.
- `build-price-list.py`: added the same OG/Twitter tag block to the generated `<head>`, with the comp count dynamic (`%%NCOMPS%% verified comps and counting`) — previously the tags were hardcoded in price-list.html and every regen wiped them.
- `price-list.html`: regenerated (266 comps / 116 tiers) — now carries the OG tags.
- `sw.js`: bumped `CACHE` from `dragginmasters-v14` to `dragginmasters-v15`.

## Why
Don asked why Facebook shares don't look pretty. The tags were added this morning (PR #2, commit 3dad084) but commit 4acebc6 ("docs: point comp hunters at COMPS.md", 10:21 AM) stripped them from both index.html and price-list.html — looked accidental (commit message is about docs). Separately, build-price-list.py never emitted OG tags, so each regen would have wiped them anyway; that's fixed now.

## What's left
- Push branch, open PR, merge (then Cloudflare auto-deploys).
- After deploy: re-scrape both URLs in Facebook's Sharing Debugger (https://developers.facebook.com/tools/debug/) so Facebook drops its cached plain preview. No login needed for the debugger.

## How to verify
- `grep -c "og:" index.html price-list.html` → 5 and 5.
- Sharing Debugger on https://dragginmasterstrains.com/ shows title + description + image.

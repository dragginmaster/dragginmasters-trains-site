# HANDOFF.md

## Branch
fix/sw-never-undefined — harden the service worker's fetch handler + v23.

## What I did
- sw.js: both fetch-handler catch paths could resolve `undefined` (cache miss + network failure), which the browser surfaces as net::ERR_FAILED. Now the page fallback serves index.html or an honest offline page, and the comps.json fallback serves an empty JSON array. `respondWith` can never get undefined again.
- sw.js: CACHE v22 -> v23.

## Why
Don's phone showed "Webpage not available / net::ERR_FAILED" for price-list.html and draggin-feedback.html (both 308-redirected by Cloudflare) while the homepage loaded. Verified: the pages load fine in a fresh browser profile and in a second browser on his phone — the failure is stale/corrupted SW cache state on his main browser, left over from the v19 -> v10 -> v20 -> v22 churn on 2026-10-15. A fresh v23 install repopulates the cache and its activate step deletes the old caches, so affected browsers self-heal on the next visit — no manual cache clearing needed.

## What's left
- Nothing. Merge to main when ready; production auto-deploys on merge.

## Blockers
- None.

## How to verify
- After merge + deploy, open the site in any browser that showed the error and just visit — the v23 SW installs on navigation and heals the cache. price-list.html and draggin-feedback.html should load.

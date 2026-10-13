# HANDOFF.md

## Branch
cinder/og-tags — issue #1

## What I did
- `index.html`: added Open Graph + Twitter Card meta tags in `<head>` (og:title, og:description, og:type=website, og:url, og:image, twitter:card=summary_large_image, twitter:title, twitter:description), all with absolute URLs. Also added a `<link rel="canonical">` (index previously had none; price-list.html already had one).
- `price-list.html`: same tag set with that page's own title, description, and canonical URL.
- `sw.js`: bumped `CACHE` from `dragginmasters-v10` to `dragginmasters-v11` (mandatory per AGENTS.md — the SW caches the app shell cache-first).
- Descriptions reuse the existing meta descriptions verbatim, per the issue. og:image is `https://dragginmasterstrains.com/icon-512.png` (1200x630 redesign explicitly out of scope for v1).

## What's left
- Push branch, open PR, paste Cloudflare preview URL (blocked: no GitHub push auth on this machine yet — needs Don to add Cinder as a collaborator).
- Verify in preview: view-source shows the tags; run the Facebook Sharing Debugger (or equivalent) against the preview URL and confirm title + description + image render with no errors.

## Decisions made
- Added the missing canonical link to index.html even though the issue only listed og:url — one line, standard SEO, consistent with price-list.html. Easy to revert if unwanted.
- Did not add `twitter:image` — with `twitter:card=summary_large_image`, Twitter/X falls back to `og:image`, which is set. Keeps the tag set minimal.
- Did not add `og:site_name` — not required by the issue; the titles already carry the brand.

## Blockers
- Push/PR needs GitHub auth: Don to add Cinder as collaborator on dragginmaster/dragginmasters-trains-site (or provide a token via secure entry). All local work is committed and ready to push.

## How to verify
- Serve locally: `python3 -m http.server 8080`, then `curl -s http://localhost:8080/ | grep -i "og:\|twitter:"` — all 8 tags present; same for `/price-list.html`.
- After push: check the preview deploy at `https://cinder-og-tags.dragginmasters-trains.pages.dev/` and run the Sharing Debugger on it.

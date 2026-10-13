# AGENTS.md — dragginmasters-trains-site

Instructions for AI collaborators working on this repo (notably Cinder).
The site is a fully static PWA (HTML/CSS/vanilla JS, no framework, no build step).

## Repo & deployment

- Canonical repo: https://github.com/dragginmaster/dragginmasters-trains-site.git
- Default/production branch: `main`
- Hosting: Cloudflare Pages, project `dragginmasters-trains`, custom domain
  https://dragginmasterstrains.com
- **Every push to `main` auto-deploys to production.** There is no staging
  branch — treat `main` as live at all times.
- Pushes to any other branch get an automatic Cloudflare **preview deployment**
  at `https://<branch-name>.dragginmasters-trains.pages.dev` — use these for
  review before merging.
- Comp data (comps.json + screenshots) lives in a SEPARATE repo,
  `dragginmaster/dragginmasters-comps-data`, and is loaded at runtime from
  `https://raw.githubusercontent.com/...` — never bundle comp data into this repo.

## Local development (exact commands)

```bash
git clone https://github.com/dragginmaster/dragginmasters-trains-site.git
cd dragginmasters-trains-site
# serve over http (the service worker will NOT run from file://)
python3 -m http.server 8080
# open http://localhost:8080
```

No install step, no build step, no dependencies. To regenerate the SEO
snapshot after comp-data changes:

```bash
python3 build-price-list.py   # rebuilds price-list.html from the data repo
```

## Branch naming

`cinder/<short-task-name>` — e.g. `cinder/og-tags`, `cinder/trend-road-split`.
One branch per issue; delete after merge.

## Commit messages

Short imperative summary, then context if needed:

```
trend modal: per-road-name average breakdown
```

Good: `seo: add Open Graph tags for link previews`
Good: `fix: trend modal legend overlapping chart on small screens`
Bad: `updates`, `fix stuff`, `WIP`

Reference the issue number in the body when there is one (`Closes #12`).

## Code conventions

- Vanilla JS, single-file app (`index.html` holds the markup, CSS, and JS).
  Keep it that way — no frameworks, no bundlers.
- Shared helpers (use them, don't reinvent):
  - `esc(s)` — HTML-escape any string from data before injecting into the DOM
  - `money(n)` — format a price as `$xx.xx`
  - `fmtDate(iso)` — format an ISO date for display
  - `roadName(r)` — railroad name only ("BNSF #9779 Executive" → "BNSF")
- **Service worker: bump the `CACHE` version string in `sw.js` on EVERY deploy
  that changes site files** (e.g. `dragginmasters-v10` → `dragginmasters-v11`).
  The SW caches the app shell cache-first; without a bump, installed apps and
  returning tabs keep the old page forever and never receive the fix.
- New static pages that should work offline: add to the `SHELL` array in sw.js.
- Comp-data fields come from the data repo; never invent field names — read
  one real entry of comps.json first if unsure.
- Don's product rules that affect display: control types (DC / DCC-ready /
  DCC / DCC+Sound) are always separate price lines; trend charts group by
  brand+model+scale+control (road name excluded from the key, shown per dot).
- Keep the mobile layout working — Don uses the installed PWA on his phone
  at train shows. Test at 390px width.
- Comp hunting has its own rulebook: `COMPS.md` in the
  `dragginmasters-comps-data` repo. Read it before any comp work — the
  validity rules there are Don's directives, no exceptions.

## Workflow

1. Pick an issue from the task board (GitHub Issues).
2. Branch `cinder/<short-task-name>` from `main`.
3. Make the change; verify locally via `python3 -m http.server`.
4. Update HANDOFF.md on your branch (what you did / what's left / decisions / blockers).
5. Push the branch, open a PR, paste the Cloudflare preview URL in the PR.
6. Merge to `main` only after the preview is reviewed. `main` auto-deploys.

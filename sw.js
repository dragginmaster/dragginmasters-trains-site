/* Dragginmasters Trains — offline service worker.
   Cache-first for the app shell; comp screenshots (now served from the
   data-repo CDN) are cached as viewed, so the price guide works at train
   shows with no signal.
   comps.json is NETWORK-FIRST: fresh data whenever there's a connection,
   last-cached copy when offline.

   IMPORTANT (2026-10-16): Cloudflare Pages 308-redirects every "*.html" URL
   to its clean canonical form ("/price-list.html" -> "/price-list"), and the
   Cache API REFUSES to store redirected responses. So cache.addAll() listing
   an .html URL rejects, the whole install fails, and the previous worker
   stays stuck in control forever (this caused net::ERR_FAILED on subpages).
   Therefore:
   - SHELL lists only canonical URLs that serve 200 directly (no redirects);
   - install caches each file individually, so one failure can't sink it. */
const CACHE = "dragginmasters-v64"; // bump on every deploy or installed apps never get the new shell
const SHELL = [
  "./",
  "price-list",
  "draggin-feedback",
  "draggin-submit",
  "manifest.json",
  "icon-192.png",
  "icon-512.png"
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) =>
      // One bad asset must never sink the whole install (that bricks updates).
      Promise.allSettled(SHELL.map((url) => c.add(url)))
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;

  // Last-resort fallbacks: respondWith must NEVER resolve undefined or reject —
  // either surfaces as net::ERR_FAILED. If the cache has nothing, serve an
  // honest offline page (or empty JSON for the data feed) instead.
  function offlinePage() {
    return caches.match("/", { ignoreSearch: true }).then((r) =>
      r || new Response(
        "<!DOCTYPE html><title>Offline</title><h1>You are offline</h1>" +
        "<p>Reconnect and reload — the price guide will pick up where it left off.</p>",
        { status: 503, headers: { "Content-Type": "text/html" } }
      )
    ).catch(() => new Response("Offline",
      { status: 503, headers: { "Content-Type": "text/html" } }));
  }

  function cachePut(request, res) {
    try {
      const copy = res.clone();
      // Cache under the FINAL url: the Cache API won't store a redirected
      // response under the pre-redirect request.
      const key = copy.url || request;
      caches.open(CACHE).then((c) => c.put(key, copy)).catch(() => {});
    } catch (_) {}
  }

  e.respondWith((async () => {
    try {
      // Price data: try the network first so new comps show up without an
      // app update; fall back to the cached copy when offline.
      if (e.request.url.indexOf("comps.json") !== -1) {
        try {
          const res = await fetch(e.request);
          if (res && res.ok) cachePut(e.request, res);
          if (res) return res;
        } catch (_) {}
        const hit = await caches.match(e.request, { ignoreSearch: true }).catch(() => null);
        return hit || new Response("[]",
          { status: 503, headers: { "Content-Type": "application/json" } });
      }

      const hit = await caches.match(e.request, { ignoreSearch: true }).catch(() => null);
      if (hit) return hit;
      try {
        const res = await fetch(e.request);
        if (res && res.ok) cachePut(e.request, res);
        if (res) return res;
      } catch (_) {}
      return await offlinePage();
    } catch (_) {
      // Absolute last resort: let the network try. Never reject.
      try { return await fetch(e.request); }
      catch (_) { return await offlinePage(); }
    }
  })());
});

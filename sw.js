/* Dragginmasters Trains — offline service worker.
   Cache-first for the app shell; comp screenshots (now served from the
   data-repo CDN) are cached as viewed, so the price guide works at train
   shows with no signal.
   comps.json is NETWORK-FIRST: fresh data whenever there's a connection,
   last-cached copy when offline. */
const CACHE = "dragginmasters-v12"; // bump on every deploy or installed apps never get the new shell
const SHELL = [
  "./",
  "index.html",
  "manifest.json",
  "icon-192.png",
  "icon-512.png",
  "draggin-submit.html",
  "draggin-feedback.html",
  "price-list.html"
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting())
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

  // Price data: try the network first so new comps show up without an
  // app update; fall back to the cached copy when offline.
  if (e.request.url.indexOf("comps.json") !== -1) {
    e.respondWith(
      fetch(e.request).then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(e.request, copy));
        }
        return res;
      }).catch(() => caches.match(e.request, { ignoreSearch: true }))
    );
    return;
  }

  e.respondWith(
    caches.match(e.request, { ignoreSearch: true }).then((hit) => {
      if (hit) return hit;
      return fetch(e.request).then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(e.request, copy));
        }
        return res;
      }).catch(() => caches.match("index.html"));
    })
  );
});

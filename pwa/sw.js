/* Kronikár service worker: app shell offline, fresh version when online */
const VERSION = "kronikar-v10";
const SHELL = ["./", "index.html", "manifest.webmanifest", "pdfmake.min.js", "icon-192.png", "icon-512.png", "icon-maskable-512.png", "apple-touch-icon.png", "favicon.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  const req = e.request; if (req.method !== "GET") return;
  const url = new URL(req.url);
  // the page itself: network first, so updates arrive; cache when offline
  if (req.mode === "navigate" || (url.origin === location.origin && url.pathname.endsWith("index.html"))) {
    e.respondWith(fetch(req).then(r => { const c = r.clone(); caches.open(VERSION).then(x => x.put("index.html", c)); return r; }).catch(() => caches.match("index.html")));
    return;
  }
  // fonts, thumbnails and app files: cache first, refresh in background
  if (url.origin === location.origin || /fonts\.(googleapis|gstatic)\.com|i\.ytimg\.com|cdn\.jsdelivr\.net/.test(url.host)) {
    e.respondWith(caches.match(req).then(hit => {
      const net = fetch(req).then(r => { if (r && (r.ok || r.type === "opaque")) { const c = r.clone(); caches.open(VERSION).then(x => x.put(req, c)); } return r; }).catch(() => hit);
      return hit || net;
    }));
  }
});

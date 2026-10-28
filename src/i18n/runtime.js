/* ================= language: Slovak source, English translation ================= */
const LANG = (() => {
  try { const v = localStorage.getItem("kronikar:lang"); if (v === "sk" || v === "en") return v; } catch { }
  return /^(sk|cs)\b/i.test(navigator.language || "") ? "sk" : "en";
})();
document.documentElement.lang = LANG;
const EN = {};
async function setLang(l) {
  if (l === LANG) return;
  try { localStorage.setItem("kronikar:lang", l); } catch { }
  try { if (typeof flush === "function") await flush(); } catch { }
  location.reload();
}
const I18N = {
  exact: null, pats: null, miss: new Set(),
  norm: s => s.replace(/\s+/g, " ").trim(),
  build() {
    this.exact = new Map(); this.pats = [];
    const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    for (const [k0, v] of Object.entries(EN)) {
      const k = this.norm(k0);
      if (!k.includes("{x}")) { this.exact.set(k, v); continue; }
      const parts = k.split("{x}"), lit = parts.reduce((a, b) => b.length > a.length ? b : a, "");
      if (lit.replace(/[^\p{L}]/gu, "").length < 2) continue;
      this.pats.push({ re: new RegExp("^" + parts.map(esc).join("(.+?)") + "$", "s"), v, lit: lit.trim() });
    }
    this.pats.sort((a, b) => b.lit.length - a.lit.length);
  },
  fill(v, args) {
    if (/\{\d\}/.test(v)) return v.replace(/\{(\d)\}/g, (m, i) => args[+i - 1] ?? "");
    let i = 0; return v.replace(/\{x\}/g, () => args[i++] ?? "");
  },
  /* translate one string; returns null when unknown */
  tr(s, depth = 0) {
    if (!this.exact) this.build();
    const k = this.norm(s); if (!k) return null;
    const hit = this.exact.get(k); if (hit !== undefined) return hit;
    for (const p of this.pats) { if (!k.includes(p.lit)) continue; const m = k.match(p.re); if (m) return this.fill(p.v, m.slice(1).map(a => this.tr(a, depth + 1) ?? a)); }
    if (depth > 2) return null;
    /* composed labels: "Deity · Greater deity", "lives in (formerly)", "Part: Stone" */
    const segs = k.split(/( · |: | → |→ | ←| \(|\)$)/);
    if (segs.length > 1) { let any = false; const out = segs.map((x, i) => { if (i % 2) return x; if (!/\p{L}/u.test(x)) return x; const r = this.tr(x, depth + 1); if (r !== null) { any = true; return r; } return x; }); if (any) return out.join(""); }
    /* several sentences glued together */
    const sen = k.split(/(?<=[.!?…])\s+(?=\p{Lu})/u);
    for (let c = 1; c < sen.length; c++) { const a = this.tr(sen.slice(0, c).join(" "), depth + 1); if (a === null) continue; const b = this.tr(sen.slice(c).join(" "), depth + 1); if (b !== null) return a + " " + b; }
    return null;
  },
};
/* tl(): translate a Slovak source string for the current language */
function tl(s, ...args) {
  let out = s;
  if (LANG === "en") { const r = I18N.tr(s); if (r !== null) out = r; }
  if (args.length) { let i = 0; out = out.replace(/\{(x|\d)\}/g, (m, k) => k === "x" ? (args[i++] ?? "") : (args[+k - 1] ?? "")); }
  return out;
}
/* translate every text run between tags of an html string (sample content, generated html) */
const trHtml = html => LANG === "en" ? String(html).replace(/>([^<]+)</g, (m, s) => ">" + tl(s) + "<").replace(/^([^<]+)/, (m, s) => tl(s)) : html;
/* live DOM translation: the UI is written in Slovak and translated as it is rendered */
if (LANG === "en") (() => {
  const SKIP = "#ed,[contenteditable],textarea,script,style,.no-tr,.pv-c,.pv-hf";
  const ATTRS = ["placeholder", "title", "aria-label"];
  const SKCHR = /[áäčďéíĺľňóôŕšťúýžÁÄČĎÉÍĹĽŇÓÔŔŠŤÚÝŽ]/;
  const text = n => {
    const v = n.nodeValue; if (!v || !/\p{L}/u.test(v)) return;
    const r = I18N.tr(v);
    if (r !== null) { const lead = v.match(/^\s*/)[0], trail = v.match(/\s*$/)[0]; const nv = lead + r + trail; if (nv !== v) n.nodeValue = nv; }
    else if (window.KRONIKAR_I18N_DEBUG && SKCHR.test(v)) I18N.miss.add(I18N.norm(v));
  };
  const attrs = el => {
    for (const a of ATTRS) { const v = el.getAttribute(a); if (v && /\p{L}/u.test(v)) { const r = I18N.tr(v); if (r !== null && r !== v) el.setAttribute(a, r); else if (r === null && window.KRONIKAR_I18N_DEBUG && SKCHR.test(v)) I18N.miss.add("@" + a + ": " + I18N.norm(v)); } }
    if (el.tagName === "OPTION" && el.parentElement?.tagName === "DATALIST") { const r = I18N.tr(el.value); if (r !== null && r !== el.value) el.value = r; }
  };
  const walkEl = root => {
    if (root.nodeType === 3) { if (!root.parentElement?.closest(SKIP)) text(root); return; }
    if (root.nodeType !== 1) return; if (root.closest(SKIP)) { if (root.tagName === "TEXTAREA" && !root.parentElement?.closest(SKIP)) attrs(root); return; }
    attrs(root);
    const w = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, { acceptNode: n => { if (n.nodeType === 1 && n.matches(SKIP)) { if (n.tagName === "TEXTAREA") attrs(n); return NodeFilter.FILTER_REJECT; } return NodeFilter.FILTER_ACCEPT; } });
    let n; while ((n = w.nextNode())) { if (n.nodeType === 3) text(n); else attrs(n); }
  };
  const mo = new MutationObserver(list => {
    for (const m of list) {
      if (m.type === "childList") m.addedNodes.forEach(walkEl);
      else if (m.type === "characterData") { if (!m.target.parentElement?.closest(SKIP)) text(m.target); }
      else if (m.type === "attributes" && (!m.target.closest(SKIP) || m.target.tagName === "TEXTAREA")) attrs(m.target);
    }
  });
  const start = () => { walkEl(document.body); mo.observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ATTRS }); };
  if (document.body) start(); else document.addEventListener("DOMContentLoaded", start);
  document.title = "Kronikár";
})();

const bookLang = () => (typeof S !== "undefined" && S.p && S.p.lang) || LANG;
/* translate for the language of the book being exported (may differ from the app language) */
const tlb = s => bookLang() === "en" ? (I18N.tr(s) ?? s) : s;

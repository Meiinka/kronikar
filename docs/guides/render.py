"""Render Kronikár guides to HTML; pdf.js prints them to docs/*.pdf with Chromium (Playwright).
Content lives in content_sk.py / content_en.py. Screenshots: node shots.js (needs dist/Kronikar.html)."""
import html, os, re, subprocess, sys, base64

HERE = os.path.dirname(os.path.abspath(__file__))
LIT = os.path.join(HERE, "..", "fonts")

def font_face(fam, path, weight, style="normal"):
    return f"@font-face{{font-family:'{fam}';src:url('file://{os.path.abspath(path)}');font-weight:{weight};font-style:{style}}}"

FONTS = "\n".join([
    font_face("Literata", f"{LIT}/Literata_400Regular.ttf", 400),
    font_face("Literata", f"{LIT}/Literata_400Regular_Italic.ttf", 400, "italic"),
    font_face("Literata", f"{LIT}/Literata_600SemiBold.ttf", 600),
    font_face("Literata", f"{LIT}/Literata_700Bold.ttf", 700),
])

CSS = FONTS + """
@page{size:A4;margin:20mm 19mm 22mm 19mm}
:root{--ac:#2E6B66;--acs:#E3EFEC;--ink:#1B2130;--ink2:#4F586B;--ink3:#8790A1;--line:#D9DEE5;--warn:#946812;--warns:#FBF3E2}
*{box-sizing:border-box}
html{font-family:Inter,'DejaVu Sans',sans-serif;font-size:10pt;line-height:1.55;color:var(--ink)}
body{margin:0}
h1,h2,h3{font-family:Literata,Georgia,serif;font-weight:600;color:var(--ink);line-height:1.25}
.cover{height:251mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always}
.cover .top{display:flex;align-items:center;gap:14px}
.cover .top img{width:54px;height:54px;border-radius:12px}
.cover .brand{font-family:Literata;font-size:22pt;font-weight:600;letter-spacing:.01em}
.cover h1{font-size:34pt;margin:0 0 10px;letter-spacing:-.01em}
.cover .sub{font-size:13pt;color:var(--ink2);max-width:135mm}
.cover .band{height:6px;background:var(--ac);width:60mm;margin:18px 0 22px;border-radius:3px}
.cover .meta{color:var(--ink3);font-size:9pt;border-top:1px solid var(--line);padding-top:10px;display:flex;justify-content:space-between}
.cover .hero{width:100%;border-radius:10px;border:1px solid var(--line);box-shadow:0 6px 24px rgba(20,30,45,.12)}
.toc{page-break-after:always}
.toc h2{font-size:18pt;margin:0 0 14px}
.toc ol{list-style:none;padding:0;margin:0;counter-reset:t}
.toc li{counter-increment:t;display:flex;gap:10px;padding:7px 0;border-bottom:1px solid var(--line);font-size:11pt}
.toc li::before{content:counter(t);font-family:Literata;color:var(--ac);font-weight:700;width:22px}
.toc li span{color:var(--ink3);font-size:9.5pt;margin-left:auto;text-align:right;max-width:95mm}
section{counter-increment:sec}
body{counter-reset:sec}
section>h2{font-size:17pt;margin:0 0 6px;padding-top:2px;break-after:avoid}
section>h2::before{content:counter(sec) ". ";color:var(--ac)}
section.newpage{break-before:page}
section+section{margin-top:22px}
section>h2{break-after:avoid}
h3+ul,h3+p,h3+ol{break-before:avoid}
.lead{color:var(--ink2);font-size:10.5pt;margin:0 0 12px}
h3{font-size:12pt;margin:16px 0 4px;break-after:avoid}
p{margin:0 0 8px}
ul,ol{margin:0 0 10px;padding-left:20px}
li{margin:2px 0}
ol.steps{list-style:none;padding:0;counter-reset:st}
ol.steps>li{counter-increment:st;position:relative;padding:3px 0 6px 34px;break-inside:avoid}
ol.steps>li::before{content:counter(st);position:absolute;left:0;top:2px;width:22px;height:22px;border-radius:50%;background:var(--ac);color:#fff;font-weight:600;font-size:9.5pt;display:grid;place-items:center}
.box{border-radius:8px;padding:9px 12px 9px 12px;margin:10px 0 12px;break-inside:avoid;font-size:9.6pt}
.box b.t{display:block;font-size:8.5pt;letter-spacing:.07em;text-transform:uppercase;margin-bottom:2px}
.tip{background:var(--acs);border-left:4px solid var(--ac)}
.tip b.t{color:var(--ac)}
.warn{background:var(--warns);border-left:4px solid #C9962E}
.warn b.t{color:var(--warn)}
figure{margin:10px 0 14px;break-inside:avoid;text-align:center}
figure img{max-width:100%;border:1px solid var(--line);border-radius:8px;box-shadow:0 3px 14px rgba(20,30,45,.10)}
figure.phone img{max-height:115mm;width:auto}
figure.pair{display:flex;gap:12px;justify-content:center}
figure.pair img{max-height:118mm;width:auto}
figcaption{font-size:8.6pt;color:var(--ink3);margin-top:5px;font-style:italic}
table{width:100%;border-collapse:collapse;margin:6px 0 12px;font-size:9.4pt;break-inside:auto}
th{text-align:left;font-size:8.3pt;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);font-weight:600;border-bottom:1.5px solid var(--ink3);padding:5px 8px}
td{border-bottom:1px solid var(--line);padding:6px 8px;vertical-align:top}
tr{break-inside:avoid}
td:first-child{font-weight:600;width:30%}
code,.k{font-family:'DejaVu Sans Mono',monospace;font-size:8.6pt;background:#EEF1F4;border:1px solid var(--line);border-radius:4px;padding:0 4px;word-break:break-all}
.k{font-family:Inter;font-weight:600;font-size:8.6pt}
a{color:var(--ac);text-decoration:none;border-bottom:1px solid #A9C9C3}
.ui{font-weight:600;color:#23504C}
"""

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[\[(.+?)\]\]", r'<span class="ui">\1</span>', s)          # UI label
    s = re.sub(r"\{\{(.+?)\}\}", r'<span class="k">\1</span>', s)           # key
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"\(\((https?://[^ )]+)\)\)", lambda m: f'<a href="{m.group(1)}">{m.group(1).replace("https://", "")}</a>', s)
    return s

def block(b, lang):
    kind = b[0]
    if kind == "p": return f"<p>{inline(b[1])}</p>"
    if kind == "lead": return f'<p class="lead">{inline(b[1])}</p>'
    if kind == "h3": return f"<h3>{inline(b[1])}</h3>"
    if kind == "ul": return "<ul>" + "".join(f"<li>{inline(x)}</li>" for x in b[1]) + "</ul>"
    if kind == "steps": return '<ol class="steps">' + "".join(f"<li>{inline(x)}</li>" for x in b[1]) + "</ol>"
    if kind in ("tip", "warn"): return f'<div class="box {kind}"><b class="t">{inline(b[1])}</b>{inline(b[2])}</div>'
    if kind == "table":
        head, rows = b[1], b[2]
        return "<table><thead><tr>" + "".join(f"<th>{inline(h)}</th>" for h in head) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>"
    if kind == "fig":
        cls = b[3] if len(b) > 3 else ""
        imgs = b[1] if isinstance(b[1], list) else [b[1]]
        tags = "".join(f'<img src="../img/{lang}_{i}.jpg">' for i in imgs)
        if cls == "pair": return f'<figure class="pair">{tags}</figure><figcaption style="text-align:center;margin-top:-8px;margin-bottom:12px">{inline(b[2])}</figcaption>'
        return f'<figure class="{cls}">{tags}<figcaption>{inline(b[2])}</figcaption></figure>'
    raise ValueError(kind)

def render(doc, lang, out_html):
    secs = doc["sections"]
    toc = "".join(f"<li>{inline(s['title'])}<span>{inline(s.get('toc', ''))}</span></li>" for s in secs)
    body = []
    for s in secs:
        cls = ' class="newpage"' if s.get("newpage") else ""
        body.append(f"<section{cls}><h2>{inline(s['title'])}</h2>" + "".join(block(b, lang) for b in s["blocks"]) + "</section>")
    hero = f'<img class="hero" src="../img/{lang}_{doc["hero"]}.jpg">' if doc.get("hero") else ""
    page = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{html.escape(doc['title'])}</title><style>{CSS}</style></head><body>
<div class="cover"><div><div class="top"><img src="../../pwa/icon-512.png"><span class="brand">Kronikár</span></div>
<div class="band"></div><h1>{inline(doc['title'])}</h1><div class="sub">{inline(doc['subtitle'])}</div></div>
{hero}
<div class="meta"><span>{inline(doc['meta_left'])}</span><span>{inline(doc['meta_right'])}</span></div></div>
<div class="toc"><h2>{inline(doc['toc_title'])}</h2><ol>{toc}</ol></div>
{''.join(body)}
</body></html>"""
    open(out_html, "w").write(page)

if __name__ == "__main__":
    sys.path.insert(0, HERE)
    import content_sk, content_en
    for lang, mod in (("sk", content_sk), ("en", content_en)):
        for key, doc in mod.DOCS.items():
            render(doc, lang, os.path.join(HERE, f"{key}_{lang}.html"))
    print("html ok")

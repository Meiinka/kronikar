#!/usr/bin/env python3
"""Build Kronikár from src/ into dist/ (standalone page, PWA, Windows files) and android/assets/.

    python3 tools/build.py

No dependencies besides Python 3. The app is plain HTML + JavaScript split into parts
(src/parts, joined in the order of src/parts/ORDER.txt); the English translation lives in src/i18n.
"""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
read = lambda p: open(p, encoding="utf-8").read()

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)

def i18n_part():
    d = P("src", "i18n")
    dicts = "".join(read(os.path.join(d, f)) + "\n" for f in sorted(os.listdir(d)) if f.startswith("en") and f.endswith(".js"))
    return "<script>\n" + read(os.path.join(d, "runtime.js")) + "\n" + dicts + "I18N.exact = null; /* rebuild with the full dictionary */\n</script>\n"

def body():
    out = []
    for name in read(P("src", "parts", "ORDER.txt")).split():
        out.append(i18n_part() if name == "p0_i18n.html" else read(P("src", "parts", name)))
    return "".join(out)

def page(shell, b):
    return read(P("src", "shell", shell + ".head.html")) + b + read(P("src", "shell", "tail.html"))

def main():
    b = body()
    pdfmake = P("vendor", "pdfmake.min.js")
    # standalone page (PC, macOS) + Windows installer input
    write(P("dist", "Kronikar.html"), page("standalone", b))
    for f in ("Kronikar.html",):
        shutil.copy(P("dist", f), P("win", f))
    shutil.copy(pdfmake, P("dist", "pdfmake.min.js")); shutil.copy(pdfmake, P("win", "pdfmake.min.js"))
    # installable web app
    write(P("dist", "pwa", "index.html"), page("pwa", b))
    for f in os.listdir(P("pwa")):
        shutil.copy(P("pwa", f), P("dist", "pwa", f))
    shutil.copy(pdfmake, P("dist", "pwa", "pdfmake.min.js"))
    # android
    write(P("android", "assets", "index.html"), page("android", b))
    shutil.copy(pdfmake, P("android", "assets", "pdfmake.min.js"))
    print("built: dist/Kronikar.html, dist/pwa/, win/Kronikar.html, android/assets/index.html")

if __name__ == "__main__":
    main()

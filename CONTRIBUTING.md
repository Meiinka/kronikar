# Contributing to Kronikár

Thanks for wanting to help! Bug reports and ideas go to [Issues](https://github.com/meiinka/kronikar/issues). For code changes, open a pull request – small, focused ones are easiest to review.

*Slovensky: podnety a chyby môžeš písať do Issues aj po slovensky.*

## Ground rules

- **Your writing stays yours.** Kronikár must never send data anywhere. No analytics, trackers or remote calls besides optional font/library loading that already exists. PRs adding network calls will be declined.
- **No build dependencies.** Plain HTML, CSS and JavaScript; the build is a single Python script with no dependencies.
- **Keep data compatible.** Projects are stored as JSON (`title.kronikar.json`). New fields need sensible defaults so old projects still open.
- **Both languages.** Every new visible text must work in Slovak and English (see below).

## How the code is organised

```
src/parts/        the app, split into parts joined in the order of ORDER.txt
  p1_style        all CSS
  p2_core         helpers, icons, categories, storage, state
  p3_projects     projects, backup/restore, sample project
  p4_shell        home screen, top bar, section switching
  p5_write        manuscript: binder, editor, corkboard, inspector
  p6_world        world entries and categories
  p7_graph        relationship map
  p8_export       export helpers, Markdown, Project page
  p9_fonts        embedded font subsets for PDF export (generated, large)
  p10_sync        auto-save to a folder (File System Access API), conflicts
  p11_refs        links (Instagram, YouTube…)
  p12_tpl         export templates, PDF (pdfmake) and DOCX builders, preview
  p13_pwa         installable app, loading pdfmake
  p14_android     Android bridge (emulates the folder API)
  p15_selpop      “select a word → add to world” popup
  p16_forms       name forms / Slovak declension suggestions
  p17_quotes      smart quotation marks
  p18_notes       sticky notes
src/i18n/         English translation (runtime.js + dictionaries en*.js)
src/shell/        <head> for each build target
pwa/              manifest, service worker, icons
android/          Android wrapper (WebView + Storage Access Framework)
win/              Windows installer (NSIS)
docs/             PDF guides and their sources
tools/build.py    builds everything into dist/
```

## Building and testing

```bash
python3 tools/build.py
```

Then open `dist/Kronikar.html` in Chrome. Use **Sample project** on the home screen to get test data. Please check both desktop and a narrow (phone) window, and both languages (switch SK / EN at the top right of the home screen).

## Translations

The source language of the UI is Slovak. English is applied at runtime: `src/i18n/runtime.js` translates text in the page using the dictionaries `src/i18n/en*.js`.

- When you add a visible Slovak text, add its English version to `en2.js` (or a new `en3.js`): `"Slovenský text": "English text"`.
- Dynamic parts are written as `{x}`: `"Zmazať „{x}“?": "Delete “{x}”?"`.
- Text that does not go through the page (PDF/Word export, default names of new items) is wrapped in `tl("…")` (app language) or `tlb("…")` (book language).
- To find missing translations, set `window.KRONIKAR_I18N_DEBUG = true` before loading the page with the English UI; untranslated Slovak texts collect in `I18N.miss`.

## Releasing (maintainer)

1. Bump the version in `android/AndroidManifest.xml` (`versionCode` + `versionName`), `win/installer.nsi` (`VERSION`, `VIProductVersion`) and the cache name in `pwa/sw.js`.
2. `python3 tools/build.py`, `makensis win/installer.nsi`, `android/build.sh` (with your keystore).
3. Create a GitHub release and attach `dist/Kronikar.html`, `Kronikar-Setup.zip`, `Kronikar.apk`, `kronikar-app.zip` (zip of `dist/pwa`) and the PDF guides.

The Android signing key is **never** committed. Keep it and its password private – anyone who has it can publish “updates” of the app.

# Contributing to Kronikár

Thanks for wanting to help! Bug reports and ideas go to [Issues](https://github.com/meiinka/kronikar/issues). For code changes, open a pull request – small, focused ones are easiest to review.

*Slovensky: podnety a chyby môžeš písať do Issues aj po slovensky.*

## Ground rules

- **Your writing stays yours.** Kronikár must never send data anywhere. No analytics, trackers or remote calls besides optional font/library loading that already exists. PRs adding network calls will be declined.
- **No build dependencies.** Plain HTML, CSS and JavaScript; the build is a single Python script with no dependencies.
- **Keep data compatible.** In the folder, a book is `projekt.json`, `rukopis/<scene>.html`, `svet.json`, `poznamky.json`, `statistiky.json` pictures in `obrazky/` and scene versions in `verzie/` (see the top of `p10_sync.html`). New fields need sensible defaults so old projects still open; purely device-local state (expanded chapters, graph layout) must not end up in these files.
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
  p10_sync        folder sync: one subfolder per book, parts compared by hash, per-part conflicts, readable copy
  p11_refs        links (Instagram, YouTube…)
  p12_tpl         export templates, PDF (pdfmake) and DOCX builders, preview
  p13_pwa         installable app, loading pdfmake
  p14_android     Android bridge (emulates the folder API)
  p15_selpop      “select a word → add to world” popup
  p16_forms       name forms / Slovak declension suggestions
  p17_quotes      smart quotation marks
  p18_notes       sticky notes
  p19_media       photos of world entries, maps with pins, pictures in the folder
  p20_revise      scene versions, repetitions, names check, find & replace, sprints, reading aloud
  p21_story       calendar and timeline, plot templates, character arcs
  p22_extras      ages in scenes, family tree, journeys on maps, book appendices, plot threads, who knows what
  p23_more        search everywhere, appearance from the text, name generator, dictation, tempo, relationships in time, scene card, calendar extras
  p24_flows       magical currents: occurrence and density in sources, colour layer on maps
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

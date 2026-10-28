<p align="center"><img src="pwa/icon-192.png" width="96" alt="Kronikár logo"></p>

<h1 align="center">Kronikár</h1>

<p align="center"><b>A writing studio for fantasy novels – manuscript, world, relationships and book export in one app.</b><br>
Runs on your own devices. No account, no server, no internet required.</p>

<p align="center"><a href="README.sk.md">Slovensky</a> · <a href="https://github.com/meiinka/kronikar/releases">Download</a> · <a href="docs/kronikar-installation.pdf">Installation guide</a> · <a href="docs/kronikar-user-guide.pdf">User guide</a></p>

![Kronikár – manuscript view](docs/img/en_write.jpg)

## Features

- **Manuscript** split into parts, chapters and scenes, with a corkboard, scene status, POV, word goals and standard-page counts.
- **World** – characters, places, races, religions, deities, magic, factions, artefacts, events, plus your own categories with custom fields.
- **Select a word while writing and add it to the world** – Kronikár suggests other forms of the name and later finds every mention in the manuscript.
- **Relationship map** as a network or a tree, including past relationships (“until chapter 7”).
- **Sticky notes** with categories (To do, Idea, Check…), optionally attached to chapters and scenes.
- **Export to PDF and Word** – printed-book templates (Classic, Chronicle, Elegant, Modern) and manuscript formats for publishers (Standard, SK/CZ, US Shunn, UK, AU), detailed typesetting, saved templates, contents, book description (logline, blurb, synopsis).
- **Smart quotation marks** – American, British, Slovak/Czech, German, French.
- **Slovak and English** interface; the book language is set separately.
- **Auto-save to a folder** of your choice, daily backups, and sync between devices with Syncthing or any folder-sync tool.

![World and relationships](docs/img/en_graph.jpg)

## Download

Get the latest version from **[Releases](https://github.com/meiinka/kronikar/releases)**:

| File | For |
|---|---|
| `Kronikar-Setup.zip` | Windows installer (opens Kronikár in its own Chrome / Edge window) |
| `Kronikar.html` | Windows, macOS, Linux – a single file, open it in Chrome, Edge or Brave |
| `Kronikar.apk` | Android 7+ |
| `kronikar-app.zip` | installable web app (PWA) for your own hosting |

Step-by-step instructions, including syncing between computer and phone: [Installation guide (PDF)](docs/kronikar-installation.pdf) · [User guide (PDF)](docs/kronikar-user-guide.pdf)

> **Browser note:** Safari and Firefox cannot save to a folder, so use Chrome, Edge or Brave on desktop.

## Syncing between devices

Kronikár never sends your writing anywhere. It saves each project as `title.kronikar.json` in a folder you choose and checks that folder for changes every 15 seconds. To write on several devices, keep that folder in sync with a tool such as **[Syncthing](https://syncthing.net)** (Android: *Syncthing-Fork* from Google Play or F-Droid), or OneDrive / Dropbox / Google Drive on desktop.

## Building from source

Kronikár is plain HTML and JavaScript with no frameworks and no npm dependencies.

```bash
python3 tools/build.py        # -> dist/Kronikar.html, dist/pwa/, win/, android/assets/
```

- **Windows installer:** `makensis win/installer.nsi` (NSIS 3)
- **Android APK:** `android/build.sh` – see the comments in the script; you need your own signing key
- **Guides:** `docs/guides/` – `node shots.js`, `python3 render.py`, `node pdf.js` (Playwright)

See [CONTRIBUTING.md](CONTRIBUTING.md) for how the code is organised.

## Contributing

Ideas and bug reports are welcome in [Issues](https://github.com/meiinka/kronikar/issues). Pull requests too – please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

[MIT](LICENSE) © 2026 meiinka. Bundled fonts are under the SIL Open Font License 1.1 and pdfmake under MIT – see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

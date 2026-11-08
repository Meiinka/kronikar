# Changelog

## 1.35
- **Light or dark theme by choice:** a sun / moon button in the top bar switches Follow the system → Light → Dark; the same choice is under Project → Theme. It is remembered per device, so a phone can be dark and a computer light.

## 1.34.1
- Fixed: a map symbol linked to a World entry (e.g. a castle linked to a city) made the World list fail to draw.
- Scene ideas with an unknown kind or status no longer break the ideas list.
- User guides rewritten for all features up to 1.34 (Slovak and English, new screenshots).

## 1.34
- **Fields in Properties per category:** “Fields” in the Properties card opens the list of a category's fields – change their order, hide the ones you don't use (their data stays) and rename them. A new field added there appears in every entry of the category at once.
- **Entry status:** sketch / in progress / done for every World entry, shown as a coloured dot in the list; the list can be filtered by status.
- **Character gallery:** all characters as cards with photo, role, nickname and age in the story, filterable by role and printable (or saved as HTML on Android).
- **Compare two entries** side by side: fields, custom fields, name forms, age, time, currents, links, shared links and mentions; “Differences only” hides matching rows.
- **History of a place:** a card in each place's entry that lists in time order its founding, events, scenes set there, and who lived there or was linked with it and when; items without an exact time follow below.
- **Find a place for a portal:** choose a current, minimum density, a centre (e.g. the silver tree), a map and a maximum distance – the list shows the places with the current, their density, distance in km by the map scale, structure and other currents, suitable ones first.
- **Currents in map export:** JPG and SVG can include the current colour layer (all currents or the one picked), with the currents in the legend.
- **Faster with big books:** cached text of scenes and name patterns – opening a character in a book with 100 chapters and 200 characters went from about 2.2 s to 0.25 s, the timeline from 3.6 s to 0.2 s.

## 1.33
- **Arrange the sections of World entries:** “Arrange” in an entry opens the list of its sections (Properties, Plot line, Arc, Sticky notes, Photos, Timeline, Links, Notes…). Drag them or use the arrows to change the order and untick the ones you don't need; “Save” applies it to every entry of that category, “Default order” brings the original back.

## 1.32
- **For consulting:** the inspector of a chapter, scene or part can download just that piece as PDF, Word or plain text, or copy its text, optionally with paragraph numbers (3.12) for comments. Typesetting follows the export settings.
- **Chapter by chapter** in Export: every chapter as its own PDF, Word or text file, packed in one ZIP.

## 1.31
- **Folder not allowed – visible warning:** when a sync folder is set up but its permission was not granted in this session, a bar under the top bar says so; after the first edit it turns red (“edits are saved only in this browser”) with an “Allow folder” button. Allowing writes all waiting edits to the folder, also for other books.
- **Closing with unsaved edits asks first:** closing the app or the browser tab while edits are not in the folder yet (or not saved at all) brings up the browser's “Leave?” question.
- Books with edits that are not in the folder are remembered across restarts.

## 1.30
- **Character plot line:** a card in each character's entry for what the story will bring her and what she must resolve – each item with a rough place in the story (beginning, first quarter, middle, three quarters, end – or anything in between with a slider), an optional chapter and a “done” tick. A track above shows all items along the story, done ones in green, with a done / total count.

## 1.29
- **Magical currents:** a new World category. Each current has a colour and fields for its essence, structure, how it bends and behaves, who works with it (benders, weavers…), how it shows, cost and risks.
- **Occurrence and density:** in a current's entry, a table of where it occurs – places, animals, races, objects or plain words (water, desert) – with density 0–5 (also the saturation of its colour), the structure it has there and a note. Every source shows its own mix of currents as a coloured bar and can add or adjust them too.
- **Currents on maps:** “Currents” on a map tints areas and pins linked to places by the currents in them – the denser, the deeper – and can show a single current only.
- Relationship suggestions for currents: strengthens, weakens, cancels, bends towards, repels, mixes with, arises from; for characters: bends, weaves and structures, senses, draws from.

## 1.28
- **Places on maps:** every place in the World list shows on how many maps it is (pin, area, route or symbol), places on no map are marked, and “Places” can be filtered to On a map / No map.
- A place's “On a map” card says when it is on no map yet and offers “Place on the map”: choose a map, tap where it lies, and the pin is linked to the place. Places already on a map can be added to another one the same way.

## 1.27
- **Search everywhere** (magnifier in the top bar or Ctrl+K): scenes, chapters, World entries, sticky notes, scene ideas, plot threads and secrets in one list with highlighted snippets; arrows and Enter to open.
- **Appearance from the text:** a character's entry lists descriptions of eyes, hair, skin, face, beard, voice, hands, scars and build found in the manuscript (a body part with a describing word in a sentence that names the character), groups them and flags conflicting colours. “+” adds a line to Appearance, “×” hides a false hit.
- **Relationships in time:** in the Relationships graph, “In time” with a year slider fades out entries and relationships that do not exist in that year.
- **Scene card:** goal, conflict / obstacle, outcome and what changed for each scene in the inspector; the chapter corkboard can show the cards instead of synopses.
- **Chapter tempo** (Tools → Tempo): length of each chapter, share of dialogue, number and average length of scenes, with hints for unusually long or dialogue-free chapters.
- **Name generator** (World → Names): new names that sound like the names already in your world, or like a list you type.
- **Dictation** of scene ideas and sticky notes: the system speech recogniser on Android, Web Speech in desktop Chrome / Edge.
- **Calendar of the world:** holidays, moons with their cycle and seasons; a scene with a date shows the season, holiday and full or new moon.

## 1.26.1
- World: the list of entries no longer goes empty when one entry arrives incomplete (for example without a name or with an unusual field value after sync). Such entries are repaired when the book opens; a single broken entry can never hide the others.
- An unexpected error now shows a short message instead of leaving a page half drawn.

## 1.26
- **Deities → Mythology.** The category now holds gods, deified heroes and founders, saints and prophets, spirits, demons, mythical creatures, guardians and cosmic forces such as a world tree. The kind is grouped (Gods · Between gods and mortals · Beings · Sacred and cosmic) and the World list can be filtered by group.
- Fields that fit every kind: domain / what it embodies, appearance, origin and legends, cult and shrines, symbols, power and limits, relation to mortals. Existing entries are converted automatically – no text is lost.
- New relationship suggestions: founded, has a shrine in, is the patron of, is worshipped in, is a descendant of, prays to.

## 1.25
- **Two-way relationships:** a relationship can hold in both directions (↔). Tick “two-way” when linking (World, Relationships, map panel), optionally with a different wording the other way (“je priateľkou” / “je priateľom”). Each entry shows the wording from its own side; the graph draws arrows at both ends and both wordings.

## 1.24
- **Scene ideas** (Notes → Scene ideas): longer drafts kept outside the book – title, free text of any length, kind (for later / flashback), status, the chapter it roughly belongs to, characters and places, story time. Filter and search.
- **Put into the manuscript as a scene:** one button creates a new scene in a chosen chapter with the idea's text, characters, place and time; the idea stays marked as used with a link to the scene.
- Ideas linked to a character show in its entry; ideas for a chapter show in the chapter's inspector.

## 1.23
- **Sticky notes for characters** (and any World entry): a “Sticky notes” card in the entry – add a to-do with a category, tick it off when done. Entries with open notes show a count in the World list.
- On the Notes board a note can be assigned to characters and other World entries as well as chapters and scenes, and the board can be filtered by a character. Clicking the character on a note opens it in the World.

## 1.22.1
- Scene and chapter inspector: a link to the overview of all plot threads is always there; clicking a thread opens the overview.

## 1.22
- Characters: new field **Nickname** (several separated by commas). It is shown in the World list next to the name, in the list of characters in the book appendix, and Kronikár finds the character in the text by the nickname too.
- Chapters and parts: **Point-of-view characters** in the inspector – the characters a chapter focuses on. Shown on the chapter card, in the inspector of its scenes (“Chapter focus”), as a badge in the character arc, and counted as present in those scenes (timeline, ages, who knows what, journeys).

## 1.21
- **Ages in scenes:** the scene inspector shows how old each character in the scene is (from the scene's time and the character's birth) and warns when someone is not born yet or no longer alive. A character's entry shows their age span across the story.
- **Family tree** (Relationships → Family tree): built automatically from relationships such as father, mother, son, daughter, sibling, husband / wife, for characters and for deities. Any relationship (also your own) can be assigned a family meaning. Save as an image.
- **Journeys on maps:** on a map, “Journeys” draws the route of chosen characters through the places of their scenes, in book order or story time. With a map scale it shows distances and warns when a journey would be too fast for the time between scenes.
- **Glossary:** a new World category for invented words, names and titles (kind, pronunciation, meaning, language). Names in it are known to the names check.
- **Book appendices** in Export: maps and a list of characters at the beginning, family tree and glossary at the end – in PDF, Word and EPUB, for the full book and the beta reader version.
- **Plot threads** (Tools): setups and their payoffs linked to chapters or scenes, open threads at a glance, a warning when the payoff comes before the setup; also in the scene inspector.
- **Who knows what** (Tools): secrets with the chapter from which each character knows them and when the reader learns them; the scene inspector shows who of those present already knows.
- English interface: missing translations from recent versions added.

## 1.20
- Characters: **Role in the story** is now the main field, shown above the name in the World list (“Character · Main character”) and as a badge in the entry, like the kind of a deity. It offers main character, protagonist, supporting character, antagonist, mentor, ally, love interest, narrator and minor character, or your own words. Unlike deities it is not required.

## 1.19
- **Own relationships:** a relationship you type that is not among the suggestions is saved to the book's list and offered next time (everywhere you link entries: World, Relationships, map panel). Relationships already used in older books are added automatically.
- **Typo guard:** when a new relationship looks like an existing one (“bojoval po bokú” vs “bojoval po boku”, “zila tam” vs “žila tam”), Kronikár asks whether to use the existing one or save the new one.
- **Edit the list of relationships:** rename (all links follow), merge into another relationship, delete unused ones, and a “Possible duplicates” section with one-click merge or “Not a duplicate”.

## 1.18
- **↻ Refresh** in the top bar, everywhere (book list and every section of a book, PC and mobile). It saves what is pending, loads the latest changes from the sync folder (other devices) and redraws the current page.

## 1.17.1
- Timeline: the character selection is recomputed every time, so characters that got a time or an event later show up automatically. Your own ticks and unticks are kept. Switching books resets the timeline.
- **Refresh** button: reloads the timeline and zooms out to show everything.
- “Without time” now also lists own events with no time yet; type a year and they move onto the timeline.
- The timeline redraws after sync from another device.

## 1.17
- Timeline: a second view, **Axis**. It shows one line through the middle, with a mark for every month that has something on it (years, decades… when zoomed out; never days). Click a mark to see the chapters, events and characters of that month, with arrows to the previous and next mark. A “Still going on” list shows longer events and relationships.
- **Split into lines:** separate lines for Chapters, Events and Characters.
- The original lane view stays; switch with Lanes / Axis. The choice is remembered.

## 1.16.1
- Timeline: a character's own events and relationships with a time now show even when no scene or birth has a time yet (the timeline was empty). Event markers are larger.

## 1.16
- World entries: **own events** in “On the timeline” – name, time in words and/or on the timeline, linked to one or more chapters or scenes. Flashback chapters are fine: the order is not checked.
- Linked events appear in the inspector of the scene or chapter (“Events from the World”). On the Timeline they show among world events, or on the character's own lane.
- Text you write (event names, “100 years ago”) is no longer machine-translated in the English interface.

## 1.15
- Deities: new kind **Divine entity** (Božská entita).
- Relationships get a **time**: write it in words (“100 years ago”) and/or pick an exact span on the book's timeline. Shown on relation chips and rows; relations with a time appear as bars on the character lanes of the Timeline.
- Map panel of a place: per chapter/scene you can mark **which characters were there** (“Were there:” chips, add/remove), and assign a scene together with a character in one step.
- New relationship suggestions for character → place: lived there, was born in, died in, hid in, was imprisoned in.

## 1.14
- Map symbols grouped (Land, Water, Settlements and buildings, Animals, Other) with new **water** symbols (waves, lake, waterfall, spring, marsh, sea creature) and **animals** (deer, wolf, bear, horse, birds, fish, snake). “Here be dragons” removed from the picker (existing ones stay on the map).
- **Eraser in the symbol picker** and a real wiping eraser: drag over symbols and labels to delete many at once, in three sizes, with a visible eraser circle; “Back to symbols” returns to drawing.

## 1.13.1
- Maps: the map image (or the underlay of a drawn map) can be removed; everything drawn stays on a plain background.

## 1.13
- Maps: **Undo / Redo** (buttons and Ctrl+Z / Ctrl+Y) for everything drawn on a map; Delete removes the selected item.
- **Chains of symbols:** in the Symbol tool, drag across the map to draw a whole mountain range or forest in one stroke (slightly varied sizes for a hand-drawn look).
- **Eraser:** tap anything to delete it, or drag to wipe symbols, labels and pins.
- **Extend map:** add space on any side (presets or percentages); everything drawn stays in place and keeps its size. Works for image maps too – the image stays where it was and the new space gets a background.

## 1.12
- **Draw your own map (vector):** start a map without an image – parchment, white paper, sea or dark background in landscape, wide, square, portrait or A4 format.
- **Freehand drawing:** drag to draw coastlines, forests, mountains, rivers and routes; shapes are simplified and smoothed automatically (smoothing can be switched off). New terrain types *Land* and *Sea and lakes*, new line style *River*.
- **Map symbols:** mountain, range, hill, forests, city, castle, village, tower, temple, ruins, cave, bridge, ship, compass rose and “here be dragons” – with size, caption and link to a World entry.
- **Map labels:** free text for seas, regions or mountains in three styles, with size, rotation and colour.
- **SVG export** next to JPG – a true vector file, sharp at any size and editable in Inkscape or Illustrator.
- A drawn map can get an underlay image (e.g. a scanned sketch) to trace over.
- Two-finger pinch now also moves the map.

## 1.11.3
- Scenes placed directly in a part (not in a chapter) now belong to the part: they are no longer counted as chapters, so the chapters after them are numbered from one. Export (PDF, Word, EPUB, Markdown, contents) prints them after the part title without a chapter heading.

## 1.11.2
- Character arc: every row shows whether it is a part, chapter or scene, the part a chapter belongs to, and explains when scenes lying directly in a part are numbered as chapters.

## 1.11.1
- Character arc: rows follow the folders that hold the scenes, so scenes placed directly in a part are no longer listed one by one.

## 1.11
**Writing and revision**
- **Scene versions:** save a version before a rewrite, compare it with the current text (changed words highlighted) and restore it. Versions are also saved automatically before replacing text or restoring. They sync as readable files in `verzie/`.
- **Repetition check:** highlights words repeated close together (within 20–150 words), including other forms of the same word (bol / bola / boli).
- **Names not in the world:** finds capitalised words that aren't in the World – typos in names (Ilas → Ilsa) and forgotten characters or places – with one-click fix, add to the world, add as a name form or ignore.
- **Find and replace in the whole manuscript**, including renaming a World entry together with all its name forms.
- **Writing sprints** (10–45 min, optional word goal) with a timer, results and statistics on the Project page.
- **Reading aloud** from the cursor with the current sentence highlighted (on Android through the phone's text-to-speech).

**World and story**
- **Timeline** (new section *Time*): scenes, events and characters' lives on one axis in your world's own calendar (era, month names, days). Warns when a character is in two places at once or appears before birth / after death.
- **Plot templates:** three-act structure, Save the Cat, Hero's Journey, seven-point structure – assign scenes to beats, see ideal positions and where you are; beats show on the corkboard and in the inspector.
- **Character arc:** want, need, lie and truth plus a row per chapter (what they want, what changed, how they're doing) with a small chart.

## 1.10
- **Terrain and territories on maps:** trace areas point by point – kingdoms and borders, forests, mountains, water, desert, marsh, fields, cities, ruins, ice – each with its own colour and pattern. An area can be linked to a world entry (or turned into a new place) and shows its characters and chapters.
- **Routes:** draw a character's journey, an army's march or a trade road as a solid, dashed or dotted line with an arrow; link it to a character.
- **Layers:** e.g. political borders and terrain, or borders before and after a war – show or hide them, choose which one you draw into.
- **Editing shapes:** drag points, add points between them, remove a point, drag the label to a better spot.
- **Save the map as JPG for printing** – with title, legend and labels, in original or larger size (shows how big it prints sharply at 300 dpi).
- The map view now follows the image's shape, so there are no empty bands on a phone.

## 1.9
- **Maps:** new world category *Maps*. Upload a map image, zoom and pan it (mouse wheel, pinch), and pin places on it – an existing entry or a new place created right from the map. A pin shows the place's characters and the chapters and scenes it appears in; you can link a character or assign a chapter directly from the pin.
- **Photos for every world entry:** add pictures (also by drag and drop on a computer), set the main one (shown next to the name and in the list), add captions, browse them full screen.
- Places and other entries show **“On the map”** with a preview; clicking it opens the map at that pin.
- World entries can be **assigned to a chapter or scene from the World section** (a place becomes the scene's setting).
- Pictures are stored in the book folder in `obrazky/` and synced like the rest; *Backup* in Export now includes them.
- Android: picture picker opens the gallery and allows choosing several photos at once.

## 1.8
- **EPUB export** for e-readers (Kindle via Send to Kindle, Kobo, PocketBook, Apple Books, phone readers) – whole book or text only, with a contents menu, parts and chapters.
- **Beta reader edition** in PDF, Word and EPUB: paragraphs numbered per chapter (3.12) so readers can point to an exact spot, a title page with instructions and a “work in progress – please do not share” mark on every page.

## 1.7.1
- Phone layout: language picker and the folder card on the home screen no longer get squeezed.

## 1.7
- **New folder layout:** every book has its own subfolder – `projekt.json`, one HTML file per scene in `rukopis/`, `svet.json`, `poznamky.json`, plus a readable copy of the book, world and notes in `citatelne/`. Old `*.kronikar.json` files are converted automatically on first start (the original goes to `zalohy/`).
- **Conflicts per part:** editing different scenes, notes or the world on two devices no longer conflicts. If the same part changes on both, Kronikár shows which one, lets you view the other version and choose.
- **Fewer saves:** saving waits 2 s after the last change (at most 20 s while typing), writes only parts that really changed, and browsing (selecting chapters, expanding the tree, switching sections) writes nothing.
- Android: support for nested folders.

## 1.6
- English interface (switch SK / EN on the home screen or in Project); separate book language for export.
- Bilingual Windows installer.

## 1.5
- Sticky notes with categories, optionally attached to chapters and scenes.
- New world category: Races and peoples.

## 1.4
- Smart quotation marks (Slovak, American, British, German, French), converting the whole manuscript, quotes in export.

## Earlier
- Manuscript, corkboard, world with custom categories, relationship map, PDF/Word export with templates, manuscript formats, auto-save to a folder with Syncthing support, Android app, Windows installer, select-a-word-to-add-to-world with name forms.

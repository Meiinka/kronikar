SYNCTHING = "https://syncthing.net"
FORK = "https://f-droid.org/packages/com.github.catfriend1.syncthingfork/"

INSTALL = {
 "title": "Inštalácia a synchronizácia",
 "subtitle": "Ako Kronikár nainštalovať na Windows, macOS a Android, kam ukladá projekty a ako ich mať rovnaké na všetkých zariadeniach.",
 "meta_left": "Kronikár 1.6", "meta_right": "Návod 1 / 2",
 "toc_title": "Obsah", "hero": "home",
 "sections": [
  {"title": "Čo budeš potrebovať", "toc": "zariadenia, súbory, prehliadač", "blocks": [
   ("lead", "Kronikár je písacie štúdio, ktoré beží celé u teba. Nepotrebuje účet, server ani internet. Projekty ukladá do priečinka, ktorý si vyberieš."),
   ("table", ["Zariadenie", "Čo stiahnuť", "Na čom beží"], [
     ["Windows 10 / 11", "`Kronikar-Setup.zip` (inštalátor) alebo `Kronikar.html`", "Google Chrome, Microsoft Edge alebo Brave"],
     ["macOS", "`Kronikar.html`", "Google Chrome, Microsoft Edge alebo Brave"],
     ["Android 7 a novší", "`Kronikar.apk`", "vlastná aplikácia, prehliadač netreba"],
   ]),
   ("warn", "Safari a Firefox", "Kronikár sa v nich otvorí, ale nevedia ukladať do priečinka. Projekty by ostali len v prehliadači a nedali by sa synchronizovať. Použi Chrome, Edge alebo Brave."),
   ("tip", "Odkiaľ sťahovať", "Súbory sťahuj len z oficiálnej stránky projektu: ((https://github.com/meiinka/kronikar/releases)). Tak máš istotu, že sú pravé."),
  ]},
  {"title": "Windows", "toc": "inštalátor alebo samostatný súbor", "blocks": [
   ("h3", "Inštalátor (odporúčané)"),
   ("steps", [
     "Rozbaľ `Kronikar-Setup.zip` (pravé tlačidlo → [[Extrahovať všetko]]).",
     "Spusti `Kronikar-Setup.exe`. Ak Windows zobrazí modré okno **Systém Windows ochránil váš počítač**, klikni na [[Ďalšie informácie]] a potom [[Spustiť aj tak]]. Upozornenie sa zobrazí preto, že inštalátor nie je podpísaný plateným certifikátom, nie preto, že by bol škodlivý.",
     "Prejdi sprievodcom. Práva správcu netreba, Kronikár sa inštaluje len pre teba.",
     "Na ploche a v ponuke Štart pribudne **Kronikár**. Otvorí sa v samostatnom okne prehliadača Chrome, a ak Chrome nemáš, v Edge.",
   ]),
   ("h3", "Bez inštalácie – len súbor Kronikar.html"),
   ("p", "Kronikár je jeden súbor. Ulož `Kronikar.html` napríklad do `Dokumenty\\Kronikar` a otvor ho dvojklikom. Ak chceš, aby sa otváral vo vlastnom okne ako aplikácia, vytvor si odkaz na ploche:"),
   ("steps", [
     "Pravé tlačidlo na ploche → [[Nový]] → [[Odkaz]].",
     "Ako umiestnenie vlož (cestu uprav podľa seba): `\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --app=\"file:///C:/Users/MENO/Documents/Kronikar/Kronikar.html\"`",
     "Medzery v ceste k súboru nahraď znakmi `%20` (napríklad `OneDrive%20-%20Firma`).",
     "Pomenuj odkaz **Kronikár**. Ikonu zmeníš cez pravé tlačidlo → [[Vlastnosti]] → [[Zmeniť ikonu]].",
   ]),
   ("tip", "Brave", "Pre Brave použi cestu `C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe`. Ukladanie do priečinka v Brave zapneš na adrese `brave://flags/#file-system-access-api`: nastav [[Enabled]] a reštartuj prehliadač."),
   ("h3", "Odinštalovanie"),
   ("p", "[[Nastavenia]] → [[Aplikácie]] → **Kronikár** → [[Odinštalovať]]. Tvoje projekty v priečinku ostanú nedotknuté."),
  ]},
  {"title": "macOS", "toc": "Kronikar.html v Chrome", "blocks": [
   ("steps", [
     "Ulož `Kronikar.html` napríklad do `Dokumenty/Kronikar`.",
     "Pravé tlačidlo na súbore → [[Otvoriť v aplikácii]] → **Google Chrome** (alebo Edge, Brave).",
     "Aby sa súbor otváral v Chrome vždy: pravé tlačidlo → [[Informácie]] → [[Otvoriť v aplikácii]] → Chrome → [[Zmeniť všetky]].",
     "Pre rýchly prístup si súbor pretiahni do Docku (do pravej časti, k priečinkom) alebo si ho pridaj medzi záložky.",
   ]),
   ("tip", "Vlastné okno", "Ak chceš Kronikár otvárať v samostatnom okne bez panelov prehliadača, v Termináli spusti: `open -na \"Google Chrome\" --args --app=\"file:///Users/MENO/Documents/Kronikar/Kronikar.html\"`"),
  ]},
  {"title": "Android", "toc": "inštalácia APK a aktualizácie", "blocks": [
   ("steps", [
     "Stiahni `Kronikar.apk` do telefónu (alebo ho tam skopíruj).",
     "Otvor ho v aplikácii [[Súbory]] alebo zo stiahnutých súborov.",
     "Android sa spýta, či smie táto aplikácia inštalovať neznáme aplikácie. Ťukni na [[Nastavenia]], zapni [[Povoliť z tohto zdroja]] a vráť sa späť.",
     "Ťukni na [[Inštalovať]]. Ak sa ozve Google Play Protect, zvoľ [[Viac podrobností]] → [[Napriek tomu inštalovať]]. Aplikácia nie je z Obchodu Play, preto ju Android nepozná.",
     "Kronikár nájdeš medzi aplikáciami s ikonou knihy.",
   ]),
   ("h3", "Aktualizácia"),
   ("p", "Novšie `Kronikar.apk` nainštaluj priamo cez starú verziu. Údaje ostanú. Starú verziu predtým **neodinštalovávaj** – zmazali by sa projekty, ktoré nie sú uložené v priečinku."),
   ("tip", "Kam idú exporty", "PDF a Word súbory z Exportu sa v telefóne ukladajú do podpriečinka `exporty` vo vybranom priečinku."),
  ]},
  {"title": "Prvé spustenie: priečinok na projekty", "toc": "automatické ukladanie do súboru", "blocks": [
   ("lead", "Bez priečinka Kronikár ukladá len do prehliadača. To stačí na vyskúšanie, ale nie na skutočnú prácu: vymazanie údajov prehliadača by projekty zmazalo a nedali by sa synchronizovať."),
   ("steps", [
     "Vytvor si prázdny priečinok, napríklad `Kronikar`.",
     "Na úvodnej obrazovke Kronikára klikni na [[Vybrať priečinok]] a vyber ho.",
     "Prehliadač sa spýta na povolenie upravovať súbory. Potvrď [[Povoliť]] / [[Upraviť súbory]].",
     "Na Androide sa otvorí systémový výber priečinka: vyber alebo vytvor priečinok a ťukni na [[Použiť tento priečinok]] → [[Povoliť]].",
   ]),
   ("fig", "home", "Úvodná obrazovka s tlačidlom Vybrať priečinok."),
   ("table", ["Súbor v priečinku", "Čo obsahuje"], [
     ["`názov.kronikar.json`", "celý projekt – rukopis, svet, vzťahy, poznámky aj nastavenia exportu; prepíše sa po každej zmene"],
     ["`zalohy/`", "raz denne kópia každého projektu"],
     ["`kronikar-sablony.json`", "tvoje uložené šablóny sadzby"],
     ["`exporty/`", "len na Androide – exportované PDF a Word súbory"],
   ]),
   ("tip", "Povoliť prístup", "Po reštarte prehliadača sa niekedy na úvodnej obrazovke zobrazí [[Povoliť prístup]]. Stačí kliknúť – prehliadač sa z bezpečnostných dôvodov pýta znova."),
  ]},
  {"title": "Synchronizácia medzi zariadeniami", "toc": "Syncthing a iné možnosti", "blocks": [
   ("lead", "Kronikár sám nič neposiela na internet. Ak chceš písať na počítači aj v mobile, potrebuješ program, ktorý udržiava ten istý priečinok rovnaký na všetkých zariadeniach. Kronikár potom zmeny z ostatných zariadení načíta sám, približne každých 15 sekúnd."),
   ("h3", "Odporúčanie: Syncthing"),
   ("p", "Syncthing je bezplatný otvorený program. Zariadenia si súbory posielajú priamo medzi sebou, bez cloudu a bez účtu, a zmenu prenesú do niekoľkých sekúnd. Funguje na Windows, macOS, Linuxe aj Androide."),
   ("ul", [
     "Webová stránka a stiahnutie: ((https://syncthing.net))",
     "Pre Android: aplikácia **Syncthing-Fork** z Obchodu Google Play alebo z F-Droid: ((https://f-droid.org/packages/com.github.catfriend1.syncthingfork/))",
   ]),
   ("steps", [
     "Nainštaluj Syncthing na všetky zariadenia.",
     "Prepoj zariadenia navzájom (každé má svoje ID, stačí ho pridať na druhom).",
     "Zdieľaj medzi nimi priečinok `Kronikar`.",
     "Na každom zariadení v Kronikári vyber práve tento synchronizovaný priečinok.",
   ]),
   ("p", "Podrobný postup nastavenia nájdeš v dokumentácii Syncthingu – tu ho neopisujeme, lebo sa s novými verziami mení."),
   ("h3", "Iné možnosti"),
   ("p", "Poslúži hocijaký nástroj, ktorý synchronizuje **skutočný priečinok na disku** a robí to čo najrýchlejšie, ideálne okamžite."),
   ("table", ["Nástroj", "Poznámka"], [
     ["OneDrive, Dropbox, Google Drive na PC a Macu", "fungujú, ak je priečinok uložený v počítači (nie len „online“)"],
     ["Android", "oficiálne aplikácie cloudov zvyčajne nevytvoria skutočný priečinok – použi Syncthing alebo aplikáciu, ktorá priečinok synchronizuje obojsmerne"],
   ]),
   ("warn", "Nepíš na dvoch miestach naraz", "Ten istý projekt neupravuj súčasne na dvoch zariadeniach. Keď prechádzaš z počítača na mobil, počkaj pár sekúnd, kým sa zmena prenesie. Ak predsa vznikne konflikt, Kronikár nič nezahodí: druhú verziu uloží ako kópiu a na úvodnej obrazovke ponúkne [[Načítať ako kópiu]] alebo [[Zahodiť]]."),
  ]},
  {"title": "Zálohy, aktualizácie a problémy", "toc": "keď niečo nejde", "blocks": [
   ("h3", "Zálohy"),
   ("ul", [
     "Automaticky: raz denne do podpriečinka `zalohy`.",
     "Ručne: na karte projektu [[Záloha]] alebo v sekcii [[Projekt]] → [[Stiahnuť zálohu]]. Vznikne súbor `.json`.",
     "Obnovenie: na úvodnej obrazovke [[Obnoviť zo zálohy]].",
   ]),
   ("h3", "Nová verzia"),
   ("table", ["Kde", "Ako aktualizovať"], [
     ["Windows – inštalátor", "spusti nový `Kronikar-Setup.exe`, prepíše starú verziu"],
     ["Kronikar.html", "nahraď starý súbor novým (rovnaký názov a miesto)"],
     ["Android", "nainštaluj nové `Kronikar.apk` cez staré"],
   ]),
   ("p", "Projekty sa pri aktualizácii nemenia – sú v tvojom priečinku."),
   ("h3", "Riešenie problémov"),
   ("table", ["Problém", "Riešenie"], [
     ["Chýba tlačidlo Vybrať priečinok", "používaš Safari alebo Firefox – prejdi na Chrome, Edge alebo Brave; v Brave zapni `brave://flags/#file-system-access-api`"],
     ["Zmeny z iného zariadenia sa neukazujú", "skontroluj, či synchronizačný program beží na oboch zariadeniach a či je v Kronikári vybraný ten istý priečinok; počkaj aspoň 15 sekúnd"],
     ["Na úvodnej obrazovke je Povoliť prístup", "klikni naň – prehliadač po reštarte žiada povolenie znova"],
     ["Varovanie Windows SmartScreen alebo Play Protect", "aplikácia nie je podpísaná komerčným certifikátom; ak je súbor z oficiálneho zdroja, pokračuj cez Ďalšie informácie / Napriek tomu inštalovať"],
     ["Objavil sa projekt s „konflikt“ v názve", "dve zariadenia menili projekt naraz; porovnaj obe verzie a nepotrebnú zmaž"],
   ]),
  ]},
 ],
}

USAGE = {
 "title": "Ako písať v Kronikári",
 "subtitle": "Rukopis, svet, vzťahy, poznámky a export knihy – všetko, čo Kronikár vie, krok za krokom.",
 "meta_left": "Kronikár 1.6", "meta_right": "Návod 2 / 2",
 "toc_title": "Obsah", "hero": "write",
 "sections": [
  {"title": "Prehľad", "toc": "šesť sekcií projektu", "blocks": [
   ("lead", "Každá kniha je samostatný projekt. V projekte sa prepínaš medzi šiestimi sekciami v hornej lište (na mobile v dolnej)."),
   ("table", ["Sekcia", "Na čo slúži"], [
     ["Rukopis", "písanie textu, štruktúra častí, kapitol a scén, nástenka"],
     ["Svet", "postavy, miesta, rasy, náboženstvá, božstvá, mágia, frakcie, artefakty, udalosti a vlastné kategórie"],
     ["Vzťahy", "mapa vzťahov medzi záznamami sveta ako sieť alebo strom"],
     ["Poznámky", "lepiace poznámky s kategóriami, voliteľne priradené ku kapitolám"],
     ["Export", "PDF a Word – kniha, rukopis pre vydavateľstvo, obsah, popis knihy"],
     ["Projekt", "jazyk, úvodzovky, ciele, štatistiky a záloha"],
   ]),
   ("tip", "Začni ukážkou", "Na úvodnej obrazovke klikni na [[Ukážkový projekt]]. Otvorí sa krátka fantasy so svetom a vzťahmi, na ktorej si všetko vyskúšaš."),
   ("h3", "Projekty"),
   ("ul", [
     "[[Nový projekt]] – zadáš názov knihy, žáner a meno autora.",
     "Na karte projektu sú tlačidlá [[Záloha]] a [[Zmazať]]. Zmazanie sa vždy potvrdzuje.",
     "Jazyk aplikácie (slovenčina / angličtina) prepneš vpravo hore na úvodnej obrazovke alebo v sekcii Projekt.",
   ]),
  ]},
  {"title": "Rukopis", "toc": "štruktúra, editor, inšpektor, nástenka", "blocks": [
   ("fig", "write", "Rukopis: vľavo štruktúra, v strede text, vpravo inšpektor scény."),
   ("h3", "Štruktúra"),
   ("ul", [
     "Rukopis sa skladá z **častí**, **kapitol** a **scén**. Pridáš ich tlačidlami [[+ Scéna]], [[+ Kapitola]] a [[+ Časť]] dole vľavo.",
     "Poradie meníš ťahaním myšou alebo v inšpektore tlačidlami [[Vyššie]], [[Nižšie]] a [[Presunúť do…]].",
     "Farebná bodka pri scéne ukazuje jej stav, číslo vpravo počet slov. Číslo v béžovom rámčeku je počet otvorených lepiacich poznámok.",
     "Pole [[Hľadať v rukopise]] prehľadá názvy, synopsy aj text.",
   ]),
   ("h3", "Písanie"),
   ("ul", [
     "Text sa ukladá priebežne, netreba nič potvrdzovať.",
     "[[B]] a [[I]] (alebo {{Ctrl+B}} a {{Ctrl+I}}) – tučné a kurzíva; [[Na stred]] – centrovaný odsek; [[Citát]] – list alebo citát; [[* * *]] – oddeľovač scén.",
     "Ikona so štyrmi rohmi zapne **režim sústredenia** bez panelov. Ukončíš ho klávesom {{Esc}}.",
     "Úvodzovky sa píšu samé: {{\"}} vloží hlavné, {{'}} vnorené. Štýl (slovenské „…“, anglické “…” a ďalšie) nastavíš v sekcii Projekt.",
     "Vpravo hore je počet slov a normostrán (1 normostrana = 1 800 znakov vrátane medzier).",
   ]),
   ("h3", "Inšpektor"),
   ("p", "Panel vpravo otvoríš ikonou panelu v lište editora. Pri scéne v ňom nastavíš:"),
   ("ul", [
     "**Synopsu** – zobrazí sa na nástenke a dá sa z nej vygenerovať synopsa knihy.",
     "**Stav** – Nápad, Koncept, Revízia, Hotovo.",
     "**Rozprávača (POV)**, **miesto deja** a záznamy sveta, ktoré v scéne **vystupujú**.",
     "**Cieľ slov**, poznámky k scéne, **lepiace poznámky** a **odkazy**.",
     "**Zahrnúť do exportu** – čo odškrtneš, v knihe nebude.",
   ]),
   ("h3", "Nástenka"),
   ("p", "Klikni na kapitolu alebo časť. Zobrazia sa karty jej scén so synopsami a stavom – ako kartičky pripnuté na korkovej tabuli. [[Čítať celé]] ukáže celý text kapitoly naraz."),
   ("fig", "cork", "Nástenka kapitoly."),
  ]},
  {"title": "Zo slova rovno do sveta", "toc": "označ slovo a pridaj ho", "blocks": [
   ("lead", "Keď v texte vymyslíš nové meno, nemusíš odbiehať. Označ ho myšou (na mobile podržaním prsta) a objaví sa okienko."),
   ("fig", "selpop", "Označené slovo a okienko na pridanie do sveta."),
   ("steps", [
     "Uprav **základný tvar** mena, ak si označila skloňovaný tvar (napríklad *Ilsou* → *Ilsa*).",
     "Vyber kategóriu – Postava, Miesto, Rasa, Božstvo…",
     "Kronikár navrhne **skloňované tvary**. Nesprávne vypneš ťuknutím, vlastné dopíšeš.",
     "Zvoľ [[Uložiť a písať ďalej]] alebo [[Uložiť a otvoriť kartu]].",
   ]),
   ("p", "Okno zavrieš krížikom alebo klávesom {{Esc}}. Ak slovo patrí k existujúcemu záznamu (napríklad prezývka), vyber ho v časti **Je to tvar existujúceho záznamu?** alebo cez [[Priradiť ako tvar k inému záznamu…]]"),
   ("tip", "Prečo tvary", "Podľa tvarov mena Kronikár na karte záznamu ukáže, v ktorých scénach sa postava či miesto spomína (sekcia [[V rukopise]])."),
  ]},
  {"title": "Svet", "toc": "kategórie, záznamy, prepojenia", "blocks": [
   ("fig", "world", "Svet: kategórie, zoznam záznamov a karta postavy."),
   ("h3", "Kategórie"),
   ("ul", [
     "Vstavané: krajiny a miesta, postavy, rasy a národy, náboženstvá, božstvá, mágia, rody a frakcie, artefakty, dejiny a udalosti, poznámky.",
     "[[Nová kategória]] – vlastná kategória s názvom, farbou a vlastnými poliami (napríklad *Bytosti* s poliami Výskyt, Schopnosti, Slabiny).",
   ]),
   ("h3", "Karta záznamu"),
   ("ul", [
     "**Meno** a **jednou vetou** kto alebo čo to je.",
     "**Vlastnosti** – polia podľa kategórie. Božstvá a rasy majú povinné pole **Druh** s výberom alebo vlastnou hodnotou. [[Vlastné pole]] pridá ďalšie.",
     "**Prepojenia** – napíš vzťah (napríklad *ovláda*) a vyber druhý záznam. Kronikár ponúka vhodné vzťahy podľa kategórií.",
     "Keď vzťah prestane platiť (postava odíde, pohádajú sa), klikni na [[aktuálny]] a označ ho ako **minulý**, prípadne doplň **kedy**. Potom pridaj nový vzťah.",
     "**Tvary mena a prezývky**, **V rukopise** (kde sa spomína), **odkazy** (Instagram, YouTube, Spotify, mapy…) a voľné **poznámky**.",
   ]),
   ("fig", "world2", "Spodná časť karty: tvary mena s návrhmi skloňovania, odkazy a poznámky."),
  ]},
  {"title": "Vzťahy", "toc": "sieť a strom", "blocks": [
   ("fig", "graph", "Mapa vzťahov ako sieť."),
   ("ul", [
     "[[Sieť]] ukáže celý svet naraz. Veľkosť uzla zodpovedá počtu prepojení.",
     "[[Strom]] vychádza z jedného koreňa – napríklad krajina → jej postavy → ich viera a mágia. Koreň vyberieš hore alebo tlačidlom [[Strom odtiaľto]].",
     "Farebné filtre skryjú kategórie, [[Popisy vzťahov]] a [[Minulé vzťahy]] zapínajú popisy a neaktuálne vzťahy (prerušovaná čiara).",
     "[[Spájať]] – klikni na dva záznamy a pomenuj vzťah.",
     "Uzly ťaháš myšou, koliesko približuje. Klik na záznam otvorí vpravo jeho prepojenia.",
   ]),
  ]},
  {"title": "Poznámky", "toc": "lepiace papieriky", "blocks": [
   ("fig", "notes", "Lepiace poznámky s kategóriami."),
   ("ul", [
     "[[Nová poznámka]] pridá papierik. Text píšeš priamo do neho.",
     "Kategória (Zapracovať, Nápad, Overiť / dohľadať, Opraviť, Otázka) určuje farbu. Tlačidlom [[Kategórie]] ich premenuješ, prefarbíš alebo pridáš vlastné.",
     "[[+ Priradiť ku kapitole…]] – poznámka môže patriť k jednej či viacerým kapitolám a scénam, alebo ostať voľná.",
     "Fajka označí poznámku ako **vybavenú**. [[Skryť vybavené]] ich schová.",
     "Filtre: podľa kategórie, podľa kapitoly a vyhľadávanie v texte.",
     "V Rukopise vidíš poznámky vybranej scény v inšpektore (časť **Lepiace poznámky**) a môžeš tam rovno pridať novú.",
   ]),
  ]},
  {"title": "Export", "toc": "PDF a Word, šablóny, sadzba, popis knihy", "blocks": [
   ("fig", "export", "Export: šablóny, náhľad a sťahovanie."),
   ("h3", "Šablóny"),
   ("table", ["Skupina", "Šablóny"], [
     ["Tlačená kniha", "Klasická, Kronika (pre fantasy), Elegantná, Moderná"],
     ["Rukopis pre vydavateľstvo / agenta", "Rukopis (štandard), Rukopis SK / CZ (normostrany), US – Shunn, UK – agent, AU – vydavateľ"],
   ]),
   ("warn", "Over si pokyny", "Požiadavky na rukopis sa medzi vydavateľstvami líšia. Šablóny pokrývajú bežné zvyklosti, konkrétne pokyny si vždy prečítaj."),
   ("h3", "Nastavenia"),
   ("ul", [
     "**Kniha** – názov, podtitul, autor, žáner, kontakt a **jazyk knihy** (podľa neho sa píše *Prvá kapitola* alebo *Chapter One*, *Obsah* alebo *Contents*).",
     "**Sadzba** – formát strany, písmo, veľkosť, riadkovanie, okraje, zarovnanie, číslovanie kapitol, **úvodzovky v exporte**, oddeľovač scén, záhlavie a obsah.",
     "**Podrobná sadzba a vlastné šablóny** – odsadenie, medzery, úvod kapitoly (iniciála, kapitálky), nadpisy, čísla strán, kapitoly na pravej strane. [[Uložiť ako šablónu]] ich zapamätá pre všetky projekty.",
     "**Úvodné strany** – venovanie a tiráž.",
     "**Popis knihy** – logline, anotácia a synopsa. Synopsu môžeš vygenerovať zo synops kapitol a scén.",
   ]),
   ("fig", "export2", "Sadzba a úvodné strany."),
   ("h3", "Čo sa dá stiahnuť"),
   ("table", ["Voľba", "Obsah"], [
     ["Celá kniha", "titulná strana, tiráž, venovanie, obsah a text – PDF alebo Word"],
     ["Len text knihy", "kapitoly bez úvodných strán, napríklad ukážka prvých kapitol"],
     ["Len obsah", "zoznam častí a kapitol s číslami strán"],
     ["Popis knihy", "údaje, logline, anotácia a synopsa"],
     ["Ostatné", "Markdown (čistý text) a záloha projektu"],
   ]),
  ]},
  {"title": "Projekt a nastavenia", "toc": "jazyk, úvodzovky, ciele, štatistiky", "blocks": [
   ("fig", "stats", "Sekcia Projekt."),
   ("ul", [
     "**Jazyk aplikácie** – slovenčina alebo angličtina. Mení len texty aplikácie, nie tvoj rukopis.",
     "**Úvodzovky pri písaní** a tlačidlo [[Prepísať úvodzovky v celom rukopise na…]], ktoré prevedie už napísaný text.",
     "**Ciele** – celkový počet slov a slov denne. Plnenie vidíš v hornej lište.",
     "**Štatistiky** – slová, normostrany, scény, záznamy sveta, graf písania za 30 dní a stav scén.",
     "**Všetky odkazy** z celého projektu na jednom mieste a [[Stiahnuť zálohu]].",
   ]),
  ]},
  {"title": "Na mobile", "toc": "rozdiely v telefóne", "blocks": [
   ("fig", ["phone", "phone_world"], "Kronikár v telefóne: rukopis a svet.", "pair"),
   ("ul", [
     "Sekcie sú v dolnej lište. Druhým ťuknutím na [[Rukopis]] otvoríš alebo zavrieš zoznam kapitol a scén.",
     "Slovo označíš podržaním prsta. Okienko na pridanie do sveta sa ukáže na opačnom okraji obrazovky, aby ho neprekrývala lišta Androidu (Kopírovať, Vložiť…).",
     "Exporty sa ukladajú do podpriečinka `exporty`.",
   ]),
  ]},
  {"title": "Klávesové skratky a tipy", "toc": "", "blocks": [
   ("table", ["Kláves", "Čo urobí"], [
     ["{{Ctrl+B}} / {{Ctrl+I}}", "tučné / kurzíva"],
     ["{{\"}} / {{'}}", "hlavné / vnorené úvodzovky podľa nastavenia"],
     ["{{Enter}} v názve scény", "skok do textu scény"],
     ["{{Esc}}", "ukončí režim sústredenia, zavrie okienko pri označenom slove"],
   ]),
   ("tip", "Tip", "Prázdne riadky medzi odsekmi nepíš – {{Enter}} vytvorí nový odsek a odsadenie či medzery doplní export podľa šablóny."),
  ]},
 ],
}

DOCS = {"kronikar-instalacia": INSTALL, "kronikar-pouzivanie": USAGE}

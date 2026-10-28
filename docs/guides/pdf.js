const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const docs = [['kronikar-instalacia_sk','Kronikár – Inštalácia a synchronizácia','Strana'],['kronikar-pouzivanie_sk','Kronikár – Ako písať v Kronikári','Strana'],['kronikar-installation_en','Kronikár – Installation and sync','Page'],['kronikar-user-guide_en','Kronikár – Writing with Kronikár','Page']];
  for (const [f, title, pg] of docs) {
    await p.goto('file://' + path.resolve(f + '.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join('..', f.replace(/_(sk|en)$/, '') + '.pdf'), format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#8790A1;padding:0 19mm;display:flex;justify-content:space-between"><span>${title}</span><span>${pg} <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
      margin: { top: '18mm', bottom: '20mm', left: '19mm', right: '19mm' } });
  }
  await b.close();
})();

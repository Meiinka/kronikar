const { chromium } = require('playwright');
const path = require('path'); const ROOT = path.resolve(__dirname, '..', '..');
(async () => {
  const b = await chromium.launch();
  for (const L of ['sk','en']) {
    const ctx = await b.newContext({ viewport:{width:1280,height:780}, deviceScaleFactor:1.5, locale: L==='sk'?'sk-SK':'en-US' });
    const p = await ctx.newPage();
    await p.addInitScript(l => { localStorage.setItem('kronikar:lang', l); }, L);
    await p.goto('file://' + ROOT + '/dist/Kronikar.html'); await p.waitForTimeout(800);
    const shot = async (n, opt={}) => { await p.waitForTimeout(450); await p.screenshot({path:`${ROOT}/docs/img/${L}_${n}.jpg`, type:'jpeg', quality:82, ...opt}); };
    await shot('home');
    await p.click('#btnSample'); await p.waitForTimeout(1000);
    await p.evaluate(()=>{ toggleInsp && toggleInsp(true); }); await shot('write');
    // selection popup
    await p.evaluate(()=>{ toggleInsp(false); const ed=document.querySelector('#ed'); const ps=[...ed.querySelectorAll('p')]; for (const el of ps) { const tn=el.firstChild; if(!tn||tn.nodeType!==3) continue; const m=tn.data.match(/\b(mecha|bellows|kladiva|hammer)\b/); if(m){ const r=document.createRange(); r.setStart(tn,m.index); r.setEnd(tn,m.index+m[0].length); getSelection().removeAllRanges(); getSelection().addRange(r); break; } } });
    await p.waitForTimeout(700); await shot('selpop');
    await p.evaluate(()=>{ SelPop.close(); S.sel = S.p.binder[0].children[0].id; renderMode(); }); await shot('cork');
    await p.evaluate(()=>{ setMode('world'); openEnt(Object.values(S.ents).find(e=>e.cat==='postava' && /Ilsa/.test(e.name)).id); }); await shot('world');
    await p.evaluate(()=>{ document.querySelector('.pane.center, .world-detail, #wDetail')?.scrollTo?.(0, 900); const d=[...document.querySelectorAll('*')].find(x=>x.scrollHeight>x.clientHeight+200 && getComputedStyle(x).overflowY==='auto' && x.querySelector('#eSum')); if(d) d.scrollTop=820; }); await shot('world2');
    await p.evaluate(()=>setMode('graph')); await p.waitForTimeout(1500); await shot('graph');
    await p.evaluate(()=>setMode('notes')); await shot('notes');
    await p.evaluate(()=>setMode('export')); await p.waitForTimeout(600); await shot('export');
    await p.evaluate(()=>{ const x=document.querySelector('.export'); x.scrollTop=1150; }); await shot('export2');
    await p.evaluate(()=>setMode('stats')); await shot('stats');
    await ctx.close();
    // phone
    const m = await b.newContext({ viewport:{width:390,height:780}, deviceScaleFactor:2, locale: L==='sk'?'sk-SK':'en-US', hasTouch:true, isMobile:true });
    const q = await m.newPage(); await q.addInitScript(l => { localStorage.setItem('kronikar:lang', l); }, L);
    await q.goto('file://' + ROOT + '/dist/Kronikar.html'); await q.waitForTimeout(800);
    await q.click('#btnSample'); await q.waitForTimeout(1000);
    await q.screenshot({path:`${ROOT}/docs/img/${L}_phone.jpg`, type:'jpeg', quality:82});
    await q.evaluate(()=>setMode('world')); await q.waitForTimeout(400); await q.screenshot({path:`${ROOT}/docs/img/${L}_phone_world.jpg`, type:'jpeg', quality:82});
    await m.close();
  }
  await b.close();
})();

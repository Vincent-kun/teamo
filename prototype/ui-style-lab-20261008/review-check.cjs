const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const target = process.argv[2];
  const out = process.argv[3];
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 1 });
  const errs = [], warns = [];
  page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); if (m.type() === 'warning') warns.push(m.text()); });
  page.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
  await page.goto('file:///' + target.replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(1200);

  const stat = await page.evaluate(() => {
    const q = s => document.querySelectorAll(s).length;
    const phones = [...document.querySelectorAll('.phone')];
    const empties = phones.filter(p => !p.querySelector('.sc') || !p.querySelector('.sc').children.length).length;
    const overflowX = document.documentElement.scrollWidth - document.documentElement.clientWidth;
    const rects = phones.slice(0, 5).map(p => { const r = p.getBoundingClientRect(); return [Math.round(r.width), Math.round(r.height)]; });
    return {
      phones: q('.phone'), slots: q('.slot'), strips: q('.strip'), sections: q('.dir'),
      divs: q('.dev-unit'), empties, overflowX, rects,
      title: document.title,
      bodyH: document.body.scrollHeight
    };
  });
  console.log(JSON.stringify({ stat, errs, warns: warns.slice(0, 5) }, null, 1));

  await page.screenshot({ path: out, fullPage: false });
  await browser.close();
})();

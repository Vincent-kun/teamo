const { chromium } = require('playwright');
(async () => {
  const target = process.argv[2];
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1500, height: 1100 } });
  await page.goto('file:///' + target.replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(900);
  const rows = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.sc').forEach(sc => {
      const skin = sc.getAttribute('data-skin');
      const cs = getComputedStyle(sc);
      // sample a brand-colored element if present (button/brand chip)
      const brandEl = sc.querySelector('[data-brand]') || sc.querySelector('.btn') || sc.querySelector('.brand');
      const brand = brandEl ? getComputedStyle(brandEl).backgroundColor : null;
      out.push({
        skin,
        bg: cs.backgroundColor,
        surface: getComputedStyle(sc.querySelector('.card') || sc).backgroundColor,
        brand: brand || '(none)'
      });
    });
    // de-dupe by skin
    const seen = new Set(); const uniq = [];
    out.forEach(r => { if (!seen.has(r.skin)) { seen.add(r.skin); uniq.push(r); } });
    return uniq;
  });
  console.log(JSON.stringify(rows, null, 1));
  await browser.close();
})();

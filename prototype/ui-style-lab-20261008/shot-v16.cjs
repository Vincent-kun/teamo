const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  await page.goto('file:///D:/work/sportmate/prototype/ui-style-lab-20261008/index.html?mobile=1', { waitUntil: 'load' });
  await page.waitForTimeout(1200);
  for (const p of ['home', 'ai', 'growth']) {
    if (p !== 'home') { await page.click(`[data-flow="nav-${p}"]`); await page.waitForTimeout(400); }
    await page.screenshot({ path: `_shots/v16-${p}.png` });
  }
  await browser.close();
  console.log('shots done');
})();

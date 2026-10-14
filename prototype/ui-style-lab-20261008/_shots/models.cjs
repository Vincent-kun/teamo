const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1000 } });
  await page.goto('file:///D:/work/sportmate/prototype/ui-style-lab-20261008/index.html', { waitUntil: 'load' });
  await page.waitForTimeout(1000);
  const targets = ['ip16pm', 'hwmt60', 'hwpr70', 'opfx7', 'oprn12', 'ss24u', 'ss24', 'ip13'];
  for (const id of targets) {
    await page.selectOption('#lab-model', id);
    await page.waitForTimeout(500);
    const sel = await page.$('.stage-phone .phone');
    await sel.screenshot({ path: `_shots/m-${id}.png` });
    const notch = await page.$eval('.stage-phone .phone', el => el.getAttribute('data-notch'));
    console.log(id, '->', notch);
  }
  await browser.close();
  console.log('model shots done');
})();

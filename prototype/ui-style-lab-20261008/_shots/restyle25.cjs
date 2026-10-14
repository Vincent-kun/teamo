// V2.5 target-layout restyle: screenshot phone home + device pages
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1500, height: 1000 } });
  await page.goto('file:///' + path.resolve(__dirname, '..', 'deploy', 'index.html').replace(/\\/g, '/'));
  await page.waitForTimeout(700);
  const phone = page.locator('.phone').first();
  // home
  await page.evaluate("STATE.page='home';STATE.direction='clear';STATE.version=2;render()");
  await page.waitForTimeout(500);
  await phone.screenshot({ path: path.join(__dirname, 'restyle-home.png') });
  // device page
  await page.evaluate("STATE.page='device';render()");
  await page.waitForTimeout(500);
  await phone.screenshot({ path: path.join(__dirname, 'restyle-device.png') });
  await browser.close();
  console.log('shots done');
})();

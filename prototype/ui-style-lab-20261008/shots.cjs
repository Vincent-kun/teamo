const { chromium } = require('playwright');
(async () => {
  const target = process.argv[2];
  const dir = process.argv[3];
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1500, height: 1100 }, deviceScaleFactor: 1.4 });
  await page.goto('file:///' + target.replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(1600);
  const strips = await page.$$('.strip');
  for (let i = 0; i < strips.length; i++) {
    await strips[i].scrollIntoViewIfNeeded();
    await page.waitForTimeout(150);
    await strips[i].screenshot({ path: `${dir}/strip-${i}.png` });
  }
  // 设备端行
  const devrows = await page.$$('.dev-row');
  for (let i = 0; i < devrows.length; i++) {
    await devrows[i].scrollIntoViewIfNeeded();
    await page.waitForTimeout(150);
    await devrows[i].screenshot({ path: `${dir}/dev-${i}.png` });
  }
  await browser.close();
  console.log('done strips=' + strips.length + ' devrows=' + devrows.length);
})();

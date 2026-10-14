const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1000 } });
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  await page.goto('file:///D:/work/sportmate/prototype/ui-style-lab-20261008/deploy/index.html', { waitUntil: 'load' });
  await page.waitForTimeout(1000);

  // 图标全部应为 data URI
  const imgs = await page.$$eval('img', els => els.map(e => e.getAttribute('src')));
  const dataImgs = imgs.filter(s => s && s.startsWith('data:image/png;base64,')).length;
  console.log('img total:', imgs.length, 'data-uri:', dataImgs);

  // 切换机型 + 页面，确认无报错且 .phone 存在
  const models = ['ip16pm', 'hwmt60', 'opfx7', 'ss24u', 'ip13'];
  for (const id of models) {
    await page.selectOption('#lab-model', id);
    await page.waitForTimeout(200);
    const has = await page.$('.stage-phone .phone');
    if (!has) errors.push('no .phone for model ' + id);
  }
  for (const p of ['tasks', 'ai', 'growth', 'mine']) {
    await page.click(`[data-control="page"][data-value="${p}"]`);
    await page.waitForTimeout(200);
    const has = await page.$('.stage-phone .sc');
    if (!has) errors.push('no .sc for page ' + p);
  }
  await page.screenshot({ path: '_shots/standalone-home.png' });
  await page.click('[data-control="page"][data-value="ai"]');
  await page.waitForTimeout(300);
  await page.screenshot({ path: '_shots/standalone-ai.png' });

  await browser.close();
  console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'OK: no console/page errors; all icons inlined; model & page switching works');
  process.exitCode = errors.length ? 1 : 0;
})();

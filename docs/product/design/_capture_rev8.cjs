const { chromium } = require('playwright-core');
const fs = require('fs');

const OUT = 'assets/teamo-icons-20261009/_check';
if (!fs.existsSync(OUT)) fs.mkdirSync(OUT, { recursive: true });

const URL = 'http://localhost:8792/' + encodeURIComponent('Teamo设备端UE展示.html') + '?v=' + Date.now();

(async () => {
  const browser = await chromium.launch({
    channel: 'msedge',
    args: ['--no-proxy-server', '--disable-dev-shm-usage']
  });
  const page = await browser.newPage({ viewport: { width: 1280, height: 920 }, deviceScaleFactor: 2 });
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push('PAGEERR: ' + e.message));

  await page.goto(URL, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  // device element at idle
  const wrap = await page.$('.device-wrap');
  await wrap.screenshot({ path: OUT + '/rev8-idle.png' });

  // privacy closed
  await page.evaluate(() => togglePrivacy());
  await page.waitForTimeout(300);
  await wrap.screenshot({ path: OUT + '/rev8-privacy.png' });

  // back to open
  await page.evaluate(() => togglePrivacy());
  await page.waitForTimeout(300);

  // screen element alone (in-screen states)
  const screen = await page.$('#screen');
  for (const s of ['todo', 'plan', 'select', 'running']) {
    await page.evaluate(m => go(m), s);
    await page.waitForTimeout(300);
    await screen.screenshot({ path: OUT + '/rev8-' + s + '.png' });
  }

  // mobile
  await page.evaluate(() => go('idle'));
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(300);
  await wrap.screenshot({ path: OUT + '/rev8-mobile.png' });

  console.log('ERRORS:', errors.length ? errors.join(' | ') : 'none');
  await browser.close();
})().catch(e => { console.error('FATAL', e); process.exit(1); });

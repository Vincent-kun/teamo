const { chromium } = require('playwright-core');
const fs = require('fs');

const OUT = 'assets/teamo-icons-20261009/_check';
if (!fs.existsSync(OUT)) fs.mkdirSync(OUT, { recursive: true });

const URL = 'http://127.0.0.1:8791/' + encodeURIComponent('Teamo设备端UE展示.html') + '?v=' + Date.now();

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
  await page.waitForTimeout(400);

  // desktop full page (split layout)
  await page.screenshot({ path: OUT + '/rev7-desktop.png', fullPage: true });

  // device element at idle
  const screen = await page.$('#screen');
  await screen.screenshot({ path: OUT + '/rev7-idle.png' });

  // in-screen states
  const states = ['todo', 'plan', 'rank', 'select', 'target', 'running', 'task_arrive'];
  for (const s of states) {
    await page.evaluate(m => go(m), s);
    await page.waitForTimeout(350);
    await screen.screenshot({ path: OUT + '/rev7-' + s + '.png' });
  }

  // privacy (camera cover)
  await page.evaluate(() => go('idle'));
  await page.waitForTimeout(200);
  await page.evaluate(() => togglePrivacy());
  await page.waitForTimeout(250);
  await screen.screenshot({ path: OUT + '/rev7-privacy.png' });

  // mobile width full page
  await page.setViewportSize({ width: 390, height: 844 });
  await page.evaluate(() => { togglePrivacy(); });
  await page.waitForTimeout(200);
  await page.screenshot({ path: OUT + '/rev7-mobile.png', fullPage: true });

  console.log('ERRORS:', errors.length ? errors.join(' | ') : 'none');
  await browser.close();
})().catch(e => { console.error('FATAL', e); process.exit(1); });

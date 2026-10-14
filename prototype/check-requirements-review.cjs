// Browser review follows the repository's existing review-check.cjs pattern.
// Run: node prototype/check-requirements-review.cjs <bundled-node_modules>
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { pathToFileURL } = require('node:url');
const { chromium } = require(require.resolve('playwright', { paths: [process.argv[2]] }));

(async () => {
  const root = __dirname, out = path.join(root, 'requirements-review-evidence');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage({ viewport: { width: 1536, height: 1100 } });
  const errors = [], checks = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  const check = (label, condition) => { assert.ok(condition, label); checks.push(label); };
  try {
    await page.goto(pathToFileURL(path.join(root, 'requirements-review-workbench.html')).href);
    check('Reader overview is the default entry', await page.locator('#view-start').isVisible());
    await page.locator('#tab-trace').click();
    check('Initial view includes all 45 PRD rows', await page.locator('[data-req]').count() === 45);
    await page.screenshot({ path: path.join(out, 'trace-desktop.png') });
    await page.locator('#req-module').selectOption('A');
    check('All seven actions remain visible in PRD module A', await page.locator('[data-req]').count() === 8);
    await page.locator('[data-req="R08"]').click();
    check('Plank retains effective duration and does not claim session time is its result', (await page.locator('#req-detail').innerText()).includes('不能用会话用时充当成绩'));
    await page.locator('#req-module').selectOption('all');
    await page.locator('#req-search').fill('R30');
    await page.locator('[data-req="R30"]').click();
    check('Offline local recognition is shown as an existing PRD requirement', (await page.locator('#req-detail').innerText()).includes('PRD已有明确要求'));
    await page.locator('#req-search').fill('');
    await page.locator('[data-req="R03"]').click();
    await page.locator('#req-draft select[name="scope"]').selectOption('建议本次纳入');
    await page.locator('#req-draft input[name="owner"]').fill('本地评审测试');
    await page.locator('#req-draft textarea[name="notes"]').fill('草稿往返测试；不是批准。');
    await page.locator('#req-draft button[type="submit"]').click();
    check('Draft save leaves approval and validation axes unchanged', (await page.locator('#req-detail .axis').innerText()).includes('REVIEW / 未批准'));
    const downloadPromise = page.waitForEvent('download');
    await page.locator('#export-review').click();
    const download = await downloadPromise, draftPath = path.join(out, 'roundtrip-draft.json');
    await download.saveAs(draftPath);
    const exported = JSON.parse(fs.readFileSync(draftPath, 'utf8'));
    check('Export includes original baseline and clearly marked discussion draft', exported.kind === 'teamo-review-draft' && exported.draft.requirements.R03.owner === '本地评审测试');
    await page.reload();
    check('Reload starts with source state rather than an implicit approval', (await page.locator('#req-draft input[name="owner"]').inputValue()) === '');
    await page.locator('#review-file').setInputFiles(draftPath);
    check('Explicit import restores only draft fields', await page.locator('#req-draft input[name="owner"]').inputValue() === '本地评审测试');
    await page.locator('#review-file').setInputFiles({ name: 'invalid.json', mimeType: 'application/json', buffer: Buffer.from('{"kind":"wrong"}') });
    check('Invalid import is rejected without overwriting current draft', (await page.locator('#footer-status').innerText()).includes('导入失败') && await page.locator('#req-draft input[name="owner"]').inputValue() === '本地评审测试');
    await page.locator('#req-detail [data-target="D02"]').click();
    check('Requirement decision reference opens the matching issue', (await page.locator('#decision-detail').innerText()).includes('D02'));
    await page.locator('#tab-state').click();
    await page.locator('#state-branches [data-target="pause"]').click();
    check('Pause retains progress and next confirmed repetition is 13', (await page.locator('#state-detail').innerText()).includes('13'));
    check('Pause recovery has an explicit guard and pending countdown decision', (await page.locator('#transition-table').innerText()).includes('OPEN-006'));
    await page.screenshot({ path: path.join(out, 'states-desktop.png') });
    await page.locator('#state-detail [data-go="req"]').first().click();
    check('State returns to its source requirement', await page.locator('#view-trace').isVisible());
    await page.locator('#tab-decision').click();
    await page.locator('[data-decision-group="open"]').click();
    await page.locator('[data-decision="OPEN-001"]').click();
    await page.locator('[data-option="2"]').click();
    check('Comparing streaming does not accept a decision', (await page.locator('#option-preview').innerText()).includes('未改变范围或方案状态') && (await page.locator('#decision-detail').innerText()).includes('待讨论 · 非已接受 ADR'));
    await page.screenshot({ path: path.join(out, 'decisions-desktop.png') });
    await page.locator('#tab-delivery').click();
    check('Delivery view retains 25 work packages and unregistered evidence', await page.locator('#acceptance-table tbody tr').count() === 25 && (await page.locator('#gate-detail').innerText()).includes('未登记'));
    const sizes = [];
    for (const width of [1536, 1024, 390, 320]) {
      await page.setViewportSize({ width, height: 1100 });
      for (const tab of ['trace', 'state', 'decision', 'delivery']) {
        await page.locator('#tab-'+tab).click();
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
        check(`${width}px ${tab} has no page-wide horizontal overflow`, overflow <= 1);
        sizes.push({ width, view: tab, overflow });
      }
      if (width === 390) { await page.locator('#tab-trace').click(); await page.screenshot({ path: path.join(out, 'trace-mobile.png') }); }
    }
    check('No browser runtime errors', errors.length === 0);
    const sourceLinks = await page.locator('a').evaluateAll(links => links.map(a => a.href).filter(h => h.startsWith('file:')));
    for (const href of sourceLinks) check('Local link exists: '+decodeURI(href.split('/').at(-1)), fs.existsSync(require('node:url').fileURLToPath(href)));
    fs.writeFileSync(path.join(out, 'browser-review.json'), JSON.stringify({ checkedAt: new Date().toISOString(), status: 'passed', checks, errors, viewports: sizes, scope: 'UI navigation, source tracing, draft roundtrip and responsive layout; no real hardware or algorithm acceptance.' }, null, 2));
    console.log(JSON.stringify({ status: 'passed', checks: checks.length, errors, evidence: out }));
  } catch (error) {
    fs.writeFileSync(path.join(out, 'browser-review.json'), JSON.stringify({ checkedAt: new Date().toISOString(), status: 'failed', checks, errors, failure: error.message }, null, 2));
    throw error;
  } finally { await browser.close(); }
})().catch(e => { console.error(e.stack); process.exitCode=1; });

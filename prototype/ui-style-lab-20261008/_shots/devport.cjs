const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 1000 } });
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  await page.goto('file:///D:/work/sportmate/prototype/ui-style-lab-20261008/index.html', { waitUntil: 'load' });
  await page.waitForTimeout(800);
  const shot = async n => {
    await page.waitForTimeout(420); /* 等 devFadeIn .3s 播完，避免截到半透明帧 */
    const el = await page.$('.stage-device .dev-unit');
    await el.screenshot({ path: `_shots/devport-${n}.png` });
  };
  const run = js => page.evaluate(js);

  await shot('1-idle');
  await run(`flow.dispatch({type:'CREATE',id:'d1',action:'开合跳',target:20});flow.dispatch({type:'ACCEPTED',commandId:'d1-create'});`);
  await shot('2-arrive');
  await run(`deviceAction('receive')`);
  await shot('3-ready');
  await run(`deviceAction('prepare')`);
  await shot('4-entry');
  await run(`deviceAction('present')`);
  await run(`deviceAction('countdown')`);
  await shot('5-countdown');
  await run(`deviceAdvance();deviceAdvance();deviceAdvance();`);
  await run(`for(let i=0;i<5;i++)deviceAction('count')`);
  await shot('6-running');
  await run(`deviceAction('pause')`);
  await shot('7-paused');
  await run(`deviceAction('privacy')`);
  await shot('8-privacy');
  await run(`deviceAction('privacy')`);
  await run(`deviceAction('away')`);
  await shot('9-away');
  await run(`deviceAction('present');deviceAction('countdown');deviceAdvance();deviceAdvance();deviceAdvance();`);
  await run(`for(let i=0;i<15;i++)deviceAction('count')`);
  await shot('10-celebrate');
  await run(`deviceAction('idle');deviceAction('online')`);
  await shot('11-offline');
  await run(`deviceAction('online')`);
  await run(`flowAction('reset');render()`);
  await shot('12-idle-reset');

  await browser.close();
  console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'OK: no console/page errors; 12 device states captured');
  process.exitCode = errors.length ? 1 : 0;
})();

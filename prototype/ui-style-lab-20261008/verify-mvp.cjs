const { chromium } = require('playwright');
(async () => {
  const target = process.argv[2];
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1500, height: 1100 } });
  const errs = [];
  page.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text()); });
  await page.goto('file:///' + target.replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(1400);
  const out = await page.evaluate(() => {
    const q = s => document.querySelectorAll(s).length;
    const scs = [...document.querySelectorAll('.sc')];
    /* 按页型分别校验 MVP 关键文案（四屏各自的关键词组） */
    const PAGE_KEYS = {
      home:    ['客厅运动伙伴','AI 运动计划助手','今日任务','摄像头带物理遮挡'],
      tasks:   ['运动邀请','发出邀请','设备已确认接收'],
      device:  ['客厅运动伙伴','物理隐私滑盖','准备好陪你运动','设备能力'],
      analysis:['动作质量','AI 建议','不作为医疗判断']
    };
    const kinds = { home:0, tasks:0, device:0, analysis:0, unknown:0 };
    let withKeys = 0, totalKeys = 0;
    const missed = [];
    const skins = {};
    scs.forEach(sc => {
      const txt = sc.innerText || '';
      let kind = 'unknown';
      if (txt.includes('准备好陪你运动') && txt.includes('物理隐私滑盖')) kind = 'device';
      else if (txt.includes('设备已确认接收')) kind = 'tasks';
      else if (txt.includes('不作为医疗判断')) kind = 'analysis';
      else if (txt.includes('AI 运动计划助手')) kind = 'home';
      kinds[kind]++;
      if (kind !== 'unknown') {
        const miss = PAGE_KEYS[kind].filter(k => !txt.includes(k));
        totalKeys += PAGE_KEYS[kind].length;
        withKeys += PAGE_KEYS[kind].length - miss.length;
        if (miss.length) missed.push({ skin: sc.getAttribute('data-skin'), kind, miss });
      }
      const sk = sc.getAttribute('data-skin');
      if (!skins[sk]) {
        const btn = sc.querySelector('.eb-btn,.cl-btn,.kp-btn,.btn');
        skins[sk] = {
          bg: getComputedStyle(sc).backgroundColor,
          brand: btn ? getComputedStyle(btn).backgroundColor : '(none)'
        };
      }
    });
    return {
      totalSc: scs.length,
      kinds, withKeys, totalKeys, missed,   /* withKeys 期望 = totalKeys（36 屏 × 各自关键词全命中） */
      ebPages: q('.eb-page'),  /* 期望 12（3 皮肤 × 4 页） */
      clPages: q('.cl-page'),  /* 期望 12 */
      kpPages: q('.kp-page'),  /* 期望 12 */
      marquees: q('.kp-marq'), /* 期望 12（仅方向三每页一条） */
      clayCards: q('.cl-clay'),
      bentoCells: q('.eb-cell'),
      lgIn: q('.lg-in'),       /* 期望 36 */
      skins
    };
  });
  console.log(JSON.stringify({ errs, ...out }, null, 1));
  await browser.close();
})();

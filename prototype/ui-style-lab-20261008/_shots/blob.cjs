const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  await page.goto('file:///D:/work/sportmate/prototype/ui-style-lab-20261008/index.html?mobile=1', { waitUntil: 'load' });
  await page.waitForTimeout(1000);
  await page.evaluate(`(()=>{
    const el=[...document.querySelectorAll('.section-title')].find(e=>e.textContent.includes('今日任务'));
    if(el)el.scrollIntoView({block:'start'});
  })()`);
  await page.waitForTimeout(300);
  await page.screenshot({ path: '_shots/blob-mobile.png' });
  const info = await page.evaluate(`(()=>{
    const item=[...document.querySelectorAll('.list-item')][0];
    if(!item)return {err:'no list-item', all:[...document.querySelectorAll('.section-title')].map(e=>e.textContent.slice(0,12))};
    const r=item.getBoundingClientRect();
    const stack=document.elementsFromPoint(r.left+r.width/2, r.top+r.height/2)
      .map(e=>e.tagName+'.'+(e.className&&e.className.toString().slice(0,50))+' '+Math.round(e.getBoundingClientRect().width)+'x'+Math.round(e.getBoundingClientRect().height));
    const imgs=[...document.querySelectorAll('img')].map(i=>({cls:i.className,src:decodeURIComponent((i.src||'').slice(-30)),box:Math.round(i.getBoundingClientRect().width)+'x'+Math.round(i.getBoundingClientRect().height),nat:i.naturalWidth+'x'+i.naturalHeight})).filter(i=>i.box.split('x')[0]>60||i.nat.split('x')[0]>200);
    return {stack,imgs};
  })()`);
  console.log(JSON.stringify(info, null, 1));
  await browser.close();
})();

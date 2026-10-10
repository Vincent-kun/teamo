const {chromium}=require('C:/Users/13896/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path=require('path');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Users/13896/AppData/Local/ms-playwright/chromium-1234/chrome-win64/chrome.exe'});
 const page=await browser.newPage({viewport:{width:1440,height:1050}});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file:///'+path.join(__dirname,'index.html').replace(/\\/g,'/'));
 await page.waitForSelector('#gallery .product');
 const results=[];
 for(const code of ['S0','S1','S2','S3','S4','S5']){
  await page.locator(`[data-scheme="${code}"]`).click();
  results.push({scheme:code,state:await page.evaluate(()=>window.teamoReview.state),title:await page.locator('#scene-title').textContent()});
 }
 await page.locator('[data-scheme="S4"]').click();
 const a=await page.locator('#width-result').textContent();
 await page.locator('#envelope').selectOption('B');const b=await page.locator('#width-result').textContent();
 if(!a.includes('宽轴不足')||!b.includes('仅宽轴必要条件满足'))throw Error('Width check did not update');
 await page.locator('#ortho-btn').click();
 await page.locator('#part-buttons button').filter({hasText:'D05'}).click();
 await page.locator('#open-photo').click();if(!await page.locator('#image-dialog').isVisible())throw Error('Photo modal failed');await page.locator('#close-dialog').click();
 await page.locator('#wall').fill('');if(!(await page.locator('#width-result').textContent()).includes('请填有效'))throw Error('Invalid budget not rejected');await page.locator('#wall').fill('2');
 const quote=page.locator('#quote-inputs input').first();await quote.fill('123.45');if(!(await page.locator('#quote-result').textContent()).includes('123.45'))throw Error('Quote total failed');await quote.fill('');
 await page.locator('#filters button').filter({hasText:'摄像头'}).click();if(await page.locator('#gallery .product').count()!==2)throw Error('Filter failed');await page.locator('#filters button').filter({hasText:'全部',exact:true}).click();
 const images=await page.evaluate(async()=>{for(const im of document.images){im.loading='eager';await im.decode().catch(()=>{})}return [...document.images].filter(i=>i.getAttribute('src')&&!i.naturalWidth).map(i=>i.getAttribute('src'))});
 await page.locator('[data-scheme="S3"]').click();await page.locator('#iso-btn').click();
 fs.mkdirSync(path.join(__dirname,'review'),{recursive:true});
 for(const width of [1440,768,390,320]){
  await page.setViewportSize({width,height:1050});await page.waitForTimeout(150);
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
  if(overflow)throw Error(`Horizontal page overflow at ${width}`);
  await page.screenshot({path:path.join(__dirname,'review',`width-${width}.png`),fullPage:width===1440});
 }
 if(errors.length||images.length)throw Error(JSON.stringify({errors,images}));
 const report={date:'2026-10-08',results,widthBudget:{A:a,B:b},testedWidths:[1440,768,390,320],pageErrors:errors,brokenImages:images,status:'passed',notes:'Local file browser check; geometry remains candidate envelopes, not CAD fit approval.'};
 fs.writeFileSync(path.join(__dirname,'review','browser-check.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});

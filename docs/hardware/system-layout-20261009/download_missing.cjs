// 二次补抓无图候选：无头浏览器加载型号页 → og:image / 页面主图 → 带 Referer 下载
// 规则：只收型号页自身的图；拿不到就留缺，不用近似图充数。结果同步回 WP 源 JSON 保证可重建。
const {chromium}=require('C:/Users/13896/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
const dir='D:/work/sportmate/docs/hardware/system-layout-20261009/';
const wpDir='D:/work/sportmate/docs/hardware/全品类补全_20261009/';
const parts=JSON.parse(fs.readFileSync(dir+'components.json','utf8'));
const targets=parts.filter(p=>!p.photo && !/^MR/.test(p.id));
const wpFiles=fs.readdirSync(wpDir).filter(f=>f.endsWith('.json')&&!f.includes('总览'));
const wpData={};
for(const f of wpFiles){const d=JSON.parse(fs.readFileSync(wpDir+f,'utf8'));wpData[f]=d;}
(async()=>{
const b=await chromium.launch({headless:true,executablePath:'C:/Users/13896/AppData/Local/ms-playwright/chromium-1234/chrome-win64/chrome.exe'});
const ctx=await b.newContext({userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',viewport:{width:1280,height:900},locale:'zh-CN'});
const log={};let ok=0,fail=0;
for(const p of targets){
 const rec={url:p.url,status:''};
 try{
  const page=await ctx.newPage();
  await page.goto(p.url,{timeout:22000,waitUntil:'domcontentloaded'});
  await page.waitForTimeout(1800);
  let img=await page.evaluate(()=>{
    const m=document.querySelector('meta[property="og:image"],meta[name="twitter:image"],meta[itemprop="image"]');
    if(m&&m.content&&/^https?:/.test(m.content))return m.content;
    const bad=/(logo|icon|sprite|placeholder|noimg|no-image|banner|avatar|default|loading)/i;
    const imgs=[...document.querySelectorAll('img')].map(i=>({src:i.currentSrc||i.src,w:i.naturalWidth,h:i.naturalHeight}))
      .filter(i=>i.src&&/^https?:/.test(i.src)&&!bad.test(i.src)&&i.w>=180&&i.h>=140);
    imgs.sort((a,c)=>c.w*c.h-a.w*a.h);
    return imgs[0]?imgs[0].src:null;});
  if(img){
    img=new URL(img,p.url).href;
    const resp=await ctx.request.get(img,{headers:{Referer:p.url}});
    const ct=(resp.headers()['content-type']||'').toLowerCase();
    const buf=await resp.body();
    if(ct.startsWith('image/')&&buf.length>3000){
      const ext=ct.includes('png')?'png':ct.includes('webp')?'webp':ct.includes('gif')?'gif':'jpg';
      fs.writeFileSync(dir+'assets/'+p.id+'.'+ext,buf);
      p.photo='assets/'+p.id+'.'+ext;
      p.photo_note='型号页主图（浏览器补抓 2026-10-09）；来源页与型号对应关系待逐项复核';
      rec.status='OK '+ext+' '+buf.length+'B '+img.slice(0,90);ok++;
    } else rec.status='BAD ct='+ct+' len='+(buf?buf.length:0)+' img='+img.slice(0,90);
  } else rec.status='NOIMG';
  await page.close();
 }catch(e){rec.status='ERR '+String(e.message||e).slice(0,140);}
 log[p.id]=rec;process.stdout.write(p.id+' '+rec.status.slice(0,80)+'\n');
 // 同步回 WP 源 JSON
 for(const f of wpFiles){
   const d=wpData[f];const items=Array.isArray(d)?d:d.items;
   const r=items.find(x=>x.id===p.id);
   if(r){r.photo=p.photo;r.photo_note=p.photo_note;}
 }
}
fs.writeFileSync(dir+'download_missing.log.json',JSON.stringify(log,null,1));
fs.writeFileSync(dir+'components.json',JSON.stringify(parts,null,1));
for(const f of wpFiles)fs.writeFileSync(wpDir+f,JSON.stringify(wpData[f],null,1));
console.log('DONE ok='+ok+' fail='+fail+' total='+targets.length);
await b.close();})().catch(e=>{console.error(e);process.exit(1)});

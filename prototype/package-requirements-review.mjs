import fs from 'node:fs';
import path from 'node:path';
const root=path.resolve('prototype'),entry=path.join(root,'requirements-review-workbench.html');
const model=JSON.parse(fs.readFileSync(path.join(root,'requirements-review-model.json'),'utf8'));
const documents={};
const mime=p=>({'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.js':'text/javascript','.css':'text/css','.woff2':'font/woff2'}[path.extname(p).toLowerCase()]||'application/octet-stream');
function asset(p){return 'data:'+mime(p)+';base64,'+fs.readFileSync(p).toString('base64');}
function inline(html,p){
  return html.replace(/\b(src|href)=(['"])([^'"]+)\2/g,(all,attr,q,url)=>{
    if(/^(?:https?:|data:|#|mailto:|javascript:)/i.test(url))return all;
    const target=path.resolve(path.dirname(p),decodeURI(url.split('#')[0]));
    if(!fs.existsSync(target)||fs.statSync(target).isDirectory())return all;
    if(attr==='href'&&!/\.(css|woff2?)$/i.test(target))return all;
    if(target.endsWith('.css')){
      let css=fs.readFileSync(target,'utf8').replace(/url\((['"]?)([^)'"\s]+)\1\)/g,(m,q,u)=>{
        if(/^(data:|https?:)/.test(u))return m;
        const a=path.resolve(path.dirname(target),u);return fs.existsSync(a)?'url("'+asset(a)+'")':m;
      });
      return attr+'='+q+'data:text/css;base64,'+Buffer.from(css).toString('base64')+q;
    }
    return attr+'='+q+asset(target)+q;
  });
}
for(const relative of [...Object.values(model.files),'prototype/state-design-lab-prototype.html','prototype/Teamo设备端UE_状态机与思维导图.html','AI运动伙伴/小程序MVP_V0.1/预览_小程序MVP.html']){
  const p=path.resolve(relative);if(!fs.existsSync(p))throw Error('Missing '+p);
  documents[p.replaceAll('\\','/')]= {name:path.basename(p),html:p.endsWith('.html'),content:p.endsWith('.html')?inline(fs.readFileSync(p,'utf8'),p):fs.readFileSync(p,'utf8')};
}
let html=fs.readFileSync(entry,'utf8');
const runtime=`<script>
(()=>{
const embedded=${JSON.stringify(documents).replace(/</g,'\\u003c')};
const base=${JSON.stringify('file:///'+entry.replaceAll('\\','/'))};
const dialog=document.createElement('dialog');dialog.style.cssText='width:94vw;height:92vh;padding:16px;background:Canvas;color:CanvasText;border:1px solid GrayText';
dialog.innerHTML='<button type="button">关闭，返回工作台</button><strong style="margin-left:16px"></strong><iframe style="display:block;width:100%;height:calc(100% - 48px);border:0;margin-top:12px" sandbox="allow-scripts allow-same-origin allow-forms allow-downloads"></iframe>';
document.body.append(dialog);dialog.querySelector('button').onclick=()=>dialog.close();
document.addEventListener('click',e=>{
 const a=e.target.closest('a[href]');if(!a)return;
 const u=new URL(a.getAttribute('href'),base);if(u.protocol!=='file:')return;
 const key=decodeURIComponent(u.pathname).replace(/^\\/([A-Za-z]:)/,'$1');const doc=embedded[key];if(!doc)return;
 e.preventDefault();dialog.querySelector('strong').textContent=doc.name;
 const safe=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
 dialog.querySelector('iframe').srcdoc=doc.html?doc.content:'<!doctype html><meta charset="utf-8"><style>:root{color-scheme:light dark}body{background:Canvas;color:CanvasText;font:16px/1.7 system-ui;padding:24px}pre{white-space:pre-wrap;overflow-wrap:anywhere}</style><pre>'+safe(doc.content)+'</pre>';
 dialog.showModal();
});
})();
</script>`;
html=html.replace('</body>',runtime+'</body>');
const out=path.join(root,'运动伙伴需求评审工作台_单文件.html');fs.writeFileSync(out,html);
console.log(JSON.stringify({output:out,embeddedDocuments:Object.keys(documents).length,bytes:fs.statSync(out).size}));

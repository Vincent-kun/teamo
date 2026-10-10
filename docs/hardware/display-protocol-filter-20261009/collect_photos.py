from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import urllib.request,re,json
root=Path(__file__).resolve().parent
pool=json.loads((root/'displays.json').read_text(encoding='utf-8'))['candidates']
def fetch(p):
 out=[]
 for page in p['sources']:
  if page.endswith('.pdf'):continue
  try:
   raw=urllib.request.urlopen(urllib.request.Request(page,headers={'User-Agent':'Mozilla/5.0'}),timeout=15).read().decode('utf-8','replace')
   (root/(p['id']+'-page.html.source')).write_text(raw,encoding='utf-8')
   urls=list(dict.fromkeys(urljoin(page,u.replace('&amp;','&')) for u in re.findall(r'(?:src|href|content)=["\']([^"\']+\.(?:jpg|png|webp)(?:\?[^"\']*)?)["\']',raw,re.I)))
   out.append(dict(page=page,images=[u for u in urls if not any(s in u.lower() for s in ['logo','icon','qr-code','pay','flags','avatar'])]))
  except Exception as exc:out.append(dict(page=page,error=str(exc)))
 return dict(id=p['id'],model=p['model'],pages=out)
res=list(ThreadPoolExecutor(max_workers=8).map(fetch,pool))
(root/'photo-inventory.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
for r in res:
 images=[u for p in r['pages'] for u in p.get('images',[])]
 main=[u for u in images if '/media/catalog/product/' in u or '-1.' in u.lower() or '_entity' in u.lower() or '970x728' in u]
 print(r['id'],json.dumps(main[:5],ensure_ascii=False),'; errors',sum('error' in p for p in r['pages']))

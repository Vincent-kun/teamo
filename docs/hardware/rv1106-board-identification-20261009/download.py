from pathlib import Path
import json, urllib.request, hashlib
from concurrent.futures import ThreadPoolExecutor
root=Path(__file__).resolve().parent
inventory=json.loads((root/'page-image-inventory.json').read_text(encoding='utf-8'))
jobs=[]
for p in inventory:
 urls=p.get('images',[])
 for role,match in [('front',lambda u:'-1-1600x1200' in u),('back',lambda u:'-2-1600x1200' in u),('drawing',lambda u:'details-size.' in u)]:
  found=next((u for u in urls if match(u)),None)
  if found:jobs.append((p['name']+'-'+role+'.jpg',found,p['page'],role))
 for key in ['Luckfox-Pico-Pro-1_93.jpg','Luckfox-Pico-Pro-M-1_93.jpg','Luckfox-Pico-Max-M-1_93.jpg','Luckfox-Pico-Ultra-W-3_93.jpg']:
  u=next((u for u in urls if u.endswith(key)),None)
  if u:jobs.append((key,u,p['page'],'variant-thumbnail'))
jobs.extend([
 ('lubancat-core.jpg','https://data.embedfire.com/2026/06/%E9%B2%81%E7%8F%AD%E7%8C%ABRV06%E6%A0%B8%E5%BF%83%E6%9D%BF.jpg','https://embedfire.com/products-3/','factory-photo'),
 ('lubancat-board.jpg','https://data.embedfire.com/2026/06/%E9%B2%81%E7%8F%AD%E7%8C%ABRV06%E6%95%B4%E6%9D%BF.jpg','https://embedfire.com/products-3/','factory-photo'),
 ('firefly-ct36l.png','https://community.t-firefly.com/wiki-api/assets/objects/08a683b699518f8df26e2eeb5fae1f4d5b800907c570acb2d1219bc76c77b154/CT36L.png','https://community.t-firefly.com/','factory-photo')])
def get(job):
 name,url,page,role=job
 try:
  blob=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':page}),timeout=20).read()
  if blob[:15].lower().startswith(b'<!doctype'):raise ValueError('HTML instead of image')
  (root/'assets'/name).write_bytes(blob)
  return dict(file=name,source_url=url,page=page,role=role,date='2026-10-09',sha256=hashlib.sha256(blob).hexdigest(),bytes=len(blob),status='ok')
 except Exception as e:return dict(file=name,source_url=url,page=page,role=role,status='failed',error=str(e))
res=list(ThreadPoolExecutor(max_workers=6).map(get,jobs))
(root/'image-sources.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
for x in res:print(x['file'],x['status'],x.get('error',''))

from pathlib import Path
from urllib.request import Request,urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin,urlparse
from concurrent.futures import ThreadPoolExecutor
import json,hashlib
root=Path(__file__).resolve().parent;rows=json.loads((root/'batteries.json').read_text(encoding='utf-8'))
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['src','href','content'] and v and any(x in v.lower() for x in ['.jpg','.webp','.png']):self.urls.append(v)
def get(u):return urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
def process(r):
 if '.pdf' in r['url']:return r
 try:
  data=get(r['url']);(root/(r['id']+'-source.html')).write_bytes(data);p=Parser();p.feed(data.decode('utf-8','replace'));urls=list(dict.fromkeys(urljoin(r['url'],u) for u in p.urls));r['observed_images']=urls
  sku=r['model'].split('#')[-1].split(' /')[0] if 'Adafruit' in r['model'] else None
  choices=[u for u in urls if (sku and f'/{sku}-' in u and '/970x728/' in u) or (not sku and 'p28a' in u.lower() and not 'logo' in u.lower())]
  for u in choices[:3]:
   try:
    raw=get(u);f=root/'assets'/(r['id']+Path(urlparse(u).path).suffix);f.write_bytes(raw);r.update(photo='assets/'+f.name,photo_note='厂家型号页原始产品图',image_source={'source_url':u,'product_page':r['url'],'sha256':hashlib.sha256(raw).hexdigest()});break
   except Exception:pass
 except Exception as e:r['image_error']=str(e)
 print(r['id'],bool(r['photo']),flush=True);return r
with ThreadPoolExecutor(max_workers=6) as ex:rows=list(ex.map(process,rows))
(root/'batteries.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')

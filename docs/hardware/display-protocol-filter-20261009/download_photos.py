from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urljoin,urlparse
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import json,hashlib
root=Path(__file__).resolve().parent
inventory=json.loads((root/'photo-inventory.json').read_text(encoding='utf-8'))
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  for k in ['src','href','content']:
   u=a.get(k,'')
   if any(x in u.lower() for x in ['.jpg','.png','.webp']) and not u.startswith('data:'):self.urls.append(u)
def fetch(u):
 return urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
retry={'WS01':'https://www.waveshare.com/wiki/Pico-LCD-1.3','WS02':'https://www.waveshare.com/product/1.28inch-lcd-module.htm','WS04':'https://www.waveshare.com/wiki/1.3inch_LCD_Module','WS09':'https://www.waveshare.com/wiki/1.8inch_LCD_Module','WS16':'https://www.waveshare.com/wiki/3.5inch_Capacitive_Touch_LCD'}
def refresh(r):
 if r['id'] not in retry:return r
 u=retry[r['id']]
 try:
  s=fetch(u).decode('utf-8','replace');p=Parser();p.feed(s)
  r['parsed_images']=list(dict.fromkeys(urljoin(u,v) for v in p.urls));r['pages']=[{'page':u,'images':r['parsed_images']}]
 except Exception as e:r['retry_error']=str(e)
 return r
with ThreadPoolExecutor(max_workers=6) as ex:inventory=list(ex.map(refresh,inventory))
(root/'photo-inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
keys={'WS01':'Pico-LCD-1.3','WS02':'1.28inch-lcd-module-1','WS03':'1.28inch-touch-lcd-1','WS04':'1.3inch-LCD-Module','WS05':'1.54inch-LCD-Module-1','WS06':'1.54-product1','WS07':'1.69inch_LCD_Module','WS08':'1.69inch-touch-lcd-module-1','WS09':'1.8inch-LCD-Module','WS10':'1.83inch_LCD_Module','WS11':'1.83-product1','WS12':'2inch-lcd-module-1','WS13':'2inch-capacitive-touch-lcd-1','WS14':'2.4inch-lcd-module-1','WS15':'2.8inch-capacitive-touch-lcd-1','WS16':'3.5inch-capacitive-touch-lcd-1','EX01':'Circular-smart-watch-TFT','EX02':'1.85-introduce','EX03':'ESP32-S3-Touch-LCD-1.85-1-','EX04':'LF40-480480-ARK-details-1','EX05':'LF40-720720-ARK-details-1','EX06':'1.46inch-touch-lcd-module-1','EX11':'4421-00'}
assets=root/'assets';assets.mkdir(exist_ok=True)
def download(r):
 ident=r['id'];key=keys.get(ident)
 urls=list(dict.fromkeys(r.get('parsed_images',[])+[u for p in r['pages'] for u in p.get('images',[])]))
 if ident=='WS03':urls+=next(x for x in inventory if x['id']=='WS02').get('parsed_images',[])
 matches=[u for u in urls if key and key.lower() in u.lower() and '/File:' not in u and '/thumbnail/' not in u and not any(x in u.lower() for x in ['drawing','size','connect','pinout'])]
 matches.sort(key=lambda u:('/image/800x800/' not in u,'1200px' not in u,'300px' in u))
 out={'id':ident,'model':r['model'],'status':'未取得精确型号产品图'}
 for u in matches:
  try:
   data=fetch(u);suffix=Path(urlparse(u).path).suffix.lower();f=assets/(ident+suffix);f.write_bytes(data)
   out.update(status='厂家产品图',file='assets/'+f.name,url=u,page=next((p['page'] for p in r['pages'] if u in p.get('images',[])),r['pages'][-1]['page']),sha256=hashlib.sha256(data).hexdigest(),caption='厂家型号页产品图；点击查看原图')
   if ident=='WS10':out.update(status='型号页版本待核',caption='厂家1.83型号页图；图片未证明Rev2版本，待核')
   break
  except Exception as e:out['error']=str(e)
 print(ident,out['status'],flush=True);return out
with ThreadPoolExecutor(max_workers=8) as ex:manifest=list(ex.map(download,inventory))
(root/'photo-sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

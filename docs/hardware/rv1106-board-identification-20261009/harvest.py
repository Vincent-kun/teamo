from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, re, json, hashlib
from urllib.parse import urljoin
root=Path(__file__).resolve().parent
(root/'assets').mkdir(exist_ok=True)
pages={'pro-max':'https://www.luckfox.com/EN-Luckfox-Pico-Pro','ultra':'https://www.luckfox.com/EN-Luckfox-Pico-Ultra','core':'https://www.luckfox.com/Core1106','pi':'https://www.luckfox.com/luckfox-pico-pi','zero':'https://www.luckfox.com/luckfox-pico-zero','86':'https://www.luckfox.com/Luckfox-Pico-86-Panel'}
def fetch(pair):
 name,url=pair
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
  (root/(name+'.html.source')).write_bytes(raw)
  s=raw.decode('utf-8','replace')
  images=list(dict.fromkeys(urljoin(url,x.replace('&amp;','&')) for x in re.findall(r'(?:src|href)=["\']([^"\']+\.(?:jpg|png|webp)(?:\?[^"\']*)?)["\']',s,re.I)))
  relevant=[x for x in images if '/development-board/' in x or '/Core1106' in x]
  return dict(name=name,page=url,images=relevant,status='ok',sha256=hashlib.sha256(raw).hexdigest())
 except Exception as e: return dict(name=name,page=url,status='failed',error=str(e))
res=list(ThreadPoolExecutor(max_workers=6).map(fetch,pages.items()))
(root/'page-image-inventory.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
for x in res:print(x['name'],json.dumps(x.get('images',x.get('error')),ensure_ascii=False))

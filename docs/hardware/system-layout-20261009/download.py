from pathlib import Path
from urllib.request import urlopen,Request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import json,hashlib
root=Path(__file__).resolve().parent;data=json.loads((root/'components.json').read_text(encoding='utf-8'))
def get(r):
 if not r.get('photo_url'):return r
 try:
  raw=urlopen(Request(r['photo_url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read();ext=Path(urlparse(r['photo_url']).path).suffix.lower();ext=ext if ext in ['.png','.jpg','.webp'] else '.png';f=root/'assets'/(r['id']+ext);f.write_bytes(raw);r['photo']='assets/'+f.name;r['photo_sha256']=hashlib.sha256(raw).hexdigest()
 except Exception as e:r['photo_error']=str(e)
 print(r['id'],bool(r.get('photo')),flush=True);return r
with ThreadPoolExecutor(max_workers=8) as ex:data=list(ex.map(get,data))
(root/'components.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')

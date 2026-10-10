from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
import json
root=Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  for k in ['src','href','content']:
   u=a.get(k,'')
   if any(x in u.lower() for x in ['.jpg','.png','.webp']) and not u.startswith('data:'):self.urls.append(u)
inventory=json.loads((root/'photo-inventory.json').read_text(encoding='utf-8'))
for r in inventory:
 f=root/(r['id']+'-page.html.source')
 if not f.exists():continue
 parser=Parser();parser.feed(f.read_text(encoding='utf-8'))
 page=next((p['page'] for p in reversed(r['pages']) if 'images' in p),r['pages'][0]['page'])
 urls=list(dict.fromkeys(urljoin(page,u) for u in parser.urls))
 r['parsed_images']=[u for u in urls if '/wiki/File:' not in u and not any(x in u.lower() for x in ['logo','social-card','icon','avatar'])]
 if r['id'] in ['WS01','WS06','WS11','EX02','EX03']:print(r['id'],json.dumps(r['parsed_images'][:8],ensure_ascii=False))
(root/'photo-inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')

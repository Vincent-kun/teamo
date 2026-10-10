"""归档已核实厂家图片，不改图片；保留来源、SHA256及下载失败记录。"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import hashlib
import json
import shutil

root = Path(__file__).resolve().parent
assets = root / 'assets'
assets.mkdir(exist_ok=True)
items = {
 'core.jpg': ('https://www.luckfox.com/image/cache/catalog/development-board/Core11061408/Core11061408/Core11061408-1-1600x1200.jpg','https://www.luckfox.com/Core1106','Core11061408官方产品图'),
 'max.jpg': ('https://www.luckfox.com/image/cache/catalog/development-board/Luckfox-Pico-Pro/Luckfox-Pico-Max-1-1600x1200.jpg','https://www.luckfox.com/EN-Luckfox-Pico-Pro','Pico Max无预焊排针图'),
 'ultra.jpg': ('https://www.luckfox.com/image/cache/catalog/development-board/Luckfox-Pico-Ultra/Luckfox-Pico-Ultra-1-1600x1200.jpg','https://www.luckfox.com/EN-Luckfox-Pico-Ultra','Ultra系列产品图，不能单凭图确认W配置'),
 'camera.jpg': ('https://www.luckfox.com/image/cache/catalog/accBoard/MIS5001-5MP-Camera-B/MIS5001-5MP-Camera-B-1-1600x1200.jpg','https://www.luckfox.com/MIS5001-5MP-Camera-B','MIS5001(B)官方产品图'),
 'square.jpg': ('https://www.waveshare.com/media/catalog/product/cache/1/image/800x800/9df78eab33525d08d6e5fb8d27136e95/1/_/1.69inch-lcd-module-1.jpg','https://www.waveshare.com/product/displays/1.69inch-lcd-module.htm','1.69inch LCD Module官方产品图'),
 'round.webp': ('https://www.nosedisplay.com/wp-content/uploads/2025/08/Circular-smart-watch-TFT-LCD-screen-FPC-flexible-cable.webp','https://www.nosedisplay.com/products/tft-display-1-8-inch-round-display-ips-360x360-resolution-qspi-4-line/','ND018TCM360360-A01型号页产品图'),
 'esp32.jpg': ('https://www.waveshare.com/w/upload/5/5f/ESP32-S3-Touch-LCD-1.85_Entity.jpg','https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-1.85','ESP32-S3-Touch-LCD-1.85官方产品图'),
}

def download(item):
 name,(url,page,label)=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':page})
  blob=urllib.request.urlopen(req,timeout=25).read()
  if blob[:15].lower().startswith(b'<!doctype html'): raise ValueError('Expected image, got HTML')
  (assets/name).write_bytes(blob)
  return {'file':name,'source_url':url,'product_page':page,'caption':label,'date':'2026-10-08','sha256':hashlib.sha256(blob).hexdigest(),'bytes':len(blob),'status':'downloaded'}
 except Exception as exc:
  return {'file':name,'source_url':url,'product_page':page,'status':'failed','error':str(exc)}

manifest=list(ThreadPoolExecutor(max_workers=5).map(download,items.items()))
evidence=root.parents[2]/'AI运动伙伴'/'00_现行研究与规范_20260918'/'硬件筛选证据_20261008'
for name in ['Core1106-size.jpg','Pico-Pro-size.jpg','Pico-Ultra-size.jpg','MIS5001-B-size.jpg','LCD169-Touch-drawing.png','LP503450-850mAh.png']:
 src=evidence/name
 shutil.copy2(src,assets/name)
 manifest.append({'file':name,'source_local':str(src),'caption':'已归档厂家机械图/规格书渲染','status':'copied','sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
for name in ['IMG_2466.jpeg','IMG_2474.jpeg']:
 src=root.parents[1]/'research'/'bodypark-teardown'/'teardown-images'/name
 shutil.copy2(src,assets/name)
 manifest.append({'file':name,'source_local':str(src),'caption':'BodyPark实机参考，不能当新方案供应商板照片','status':'copied','sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
(root/'image-sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
for entry in manifest: print(entry['file'],entry['status'],entry.get('bytes',''),entry.get('error',''))

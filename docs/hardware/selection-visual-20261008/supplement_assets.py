from pathlib import Path
import urllib.request
import hashlib
root=Path(__file__).resolve().parent
assets=root/'assets'
def download(item):
 name,(url,page,label)=item
 try:
  blob=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':page}),timeout=25).read()
  if blob[:15].lower().startswith(b'<!doctype html'): raise ValueError('HTML instead of image')
  (assets/name).write_bytes(blob)
  return dict(file=name,source_url=url,product_page=page,caption=label,date='2026-10-08',sha256=hashlib.sha256(blob).hexdigest(),bytes=len(blob),status='downloaded')
 except Exception as exc: return dict(file=name,source_url=url,product_page=page,status='failed',error=str(exc))
from concurrent.futures import ThreadPoolExecutor
import json

items = {
 'ec800g.png': ('https://www.quectel.com.cn/wp-content/uploads/2024/05/LTE-EC800G-CN.png','https://www.quectel.com.cn/product/ec800g-cn','EC800G-CN系列厂家图，不证明具体订货后缀'),
 'air780e.png': ('https://cdn.openluat-luatcommunity.openluat.com/images/20230509102332246_Air780E%E9%9D%A2%E5%9B%BE.PNG','https://docs.openluat.com/air780e/product/','Air780E厂家产品图'),
 'ultra-w.jpg': ('https://www.luckfox.com/image/catalog/development-board/Luckfox-Pico-Ultra-W/Luckfox-Pico-Ultra-W-3_93.jpg','https://www.luckfox.com/EN-Luckfox-Pico-Ultra','Ultra W厂家型号图'),
 'screen185-drawing.webp': ('https://docs.waveshare.com/assets/images/1.85-size-1-9393d4b56161d97a2b9c7e10e446fd7b.webp','https://docs.waveshare.com/1.85inch_Touch_LCD_Module','1.85寸独立屏模组尺寸图'),
 'lf40.jpg': ('https://www.luckfox.com/image/catalog/LCD-OLED/LF40-480480-ARK/LF40-480480-ARK-details-4.jpg','https://www.luckfox.com/LF40-480480-ARK','LF40厂家型号页图'),
 'amp.jpg': ('https://cdn-shop.adafruit.com/970x728/2130-05.jpg','https://www.adafruit.com/product/2130','PAM8302产品图'),
 'speaker.jpg': ('https://cdn-shop.adafruit.com/970x728/3923-06.jpg','https://www.adafruit.com/product/3923','3923厂家产品图，线长须核当批版本'),
 'battery1200.jpg': ('https://cdn-shop.adafruit.com/970x728/258-02.jpg','https://www.adafruit.com/product/258','258电池产品图'),
 'battery2000.jpg': ('https://cdn-shop.adafruit.com/970x728/2011-05.jpg','https://www.adafruit.com/product/2011','2011电池产品图'),
 'camera-a.jpg': ('https://www.luckfox.com/image/cache/catalog/accBoard/MIS5001-5MP-Camera/MIS5001-5MP-Camera-A-1-1600x1200.jpg','https://www.luckfox.com/MIS5001-5MP-Camera-A','MIS5001 A厂家产品图'),
}
path=root/'image-sources.json'
manifest=json.loads(path.read_text(encoding='utf-8'))
results=list(ThreadPoolExecutor(max_workers=5).map(download,items.items()))
for x in results:
 local=assets/x['file']
 if x['status']=='failed' and local.is_file():
  x.update(status='previous_download_retained',sha256=hashlib.sha256(local.read_bytes()).hexdigest(),bytes=local.stat().st_size,caption=items[x['file']][2],date='2026-10-08')
manifest=[x for x in manifest if x['file'] not in items]+results
path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
for x in results: print(x['file'],x['status'],x.get('error',''))

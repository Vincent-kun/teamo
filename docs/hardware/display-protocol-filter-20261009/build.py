from pathlib import Path
import json
root=Path(__file__).resolve().parent
hardware=root.parent
pool=json.loads((hardware/'SPI显示屏市场候选池_20261009.json').read_text(encoding='utf-8'))['candidates']
for p in pool:
 p['bus']='SPI';p['grade']='A' if p['id']=='WS01' else 'B'
 p['has_touch']=p.get('has_touch',bool(p.get('touch_controller')) or 'Touch' in p['model'])
 p['stock']='国内库存/指定版本报价待确认'
 p['photo']=None
photos={'WS02':'square.jpg','WS07':'square.jpg','WS08':'LCD169-Touch-drawing.png'}
# WS02不能使用方屏图；只映射精确已有型号。
photos.pop('WS02')
for p in pool:p['photo']=photos.get(p['id'])
def add(ident,model,inch,res,bus,ic,module,shape,touch,url,notes,grade='C',photo=None,t=None,aa=None):
 pool.append(dict(id=ident,model=model,diagonal_in=inch,resolution=res,bus=bus,interface=bus,controller=ic,module_mm=module,shape=shape,has_touch=touch,touch_controller=None,aa_mm=aa,thickness_mm=t,sources=[url],notes=notes,grade=grade,stock='国内库存/指定版本报价待确认',photo=photo))
add('EX01','ND018TCM360360-A01',1.8,[360,360],'QSPI','ST77916',[48.08,49.59],'round',False,'https://www.nosedisplay.com/products/tft-display-1-8-inch-round-display-ips-360x360-resolution-qspi-4-line/','针数/电压口径冲突；QSPI主机与驱动未闭环。',photo='round.webp',t=1.96,aa=[45.68,45.68])
add('EX02','1.85inch Touch LCD Module SKU35079',1.85,[360,360],'QSPI','ST77916',[55,55],'round',True,'https://docs.waveshare.com/1.85inch_Touch_LCD_Module','独立QSPI屏板，不是ESP整板；完整T与RV驱动未知。',photo='screen185-drawing.webp',aa=[45.68,45.68])
add('EX03','ESP32-S3-Touch-LCD-1.85 无B/C后缀',1.85,[360,360],'UART/协处理器','ESP32-S3 + ST77916',[55,55],'round',True,'https://docs.waveshare.com/ESP32-S3-Touch-LCD-1.85','需指定触控版本；UART事件协议与UI工程待开发，不能当裸屏直接RV驱动。',grade='D',photo='esp32.jpg',aa=[45.68,45.68])
add('EX04','LF40-480480-ARK',4,[480,480],'RGB','待厂家指定',[84.2,84.2],'square',True,'https://www.luckfox.com/LF40-480480-ARK','Ultra/Ultra W官方支持；仅台架，尺寸超产品池。',grade='A',photo='lf40.jpg',aa=[71.86,70.18])
add('EX05','LF40-720720-ARK',4,[720,720],'RGB','待厂家指定',[84,84],'square',True,'https://www.luckfox.com/LF40-720720-ARK','Ultra/Ultra W官方支持；720与480款尺寸不同，勿复用。',grade='A',aa=[71.93,71.93])
add('EX06','1.46inch Touch LCD Module SKU34955',1.46,[412,412],'QSPI','SPD2010',[44.77,44.77],'round',True,'https://www.waveshare.com/product/displays/1.46inch-touch-lcd-module.htm','完整板框紧凑，但QSPI不是普通SPI；厂家例程ESP/Pico/STM32，不证明RV可用。',aa=[36.96,36.96])
add('EX07','TTH185BRS-01C',1.85,[360,360],'多模式待确认','ST77916',[55,55],'round',True,'https://tailorpixels.com/wp-content/uploads/2024/06/TTH185BRS-01C_1.85-inch-Round-LCD-360x360-MIPI-QSPI-SRGB-8BIT.pdf','LCM48.08×49.95×1.52；带触控外框55×55。资料列MIPI/QSPI/8BIT/SRGB，需锁IM配置、39pin与自研板驱动；不是任意接口可直接用。',aa=[45.68,45.68])
add('EX08','ER-TFT021-1-5714',2.1,[480,480],'RGB','ST7701S',None,'round',True,'https://www.buydisplay.com/chinese/catalog/product/view/id/1987/s/480x480-round-ips-tft-lcd-display-2-1-inch-capacitive-touch-circle-screen/','厂家指定3SPI初始化＋18RGB像素接口；不与ER-TFT021-2纯MIPI款混淆。完整包络/时序/交期待询。')
add('EX09','ER-TFT1.28-3 无触控版',1.28,[240,240],'SPI','待指定版本确认',[35.59,37.74],'round',False,'https://www.buydisplay.com/1-28-inch-tft-lcd-display-240x240-round-circle-screen-for-smart-watch','厂家目录/图纸可查；普通SPI模式、控制器与Pinout需锁单；触控版另计包络。',t=1.6,aa=[32.4,32.4])
add('EX10','ER-TFT021-1-5982 智能屏',2.1,[480,480],'UART/协处理器','内置MCU',None,'round',True,'https://www.buydisplay.com/2-1-inch-480x480-hmi-intelligent-smart-uart-spi-round-capacitive-touch','页面56.18×59.71×2.2未证明MCU/屏蔽罩/控制板完整包络；保留整套尺寸未知。需厂家智能屏协议/UI工具。',grade='D')
add('EX11','Adafruit #4421 1.54 TFT',1.54,[240,240],'SPI','ST7789',None,'square',False,'https://www.adafruit.com/product/4421','真实裸屏与Waveshare板不是同包络；本轮完整机械数据未核，不以照片测尺寸。',grade='B')
manifest={r['id']:r for r in json.loads((root/'photo-sources.json').read_text(encoding='utf-8'))}
for p in pool:
 r=manifest[p['id']]
 p['photo']=r.get('file');p['photo_caption']=r.get('caption',r['status']);p['photo_source']=r.get('page');p['photo_status']=r['status']
 p['other_views']=r.get('other_views',[]);p['missing_reason']=r.get('missing_reason')
 p['drawing']={'WS08':'../selection-visual-20261008/assets/LCD169-Touch-drawing.png','EX02':'../selection-visual-20261008/assets/screen185-drawing.webp'}.get(p['id'])
(root/'displays.json').write_text(json.dumps(dict(date='2026-10-09',scope='28 representative exact-model records across 6 manufacturer catalogs; not exhaustive market or confirmed stock',candidates=pool),ensure_ascii=False,indent=2),encoding='utf-8')
template=(root/'template.html').read_text(encoding='utf-8')
(root/'index.html').write_text(template.replace('__DATA__',json.dumps(pool,ensure_ascii=False).replace('<',chr(92)+'u003c')),encoding='utf-8')
print(f'Built {len(pool)} sourced screen records')
import csv
with (root/'displays.csv').open('w',encoding='utf-8-sig',newline='') as f:
 writer=csv.writer(f);writer.writerow(['ID','型号','协议','证据等级','inch','像素','模组W/H','总T','触控','控制器','来源','缺项'])
 for p in pool:writer.writerow([p['id'],p['model'],p['bus'],p['grade'],p['diagonal_in'],p['resolution'],p['module_mm'],p['thickness_mm'],p['has_touch'],p['controller'],'; '.join(p['sources']),p['notes']])
shortlist=[p for p in pool if p['bus']=='SPI' and 1.5<=p['diagonal_in']<=2.1 and min(p['resolution'])>=240 and p['module_mm'] and max(p['module_mm'])<=55]
lines=['# 默认产品初筛结果｜2026-10-09','> 满足尺寸/分辨率/协议筛选不是已兼容。实际开发板与SDK未确认；产品自研主板。','当前条件：普通SPI、1.5–2.1寸、两轴≥240px、模组两轴≤55mm、触控不强制。',f'28条池中保留{len(shortlist)}条；相同产品不同Rev分条，不夸大独立型号数量。','| 型号 | 分辨率 | 模组W×H mm | 触控 | 缺项 |','|---|---|---|---|---|']
for p in shortlist:lines.append(f'| {p["model"]} | {p["resolution"][0]}×{p["resolution"][1]} | {p["module_mm"][0]}×{p["module_mm"][1]} | {"是" if p["has_touch"] else "否"} | {p["notes"] or "指定板驱动/初始化、完整T、含税价与库存待验证"} |')
lines += ['','建议优先收敛：1.69非触控／触控，1.54触控，1.83触控。1.83非触控Rev冲突未锁前暂缓下单。最终需UE确认尺寸/触控与开发者确认驱动工时。','参考验证屏Pico-LCD-1.3只有1.3寸，虽有官方Pro/Max示例，被当前产品最小1.5寸条件排除；它仍是台架基准。','圆屏：1.28普通SPI被当前最小尺寸阈值排除，可放宽至1.28查看；1.46/1.8/1.85 QSPI保留条件分支，不列已支持。RGB的LF40两款被体积阈值排除，保留台架。','[调整筛选条件](index.html) · [全部候选CSV](displays.csv) · [协议与规则](../显示屏协议与筛选规则_20261009.md)。']
(root/'默认初筛结果_20261009.md').write_text('\n'.join(lines).replace('| 型号 |','\n| 型号 |'),encoding='utf-8')

"""将既有真实选型CSV和已核实机械参数编译为离线展示页。"""
from pathlib import Path
import csv
import json
import re

root=Path(__file__).resolve().parent
base=root.parents[2]/'AI运动伙伴'/'00_现行研究与规范_20260918'
rows=list(csv.DictReader((base/'真实硬件候选_20261008_V0.1.csv').open(encoding='utf-8-sig',newline='')))
clean=lambda s: re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',s).replace('**','').replace('`','')
# 手工机械参数均来自对应厂家资料；None表示完整尺寸没有闭环，不推测。
geometry={
 'M01':(30,30,5.50,'Core11061408','Core1106','core.jpg','Core1106-size.jpg','Core11061408厂家产品图；总厚5.50与PCB厚1.60需区分。'),
 'M02':(30,30,None,'Core11060408','Core无无线',None,'Core1106-size.jpg','Core系列机械图，仅作共用板框参考；无无线版本器件高度待确认。'),
 'M03':(21,72,None,'Luckfox Pico Max','Pico Max','max.jpg','Pico-Pro-size.jpg','Pico Max无预焊排针厂家图；RJ45/USB及插线总高待核。'),
 'M04':(50,50,None,'Luckfox Pico Ultra W','Ultra W','ultra-w.jpg','Pico-Ultra-size.jpg','Ultra W型号厂家缩略图；分辨率93px，不用于量尺寸；完整高度待核。'),
 'D01':(31.5,39,None,'1.69inch LCD Module','1.69″方屏','square.jpg',None,'非触控型号厂家产品图；照片不是正投影机械图。'),
 'D02':(33.13,41.13,None,'1.69inch Touch LCD Module','1.69″触控',None,'LCD169-Touch-drawing.png','厂家机械图：侧图7和连接器局部突出2.5；整体T/公差/插线空间待核。'),
 'D03':(48.08,49.59,1.96,'ND018TCM360360-A01','1.8″裸圆屏','round.webp',None,'对应型号页厂家图；显示图案仅为厂家示例，FPC/针数/电压仍需确认。'),
 'D04':(55,55,None,'1.85inch Touch LCD Module','1.85″屏模组',None,'screen185-drawing.webp','厂家尺寸图：55×55；侧图9.10及局部4.00须结合连接器与线缆核总包络，不强行当完整T。'),
 'D05':(55,55,None,'ESP32-S3-Touch-LCD-1.85','ESP32圆屏','esp32.jpg',None,'无B/C后缀型号厂家图；触控配置和整板厚度须订货时确认。'),
 'D06':(84.2,84.2,None,'LF40-480480-ARK','4″台架屏','lf40.jpg',None,'厂家型号页触控演示图；不是实测板框。'),
 'C01':(25,24,None,'MIS5001 5MP Camera (B)','5MP相机B','camera.jpg','MIS5001-B-size.jpg','厂家B镜头图；前侧16.60不是完整厚度，整体T仍需核图/实测。'),
 'C02':(None,None,None,'MIS5001 5MP Camera (A)','5MP相机A','camera-a.jpg',None,'厂家A镜头产品图；不套用B型镜头高度。'),
 'N01':(17.7,15.8,2.4,'EC800G-CN / LD-I03-SNNDA2','EC800G','ec800g.png',None,'EC800G-CN系列厂家产品图，不证明具体订货后缀或固件。'),
 'N02':(17.7,15.8,2.3,'Air780E','Air780E','air780e.png',None,'Air780E厂家产品图；尺寸按产品页，介绍页不同口径仍需厂家闭环。'),
 'B01':(34,50,5,'LP503450 / 850mAh / PCM','850mAh电池',None,'LP503450-850mAh.png','厂家规格书渲染；34±0.5、50±1、5±0.3，另计引线/膨胀/支架；非高倍率电池。'),
 'B02':(None,None,None,'Adafruit #258 / 1200mAh','1200mAh参考','battery1200.jpg',None,'厂家产品图；网页尺寸口径冲突，待确认。'),
 'B03':(36,60,7,'Adafruit #2011 / 2000mAh','2000mAh参考','battery2000.jpg',None,'厂家产品图；本图不代表当前库存或国内供应商交期。'),
 'A01':(15,24,2,'Adafruit #2130 / PAM8302','模拟功放','amp.jpg',None,'厂家产品图；2mm不含排针及插线。'),
 'A02':(30,20,5,'Adafruit #3923 / 8Ω 1W','扬声器','speaker.jpg',None,'厂家产品图；线长以当批版本确认，照片不证明线缆包络。'),
}
data=[]
for row in rows:
 ident=row['候选ID'];w,h,t,short,label,photo,evidence,note=geometry[ident]
 data.append(dict(id=ident,category=row['类别'],short=short,label=label,w=w,h=h,t=t,photo=photo,evidence=evidence,imageNote=note,
                  dimensions=clean(row['尺寸与规格']),technical=clean(row['接口与配置']),price=clean(row['页面价格与库存']),
                  result=clean(row['筛选结论']),sources=row['官方来源URL'].split('; ')))
data.append(dict(id='M00',category='主控',short='BodyPark同芯片 / RV1106B待定',label='RV1106B路线',w=None,h=None,t=None,
                photo='IMG_2466.jpeg',evidence='IMG_2474.jpeg',imageNote='仓库BodyPark实机/拆解照片，只作竞品参考；不是我方供应商整板。',
                dimensions='拆解架构图记录U1000为RV1106B。具体供应商板型、RAM/存储、机械外形待今晚确认。',
                technical='沿用芯片不等于获得原机SDK、驱动或可采购板；团队经验未知。',price='指定方案正式报价、合作供应商、交期未知。',
                result='待技术负责人确认',sources=[]))
for p in data:
 for kind in ('photo','evidence'):
  if p[kind] and not (root/'assets'/p[kind]).is_file():raise FileNotFoundError(p[kind])
payload=json.dumps(data,ensure_ascii=False).replace('<',chr(92)+'u003c')
template=(root/'template.html').read_text(encoding='utf-8')
assert template.count('__DATA__')==1
legacy=template.replace('__DATA__',payload)
(root/'layout-reference.html').write_text(legacy,encoding='utf-8')
if (root.parent/'system-layout-20261009/index.html').exists():
 (root/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=../system-layout-20261009/index.html"><title>硬件候选工作台</title><p>硬件候选总览已扩展，<a href="../system-layout-20261009/index.html">打开全品类候选与排布</a>。</p><p><a href="layout-reference.html">早期布局参考</a></p></html>',encoding='utf-8')
else:(root/'index.html').write_text(legacy,encoding='utf-8')
(root/'candidates.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Built {len(rows)} candidates + BodyPark pending route; {sum(bool(p["photo"]) for p in data)} product/reference images')

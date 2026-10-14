import json
from pathlib import Path

root=Path(__file__).parent
rows=[]
def add(id,model,inch,res,ic,tp,aa,mod,shape,url,notes='',status='协议候选；RV1106适配待验证'):
    rows.append(dict(id=id,model=model,diagonal_in=inch,resolution=res,controller=ic,touch_controller=tp,interface='4-wire SPI'+(' + I2C touch' if tp else ''),aa_mm=aa,module_mm=mod,thickness_mm=None,shape=shape,sources=[url],notes=notes,compatibility=status))
add('WS01','Pico-LCD-1.3',1.3,[240,240],'ST7789VW',None,[23.4,23.4],[26.5,52],'square','https://www.waveshare.net/wiki/Pico-LCD-1.3','带按键/摇杆的开发附件，不能用其尺寸反推产品裸屏；Luckfox Pro/Max官方LVGL示例引用此型号。','官方平台示例引用；具体采购板版本仍需确认')
rows[-1]['sources'].append('https://wiki.luckfox.com/Luckfox-Pico-Plus-Mini/Luckfox-Pico-LVGL/')
add('WS02','1.28inch LCD Module',1.28,[240,240],'GC9A01',None,[32.4,32.4],[40.4,37.5],'round','https://www.waveshare.com/product/1.28inch-touch-lcd.htm','AA为直径32.4；板体直径37.5，完整包络40.4×37.5含凸出。')
add('WS03','1.28inch Touch LCD',1.28,[240,240],'GC9A01','CST816S',[32.4,32.4],[39.89,38.5],'round','https://www.waveshare.com/product/1.28inch-touch-lcd.htm','AA为直径32.4；板体直径38.5，完整包络39.89×38.5。')
add('WS04','1.3inch LCD Module',1.3,[240,240],'ST7789',None,[23.4,23.4],[45,31],'square','https://www.waveshare.com/catalog/product/view/id/3637/s/1.3inch-lcd-module/category/356/')
add('WS05','1.54inch LCD Module',1.54,[240,240],'ST7789',None,[27.72,27.72],[50,35],'square','https://www.waveshare.com/wiki/1.54inch_LCD_Module')
add('WS06','1.54inch Touch LCD Module',1.54,[240,240],'ST7789S','CST816D',[27.72,27.72],[40.2,40.2],'square','https://docs.waveshare.com/1.54inch_Touch_LCD_Module','新文档CST816D；ESP32驱动板汇总表写CST816S，采购前锁BOM。')
add('WS07','1.69inch LCD Module',1.69,[240,280],'ST7789V2',None,[27.972,32.634],[31.5,39],'rounded-rectangle','https://www.waveshare.com/wiki/1.69inch_LCD_Module')
add('WS08','1.69inch Touch LCD Module',1.69,[240,280],'ST7789V2','unconfirmed',[27.972,32.634],[33.13,41.13],'rounded-rectangle','https://www.waveshare.com/product/1.69inch-touch-lcd-module.htm','商品页CST816T；旧wikiCST816S，触控IC字段null表示待核不是无触控。不是完整圆形，标题中的Round不可据此画圆。')
rows[-1]['touch_controller']=None
rows[-1]['has_touch']=True
rows[-1]['sources'].append('https://www.waveshare.com/wiki/1.69inch_Touch_LCD_Module')
add('WS09','1.8inch LCD Module',1.8,[128,160],'ST7735S',None,[28.3,34.5],[56.5,34],'rectangle','https://www.waveshare.com/catalog/product/view/id/5540/s/1.69inch-lcd-module/category/356/','仅128×160，分辨率偏低；该来源官方选型表。')
add('WS10','1.83inch LCD Module Rev2',1.83,[240,284],None,None,[29.52,34.93],[33,40],'rounded-rectangle','https://www.waveshare.com/wiki/1.83inch_LCD_Module','Wiki Rev2写ST7789P，商品页仍写ST7789B，IC待核；Rev1例程不兼容。')
rows[-1]['sources'].append('https://www.waveshare.com/product/raspberry-pi/displays/1.83inch-lcd-module.htm')
add('WS11','1.83inch Touch LCD Module',1.83,[240,284],'ST7789P','CST816D',[29.52,34.93],[35,42],'rounded-rectangle','https://docs.waveshare.com/1.83inch_Touch_LCD_Module')
add('WS12','2inch LCD Module',2,[240,320],'ST7789VW',None,[30.6,40.8],[58,35],'rectangle','https://www.waveshare.com/product/displays/lcd-oled/2inch-lcd-module.htm')
add('WS13','2inch Capacitive Touch LCD',2,[240,320],'ST7789T3','CST816D',[30.6,40.8],[37.1,58.8],'rectangle','https://www.waveshare.com/product/displays/lcd-oled/lcd-oled-3/2inch-capacitive-touch-lcd.htm','ESP32驱动板汇总表CST816S，产品标题CST816D，采购确认当批版本。')
add('WS14','2.4inch LCD Module',2.4,[240,320],'ILI9341',None,[36.72,48.96],[70.5,43.3],'rectangle','https://www.waveshare.com/product/2.4inch-lcd-module.htm')
add('WS15','2.8inch Capacitive Touch LCD',2.8,[240,320],'ST7789T3','CST328',[43.2,57.6],[50.54,73.06],'rectangle','https://www.waveshare.com/catalog/product/view/id/6414/s/2.8inch-capacitive-touch-lcd/category/346/')
add('WS16','3.5inch Capacitive Touch LCD',3.5,[320,480],'ST7796S','FT6336U',[48.96,73.44],[61,92.44],'rectangle','https://www.waveshare.com/product/3.5inch-capacitive-touch-lcd.htm')
add('WS17','1.83inch LCD Module Rev1',1.83,[240,280],'NV3030B',None,[30.197,35.230],[33,40],'rounded-rectangle','https://www.waveshare.com/wiki/1.83inch_LCD_Module','历史Rev1；不把当前在售Rev2的报价/供货套用到本型号，先确认库存版本。')
for r in rows:r.setdefault('has_touch',r['touch_controller'] is not None)
payload=dict(verified_on='2026-10-09',scope='Waveshare代表性4线SPI彩色LCD，非全市场穷尽；不含所有HAT和OLED',candidates=rows)
(root/'SPI显示屏市场候选池_20261009.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# SPI显示屏市场候选池 · 2026-10-09','', '> 自研产品主板；开发板只用于SDK与接口验证。以下17项是官方可查的代表性型号，不等于全市场，也不等于RV1106已经适配。模组尺寸为厂家二维外廓，厚度全部待机械图确认。','', '## 候选表','', '| ID / 型号 | 分辨率 / 显示IC | 触控IC | 显示AA mm | 模组二维尺寸 mm | 官方来源 |','|---|---|---|---|---|---|']
for r in rows:
    md.append(f"| {r['id']} {r['model']} | {'×'.join(map(str,r['resolution']))} / {r['controller'] or 'IC待核'} | {r['touch_controller'] or ('待核' if r['has_touch'] else '无')} | {'×'.join(map(str,r['aa_mm']))}{'（圆屏直径）' if r['shape']=='round' else ''} | {'×'.join(map(str,r['module_mm']))} | [厂家]({r['sources'][0]}) |")
md += ['','## 筛选与验证条件','', '1. 首先以实际采购板的SPI pinmux、可用GPIO、供电/逻辑电压、内核spidev或显示驱动与LVGL接入作为门槛。树莓派或ESP32示例不构成RV1106已兼容证据。','2. 常规SPI与显示QSPI分开；不能因为SPI Flash支持四线就认定LCD QSPI可驱动。1.46/1.85圆屏QSPI应另列待验证池。','3. 对完整模组按短边作宽度、长边作高度初筛。旋转只能改变安装方向，不能让长边消失；还要为摄像头、插头、排线折弯留空间。55mm仅为待讨论预算，不能当冻结产品尺寸。','4. 角色表情候选先看240×240及以上、可视角、实际亮度与背光功耗；淘汰ST7735S低分辨率或过大模组是产品条件，不是通信不支持。','5. 每款锁定当批驱动IC、初始化、偏移、色序、触控IC与排线引脚；实测相机算法运行时的刷新速度、CPU负载、温升和供电峰值。','6. 价格、供货、合作供应商、SDK熟悉度均需RFQ/团队答复，没有自动合格的低价方案。','', '## 型号版本与差异','']
for r in rows:
    if r['notes']:md += [f"- **{r['model']}**：{r['notes']}"]
md += ['', '## 用于讨论的优先顺序','', '- 台架基准：Pico-LCD-1.3，Luckfox Pro/Max官方LVGL资料引用；不等于涛哥采购板已确认。','- 紧凑方屏：1.69非触控/触控、1.83非触控/触控。','- 较大可视区域：2inch非触控/触控；完整模组高度约58mm，需要重新排摄像头。','- 普通SPI圆屏：1.28非触控/触控，AA直径仅32.4mm；可做验证，不代表满足1.8寸角色显示体验。','- 2.4/2.8/3.5保留在池中，按机身空间和外观需求筛掉或列大机身方案。','', '机械图未核实前不能用二维表承诺三维装配通过。']
(root/'SPI显示屏市场候选池_20261009.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(len(rows),'candidates saved')

from pathlib import Path
import json,math
root=Path(__file__).resolve().parent;root.mkdir(exist_ok=True);(root/'assets').mkdir(exist_ok=True)
hardware=root.parent
existing=json.loads((hardware/'selection-visual-20261008/candidates.json').read_text(encoding='utf-8'))
data=[]
def add(id,category,model,w,h,t,url,notes,photo=None,price='国内含税报价/合作供应商/交期待核'):
 data.append(dict(id=id,category=category,model=model,w=w,h=h,t=t,url=url,notes=notes,photo=photo,price=price))
for p in existing:
 if p['category'] in ['主控','摄像头','联网'] or p['id']=='A01':
  category='功放' if p['id']=='A01' else p['category']
  add(p['id'],category,p['short'],p['w'],p['h'],p['t'],p['sources'][0] if p['sources'] else '',p['dimensions']+'；'+p['result'],('../selection-visual-20261008/assets/'+p['photo']) if p['photo'] else None)
for p in json.loads((hardware/'display-protocol-filter-20261009/displays.json').read_text(encoding='utf-8'))['candidates']:
 add(p['id'],'显示屏',p['model'],*(p['module_mm'] or [None,None]),p['thickness_mm'],p['sources'][0],p['bus']+'；'+p['notes'],('../display-protocol-filter-20261009/'+p['photo']) if p['photo'] else None)
for p in json.loads((hardware/'battery-selection-20261009/batteries.json').read_text(encoding='utf-8')):
 add(p['id'],'电池',p['model'],*(p['dims'] or [None,None,None]),p['url'],str(p['capacity'])+'mAh；'+p['dimension_status']+'；'+p['notes'],('../battery-selection-20261009/'+p['photo']) if p['photo'] else None,p['price'])
for name,cat in [('喇叭候选池_20261009.json','喇叭'),('天线候选池_20261009.json','天线')]:
 for p in json.loads((hardware/name).read_text(encoding='utf-8'))['candidates']:
  notes=(f"{p.get('impedance')}Ω / {p.get('power')}W；" if cat=='喇叭' else p['bands']+'；'+p['connector']+'；')+p['notes']
  add(p['id'],cat,p['model'],p['w'],p['h'],p['t'],p['url'],notes)
  data[-1]['photo_url']=p.get('photo_url');data[-1]['photo_note']=p.get('photo_kind',p.get('photo_status'))
add('C03','摄像头','SC3336 3MP Camera (A)',None,None,None,'https://www.waveshare.com/wiki/SC3336_3MP_Camera_%28A%29','真实3MP CSI候选；Luckfox平台参考，镜头FOV/端到端厚度和具体板SDK须核；不套用MIS5001尺寸。')
add('C04','摄像头','SC3336 3MP Camera (B)',None,None,None,'https://www.waveshare.com/sc3336-3mp-camera-b.htm','真实3MP CSI候选；不同镜头配置，尺寸、畸变、FOV与算法最低像素待评估。')
add('C05','摄像头','IMX415-8MP-USB-Camera-A',None,None,None,'https://docs.waveshare.com/IMX415-8MP-USB-Camera-A','真实8MP USB方案；不是CSI替代即插即用，需核UVC、带宽、功耗、FOV与完整载板。尺寸未核，排布不使用。')
add('N03','联网','Air780ER',17.7,15.8,2.3,'https://docs.openluat.com/air780er/product/','主打USB上网，与Air780E功能不同；Linux驱动/固件/峰值/天线座待确认。')
add('N04','联网','SIMCom A7670C',None,None,None,'https://cn.simcom.com/product/A7670X.html','厂家A7670系列CN候选；中国频段及LinuxUSB/AT订货变体待锁，完整封装图本轮未抽取，不用系列相近尺寸代替。')
add('N05','联网','Quectel EG915U-CN',23.6,19.9,2.4,'https://www.quectel.com/content/uploads/2024/03/Quectel_EG915U_Series_LTE_Standard_Module_Specification_V1.6.pdf','Cat1国内版对照；更大封装，USB网络驱动、供电和固件团队熟悉度待核。')
add('N06','联网','ESP32-C3-MINI-1-N4X',13.2,16.6,2.4,'https://documentation.espressif.com/esp32-c3-mini-1_datasheet_en.html','Wi-Fi/BLE协处理器路线；不是RV1106原生LinuxWiFi驱动。需主机协议/ESP-IDF维护；板载天线净空依厂家布局。')
for id,cat,model,url,notes in [
 ('PWR01','充电与电源','BQ24074','https://www.ti.com/product/BQ24074','单节PowerPath充电候选；热耗散/NTC/边充边用及电池充电倍率待设计。'),
 ('PWR02','充电与电源','TPS61088','https://www.ti.com/product/TPS61088','升压候选；开关10A不能当5V输出10A；电感/布局/效率/热验算。'),
 ('AMP02','功放','MAX98357A','https://www.analog.com/en/products/max98357a.html','I2S功放候选；RV1106接口/SDK、阻抗、供电与限幅待核；芯片封装不是整电路空间。'),
 ('AUD01','音频采集','TLV320AIC3104','https://www.ti.com/product/TLV320AIC3104','Codec候选；团队方案、驱动及麦克风输入选型待定，不能当麦克风产品。'),
 ('MIC01','音频采集','SPH0645LM4H-B / Adafruit #3421','https://www.adafruit.com/product/3421','真实I2S麦克风验证模块；RV1106采样格式/接口冲突/AEC适配待核，生产可换MEMS单体方案。')]:add(id,cat,model,None,None,None,url,notes)
(root/'components.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
phi=(1+math.sqrt(5))/2
plans=[]
for id,title,w,screen,speaker,battery,notes in [
 ('S1','紧凑方屏 / Wi-Fi优先',63.2,[33.13,41.13,9.5],[30,20,4],[36,60,7],'摄像头在上、方屏中部、椭圆喇叭下部；屏背自研板、板背软包。LTE内置净空不足未闭环，首轮可外置天线验证。'),
 ('S2','圆屏 / LTE优先空间',76.4,[55,55,13],[28,28,5.2],[36,60,7],'独立1.85QSPI屏或ESP协处理路线均未闭环；右侧纵向预留FXP14、左上WiFi，PCB/电池偏左，2W喇叭独立后腔。'),
 ('S3','裸圆屏 / 圆柱容量路线',73.2,[48.08,49.59,1.96],[28,28,5.2],[37,69,18],'裸圆屏QSPI适配待定；1S2P电池包后置增加厚度，PCB与电池不能侵占下部声腔；LTE区域需供应商审图。')]:
 h=round(w*phi,1);d=round(w/phi,1)
 front_min=24+screen[1]+speaker[1]+16
 stack=screen[2]+1+10+2+battery[2]+2+4
 plans.append(dict(id=id,title=title,w=w,h=h,d=d,phi=phi,screen=screen,speaker=speaker,battery=battery,pcb=[42,55,10],front_min=front_min,depth_min=stack,box_volume_cm3=w*h*d/1000,rounded_estimate_cm3=(w*h-(4-math.pi)*15**2)*d/1000,notes=notes,status='讨论占位，未完成CAD/RF/声学验证',wall=2,corner_radius=15))
(root/'layout-plans.json').write_text(json.dumps(plans,ensure_ascii=False,indent=2),encoding='utf-8')
print('Prepared',len(data),'component records and 3 layouts')

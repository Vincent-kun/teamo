from pathlib import Path
import json,shutil,hashlib
root=Path(__file__).resolve().parent;root.mkdir(exist_ok=True);(root/'assets').mkdir(exist_ok=True)
items=[]
def add(id,model,form,cap,v,dims,continuous,price,url,notes,pcm=True,ntc=False,tolerance=None):
 items.append(dict(id=id,model=model,form=form,capacity=cap,voltage=v,dims=dims,continuous=continuous,price=price,url=url,notes=notes,pcm=pcm,ntc=ntc,tolerance=tolerance,photo=None,photo_note='精确型号产品图待补',domestic='供应商关系/MOQ/含税报价/交期待询',dimension_status='商品页包体参考，线材连接器及公差另核'))
add('BAT01','LiPol LP503450 / 850mAh PCM','软包',850,3.7,[34,50,5],.85,'RFQ','https://www.lipolbattery.com/LiPo-Battery-Datahseet/LiPo_Battery_LP503450_3.7V_850mAh.pdf','同型号不同厂家容量可能不同；保护阈值不是允许连续电流。',tolerance=[.5,1,.3])
add('BAT02','LiPol LP603450 / 1100mAh PCM+NTC','软包',1100,3.7,[34,50,6],1.1,'RFQ','https://www.lipolbattery.com/LiPo-Battery-Datahseet/LiPo_Battery_LP603450_3.7V_1100mAh.pdf','厂家PDF明确PCM+10k NTC、3pin Molex；需当批确认。',ntc=True,tolerance=[.5,1,.3])
add('BAT03','Adafruit #258 / 1200mAh','软包',1200,3.7,[35,62,5],None,'USD 9.95 / 零售','https://www.adafruit.com/product/258','商品写34×62×5，链接图纸35±0.3×62±0.3×5±0.3；本轮以35mm保守参考，冲突未闭环。2A线材不代表电芯连续2A。',tolerance=[.3,.3,.3])
add('BAT04','Adafruit #2011 / 2000mAh','软包',2000,3.7,[36,60,7],None,'USD 12.50 / 零售','https://www.adafruit.com/product/2011','标准放电约0.5A，不作为最大连续值；JST-PH、无NTC。旧资料缺货已过时，本轮不保证国内库存。')
add('BAT05','Adafruit #328 / 2500mAh','软包',2500,3.7,[50,60,7.3],None,'USD 14.95 / 零售','https://www.adafruit.com/product/328','较宽软包，放入60mm外宽机身时须扣壁厚、支架和公差；最大连续待数据表核。')
add('BAT06','Adafruit #1578 / 500mAh','软包',500,3.7,[29,36,4.75],None,'USD 7.95 / 零售','https://www.adafruit.com/product/1578','小容量对照；不是RV1106+4G主电池推荐。线长102mm另计收纳。')
add('BAT07','Adafruit #1781 / 2200mAh','圆柱包',2200,3.7,[18,69,18],1,'USD 9.95 / 零售','https://www.adafruit.com/product/1781','带保护的整包长69mm，不能按裸18650的65mm画槽；厂家建议持续负载低于约1A，4.4A为峰值。')
add('BAT08','Adafruit #354 / 4400mAh 1S2P','圆柱包',4400,3.7,[37,69,18],2.2,'USD 19.95 / 零售','https://www.adafruit.com/product/354','两芯并联成品包；2.2A为厂家建议最大放电值，线材/接口电流另核。')
add('BAT09','Adafruit #353 / 6600mAh 1S3P','圆柱包',6600,3.7,[54,69,18],3.3,'USD 24.50 / 零售','https://www.adafruit.com/product/353','三芯并联包；容量高但宽厚，不宜紧凑首选。连接器是否支持3.3A需单独核对。')
add('BAT10','Molicel INR-18650-P28A / 2800mAh','裸圆柱',2800,3.6,[18.6,65.2,18.6],None,'RFQ','https://www.molicel.com/product/inr-18650-p28a/','裸电芯最大直径18.6/高65.2；最大放电35A是电芯规格，未作为整包连续评级。PCM、NTC、镍带和绝缘尺寸另设计。',pcm=False,ntc=None,tolerance=[0,0,0])
old=root.parent/'selection-visual-20261008'
sources=json.loads((old/'image-sources.json').read_text(encoding='utf-8'))
for id,f in [('BAT03','battery1200.jpg'),('BAT04','battery2000.jpg')]:
 r=next(x for x in items if x['id']==id);shutil.copyfile(old/'assets'/f,root/'assets'/f);r['photo']='assets/'+f;r['photo_note']='厂家产品照片（既有来源归档）';r['image_source']=next((x for x in sources if x['file']==f),{})
for r in items:
 if r['id'] in ['BAT01','BAT02']:r['dimension_status']='厂家PDF带PCM包体公差；线材/插头另计'
 if r['id']=='BAT10':r['dimension_status']='裸电芯最大包络，不是成品电池包'
(root/'batteries.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
print('Prepared',len(items),'exact battery records')

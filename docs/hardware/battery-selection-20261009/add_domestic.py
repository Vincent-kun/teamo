from pathlib import Path
import json
root=Path(__file__).resolve().parent
rows=json.loads((root/'batteries.json').read_text(encoding='utf-8'))
for id,model,cap,dims,url,notes in [
 ('BAT11','EEMB LP603450HA',1100,[34.5,52,6.3],'https://www.eemb.com/product-252','裸芯最大外缘L1≤52；最大11A/10C未另列持续温升条件，成品连续/PCM/NTC待定。'),
 ('BAT12','EEMB LP803560HA',1700,[35.5,62,8.3],'https://www.eemb.com/product-253','裸芯L1≤62；最大17A/10C，不作为成品包持续供电能力。'),
 ('BAT13','EEMB LP103454LC',2000,[34.5,56,10.3],'https://www.eemb.com/product-161','低温裸芯L1≤56；常温最大4A，保护包外形及连续温升条件待核。')]:
 if any(r['id']==id for r in rows):continue
 rows.append(dict(id=id,model=model,form='软包',capacity=cap,voltage=3.7,dims=dims,continuous=None,price='RFQ',url=url,notes=notes,pcm=False,ntc=None,tolerance=None,photo=None,photo_note='厂家型号页图片待归档',domestic='中国厂家可询；合作/MOQ/交期/含税价待核',dimension_status='裸电芯最大外缘；成品保护包尺寸未知'))
(root/'batteries.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')

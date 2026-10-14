from pathlib import Path
import json,re,hashlib
root=Path(__file__).resolve().parent
inventory={r['id']:r for r in json.loads((root/'photo-inventory.json').read_text(encoding='utf-8'))}
manifest=json.loads((root/'photo-sources.json').read_text(encoding='utf-8'))
reasons={'WS09':'厂家网页抓取未成功，尚未取得对应1.8寸128×160模组图。','WS16':'厂家网页抓取未成功；不得使用480×800、HDMI或ESP整板版本代图。','WS17':'历史Rev1尚未取得版本可识别产品图；当前Rev2图片不能证明Rev1外观。','EX07':'目前只有对应型号厂家PDF资料，未取得产品照片。','EX08':'厂家页面返回403；对应5714触控版照片未取得。','EX09':'厂家页面返回403；无触控版照片未取得。','EX10':'厂家页面返回403；5982带MCU智能屏照片未取得。'}
for r in manifest:
 inv=inventory[r['id']]
 urls=list(dict.fromkeys(inv.get('parsed_images',[])+[u for pg in inv['pages'] for u in pg.get('images',[])]))
 own=[u for u in urls if u!=r.get('url') and '/thumbnail/' not in u and '/File:' not in u and ('product2' in u or re.search(r'-(?:2|3)(?:_1)?\.jpg$',u))]
 # Only model-specific views already present in a manufacturer page. No recommendation/sidebar images.
 own=[u for u in own if ('1.54-product2' in u and r['id']=='WS06') or ('1.83-product2' in u and r['id']=='WS11') or (r['id']=='WS10' and '1.83inch-lcd-module-' in u.lower()) or (r['id']=='WS08' and '1.69inch-touch-lcd-module-' in u.lower()) or (r['id']=='WS03' and '1.28inch-touch-lcd-' in u.lower())]
 r['other_views']=[{'url':u,'caption':'厂家其他视角原图（在线打开，视角与版本需核）'} for u in own[:2]]
 r['missing_reason']=reasons.get(r['id'])
(root/'photo-sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 屏幕产品图片证据与缺项｜2026-10-09','','已有20条厂家型号页产品图，加1条版本待核图片。7条缺图；不以其他型号代替。厂家的屏幕演示画面不是团队上电验证证据。','','| ID | 型号 | 缺图原因 | 厂家入口 |','|---|---|---|---|']
data=json.loads((root/'displays.json').read_text(encoding='utf-8'))['candidates']
for p in data:
 if p['id'] in reasons:lines.append(f"| {p['id']} | {p['model']} | {reasons[p['id']]} | [厂家资料]({p['sources'][0]}) |")
lines+=['','找涛哥/供应商补齐：','', '请提供指定型号及Rev的正面、背面、侧面实物照片；附带丝印/排线编号与尺寸图。请确认报价对象是裸LCM、带触控LCM还是含载板模组，并提供完整W×H×T、连接器/排线伸出量、触控玻璃外形以及允许的排线弯折区域。照片仅确认形态，机械尺寸以图纸与样品测量为准。','','图片来源和SHA256见 [photo-sources.json](photo-sources.json)。']
(root/'产品图片缺项与供应商补图清单.md').write_text('\n'.join(lines),encoding='utf-8')
print('Updated photo evidence and missing-model checklist')

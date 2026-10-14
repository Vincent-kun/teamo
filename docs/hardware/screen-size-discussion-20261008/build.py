"""真实器件输入＋明确设计预算，生成讨论图和可复算JSON；不判定CAD容纳性。"""
from pathlib import Path
import json, math, html
root=Path(__file__).resolve().parent
phi=(1+math.sqrt(5))/2
plans=[
 dict(id='P1',title='方屏 · 核心板',d=38,screen=(33.13,41.13),pic='LCD169-Touch-drawing.png',model='1.69inch Touch LCD Module',board=(42,55),budget=36,terms=[9.5,1,10,1,7.2,3,4.3],note='Core30×30×5.50；载板42×55×10为待设计占位。SPI显示/I2C触控仍需适配。'),
 dict(id='P2',title='圆屏 · 双处理器',d=42,screen=(55,55),pic='esp32.jpg',model='ESP32-S3-Touch-LCD-1.85',board=(42,55),budget=39.5,terms=[13,1,10,1,7.2,3,4.3],note='55×55真实整板；T暂占13，不是厂家厚度。ESP负责UI，RV负责视觉；协议待开发。'),
 dict(id='P3',title='裸圆屏 · 产品化',d=35,screen=(48.08,49.59),pic='round.webp',model='ND018TCM360360-A01',board=(42,55),budget=31.3,terms=[24,3,4.3],note='屏厚1.96已公开；此路线深度由24mm相机安装占位主导。QSPI/FPC/电压未闭环。'),
 dict(id='P4',title='开发平台 · 非产品尺寸',d=52,screen=(33.13,41.13),pic='LCD169-Touch-drawing.png',model='Pico Max + 1.69inch Touch LCD Module',board=(21,72),budget=51,terms=[9.5,1,25,1,7.2,3,4.3],note='21×72真实板框，含插线T暂占25。52mm深度保留同截面电池预算；连接器超预算需扩大。'),
]
for p in plans:
 p.update(w=p['d']*phi,h=p['d']*phi**2,remaining=p['d']-p['budget'])
 p['width_min']=max(p['screen'][0],p['board'][0],36,25)+5.5
 p['front_height_min']=p['screen'][1]+24+4+5.5
 assert math.isclose(sum(p['terms']),p['budget'])
 assert p['w']>=p['width_min'] and p['h']>=p['front_height_min']
(root/'size-budgets.json').write_text(json.dumps(dict(date='2026-10-08',phi=phi,units='mm',status='discussion proposals; not verified CAD',plans=plans),ensure_ascii=False,indent=2),encoding='utf-8')
def drawing(p):
 # All dimensions in SVG are mm; rectangle projections are not actual rounded cavity.
 w,h=p['w'],p['h']; sw,sh=p['screen'];bw,bh=p['board'];cam_y=8;sy=cam_y+24+4
 parts=f'<rect x="{(w-25)/2}" y="{cam_y}" width="25" height="24" fill="#f6e2b4" stroke="#ac792d"/><text x="{w/2}" y="{cam_y+14}" text-anchor="middle">相机25×24</text><rect x="{(w-sw)/2}" y="{sy}" width="{sw}" height="{sh}" fill="#d6e5f6" stroke="#426ead"/><text x="{w/2}" y="{sy+sh/2}" text-anchor="middle">屏{sw}×{sh}</text>'
 rear=f'<rect x="{w+14+(w-bw)/2}" y="12" width="{bw}" height="{bh}" fill="#dcebe1" stroke="#17775f"/><text x="{w*1.5+14}" y="28" text-anchor="middle">板{bw}×{bh}</text><rect x="{w+14+(w-36)/2}" y="{h-68}" width="36" height="60" fill="#ecedd5" fill-opacity=".6" stroke="#838b3c" stroke-dasharray="2 1"/><text x="{w*1.5+14}" y="{h-20}" text-anchor="middle">电池36×60</text>'
 return f'<svg viewBox="-3 -8 {2*w+20} {h+20}" role="img" aria-label="{p["id"]}毫米正投影讨论排布"><rect width="{w}" height="{h}" rx="5" fill="white" stroke="#19362f"/><rect x="{w+14}" width="{w}" height="{h}" rx="5" fill="white" stroke="#19362f"/>{parts}{rear}<text x="{w/2}" y="{h+8}" text-anchor="middle">前脸 · 屏/镜头</text><text x="{w*1.5+14}" y="{h+8}" text-anchor="middle">后层 · 不同深度叠放</text></svg>'
cards=[]
for p in plans:
 cards.append(f'''<article><small>{p['id']} · 讨论提案</small><h2>{p['title']}</h2><div class="size">{p['w']:.2f} × {p['d']:.2f} × {p['h']:.2f}<span>W×D×H / mm</span></div>{drawing(p)}<p class="note">包络正投影；圆角仅示意。载板与电池投影重叠代表前后分层，尚未完成三维干涉验证。</p><img src="../selection-visual-20261008/assets/{p['pic']}" alt="{html.escape(p['model'])}厂家产品或机械图"><h3>{html.escape(p['model'])}</h3><p>{p['note']}</p><p class="formula">深度截面预算 {p['budget']:.2f} mm<br>提案未分配余量 {p['remaining']:.2f} mm<br>前脸单高轴下限 {p['front_height_min']:.2f} mm</p></article>''')
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>屏幕与机身尺寸讨论方案</title><style>*{box-sizing:border-box}body{margin:0;background:#f5f7f1;color:#19362f;font:15px/1.7 "Segoe UI","Microsoft YaHei",sans-serif}main{max-width:1350px;margin:auto;padding:32px}h1{font-size:32px;line-height:1.3}h2{font-size:20px}h3{font-size:14px}a{color:#17775f}.intro{max-width:900px;color:#536a60}.warning{background:#fff3da;padding:14px 18px;border-left:3px solid #bd8636;margin:22px 0}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}article{padding:24px;background:white;border:1px solid #dce4dd;border-radius:12px}small{color:#17775f}.size{font-size:27px;font-weight:700;font-variant-numeric:tabular-nums}.size span{display:block;font-size:12px;font-weight:400;color:#6d7e76}svg{width:100%;height:310px;margin:16px 0}svg text{font-size:3.8px;fill:#19362f}img{width:100%;height:160px;object-fit:contain}.note{font-size:12px;color:#6d7e76}.formula{background:#e5f1e9;padding:12px;font-size:13px}footer{margin-top:24px;padding-top:18px;border-top:1px solid #dce4dd}@media(max-width:700px){main{padding:18px}.grid{grid-template-columns:1fr}article{padding:18px}.size{font-size:23px}h1{font-size:25px}}@media print{body{background:white}article{break-inside:avoid}}</style><main><div class="warning">2026-10-09范围更新：开发板仅作算法/驱动/接口验证平台，产品由团队自研主板。旧Core＋载板组合只保留为尺寸案例，未选为最终架构；P4不再是产品机身候选，开发板尺寸不反推产品PCB。 <a href="../rv1106-board-identification-20261009/index.html">开发平台辨认图册</a></div><small>TEAMO / 魏子奇硬件讨论输入 · 2026-10-08</small><h1>先选屏幕路线，再讨论机身多大。</h1><p class="intro">建议带P1方屏核心板与P2圆屏双处理器两套主方案。P3作为裸屏产品化方向，P4作为现成开发板工程样机。尺寸包含真实器件平面输入与明确设计预留，所有未知完整厚度继续标注。</p><div class="warning">主控尚未选定：Core只是有尺寸的备选参考。RV1106B供应商板到手后重新计算。电池#2011仅作2000mAh真实包络参考，官方缺货；4G/天线/声腔、散热与曲面容纳性尚未闭环。</div><p><a href="../屏幕与整机尺寸方案_20261008_V0.1.md">完整方案、截面计算与讨论议程</a> · <a href="../屏幕候选官方复核_20261008.md">六屏官方复核</a> · <a href="../selection-visual-20261008/index.html">真实器件图册</a></p><div class="grid">__CARDS__</div><footer>公式：W=φD，H=φ²D；D是本轮透明设计预算，φ≈1.618。两位小数表示计算显示精度，制造偏差由同工艺打印试片校准。图不包含厂家精确板框、孔位或FPC。<br><a href="size-budgets.json">可复算尺寸JSON</a></footer></main></html>'''
(root/'index.html').write_text(page.replace('__CARDS__',''.join(cards)),encoding='utf-8')
print('Built 4 discussion proposals with explicit budget assumptions')
md=root.parent/'屏幕与整机尺寸方案_20261008_V0.1.md'
s=md.read_text(encoding='utf-8').replace('**77.67×48.00×125.67**','**84.14×52.00×136.14**').replace('讨论深度35/38/42/48','讨论深度35/38/42/52')
s=s.replace('所以P4不能让屏、开发板、电池三层同截面！','P4主提案取D=52.0，保留1.0mm未分配预算。缩至48mm才需要错层。')
s=s.replace('**P4的48mm版是条件提案，优先给技术负责人检查电池是否能错层；不能为外观压缩电池。**','**P4主提案是52mm深度；48mm版仅是错层可行时的缩小方向，不能为外观压缩电池。**')
md.write_text(s,encoding='utf-8')

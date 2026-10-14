# -*- coding: utf-8 -*-
"""Teamo 运动图标方案对比页 v2:A-I 九组(库选型 A-D + 像素/手绘/配色/手机端/duotone E-I)"""
import urllib.request, json, os

UA = {'User-Agent': 'Mozilla/5.0'}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=15).read().decode()

BATCH = {
    'tabler': 'jump-rope,run,walk,barbell,dumbbell,stretching,stretching-2,trophy,settings,heartbeat,activity,yoga,treadmill,user,bell,calendar,clock,share,home,circle-check,chevron-right,heart,moon,plus,send,stopwatch,flame',
    'mingcute': 'squats-line,yoga-line,walk-line,run-line,heartbeat-line,trophy-line,settings-6-line,squats-fill,yoga-fill,heartbeat-fill,walk-fill,trophy-fill,settings-6-fill',
    'lucide': 'activity,dumbbell,trophy,settings,person-standing,heart-pulse,footprints',
    'iconoir': 'running,yoga,activity,settings',
    'material-symbols': 'exercise,sprint',
    'ph': 'trophy-duotone,heartbeat-duotone,barbell-duotone,timer-duotone,flame-duotone,user-duotone,gear-duotone,check-fat-duotone',
    'pixelarticons': 'trophy,heart,human',
}
symbols, available = {}, set()
for prefix, icons in BATCH.items():
    try:
        data = json.loads(get(f'https://api.iconify.design/{prefix}.json?icons={icons}'))
        w_def, h_def = data.get('width', 24), data.get('height', 24)
        for name, info in data.get('icons', {}).items():
            w, h = info.get('width', w_def), info.get('height', h_def)
            symbols[f'{prefix}-{name}'] = f'<symbol id="{prefix}-{name}" viewBox="0 0 {w} {h}">{info["body"]}</symbol>'
            available.add(f'{prefix}:{name}')
        print(f'{prefix}: ok')
    except Exception as e:
        print(f'{prefix}: ERR {e}')

def use(name, cls='ic', style=''):
    if not name or name.replace(':', '-') not in symbols:
        return f'<i class="miss">{name or "?"}</i>'
    st = f' style="{style}"' if style else ''
    return f'<svg class="{cls}" viewBox="0 0 24 24"{st}><use href="#{name.replace(":", "-")}"/></svg>'

# ── E 组:自绘 12×12 像素画(shape-rendering:crispEdges) ──
PIX = {
 'rope':  [(1,0),(2,0),(3,0),(8,0),(9,0),(10,0),(2,1),(9,1),(2,2),(9,2),(2,3),(9,3),
           (2,4),(9,4),(1,5),(10,5),(1,6),(10,6),(1,7),(10,7),(2,8),(9,8),(3,9),(8,9),
           (4,10),(5,10),(6,10),(7,10)],
 'jump':  [(5,0),(6,0),(5,1),(6,1),(2,0),(9,0),(3,1),(8,1),(4,2),(7,2),(5,2),(6,2),
           (5,3),(6,3),(5,4),(6,4),(4,5),(7,5),(3,6),(8,6),(3,7),(8,7),(2,8),(9,8),
           (2,9),(9,9),(1,10),(10,10)],
 'squat': [(6,1),(7,1),(6,2),(7,2),(5,3),(5,4),(4,5),(3,5),(2,5),(1,5),(4,6),(1,6),
           (4,7),(1,7),(4,8),(1,8),(4,9),(1,9),(0,10),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10)],
 'stretch':[(5,0),(6,0),(5,1),(6,1),(8,0),(7,1),(5,2),(6,2),(5,3),(6,3),(4,3),(3,4),
           (5,4),(6,4),(5,5),(6,5),(5,6),(6,6),(5,7),(6,7),(4,8),(7,8),(4,9),(7,9),(4,10),(7,10)],
}
def pixel_svg(key, cls='ic pix'):
    rects = ''.join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for x, y in PIX[key])
    return f'<svg class="{cls}" viewBox="0 0 12 12" style="shape-rendering:crispEdges" fill="currentColor">{rects}</svg>'

SKETCH_JS = None  # 滤镜直接写在 HTML 头部

NAMES = {'rope':'跳绳','jump':'开合跳','squat':'深蹲','stretch':'拉伸'}
HINTS = {'rope':'协调 · 心肺','jump':'全身 · 热身','squat':'下肢力量','stretch':'放松 · 柔韧'}
D_SPORTS = {'rope':'tabler:jump-rope','jump':'iconoir:running','squat':'mingcute:squats-line','stretch':'tabler:stretching'}
D_MENU = ['tabler:heartbeat','tabler:barbell','tabler:trophy','tabler:settings']

def sports_cards(mapping, notes=None):
    out = ''
    for k, n in mapping.items():
        note = (notes or {}).get(k, n)
        out += f'<div class="sp"><div class="sp-ico">{use(n) if ":" in str(n) else n}</div><b>{NAMES[k]}</b><small>{note}</small><em>{HINTS[k]}</em></div>'
    return out

def ctx_sports(mapping):
    tabs = ''.join(f'<span class="{"on" if i==0 else ""}">{use(n)}</span>' for i,(k,n) in enumerate(mapping.items()))
    choice = use(list(mapping.values())[0])
    return f'''<div class="sim"><small>设备端 · 运动选择(选中态)</small>
      <div class="sim-tabs">{tabs}</div><div class="sim-choice">{choice}</div></div>'''

def ctx_menu(items):
    menu = ''.join(f'<span>{use(n)}</span>' for n in items)
    return f'''<div class="sim"><small>设备端 · Workout 菜单四宫格</small>
      <div class="sim-menu">{menu}</div><small class="dim">记录 · 力量 · 成就 · 设置</small></div>'''

blocks = []

# ── A-D:库选型四组(沿用 v1) ──
LIB_SCHEMES = [
 ('A','方案 A · Tabler 纯系','MIT · 1.5px 锐利线稿 · 细节丰富',
  {'rope':('tabler:jump-rope','唯一正解图标'),'jump':('tabler:run','近似:跑步人形'),'squat':('tabler:barbell','近似:杠铃负重'),'stretch':('tabler:stretching-2','正解')},
  ['tabler:heartbeat','tabler:barbell','tabler:trophy','tabler:settings']),
 ('B','方案 B · MingCute 圆润系','Apache 2.0 · 圆头填充线稿 · 儿童亲和感',
  {'rope':('tabler:jump-rope','正解(跨库)'),'jump':('mingcute:run-line','近似:跑步人形'),'squat':('mingcute:squats-line','正解:深蹲人形'),'stretch':('mingcute:yoga-line','近似:瑜伽伸展')},
  ['mingcute:heartbeat-line','mingcute:squats-line','mingcute:trophy-line','mingcute:settings-6-line']),
 ('C','方案 C · Lucide 极简几何','ISC · 极简抽象 · 语义最弱(对照组)',
  {'rope':('lucide:activity','抽象:节律波'),'jump':('lucide:person-standing','抽象:人形'),'squat':('lucide:dumbbell','近似:哑铃'),'stretch':('lucide:footprints','抽象:步迹')},
  ['lucide:activity','lucide:dumbbell','lucide:trophy','lucide:settings']),
 ('D','方案 D · 混合精选(推荐)','跨库取语义最准 · 视觉重统一',
  {'rope':('tabler:jump-rope','正解'),'jump':('iconoir:running','近似:动作人形'),'squat':('mingcute:squats-line','正解:深蹲人形'),'stretch':('tabler:stretching','正解')},
  ['tabler:heartbeat','tabler:barbell','tabler:trophy','tabler:settings']),
]
for key, title, meta, sports, menu in LIB_SCHEMES:
    mapping = {k: v[0] for k, v in sports.items()}
    notes = {k: v[1] for k, v in sports.items()}
    blocks.append(f'''<section class="scheme" id="s{key}"><header><b>{title}</b><small>{meta}</small></header>
    <div class="sports">{sports_cards(mapping, notes)}</div>
    <div class="ctx">{ctx_sports(mapping)}{ctx_menu(menu)}</div></section>''')

# ── E:像素风 ──
pix_cards = ''.join(f'<div class="sp"><div class="sp-ico">{pixel_svg(k)}</div><b>{NAMES[k]}</b><small>自绘 12×12</small><em>{HINTS[k]}</em></div>' for k in NAMES)
pix_menu = f'''<span style="color:#c6ff45;border:3px solid #c6ff45;background:transparent">{use('pixelarticons:heart')}</span>
<span>{pixel_svg('squat','ic pix2')}</span><span>{use('pixelarticons:trophy')}</span><span>{use('pixelarticons:human')}</span>'''
pix_tabs = ''.join(f'<span class="{"on" if i==0 else ""}">{pixel_svg(k,"ic pix3")}</span>' for i,k in enumerate(NAMES))
blocks.append(f'''<section class="scheme" id="sE"><header><b>方案 E · 像素风(游戏感)</b><small>动作图标自绘 12×12 像素画 · 菜单混搭 PixelartIcons(MIT) · 复古街机气质</small></header>
<div class="sports">{pix_cards}</div>
<div class="ctx">
<div class="sim"><small>设备端 · 运动选择(选中态)</small><div class="sim-tabs">{pix_tabs}</div><div class="sim-choice">{pixel_svg('rope','ic pix4')}</div></div>
<div class="sim"><small>设备端 · Workout 菜单四宫格</small><div class="sim-menu">{pix_menu}</div><small class="dim">记录 · 力量 · 成就 · 个人</small></div>
</div></section>''')

# ── F:手绘涂鸦风(feTurbulence 抖动滤镜) ──
sk_style = 'filter:url(#sketchy)'
sk_cards = ''.join(f'<div class="sp paper"><div class="sp-ico ink">{use(n,"ic",sk_style)}</div><b>{NAMES[k]}</b><small>{n}</small><em>{HINTS[k]}</em></div>' for k,n in D_SPORTS.items())
sk_tabs = ''.join(f'<span class="{"on" if i==0 else ""}">{use(n,"ic",sk_style)}</span>' for i,(k,n) in enumerate(D_SPORTS.items()))
sk_menu = ''.join(f'<span class="paper2">{use(n,"ic",sk_style)}</span>' for n in D_MENU)
blocks.append(f'''<section class="scheme paper-bg" id="sF"><header><b>方案 F · 手绘涂鸦风</b><small>Tabler/MingCute 线稿 × feTurbulence 位移滤镜 · 蜡笔纸感</small></header>
<div class="sports">{sk_cards}</div>
<div class="ctx">
<div class="sim"><small>设备端 · 运动选择(选中态)</small><div class="sim-tabs">{sk_tabs}</div><div class="sim-choice">{use(D_SPORTS["rope"],"ic",sk_style)}</div></div>
<div class="sim"><small>设备端 · Workout 菜单四宫格</small><div class="sim-menu">{sk_menu}</div><small class="dim">记录 · 力量 · 成就 · 设置</small></div>
</div></section>''')

# ── G:配色探索(D 组正解图标 × 5 主题) ──
THEMES = [
 ('现状 · 荧光绿','#0d1216','#c6ff45','present'),
 ('活力橙黄','#10151f','#ffb03a',''),
 ('糖果撞色','#171225','#ff6b9d',''),
 ('海盐薄荷','#0e1a18','#5ef2c8',''),
 ('阳光柠檬','#151310','#ffe14d',''),
]
theme_rows = ''
for tname, bg, fg, cls in THEMES:
    icons4 = ''.join(f'<span>{use(n)}</span>' for n in D_SPORTS.values())
    menu4 = ''.join(f'<span>{use(n)}</span>' for n in D_MENU)
    theme_rows += f'''<div class="theme"><div class="tname">{tname}<small>{fg} on {bg}</small></div>
    <div class="tchip" style="background:{bg};color:{fg}"><div class="trow">{icons4}</div><div class="trow">{menu4}</div></div></div>'''
blocks.append(f'''<section class="scheme" id="sG"><header><b>方案 G · 配色探索</b><small>D 组语义正解图标 × 5 套配色 · 同一图标换主题 instantly</small></header>
{theme_rows}
<small class="dim" style="color:#5f6b74;font-size:11px">每行上排=运动四件套,下排=Workout 菜单;所有配色保持 ≥4.5:1 对比度</small>
</section>''')

# ── H:手机端 UI 图标全套 + 手机语境 ──
PHONE_ICONS = [('tabler:user','我的孩子'),('tabler:bell','通知'),('tabler:send','发送邀请'),('tabler:calendar','运动计划'),
 ('tabler:clock','时长'),('tabler:stopwatch','倒计时'),('tabler:heart','鼓励'),('tabler:trophy','成就'),
 ('tabler:flame','卡路里'),('tabler:moon','休息'),('tabler:circle-check','已完成'),('tabler:share','分享成绩'),
 ('tabler:home','首页'),('tabler:plus','添加'),('tabler:chevron-right','进入'),('tabler:gear' if 'tabler-gear' in symbols else 'tabler:settings','设置')]
phone_grid = ''.join(f'<div class="ph-ic">{use(n)}<b>{label}</b></div>' for n,label in PHONE_ICONS)
phone_sim = f'''<div class="sim-phone">
<div class="ph-top">{use('tabler:user','ic2')}<b>小宇的运动</b>{use('tabler:bell','ic2')}</div>
<div class="ph-card">{use('tabler:jump-rope','ic3')}<div><b>跳绳</b><small>协调 · 心肺</small></div>{use('tabler:chevron-right','ic2')}</div>
<div class="ph-card">{use('tabler:barbell','ic3')}<div><b>深蹲</b><small>下肢力量</small></div>{use('tabler:chevron-right','ic2')}</div>
<div class="ph-cta">{use('tabler:send','ic2')} 邀请运动</div>
<div class="ph-check">{use('tabler:circle-check','ic2')} 已连接设备 {use('tabler:clock','ic2')} 08:24</div>
</div>'''
blocks.append(f'''<section class="scheme" id="sH"><header><b>方案 H · 手机端 UI 图标全套</b><small>Tabler 统一 · 家长端 App 16 枚常用图标 + 真实界面模拟</small></header>
<div class="phone-grid">{phone_grid}</div>
<div class="ctx" style="grid-template-columns:1fr">{phone_sim}</div>
</section>''')

# ── I:厚实 Duotone / 填充风 ──
I_SPORTS = {'rope':('tabler:jump-rope','线稿正解(duotone 无跳绳,后续可手绘 duotone 化)'),'jump':('mingcute:walk-fill','近似:动作人形'),'squat':('mingcute:squats-fill','正解填充版'),'stretch':('mingcute:yoga-fill','近似:瑜伽伸展')}
I_MENU = ['ph:heartbeat-duotone','ph:barbell-duotone','ph:trophy-duotone','ph:gear-duotone']
i_cards = ''.join(f'<div class="sp"><div class="sp-ico">{use(n)}</div><b>{NAMES[k]}</b><small>{note}</small><em>{HINTS[k]}</em></div>' for k,(n,note) in I_SPORTS.items())
i_tabs = ''.join(f'<span class="{"on" if i==0 else ""}">{use(n)}</span>' for i,(k,(n,_)) in enumerate(I_SPORTS.items()))
i_menu = ''.join(f'<span>{use(n)}</span>' for n in I_MENU)
blocks.append(f'''<section class="scheme" id="sI"><header><b>方案 I · 厚实 Duotone / 填充风</b><small>Phosphor Duotone(MIT) + MingCute Fill(Apache 2.0) · 高辨识度 · 远距可读性最好</small></header>
<div class="sports">{i_cards}</div>
<div class="ctx">
<div class="sim"><small>设备端 · 运动选择(选中态)</small><div class="sim-tabs">{i_tabs}</div><div class="sim-choice">{use("mingcute:squats-fill")}</div></div>
<div class="sim"><small>设备端 · Workout 菜单四宫格</small><div class="sim-menu">{i_menu}</div><small class="dim">记录 · 力量 · 成就 · 设置</small></div>
</div></section>''')

nav = ''.join(f'<a href="#s{k}">{t}</a>' for k,t in [('A','A Tabler'),('B','B MingCute'),('C','C Lucide'),('D','D 混合'),('E','E 像素'),('F','F 手绘'),('G','G 配色'),('H','H 手机端'),('I','I Duotone')])

html = f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Teamo · 运动图标方案对比 v2(A-I 九组)</title><style>
:root{{font-family:Inter,'Noto Sans SC',sans-serif;color:#eef2f5}}
*{{box-sizing:border-box}}
body{{margin:0;background:radial-gradient(circle at 50% -20%,#26313a 0,#131a20 43%,#0d1216 100%);min-height:100vh;padding:36px 5vw 90px}}
h1{{font-size:25px;margin:0 0 6px}} .sub{{color:#8f9aa4;font-size:13px;margin:0 0 18px;line-height:1.8}}
.sub b{{color:#c6ff45}}
nav.top{{position:sticky;top:0;z-index:9;display:flex;gap:8px;flex-wrap:wrap;padding:10px 0;background:linear-gradient(#0d1216f0,#0d121600);margin-bottom:8px}}
nav.top a{{padding:7px 14px;border:1px solid #2e3840;border-radius:16px;color:#aab4bd;font-size:12px;text-decoration:none}}
nav.top a:hover{{border-color:#c6ff45;color:#c6ff45}}
.note{{border-left:3px solid #c6ff45;padding:10px 16px;color:#aab4bd;font-size:13px;line-height:1.8;margin-bottom:26px}}
.scheme{{border:1px solid #2a3137;border-radius:22px;background:#11161a;padding:26px 28px;margin-bottom:26px;scroll-margin-top:60px}}
.scheme header{{display:flex;align-items:baseline;gap:14px;margin-bottom:20px;flex-wrap:wrap}}
.scheme header b{{font-size:19px}} .scheme header small{{color:#7f8a91;font-size:12.5px}}
.sports{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}
.sp{{border:1px solid #262e35;border-radius:16px;background:#151b20;padding:20px 10px 14px;display:grid;justify-items:center;gap:6px;text-align:center}}
.sp.paper{{background:#f5f0e2;border-color:#d8d0bc}} .sp.paper b{{color:#3a3226}} .sp.paper small{{color:#8a7f68}} .sp.paper em{{color:#7a6f5a}}
.sp-ico{{width:64px;height:64px;display:grid;place-items:center;color:#c6ff45}}
.sp.paper .sp-ico{{color:#4a3f2d}}
.sp-ico svg{{width:54px;height:54px}}
.sp b{{font-size:14.5px}} .sp small{{font-size:10px;color:#5f6b74;word-break:break-all}} .sp em{{font-style:normal;font-size:11px;color:#7f8a91}}
.ctx{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}}
.sim{{border:1px dashed #2e3840;border-radius:16px;padding:16px;display:grid;gap:12px;justify-items:center}}
.sim>small{{color:#8f9aa4;font-size:12px}} .sim .dim{{color:#5f6b74}}
.paper-bg{{background:#efe8d5;border-color:#d8d0bc}} .paper-bg .sim{{border-color:#c9bfa5}} .paper-bg .sim>small{{color:#8a7f68}}
.paper-bg .sp-ico,.paper-bg .sim-choice,.paper-bg .sim-tabs .on{{color:#6b4f2a}}
.paper2{{background:#f5f0e2!important;color:#4a3f2d!important;border:0!important}}
.sim-tabs{{display:flex;gap:22px;color:#69747c}}
.sim-tabs span svg{{width:26px;height:26px;display:block}}
.sim-tabs span.on{{color:#c6ff45}}
.sim-choice{{width:76px;height:76px;border:3px solid #c6ff45;border-radius:50%;display:grid;place-items:center;color:#c6ff45}}
.sim-choice svg{{width:38px;height:38px}}
.sim-menu{{display:grid;grid-template-columns:repeat(2,64px);gap:10px}}
.sim-menu span{{display:grid;place-items:center;width:64px;height:64px;border-radius:50%;background:#222a30;color:#eef2f5}}
.sim-menu span:first-child{{color:#c6ff45;border:3px solid #c6ff45;background:transparent}}
.sim-menu svg{{width:30px;height:30px}}
svg.ic{{width:48px;height:48px}}
svg.pix{{image-rendering:pixelated}}
.miss{{color:#e8b93c;font-size:10px}}
/* G 配色 */
.theme{{display:grid;grid-template-columns:170px 1fr;gap:16px;align-items:center;margin-bottom:12px}}
.tname b{{font-size:14px;display:block}} .tname small{{color:#5f6b74;font-size:10.5px}}
.tchip{{border-radius:14px;padding:14px 18px;display:grid;gap:10px}}
.trow{{display:flex;gap:26px;align-items:center}}
.trow span svg{{width:26px;height:26px;display:block}}
/* H 手机端 */
.phone-grid{{display:grid;grid-template-columns:repeat(8,1fr);gap:10px}}
.ph-ic{{border:1px solid #262e35;border-radius:12px;background:#151b20;padding:12px 6px;display:grid;justify-items:center;gap:6px}}
.ph-ic svg{{width:24px;height:24px;color:#c6ff45}} .ph-ic b{{font-size:11px;color:#aab4bd;font-weight:500}}
.sim-phone{{width:min(320px,100%);border:1px solid #2e3840;border-radius:26px;background:#0b0f13;padding:14px;display:grid;gap:10px;margin:auto}}
.ph-top{{display:flex;align-items:center;gap:9px;color:#eef2f5;font-size:14px}}
.ph-top svg{{color:#c6ff45}} .ph-top b{{flex:1;text-align:left}}
.ph-card{{display:flex;align-items:center;gap:10px;border:1px solid #262e35;border-radius:13px;background:#151b20;padding:11px 12px;font-size:13px}}
.ph-card div{{flex:1;text-align:left}} .ph-card small{{display:block;color:#7f8a91;font-size:11px}}
.ph-cta{{border:0;border-radius:22px;background:#c6ff45;color:#11170a;font-weight:700;padding:12px;font-size:14px;display:flex;gap:8px;align-items:center;justify-content:center}}
.ph-check{{display:flex;gap:14px;color:#7f8a91;font-size:11.5px;align-items:center}}
.ph-check svg{{width:15px;height:15px;color:#c6ff45}}
svg.ic2{{width:17px;height:17px}} svg.ic3{{width:30px;height:30px;color:#c6ff45}}
@media(max-width:900px){{.sports{{grid-template-columns:repeat(2,1fr)}}.ctx{{grid-template-columns:1fr}}.phone-grid{{grid-template-columns:repeat(4,1fr)}}.theme{{grid-template-columns:1fr}}}}
</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
{''.join(symbols.values())}
<filter id="sketchy" x="-10%" y="-10%" width="120%" height="120%">
<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="3" seed="7" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/>
</filter>
</svg>
<h1>Teamo 运动图标 · 九组方案(A-I)</h1>
<p class="sub">四组<b>库选型</b>(A-D) + 五轮<b>风格扩展</b>(E 像素 / F 手绘 / G 配色 / H 手机端全套 / I 厚实 Duotone)。全部免费商用:Tabler=MIT · MingCute=Apache2.0 · Lucide=ISC · Iconoir=MIT · Phosphor=MIT · PixelartIcons=MIT · Material Symbols=Apache2.0。<b>回复编号或「E+G-2」这类组合都行</b>。</p>
<nav class="top">{nav}</nav>
<div class="note">说明:①「开合跳」所有库均无正解,各方案用近似人形并标注;②像素风动作图标为自绘 12×12(正是补缺口的思路);③手绘风是真实 SVG 滤镜处理,不是贴图;④跳绳只有 Tabler 有正解,别的方案都是近似。</div>
{''.join(blocks)}
</body></html>'''

out = r'D:/work/sportmate/prototype/icon-schemes.html'
open(out, 'w', encoding='utf-8').write(html)
print('written:', out, os.path.getsize(out), 'bytes, symbols:', len(symbols))

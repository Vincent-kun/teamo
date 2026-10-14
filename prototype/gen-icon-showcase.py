# -*- coding: utf-8 -*-
"""Teamo 图标方案库 v3:白底黑字 + 导航真切换(每方案一种画布风格) + 底部色球全局换色
修正 v2 问题:C 组跳绳误用心率/拉伸误用脚印 -> 自绘 Lucide 风格;G 配色死图 -> 色球交互;新增远距尺寸阶梯"""
import urllib.request, json, os

UA = {'User-Agent': 'Mozilla/5.0'}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=15).read().decode()

BATCH = {
    'tabler': 'jump-rope,barbell,stretching,stretching-2,run,heartbeat,trophy,settings,user,bell,send,calendar,clock,stopwatch,heart,flame,moon,circle-check,share,home,plus,chevron-right',
    'mingcute': 'squats-line,yoga-line,run-line,heartbeat-line,trophy-line,settings-6-line,squats-fill,yoga-fill,walk-fill',
    'lucide': 'dumbbell,trophy,settings,heart-pulse',
    'iconoir': 'running',
    'ph': 'heartbeat-duotone,barbell-duotone,trophy-duotone,gear-duotone',
    'pixelarticons': 'trophy,heart,human',
}
symbols = {}
for prefix, icons in BATCH.items():
    ok = False
    for attempt in range(4):
        try:
            data = json.loads(get(f'https://api.iconify.design/{prefix}.json?icons={icons}'))
            wd, hd = data.get('width', 24), data.get('height', 24)
            for name, info in data.get('icons', {}).items():
                w, h = info.get('width', wd), info.get('height', hd)
                symbols[f'{prefix}-{name}'] = f'<symbol id="{prefix}-{name}" viewBox="0 0 {w} {h}">{info["body"]}</symbol>'
            print(f'{prefix}: ok')
            ok = True
            break
        except Exception as e:
            print(f'{prefix}: attempt {attempt + 1} ERR {e}')
            __import__('time').sleep(2)
    if not ok:
        raise SystemExit(f'FATAL: {prefix} 下载失败,不生成缺图标的页面')

# ── 自绘补缺(行业无正解的图标) ──
def L(body):  # 24px stroke 风(Lucide/Tabler 通用语法)
    return ('<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            + body + '</g>')
symbols['self-jack-tabler'] = ('<symbol id="self-jack-tabler" viewBox="0 0 24 24">' + L(
    '<circle cx="12" cy="4" r="2"/><path d="M12 8v5"/>'
    '<path d="M12 8l-5.5-4.5"/><path d="M12 8l5.5-4.5"/>'
    '<path d="M12 13l-4.5 8"/><path d="M12 13l4.5 8"/>') + '</symbol>')
symbols['self-rope-lucide'] = ('<symbol id="self-rope-lucide" viewBox="0 0 24 24">' + L(
    '<path d="M4 21l2.2-2.2"/><path d="M20 21l-2.2-2.2"/>'
    '<path d="M6.2 18.8C6.2 11 9 5 12 5s5.8 6 5.8 13.8"/>') + '</symbol>')
symbols['self-jack-lucide'] = ('<symbol id="self-jack-lucide" viewBox="0 0 24 24">' + L(
    '<circle cx="12" cy="4" r="2"/><path d="M12 8v5"/>'
    '<path d="M12 8l-5.5-4.5"/><path d="M12 8l5.5-4.5"/>'
    '<path d="M12 13l-4.5 8"/><path d="M12 13l4.5 8"/>') + '</symbol>')
symbols['self-stretch-lucide'] = ('<symbol id="self-stretch-lucide" viewBox="0 0 24 24">' + L(
    '<circle cx="12" cy="4.5" r="2"/><path d="M12 6.5V14"/>'
    '<path d="M8.5 9.5L12 8l6.5-2.5"/>'
    '<path d="M12 14l-3.5 7"/><path d="M12 14l4 7"/>') + '</symbol>')

# ── 自绘 12x12 像素四件套 ──
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
for k, cells in PIX.items():
    rects = ''.join(f'<rect x="{x}" y="{y}" width="1" height="1" fill="currentColor"/>' for x, y in cells)
    symbols[f'pix-{k}'] = f'<symbol id="pix-{k}" viewBox="0 0 12 12">{rects}</symbol>'

def mk(name, size, sk=False):
    st = ''
    if name.startswith('pix:'):
        st += 'shape-rendering:crispEdges;image-rendering:pixelated;'
    if sk:
        st += 'filter:url(#sketchy);'
    a = f' style="{st}"' if st else ''
    return f'<svg width="{size}" height="{size}"{a}><use href="#{name.replace(":", "-")}"/></svg>'

NAMES = {'rope': '跳绳', 'jump': '开合跳', 'squat': '深蹲', 'stretch': '拉伸'}
HINTS = {'rope': '协调 · 心肺', 'jump': '全身 · 热身', 'squat': '下肢力量', 'stretch': '放松 · 柔韧'}

# src: (css类, 文案)  ok=正解黑 chip / self=自绘描边 chip / approx=近似灰 chip
OK, SELF_, APPROX = ('ok', '正解'), ('self', '自绘'), ('approx', '近似')

SCHEMES = [
 dict(k='A', name='Tabler 纯系线稿', lic='MIT', pos='1.5px 锐利线稿 · 细节最丰富',
      crit='专业但偏成人健身感,儿童亲和度是短板;深蹲只能借杠铃', canvas='', sk=False,
      sports=[('rope', 'tabler:jump-rope', OK, '正解 · 全场唯一库内跳绳'),
              ('jump', 'self-jack-tabler', SELF_, '自绘补缺 · 原误用跑步人形'),
              ('squat', 'tabler:barbell', APPROX, '近似 · 杠铃负重'),
              ('stretch', 'tabler:stretching-2', OK, '正解')],
      menu=[('tabler:heartbeat', '记录'), ('tabler:barbell', '力量'), ('tabler:trophy', '成就'), ('tabler:settings', '设置')]),
 dict(k='B', name='MingCute 圆润系', lic='Apache 2.0', pos='圆头线稿 · 儿童亲和感最强',
      crit='气质最贴 6-15 岁,跳绳需跨库借 Tabler,风格接缝要收口', canvas='', sk=False,
      sports=[('rope', 'tabler:jump-rope', OK, '正解 · 跨库借 Tabler'),
              ('jump', 'mingcute:run-line', APPROX, '近似 · 跑步人形'),
              ('squat', 'mingcute:squats-line', OK, '正解 · 深蹲人形'),
              ('stretch', 'mingcute:yoga-line', APPROX, '近似 · 瑜伽伸展')],
      menu=[('mingcute:heartbeat-line', '记录'), ('mingcute:squats-line', '力量'), ('mingcute:trophy-line', '成就'), ('mingcute:settings-6-line', '设置')]),
 dict(k='C', name='Lucide 极简几何', lic='ISC', pos='几乎全部自绘的极简实验(对照组)',
      crit='v2 错拿心率当跳绳、脚印当拉伸,已修正为自绘;语义全靠字形,风险最高', canvas='', sk=False,
      sports=[('rope', 'self-rope-lucide', SELF_, '自绘修正 · 原误用心率波形'),
              ('jump', 'self-jack-lucide', SELF_, '自绘补缺 · 原用站立人形'),
              ('squat', 'lucide:dumbbell', APPROX, '近似 · 哑铃'),
              ('stretch', 'self-stretch-lucide', SELF_, '自绘修正 · 原误用脚印')],
      menu=[('lucide:heart-pulse', '记录'), ('lucide:dumbbell', '力量'), ('lucide:trophy', '成就'), ('lucide:settings', '设置')]),
 dict(k='D', name='混合精选(务实推荐)', lic='MIT / Apache', pos='跨库取语义最准 · 同描边宽度保统一',
      crit='四个运动三个正解,落地最快;风格统一靠 2px 描边这条规矩吊着', canvas='', sk=False,
      sports=[('rope', 'tabler:jump-rope', OK, '正解'),
              ('jump', 'iconoir:running', APPROX, '近似 · 动作人形'),
              ('squat', 'mingcute:squats-line', OK, '正解 · 深蹲人形'),
              ('stretch', 'tabler:stretching', OK, '正解')],
      menu=[('tabler:heartbeat', '记录'), ('tabler:barbell', '力量'), ('tabler:trophy', '成就'), ('tabler:settings', '设置')]),
 dict(k='E', name='像素风(游戏感)', lic='自绘 + MIT', pos='12×12 自绘像素 · 菜单混搭 PixelartIcons',
      crit='证明了补缺口可以靠自绘;精细度封顶,只适合小尺寸场景', canvas='pix', sk=False,
      sports=[('rope', 'pix:rope', SELF_, '自绘 12×12'),
              ('jump', 'pix:jump', SELF_, '自绘 12×12'),
              ('squat', 'pix:squat', SELF_, '自绘 12×12'),
              ('stretch', 'pix:stretch', SELF_, '自绘 12×12')],
      menu=[('pixelarticons:heart', '记录'), ('pix:squat', '力量'), ('pixelarticons:trophy', '成就'), ('pixelarticons:human', '个人')]),
 dict(k='F', name='手绘涂鸦风', lic='MIT / Apache', pos='线稿 × feTurbulence 位移滤镜 · 蜡笔纸感',
      crit='独一份的纸感;低端芯片上滤镜开销未验证,可能得降级成静态抖动', canvas='paper', sk=True,
      sports=[('rope', 'tabler:jump-rope', OK, '正解'),
              ('jump', 'iconoir:running', APPROX, '近似'),
              ('squat', 'mingcute:squats-line', OK, '正解'),
              ('stretch', 'tabler:stretching', OK, '正解')],
      menu=[('tabler:heartbeat', '记录'), ('tabler:barbell', '力量'), ('tabler:trophy', '成就'), ('tabler:settings', '设置')]),
 dict(k='G', name='Duotone 厚实填充', lic='MIT / Apache', pos='Phosphor Duotone + MingCute Fill · 远距辨识度最好',
      crit='1.5m 余光扫视最稳;无跳绳正解,选定后要手绘 duotone 化', canvas='', sk=False,
      sports=[('rope', 'tabler:jump-rope', OK, '线稿正解 · duotone 无'),
              ('jump', 'mingcute:walk-fill', APPROX, '近似 · 动作人形'),
              ('squat', 'mingcute:squats-fill', OK, '正解填充版'),
              ('stretch', 'mingcute:yoga-fill', APPROX, '近似 · 瑜伽伸展')],
      menu=[('ph:heartbeat-duotone', '记录'), ('ph:barbell-duotone', '力量'), ('ph:trophy-duotone', '成就'), ('ph:gear-duotone', '设置')]),
]

def sp_card(key, icon, cls, txt, sk):
    return (f'<div class="sp"><div class="sp-main">{mk(icon, 64, sk)}</div>'
            f'<b>{NAMES[key]}</b><span class="src {cls}">{txt}</span>'
            f'<div class="ladder">{mk(icon, 32, sk)}{mk(icon, 20, sk)}<i>远距 64→32→20</i></div></div>')

def sim_device(sports, sk):
    tabs = ''.join(f'<span class="{"on" if i == 0 else ""}">{mk(n, 26, sk)}</span>' for i, (k, n, c, t) in enumerate(sports))
    return (f'<div class="sim"><small>设备端圆屏 · 选中态(黑屏为产品真实环境)</small>'
            f'<div class="screen"><div class="scr-tabs">{tabs}</div>'
            f'<div class="scr-main">{mk(sports[0][1], 38, sk)}</div>'
            f'<div class="scr-name">{NAMES[sports[0][0]]}</div></div></div>')

def sim_menu(menu, sk):
    cells = ''.join(f'<span class="{"on" if i == 0 else ""}">{mk(n, 28, sk)}</span>' for i, (n, l) in enumerate(menu))
    labs = ' · '.join(l for _, l in menu)
    return (f'<div class="sim"><small>Workout 菜单四宫格</small>'
            f'<div class="menu">{cells}</div><div class="menu-lab">{labs}</div></div>')

panels = []
for s in SCHEMES:
    cards = ''.join(sp_card(k, n, c, t, s['sk']) for k, n, c, t in s['sports'])
    panels.append(f'''<section class="panel" id="p{s['k']}">
<div class="p-head"><h2>{s['k']} · {s['name']}</h2><span class="lic">{s['lic']}</span><span class="p-pos">{s['pos']}</span></div>
<p class="p-crit"><b>锐评</b> · {s['crit']}</p>
<div class="canvas {s['canvas']}"><div class="sports">{cards}</div>
<div class="sim-row">{sim_device(s['sports'], s['sk'])}{sim_menu(s['menu'], s['sk'])}</div></div>
</section>''')

# ── H 手机端(特殊面板) ──
PHONE_ICONS = [('tabler:user','我的孩子'),('tabler:bell','通知'),('tabler:send','发送邀请'),('tabler:calendar','运动计划'),
 ('tabler:clock','时长'),('tabler:stopwatch','倒计时'),('tabler:heart','鼓励'),('tabler:trophy','成就'),
 ('tabler:flame','卡路里'),('tabler:moon','休息'),('tabler:circle-check','已完成'),('tabler:share','分享成绩'),
 ('tabler:home','首页'),('tabler:plus','添加'),('tabler:chevron-right','进入'),('tabler:settings','设置')]
phone_grid = ''.join(f'<div class="phi">{mk(n, 24)}<b>{l}</b></div>' for n, l in PHONE_ICONS)
phone_sim = f'''<div class="psim">
<div class="ps-top">{mk('tabler:user', 17)}<b>小宇的运动</b>{mk('tabler:bell', 17)}</div>
<div class="ps-card">{mk('tabler:jump-rope', 30)}<div><b>跳绳</b><small>协调 · 心肺</small></div>{mk('tabler:chevron-right', 17)}</div>
<div class="ps-card">{mk('mingcute:squats-line', 30)}<div><b>深蹲</b><small>下肢力量</small></div>{mk('tabler:chevron-right', 17)}</div>
<div class="ps-cta">{mk('tabler:send', 17)} 邀请运动</div>
<div class="ps-meta">{mk('tabler:circle-check', 15)} 已连接设备 {mk('tabler:clock', 15)} 08:24</div>
</div>'''
panels.append(f'''<section class="panel" id="pH">
<div class="p-head"><h2>H · 手机端全套(家长端)</h2><span class="lic">MIT</span><span class="p-pos">家长端 App 16 枚常用图标 + 真实界面模拟</span></div>
<p class="p-crit"><b>锐评</b> · 家长端是浅色 App,白底才是它的真实语境;风格应与设备端同源选定</p>
<div class="canvas phone"><div class="phone-grid">{phone_grid}</div>{phone_sim}</div>
</section>''')

tabs_html = ''.join(f'<button class="tab" data-k="{s["k"]}" onclick="go(\'{s["k"]}\',this)">{s["k"]} {s["name"].split("(")[0]}</button>' for s in SCHEMES)
tabs_html += '<button class="tab" data-k="H" onclick="go(\'H\',this)">H 手机端</button>'

COLORS = [('自动 · 跟随深浅', 'auto'), ('墨黑', '#111111'), ('荧光绿', '#9be800'), ('活力橙', '#ff8a00'), ('天空蓝', '#2f7bff'),
          ('糖果粉', '#ff5c8a'), ('葡萄紫', '#8a5cff'), ('薄荷青', '#00b3a4'), ('番茄红', '#e5484d')]
def dot_style(c):
    return 'background:linear-gradient(135deg,#111 50%,#eef2f5 50%)' if c == 'auto' else f'background:{c}'
dots = ''.join(f'<button class="dot{" on" if i == 0 else ""}" style="{dot_style(c)}" title="{n}" onclick="pick(this,\'{c}\')"></button>' for i, (n, c) in enumerate(COLORS))

CSS = """
:root{--acc:#111111;--accd:#eef2f5;
--bg:#fff;--ink:#111;--dim:#666;--faint:#999;--line:#eee;--card:#fff;--chip:#f3f4f5;--navbg:#fffffff2;
font-family:Inter,'Noto Sans SC',sans-serif}
html[data-theme=dark]{--bg:#0d1216;--ink:#eef2f5;--dim:#8f9aa4;--faint:#5f6b74;--line:#262e35;--card:#151b20;--chip:#222a30;--navbg:#0d1216f2}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);padding:0 0 120px;transition:background .25s,color .25s}
.hd{max-width:1180px;margin:0 auto;padding:34px 24px 8px}
.hd-row{display:flex;align-items:center;justify-content:space-between;gap:12px}
h1{font-size:24px;margin:0 0 6px}
h1 span{font-size:13px;color:var(--faint);font-weight:400}
.tbtn{border:1px solid var(--line);background:var(--card);color:var(--dim);border-radius:999px;padding:7px 16px;font-size:12.5px;cursor:pointer;white-space:nowrap}
.tbtn:hover{border-color:var(--ink);color:var(--ink)}
.sub{color:var(--dim);font-size:13px;line-height:1.9;margin:0}
.sub b{color:var(--ink)}
.fix{margin-top:12px;font-size:12px;color:var(--faint);border:1px dashed var(--line);border-radius:10px;padding:9px 14px;line-height:1.9}
.fix b{color:var(--ink)}
nav.tabs{position:sticky;top:0;z-index:20;background:var(--navbg);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);margin-top:18px}
nav.tabs .in{max-width:1180px;margin:0 auto;padding:10px 24px;display:flex;gap:8px;flex-wrap:wrap}
.tab{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:7px 16px;font-size:13px;cursor:pointer;color:var(--dim)}
.tab:hover{border-color:var(--ink);color:var(--ink)}
.tab.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
main{max-width:1180px;margin:0 auto;padding:26px 24px 0}
.panel{display:none}
.panel.show{display:block}
.p-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:6px}
.p-head h2{font-size:19px;margin:0}
.lic{font-size:10.5px;border:1px solid var(--line);border-radius:6px;padding:2px 7px;color:var(--dim)}
.p-pos{font-size:13px;color:var(--faint)}
.p-crit{margin:2px 0 18px;font-size:12.5px;color:var(--faint)}
.p-crit b{color:var(--ink);font-weight:600}
.canvas{border:1px solid var(--line);border-radius:20px;padding:24px;background:var(--card)}
.sports{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.sp{border:1px solid var(--line);border-radius:16px;padding:18px 10px 14px;display:grid;justify-items:center;gap:5px;text-align:center;background:var(--card)}
.sp-main{height:84px;display:grid;place-items:center;color:var(--acc)}
.sp b{font-size:14px}
.src{font-size:10.5px;padding:2px 8px;border-radius:6px}
.src.ok{background:var(--ink);color:var(--bg)}
.src.self{background:transparent;border:1px solid var(--ink);color:var(--ink)}
.src.approx{background:var(--chip);color:var(--faint)}
.ladder{display:flex;align-items:flex-end;gap:10px;color:var(--acc);margin-top:8px;padding-top:9px;border-top:1px dashed var(--line);width:100%;justify-content:center}
.ladder i{font-style:normal;font-size:9.5px;color:var(--faint);align-self:center}
.sim-row{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}
.sim{border:1px dashed var(--line);border-radius:16px;padding:18px;display:grid;gap:14px;justify-items:center;background:var(--card)}
.sim>small{color:var(--faint);font-size:12px}
.screen{background:#0d1216;border-radius:22px;padding:20px 26px;display:grid;gap:15px;justify-items:center;width:min(300px,100%)}
.scr-tabs{display:flex;gap:20px;color:#5b666e}
.scr-tabs .on{color:var(--accd)}
.scr-main{width:74px;height:74px;border:3px solid var(--accd);border-radius:50%;display:grid;place-items:center;color:var(--accd)}
.scr-name{color:#e8edf0;font-size:12px;letter-spacing:3px}
.menu{display:grid;grid-template-columns:repeat(2,66px);gap:10px}
.menu span{width:66px;height:66px;border-radius:50%;background:var(--chip);display:grid;place-items:center;color:var(--faint)}
.menu span.on{background:var(--card);border:2.5px solid var(--acc);color:var(--acc)}
.menu-lab{font-size:11px;color:var(--faint)}
.canvas.pix .sp{border:2px solid var(--ink);border-radius:4px;box-shadow:4px 4px 0 var(--ink);font-family:'Courier New',monospace}
.canvas.pix .sim{border:2px solid var(--ink);border-radius:4px;box-shadow:4px 4px 0 var(--ink)}
.canvas.pix .menu span{border-radius:4px}
.canvas.pix .scr-main{border-radius:4px}
.canvas.paper{background:#f8f3e6;--card:#fffdf4;--ink:#3a3226;--dim:#8a7f68;--faint:#a89a7d;--line:#e4d9bd;--chip:#f1e9d2}
.canvas.paper .sp{border-radius:14px 5px 16px 7px}
.canvas.phone{background:#f4f5f6;--card:#fff;--ink:#111;--dim:#666;--faint:#999;--line:#e6e7e8;--chip:#f3f4f5}
.phone-grid{display:grid;grid-template-columns:repeat(8,1fr);gap:10px}
.phi{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 6px;display:grid;justify-items:center;gap:6px;color:var(--acc)}
.phi b{font-size:11px;color:var(--dim);font-weight:500}
.psim{width:min(320px,100%);background:#fff;border:1px solid #e6e7e8;border-radius:28px;padding:16px;display:grid;gap:10px;margin:18px auto 2px;box-shadow:0 8px 30px rgba(0,0,0,.06);color:#111}
.ps-top{display:flex;align-items:center;gap:9px;font-size:14px}
.ps-top svg{color:var(--acc)}.ps-top b{flex:1}
.ps-card{display:flex;align-items:center;gap:10px;border:1px solid #eee;border-radius:14px;padding:11px 12px;font-size:13px}
.ps-card svg{color:var(--acc)}.ps-card div{flex:1}.ps-card small{display:block;color:#999;font-size:11px}
.ps-cta{background:#111;color:#fff;border-radius:22px;padding:12px;font-size:14px;font-weight:600;display:flex;gap:8px;align-items:center;justify-content:center}
.ps-cta svg{color:#fff}
.ps-meta{display:flex;gap:14px;color:#999;font-size:11.5px;align-items:center}
.ps-meta svg{color:var(--acc)}
.dock{position:fixed;left:0;right:0;bottom:0;z-index:30;background:var(--navbg);backdrop-filter:blur(8px);border-top:1px solid var(--line)}
.dock .in{max-width:1180px;margin:0 auto;padding:12px 24px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.dock .lab{font-size:12px;color:var(--faint)}
.dots{display:flex;gap:10px}
.dot{width:26px;height:26px;border-radius:50%;border:2px solid var(--bg);box-shadow:0 0 0 1px var(--line);cursor:pointer;padding:0}
.dot.on{box-shadow:0 0 0 2px var(--ink)}
.dock .cur{font-size:12px;color:var(--faint)}
body.embedded{padding-bottom:70px}
body.embedded .hd{display:none}
body.embedded main{padding-top:14px}
@media(max-width:900px){.sports{grid-template-columns:repeat(2,1fr)}.sim-row{grid-template-columns:1fr}.phone-grid{grid-template-columns:repeat(4,1fr)}}
"""

JS = """
var theme='light',sel='auto';
function autoColor(){return theme==='light'?'#111111':'#eef2f5'}
function applyAcc(c){document.documentElement.style.setProperty('--acc',c);document.documentElement.style.setProperty('--accd',c==='#111111'?'#eef2f5':c);document.getElementById('cur').textContent=(sel==='auto'?'自动 · ':'')+c}
function pick(el,c){sel=c;document.querySelectorAll('.dot').forEach(d=>d.classList.toggle('on',d===el));applyAcc(c==='auto'?autoColor():c)}
function toggleTheme(){theme=theme==='light'?'dark':'light';document.documentElement.dataset.theme=theme;document.getElementById('themeBtn').textContent=theme==='light'?'深色模式':'浅色模式';if(sel==='auto')applyAcc(autoColor())}
function go(k,el){document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('on',t===el));document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('show',p.id==='p'+k));window.scrollTo({top:0})}
if(new URLSearchParams(location.search).has('embedded'))document.body.classList.add('embedded');
document.querySelector('.tab').click();
"""

html = f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Teamo 图标方案库 v3</title><style>{CSS}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
{''.join(symbols.values())}
<filter id="sketchy" x="-10%" y="-10%" width="120%" height="120%">
<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="3" seed="7" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/>
</filter>
</svg>
<header class="hd">
<div class="hd-row"><h1>Teamo 图标方案库 <span>v3</span></h1><button class="tbtn" id="themeBtn" onclick="toggleTheme()">深色模式</button></div>
<p class="sub">点导航切换方案画布,底部色球全局换色,右上角切换深色/浅色。运动四件套 = 跳绳 / 开合跳 / 深蹲 / 拉伸;每卡带 <b>64→32→20</b> 远距递减与语义来源标注(<b>实心 chip=正解 · 描边 chip=自绘 · 灰 chip=近似</b>)。全部免费商用。</p>
<div class="fix"><b>v3 修正</b> · ① C 组跳绳误用心率波形、拉伸误用脚印 → 改为自绘 Lucide 风格正解;A 组开合跳误用跑步 → 自绘补缺。② 原 G 配色死图 → 升级为底部色球(全局实时换色,黑屏模拟同步;第一颗「自动」跟随深浅主题)。③ 新增远距尺寸阶梯。④ 画布随方案切换风格:E 像素硬阴影 / F 手绘纸感 / H 手机端浅灰。⑤ 深色/浅色双主题。旧版存 icon-schemes.html.bak-v2。</div>
</header>
<nav class="tabs"><div class="in">{tabs_html}</div></nav>
<main>{''.join(panels)}</main>
<div class="dock"><div class="in"><span class="lab">配色 · 点击色球全局换色</span><div class="dots">{dots}</div><span class="cur" id="cur">#111111</span></div></div>
<script>{JS}</script>
</body></html>'''

out = r'D:/work/sportmate/prototype/icon-schemes.html'
open(out, 'w', encoding='utf-8').write(html)
print('written:', out, os.path.getsize(out), 'bytes, symbols:', len(symbols))

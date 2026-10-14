# -*- coding: utf-8 -*-
"""往 live-demo 注入图标方案切换器:
- 抓所有方案的图标 + 自描 + 像素 + 手绘滤镜,做成 sprite 塞进 body
- 顶栏加 7 方案(A-G)切换按钮,点哪个就看到那套方案在实际圆屏 UI 的样子
- SPORTS.sym 改成 getter,渲染函数无需改动
- 同步 public/live-demo/ 副本"""
import urllib.request, json, re, shutil, os, sys, time

UA = {'User-Agent': 'Mozilla/5.0'}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=15).read().decode()

BATCH = {
    'tabler': 'jump-rope,barbell,stretching,stretching-2,run,heartbeat,trophy,settings',
    'mingcute': 'run-line,squats-line,yoga-line,heartbeat-line,trophy-line,settings-6-line,walk-fill,squats-fill,yoga-fill',
    'lucide': 'dumbbell,trophy,settings,heart-pulse',
    'iconoir': 'running',
    'ph': 'heartbeat-duotone,barbell-duotone,trophy-duotone,gear-duotone',
    'pixelarticons': 'heart,trophy,human',
}
symbols = {}
for prefix, icons in BATCH.items():
    for attempt in range(4):
        try:
            data = json.loads(get(f'https://api.iconify.design/{prefix}.json?icons={icons}'))
            wd, hd = data.get('width', 24), data.get('height', 24)
            for name, info in data.get('icons', {}).items():
                w, h = info.get('width', wd), info.get('height', hd)
                symbols[f'{prefix}-{name}'] = f'<symbol id="{prefix}-{name}" viewBox="0 0 {w} {h}">{info["body"]}</symbol>'
            print(f'{prefix}: ok ({len(data.get("icons",{}))} symbols)')
            break
        except Exception as e:
            print(f'{prefix}: attempt {attempt+1} ERR {e}')
            time.sleep(2)
    else:
        sys.exit(f'FATAL {prefix} download failed')

def L(body):
    return ('<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            + body + '</g>')

jack_paths = '<circle cx="12" cy="4" r="2"/><path d="M12 8v5"/><path d="M12 8l-5.5-4.5"/><path d="M12 8l5.5-4.5"/><path d="M12 13l-4.5 8"/><path d="M12 13l4.5 8"/>'
rope_paths = '<path d="M4 21l2.2-2.2"/><path d="M20 21l-2.2-2.2"/><path d="M6.2 18.8C6.2 11 9 5 12 5s5.8 6 5.8 13.8"/>'
stretch_paths = '<circle cx="12" cy="4.5" r="2"/><path d="M12 6.5V14"/><path d="M8.5 9.5L12 8l6.5-2.5"/><path d="M12 14l-3.5 7"/><path d="M12 14l4 7"/>'

extra = []
extra.append('<symbol id="self-jack-tabler" viewBox="0 0 24 24">' + L(jack_paths) + '</symbol>')
extra.append('<symbol id="self-jack-lucide" viewBox="0 0 24 24">' + L(jack_paths) + '</symbol>')
extra.append('<symbol id="self-rope-lucide" viewBox="0 0 24 24">' + L(rope_paths) + '</symbol>')
extra.append('<symbol id="self-stretch-lucide" viewBox="0 0 24 24">' + L(stretch_paths) + '</symbol>')

PIX = {
    'rope':  [(1,0),(2,0),(3,0),(8,0),(9,0),(10,0),(2,1),(9,1),(2,2),(9,2),(2,3),(9,3),
              (2,4),(9,4),(1,5),(10,5),(1,6),(10,6),(1,7),(10,7),(2,8),(9,8),(3,9),(8,9),
              (4,10),(5,10),(6,10),(7,10)],
    'jump':  [(5,0),(6,0),(5,1),(6,1),(2,0),(9,0),(3,1),(8,1),(4,2),(7,2),(5,2),(6,2),
              (5,3),(6,3),(5,4),(6,4),(4,5),(7,5),(3,6),(8,6),(3,7),(8,7),(2,2),(9,2),
              (2,9),(9,9),(1,10),(10,10)],
    'squat': [(6,1),(7,1),(6,2),(7,2),(5,3),(5,4),(4,5),(3,5),(3,5),(1,5),(4,6),(1,6),
              (4,7),(1,7),(4,8),(1,8),(4,9),(1,9),(0,10),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10)],
    'stretch':[(5,0),(6,0),(5,1),(6,1),(8,0),(7,1),(5,2),(6,2),(5,3),(6,3),(4,3),(3,4),
               (5,4),(6,4),(5,5),(6,5),(5,6),(6,6),(5,7),(6,7),(4,8),(7,8),(4,9),(7,9),(4,10),(7,10)],
}
for k, cells in PIX.items():
    rects = ''.join(f'<rect x="{x}" y="{y}" width="1" height="1" fill="currentColor"/>' for x, y in cells)
    extra.append(f'<symbol id="pix-{k}" viewBox="0 0 12 12">{rects}</symbol>')

sprite = ('<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">'
          + ''.join(symbols.values())
          + ''.join(extra)
          + '<filter id="sketchy" x="-10%" y="-10%" width="120%" height="120%">'
              '<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="3" seed="7" result="n"/>'
              '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/>'
            '</filter>'
          + '</svg>')
print('sprite symbols:', len(symbols) + len(extra))

# ── Schemes ──
SCHEMES_JS = r"""
const SCHEMES = {
 A: { sports:{rope:'tabler:jump-rope',jump:'self-jack-tabler',squat:'tabler:barbell',stretch:'tabler:stretching'}, sketch:false },
 B: { sports:{rope:'tabler:jump-rope',jump:'mingcute:run-line',squat:'mingcute:squats-line',stretch:'mingcute:yoga-line'}, sketch:false },
 C: { sports:{rope:'self-rope-lucide',jump:'self-jack-lucide',squat:'lucide:dumbbell',stretch:'self-stretch-lucide'}, sketch:false },
 D: { sports:{rope:'tabler:jump-rope',jump:'iconoir:running',squat:'mingcute:squats-line',stretch:'tabler:stretching'}, sketch:false },
 E: { sports:{rope:'pix:rope',jump:'pix:jump',squat:'pix:squat',stretch:'pix:stretch'}, sketch:false },
 F: { sports:{rope:'tabler:jump-rope',jump:'iconoir:running',squat:'mingcute:squats-line',stretch:'tabler:stretching'}, sketch:true },
 G: { sports:{rope:'tabler:jump-rope',jump:'mingcute:walk-fill',squat:'mingcute:squats-fill',stretch:'mingcute:yoga-fill'}, sketch:false },
};
let currentScheme = 'D';
function tIcon(name){
 const sid = name.replace(':','-');
 const isPix = name.startsWith('pix:');
 const sketch = SCHEMES[currentScheme].sketch;
 const st = (isPix?'shape-rendering:crispEdges;image-rendering:pixelated;':'') + (sketch?'filter:url(#sketchy);':'');
 const vb = isPix?'0 0 12 12':'0 0 24 24';
 const sz = isPix?44:null;
 const szAttr = sz?` width="${sz}" height="${sz}"`:'';
 return `<svg${szAttr} viewBox="${vb}" class="ui-icon" style="${st}"><use href="#${sid}"/></svg>`;
}
function applyScheme(k){
 if(!SCHEMES[k]) return;
 currentScheme = k;
 document.querySelectorAll('#schemePicker button').forEach(b=>b.classList.toggle('on',b.dataset.k===k));
 try{renderPhone();}catch(_){}
 try{renderDevice();}catch(_){}
}
document.getElementById('schemePicker').addEventListener('click', e=>{
 const b = e.target.closest('button'); if(b) applyScheme(b.dataset.k);
});
// 默认高亮 D
SPORTS.forEach(s=>Object.defineProperty(s,'sym',{get(){return sportIcon(s.id)}}));
const sportIcon=id=>tIcon(SCHEMES[currentScheme].sports[id]||SCHEMES[currentScheme].sports.rope);
""".strip('\n')

# ── Picker HTML ──
PICKER = ('<div class="scheme-picker" id="schemePicker" aria-label="图标方案切换">'
          '<span class="sp-label">方案</span>'
          '<button type="button" data-k="A">A Tabler</button>'
          '<button type="button" data-k="B">B MingCute</button>'
          '<button type="button" data-k="C">C Lucide</button>'
          '<button type="button" data-k="D" class="on">D 混合</button>'
          '<button type="button" data-k="E">E 像素</button>'
          '<button type="button" data-k="F">F 手绘</button>'
          '<button type="button" data-k="G">G Duotone</button>'
          '</div>')

# ── Picker CSS ──
PICKER_CSS = """
.scheme-picker{display:flex;align-items:center;gap:3px;border:1px solid #303941;border-radius:10px;padding:3px;background:#0c1115;max-width:100%}
.scheme-picker .sp-label{font-size:10px;color:#5e6a73;padding:0 6px 0 4px;letter-spacing:.5px;flex:none}
.scheme-picker button{border:0;background:transparent;color:#88939f;border-radius:7px;padding:5px 8px;font-size:11px;font-weight:600;letter-spacing:.2px;cursor:pointer;white-space:nowrap}
.scheme-picker button:hover:not(.on){background:#1a2126;color:#eef2f5}
.scheme-picker button.on{background:var(--accent);color:#101507}
"""

# ── Inject into live-demo ──
SRC = r'D:\work\sportmate\prototype\teamo-live-demo\index.html'
DST = r'D:\work\sportmate\prototype\teamo-ui-flow-html\public\live-demo\index.html'

s = open(SRC, encoding='utf-8').read()
print('source size before:', len(s))

# 1. Inject sprite after <body>
body_marker = '<body>\n'
if sprite.split('<svg')[1][:80] not in s:  # already injected?
 s = s.replace(body_marker, body_marker + sprite + '\n', 1)
 print('sprite injected')

# 2. Inject picker into topbar (after the .grow div)
s = s.replace('<div class="grow"></div>\n', '<div class="grow"></div>\n  ' + PICKER + '\n', 1)
print('picker injected')

# 3. Inject picker CSS before </style>
if '.scheme-picker{' not in s:
 s = s.replace('</style>', PICKER_CSS + '</style>', 1)
 print('picker css injected')

# 4. Replace sportIcon with scheme-driven version + applyScheme + picker listener
old_sportIcon = "const sportIcon=id=>({rope:IC.rope,jump:IC.jump,squat:IC.squat,stretch:IC.stretch}[id]||IC.rope);"
if old_sportIcon in s:
 s = s.replace(old_sportIcon, SCHEMES_JS)
 print('sportIcon replaced')
else:
 print('WARN sportIcon old form not found — already replaced?')

open(SRC, 'w', encoding='utf-8').write(s)
shutil.copy(SRC, DST)
print('synced to public/live-demo/index.html')
print('final size:', len(s))
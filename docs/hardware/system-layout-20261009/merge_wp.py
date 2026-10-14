# 集成脚本：把 2026-10-09 五个工作包（A/C/D/E/F）的候选合并进 components.json
# 规则：幂等（重跑不重复追加）；图片拷入本目录 assets 并按候选ID命名；先备份。
# 来源：docs/hardware/全品类补全_20261009/{A_摄像头,C_网络与天线,D_电源,E_声学与采集,F_连接器与结构}.json
import json, shutil, os
from pathlib import Path

root = Path(__file__).resolve().parent
wp = root.parent / '全品类补全_20261009'
backup = root / 'components.pre_wp_backup_20261009.json'

parts = json.loads((root / 'components.json').read_text(encoding='utf-8'))
if not backup.exists():
    shutil.copy2(root / 'components.json', backup)
    print('backup ->', backup.name)

WP_IDS = set()
def strip_wp(pool):
    global parts
    parts = [p for p in pool if p['id'] not in WP_IDS]

# 先记录所有将并入的 ID（含历史重跑残留），再清除
files = ['A_摄像头.json', 'C_网络与天线.json', 'D_电源.json',
         'E_声学与采集.json', 'F_连接器与结构.json']
for fn in files:
    d = json.loads((wp / fn).read_text(encoding='utf-8'))
    items = d['items'] if isinstance(d, dict) else d
    WP_IDS |= {r['id'] for r in items}
strip_wp(parts)
WP_IDS |= {'MR01', 'MR02', 'MR03'}
strip_wp(parts)

merged = []
for fn in files:
    d = json.loads((wp / fn).read_text(encoding='utf-8'))
    items = d['items'] if isinstance(d, dict) else d
    for r in items:
        rec = {
            'id': r['id'], 'category': r['category'], 'model': r['model'],
            'manufacturer': r.get('manufacturer'),
            'w': r.get('w'), 'h': r.get('h'), 't': r.get('t'),
            'url': r['url'], 'notes': r['notes'],
            'price': r.get('price', '国内含税报价/合作供应商/交期待核'),
            'photo_note': r.get('photo_note'),
            'sources': r.get('sources', []),
            'missing': r.get('missing', []),
        }
        ph = r.get('photo')
        if ph:
            src = wp / ph.replace('/', os.sep)
            if src.exists():
                dst = root / 'assets' / (r['id'] + src.suffix.lower())
                shutil.copy2(src, dst)
                rec['photo'] = 'assets/' + dst.name
            else:
                rec['photo'] = None
                rec['photo_note'] = '来源图片文件缺失：' + ph
        merged.append(rec)

# 主控三条架构路线（规范§3：开发板另列，M00–M04 保持不动）
arch = [
    {'id': 'MR01', 'model': '路线A：RV1106 芯片级自研整机PCB',
     'notes': 'Rockchip RV1106（具体后缀待涛哥确认）直接布自研主板：成本与体积潜力最优，但需自担 DDR/PMU/ISP/RF 参考设计、SDK 适配与 SMT 产线，EVT 风险最高；开发板阶段不采用，产品阶段二选一候选。证据：RV1106 开发平台辨认_20261009.md。',
     'url': 'https://www.rock-chips.com/a/en/products/RV11_Series/2023/0215/1698.html'},
    {'id': 'MR02', 'model': '路线B：Core1106 核心板 + 自研载板',
     'notes': 'Core1106（Core11061408/0408 见 M01/M02）作核心板，自研载板承接口：RAM/eMMC/电源复用厂家验证，载板只做外设（屏/相机/4G/音频/电池），MVP 主推路线；载板 42×55×10 为占位待布线验证。Core 板与载板的连接器选型见连接器与结构 CN 组。',
     'url': 'https://wiki.luckfox.com/zh/Luckfox-Core1106'},
    {'id': 'MR03', 'model': '路线C：成熟供应商开发板直接验证',
     'notes': 'Luckfox Pico Max / Ultra W（M03/M04）等整板直接用于 MVP 交互与算法验证，不进产品外形；优点是 SDK/例程最全、零硬件风险，缺点是尺寸与接口不匹配掌心形态，须与路线B并行推进。',
     'url': 'https://wiki.luckfox.com/'},
]
for a in arch:
    merged.append({'id': a['id'], 'category': '主控', 'model': a['model'],
                   'manufacturer': None, 'w': None, 'h': None, 't': None,
                   'url': a['url'], 'notes': a['notes'],
                   'price': '架构路线记录，非采购型号',
                   'photo': None, 'photo_note': '路线说明，无单件产品图',
                   'sources': [{'fact': 'RV1106 开发平台辨认与板型清单', 'url': '../rv1106-board-identification-20261009/index.html', 'date': '2026-10-09'}],
                   'missing': []})

order = ['主控', '摄像头', '联网', '天线', '显示屏', '电池', '充电与电源',
         '功放', '音频采集', '喇叭', '连接器与结构']
parts += merged
parts.sort(key=lambda p: (order.index(p['category']) if p['category'] in order else 99, p['id']))
(root / 'components.json').write_text(
    json.dumps(parts, ensure_ascii=False, indent=1), encoding='utf-8')

from collections import Counter
print('total', len(parts))
for k, v in Counter(p['category'] for p in parts).items():
    print(' ', k, v)
imgs = sum(1 for p in parts if p.get('photo'))
print('with photo:', imgs)

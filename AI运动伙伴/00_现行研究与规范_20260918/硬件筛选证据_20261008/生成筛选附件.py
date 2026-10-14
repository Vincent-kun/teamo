"""从选型工作稿提取CSV，并为官方机械证据生成下载清单。"""
from pathlib import Path
import csv
import hashlib
import json
import re

here = Path(__file__).resolve().parent
base = here.parent
source = base / '真实硬件候选与五套组合_20261008_V0.1.md'
headers = ['类别', '候选ID', '型号', '尺寸与规格', '接口与配置', '页面价格与库存',
           '筛选结论', '官方来源URL', '国内含税单价CNY', '国内库存', '最早到货',
           '选择或淘汰理由', '核查日期']
categories = {'M': '主控', 'D': '显示', 'C': '摄像头', 'N': '联网', 'B': '电池', 'A': '音频'}
rows = []
for line in source.read_text(encoding='utf-8').splitlines():
    if not re.match(r'^\| [MDCNBA]\d\d \|', line):
        continue
    cells = [s.strip() for s in line.strip().strip('|').split('|')]
    ident, model, dimensions = cells[:3]
    if ident[0] in 'MD':
        tech, price, result = cells[3:6]
    else:
        tech = ''
        price, result = cells[3:5]
    urls = '; '.join(dict.fromkeys(re.findall(r'\]\((https://[^)]+)\)', line)))
    clean = lambda s: s.replace('**', '').replace('`', '')
    rows.append([categories[ident[0]], ident, clean(model), clean(dimensions),
                 clean(tech), clean(price), clean(result), urls, '', '', '', '', '2026-10-08'])
assert len(rows) == 19, f'Expected 19 candidates, found {len(rows)}'
assert len({row[1] for row in rows}) == len(rows)
target = base / '真实硬件候选_20261008_V0.1.csv'
with target.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

downloads = {
    'Pico-Pro-size.jpg': 'https://www.luckfox.com/image/catalog/development-board/Luckfox-Pico-Pro/Luckfox-Pico-Pro-details-size.jpg',
    'Pico-Ultra-size.jpg': 'https://www.luckfox.com/image/catalog/development-board/Luckfox-Pico-Ultra/Luckfox-Pico-Ultra-details-size.jpg',
    'Core1106-size.jpg': 'https://www.luckfox.com/image/catalog/development-board/Core11061408/Core11061408-details-size.jpg',
    'MIS5001-B-size.jpg': 'https://www.luckfox.com/image/catalog/accBoard/MIS5001-5MP-Camera/MIS5001-5MP-Camera-details-size-B.jpg',
    'LCD169-Touch-drawing.pdf': 'https://files.waveshare.com/wiki/1.69inch-Touch-LCD-Module/1.69inch_Touch_LCD_Module_2D_Drawing.pdf',
    'LP503450-850mAh.pdf': 'https://www.lipolbattery.com/LiPo-Battery-Datahseet/LiPo_Battery_LP503450_3.7V_850mAh.pdf',
}
generated = {'LCD169-Touch-drawing.png': 'LCD169-Touch-drawing.pdf',
             'LP503450-850mAh.png': 'LP503450-850mAh.pdf'}
evidence = []
for name in [*downloads, *generated]:
    path = here / name
    if not path.exists():
        raise FileNotFoundError(path)
    blob = path.read_bytes()
    evidence.append({'file': name, 'source_url': downloads.get(name),
                     'rendered_from': generated.get(name),
                     'retrieved_date': '2026-10-08', 'bytes': len(blob),
                     'sha256': hashlib.sha256(blob).hexdigest()})
(here / '证据清单.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'{target.name}: {len(rows)} candidates; {len(evidence)} evidence files')

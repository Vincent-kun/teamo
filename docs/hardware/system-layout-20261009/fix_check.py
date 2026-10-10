from pathlib import Path
p=Path(__file__).resolve().parent
f=p/'verify.cjs';s=f.read_text(encoding='utf-8').replace("count()!==4)throw Error('battery filtered count')","count()!==6)throw Error('battery filtered count')");f.write_text(s,encoding='utf-8')
for f in [p/'build.py',p.parent/'battery-selection-20261009/build.py']:
 s=f.read_text(encoding='utf-8');s=s.replace("body=", "css+=' @media(max-width:700px){.page-head{flex-wrap:wrap}.page-head .primary{margin-top:4px}}'\nbody=",1) if 'body=' in s else s
 f.write_text(s,encoding='utf-8')

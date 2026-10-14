"""Render the pinned PRD Markdown to a self-contained, offline review page."""
from pathlib import Path
from html.parser import HTMLParser
import sys, os, re, hashlib, html, json

sys.path.insert(0,str(Path(os.environ['TEMP'])/'teamo-prd-html-deps'))
import markdown

root=Path(__file__).resolve().parents[1]
source=Path(sys.argv[sys.argv.index('--source')+1]) if '--source' in sys.argv else root/'docs/product/requirements/Teamo_Device_PRD_v1.0.0_Draft.md'
output=source.with_suffix('.html')
if output.exists() and '--refresh' not in sys.argv: raise RuntimeError('Output exists; refusing overwrite')
original=source.read_bytes(); text=source.read_text(encoding='utf-8')
# Legacy files have header/separator column mismatches. Normalize only the
# Markdown separator for rendering; source requirements and cells stay intact.
lines=text.splitlines()
for index,line in enumerate(lines):
 if index and re.fullmatch(r'\s*\|?[ :|\-]+\|?\s*',line) and '|' in line and lines[index-1].strip().startswith('|'):
  header=lines[index-1].strip().strip('|').split('|')
  delimiters=line.strip().strip('|').split('|')
  if len(header)!=len(delimiters):
   lines[index]='|'+'|'.join(delimiters[i].strip() if i<len(delimiters) else '---' for i in range(len(header)))+'|'
text='\n'.join(lines)
version=re.search(r'\| Current Version \| (v[\d.]+) \|',text)[1]
is_rtm='Traceability_Matrix' in source.name
title='Teamo 设备端需求追踪矩阵 RTM' if is_rtm else 'Teamo 设备端产品需求文档 PRD'
for token,label in [('Function_Specification','Teamo 设备端软件功能大纲'),('Feature_Specification','Teamo 设备端功能规格'),('Governance_Log','Teamo 设备端文档治理日志'),('Requirement_Baseline','Teamo 设备端需求基线'),('UE_IA','Teamo 设备端UE信息架构'),('UE_Engineering_Reference','Teamo 设备端UE工程参考')]:
 if token in source.name:title=label
md=markdown.Markdown(extensions=['tables','fenced_code','toc'],extension_configs={'toc':{'toc_depth':'1-3'}})
body=md.convert(text)
if 'Function_Specification' in source.name:
 # Function deep links and a visible jump into device binding.
 linked_functions=set()
 def function_anchor(match):
  fid=match[2]
  if fid in linked_functions:return match[0]
  linked_functions.add(fid)
  return match[1]+'<span id="function-'+fid.replace('.','-')+'">'+fid+'</span>'+match[3]
 body=re.sub(r'(<tr>\s*<td>)(\d+\.\d+\.\d+)(</td>)',function_anchor,body)
architecture='''<figure class="architecture" aria-label="产品职责关系，部署位置待确认"><div class="arch-row"><span>家长 APP / 小程序</span><b>⇄</b><span>平台<br><small>权限关系与统一服务</small></span><b>⇄</b><span>设备端<br><small>真实运动执行与记录</small></span></div><div class="arch-support">算法：审核规则与有效事件　→　设备端　←　硬件：输入输出与隐私状态</div><figcaption>平台传递任务、授权和已确认记录；设备维护真实运动事实。算法部署位置及硬件选型 TBD。</figcaption></figure>'''
body=re.sub(r'<pre><code class="language-mermaid">.*?</code></pre>',architecture,body,flags=re.S)
# Wrap every table for narrow screens, without changing cells or source text.
body=re.sub(r'(<table>.*?</table>)',r'<div class="table-scroll" tabindex="0">\1</div>',body,flags=re.S)
css='''
:root{color-scheme:light dark;background:Canvas;color:CanvasText;font-family:system-ui,"Microsoft YaHei",sans-serif;--line:color-mix(in srgb,CanvasText 22%,Canvas)}
*{box-sizing:border-box}body{margin:0;font-size:15px;line-height:1.8}a{color:inherit;text-decoration:underline;text-underline-offset:3px}a:focus-visible,button:focus-visible,[tabindex]:focus-visible{outline:2px solid GrayText;outline-offset:4px}
header{border-bottom:1px solid var(--line);padding:24px 32px}header h1{font-size:25px;margin:0 0 6px}header p{margin:4px 0}small,.meta{color:GrayText}button{font:inherit;color:ButtonText;background:ButtonFace;border:1px solid GrayText;border-radius:5px;padding:6px 14px;cursor:pointer}.actions{display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin-top:12px}
.layout{display:grid;grid-template-columns:270px minmax(0,1fr);max-width:1600px;margin:auto}nav{position:sticky;top:0;max-height:100vh;overflow:auto;padding:24px 18px;border-right:1px solid var(--line)}nav ul{list-style:none;padding-left:0}nav ul ul{padding-left:14px}nav li{margin:8px 0}nav a{font-size:13px;text-decoration:none}nav a:hover{text-decoration:underline}main{min-width:0;padding:24px 40px 64px}h1,h2,h3,h4,h5{line-height:1.5;scroll-margin-top:20px}main h1{font-size:27px;margin-top:40px}h2{font-size:24px;border-top:1px solid var(--line);padding-top:26px;margin-top:48px}h3{font-size:21px;margin-top:34px}h4{font-size:18px;margin-top:28px}h5{font-size:17px;margin-top:28px;border-left:3px solid GrayText;padding-left:12px}p{margin:12px 0}.table-scroll{overflow:auto;margin:16px 0}table{border-collapse:collapse;width:100%;font-size:14px;min-width:650px}th,td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}th{font-weight:650}blockquote{border-left:3px solid GrayText;margin:20px 0;padding:2px 16px}pre{overflow:auto;border:1px solid var(--line);padding:16px;white-space:pre}code{font-family:Consolas,monospace}details{border:1px solid var(--line);padding:12px 16px;margin:12px 0}summary{cursor:pointer;font-weight:600}figure{margin:20px 0;padding:20px;border:1px solid var(--line)}.arch-row{display:flex;gap:15px;align-items:center;justify-content:center;flex-wrap:wrap}.arch-row span{padding:14px 20px;border:1px solid GrayText;text-align:center}.arch-support{text-align:center;margin:20px 0 10px}figcaption{font-size:13px;color:GrayText}footer{border-top:1px solid var(--line);padding:18px 32px;font-size:12px;overflow-wrap:anywhere}
@media(max-width:850px){.layout{display:block}nav{position:static;max-height:320px;border-right:0;border-bottom:1px solid var(--line)}main{padding:18px}header{padding:18px}h2{font-size:21px}}
@media print{nav,.actions{display:none}.layout{display:block}main{padding:0}body{font-size:10pt;background:white;color:black}header{padding:0 0 12px}h2{break-before:page}h3,h4,h5{break-after:avoid}table{min-width:0;font-size:9pt}tr{break-inside:avoid}.table-scroll{overflow:visible}details{display:block}details>*{display:block}footer{font-size:8pt}a{text-decoration:none}}
'''
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Teamo 设备端 PRD v1.0 Draft · Review</title><style>'''+css+'''</style></head><body><header><h1>Teamo 设备端产品需求文档</h1><p>v1.0 Draft · 控制版本 v1.0.0 · Review · 2026-10-12</p><p class="meta">正式评审材料，未冻结。47项核心需求 · 20项候选 · 17项 OQ · 11项 UE-OQ</p><div class="actions"><button type="button" onclick="document.querySelectorAll('details').forEach(d=>d.open=true)">展开全部问题</button><button type="button" onclick="document.querySelectorAll('details').forEach(d=>d.open=false)">收起问题</button><button type="button" onclick="document.querySelectorAll('details').forEach(d=>d.open=true);window.print()">打印 / 保存 PDF</button><a href="'''+source.name+'''">Markdown 源文档</a></div></header><div class="layout"><nav aria-label="文档目录"><strong>评审目录</strong>'''+md.toc+'''</nav><main id="content">'''+body+'''</main></div><footer>从固定Markdown导出；内容状态与来源追踪不变。Markdown SHA256：'''+hashlib.sha256(original).hexdigest()+'''</footer></body></html>'''
page=page.replace('<title>Teamo 设备端 PRD v1.0 Draft · Review</title>','<title>'+title+' '+version+' · Review</title>').replace('<h1>Teamo 设备端产品需求文档</h1>','<h1>'+title+'</h1>').replace('v1.0 Draft · 控制版本 v1.0.0',version+' Draft · 控制版本 '+version)
if 'Function_Specification' in source.name:
 page=page.replace('正式评审材料，未冻结。47项核心需求 · 20项候选 · 17项 OQ · 11项 UE-OQ','功能大纲 · Review · 47项核心P0 / 20项候选 / 2项停用追溯；MVP演示仅三个动作已确认')
 page=page.replace('Markdown 源文档</a>','Markdown 源文档</a><a href="#function-7-2-3">设备绑定与儿童确认</a>')
output.write_text(page,encoding='utf-8',newline='\n')
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k=='id':self.ids.append(v)
   if k=='href':self.links.append(v)
c=Check();c.feed(page);bad=[]
for link in c.links:
 if link.startswith('#') and link[1:] not in c.ids:bad.append(link)
 elif not link.startswith(('#','http:','https:')) and not (output.parent/link.split('#')[0]).exists():bad.append(link)
assert not bad,bad
assert len(c.ids)==len(set(c.ids)), 'duplicate anchors'
assert source.read_bytes()==original
cards=len(re.findall(r'<h5\b[^>]*>Function ',page))
if '##### Function ' in text: assert cards==47
print(json.dumps({'output':str(output),'bytes':output.stat().st_size,'core_cards':cards,'toc_anchors':len(c.ids),'broken_links':bad,'markdown_unchanged':True,'external_runtime_dependencies':0},ensure_ascii=False))

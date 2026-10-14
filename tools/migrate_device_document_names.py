"""One-shot approved document governance migration; preserves historical files."""
from pathlib import Path
import hashlib, json, re, zipfile, html, urllib.parse
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / 'docs/product/requirements'
G = ROOT / 'docs/governance'
DATE = '2026-10-12'
BACK = G / 'backups/device-naming-migration-20261012'
M = {
 '设备端需求基线_评审稿_V0.1_20261010.md': 'Teamo_Device_Requirement_Baseline_v0.1.1.md',
 'Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.md': 'Teamo_Device_Function_Specification_v0.5.2.md',
 'Teamo_MVP_设备端UE信息架构_v0.3.1_20261012.md': 'Teamo_Device_UE_IA_v0.3.1.md',
 'Teamo_MVP_UE工程附录.md': 'Teamo_Device_UE_Engineering_Reference_v0.1.0.md',
 'Teamo_MVP_Device_PRD_v0.6_Draft.md': 'Teamo_Device_PRD_v0.6.0_Draft.md',
}
for old, new in list(M.items()):
 if (D / old.replace('.md', '.html')).exists():
  M[old.replace('.md', '.html')] = new.replace('.md', '.html')
ALT = 'Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.md.html'

def sha(b): return hashlib.sha256(b).hexdigest()
def write(p, t): p.write_text(t.replace('\r\n', '\n'), encoding='utf-8', newline='\n')
def replace_links(t):
 t=t.replace(ALT, '__PRESERVED_ALTERNATE_HTML__')
 # Only path tokens change; human-readable titles and historical version references stay.
 for old, new in sorted(M.items(), key=lambda x: -len(x[0])):
  for a, b in [(old, new), (urllib.parse.quote(old), urllib.parse.quote(new))]:
   t = t.replace(']('+a, ']('+b)
   t = re.sub(r'((?:href|src)=["\x27])'+re.escape(a), lambda m: m[1]+b, t)
 return t.replace('__PRESERVED_ALTERNATE_HTML__', ALT)

def control(dtype, version='v1.0.0', status='Review'):
 return f'''# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | {dtype} |
| Current Version | {version} |
| Status | {status} |
| Owner | 待确认（项目协调：魏子奇；不等同审批责任人） |
| Reviewer | 待指派 |
| Created Date | {DATE} |
| Last Updated | {DATE} |

'''

def end(version='v1.0.0', summary='新增设备端文档治理迁移记录与导航'):
 return f'''
# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| {version} | {DATE} | Codex（AI，执行用户指令） | Review | {summary} |

# Change Impact

- Section: 文件名称、引用路径、治理记录及导航。
- Before: 职责名称不一致，版本、日期及状态混入路径。
- After: 使用批准映射，保留历史及旧路径兼容入口；需求和编号不变。
- Risk: Low；完整原文件及SHA256见治理备份。
- Change Type: Document Governance Migration；不构成需求升级。

# Decision Log

本次无产品/架构决策。用户已批准命名迁移；文档仍为Draft/Review，不代表需求批准。
'''

class Links(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.ids=[]
 def handle_starttag(self, tag, attrs):
  for k,v in attrs:
   if k in ('href','src') and v: self.links.append(v)
   if k=='id' and v: self.ids.append(v)

def links(p, t):
 parser=Links(); parser.feed(t)
 if p.suffix=='.html': return parser.links
 # Balanced parentheses, including non-ASCII meeting filenames.
 out=parser.links[:]
 for m in re.finditer(r'\]\(',t):
  i=m.end(); j=i; depth=1
  while j<len(t) and depth:
   if t[j]=='(': depth+=1
   elif t[j]==')': depth-=1
   j+=1
  if depth==0: out.append(t[i:j-1].strip().strip('<>'))
 return out

def broken(files):
 result=[]; total=0
 for p in files:
  for raw in links(p,p.read_text(encoding='utf-8-sig')):
   u=urllib.parse.urlsplit(raw)
   if u.scheme or u.netloc or raw.startswith('data:'): continue
   total+=1
   target=(p.parent/urllib.parse.unquote(u.path)) if u.path else p
   if not target.exists(): result.append({'source':p.relative_to(ROOT).as_posix(),'link':raw,'kind':'missing file'})
   elif u.fragment and target.suffix=='.html':
    parser=Links(); parser.feed(target.read_text(encoding='utf-8-sig'))
    if urllib.parse.unquote(u.fragment) not in parser.ids:
     result.append({'source':p.relative_to(ROOT).as_posix(),'link':raw,'kind':'missing HTML anchor'})
 return total,result

def main():
 import sys
 resume='--resume' in sys.argv
 if (BACK.exists() or any((D/n).exists() for n in M.values())) and not resume: raise RuntimeError('Migration already exists; refusing overwrite')
 if resume:
  with zipfile.ZipFile(BACK/'originals.zip') as z: originals={ROOT/n:z.read(n) for n in z.namelist()}
  for p,b in originals.items(): p.write_bytes(b)
 else:
  originals={p:p.read_bytes() for p in D.iterdir() if p.is_file()}
  for p in [G/'DOCUMENT_REGISTER.md',G/'managed-documents.json']: originals[p]=p.read_bytes()
 before_count,before_broken=broken([p for p in originals if p.parent==D])
 if not resume:
  BACK.mkdir(parents=True)
  with zipfile.ZipFile(BACK/'originals.zip','w',zipfile.ZIP_DEFLATED) as z:
   for p,b in originals.items(): z.writestr(p.relative_to(ROOT).as_posix(),b)
  write(BACK/'sha256-before.json',json.dumps({p.relative_to(ROOT).as_posix():sha(b) for p,b in originals.items()},ensure_ascii=False,indent=2))
 change=G/'CHANGE-DEVICE-NAMING-MIGRATION-20261012.md'
 write(change,control('Document Governance Migration')+'# Approved Migration Plan\n\n用户于2026-10-12批准最终映射。先备份再迁移；文件治理修订不升级需求版本。PRD仅将v0.6 Draft规范表示为v0.6.0 / Draft。\n\n| Old Name | New Name |\n|---|---|\n'+''.join(f'| {o} | {n} |\n' for o,n in M.items())+'\n旧路径保留完整兼容快照及替代入口，支持历史深链接；不合并历史，不删除旧路径记录。外部既有引用保持，通过兼容入口可访问。'+end())
 rows=[]
 for old,new in M.items():
  p=D/old; b=originals[p]; t=b.decode('utf-8-sig').replace('\r\n','\n'); updated=replace_links(t)
  if old.endswith('.md'):
   if old=='Teamo_MVP_UE工程附录.md':
    updated=re.sub(r'^\|v0\.1\.0\|([^\n]+)\|$',lambda m:'| v0.1.0 | '+' | '.join(x.strip() for x in m[1].split('|'))+' |',updated,flags=re.M)
   if 'Device_PRD' in old:
    updated=updated.replace('| Current Version | v0.6 Draft |','| Current Version | v0.6.0 |').replace('| Status | Draft / Pending Review（未冻结） |','| Status | Draft |')
   # Append migration metadata without changing original business text or logs.
   version=re.search(r'_v(\d+\.\d+\.\d+)',new)[1]
   status='Draft' if 'PRD' in new else 'Review'
   if not re.search(r'^# Version History\s*$',updated,re.M):
    updated+='\n\n# Version History\n\n既有版本记录完整保留在正文。\n\n| Version | Date | Author | Status | Change Summary |\n|---|---|---|---|---|\n'+f'| v{version} | {DATE} | Codex（AI，执行用户指令） | {status} | Document Governance Migration：规范名称与引用；无需求修改，无版本升级 |\n'
   updated+='\n\n## Document Governance Migration — 2026-10-12\n\nChange Type: Document Governance Migration\n\n- Rename only（职责命名）；链接迁移及治理记录不改变需求。\n- No requirement modification；Function/PAGE/State/OQ/UE-OQ及历史保留。\n- 旧路径：`'+old+'`。\n- [迁移变更单](../../governance/CHANGE-DEVICE-NAMING-MIGRATION-20261012.md)。\n'
   for h in ['Document Control','Change Impact','Decision Log']:
    if not re.search(r'^# '+h+r'\s*$',updated,re.M):
     if h=='Document Control':
      updated=re.sub(r'^#{2,3} Document Control\s*$', '# Document Control',updated,flags=re.M)
      start=updated.index('# Document Control'); stop=updated.find('\n\n',updated.find('|',start))
      block=updated[start:stop]
      block=re.sub(r'^\|([^\n]+)\|$',lambda m:'| '+' | '.join(x.strip() for x in m[1].split('|'))+' |',block,flags=re.M)
      updated=updated[:start]+block+updated[stop:]
     else: updated+='\n# '+h+'\n\n本次仅命名、链接及治理记录迁移，无产品/架构决策；详见迁移变更单。\n'
  write(D/new,updated)
  # Keep the original bytes as a compatibility snapshot with an explicit successor notice.
  if p.suffix=='.md': alias='> **旧路径兼容快照（2026-10-12）**：后续维护请使用['+new+']('+new+')。下方保留迁移前正文及历史，不作为独立维护入口。\n\n'+t
  else:
   notice='<aside style="padding:1em;border:1px solid GrayText;color:CanvasText;background:Canvas">旧路径兼容快照；现行入口：<a style="color:inherit" href="'+html.escape(new)+'">'+html.escape(new)+'</a>。历史锚点保留。</aside>'
   alias=re.sub(r'(<body\b[^>]*>)',lambda m:m[1]+notice,t,count=1,flags=re.I)
   if alias==t: alias=notice+t
  write(p,alias)
  rows.append({'old':old,'new':new,'before':sha(b),'after':sha((D/new).read_bytes()),'alias_after':sha(p.read_bytes())})
 # Alternate HTML is materially different: preserve it, do not overwrite or merge it.
 p=D/ALT; t=originals[p].decode('utf-8-sig'); target='Teamo_Device_Function_Specification_v0.5.2.html'
 notice='<aside style="padding:1em;border:1px solid GrayText;color:CanvasText;background:Canvas">历史导出兼容快照；<a style="color:inherit" href="'+target+'">现行功能规格入口</a>。原内容保留。</aside>'
 write(p,re.sub(r'(<body\b[^>]*>)',lambda m:m[1]+notice,t,count=1,flags=re.I))
 readme=control('Device Requirements Navigation')+'''# Teamo Device Requirements

## Document Hierarchy

Requirement Baseline → Function Specification → UE IA → PRD → FR → TR。

这是细化和追踪路线，不是自动覆盖的权威顺序。产品边界与竞品规范按根AGENTS.md §4；既有整体PRD V3.0仍保留权威。设备端PRD为Draft，三/七动作、候选范围及工程细则仍待确认。

## Authority Rules

| 对象 | 维护依据 |
|---|---|
| Function ID / Priority / OQ | Function Specification；本轮不重新编号或裁决 |
| PAGE ID / User Flow / UE-OQ | UE IA |
| State Reference / Exception Reference | UE Engineering Reference；不是已批准实现枚举 |
| 需求追踪号 | Requirement Baseline；已有FR编号保留，不推断正式FR已冻结 |
| Test Evidence | 后续TR与实际测试记录；当前不得将TC-TBD或自检当作实机通过 |

## Current Entry

[本目录登记表](DOCUMENT_REGISTER.md)列出现行稿、历史文件和兼容路径；[全局登记表](../../governance/DOCUMENT_REGISTER.md)保持全项目治理入口。

## Naming and Maintenance

本次采用用户批准的Teamo_Device_<Document_Type>_vX.Y.Z命名；PRD特例保留_Draft。版本由Document Control管理，状态不代表批准。未来修改在登记入口内进行，不持续复制多份正文；如文件名需随版本迁移，须重新核对引用并保留兼容入口。历史快照不修改。
'''+end()
 write(D/'README.md',readme)
 local=control('Device Document Register')+'# Device Document Register\n\n## Current Documents\n\n| Document | Version | Status |\n|---|---|---|\n'
 for new in M.values():
  if new.endswith('.md'): local+=f'| [{new}]({new}) | v{re.search(r"_v(\d+\.\d+\.\d+)",new)[1]} | '+('Draft' if 'PRD' in new else 'Review')+' |\n'
 local+='\n## Historical Files\n\n'
 for p in originals:
  if p.parent==D and p.name not in M and p.name!=ALT: local+=f'- [{p.name}]({p.name})\n'
 local+='\n## Old Path Compatibility\n\n| Old Path | Successor |\n|---|---|\n'+''.join(f'| [{o}]({o}) | [{n}]({n}) |\n' for o,n in M.items())+f'| [{ALT}]({ALT}) | [{target}]({target}) |\n'+end()
 write(D/'DOCUMENT_REGISTER.md',local)
 reg=G/'DOCUMENT_REGISTER.md'; t=originals[reg].decode('utf-8-sig')
 for old,new in M.items(): t=t.replace(old,new)
 t=t.replace('本表登记本次治理范围，路径保持不变。','本表登记治理范围；设备端文档已按批准映射迁移，旧路径兼容快照保留。')
 # Refresh UE latest entry only in the family row, preserving historical links.
 lines=t.splitlines()
 for i,line in enumerate(lines):
  if line.startswith('| Teamo MVP设备端UE信息架构 |'):
   lines[i]='| Teamo MVP设备端UE信息架构 | [Teamo_Device_UE_IA_v0.3.1.md](../product/requirements/Teamo_Device_UE_IA_v0.3.1.md) | v0.1、v0.2、v0.3原位保留，详见[目录登记表](../product/requirements/DOCUMENT_REGISTER.md) | Review；不代表批准 |'
  if 'Teamo_Device_Function_Specification_v0.5.2.md' in line: lines[i]=lines[i].replace('| v0.5.1 |','| v0.5.2 |')
 t='\n'.join(lines)+'\n'
 t=t.replace('| Current Version | v1.0.0 |','| Current Version | v1.0.1 |',1)
 pos=t.index('\n# Decision Log')
 t=t[:pos]+f'\n| v1.0.1 | {DATE} | Codex（AI，执行用户指令） | Review | 同步设备端命名、UE v0.3.1入口、功能v0.5.2及目录登记；无需求变更 |\n'+t[pos:]
 t+='\n## Device Migration Register Update\n\n[设备端登记表](../product/requirements/DOCUMENT_REGISTER.md)；新增PRD、UE工程参考及UE v0.3.1现行入口。旧路径与历史原样备份可恢复；本次无产品/架构决策。\n\n| 文档 | 治理版本 | 提交状态 |\n|---|---|---|\n'
 for new in M.values():
  if new.endswith('.md') and ('UE_IA' in new or 'Engineering' in new or 'PRD' in new): t+=f'| [{new}](../product/requirements/{new}) | v{re.search(r"_v(\d+\.\d+\.\d+)",new)[1]} | '+('Draft' if 'PRD' in new else 'Review')+' |\n'
 write(reg,t)
 managed=json.loads(originals[G/'managed-documents.json'])
 for old,new in M.items():
  if old.endswith('.md'):
   a='docs/product/requirements/'+old; b='docs/product/requirements/'+new
   managed=[b if x==a else x for x in managed]
   if b not in managed: managed.append(b)
 for n in ['README.md','DOCUMENT_REGISTER.md']:
  managed.append('docs/product/requirements/'+n)
 write(G/'managed-documents.json',json.dumps(managed,ensure_ascii=False,indent=2)+'\n')
 after_count,after_broken=broken(list(D.iterdir()))
 historical=[p for p in originals if p.parent==D and p.name not in M and p.name!=ALT]
 assert all(p.read_bytes()==originals[p] for p in historical)
 # Business text equality verified after reversing the authorized path substitutions.
 invariants=[]
 for old,new in M.items():
  if not old.endswith('.md'): continue
  source=originals[D/old].decode('utf-8-sig').replace('\r\n','\n'); now=(D/new).read_text(encoding='utf-8')
  ids=lambda t:re.findall(r'\b(?:PAGE-\d+|(?:UE-)?OQ-\d+|FR-[A-Z]+-\d+|\d+\.\d+\.\d+|INIT|READY|COUNTDOWN|RUNNING|PAUSED|FINISHED|SAVED|SYNCING|SYNCED)\b',t)
  # All original business lines retained after approved governance normalization.
  expected=replace_links(source)
  if 'Device_PRD' in old: expected=expected.replace('| Current Version | v0.6 Draft |','| Current Version | v0.6.0 |').replace('| Status | Draft / Pending Review（未冻结） |','| Status | Draft |')
  normalize=lambda t:re.sub(r'^#{1,3} Document Control\s*$','# Document Control', re.sub(r'^\|([^\n]+)\|$',lambda m:'| '+' | '.join(x.strip() for x in m[1].split('|'))+' |',t,flags=re.M),flags=re.M)
  assert normalize(now).startswith(normalize(expected).rstrip())
  invariants.append({'file':new,'original_business_content_preserved':True})
 data={'mapping':rows,'historical_unchanged':[p.name for p in historical],'content_checks':invariants,'links_before':before_count,'links_after':after_count,'broken_before':before_broken,'broken_after':after_broken,'alternate_html_preserved':True,'all_original_file_hashes':[{'path':p.relative_to(ROOT).as_posix(),'before':sha(b),'after':sha(p.read_bytes())} for p,b in originals.items()]}
 write(G/'device-naming-migration-evidence.json',json.dumps(data,ensure_ascii=False,indent=2))
 report=control('Document Migration Report')+'# Migration Report\n\n## 1. Rename Summary\n\n迁移5份Markdown及3份HTML。旧路径保留完整兼容快照；另保留不同内容的.md.html历史导出。14个历史文件及整体PRD原字节保持。需求版本不升级；PRD v0.6 Draft仅规范为v0.6.0 / Draft。\n\n## 2. File Hash Before/After\n\nSHA256不同源于链接及治理元数据；不是需求变化。完整原文见[备份](backups/device-naming-migration-20261012/originals.zip)。\n\n| Old | New | SHA256 Before | SHA256 After |\n|---|---|---|---|\n'
 for row in rows: report+=f'| {row["old"]} | {row["new"]} | `{row["before"]}` | `{row["after"]}` |\n'
 report+=f'\n## 3. Link Migration Result\n\n规范文件路径引用已迁移。目录本地引用检查：迁移前{before_count}处，迁移后{after_count}处；HTML文件及显式锚点检查完成。旧HTML兼容快照保留全部原锚点，旧Markdown保留原正文与标题。外部引用未改写，继续经旧路径兼容入口访问。未验证远程链接或浏览器动态脚本。\n\n## 4. Broken Link Report\n\n迁移前：{len(before_broken)}处；迁移后：{len(after_broken)}处。详见[检查证据](device-naming-migration-evidence.json)。Markdown标题锚点未自动验收，采用正文标题原样保留策略。\n'
 for issue in after_broken: report+='\n- '+str(issue)+'\n'
 report+='\n## 5. Document Register Update\n\n全局登记表v1.0.0→v1.0.1（登记修订）；补充设备端目录README和REGISTER；managed-documents.json迁移路径并补登记现行文档。历史审计、变更单、保护目录不改写。\n\n## 6. Final Requirement Tree\n\n```text\ndocs/product/requirements/\n'+''.join('  '+p.name+'\n' for p in sorted(D.iterdir()))+'```\n'+end()
 write(G/'DEVICE_NAMING_MIGRATION_REPORT.md',report)
 print(json.dumps({'migrated':len(rows),'historical_unchanged':len(historical),'broken_before':len(before_broken),'broken_after':len(after_broken),'report':str(G/'DEVICE_NAMING_MIGRATION_REPORT.md')},ensure_ascii=False))

if __name__=='__main__': main()

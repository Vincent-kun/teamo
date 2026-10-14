"""Separate feature reading, traceability, and governance without changing IDs."""
from pathlib import Path
import re,json,zipfile,hashlib,subprocess,importlib.util
R=Path(__file__).resolve().parents[1];D=R/'docs/product/requirements';G=R/'docs/governance'
OLD=D/'Teamo_Device_Function_Specification_v0.5.2.md';NEW=D/'Teamo_Device_Feature_Specification_v0.6.0.md';RTM=D/'Teamo_Device_Requirement_Traceability_Matrix.md';LOG=G/'Teamo_Device_Governance_Log.md'
spec=importlib.util.spec_from_file_location('b',R/'tools/build_device_prd_review.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
def write(p,t):p.write_text(t,encoding='utf-8',newline='\n')
def main():
 if NEW.exists():raise RuntimeError('Output exists; refusing overwrite')
 old=OLD.read_text(encoding='utf-8');rtm=RTM.read_text(encoding='utf-8');paths=[OLD,OLD.with_suffix('.html'),RTM,RTM.with_suffix('.html'),D/'README.md',D/'DOCUMENT_REGISTER.md',G/'DOCUMENT_REGISTER.md',G/'managed-documents.json']
 back=G/'backups/feature-document-separation-20261012';back.mkdir(parents=True,exist_ok=False)
 with zipfile.ZipFile(back/'baseline.zip','w',zipfile.ZIP_DEFLATED) as z:
  for p in paths:z.write(p,p.relative_to(R).as_posix())
 write(back/'sha256.json',json.dumps({p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},ensure_ascii=False,indent=2))
 change=b.ctrl('Document Separation Change')+'''# Change Impact

- Before: 功能大纲包含功能正文、RTM映射、OQ展开、变更表、影响和决策记录。
- After: 功能规格v0.6.0只负责产品功能/业务评审；既有RTM维护映射；独立治理日志维护原问题、变更和决策；Excel为RTM的可筛选导出。
- Change Type: Minor（文档职责/结构重组）；47核心、20候选、2停用、原优先级与编号不变。
- Compatibility: 旧源文件保留完整快照和替代入口；旧HTML保留快照并转向当前预览。
- Risk: Medium；细节迁出后须核对完整保留，不以范围状态替代交付批准。
- Baseline: backups/feature-document-separation-20261012/baseline.zip及sha256.json。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录功能正文、RTM与治理日志拆分的影响和恢复基线 |

# Decision Log

无产品/架构决策；按用户Document Separation Rule执行职责隔离，不批准候选范围或修改动作规则。
'''
 write(G/'CHANGE-FEATURE-DOCUMENT-SEPARATION-20261012.md',change)
 biz=b.section(old,'## 1 设备','### 8.3 ');rows={x[0]:x for x in b.table_rows(biz) if len(x)==8 and re.fullmatch(r'\d+\.\d+\.\d+',x[0])};assert len(rows)==69
 modules={m[1]:m[2] for m in re.finditer(r'^## ([1-8]) (.+)$',biz,re.M)};subs={m[1]:m[2] for m in re.finditer(r'^### ([1-8]\.\d+) (.+)$',biz,re.M)}
 def natural(t):
  for id,row in sorted(rows.items(),key=lambda x:-len(x[0])):t=re.sub(r'(?<![\d.])'+re.escape(id)+r'(?![\d.])',row[1],t)
  for a,c in [('第3章','运动任务与执行模块'),('第4章','动作识别与计数模块'),('第5章','运动反馈模块'),('第6章','记录与同步模块')]:t=t.replace(a,c)
  return t
 text='# Teamo 设备端功能规格 v0.6\n\n'+b.ctrl('Feature Specification','v0.6.0')+'''## 产品定位

面向6–15岁儿童家庭运动。设备负责运动当下的交互、视觉识别、可信计数、角色反馈、本地记录与同步；家长管理任务、授权和结果；平台维护有效身份关系与统一服务。陪伴服务运动，不转为开放聊天或家庭视频监控。

## 功能范围

MVP演示已确定仅开合跳、深蹲起、高抬腿。七动作整体产品追踪保留，不删除其余动作。本文保持47项原P0 / Pending Review、20项已有细化功能优先级TBD、2项历史停用追溯；原P1后续候选也保持。范围状态与实现方案分开，功能列入正文不等于全部批准。

绑定、二维码、儿童切换、解绑等统一放在对应功能模块，不再单独藏在“补充提议”区。未获确认的功能在业务规则中明确范围/优先级待评审；二维码、输入方式、授权、目标范围和有效规则等待确认内容不擅自确定。

编号用于定位功能和评审讨论，沿用原号。完整追踪见附录A；原问题清单与变更记录分别见独立治理日志。本文不定义数据库字段、工程状态枚举、测试索引或具体性能阈值。

## 功能详细说明

'''
 lastmod=lastsub=None
 for fid,row in rows.items():
  if '已停用' in row[5]:continue
  mod=fid.split('.')[0];sub='.'.join(fid.split('.')[:2])
  if mod!=lastmod:text+=f'\n## {mod} {modules[mod]}\n';lastmod=mod
  if sub!=lastsub:text+=f'\n### {sub} {subs[sub]}\n';lastsub=sub
  text+=f'\n#### {fid} {row[1]}\n\n**功能目标**\n\n{row[3]}\n\n**使用场景**\n\n'+('本细化功能的范围仍待确认；若获准，家庭在'+row[1]+'环节使用。' if row[4]=='待确认' else '家庭在'+row[1]+'环节，需要获得明确、真实且可理解的操作结果。')+'\n\n**功能描述**\n\n'+natural(row[2])+'\n\n**用户流程**\n\n'
  if fid in b.DETAIL:
   inp,out,pre,exc,acc=b.DETAIL[fid]
   text+='```text\n'+natural(pre)+' → '+row[1]+' → '+natural(out)+'\n```\n\n**业务规则**\n\n- 优先级：'+row[4]+'；状态：'+row[5]+'（Pending Review）。\n- 行为归属：'+row[6]+'；具体人员待指定。\n- 前置：'+natural(pre)+'。\n- 待确认：'+row[7]+'。\n\n**异常处理**\n\n'+natural(exc)+'。\n\n**验收标准**\n\n'+natural(acc)+' 正式量化方法和实际测试用例仍待建立。\n'
  else:
   text+='```text\n范围获准且满足对应授权/业务条件 → '+row[1]+' → 表达真实处理结果\n```\n\n**业务规则**\n\n- 优先级：TBD；状态：Candidate / Pending Review；不默认承诺MVP交付。\n- 行为归属：'+row[6]+'；具体人员待指定。\n- 待确认：'+row[7]+'。\n\n**异常处理**\n\n具体失败、取消、返回和恢复条件待该功能范围评审后确定；不能绕过隐私/授权或伪造处理成功。\n\n**验收标准**\n\n范围与规则未确认，不能填入已批准验收值；若纳入，按上述功能描述与待确认结论形成可观察标准。\n'
 text+='''
## 业务状态模型

一次运动：目标与归属确认→准备→倒计时→运动→真实结束→保存→结果展示。暂停保留已确认努力，继续前重新检查隐私和准备；是否再次倒计时待确认。准备、倒计时与暂停不累计成绩。

执行、保存和同步是三个维度：运动结束不等于已保存，已保存不等于平台收到；可同时表达“提前结束 / 已保存 / 待同步”。上传/补传可在后台进行，不阻断允许的本地运动。首次绑定、儿童身份、网络及隐私各有独立事实，不能强行套成单一运动状态。

原始摄像帧不持久化，不进入记录、日志或缓存，不上传持久化。未授权、关闭、撤权或本地状态未知禁止采集；退出/结束停止采集。低置信度不作确定纠错，提前结束不伪称达标。不支持广告、儿童充值、陌生人社交、公开身体数据、医疗或视频监控。

## 跨端职责

'''
 cross=b.section(old,'## 12 跨端职责矩阵','### 12.1')
 for line in cross.splitlines()[1:]:
  if line.startswith('|'):text+=natural(line)+'\n'
 text+='\n算法提供审核规则与有效事件，硬件提供可用输入输出及真实隐私状态；具体方案、部署位置和人员待确认。设备不创建家长任务或管理云端账号关系，不擅自改变家长目标。\n'
 text+='''
## Open Questions（阅读摘要）

- 演示仅三动作已确认，整体七动作追踪如何衔接仍须后续明确。
- 运动有效规则、目标范围、高抬腿计数单位、多人/多儿童处理待确认。
- 绑定、联网先后关系、成功依据与失败恢复、实际输入和屏幕承载待确认。
- 说明跳过、暂停超时/恢复倒计时、保存/断电保证、补传契约待确认。
- 角色反馈深度、候选设置/独立辅助、数据删除责任与具体人员待确认。

完整原问题及关联不在正文重复，见[独立Open Question List](../../governance/Teamo_Device_Governance_Log.md#open-question-list)。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.6.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 将v0.5.4重组为独立功能规格，保留原功能号/优先级/未决项，迁出完整追踪及治理记录；无需求增删 |

## Appendix

- A：[Requirement Traceability Matrix](Teamo_Device_Requirement_Traceability_Matrix.md)。
- B：[Function-State Mapping](Teamo_Device_Requirement_Traceability_Matrix.md#feature-state-mapping)。
- C：[Change Log与完整历史](../../governance/Teamo_Device_Governance_Log.md)。

以下仅为治理入口指针，不承载正文或重复记录。

# Change Impact

[独立影响记录](../../governance/CHANGE-FEATURE-DOCUMENT-SEPARATION-20261012.md)。

# Decision Log

[独立治理日志](../../governance/Teamo_Device_Governance_Log.md)；本次无产品/架构决策。
'''
 write(NEW,text)
 # Preserve every source row in the RTM. The spreadsheet is generated from this same snapshot.
 pos=rtm.index('# Version History');part='\n## Feature Specification v0.6 — 完整源条目\n\n| 编号 | 功能点 | 功能描述 | 用户价值 | 优先级 | 状态 | 行为归属 | 待确认 |\n|---|---|---|---|---|---|---|---|\n'+''.join('| '+' | '.join(row)+' |\n' for row in rows.values())
 part+='\n<a id="feature-state-mapping"></a>\n\n## Feature-State Mapping\n\n'+b.section(old,'### 11.3','## 12 跨端职责矩阵')+b.section(old,'### 14.2','# Version History')
 rtm=rtm[:pos]+part+rtm[pos:];rtm=rtm.replace('| Current Version | v1.0.1 |','| Current Version | v1.1.0 |',1);pos=rtm.index('\n# Change Impact',rtm.index('# Version History'));rtm=rtm[:pos]+'\n| v1.1.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 接收功能规格原69项完整条目与功能状态/页面追踪，新增Excel同源导出；原PRD追踪保留 |\n'+rtm[pos:];rtm+='\n### Change Impact — Feature separation\n\n从功能大纲迁入机器追踪信息，功能与状态不变；[变更单](../../governance/CHANGE-FEATURE-DOCUMENT-SEPARATION-20261012.md)。\n';write(RTM,rtm)
 # Governing records remain verbatim, resolving links against their previous directory.
 original_governance=b.section(old,'## 13 Open Questions','### 14.2')+old[old.index('# Version History'):]
 original_governance=original_governance.replace('(../../governance/','(')
 original_governance=re.sub(r'\]\(([^)#]+\.md)(#[^)]*)?\)',lambda m:']('+('../product/requirements/' if not (G/m[1]).exists() and (D/m[1]).exists() else '')+m[1]+(m[2] or '')+')',original_governance)
 log='# Teamo 设备端文档治理日志\n\n'+b.ctrl('Project Documentation Governance')+'## 文档职责\n\n功能规格负责功能评审，RTM负责需求/功能/页面/状态/测试映射，本日志保存原问题、版本变化、影响和决策。原文历史仅迁入，不把AI整理当作审批。\n\n<a id="open-question-list"></a>\n\n## Open Question List及历史变更（原文迁入）\n\n'+original_governance+'\n## 最新分离记录\n\n'+change.replace('# Document Control','## 本次变更控制',1)
 # Use one canonical Version History for machine checking, retaining old headings as archived content.
 log=re.sub(r'^# Version History$', '## 原版本历史（迁入）',log,flags=re.M)
 log+='\n# Version History\n\n| Version | Date | Author | Status | Change Summary |\n|---|---|---|---|---|\n| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 集中迁入功能规格原问题、CH变更及版本/影响/决策材料，保留历史正文 |\n\n# Change Impact\n\n仅职责拆分与记录迁移；详见[变更单](CHANGE-FEATURE-DOCUMENT-SEPARATION-20261012.md)。\n\n# Decision Log\n\n本次无产品/架构决策；演示三动作的用户确认保持原决策，候选范围与规则仍待评审。\n';write(LOG,log)
 # Old Markdown is a complete recoverable compatibility snapshot, not a second maintained document.
 write(OLD,'> 旧路径兼容快照：当前评审入口为['+NEW.name+']('+NEW.name+')（v0.6.0）。下方保留v0.5.4全文与历史，后续不在此维护。\n\n'+old)
 for p in [D/'README.md',D/'DOCUMENT_REGISTER.md',G/'DOCUMENT_REGISTER.md']:
  s=p.read_text(encoding='utf-8');v=re.search(r'\| Current Version \| (v[\d.]+) \|',s)[1];ns=list(map(int,v[1:].split('.')));ns[2]+=1;nv='v'+'.'.join(map(str,ns));s=s.replace('| Current Version | '+v+' |','| Current Version | '+nv+' |',1)
  lines=s.splitlines()
  for i,l in enumerate(lines):
   if l.startswith('|') and OLD.name in l:l=l.replace(OLD.name,NEW.name).replace('| v0.5.4 |','| v0.6.0 |')
   if l.startswith('|') and RTM.name in l:l=l.replace('| v1.0.1 |','| v1.1.0 |')
   lines[i]=l
  s='\n'.join(lines)+'\n';start=s.index('# Version History');m=re.search(r'^# (?:Change Impact|Decision Log)',s[start+1:],re.M);pos=start+1+m.start();s=s[:pos]+f'\n| {nv} | 2026-10-12 | Codex（AI，执行用户指令） | Review | 登记独立Feature Specification v0.6.0、RTM及治理日志，保留旧入口快照 |\n'+s[pos:]
  prefix='' if p.parent==D else '../product/requirements/';gov='../../governance/' if p.parent==D else ''
  s+='\n## 文档类型隔离入口\n\n- [功能规格]('+prefix+NEW.name+')：PM/设计/研发阅读评审。\n- [RTM]('+prefix+RTM.name+')：内部追踪，Excel为同源导出。\n- [治理日志]('+gov+LOG.name+')：完整问题、变更、影响与决策。\n\n### Change Impact — 文档类型隔离\n\n入口重组，无需求/编号/优先级变化；旧路径保留。\n';write(p,s)
 managed=json.loads((G/'managed-documents.json').read_text(encoding='utf-8'));managed=[NEW.relative_to(R).as_posix() if x==OLD.relative_to(R).as_posix() else x for x in managed];managed.append(LOG.relative_to(R).as_posix());write(G/'managed-documents.json',json.dumps(managed,ensure_ascii=False,indent=2))
 traces=json.loads((G/'device-prd-review-evidence.json').read_text(encoding='utf-8'))['core_traceability'];traces={x['function']:x for x in traces}
 export=[]
 for fid,row in rows.items():
  tr=traces.get(fid,{});export.append(['、'.join(tr.get('baseline',[])) or 'TBD',row[1],fid,tr.get('page','TBD'),tr.get('state','TBD'),'TC-TBD',row[4],row[5],row[6],row[7],row[2]])
 write(R/'tools/feature-doc-separation-build/rtm-data.json',json.dumps(export,ensure_ascii=False,indent=2))
 assert all(row[2] in rtm and row[7] in rtm for row in rows.values())
 assert len(re.findall(r'^#### \d+\.\d+\.\d+ ',text,re.M))==67
 assert not re.search(r'\b(?:PAGE-\d+|TC-TBD|CH-\d+|OQ-\d+|UE-OQ-\d+)\b',text.split('# Version History')[0])
 for p in [NEW,RTM,LOG]:
  result=subprocess.run(['C:/Users/13896/.workbuddy/binaries/python/versions/3.13.12/python.exe',str(R/'tools/render_device_prd_html.py'),'--refresh','--source',str(p)],capture_output=True,text=True,encoding='utf-8');assert result.returncode==0,result.stderr
 # Old HTML contents remain as snapshot, but navigation goes to new human-facing page.
 oldhtml=OLD.with_suffix('.html').read_text(encoding='utf-8');oldhtml=oldhtml.replace('</head>','<script>location.replace('+json.dumps(NEW.with_suffix('.html').name)+'+location.hash)</script></head>',1);write(OLD.with_suffix('.html'),oldhtml)
 print(json.dumps({'feature':str(NEW),'rtm':str(RTM),'governance':str(LOG),'feature_cards':67,'all_function_ids':69},ensure_ascii=False))
if __name__=='__main__':main()

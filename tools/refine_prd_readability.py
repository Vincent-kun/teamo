"""Separate the human-facing PRD from its RTM without changing scope."""
from pathlib import Path
import json,re,zipfile,hashlib,subprocess,importlib.util

R=Path(__file__).resolve().parents[1];D=R/'docs/product/requirements';G=R/'docs/governance'
P=D/'Teamo_Device_PRD_v1.0.0_Draft.md';T=D/'Teamo_Device_Requirement_Traceability_Matrix.md';DATE='2026-10-12'
spec=importlib.util.spec_from_file_location('build',R/'tools/build_device_prd_review.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
def write(p,t):p.write_text(t,encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

PROFILES={
'1.1':('儿童或家长','上电、重启或回到日常使用','启动检查 → 读取可恢复事实 → 可用首页或恢复提示；无法确认时说明异常','首页说明设备是否可用；恢复只表达已确认进度，不自动继续运动。'),
'1.2':('家长或获授权维护人员','需要了解设备状态、故障、软件版本或执行必要重启','查看设备状态 → 理解可确认原因 → 按允许操作重试或重启 → 重新验证','设置中的必要设备状态和重启操作可理解；故障记录在后台处理，不新增诊断界面。'),
'2.1':('儿童','设备就绪，需要开始任务运动或自主运动','进入首页 → 查看任务或自主入口 → 选择运动 → 进入共用准备流程','首页同时呈现固定角色回应与运动入口；不要仅有表情而找不到任务和自主运动。'),
'2.2':('儿童；受限管理由家长参与','用户选择、开始、取消、暂停、继续、结束或返回','提出操作 → 系统判断是否允许 → 告知是否接受 → 呈现真实执行结果','反馈区分操作被接受与实际执行成功；不能确认时说明状态，而不是假称完成。'),
'3.1':('儿童和家长','家长任务送达，或儿童选择自主动作与目标','任务：检查 → 保存 → 回执 → 查看并确认；自主：选择支持动作和允许目标 → 确认','任务展示动作、目标、来源和执行状态；自主入口说明支持动作和允许目标。列表/详情是否分屏仍待确认。'),
'3.2':('儿童','已明确有效动作、目标和儿童归属，需要开始运动','查看审核动作说明 → 隐私与站位检查 → 准备满足 → 明确开始 → 倒计时 → 复核后运动','准备页面给一个主要调整原因；倒计时说明开始时机及取消结果；不默认视频预览或骨架。'),
'3.3':('儿童','主动暂停、识别异常需暂停、恢复、达标或提前结束','暂停并保留成绩 → 选择继续 → 重新准备后恢复；或选择结束 → 保存真实结果','运动页表达暂停原因、已有成绩及继续/结束操作；继续回准备检查，不能直接恢复计数。'),
'4.1':('儿童','准备或运动中需要确认画面可用性与有效动作','检测人体/画面 → 输出可用状态 → 按审核规则确认完整事件 → 累计有效次数或说明异常','准备阶段给站位原因；运动阶段表达可信次数和主要识别原因，不把低置信度当确定纠错。'),
'4.2':('儿童','进入当前支持动作的运动环节','完成动作完整周期 → 按审核规则判定 → 输出有效事件 → 共用计数反馈','运动页面使用同一计数依据，不为不同动作另建成绩系统；目标和实际结果的计数单位保持一致。'),
'5.1':('儿童','运动中查看进度、需要调整，或运动真实结束','查看真实进度 → 得到必要短提示 → 完成或提前结束 → 获得相应鼓励','数字、语音及固定角色回应基于同一真实状态；结束鼓励区分达标和提前结束。'),
'5.2':('儿童；家长在家长端查看记录','运动结束，需要知道成绩、保存与送达状态','查看真实结果 → 理解已保存或保存失败 → 查看独立同步状态 → 返回首页','结果展示动作、目标、实际次数、用时和结束原因；保存、同步分别表达，不把发送成功称家长已收到。'),
'6.1':('儿童和家长','一次运动需要形成可追溯的真实结果','明确儿童和来源 → 沿用唯一记录 → 汇总已确认事实 → 交给本地保存','记录为后台事实，运动和结果页面消费同一内容；页面返回不能重新生成同一结果。'),
'6.2':('儿童和家长','任务或结果需要本地保存，或设备重启需恢复','保存必要任务/结果 → 成功确认；失败说明并保留可恢复结果重试；重启只恢复可确认事实','首页、任务、运动和结果页面使用真实保存/恢复事实；保存失败的实际承载与退出规则待确认。'),
'6.3':('家长；儿童可理解必要状态','已保存结果需送达平台，或先前上传未获确认','上传同一已保存记录 → 等待业务确认 → 确认已同步；失败按契约沿用原标识补传','结果页和首页表达必要同步状态；后台处理不阻断已允许的本地运动。'),
'7.1':('家长和儿童','首次联网、网络断开或连接恢复','按获准流程配置 → 理解在线/离线状态 → 使用允许本地能力 → 恢复连接后按契约补传','绑定引导、设置与首页呈现必要连接状态，不默认增加专门网络诊断工具。'),
'7.2':('家长和儿童','需要确认有效绑定、当前儿童和必要设备状态','读取有效上下文 → 明确当前儿童 → 关联任务与成绩；必要设备状态独立同步','首次使用和必要设置承载儿童确认；设备状态同步为后台支撑，不承诺新增页面。'),
'8.1':('儿童和家长','准备、运动、退出或授权变化影响摄像头使用','检查授权和本地状态 → 允许才采集 → 展示真实状态 → 退出/撤权停止 → 恢复后重新检查','准备、倒计时、运动及隐私设置可理解真实采集状态；远程任务无法绕过本地关闭。'),
'8.2':('家长；儿童接收必要提醒','需要限制设备数据访问、请求清理或按策略接收提醒','校验有效管理权限 → 执行规定本地操作 → 回执；提醒按已设时段与频率输出','本地清理与云端账号处理分别说明；设备设置入口和提醒策略设置责任端仍待确认。')}

def main():
 import sys
 resume='--resume' in sys.argv
 if T.exists() and not resume:raise RuntimeError('RTM exists; refusing overwrite')
 if resume:
  with zipfile.ZipFile(G/'backups/prd-readability-20261012/baseline.zip') as z:
   for n in z.namelist():(R/n).write_bytes(z.read(n))
 old=P.read_text(encoding='utf-8');F=(D/b.NAMES[1]).read_text(encoding='utf-8');U=(D/b.NAMES[2]).read_text(encoding='utf-8');E=(D/b.NAMES[3]).read_text(encoding='utf-8')
 evidence=json.loads((G/'device-prd-review-evidence.json').read_text(encoding='utf-8'))
 business=b.section(F,'## 1 设备','### 8.3 ')
 rows={x[0]:x for x in b.table_rows(business) if len(x)==8 and re.fullmatch(r'\d+\.\d+\.\d+',x[0])}
 core={k:v for k,v in rows.items() if v[4]=='P0'};candidate={k:v for k,v in rows.items() if v[4]=='待确认'};retired={k:v for k,v in rows.items() if '已停用' in v[5]}
 assert (len(core),len(candidate),len(retired))==(47,20,2)
 modules={m[1]:m[2] for m in re.finditer(r'^## ([1-8]) (.+)$',business,re.M)}
 subs={m[1]:m[2] for m in re.finditer(r'^### ([1-8]\.\d+) (.+)$',business,re.M) if m[1] in PROFILES}
 pages={'00':'绑定与首次使用','01':'首页','02':'自主运动入口','03':'家长任务','04':'运动准备','05':'倒计时','06':'运动中','07':'运动结果','08':'设置','09':'候选动作辅助检测'}
 def readable(t):
  for oldchapter,newname in [('第3章','运动任务与执行模块'),('第4章','动作识别与计数模块'),('第5章','运动反馈与结果模块'),('第6章','运动记录与同步模块'),('第8章','隐私控制与数据管理模块')]: t=t.replace(oldchapter,newname)
  # Translate internal references to business names, without altering OQ/UE-OQ IDs.
  t=re.sub(r'PAGE-(\d{2})[–-](\d{2})',lambda m:'、'.join(pages[f'{i:02}'] for i in range(int(m[1]),int(m[2])+1)),t)
  t=re.sub(r'PAGE-(\d{2})(?:/\d{2})+',lambda m:'、'.join(pages[x] for x in re.findall(r'\d{2}',m[0])),t)
  t=re.sub(r'PAGE-(\d{2})',lambda m:pages[m[1]],t)
  for fid,row in sorted(rows.items(),key=lambda kv:-len(kv[0])):
   t=re.sub(r'(?<![\d.])'+re.escape(fid)+r'(?![\d.])',row[1],t)
  state={'INIT':'目标与归属确认','READY':'运动准备','COUNTDOWN':'倒计时','RUNNING':'运动中','PAUSED':'暂停','FINISHED':'运动结束','SAVED':'本地已保存','SYNCING':'同步中','SYNCED':'平台已确认接收'}
  for k,v in state.items():t=re.sub(r'\b'+k+r'\b',v,t)
  t=re.sub(r'FR-[A-Z]+-\d+','已有基线需求',t);t=t.replace('TC-TBD','正式测试用例待建立').replace('Function ID','内部功能编号').replace('PAGE ID','页面编号')
  t=re.sub(r'(?<![\d.])(?:[1-8]\.\d+)(?![\d.])',lambda m:subs.get(m[0],m[0]),t)
  return t
 changed=[P,P.with_suffix('.html'),D/'README.md',D/'DOCUMENT_REGISTER.md',G/'DOCUMENT_REGISTER.md',G/'managed-documents.json']
 backup=G/'backups/prd-readability-20261012'
 if not resume:
  backup.mkdir(parents=True,exist_ok=False)
  with zipfile.ZipFile(backup/'baseline.zip','w',zipfile.ZIP_DEFLATED) as z:
   for p in changed:z.write(p,p.relative_to(R).as_posix())
  write(backup/'sha256.json',json.dumps({p.relative_to(R).as_posix():sha(p) for p in changed},ensure_ascii=False,indent=2))
 sources={n:sha(D/n) for n in b.NAMES}
 change=b.ctrl('PRD Readability Change')+'''# Change Impact

- Section: PRD正文与独立RTM、HTML及登记导航。
- Before: 47张需求卡在正文重复Function/PAGE/State/Test引用，影响人类阅读。
- After: 正文以18个二级业务模块呈现场景、目标、流程、页面、规则、异常和验收；原47张详细卡与69项映射进入独立RTM，保留原问题编号与状态。
- Change Type: Minor（v1.0.0→v1.1.0，文档结构重组）；不新增/删除需求或更改优先级。
- Compatibility: PRD既有Markdown/HTML路径保持；控制版本更新为v1.1.0，文件名版次为历史路径标识。旧HTML锚点兼容保留。
- Risk: Medium；移出追踪可能导致信息遗漏，需核对47核心、20候选、2停用与全部原待确认事项。
- Baseline: backups/prd-readability-20261012/baseline.zip及sha256.json。
- Source: 用户本次可读性/RTM分离规则；四份需求来源不变。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录正文重组、追踪迁出、兼容路径、备份和验证计划 |

# Decision Log

无产品/架构决策；只改变文档呈现和追踪组织。TBD、候选和OQ/UE-OQ不转为批准内容。
'''
 write(G/'CHANGE-PRD-READABILITY-20261012.md',change)
 intro='''# Teamo 设备端产品需求文档 PRD v1.1 Draft

> 面向产品、设计、开发与测试的正式评审材料。Status Review，未冻结。本文先说明家庭如何使用设备以及设备如何回应；内部编号、逐项来源和测试关联见独立RTM。

'''+b.ctrl('Product Requirements Document','v1.1.0')+'''## 阅读导航

先看产品范围与四条核心流程，再读功能模块和异常；评审问题用于形成结论。功能模块均按“目标→场景→描述→流程→页面→规则→异常→验收”展开。完整内部编号与原逐项需求卡已移入[需求追踪矩阵](Teamo_Device_Requirement_Traceability_Matrix.md)，不在正文重复。

本次按稳定入口更新，文件名中的v1.0.0是历史路径标识；实际控制版本以Document Control和Version History为准。四份输入及其版本不变，旧内容完整备份可恢复。

## 输入与评审状态

'''
 intro+='| 输入 | 版本 | 作用 |\n|---|---|---|\n'+''.join(f'| [{label}]({name}) | {version} | {role} |\n' for label,name,version,role in zip(['设备端需求基线','功能规格说明','UE信息架构','UE工程参考'],b.NAMES,['v0.1.1','v0.5.2','v0.3.1','v0.1.0'],['定位、边界、通用原则','功能与优先级的唯一依据','用户旅程、页面与展示状态','详细状态、异常与边界参考']))
 intro+='''
文中的业务要求继承上述输入，全部保持Pending Review。验收条件是供评审的可观察业务标准；实际方法、阈值、时限、数据集及测试用例待确认。候选不会因为写入PRD成为交付承诺。来源章节和逐项对应保留在RTM。

## 1. 产品概述

### 1.1 产品定位

Teamo服务6–15岁儿童的家庭运动。儿童通过明确目标、视觉识别、可信计数和适度角色回应，开始、完成并再次运动；家长管理任务、权限和结果。设备负责运动发生时的操作、识别、反馈、保存及同步，陪伴服务运动。

### 1.2 产品目标

儿童能理解要做什么、如何开始、为什么暂停和结果是否真实；家长能理解任务是否送达、运动实际完成多少、记录是否保存和收到。暂停保留已完成努力，提前结束也保留真实结果，不伪称达标。

### 1.3 MVP范围

| 范围层级 | 内容 | 状态 |
|---|---|---|
| 核心及必要支撑 | 47项原P0：启动、任务/自主入口、准备、计数、反馈、保存/同步、网络/身份和隐私 | Pending Review；不调整优先级 |
| 历史细化候选 | 20项既有提议，含摘要、二维码、声音、出厂恢复、独立辅助等 | Candidate / Pending Review / 优先级TBD；不默认开放 |
| 原后续候选 | 更多动作、运动训练建议、个性化成长、内容与语音陪练 | P1 / Pending Review；不作为本轮默认交付 |
| 其他既有追踪 | 学校授权任务、独立体态观察、OTA和远程诊断 | 本轮范围与优先级TBD |
| 历史停用 | 2项原重复通信/视频保存编号保留追溯 | 详细去向见RTM，不重复实现 |

当前功能规格列开合跳、深蹲起、高抬腿三动作提议；需求基线保留七动作口径。三动作是演示切片还是产品范围仍待评审，不能宣称其他动作已删除或本轮已支持。保持动作“累计有效保持秒数”的上游口径保留为范围条件，不能用运动总用时冒充成绩，也不因此新增当前三动作功能。

### 1.4 非目标范围

不发展为开放聊天、家庭视频监控、陌生人社交或全站公开排行；不新增医疗分析、身体评价、姿态评分、成长等级或未经确认的AI能力。不加入广告、儿童充值或公开身体数据。学校授权小范围分享单独保留评审，基础运动星/个人最好成绩的深度待确认，不扩展成长体系。

## 2. 用户与场景

### 2.1 用户角色

| 角色 | 使用目的 | 职责边界 |
|---|---|---|
| 儿童 | 选择/确认运动、准备、明确开始、运动、暂停/继续/结束、查看真实结果 | 不承担家长账号管理；输入方式和实体屏幕承载待确认 |
| 家长 | 创建任务、绑定与授权、确认儿童、查看记录、发起受限数据操作 | 不远程绕过设备本地隐私关闭；APP/小程序形态待确认 |

### 2.2 核心使用场景

首次使用时完成必要家庭与儿童上下文；日常既可自主选择支持动作和允许目标，也可查看家长任务后明确开始。运动中可暂停并保留进度，继续前重新检查；结束后看到真实成绩，保存与同步分别确认。断网时继续允许的本地运动，不假称新任务已送达。

## 3. 产品架构与职责

```text
家长 APP / 小程序 ⇄ 平台 ⇄ 设备端
                             ↑
               算法有效事件 + 硬件可用输入输出与隐私状态
```

| 参与方 | 产品职责 | 仍待确认的实现 |
|---|---|---|
| 设备端 | 维护真实会话、操作、成绩、记录、本地守卫及同步 | 不自行改家长目标或创建云端账号关系 |
| 家长端 | 家长管理任务、授权、绑定/儿童和已确认记录 | 不独立递增次数，不强制开启采集 |
| 平台 | 权限/关系管理、任务投递、真实回执、结果业务确认与去重 | 接口与确认契约待确认，发送不等于送达 |
| 算法 | 画面/动作事实、审核规则与有效性证据 | 部署位置、模型和阈值待确认，不放宽离线与隐私边界 |
| 硬件 | 显示、输入、采集及真实隐私状态可用性 | 模组、屏幕、输入方式待确认，不由逻辑页面反推选型 |

这是业务职责关系，不是已冻结技术架构。各模块的行为归属和具体人员责任在RTM中维护；人员Owner仍待指定。

## 4. 核心用户流程

### 4.1 首次启动

**进入条件**：设备上电，尚无可确认的有效绑定或儿童上下文。

```text
初始化 → 检查网络/绑定事实 → 按获准方案完成必要联网与家庭绑定
       → 确认当前儿童 → 进入首页
```

联网与绑定先后依赖、成功确认依据以及是否二维码均待确认。扫码或请求发送不等于成功；儿童未明确时不能分配成绩。绑定失败说明原因，不静默解除已有有效关系，也不自动开启运动采集。日常启动先恢复真实已保存信息，不能直接续计。

### 4.2 自主运动

**进入条件**：设备可用，儿童归属明确，支持动作和允许目标有效。

```text
首页 → 自主运动 → 选择动作与目标 → 确认
     → 动作说明/隐私与站位准备 → 明确开始 → 倒计时与复核
     → 运动 → 达标或主动结束 → 保存 → 查看结果 → 首页
```

两次入口返回不能重建同一记录；不支持动作或无效目标不能伪装可开始。准备不足、倒计时未结束不计数。暂停保留已确认成绩，继续回准备复核；是否再次倒计时待确认。

### 4.3 家长任务运动

**进入条件**：收到任务，儿童、动作、目标和有效条件允许；已缓存的有效任务按允许规则可离线执行。

```text
平台投递 → 检查任务 → 本地保存后回执 → 儿童查看原目标并确认
         → 共用准备/倒计时/运动流程 → 真实结果与保存同步
```

任务到达不自动开始、不自动采集。重复投递沿用同一接收事实；任务撤销、过期或运动中新任务的处理仍待确认。列表与详情是否拆分由实际承载评审，不静默改家长目标。

### 4.4 运动完成与同步

**进入条件**：达标、主动提前结束或已确认的中断结束规则生效。

```text
停止采集/新增计数 → 汇总真实结果 → 本地保存 → 结果页 → 可返回首页
                                           ↓
                              后台上传 → 平台业务确认
                                           ↓失败
                                   沿用原记录标识补传
```

运动结束、本地保存和平台接收是三件事。保存失败不能说“记录好了”；发送完成不能说“家长收到”。同步失败不改变真实成绩，不重建结果或重复已批准奖励，也不阻断允许的本地运动。用时口径、断电保证、重试及退出规则待确认。

## 5. 功能模块

本章全部核心及支撑功能继承原P0 / Pending Review。描述以业务语言呈现；逐功能输入、输出、原待确认内容和技术追踪已完整迁入RTM。下列规则和验收不冻结实现参数。

'''
 text=intro;covered=[];section_map={};lastmod=None
 for sub,profile in PROFILES.items():
  mod=sub[0];number='5.'+sub
  if mod!=lastmod:text+=f'\n### 5.{mod} {modules[mod]}\n';lastmod=mod
  group=[(fid,row) for fid,row in core.items() if fid.startswith(sub+'.')]
  role,trigger,flow,page=profile
  text+=f'\n#### {number} {subs[sub]}\n\n**功能目标**\n\n'+ '；'.join(row[3].rstrip('。') for _,row in group)+'。\n\n'
  text+=f'**使用场景**\n\n- 用户角色：{role}。\n- 触发条件：{trigger}。\n- 使用目的：理解并完成本环节，获得与真实业务事实一致的反馈。\n\n**功能描述**\n\n'
  for fid,row in group:
   text+='- **'+row[1]+'**：'+readable(row[2])+'\n';covered.append(fid);section_map[fid]=number
  text+=f'\n**用户流程**\n\n```text\n{flow}\n```\n\n**页面逻辑**\n\n{page}\n\n**业务规则**\n\n| 规则 | 说明 |\n|---|---|\n| 状态与优先级 | 核心功能维持原P0 / Pending Review；规则未评审不当作工程冻结 |\n'
  owners=list(dict.fromkeys(row[6] for _,row in group));text+='| 业务归属 | '+'、'.join(owners)+'；具体人员待指定 |\n'
  for fid,row in group:
   pre=b.DETAIL[fid][2];text+='| '+row[1]+'的前置 | '+readable(pre)+' |\n'
  text+='\n**异常情况**\n\n'
  for fid,row in group:text+='- '+row[1]+'：'+readable(b.DETAIL[fid][3])+'。\n'
  text+='\n**验收标准**\n\n'
  for fid,row in group:text+='- '+readable(b.DETAIL[fid][4])+'\n'
  text+='\n**待评审边界**\n\n'
  for fid,row in group:
   if row[7]!='—':text+='- '+row[1]+'：'+row[7]+'。\n'
  text+='\n正式量化标准、测试方法和执行证据仍待确认；这些条件供产品评审，不表示实机通过。\n'
 text+='''
### 5.9 历史候选与后续范围

| 候选分组 | 本轮状态与边界 |
|---|---|
| 设备信息、出厂恢复、更新查询 | 待评审，优先级TBD；软件版本查看不代表OTA已纳入；本地重置不等于云端注销 |
| 今日摘要、任务列表/详情细化 | 待评审，优先级TBD；既有任务呈现继续按核心功能工作，不按新界面增加范围 |
| 音量和提示音开关 | 待评审，优先级TBD；提醒时段/频率约束不等于新增声音设置 |
| 更换网络、专门联网检查 | 待评审，优先级TBD；基础联网能力不自动证明新增诊断工具必要 |
| 绑定引导、二维码、失效重取、帮助 | 待评审，优先级TBD；二维码为方案候选，不作为默认技术 |
| 儿童切换和设备解绑细化 | 待评审，优先级TBD；授权、发起端、运动中是否可切换、离线处置待确认 |
| 独立辅助与关键点显示 | 待评审，优先级TBD；准备中的检测不证明独立工具已获准，不生成健康评分 |
| 本地摄像头使用设置、数据说明 | 待评审，优先级TBD；已有本地隐私守卫持续有效 |

20项候选的原描述、价值、待确认内容与编号全部保留在RTM。候选输入/输出、状态、异常及验收细则仍待其范围获准后细化。原P1四类及其他范围未决项保持产品概述中的分层，不整体合并、删除或默认交付。

## 6. 状态模型（业务语言）

| 阶段 | 用户看到什么 | 可以做什么 | 关键守卫与未决 |
|---|---|---|---|
| 目标与归属确认 | 当前儿童、任务或自主来源、动作与目标 | 确认或返回 | 不等于设备开机；记录创建时机待确认 |
| 运动准备 | 经审核说明、目标与主要站位/隐私原因 | 调整、明确开始或取消 | 准备标签不等于满足准入，不计数 |
| 倒计时 | 开始时机及取消/复核结果 | 等待或取消 | 结束再检查，时长和恢复适用待确认 |
| 运动中 | 实际次数、目标进度和必要识别反馈 | 运动、暂停或结束 | 完整有效周期才计数，低置信度不作确定纠错 |
| 暂停 | 已确认成绩和主要原因 | 继续或结束 | 不新增/清零；继续重新准备，超时和再倒计时待确认 |
| 运动结束 | 达标或真实提前结束 | 交给结果汇总与保存 | 停止采集/计数；不代表已保存 |
| 本地已保存 | 可靠保存事实及真实结果 | 查看、返回或允许后台上传 | 不代表已同步；保证与周期待确认 |
| 同步中 | 已保存，上传/补传尚未获业务确认 | 查看必要状态；后台按契约重试 | 不重建结果，不阻断允许的本地运动 |
| 平台已确认接收 | 同一结果已获业务确认 | 查看已同步状态 | 发送完成不能代替业务确认；冲突契约待确认 |

执行、保存、同步是独立维度，可同时表达“提前结束 / 已保存 / 待同步”。绑定、网络和隐私也是独立事实，不硬套运动阶段。绑定成功后还须确认当前儿童；断网不解绑。内部状态标签、原详细进入/退出条件与页面映射见RTM。

## 7. 数据与隐私

### 7.1 摄像头和影像

原始儿童摄像帧不持久化，不进入记录、日志或缓存，不上传持久化。教学示范资源与儿童采集影像分开；媒体缓存不放宽儿童影像边界。数据最小化适用于所有功能。

未授权、隐私关闭、撤权或状态未知时禁止采集；运动退出/结束停止本轮采集，提示真实状态。准备和恢复重查隐私条件；远程任务不能绕过本地关闭。具体提示方式、撤权响应时限与硬件方案仍待确认。

### 7.2 记录、权限和删除

保存用于任务与结果的必要结构化信息：正确儿童与来源、动作和目标、真实成绩、结束原因，以及唯一记录和独立保存/同步事实。创建时机、用时是否含暂停、存储容量、保留周期、断电恢复范围和补传冲突策略待确认；本稿不定义数据库或API字段。

设备执行有效本地访问/清理请求并回执，平台管理云端身份与权限关系。本地删除不等于账号注销或云端全量删除；未授权管理不执行，离线删除与旧队列处置规则仍待确认。必要故障摘要不能包含原始儿童视频。

## 8. 异常流程

| 异常 | 用户影响与反馈 | 恢复方向 | 待确认 |
|---|---|---|---|
'''
 exc=b.table_rows(b.section(E,'## B 异常业务依据','异常不得触发'))
 for row in exc[1:]:
  if len(row)==6:text+='| '+readable(row[0])+' | '+readable(row[2]+'；'+row[4])+' | '+readable(row[5])+' | 工程细则/参数仍待确认；已获准候选的规则也需单独评审 |\n'
 text+='''
准备中的无人/遮挡意味着不能开始；运动中只有判定为需要暂停才进入暂停。单次不完整或不确定动作仅不计该事件，不能一律视为暂停。异常不允许未经授权采集、清零成绩、虚假达标、重复结果或错误解绑。原因未知时如实说明不可确认，不虚构故障。

## 9. Open Questions

评审问题保留原OQ与UE-OQ编号，这是正文必要的管理引用。关联对象用功能/页面名称表述，完整内部映射在RTM。原状态与材料保持不变；参与方不等同已指派人员。

### 9.1 功能范围与业务问题

'''
 oqblocks=re.findall(r'<details>.*?</details>',b.section(F,'## 13 Open Questions','### 13.1'),re.S)
 text+='\n\n'.join(readable(x) for x in oqblocks)
 text+='\n\n### 9.2 用户体验与交接问题\n\n'
 ublocks=re.findall(r'<details>.*?</details>',b.section(U,'## 8 Open Questions','## 9 Document Review'),re.S)
 text+='\n\n'.join(readable(x) for x in ublocks)
 text+='''

### 9.3 必须保留的输入差异

| 差异 | 本稿处理 | 原问题入口 |
|---|---|---|
| 基线七动作与当前三动作提议 | 不自定MVP，不删除上游追踪；逐动作范围/单位仍待确认 | OQ-01/03、UE-OQ-03 |
| 基线写“3、2、1”，UE仍把时长列为待确认 | 不冻结三秒；恢复是否再次倒计时也待确认 | OQ-07、UE-OQ-05 |
| 基线含字段/版本线索，工程参考不冻结实现 | 只保留业务信息，不输出已批准接口字段、模型或部署方案 | OQ-09/10/12、UE-OQ-06/11 |
| 基线较广维护/体态场景与当前未决范围 | 原追踪保留，不默认纳入或删除 | OQ-06/15/16、UE-OQ-08/09 |
| 上游细化顺序表述不同 | 按本次要求展示PRD→FR→UI Flow→Test Case；交付物相互校验，不以顺序批准范围 | OQ-12、UE-OQ-11 |

确认结论须记录确认人、日期、证据、范围、影响与延期理由。改变既有口径时另行记录“旧口径—新证据—建议修改”；本次阅读重组不裁决这些问题。

## 10. 研发交付说明

评审后的细化链为PRD → FR → UI Flow → Test Case。功能需求明确业务守卫、异常与跨端契约；用户流程明确操作、返回/取消、页面表达及权限；测试依据已批准业务口径建立正常与异常场景。实现/测试要求文档的职责另行澄清，不在本稿补造标准。

详细编号、优先级、行为归属、上游意图和来源版本在独立RTM维护。未指派人员、接口、阈值、超时、范围、测试方法与证据继续待确认。可以草拟下游文档，不代表需求冻结或实机通过。实体承载、输入硬件、控件和资源由相应专业评审，逻辑页面数量不决定屏幕数量。

验收时先检视本稿的用户可观察行为，再由RTM核对每项核心、候选、停用与原问题的去向；不能用编号存在或文档自检代替人工签核。

'''
 # Keep the previous Version History and governance appendices verbatim, append current revision.
 gov=old[old.index('# Version History'):]
 pos=gov.index('\n# Change Impact');gov=gov[:pos]+f'\n| v1.1.0 | {DATE} | Codex（AI，执行用户指令） | Review | 重组正文为18个二级业务模块的目标/场景/流程/规则/异常/验收，迁出内部编号与47详细卡至独立RTM；47核心、20候选、2停用及原问题不变 |\n'+gov[pos:]
 gov+='\n### Change Impact — Readability and RTM\n\n正文减少编号堆叠，内部追踪迁入独立RTM，来源与需求保持不变；具体变化与备份见[变更单](../../governance/CHANGE-PRD-READABILITY-20261012.md)。控制版本v1.0.0→v1.1.0属文档结构Minor，未新增功能或批准范围。\n\n### Decision Log — Readability\n\n本次无产品/架构决策；仅根据用户要求改变正文阅读组织与追踪存放位置。\n'
 text+=gov
 assert set(covered)==set(core)
 # RTM owns the full detail and stable IDs, not invented REQ/UI/TC numbers.
 rtm='# Teamo 设备端需求追踪矩阵 RTM\n\n'+b.ctrl('Requirement Traceability Matrix')+'''## 使用规则

本矩阵与PRD v1.1.0配套。Requirement ID仅引用需求基线已有FR号，不新增REQ号；其关联为已有意图整理，正式FR映射仍待评审。Function ID与Priority唯一来源是功能规格；UI ID使用UE的PAGE号，不新增UI号；State为原沟通标签，不定义实现枚举；Test Case未建立均TC-TBD，不虚构编号。

版本、范围与状态分开管理。47核心P0 / Pending Review、20候选优先级TBD、2停用追溯保持不变。候选不能因为进入矩阵被当作MVP。正文链接指向稳定PRD路径及新章节。

[阅读PRD](Teamo_Device_PRD_v1.0.0_Draft.md) · [评审HTML](Teamo_Device_PRD_v1.0.0_Draft.html)

## 1. 核心需求追踪

| Requirement ID（已有意图） | 需求描述 | PRD章节 | Function ID | UI ID / PAGE关系 | State | Test Case ID | Priority | 状态 | Behavior Owner |
|---|---|---|---|---|---|---|---|---|---|
'''
 traces={x['function']:x for x in evidence['core_traceability']}
 for fid,row in core.items():
  tr=traces[fid]
  rtm+='| '+' | '.join(['、'.join(tr['baseline']),row[1],section_map[fid],fid,tr['page'],tr['state'],'TC-TBD',row[4],'Pending Review',row[6]+'；人员TBD'])+' |\n'
 rtm+='\n## 2. 历史候选与停用追踪\n\n| Requirement ID | 需求描述 | PRD章节 | Function ID | UI ID / State | Test Case ID | Priority | 状态 |\n|---|---|---|---|---|---|---|---|\n'
 cr={x[0]:x for x in b.table_rows(b.section(F,'### 14.2','### 14.3')) if x and x[0] in candidate}
 for fid,row in candidate.items():
  page='；'.join(x for x in cr.get(fid,[]) if 'PAGE-' in x) or 'PAGE TBD'
  rtm+=f'| TBD（不补造需求号） | {row[1]} | 5.9 | {fid} | {page}；State TBD | TC-TBD | TBD | Candidate / Pending Review |\n'
 for fid,row in retired.items():rtm+=f'| 原追溯，不新增 | {row[1]} | 1.3 / 5.9 | {fid} | '+('沿用6.3.1 / 同步维度' if fid=='7.2.2' else '全部PAGE / 全局约束')+' | TC-TBD（不重复用例） | 历史P0，不计核心 | Deprecated / 保留追溯 |\n'
 rtm+='\n### 停用源条目完整记录\n\n| 编号 | 功能点 | 行为 | 用户价值 | 原优先级 | 状态 | 行为归属 | 原历史说明 |\n|---|---|---|---|---|---|---|---|\n'+''.join('| '+' | '.join(row)+' |\n' for row in retired.values())
 rtm+='\n## 3. 固定来源\n\n'+''.join(f'- [{n}]({n})；SHA256 `{sources[n]}`。\n' for n in b.NAMES)
 # Preserve original full cards (including their tests, pending fields and source citations).
 olddetail=b.section(old,'## 5. 功能需求','## 6. 状态模型')
 rtm+='\n## 4. 完整逐项需求卡（从旧正文迁入）\n\n以下保留原47张核心卡及候选/停用原记录，以便核对完整输入、输出、前置、异常、验收和追踪。其中原5.x标题是迁入来源标识，不是新PRD章节；新章节以矩阵为准。\n\n'+olddetail
 rtm+='\n## 5. 状态、异常与问题映射\n\n'+b.section(old,'## 6. 状态模型','## 7. 数据与隐私')+b.section(old,'## 8. 异常流程','## 9. Open Questions')
 rtm+='\n### 原OQ与UE-OQ完整关联\n\n'+b.section(F,'### 13.2','## 14 版本记录')
 rtm+='\n### 来源差异与工程未决\n\n'+b.section(old,'### 9.4 输入差异','## 10. 研发交付说明')
 rtm+='\n# Version History\n\n| Version | Date | Author | Status | Change Summary |\n|---|---|---|---|---|\n| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 从PRD迁入69项追踪、47详细卡、状态/异常及问题关联，新增对应PRD业务章节；不新增需求编号或范围 |\n\n# Change Impact\n\n原正文内部管理信息独立维护；来源、编号、优先级和未决项不变。风险Medium，需检查迁移完整性。详见[变更单](../../governance/CHANGE-PRD-READABILITY-20261012.md)。\n\n# Decision Log\n\n无产品/架构决策；用户要求正文与追踪分离，既有ID继续沿用，无实际Test Case则TC-TBD。\n'
 write(T,rtm);write(P,text)
 # Navigation updates only; historical source documents are protected by hash checks.
 for p in [D/'README.md',D/'DOCUMENT_REGISTER.md',G/'DOCUMENT_REGISTER.md']:
  t=p.read_text(encoding='utf-8');m=re.search(r'\| Current Version \| (v\d+\.\d+\.\d+) \|',t);v=m[1];nums=list(map(int,v[1:].split('.')));nums[2]+=1;new='v'+'.'.join(map(str,nums));t=t.replace('| Current Version | '+v+' |','| Current Version | '+new+' |',1)
  # Only current table row updates; historical prose and changelog remain evidence.
  lines=t.splitlines()
  for i,line in enumerate(lines):
   if line.startswith('|') and P.name in line and '| v1.0.0 |' in line:lines[i]=line.replace('| v1.0.0 |','| v1.1.0 |')
  t='\n'.join(lines)+'\n';start=t.index('# Version History');m=re.search(r'^# (?:Change Impact|Decision Log)\s*$',t[start+1:],re.M);pos=start+1+m.start()
  t=t[:pos]+f'\n| {new} | {DATE} | Codex（AI，执行用户指令） | Review | 同步PRD控制版本v1.1.0与独立RTM入口，保持旧PRD路径；无需求变更 |\n'+t[pos:]
  prefix='' if p.parent==D else '../product/requirements/'
  t+='\n## PRD正文与RTM入口\n\n[PRD正文]('+prefix+P.name+')控制版本v1.1.0；[RTM]('+prefix+T.name+')控制版本v1.0.0；正文按业务阅读，完整内部编号与逐项来源在RTM。\n\n### Change Impact — Readability\n\n当前入口同步控制版本及RTM；不改变范围、优先级与历史。详见[变更单]('+('../../governance/' if p.parent==D else '')+'CHANGE-PRD-READABILITY-20261012.md)。\n'
  write(p,t)
 managed=json.loads((G/'managed-documents.json').read_text(encoding='utf-8'));managed.append(T.relative_to(R).as_posix());write(G/'managed-documents.json',json.dumps(managed,ensure_ascii=False,indent=2)+'\n')
 assert all(sha(D/n)==h for n,h in sources.items())
 assert olddetail in rtm
 # Strict internal-ID check outside the explicitly permitted OQ chapter and history.
 reader=text.split('# Version History')[0];non_oq=reader[:reader.index('## 9. Open Questions')]+reader[reader.index('## 10. 研发交付说明'):]
 assert not re.search(r'\b(?:PAGE-\d+|FR-[A-Z]+-\d+|TC-TBD|INIT|READY|COUNTDOWN|RUNNING|PAUSED|FINISHED|SAVED|SYNCING|SYNCED)\b',non_oq)
 assert all(row[2] in rtm and row[7] in rtm for row in rows.values())
 assert len(re.findall(r'^##### Function ',rtm,re.M))==47
 for target in [P,T]:
  cp=subprocess.run(['C:/Users/13896/.workbuddy/binaries/python/versions/3.13.12/python.exe',str(R/'tools/render_device_prd_html.py'),'--refresh','--source',str(target)],capture_output=True,text=True,encoding='utf-8');assert cp.returncode==0,cp.stderr;print(cp.stdout.strip())
 # Old PRD HTML section/Function deep links continue to reach the new business module.
 from html.parser import HTMLParser
 class IDs(HTMLParser):
  def __init__(self):super().__init__();self.ids=[]
  def handle_starttag(self,tag,attrs):
   self.ids += [v for k,v in attrs if k=='id']
 with zipfile.ZipFile(backup/'baseline.zip') as z: previous=z.read(P.with_suffix('.html').relative_to(R).as_posix()).decode('utf-8')
 parser=IDs();parser.feed(previous);newhtml=P.with_suffix('.html').read_text(encoding='utf-8');now=IDs();now.feed(newhtml);aliases=[]
 for anchor in parser.ids:
  if anchor in now.ids:continue
  fid=re.search(r'function-(\d)(\d)(\d)',anchor)
  if fid:
   key='.'.join(fid.groups());sectionid=section_map.get(key)
   if sectionid:
    # markdown-generated headings have stable numeric prefix; insert before target section.
    prefix=''.join(sectionid.split('.'));match=re.search(r'(<h4 id="'+prefix+r'[^\"]*">)',newhtml)
    if match:newhtml=newhtml[:match.start()]+'<span id="'+anchor+'" aria-hidden="true"></span>'+newhtml[match.start():];aliases.append(anchor);continue
  aliases.append(anchor)
 # Remaining old anchors land at top with a compatibility explanation.
 current=IDs();current.feed(newhtml);remaining=[a for a in aliases if a not in current.ids]
 block=''.join('<span id="'+a+'" aria-hidden="true"></span>' for a in remaining)
 newhtml=newhtml.replace('<main id="content">','<main id="content">'+block)
 newhtml=newhtml.replace('正式评审材料，未冻结。47项核心需求 · 20项候选 · 17项 OQ · 11项 UE-OQ','业务正文 · Review · 未冻结。完整47核心/20候选追踪见独立RTM')
 newhtml=newhtml.replace('Markdown 源文档</a>','Markdown 源文档</a><a href="'+T.with_suffix('.html').name+'">独立 RTM</a>')
 write(P.with_suffix('.html'),newhtml)
 test=subprocess.run(['C:/Users/13896/.workbuddy/binaries/python/versions/3.13.12/python.exe',str(R/'tools/document_control.py')],capture_output=True,text=True,encoding='utf-8');errors=test.stdout.splitlines();scope=[x for x in errors if any(n in x for n in [P.name,T.name,'CHANGE-PRD-READABILITY','requirements/README.md','requirements/DOCUMENT_REGISTER.md','governance/DOCUMENT_REGISTER.md'])];assert not scope,scope
 evidence={'prd_version':'v1.1.0','change_type':'Minor (document structure only)','core':47,'candidate':20,'retired':2,'business_sections':section_map,'original_detail_preserved':True,'source_sha256':sources,'source_unchanged':True,'internal_ids_outside_oq':0,'old_html_anchors_preserved':len(parser.ids),'document_control_scope_errors':scope,'preexisting_errors':errors,'prd_sha256':sha(P),'rtm_sha256':sha(T)}
 write(G/'prd-readability-evidence.json',json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
 report=b.ctrl('PRD Readability Report')+f'''# PRD Readability Revision Report

- PRD控制版本v1.0.0→v1.1.0（Minor：文档结构重组，需求范围不变）；沿用原路径。
- [PRD业务正文](../product/requirements/{P.name})与[HTML](../product/requirements/{P.with_suffix('.html').name})。
- [独立RTM](../product/requirements/{T.name})与[HTML](../product/requirements/{T.with_suffix('.html').name})。
- 18个二级模块含目标、使用场景、描述、用户流程、页面逻辑、业务规则、异常与验收；正文非OQ章节内部ID数量为0。
- 原47张详细需求卡完整迁入RTM；69项Function记录保留。17 OQ和11 UE-OQ不重新编号；所有优先级/候选/待确认内容保留。
- 原HTML的{len(parser.ids)}个锚点仍存在；原功能锚点尽可能导向对应业务模块，其余历史章节锚点进入正文首页，通过目录继续定位。Markdown旧标题锚点兼容不自动验收。
- 四份源文档SHA256一致，旧PRD/HTML已完整备份。治理检查本次范围无错误，全库仍有{len(errors)}项既有历史变更单问题。
- [备份](backups/prd-readability-20261012/baseline.zip)、[前哈希](backups/prd-readability-20261012/sha256.json)、[验证及后哈希](prd-readability-evidence.json)。
- 没有新增需求/功能/需求编号，没有把TBD变成确定，没有进行实机或算法验证。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录PRD业务正文与RTM分离、编号保留、HTML兼容及校验 |

# Change Impact

仅正文组织、追踪位置、HTML和导航登记变化；详见[变更单](CHANGE-PRD-READABILITY-20261012.md)。风险Medium，原细节迁入RTM，不能只读正文忽略未决范围。

# Decision Log

本次无产品/架构决策；结构修订不代表范围批准。
'''
 write(G/'PRD_READABILITY_REPORT.md',report)
 print(json.dumps({'prd':str(P),'rtm':str(T),'chars_before':len(old),'chars_after':len(text),'core':47,'candidate':20,'retired':2,'scope_errors':0},ensure_ascii=False))

if __name__=='__main__':main()

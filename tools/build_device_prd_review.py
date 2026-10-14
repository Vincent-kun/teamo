"""Compile the four pinned product sources into a traceable Review draft."""
from pathlib import Path
import re, json, hashlib, zipfile, subprocess

R=Path(__file__).resolve().parents[1]; D=R/'docs/product/requirements'; G=R/'docs/governance'; DATE='2026-10-12'
NAMES=['Teamo_Device_Requirement_Baseline_v0.1.1.md','Teamo_Device_Function_Specification_v0.5.2.md','Teamo_Device_UE_IA_v0.3.1.md','Teamo_Device_UE_Engineering_Reference_v0.1.0.md']
OUT='Teamo_Device_PRD_v1.0.0_Draft.md'
def write(p,t): p.write_text(t,encoding='utf-8',newline='\n')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def section(t,a,b): return t[t.index(a):t.index(b)]
def table_rows(t):
 return [[c.strip() for c in l.strip().strip('|').split('|')] for l in t.splitlines() if l.startswith('|') and not re.match(r'^\|[- :|]+$',l)]
def ctrl(dtype,ver='v1.0.0'):
 return f'''# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | {dtype} |
| Current Version | {ver} |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | {DATE} |
| Last Updated | {DATE} |

'''
def governance(ver,summary):
 return f'''
# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| {ver} | {DATE} | Codex（AI，执行用户指令） | Review | {summary} |

# Change Impact

- Section: 设备端PRD结构、需求追踪及文档登记。
- Before: 四份输入分别描述需求、功能、UE和工程参考；此前PRD Draft保留在原路径。
- After: 形成指定十章PRD评审稿，逐项引用既有编号；范围、优先级及未决状态不变。
- Affected: 本PRD、目录README/REGISTER、全局登记表与managed-documents.json。
- Risk: Medium；输入存在三/七动作与倒计时时长差异，已显式保留，不能把候选或TBD当成冻结要求。
- [修改前变更单](../../governance/CHANGE-DEVICE-PRD-REVIEW-20261012.md)。

# Decision Log

本次无产品方向、功能取舍或架构决策。v1.0表示正式PRD评审材料的文档版次，不表示MVP阶段变化、产品批准、实现或实机验收。源文档差异留待原OQ/UE-OQ评审；本稿不裁决。
'''

# Each item contains only observable business facts; thresholds/contracts stay TBD.
# input, output, precondition, exception, qualitative acceptance (not a frozen Test Case)
DETAIL={
'1.1.1':('上电/重启事件、必要运行条件','可用状态或已确认启动异常','设备上电或重启；隐私状态未明不得采集','启动/必要服务不可用，按1.2.2处理；范围与时限TBD','验证必要运行条件后进入可用或明确异常状态；启动时长TBD。'),
'1.1.2':('6.2.2给出的可恢复任务、记录、隐私与同步事实','待机、恢复提示或异常去向','启动后已取得恢复结果；恢复状态TBD','无法确认的进度不补造，具体不可恢复处理TBD','只恢复可确认事实，不自动续计、不将未完成会话表示为完成。'),
'1.2.1':('启动、任务、运动、保存、同步及异常业务事实','当前可执行操作和一致的业务状态','相应状态事实可用；各守卫由所属功能维护','故障、权限或识别异常按所属分支，恢复契约TBD','同一业务操作在不同入口遵循相同状态约束；执行、保存、同步分别表达。'),
'1.2.2':('已确认启动失败或必要运行服务不可用原因','原因说明及约定重试、返回或必要重启去向','已判定为设备级故障','原因未知如实说明不可确认；故障范围/恢复时限TBD','只展示可确认故障，恢复后重新验证；不替代4.1.3识别异常判定。'),
'1.2.3':('当前设备软件版本事实','供家长/维护人员核对的真实版本','可读取软件版本；展示入口按UE映射','读取失败表达规则TBD，不补造版本','展示与设备事实一致的软件版本；不由版本查看引入OTA或远程运维。'),
'1.2.4':('必要故障原因和发生时间','供诊断使用的必要故障记录','发生可记录故障；日志范围/周期TBD','记录失败处理TBD；日志不得包含原始儿童摄像帧','故障记录限必要信息，原始帧不进入日志；记录字段与周期TBD。'),
'1.2.5':('获准的重启操作','设备重启及1.1.2恢复结果','重启触发方式与适用权限TBD','重启失败与恢复不足按1.2.2/6.2.2；细则TBD','重启后进入启动/恢复检查，不直接续计或伪造完成记录。'),
'2.1.1':('当前任务/自主能力及必要设备可用状态','任务与自主运动可理解入口','设备进入可用首页；动作与身份按对应功能检查','不可用状态说明原因，不将候选入口默认开放','任务和自主运动入口均可理解，进入共用准备路径；不新增独立运动闭环。'),
'2.1.2':('已有运动状态与固定表情资源','与运动事实一致的固定角色回应','状态事件已确认；事件/资源清单TBD','资源不可用与降级表达TBD，不承诺新增AI对话','角色回应与真实状态一致；原P0保留，表情丰富度和运动星/PB深度另评审。'),
'2.2.1':('设备不可用或操作不可执行的已确认状态','状态、当前影响及可处理原因','设备状态事实可用；表达方式TBD','原因未确认时说明不可确认，不编造故障','提示说明是否可用及可行去向；任务、成绩、结果由各主功能提供。'),
'2.2.2':('选择、开始、取消、暂停、继续、结束、返回意图','操作是否被接受的反馈','所属业务状态允许该操作；实际输入方式TBD','不允许/未接受须区分；业务失败由所属功能说明','接收确认与业务执行结果分别表达；不默认触控、语音或手势。'),
'3.1.1':('送达任务的儿童归属、支持动作、目标、有效条件','接受资格或拒绝原因','收到任务，相关规则可检查；细则TBD','归属/动作/目标/有效性不满足则给可确认原因','未通过检查不称可执行；任务到达不自动开始或开启摄像头。'),
'3.1.2':('3.1.1检查结果、6.2.1任务保存事实','真实接收结果或失败原因','检查通过且保存成功才确认接收','检查/保存失败说明原因；重复任务沿用同一接收结果','检查并成功保存后才确认接收；重复投递不产生多条不同接收事实。'),
'3.1.3':('任务动作、目标、来源和设备执行状态','儿童可理解任务内容与状态','存在可查看任务事实；列表/详情拆分TBD','无任务/任务无效如实表达；撤销/过期细则TBD','动作、目标、来源及执行状态一致，不静默改家长目标或自建发布规则。'),
'3.1.4':('自主选择的支持动作/允许目标，或已下发任务动作/目标','明确的运动目标、来源与归属上下文','当前儿童及目标有效；自主目标范围TBD','不支持动作或无效目标不伪装可开始','自主与任务来源区分；家长任务只确认原目标，自主目标允许范围另评审。'),
'3.2.1':('已确认动作、经审核动作与安全说明','儿童可理解的动作/安全说明','开始前已选定动作；媒体形态和跳过规则TBD','资源缺失/加载失败规则TBD，安全前置不能自行省略','说明有审核依据；不将AI生成示范当成有效动作规则或默认视频方案。'),
'3.2.2':('4.1.1画面/人体可用性与准备原因','主要站位调整提示及准备状态','目标与归属明确，隐私允许才识别准备','无人、身体不完整、画面不可用则调整并复核','准备不足不得开始；提示依据检测事实，不默认视频预览或骨架显示。'),
'3.2.3':('儿童明确开始意愿、准备满足与隐私事实','倒计时与结束后的开始资格复核','准备满足、隐私允许、儿童明确开始','取消/离画回准备；隐私失效阻断；时长TBD','准备/倒计时不计数；倒计时结束仍须复核；恢复是否再倒计时TBD。'),
'3.3.1':('主动暂停或已判定需暂停的离画/识别异常','暂停状态、原因及已确认次数','运动正在执行；暂停触发判定按所属功能','单个不确定事件不一律暂停；异常阈值TBD','暂停停止新增成绩并保留已确认次数，不清零努力。'),
'3.3.2':('继续意愿、已确认成绩、隐私与准备复核结果','获准恢复或仍需处理原因','重新检查隐私/准备并明确恢复','隐私或准备不足不能恢复；恢复确认/再倒计时TBD','从保留成绩继续，重新判断动作起点/重置半周期；不能直接绕过准备恢复。'),
'3.3.3':('真实成绩、目标、主动结束意愿或已确认中断规则','真实达标或提前结束事实','达标、主动结束或已确认规则生效','自动超时结束规则TBD，不凭空结束并声称达标','结束停止新增计数；提前结束保留实际成绩和真实未达标状态。'),
'4.1.1':('有效授权下的人体和画面输入','有人/完整性/画面可用状态及主要原因','授权及本地隐私允许且状态可确认','无人、身体不完整、遮挡/画面不可用；多人/距离TBD','检测结果提供给准备与异常处理，不在画面不满足条件时开始可信计数。'),
'4.1.2':('审核动作规则和已判定完整有效周期事件','已确认有效次数','RUNNING且隐私/识别准入有效；规则阈值TBD','不完整、重复、不确定事件不计；异常由4.1.3判定','一次完整有效周期只计一次，未完成/重复/不确定事件不增加成绩；量化阈值TBD。'),
'4.1.3':('4.1.1画面状态和4.2动作判定','无人、遮挡、识别不确定或不可用原因','识别事实可确认','单次不确定与需暂停异常分开，判定阈值TBD','只输出已判定原因；暂停交3.3.1，调整提示交5.1.2，低置信度不作确定纠错。'),
'4.2.1':('开合跳阶段事实及审核有效规则','供4.1.2使用的完整有效周期间事实','当前动作是开合跳且处于RUNNING；幅度/规则TBD','半周期/不确定判定不作有效事件','并拢→打开→回收符合审核规则才构成周期；不自定幅度阈值。'),
'4.2.2':('站立、下蹲、回站立阶段及审核规则','供4.1.2使用的完整有效周期事实','当前动作是深蹲起且处于RUNNING；安全/幅度TBD','未完整回站立或不确定事件不作有效周期','站立→有效下蹲→回站立按审核规则判定；不自定安全或角度标准。'),
'4.2.3':('抬腿/落下及左右侧事件、审核计数口径','按一致左右规则供4.1.2使用的事件','当前动作是高抬腿且处于RUNNING；单/双侧口径TBD','目标与成绩口径未确认不得写成固定规则','目标与结果采用同一已确认左右侧规则；本稿不选择单侧一次或双侧一轮。'),
'5.1.1':('设备已确认次数、目标与识别状态','一致的次数、进度与必要短语音','存在真实已确认成绩；反馈频率TBD','未确认事件不进入显示成绩；异常依5.1.2','数字和短语音基于同一设备成绩，不由页面/App另行递增。'),
'5.1.2':('有效/无效/不确定动作及已判定主要原因','正向回应或一个可处理调整提示','反馈依据已确认识别事实','低置信度如实说明不确定，不确定纠错或责备','有效动作获得适度回应，异常提示具体且可处理；不作医疗/身材评价。'),
'5.1.3':('真实结束、达标或提前结束事实','尊重真实努力的适度完成鼓励','运动确已结束；运动星/PB深度TBD','提前结束不得表达为达标；候选成长深度不默认开放','达标与提前结束分别表达，保留原P0基础鼓励，不扩展成长体系。'),
'5.2.1':('已保存的动作、目标、实际次数、用时、结束原因','设备端简要真实结果','本地结果保存事实可确认；用时是否含暂停TBD','保存失败与同步状态分别说明，不称未确认结果完成','儿童能辨认实际与目标以及达标/提前结束；用时定义不在本稿冻结。'),
'5.2.2':('本地保存结果与独立平台同步确认','未保存/已保存/待同步/成功或失败提示','相应保存或同步事实可确认','保存失败不称已记录；发送完成不称平台已收到','运动结束、本地保存、业务接收各自表达，可以同时呈现提前结束/已保存/待同步。'),
'6.1.1':('当前儿童、任务或自主来源、动作与目标上下文','唯一运动记录归属','来源和归属明确；创建时机TBD','归属不明不得错分成绩；重复操作不重建同一结果','同一运动可追溯至正确儿童及来源；不把INIT等同记录已创建。'),
'6.1.2':('已确认次数、目标、用时、真实结束原因','同一运动的唯一结果内容','真实结束且事实可汇总；用时定义TBD','不完整/未知内容不伪造；写入由6.2.1执行','输出真实结果及同一记录内容，提前结束不伪称达标。'),
'6.2.1':('已缓存任务、实际结果、必要待同步信息','本地保存成功或失败事实','需保存的任务/结果存在；容量/周期TBD','保存失败交6.2.3，未经保存不按已保存结果同步','本地保存状态有真实依据；原始摄像帧不写入记录、日志或缓存。'),
'6.2.2':('本地可恢复的任务、运动记录、待同步信息','可恢复真实事实供1.1.2使用','启动/重启需恢复；保存频率与断电范围TBD','不可恢复部分如实说明，不补造成绩或重复记录','仅恢复可确认成绩与同步事实，不自动续计；断电可恢复保证TBD。'),
'6.2.3':('保存失败事实及仍可恢复的结果','尚未保存说明与可恢复结果重试','本地写入失败已判定','恢复保证、退出/不可恢复处理TBD','失败不称保存成功，保留可恢复结果供重试；不承诺未经验证的零丢失保证。'),
'6.3.1':('已保存结果、原记录标识、平台业务接收确认','独立上传/同步状态','记录已保存且允许上传；协议TBD','发送/上传失败或无业务确认保持待确认/待补传','仅平台业务接收确认后表示SYNCED；网络发送完成不作为成功接收。'),
'6.3.2':('原记录标识及失败待补传记录','同一记录补传及防重复结果','同一结果已保存但未获确认；重试/冲突TBD','失败按契约继续待补传，不重建记录','设备沿用原标识，平台按标识去重，不重复生成结果或发放已批准奖励。'),
'7.1.1':('允许的联网配置及真实连接状态','连接状态或可处理失败原因','需要完成联网；流程/责任端TBD','连接失败如实说明，不能由断网解除绑定','必要配置和连接状态可理解，不默认新增网络诊断工具。'),
'7.1.2':('在线/离线/恢复连接事实','与本地可用能力一致的网络提示','连接状态可确认','断网影响新任务/同步，不等同暂停或解绑','离线提示区分已缓存任务和未送达任务；允许本地运动、保存与后续补传保持。'),
'7.2.1':('必要在线/运行状态及软件版本','供平台传递/保存的必要设备状态','状态来源真实；内容/时机/连接方式TBD','状态发送失败处理TBD，不代替任务/结果回执','只同步必要设备事实；任务接收归3.1.2，结果同步归6.3。'),
'7.2.3':('平台有效绑定关系与当前儿童上下文','供任务/记录使用的确认归属','有效绑定和儿童事实需确认；流程/切换TBD','绑定失败或儿童不明按准入分支；断网不自动解绑','成绩归属正确儿童，不默认人脸识别，不自行创建账号或云端关系。'),
'8.1.1':('有效授权及真实本地隐私/硬件状态','允许采集或阻断事实','采集前及继续识别时需满足授权/隐私条件','未授权、关闭、撤权或未知均阻断','所有采集入口遵守同一守卫；远程任务无法绕过本地关闭。'),
'8.1.2':('真实采集状态、运动退出或撤权事实','摄像头状态提示及停止采集事实','状态可确认；提示方式与撤权响应TBD','撤权/关闭或状态未知先阻断；响应时限TBD','退出/结束或撤权停止采集；显示真实状态，不由远程请求强制开启。'),
'8.2.2':('有效家长权限、设备本地访问或规定清理请求','本地执行结果回执','权限有效且设备处置范围已明确；范围/离线响应TBD','权限不足不执行；删除及离线队列处置细则TBD','仅执行设备本地权限和规定清理；不把本地删除当账号注销或云端全量删除。'),
'8.2.3':('已设定提醒时段/频率与第5章提示内容','受时段/频率约束的提醒','存在有效提醒策略；设置责任端/参数TBD','重复/夜间打扰受策略抑制，不默认设备声音设置入口','按已确认策略限制输出与抑制重复；未冻结时段和频率不填入数值。'),
}

BASE_MAP={
'1.1':['FR-DEVICE-001'],'1.2':['FR-DEVICE-001','FR-DEVICE-003'],
'2.1':['FR-DEVICE-001','FR-DEVICE-002'],'2.2':['FR-DEVICE-001','FR-SPORT-004','FR-SPORT-006'],
'3.1':['FR-TASK-001','FR-SPORT-001'],'3.2':['FR-SPORT-002','FR-SPORT-003','FR-SPORT-004'],
'3.3':['FR-SPORT-006','FR-SPORT-007'],'4.1':['FR-SPORT-003','FR-SPORT-005','FR-SPORT-006'],
'4.2':['FR-SPORT-005'],'5.1':['FR-SPORT-005','FR-DEVICE-002'],'5.2':['FR-SPORT-007'],
'6.1':['FR-SPORT-007'],'6.2':['FR-SPORT-007','FR-DEVICE-001'],'6.3':['FR-SPORT-007'],
'7.1':['FR-TASK-001','FR-SPORT-007'],'7.2':['FR-TASK-001','FR-DEVICE-003'],
'8.1':['FR-SPORT-003','FR-SPORT-006','FR-DEVICE-003'],'8.2':['FR-DEVICE-002','FR-DEVICE-003']}

def main():
 import sys
 resume='--resume' in sys.argv
 if (D/OUT).exists() and not resume: raise RuntimeError('Output exists; refusing overwrite')
 if resume:
  with zipfile.ZipFile(G/'backups/device-prd-review-20261012/baseline.zip') as z:
   for n in z.namelist():
    if n in ['docs/governance/DOCUMENT_REGISTER.md','docs/governance/managed-documents.json','docs/product/requirements/README.md','docs/product/requirements/DOCUMENT_REGISTER.md']: (R/n).write_bytes(z.read(n))
 B,F,U,E=[(D/n).read_text(encoding='utf-8-sig') for n in NAMES]
 source_hash={n:digest(D/n) for n in NAMES}
 business=section(F,'## 1 设备','### 8.3 ')
 features={r[0]:r for r in table_rows(business) if len(r)==8 and re.fullmatch(r'\d+\.\d+\.\d+',r[0])}
 core={k:r for k,r in features.items() if r[4]=='P0'}
 candidates={k:r for k,r in features.items() if r[4]=='待确认'}
 retired={k:r for k,r in features.items() if '已停用' in r[5]}
 trace={}
 for row in table_rows(section(U,'## 6 Requirement','## 7 Design')):
  if len(row)==5:
   m=re.match(r'(\d+\.\d+\.\d+) ',row[1])
   if m and m[1] in core: trace[m[1]]=row
 assert len(core)==47 and len(candidates)==20 and len(retired)==2
 assert set(core)==set(DETAIL)==set(trace)
 # Baseline IDs are cited as intents only, never used to create new functionality.
 baseline_ids=set(re.findall(r'^### (FR-[A-Z]+-\d+)',B,re.M))
 assert all(set(v)<=baseline_ids for v in BASE_MAP.values())
 changed=[G/'DOCUMENT_REGISTER.md',G/'managed-documents.json',D/'README.md',D/'DOCUMENT_REGISTER.md']
 backup=G/'backups/device-prd-review-20261012'
 if not resume:
  backup.mkdir(parents=True,exist_ok=False)
  with zipfile.ZipFile(backup/'baseline.zip','w',zipfile.ZIP_DEFLATED) as z:
   for p in [D/n for n in NAMES]+changed+[D/'Teamo_Device_PRD_v0.6.0_Draft.md']: z.write(p,p.relative_to(R).as_posix())
  write(backup/'sha256.json',json.dumps({p.relative_to(R).as_posix():digest(p) for p in [D/n for n in NAMES]+changed+[D/'Teamo_Device_PRD_v0.6.0_Draft.md']},ensure_ascii=False,indent=2))
 # Impact recorded before PRD or register mutation.
 change=ctrl('PRD Review Compilation')+'# Change Impact\n\n- Section: 新PRD十章、逐功能产品需求卡、来源追踪、登记入口。\n- Before: 四份输入各自独立，v0.6.0 Draft保留既有内容。\n- After: 新增v1.0.0 Draft/Review评审稿，保留47核心、20候选、2停用及17 OQ/11 UE-OQ；不修改四份源文档。\n- Change Type: PRD Review Compilation；文档正式化，不是需求/产品Major升级。\n- Risk: Medium；七/三动作、倒计时数值、工程字段与未决实现之间有差异，不能擅自裁决。\n- Affected: PRD及四个登记/导航文件；旧PRD不覆盖，原资料不重写。\n- Baseline: backups/device-prd-review-20261012/baseline.zip及sha256.json。\n\n## 旧口径—输入证据—本稿处理\n\n| 旧口径 | 唯一输入证据 | 本稿处理 |\n|---|---|---|\n| 需求基线七动作 | 功能规格4.2列三动作提议；OQ-01 | 保留差异，由OQ-01/UE-OQ-03确认，不删七动作追踪或增补功能号 |\n| 基线倒计时3/2/1 | UE IA4.2时长TBD | 不冻结3秒，引用OQ-07/UE-OQ-05 |\n| 基线字段和较广维护/体态描述 | 功能规格0.5/9/10与工程参考声明工程细则TBD | 字段作为已有输入线索，不生成API规格；体态/OTA等保持范围TBD |\n| 工作流顺序有不同表述 | 功能规格0.5与13.1、工程参考F | 按用户本次要求展示PRD→FR→UI Flow→Test Case；实际同步迭代，不改变能力 |\n'+governance('v1.0.0','新增PRD编制前影响分析、差异处理及备份入口')
 # Governance file links use a different relative base.
 write(G/'CHANGE-DEVICE-PRD-REVIEW-20261012.md',change.replace('(../../governance/CHANGE-DEVICE-PRD-REVIEW-20261012.md)','(CHANGE-DEVICE-PRD-REVIEW-20261012.md)'))
 intro='''# Teamo 设备端产品需求文档 PRD v1.0 Draft

> 正式评审材料 · Review · 未冻结。v1.0为文档编制版次，控制版本为v1.0.0；不代表产品已批准或完成研发。本文仅使用下列四份固定输入。旧设备端PRD v0.6.0 Draft保留为历史草稿，未作为本稿需求来源。

'''+ctrl('Product Requirements Document')+'''| 评审补充字段 | 内容 |
|---|---|
| Version | v1.0 Draft（控制版本v1.0.0） |
| Source Documents | Requirement Baseline v0.1.1；Function Specification v0.5.2；UE IA v0.3.1；UE Engineering Reference v0.1.0 |
| Approval | Pending Review；未提供签核或冻结证据 |

## Source Documents 与引用约定

| 简称 | 固定输入 | 职责 |
|---|---|---|
'''
 for label,name,role in zip(['B','F','U','E'],NAMES,['产品边界、通用原则与已有需求意图','Function ID、Priority、行为归属、OQ的唯一来源','PAGE、旅程、展示状态与UE-OQ','详细业务状态、异常与工程参考；实现细则TBD']):
  intro+=f'| {label} | [{name}]({name}) | {role} |\n'
 intro+='''
本文的“应”描述继承的业务要求，全部保留Pending Review；不等于冻结实现。每张需求卡的输入/输出指业务信息，不定义API字段、数据结构或枚举。验收标准是基于输入可观察的评审检查点，测试方法、数据集、阈值、时限和实际Test Case均TC-TBD。

Function为原编号，PAGE与State继承U §6；后台支撑可无独立页面，非运动状态不强套INIT/RUNNING。Baseline字段按上游已有需求意图引用，属于整理关联，不是新增需求编号或已批准的一对一FR映射。以F为功能清单、以U为页面依据；差异公开登记，PRD不裁决。

## 评审导览

建议先评审§1范围和§4流程，再看§5需求卡与§6–8约束，最后在§9记录原问题结论。所有结论需明确确认人、日期、证据、影响范围与延期理由；当前人员Owner/Reviewer均待指定。

## 1. 产品概述

### 1.1 产品定位

Teamo面向6–15岁儿童家庭运动场景，帮助儿童理解目标、完成动作、获得可信成绩和适度陪伴。家长负责任务、授权和记录管理；设备负责运动当下的交互、识别、反馈、记录及同步。陪伴服务运动，不转为开放聊天或家庭远程监控。（Source: B §1；F §0.4/12）

### 1.2 产品目标

让儿童能开始、完成并再次运动；让孩子和家长理解成绩事实、暂停原因、保存与同步结果。一次完整有效周期只计一次；提前结束也保留真实努力。目标不增加未经输入定义的商业、增长或模型指标。（Source: B §1–2；F §3–6）

### 1.3 MVP范围

| 层级 | 当前内容 | 状态 |
|---|---|---|
| 核心/支撑 | F的47项P0；自主与任务共用准入、计数、暂停、保存及同步闭环 | Pending Review；编号/优先级原样继承 |
| 历史细化候选 | 20项已有候选，含二维码、声音、摘要、独立辅助等 | Candidate / Pending Review / 优先级TBD；不默认开放 |
| 停用追溯 | 7.2.2→6.3.1；8.2.1→8.3全局约束 | 不重复实现，不计47项 |
| 原P1候选 | 更多动作、运动训练建议、个性化成长、内容与语音陪练 | P1 / Pending Review；不扩展为本稿交付 |
| 其他原追踪 | 学校授权任务、独立体态观察、OTA、远程诊断 | 范围及优先级TBD，不删除或默认纳入 |

F列开合跳、深蹲起、高抬腿三动作提议，B保留七动作要求与保持动作有效秒数口径。三动作是演示切片还是产品MVP仍由OQ-01/UE-OQ-03确认。本稿不新增其他动作功能号，不删除七动作上游追踪；“有效秒数”仅保留B的范围条件，不把保持动作列入当前三动作功能清单。（Source: B §2/FR-SPORT-001/005；F §0.2/4.2/9/10；U §5）

### 1.4 非目标范围

不支持开放聊天、家庭视频监控、陌生人社交或全站公开排行；不得输出医疗分析、身体评价或姿态评分，不引入新AI能力、成长等级、广告或儿童充值。学校授权小范围分享保持原独立评审；运动星/PB最小深度保留TBD，不据此扩展成长体系。（Source: B §1/FR-DEVICE-002/FR-POSTURE-001；F §8.3/9/10；U §5）

## 2. 用户与场景

### 2.1 用户角色

| 用户 | 目标与职责 | 设备端边界 |
|---|---|---|
| 儿童 | 理解目标、准备、明确开始、运动、暂停/恢复/结束、查看真实结果 | 不承担家长账号管理；不默认触控、语音、手势或人脸识别 |
| 家长 | 创建任务、授权、绑定/当前儿童管理、查看记录、发起受限数据操作 | APP/小程序具体形态TBD；不远程绕过本地隐私关闭 |

Source: B §1及FR-DEVICE-001/003；F §0.4/7.2.3/8/12；U §1；E A §5.2。

### 2.2 核心使用场景

| 场景 | 用户问题 | 既有功能与页面 | 状态边界 |
|---|---|---|---|
| 首次使用 | 家庭尚未建立有效绑定/儿童上下文 | 1.1.1、7.1.1、7.2.3；PAGE-00 | 绑定方式/联网顺序TBD，扫码不等于绑定成功 |
| 自主运动 | 儿童希望选择支持动作和允许目标 | 2.1.1、3.1.4；PAGE-01/02 | INIT→READY；目标范围TBD |
| 家长任务运动 | 儿童查看并确认家长下发目标 | 3.1.1–3.1.4；PAGE-03 | 真实接收/保存后可执行；到达不自动采集 |
| 运动中断与恢复 | 暂停或识别异常后保留努力 | 3.3.1/3.3.2、4.1.3；PAGE-06/04 | PAUSED→READY，是否再次倒计时TBD |
| 结束和家长查记录 | 希望理解实际结果以及是否送达 | 5.2、6.1–6.3；PAGE-07/01 | FINISHED、SAVED、SYNCED分别确认 |

Source: B §3；F §2–7；U §1/4/6；E A/B。表中范围号是分组引用，不创建Function ID。

## 3. 产品架构

以下是职责关系，不确定部署位置或技术架构。（Source: F §12；B §2；E F §8.2）

```mermaid
flowchart LR
  P[家长 APP或小程序] -->|任务与授权请求| S[平台 权限关系与统一服务]
  S -->|有效上下文 任务与授权变化| D[设备端 真实运动执行与记录]
  D -->|接收回执 结果与必要状态| S
  S -->|已确认记录与状态| P
  H[硬件 输入输出与隐私状态] -->|可用条件| D
  A[算法 审核规则与有效事件] -->|识别事实| D
```

| 参与方 | 业务职责 | 不能由此推断 |
|---|---|---|
| 设备端 | 维护会话、操作、成绩、保存、同步及本地隐私守卫 | 不创建家长任务，不自行改目标或管理云端账号关系 |
| APP/小程序 | 家长任务、授权管理、发起绑定/切换及查看已确认结果 | 不另行递增次数，不远程强制采集 |
| 平台 | 校验权限、维护关系、投递、业务确认及按同一标识去重 | 发送成功不等于送达，不生成未执行成绩 |
| 算法 | 提供画面/动作有效事件及审核规则证据 | 部署位置、模型、阈值TBD，不放宽离线或隐私 |
| 硬件 | 可用显示、输入、采集及真实本地隐私状态 | 屏幕数量/比例、摄像头模组、按键/触控等TBD，不由PAGE反推选型 |

功能Behavior Owner在§5逐项继承；人员Owner由OQ-12/UE-OQ-11指定。F §12跨端矩阵可用于职责联合评审，具体操作/接口契约仍TBD。

## 4. 核心用户流程 User Flow

### Flow A：首次启动

| 维度 | 定义 |
|---|---|
| 进入条件 | 上电且没有可确认有效绑定/当前儿童上下文；已绑定日常启动走恢复分支 |
| 流程 | 初始化→检查真实网络/绑定状态→引导家长按获准方案完成必要联网与绑定→确认当前儿童→进入首页 |
| 状态变化 | 启动状态（非INIT）→未绑定/等待绑定/处理中→有效绑定→当前儿童确认→正常使用 |
| 关联Function ID | 1.1.1、1.1.2、2.2.1、2.2.2、7.1.1、7.1.2、7.2.3、8.1.1 |
| 关联PAGE | PAGE-00→PAGE-01；必要儿童/网络设置由PAGE-08承载，细则TBD |
| 异常与返回 | 网络/绑定失败不得称成功，不静默解除已有关系；身份未确认不能分配成绩；不自动开启运动采集 |
| 未决 | OQ-02/04/11/13、UE-OQ-01/02/04/10；二维码及7.2.4–7.2.7候选不因流程列出而批准 |
| Source | B FR-DEVICE-001/003；F §1/7/8/12；U §1.1/3 PAGE-00；E A §5.2/B |

### Flow B：自主运动

| 维度 | 定义 |
|---|---|
| 进入条件 | 设备可用，当前儿童及自主来源可确认；支持动作和允许目标有效 |
| 流程 | 首页→自主入口→选择动作/目标→确认→动作说明与隐私/站位准备→明确开始→倒计时→运动→达标或主动结束→保存→结果→首页 |
| 状态变化 | INIT→READY→COUNTDOWN→RUNNING→FINISHED；保存增加SAVED，SYNCING/SYNCED独立 |
| 关联Function ID | 2.1.1、2.2.2、3.1.4、3.2.1、3.2.2、3.2.3、3.3.1–3.3.3、4.1.1–4.1.3、4.2.1–4.2.3、5.1.1–5.1.3、5.2.1/5.2.2、6.1.1/6.1.2、6.2.1/6.2.3、6.3.1/6.3.2、7.2.3、8.1.1/8.1.2 |
| 关联PAGE | PAGE-01→02→04→05→06→07→01；暂停继续回PAGE-04，是否再次PAGE-05 TBD |
| 异常与返回 | 不支持/无效目标不开始；准备不足不计数；取消不生成完成记录；单个不确定事件不计，需暂停时保留成绩 |
| 未决 | OQ-01/02/03/07、UE-OQ-03/05/06；实际输入、目标范围、倒计时/恢复参数TBD |
| Source | B FR-SPORT-001–007；F §2–6/8；U §4.1/4.2；E A/B |

### Flow C：家长任务运动

| 维度 | 定义 |
|---|---|
| 进入条件 | 已收到并检查任务，儿童/动作/目标/有效条件允许；已缓存有效任务可按允许规则离线执行 |
| 流程 | 平台投递→设备检查→本地保存后回执接收→首页任务入口→查看动作/目标/来源→儿童确认执行→共用准备/倒计时/运动/结果流程 |
| 状态变化 | 任务接收事实独立→INIT任务确认→READY→COUNTDOWN→RUNNING→FINISHED；不把网络发送/接收当运动完成 |
| 关联Function ID | 3.1.1、3.1.2、3.1.3、3.1.4、6.2.1、7.2.3；运动阶段沿用Flow B的3.2、3.3、4、5、6、8.1原编号 |
| 关联PAGE | PAGE-01→03（列表/详情实际拆分TBD）→04→05→06→07→01 |
| 异常与返回 | 接收/保存失败不称送达；重复任务沿用同一回执；撤销/过期/运动中新任务处理TBD；不静默修改家长目标，不自动开采集 |
| 未决 | OQ-04/09/13/14/17、UE-OQ-01/02/04；列表/详情候选不另建一套P0能力 |
| Source | B FR-TASK-001；F §3.1/6.2/7.2/12；U §3 PAGE-03/4.1；E A/B |

### Flow D：运动完成与同步

| 维度 | 定义 |
|---|---|
| 进入条件 | 达标、主动提前结束或已确认的中断结束规则生效 |
| 流程 | 停止采集/新增计数→汇总真实结果及原记录标识→本地保存→结果显示→允许返回首页；后台上传→平台业务确认，失败按契约补传 |
| 状态变化 | FINISHED持续表示执行事实；保存成功才增加SAVED；上传中SYNCING，业务确认后SYNCED；失败仍待同步 |
| 关联Function ID | 3.3.3、5.1.3、5.2.1、5.2.2、6.1.1、6.1.2、6.2.1、6.2.3、6.3.1、6.3.2、8.1.2 |
| 关联PAGE | PAGE-06结束→PAGE-07保存/结果；PAGE-01必要同步提示；保存失败具体承载TBD |
| 异常与返回 | 未保存不按已保存结果同步、不称记录好了；未业务确认不称家长收到；补传不重建记录或重复已批准奖励；同步不阻断允许本地运动 |
| 未决 | OQ-08/09、UE-OQ-06/07；用时、保留周期、断电保证、重试/冲突与退出规则TBD |
| Source | B FR-SPORT-007；F §3.3.3/5/6/8；U §4.1/4.2；E A §5.1/5.3/B |

## 5. 功能需求

### 5.0 阅读与验收约定

本章以F的一级→二级→Function ID展开47项核心需求，20项历史候选单列，2项停用另记。每卡有场景、描述、价值、输入/输出、前置、状态、异常、页面、验收和来源。描述继承F；基于用户价值整理场景，不增加行为。卡片的验收检查仅检视输入中的业务不变量，正式量化验收及Test Case仍TC-TBD。

F为Priority和Function唯一来源；U §6为PAGE/State原关系，包含支持而非独立页面承诺。待确认内容完整保留，原条目“—”不等于所有工程细则已确认。

'''
 text=intro
 modules={}; submodules={}
 for m in re.finditer(r'^## ([1-8]) (.+)$',business,re.M): modules[m[1]]=m[2]
 for m in re.finditer(r'^### ([1-8]\.\d+) (.+)$',business,re.M): submodules[m[1]]=m[2]
 lastmod=lastsub=None; audit_cards=[]
 for fid,row in core.items():
  mod=fid.split('.')[0]; sub='.'.join(fid.split('.')[:2])
  if mod!=lastmod: text+=f'\n### 5.{mod} 一级功能：{modules[mod]}\n';lastmod=mod
  if sub!=lastsub: text+=f'\n#### 二级功能 {sub}：{submodules[sub]}\n';lastsub=sub
  inp,out,pre,exc,accept=DETAIL[fid]; tr=trace[fid]; ids='、'.join(BASE_MAP[sub])
  text+=f'''\n##### Function {fid}：{row[1]}

**用户场景**：在{modules[mod]}的{row[1]}环节，家庭需要“{row[3]}”。

**需求描述**：设备应{row[2]}

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | {row[3]} |
| Priority | {row[4]}（继承F；不调整） |
| Requirement Status | Pending Review（源状态：{row[5]}） |
| Behavior Owner | {row[6]}；人员Owner TBD |
| 输入 | {inp} |
| 输出 | {out} |
| 前置条件 | {pre} |
| 状态 | {tr[3]}；仅业务/展示语义，工程枚举TBD |
| 异常 | {exc} |
| 关联页面 | {tr[2]} |
| 验收标准（评审检查点） | {accept} 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | {row[7]} |

**Traceability**

- Baseline: B §3，{ids}；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: {fid} {row[1]}；Source: [Function Specification v0.5.2]({NAMES[1]}) §{sub}。
- PAGE: {tr[2]}；Source: [UE IA v0.3.1]({NAMES[2]}) §6。
- State: {tr[3]}；Source: U §6、[UE Engineering Reference v0.1.0]({NAMES[3]}) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。

'''
  audit_cards.append({'function':fid,'name':row[1],'priority':row[4],'owner':row[6],'pending':row[7],'page':tr[2],'state':tr[3],'baseline':BASE_MAP[sub]})
 text+='''### 5.9 历史候选：不纳入默认MVP交付

以下20项沿用F已有编号和描述，均Candidate / Pending Review / 优先级TBD。输入、输出、守卫、异常及验收细则未冻结；表中的行为只在候选获准时成立。PAGE只记录F §14.2的候选关系，不代表U已批准独立功能或入口。不得为候选补造State/API/Test Case。Source: F §1–8/14.2；U §5/6；E D/E。

| Function ID | 功能 | 候选行为（保留） | 用户价值 | Behavior Owner | 待确认内容 | PAGE / State |
|---|---|---|---|---|---|---|
'''
 candidate_pages={}
 for row in table_rows(section(F,'### 14.2','### 14.3')):
  if row and row[0] in candidates: candidate_pages[row[0]]=row
 for fid,row in candidates.items():
  cr=candidate_pages.get(fid,[]);page='；'.join(x for x in cr if 'PAGE-' in x) or 'PAGE关系TBD'
  text+=f'| {fid} | {row[1]} | {row[2]} | {row[3]} | {row[6]}；人员TBD | {row[7]} | {page}；State TBD；Candidate |\n'
 text+='''
每项候选的Traceability为本行Function（F §14.2）、本行候选PAGE关系（F/U）、State TBD（E），Test Case TC-TBD。候选无独立已批准验收承诺；输入/输出/前置/异常全部待其范围获准后在FR细化，不以需求卡模板填满而创造实现要求。

### 5.10 停用编号与原P1/未决范围

| 原编号 | 去向 | 本稿处理 |
|---|---|---|
| 7.2.2 运动结果通信（历史） | 合并至6.3.1 | 保留追溯，不重复实现/计数 |
| 8.2.1 儿童视频不保存（历史） | 移为F §8.3全局约束 | 原约束仍适用于全部功能和PAGE |

Source: F §7.2/8.2/14；U §6历史追踪。原P1四类与学校/体态/OTA/诊断的原追踪按§1.3保持，不新增编号。B FR-POSTURE-001是已有更广场景，当前F的独立辅助候选不与其自动合并；非运动体态范围仍按OQ-06/16、UE-OQ-08评审。

## 6. 状态模型

### 6.1 会话、保存与同步状态

Source: E A §5.1；U §4.2；F §11.3。全部Pending Review；下表保留原详细进入、行为、退出及PAGE关系，不定义客户端实现枚举。

'''
 state_rows=table_rows(section(E,'### 5.1','READY包含准备阶段'))
 for row in state_rows: text+='| '+' | '.join(row)+' |\n'+ ('|---|---|---|---|---|\n' if row[0]=='状态' else '')
 text+='''
INIT为任务/自主上下文确认，不能用于设备开机；READY包含准备检查，不等于已满足开始。准备/倒计时/暂停不累计成绩。PAUSED恢复重新检查隐私和准备、明确恢复并重置半周期；是否再次COUNTDOWN TBD。

### 6.2 三个独立维度

| 维度 | 事实 | 不得混同 |
|---|---|---|
| 执行 | RUNNING/PAUSED/FINISHED等真实运动过程 | FINISHED不代表已保存 |
| 保存 | 待保存/保存中/失败/SAVED | SAVED不代表平台已收到；未保存不作为已保存记录上传 |
| 同步 | 待同步/SYNCING/失败待补传/SYNCED | 只有平台业务接收确认才SYNCED，发送完成不能代替 |

可同时表达“提前结束 / 已保存 / 待同步”；返回首页不改变成绩、归属或同步事实，不要求等待上传后才能进行允许的本地运动。Source: E A §5.3；F §6/11；U §4.2/5。

### 6.3 绑定、网络与隐私

绑定展示为未绑定→等待绑定→处理中→成功→当前儿童确认→正常使用，解绑/失败是有依据的分支。断网不解除有效绑定；扫码和请求发送不等于成功；儿童归属未知不能分配成绩。网络、隐私、绑定与运动状态分别维护，不强套运动标签。具体绑定方式、超时、撤权响应、实际状态枚举TBD。（Source: E A §5.2；U §4.2；F §7/8）

## 7. 数据与隐私

### 7.1 采集与影像边界

| 规则 | 业务要求 | Traceability |
|---|---|---|
| 原始摄像帧不持久化 | 不进入记录、日志或缓存，不上传持久化；教学示范资源与儿童采集影像分开，不用媒体缓存决策放宽影像边界 | B §2；F §8.3；U §5；Function 8.1.1/8.1.2及4/6相关功能；全部PAGE/跨流程 |
| 隐私关闭禁止采集 | 未授权、本地关闭、撤权或状态未知均阻断；准备和恢复重新检查，远程任务不可绕过 | F 8.1.1/8.1.2；U PAGE-04/05/06/08；E A/B；State 隐私守卫 |
| 退出与结束停止采集 | 运动退出/结束或撤权停止本轮采集，提示真实状态；响应时限TBD | B §2；F 8.1.2；U §5；E A/B；PAGE-06/07/01与隐私提示 |
| 低置信度不确定纠错 | 未确认事件不计，不生成确定身体/医疗判断 | F 4.1.2/4.1.3/5.1.2及8.3；PAGE-06；RUNNING/PAUSED |

### 7.2 结构化信息与权限

| 数据/请求 | 产品级用途 | 状态与待确认 | Traceability |
|---|---|---|---|
| 儿童与来源归属 | 将真实运动关联正确儿童、任务或自主来源 | 创建时机、身份确认、切换规则TBD；不默认人脸识别 | B FR-TASK-001/FR-SPORT-001/007；F 6.1.1/7.2.3；U §6 |
| 任务动作/目标/有效信息 | 检查、保存和呈现真实任务，不静默改家长目标 | 撤销、过期、版本、窗口及契约TBD；已有字段是输入线索，非API冻结 | B FR-TASK-001；F 3.1.1–3.1.4/6.2.1；PAGE-03/INIT |
| 成绩与结果记录 | 记录已确认次数、目标、用时、结束原因；唯一标识沿用补传 | 用时是否含暂停、记录时机、容量/周期/断电范围TBD | F 6.1/6.2/6.3；PAGE-06/07/01；FINISHED/SAVED/SYNCING/SYNCED |
| 本地访问与清理 | 执行有效权限和规定设备清理并反馈结果 | 清理范围、离线响应、旧队列处置TBD；不等同账号注销或云端全量删除 | B FR-DEVICE-003；F 8.2.2/12；PAGE-08入口TBD；权限状态 |
| 必要故障与设备状态 | 维护定位所需原因/时间/版本与必要状态 | 日志内容/周期、同步内容/时机TBD，日志无原始帧 | F 1.2.3/1.2.4/7.2.1；后台及PAGE-08；设备状态 |

Source: B §2/3；F §6–8/12；U §5/6；E A/F。数据最小化适用于全部条目；不因PRD列出业务信息而定义具体字段格式、接口或保留数值。数据权限创建/账号关系由家长端与平台管理；设备负责有效请求、本地守卫和真实回执。

## 8. 异常流程

每个异常先确认原因与影响，再表达可行去向；原因未知如实说明。所有处理仍Pending Review，工程细则TBD / FR阶段定义。Source: E B（详细业务依据）及U §4.3；对应原Function与PAGE见表。State是发生阶段/业务去向，不新增状态枚举。

'''
 excrows=table_rows(section(E,'## B 异常业务依据','异常不得触发'))
 for row in excrows: text+='| '+' | '.join(row)+' |\n'+ ('|---|---|---|---|---|---|\n' if row[0]=='异常 / 原因' else '')
 text+='''
无人/遮挡在准备中意味着未满足开始条件；在运动中只有被判定需暂停才进入PAUSED。单次动作不完整/不确定仅不计该事件，不能自动等同所有识别失败。保存失败不伪称已记录，同步失败不改变达标事实；不解绑、不清零、不重建结果。（Source: F 3.3/4.1/6；U §4.3；E B）

## 9. Open Questions

### 9.1 Function Specification OQ（原编号完整保留）

Source: F §13。以下原问题全文引用；参与方只是原建议，不等同Named Owner，未决状态不改变。

'''
 oqsec=section(F,'## 13 Open Questions','### 13.1')
 oqblocks=re.findall(r'<details>.*?</details>',oqsec,re.S)
 text+='\n\n'.join(oqblocks)+'\n\n### 9.2 UE-OQ（原编号完整保留）\n\nSource: U §8；背景、影响、评审输入和完整材料仍见E附录E。以下全文引用，不改候选和TBD。\n\n'+section(U,'## 8 Open Questions','## 9 Document Review').split('\n',1)[1]
 text+='\n### 9.3 两类问题关联\n\nSource: F §13.2；关联只是评审定位，不合并或重新编号。\n\n'+section(F,'### 13.2','## 14 版本记录').split('\n',1)[1]
 text+='''
### 9.4 输入差异与评审处理

| 差异 | 固定输入证据 | 本稿保留状态 | 原问题入口 |
|---|---|---|---|
| 七动作与三动作 | B §2/FR-SPORT-001/005保留七动作；F §4.2列三动作提议，U §5未冻结关系 | 不扩动作号或删除上游追踪；演示/产品范围TBD | OQ-01/03、UE-OQ-03 |
| 倒计时数值 | B FR-SPORT-004写3/2/1；U §4.2写时长TBD，E恢复是否再倒计时TBD | 不把三秒写成冻结验收值；时间与恢复路径TBD | OQ-07、UE-OQ-05 |
| API字段与部署 | B §3列字段/版本线索；F §0.5与E不定义API结构、枚举或算法实现 | 作为业务信息，不生成已批准字段规范、部署方案或数值 | OQ-09/10/12、UE-OQ-06/11 |
| 维护/体态较广表述 | B FR-DEVICE-003/FR-POSTURE-001含广范围；F §9/10、U §5保持OTA/体态等未决 | 原追踪保留，本稿不纳入默认MVP，也不删除 | OQ-06/15/16、UE-OQ-08/09 |
| 交付细化顺序 | F §0.5写UE→UI Flow→FR；§13.1另有FR/TR表述 | 按用户本次要求展示PRD→FR→UI Flow→Test Case，交付物互相校验，次序不构成范围批准 | OQ-12、UE-OQ-11 |

没有新增OQ编号；差异复用现有未决项。待评审决定必须按“旧口径—新证据—建议修改”记录；未提供新证据时不能修改既有产品/功能口径。上述表是差异登记，不是已批准决策。

## 10. 研发交付说明

### 10.1 交付链与责任

PRD（本评审稿）→ FR（细化业务守卫/异常/跨端契约）→ UI Flow（操作与呈现）→ Test Case（正常/异常与可验证证据）。FR和UI Flow应回查同一Function/PAGE/State；先后顺序不妨碍相互校验。TR由后续工程/测试阶段定义实现或测试要求口径，先明确职责，不在本PRD新增标准。（Source: F §0.5/13.1；E F §8.2/8.3；用户本次指定展示顺序）

| 交付物 | 至少需要的既有引用信息 | 未决保留 |
|---|---|---|
| FR | 固定四份版本、原Function/优先级、PAGE、前置、状态变化、数据事实、异常与原OQ/UE-OQ | 具体Owner、接口版本、守卫阈值/超时、范围批准TBD；已有B的FR号不重排 |
| UI Flow | 用户任务、PAGE类型/职责、必须信息、操作确认、返回/取消、权限及异常 | 实体承载、输入硬件、控件/资源/文案TBD，不由图示批准候选能力 |
| Test Case / TR | 原功能+PAGE+状态条件+异常路径及实际批准口径 | 正式编号、方法、数据集、阈值、环境与执行证据TC-TBD；自检不等于实机通过 |

### 10.2 进入下一阶段的评审出口

评审逐项确认范围或延期理由，指定Named Owner/Reviewer，记录确认人、日期、依据、影响功能/PAGE和引用版本。关键动作规则、操作方式、准备/恢复、绑定与平台业务确认、保存/断电、隐私/删除的未知继续按原OQ追踪。没有证据的条目继续Pending Review/TBD；允许草拟FR不等于冻结实现或通过测试。（Source: F §13；U §7/8 UE-OQ-11；E F）

### 10.3 本稿检查结果与限制

| 检查 | 结果 |
|---|---|
| 核心需求来源 | 47张核心卡均引用B已有意图、F编号/优先级、U PAGE/State及E状态/异常 |
| 新增功能/编号 | 0；47核心、20候选、2停用逐项与F核对 |
| PAGE/State | 沿用U/E；后台或非会话功能不强套运动状态；PAGE-09保持候选 |
| TBD/候选/优先级 | 原待确认内容完整保留；候选未转P0，原P1不转成默认交付 |
| OQ/UE-OQ | 17项OQ及11项UE-OQ原编号/材料保留 |
| MVP边界 | 三/七动作差异明确；不新增聊天、医疗、视频监控或成长体系 |
| 源文档与历史 | 四份源文档及v0.6.0 Draft不改写；备份与SHA256可恢复 |
| 验收证据 | 只有源依据整理的评审检查点；未创建真实Test Case、未运行算法或实机验证 |

详细结构与链接校验见[编制报告](../../governance/DEVICE_PRD_REVIEW_REPORT.md)。该检查是文档一致性验证，内容和范围仍需人工联合评审。

'''
 text+=governance('v1.0.0','基于四份固定输入编制十章正式PRD评审稿，展开47项核心卡、20候选、2停用及原OQ/UE-OQ；不改范围和优先级')
 write(D/OUT,text)
 # Update only navigation/governance; historical and all pinned inputs remain untouched.
 for p in [D/'README.md',D/'DOCUMENT_REGISTER.md',G/'DOCUMENT_REGISTER.md']:
  t=p.read_text(encoding='utf-8');m=re.search(r'\| Current Version \| (v\d+\.\d+\.\d+) \|',t);oldver=m[1]; parts=list(map(int,oldver[1:].split('.')));parts[2]+=1;newver='v'+'.'.join(map(str,parts))
  t=t.replace('| Current Version | '+oldver+' |','| Current Version | '+newver+' |',1)
  marker='\n# Change Impact' if p.parent==D else '\n# Decision Log'
  pos=t.index(marker,t.index('# Version History'))
  row=f'\n| {newver} | {DATE} | Codex（AI，执行用户指令） | Review | 登记Teamo设备端PRD v1.0.0 Draft/Review为当前评审入口，保留v0.6.0历史草稿和固定四份输入 |\n'
  t=t[:pos]+row+t[pos:]
  link=OUT if p.parent==D else '../product/requirements/'+OUT
  t+='\n## PRD v1.0 Draft Review Entry\n\n['+OUT+']('+link+')为当前设备端PRD评审入口；Status Review，未批准或冻结。v0.6.0 Draft原路径保留历史草稿，不作为本次需求来源。四份输入版本不变，审批权威顺序不变。\n'
  if p.name=='DOCUMENT_REGISTER.md' and p.parent==D:
   t=t.replace('| [Teamo_Device_PRD_v0.6.0_Draft.md](Teamo_Device_PRD_v0.6.0_Draft.md) | v0.6.0 | Draft |',f'| [{OUT}]({OUT}) | v1.0.0 | Review |')
   t+='\n### PRD Historical Draft\n\n[Teamo_Device_PRD_v0.6.0_Draft.md](Teamo_Device_PRD_v0.6.0_Draft.md)原样保留；旧路径兼容关系继续有效。\n'
  if p==G/'DOCUMENT_REGISTER.md':
   family=f'| Teamo设备端PRD | [{OUT}](../product/requirements/{OUT}) | [v0.6.0 Draft](../product/requirements/Teamo_Device_PRD_v0.6.0_Draft.md)保留原位 | Review；四份指定输入，不代表批准或取代整体PRD |\n'
   anchor='| Teamo整体UI逻辑框架 |'
   t=t[:t.index(anchor)]+family+t[t.index(anchor):]
   t+='\n### PRD Review Register\n\n| 文档 | 治理版本 | 提交状态 | 角色 |\n|---|---|---|---|\n'+f'| [{OUT}](../product/requirements/{OUT}) | v1.0.0 | Review | 当前设备端PRD评审材料；未冻结 |\n'
  # Each navigation edit adds local impact, beyond its preexisting generic section.
  t+='\n### Change Impact — PRD Review Entry\n\n- Section: 当前PRD导航/登记。\n- Before: 指向v0.6.0 Draft。\n- After: 指向v1.0.0 Review，旧草稿保留；只更新文档入口，不更改产品范围。\n- Risk: Low；[变更单]('+('../../governance/' if p.parent==D else '')+'CHANGE-DEVICE-PRD-REVIEW-20261012.md)。\n'
  write(p,t)
 managed=json.loads((G/'managed-documents.json').read_text(encoding='utf-8'))
 managed.append('docs/product/requirements/'+OUT);write(G/'managed-documents.json',json.dumps(managed,ensure_ascii=False,indent=2)+'\n')
 oqids=set(re.findall(r'<summary>(OQ-\d+)',text));ueids=set(re.findall(r'<summary>(UE-OQ-\d+)',text))
 assert oqids=={f'OQ-{i:02}' for i in range(1,18)} and ueids=={f'UE-OQ-{i:02}' for i in range(1,12)}
 assert all(digest(D/n)==source_hash[n] for n in NAMES)
 assert set(re.findall(r'^##### Function (\d+\.\d+\.\d+)',text,re.M))==set(core)
 for row in core.values():
  assert row[7] in text and row[2] in text and row[3] in text
 # Validate relative links (paths only; Markdown heading anchors stay authored by renderer).
 bad=[];total=0
 for p in [D/OUT,D/'README.md',D/'DOCUMENT_REGISTER.md',G/'DOCUMENT_REGISTER.md',G/'CHANGE-DEVICE-PRD-REVIEW-20261012.md']:
  for dest in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
   if '://' in dest or dest.startswith('#'):continue
   total+=1
   if not (p.parent/dest.split('#')[0]).exists() and dest!='../../governance/DEVICE_PRD_REVIEW_REPORT.md': bad.append({'source':str(p),'link':dest})
 assert not bad,bad
 p=subprocess.run(['C:/Users/13896/.workbuddy/binaries/python/versions/3.13.12/python.exe',str(R/'tools/document_control.py')],capture_output=True,text=True,encoding='utf-8')
 errs=p.stdout.splitlines();current=[x for x in errs if OUT in x or 'CHANGE-DEVICE-PRD-REVIEW' in x or 'DEVICE_PRD_REVIEW_REPORT' in x or 'requirements/README.md' in x or 'requirements/DOCUMENT_REGISTER.md' in x or 'governance/DOCUMENT_REGISTER.md' in x]
 assert not current,current
 evidence={'date':DATE,'source_sha256':source_hash,'prd_sha256':digest(D/OUT),'core_count':47,'candidate_count':20,'retired_count':2,'core_traceability':audit_cards,'oq_ids':sorted(oqids),'ue_oq_ids':sorted(ueids),'source_unchanged':True,'local_links_checked':total,'broken_links':bad,'scope_document_control_errors':current,'global_preexisting_errors':errs}
 write(G/'device-prd-review-evidence.json',json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
 report=ctrl('PRD Compilation Report')+f'''# Teamo Device PRD Review Report

- Output: [{OUT}](../product/requirements/{OUT})。
- Version: v1.0.0；展示名v1.0 Draft；Status Review。
- Change Type: PRD Review Compilation；文档结构正式化，无需求版本/范围批准。
- 完整十章、Flow A–D、47核心需求卡、20候选、2停用、17 OQ/11 UE-OQ。
- 每张核心卡含原Function/Priority/Behavior Owner/待确认项、B意图引用、U PAGE/State、E状态/异常和评审检查点。
- 新增功能/编号为0，源输入与旧PRD草稿不改写；所有未决、P1与范围差异保留。
- 验证{total}处本地引用，断链0；本次文档控制检查无错误。全库仍有{len(errs)}项既有错误（6份历史变更单），未修改历史记录。
- 没有创建已批准Test Case，未验证远程链接、Markdown渲染锚点、算法或实机；本稿是可供评审的产品需求材料。
- Evidence: [结构与哈希检查](device-prd-review-evidence.json)。
- Baseline: [完整备份](backups/device-prd-review-20261012/baseline.zip)与[SHA256](backups/device-prd-review-20261012/sha256.json)。

## 输入固定哈希

| Source | SHA256 |
|---|---|
'''+''.join(f'| {n} | `{h}` |\n' for n,h in source_hash.items())+governance('v1.0.0','记录PRD编制范围、功能/页面/状态与未决追踪检查、来源哈希和治理登记修订')
 write(G/'DEVICE_PRD_REVIEW_REPORT.md',report.replace('(../../governance/CHANGE-DEVICE-PRD-REVIEW-20261012.md)','(CHANGE-DEVICE-PRD-REVIEW-20261012.md)'))
 print(json.dumps({'output':str(D/OUT),'core':47,'candidates':20,'oq':17,'ue_oq':11,'links':total,'broken':0,'chars':len(text)},ensure_ascii=False))

if __name__=='__main__':main()

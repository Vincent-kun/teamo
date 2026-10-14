import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { stages } from './requirements-stage-design.mjs';
import { plainStages } from './requirements-stage-plain.mjs';

stages.forEach((s,i)=>s.plain=plainStages[i]);
stages[0].plain.operation='沿用初步确定的手机端：任务页 → 创建运动邀请 → 选单项运动或AI计划 → 选动作、调次数 → 选仅今天/每天/隔天 → 设提醒时间 → 核对目标设备 → 确认邀请。AI计划目前仍是演示能力。';
stages[0].plain.why='手机端操作沿用已有小程序MVP，不重新设计单次任务与周期选择。接下来细化设备怎么接收、到点提醒、执行和回传结果。';
stages[0].plain.question='现有页面说离线后自动同步，代码却禁止离线发送，需要统一；接收回执目前是模拟，需明确真实设备确认条件。';
stages[0].recommendation='沿用用户确认的初步手机端方案：单项/AI计划、目标次数、执行周期、提醒时间、目标设备、发送与取消。真实通信和设备执行另行细化。';
stages[0].operations=[['创建邀请','任务页 → 创建运动邀请 → 单项运动或AI计划','沿用既有表单；AI计划目前是演示能力','复用任务页和接口层；计划能力仍需正式服务','沿用家长手机，无设备触屏增项'],['填写任务','开合跳/深蹲起 → 次数加减 → 仅今天/每天/隔天 → 提醒时间 → 核对设备','现有单孩子上下文；多孩子选择不作为本次新增默认','动作能力校验；周期与提醒调度；目标快照','设备时钟、存储、扬声器'],['发送或取消','确认邀请 → 接收回执；列表中可取消并二次确认','已有交互初步确定；离线文案与代码行为存在差异，待统一','真实接收与取消确认；重复指令处理；失败提示','设备网络与持久存储']];
stages[0].options[0][0]='现有单项任务表单（初步确定）';
stages[0].options[1][0]='现有周期选择（初步确定）';
stages[0].options[1][2]='沿用入口；真实周期执行和取消未来任务规则仍需细化';
stages[6].plain.question='断网存储已确定，MVP不做断电续练；需确认保存失败、空间不足、保留期与补传规则。';
stages[6].plain.operation='结束后先保存成绩；有网络再上传。重启后保留已保存成绩，不自动接着做中断的运动。';
stages[6].operations[2]=['重启与低电','使用前提示充电；重启查看已保存成绩和待上传队列','不要求断电续练；保存失败明确提示','可靠记录与队列、异常中断说明、低电提醒','持久存储；边充边用需电源与热验证'];
stages[6].extra='本地存成绩、何时上传进度、教学媒体怎样播放是不同问题。用户已确定断网存储、原始视频不持久保存、不做运动中断电续练；已保存成绩仍应保留。';
const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.dirname(here);
const files = {
  matrix: 'docs/product/planning/PRD到1115演示功能对应矩阵_V0.1_20261010.md',
  scope: 'docs/product/planning/MVP软件演示范围与逐步细化_V0.1_20261010.md',
  decisions: 'docs/product/planning/MVP关键问题与决策台账_V0.1_20261010.md',
  device: 'docs/product/requirements/设备端需求基线_评审稿_V0.1_20261010.md',
  prd: 'docs/product/requirements/03_儿童AI运动陪伴机器人_PRD_V3.0.html',
  hardware: 'docs/hardware/儿童AI运动陪伴机器人_MVP硬件技术需求说明书_V2.0.html',
  research: 'docs/product/design/专业需求基线与可视化评审方法研究_20261010.md',
  navigation: 'docs/product/planning/需求基线导航与评审入口_20261010.md',
  ueOriginal: 'docs/product/design/儿童AI运动陪伴机器人_完整产品UE_Demo_V7.3.html',
  miniappBaseline: 'AI运动伙伴/小程序MVP_V0.1/UE_Demo与小程序MVP对照说明.md',
  baselineUpdate: 'docs/product/design/UE与小程序初步基线衔接_20261010.md',
  directionUpdate: 'docs/product/design/MVP方向确认与技术评估_20261010.md',
  quickstart: 'docs/product/design/需求评审工作台_快速上手.md',
  teamoDiagrams: 'prototype/Teamo设备端UE_状态机与思维导图.html',
};
const read = key => fs.readFileSync(path.join(root, files[key]), 'utf8');
const rows = str => str.split(/\r?\n/).filter(s => s.startsWith('|')).map(s => s.split('|').slice(1, -1).map(t => t.trim()));
function refs(s, prefix) {
  const set = new Set();
  const p = prefix.replace('-', '\\-');
  for (const m of s.matchAll(new RegExp(`\\b${p}(\\d{2})(?:[–—-](?:${p})?(\\d{2}))?`, 'g'))) {
    const begin = +m[1], end = m[2] ? +m[2] : begin;
    if (end >= begin && end - begin < 60) for (let i = begin; i <= end; i++) set.add(prefix + String(i).padStart(2, '0'));
  }
  return [...set];
}
const matrix = rows(read('matrix'));
const requirements = matrix.filter(c => /^R\d{2}$/.test(c[0])).map(c => ({
  id: c[0], module: c[1].includes('；') ? c[1].split('；')[0] : '横向要求',
  title: c[1], mapping: c.length === 5 ? c[2] : '',
  proposal: c.length === 5 ? c[3] : c[2], acceptance: c.length === 5 ? c[4] : '',
  software: refs(c.join(' '), 'S'), decisions: refs(c.join(' '), 'D'), source: 'matrix',
}));
const software = rows(read('scope')).filter(c => /^S\d{2}\s/.test(c[0])).map(c => ({
  id: c[0].slice(0, 3), title: c[0].slice(4), responsibility: c[1], behavior: c[2], acceptance: c[3], decisions: refs(c[4], 'D'), source: 'scope',
}));
for (const c of matrix.filter(c => /^S\d{2}$/.test(c[0]))) software.push({ id: c[0], title: c[1], responsibility: '工作包候选 / 责任人待绑定', behavior: c[2], acceptance: c[2], decisions: [], source: 'matrix' });
software.push({ id: 'S25', title: '动作说明与示范', responsibility: '新增表达候选 / 待媒体评审', behavior: '静态图、简化动画或视频；首次/可跳过/运动中持续未决定。资源审核、离线可用与缓存失败策略需明确。', acceptance: '审核版本可追踪；既有离线运动承诺不得被媒体加载阻断；安全前置是否可跳过须决定。', decisions: ['D06', 'D12'], source: 'device' });
const decisions = rows(read('decisions')).filter(c => /^D\d{2}$/.test(c[0])).map(c => ({ id: c[0], title: c[1], options: c[2], evidence: c[3], roles: c[4], deadline: c[5], source: 'decisions' }));
const questions = rows(read('decisions')).filter(c => /^OPEN-\d{3}/.test(c[0])).map(c => ({ id: c[0].match(/^OPEN-\d{3}/)[0], alias: c[0], title: c[1], conflict: c[2], output: c[3], decisions: refs(c[0], 'D'), source: 'decisions' }));
const device = read('device');
const functional = [...device.matchAll(/^### (FR-[A-Z]+-\d{3}) (.+)\r?\n([\s\S]*?)(?=^### |^## |$(?![\s\S]))/gm)].map(m => {
  const fields = rows(m[3]).filter(c => c[0] && !['字段', '---'].includes(c[0]));
  return { id: m[1], title: m[2], fields, requirements: refs(m[3], 'R'), software: refs(m[3], 'S'), decisions: refs(m[3], 'D'), questions: [...new Set(m[3].match(/OPEN-\d{3}/g) || [])], source: 'device' };
});
const gates = rows(read('scope')).filter(c => /^(?:A |B |C |D |E |F |G |H )/.test(c[0])).map(c => ({ title: c[0], date: c[1], output: c[2], exit: c[3] }));
for (const r of requirements) {
  r.functional = functional.filter(f => f.requirements.includes(r.id)).map(f => f.id);
  r.questions = [...new Set(functional.filter(f => f.requirements.includes(r.id)).flatMap(f => f.questions))];
  r.reviewStatus = '待确认'; r.owner = ''; r.evidenceStatus = '未登记';
}
const states = [
  ['home', 'HOME', '待机 / 任务入口', 'FR-DEVICE-001', '启动恢复完成；未完成会话先提示恢复。', '任务 / 快速运动 / 必要设置', '表情、任务状态、一个主要异常。', '启动/任务选择', '已有任务和身份明确', '运动采集关闭；网络状态可独立变化'],
  ['select', 'SELECT / TASK', '选择与目标', 'FR-SPORT-001,FR-TASK-001', '自主动作或已接受任务。', '选择 / 目标确认 / 返回', '动作、目标、单位与来源。', '儿童明确选择', '动作受支持且目标合法', '收到任务不自动开启摄像头'],
  ['info', 'INSTRUCTION', '动作说明 · 待决', 'FR-SPORT-002', '已选定动作；示范形态未冻结。', '查看 / 重播 / 跳过待确认', '静态、动画或视频仍是选项。', '说明结束 / 合规跳过', '安全说明是否必看已确定', 'OPEN-001决定离线与媒体方案'],
  ['entry', 'ENTRY', '入镜与调整', 'FR-SPORT-003', '允许采集且硬件状态明确。', '调整位置 / 返回', '无人、过近/远、不完整、暗光等一种主要提示。', '人体持续满足准备', '完整入镜与稳定时间满足', '隐私关闭/未知转阻断，采集失败不开始'],
  ['ready', 'READY', '准备 / 明确意愿', 'FR-SPORT-003,FR-SPORT-004', '入镜条件连续满足。', '启动确认方式待OPEN-006', '准备符号与语音。', '确认开始', '任务、隐私和站位再次通过', '条件失效回入镜；恢复是否倒计时待决'],
  ['count', 'COUNTDOWN', '3 → 2 → 1', 'FR-SPORT-004', '开始意愿和准备均满足。', '取消', '大数字与短音。', '倒计时结束', '结束瞬间再次检查守卫', '离画回入镜；隐私变化转阻断'],
  ['active', 'SPORT_ACTIVE', '真实识别 / 计数', 'FR-SPORT-005', '倒计时正常结束或恢复条件通过。', '运动 / 暂停 / 提前结束', '确认实际/目标、单位、识别状态，反馈低频。', '有效完整动作', '事件有效、唯一且属于当前周期', '离画/采集失败暂停；断网继续本地运动'],
  ['pause', 'SPORT_PAUSE', '暂停 / 保留进度', 'FR-SPORT-006', '主动、离画、隐私或采集异常。', '重入镜确认 / 提前结束', '已完成成绩与原因。', '恢复请求', '重新站位、隐私允许、明确恢复', '半周期重置；12/20后下一次有效动作为13'],
  ['save', 'RESULT_SAVING', '结束 / 本地保存', 'FR-SPORT-007', '达标或明确提前结束。', '保存处理', '结束状态与保存状态分开。', '写入/入队成功', '本地原子保存完成', '写失败保留数据并提示重试，不说已保存'],
  ['error', 'SAVE_ERROR', '保存失败 / 重试', 'FR-SPORT-007', '写入失败且待保存数据仍保留。', '重试 / 按策略恢复', '尚未保存与明确恢复办法。', '重试', '可写且数据完整', '不得静默丢失或伪称已同步'],
  ['result', 'SPORT_RESULT', '真实成绩', 'FR-SPORT-007', '本地保存成功。', '查看 / 返回', '目标、实际、用时、达标/提前结束、同步状态。', '返回首页', '本地结果已可查看', '上传失败仍可查看；成功确认后清同步队列'],
];
const transitions = [
  ['home','select','选择任务 / 快速运动','身份与权限有效','选择动作与目标'],
  ['select','info','确认目标','动作支持且目标合法','建立来源与目标快照'],
  ['info','entry','说明结束 / 跳过','隐私明确允许；跳过规则待决','进入采集检查'],
  ['entry','ready','准备持续满足','完整入镜、距离与稳定时间','提示已准备'],
  ['ready','count','明确开始','输入映射待决；重新检查守卫','启动倒计时'],
  ['count','entry','离画','倒计时尚未结束','取消倒计时'],
  ['count','active','倒计时结束','隐私/站位/任务均满足','激活会话；成绩0'],
  ['active','active','有效事件','当前会话、完整、唯一','确认成绩+1或有效秒数'],
  ['active','pause','暂停 / 离画 / 隐私 / 采集异常','暂停原因已确定','保留进度；停止确认事件'],
  ['pause','ready','回位并明确恢复','隐私允许；准备有效','清半周期；是否再倒计时待OPEN-006'],
  ['active','save','达标 / 提前结束','结束原因确定','停止计数；原子保存与入队'],
  ['pause','save','提前结束','记录真实实际','生成未达标结果'],
  ['save','error','写入失败','保留未保存数据','提示重试；不报告保存成功'],
  ['error','save','重试','保存条件可恢复','再次写入'],
  ['save','result','保存成功','本地记录和同步队列一致','显示真实成绩'],
  ['result','home','返回','保存成功','关闭运动采集'],
];
const methodology = [
  { name: '双向追踪与基线变更', url: 'https://www.nasa.gov/reference/6-2-requirements-management/', application: 'PRD来源 → 设备FR → 软件工作包 → 决策依赖 → 验收证据；变更先评估影响。' },
  { name: '事件、守卫、动作与并行状态', url: 'https://www.w3.org/TR/scxml/', application: '转移可检查；运动、网络、隐私、同步保持不同语义，避免断网被画成运动终止。' },
  { name: '分层架构视图', url: 'https://c4model.com/diagrams', application: '职责/数据交接与运动状态分开；不是把所有信息堆进一张图。' },
  { name: '验证与用户场景确认', url: 'https://www.nasa.gov/reference/5-0-product-realization/', application: '指标符合要求与孩子/家长实际可用分别留证据；不以文档或静态图代替实机完成。' },
];
const model = { schemaVersion: 1, date: '2026-10-10', status: '评审候选 / 未共同签核', files, requirements, software, functional, decisions, questions, gates, states, transitions, methodology, stageDesign: stages };
for (const stage of stages) for (const ref of stage.refs) if (![...requirements,...decisions,...questions].some(x=>x.id===ref)) throw new Error('Missing stage reference '+ref);
const stageDoc = '# 运动主流程：操作方案与软硬件需求拆解\n\n评审候选，未共同签核。PRD已有能力由对应R编号回查；下列具体操作、器件与推荐均需评审，不代表已实现或冻结。\n\n' + stages.map((s,i)=>`## ${i+1}. ${s.title}\n\n${s.recommendation}\n\n对应：${s.refs.join('、')}\n\n| 操作 | 用户动作 | 显示与反馈 | 软件需求 | 硬件需求 |\n|---|---|---|---|---|\n${s.operations.map(r=>'| '+r.join(' | ')+' |').join('\n')}\n\n### 方案比较\n\n| 方案 | 优势 | 代价/限制 | 软件需求 | 硬件需求 |\n|---|---|---|---|---|\n${s.options.map(r=>'| '+r.join(' | ')+' |').join('\n')}\n\n数据/控制链路：${s.flow}\n\n验收场景：${s.verify}\n\n${s.extra||''}\n`).join('\n');
fs.writeFileSync(path.join(root,'docs/product/design/运动主流程_操作方案与软硬件需求拆解_V0.1_20261010.md'),stageDoc);
if (requirements.length !== 45 || software.length !== 25 || functional.length !== 12 || decisions.length !== 15 || questions.length !== 8 || gates.length !== 8) throw new Error('Source parsing count mismatch: ' + JSON.stringify([requirements.length,software.length,functional.length,decisions.length,questions.length,gates.length]));
for (const r of requirements) for (const s of r.software) if (!software.some(x => x.id === s)) throw new Error(`${r.id} -> missing ${s}`);
for (const s of states) for (const f of s[3].split(',')) if (!functional.some(x => x.id === f)) throw new Error(`State ${s[0]} -> missing ${f}`);
fs.writeFileSync(path.join(here, 'requirements-review-model.json'), JSON.stringify(model, null, 2) + '\n');
const template = fs.readFileSync(path.join(here, 'requirements-review-template.html'), 'utf8');
if (!template.includes('/* REVIEW_MODEL */ null')) throw new Error('Missing template marker');
fs.writeFileSync(path.join(here, 'requirements-review-workbench.html'), template.replace('/* REVIEW_MODEL */ null', JSON.stringify(model).replace(/</g, '\\u003c')));
console.log(JSON.stringify({ requirements: requirements.length, software: software.length, functional: functional.length, decisions: decisions.length, questions: questions.length, states: states.length, gates: gates.length, output: 'prototype/requirements-review-workbench.html' }));

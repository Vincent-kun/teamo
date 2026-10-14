import fs from 'node:fs';
const nodes=[
['idle','首页 / 学伴表情',490,30,'UE已有','待办、计划、自主运动、排行入口。UE里的滑动是参考操作，实际按键/触控方案尚未冻结。'],
['select','选运动 → 设目标',490,150,'select / target','仅开放支持动作；显示动作、目标和单位。家长任务沿用下发目标，不强制孩子重新设置。'],
['entry','站位检查',490,290,'entry','隐私允许才采集；全身完整、光照与稳定条件满足才进入准备。方向图标与短语音形式待确认。'],
['ready','已站好 / 确认开始',490,410,'ready','明确开始意愿与站好是两个条件。近身按键后要留回位过程，不能立刻计数。'],
['countdown','3 → 2 → 1',490,530,'countdown','数字和短音；最后复查站位与隐私。中途离画回到站位检查，成绩仍为0。'],
['running','识别与计数',490,650,'running','真实完整动作才加一；平板支撑用有效秒数。断网继续本地运动，暂停保留成绩。'],
['save','结束 / 本地保存',490,800,'新增补齐','停止计数，保存真实成绩和待上传记录。失败不能显示已保存。达标和提前结束分别记录。'],
['result','完成反馈 → 结果',490,960,'celebrate / result','达标才表达达标庆祝；提前结束也有真实结果。本地保存成功后可查看，待同步/已同步按实际确认显示。固定+8星不能代替奖励规则。'],
['task','新任务提示 → 详情',60,150,'task_arrive / task_alert','家长任务：马上开始进入站位，加入待办则保留任务。收到任务不代表孩子已开始。运动中收到任务不抢占当前会话。'],
['todo','待办任务',60,290,'todo','从首页进入；查看任务后明确开始。新任务可加入待办。任务版本、过期、取消与排序规则需补齐。'],
['pause','暂停 / 等孩子回来',900,650,'pause / away','主动暂停、离画或相机异常：成绩保留，半个动作清除。明确继续后先检查站位；是否再倒计时待确认。'],
['privacy','隐私关闭 / 采集阻断',900,410,'privacy','关闭立即停止采集和计数；开启不能自动恢复运动。回到准备流程，隐私未知也不能开始。'],
['save_error','保存失败 / 重试',900,800,'新增补齐','保留尚未保存的数据并提示重试。存储满、写入失败或掉电恢复分别验证，不伪称已同步。']
];
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
const rect=n=>`<g data-node="${n[0]}" tabindex="0" role="button" aria-label="${esc(n[1])}"><rect x="${n[2]}" y="${n[3]}" width="270" height="74" rx="8" fill="Canvas" stroke="CanvasText" ${n[4]==='新增补齐'?'stroke-dasharray="6 4"':''}/><text x="${n[2]+135}" y="${n[3]+30}" text-anchor="middle" font-size="18">${esc(n[1])}</text><text x="${n[2]+135}" y="${n[3]+55}" text-anchor="middle" font-size="13">${esc(n[4])}</text></g>`;
const line=(d,label,x,y)=>`<path d="${d}" fill="none" stroke="CanvasText" stroke-width="1.5" marker-end="url(#arrow)"/><text x="${x}" y="${y}" font-size="13">${label}</text>`;
const arrows=[line('M625 104V150','自主运动',635,132),line('M625 224V290','目标确认',635,261),line('M625 364V410','持续满足准备',635,392),line('M625 484V530','明确开始',635,515),line('M625 604V650','最后复查通过',635,633),line('M625 724V800','达标 / 提前结束',635,765),line('M625 874V960','本地保存成功',635,920),line('M490 67H195V150','收到家长任务',210,58),line('M195 224V290','加入待办',205,263),line('M330 187H400V327H490','马上开始',344,180),line('M330 327H490','选择任务开始',340,316),line('M760 687H900','暂停 / 离画',780,676),line('M1035 650V265H795V327H760','明确继续 → 重查站位',813,255),line('M1035 724V770H760V830','提前结束',785,758),line('M760 837H900','保存失败',785,825),line('M1035 874V911H820V860H760','重试',830,899),line('M490 567H450V327H490','倒计时离画',340,558),line('M490 997H20V67H490','返回首页',30,1050)];
const svgHead=(w,h)=>`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" style="color-scheme:light dark;background:Canvas;color:CanvasText;font-family:system-ui"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="CanvasText"/></marker></defs><g fill="CanvasText">`;
const state=svgHead(1250,1200)+arrows.join('')+nodes.map(rect).join('')+`<text x="40" y="1105" font-size="16">跨环节规则：隐私关闭 → 立即停止采集；断网 ≠ 停止运动；同步失败 ≠ 成绩丢失。</text><text x="40" y="1140" font-size="16">虚线框为建议新增状态。箭头是研发评审建议；点击节点查看与UE的对应。</text></g></svg>`;
const branches=[
['入口与任务',['首页表情 · idle','自主运动 · select / target','家长任务 · task_arrive / task_alert','待办 · todo；新任务不抢占运动']],
['站好与开始',['站位 → 准备 → 倒计时','方向图标 + 短语音（待定）','相机看得到伸开的手脚','开始方式 / 稳定时间待测']],
['运动与反馈',['运动 · running；实际 / 目标','次数与有效秒数分开','完整动作才加一，不重复','设备本地识别；算力与散热实测']],
['暂停与保护',['暂停 / 离画 · pause / away','保留成绩，重查站位后恢复','隐私关闭 · privacy：停采集','远距暂停 / 继续方式待确认']],
['保存与家长结果',['本地保存 + 待上传记录（补齐）','掉电 / 存储满 / 保存失败验证','网络恢复补传；重传只记一次','celebrate / result：真实成绩与同步状态']],
['已有扩展场景',['计划 · plan / plan_alert','逐项 / 休息 · plan_step / plan_rest','体态 · posture / posture_active','学校任务 / rank：本次范围待确认']],
['软件要做到什么',['任务与儿童身份对应','准备、计数、暂停规则完整','声音与显示不互相抢占','离线识别、可靠保存、真实回执']],
['硬件与待决定事项',['屏幕 / 按键 / 扬声器','相机视场角、摆放与隐私检测','主控 / 内存 / 存储 / 散热','动作、阈值、媒体和11/15范围待确认']]
];
const mind=svgHead(1450,1110)+`<rect x="590" y="460" width="270" height="100" rx="10" fill="Canvas" stroke="CanvasText"/><text x="725" y="500" text-anchor="middle" font-size="23">Teamo设备端UE</text><text x="725" y="531" text-anchor="middle" font-size="15">操作 → 提示 → 需求 → 验证</text>`+branches.map((b,i)=>{const left=i<4,x=left?30:970,y=30+(i%4)*265;return `<path d="M${left?590:860} 510H${left?530:920}V${y+95}H${left?480:970}" fill="none" stroke="CanvasText"/><rect x="${x}" y="${y}" width="450" height="200" rx="8" fill="Canvas" stroke="CanvasText"/><text x="${x+20}" y="${y+35}" font-size="21">${i+1}. ${b[0]}</text>${b[1].map((s,j)=>`<text x="${x+20}" y="${y+72+j*30}" font-size="16">${esc(s)}</text>`).join('')}`;}).join('')+'</g></svg>';
const html=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Teamo设备端UE：状态机与思维导图</title><style>:root{color-scheme:light dark}body{font:16px/1.7 system-ui;background:Canvas;color:CanvasText;margin:24px auto;padding:0 20px;max-width:1400px}button{font:inherit;color:CanvasText;background:Canvas;border:1px solid GrayText;padding:8px 14px;border-radius:5px;cursor:pointer}nav{display:flex;gap:12px;flex-wrap:wrap}svg{width:100%;min-width:900px}section{overflow:auto;border:1px solid GrayText;margin:16px 0}g[data-node]{cursor:pointer}g[data-node]:focus rect,g[data-node]:hover rect{stroke-width:3}#detail{padding:14px;border:1px solid GrayText}small{color:GrayText}@media print{nav{display:none}section{break-before:page}svg{min-width:0}}</style><h1>Teamo设备端UE：状态机与思维导图</h1><p>先看状态机：孩子怎样完成一次运动，出了问题去哪里。再看思维导图：每个环节要做什么、依赖什么。手机端沿用初步确定的小程序MVP；本图为设备研发评审稿，未代表实机已实现。</p><nav><button onclick="document.getElementById('state').scrollIntoView()">看状态机框图</button><button onclick="document.getElementById('mind').scrollIntoView()">看思维导图</button><button data-download="state">下载状态机SVG</button><button data-download="mind">下载思维导图SVG</button><button onclick="print()">打印 / 保存PDF</button></nav><h2>1. 状态机框图</h2><p>中间是主流程，左侧是任务入口，右侧是暂停和失败处理。点击框查看说明。实线框对应UE已有页面；虚线框是建议补齐。</p><div id="detail">点击任一状态查看说明。隐私是跨环节保护条件；图中隐私框不是只有一条路径才能触发的页面。</div><section id="state">${state}</section><h2>2. 思维导图</h2><p>已有扩展场景保留，但是否进入11月15日演示需单独确认。示范媒体形式也未冻结，不能默认推导视频播放器或大容量存储。</p><section id="mind">${mind}</section><p><small>对照源：docs/product/design/Teamo设备端UE展示.html及设备端UE参考与视觉边界。暂停直接返回运动、结果固定显示已同步、固定奖励均未当成研发已确定规则。</small></p><script>const nodes=${JSON.stringify(nodes)};function select(id){const n=nodes.find(n=>n[0]===id);document.getElementById('detail').textContent=n[1]+'（'+n[4]+'）：'+n[5];}document.addEventListener('click',e=>{const n=e.target.closest('[data-node]');if(n)select(n.dataset.node);const b=e.target.closest('[data-download]');if(b){const s=document.querySelector('#'+b.dataset.download+' svg').outerHTML;const u=URL.createObjectURL(new Blob([s],{type:'image/svg+xml'}));const a=document.createElement('a');a.href=u;a.download='Teamo-'+b.dataset.download+'.svg';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000);}});document.addEventListener('keydown',e=>{const n=e.target.closest('[data-node]');if(n&&(e.key==='Enter'||e.key===' ')){e.preventDefault();select(n.dataset.node);}});</script></html>`;
fs.writeFileSync('prototype/Teamo设备端UE_状态机与思维导图.html',html);
fs.writeFileSync('prototype/Teamo设备端UE_状态机.svg',state);
fs.writeFileSync('prototype/Teamo设备端UE_思维导图.svg',mind);
console.log('Generated standalone HTML and two SVG diagrams; '+nodes.length+' states, '+branches.length+' mind-map branches.');

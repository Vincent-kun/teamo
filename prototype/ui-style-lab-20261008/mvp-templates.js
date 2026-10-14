/* Adapted from the user-selected MVP preview; original remains unchanged. */
const MVPViews=(()=>{

const BASE = {
  profile:{parentName:'夏先生',childName:'小夏',age:8,grade:'小学二年级',goal:'增强体能'},
  device:{id:'TEAMO-DEMO-001',name:'客厅运动伙伴',online:true,status:'idle',battery:82,wifi:'家庭 Wi-Fi'},
  todayMinutes:22, streak:5, stars:46, postureAlerts:2,
  tasks:[
    {id:'T001',name:'开合跳',target:20,unit:'次',source:'家长邀请',time:'今天 19:00',status:'待执行',receipt:'设备已收到'},
    {id:'T002',name:'深蹲起',target:15,unit:'次',source:'家长邀请',time:'今天 18:20',status:'已完成',receipt:'结果已同步'}
  ],
  records:[
    {id:'R001',name:'深蹲起',date:'今天 18:20',actual:15,target:15,valid:13,duration:65,score:86,status:'已完成',source:'家长邀请',deviceName:'客厅运动伙伴',issues:['2次动作幅度不足']},
    {id:'R002',name:'开合跳',date:'昨天 19:10',actual:20,target:20,valid:18,duration:42,score:91,status:'已完成',source:'家长邀请',deviceName:'客厅运动伙伴',issues:['节奏稳定']}
  ],
  deviceTimeline:[
    {time:'18:20',text:'完成深蹲起，结果已同步'},
    {time:'17:58',text:'设备上线，网络状态良好'},
    {time:'昨天',text:'完成开合跳 20 次'}
  ],
  actions:[
    {id:'jumping_jack',name:'开合跳',short:'开',target:20,unit:'次',type:'协调与心肺',color:'purple',stage:'MVP已支持',available:true},
    {id:'squat',name:'深蹲起',short:'蹲',target:15,unit:'次',type:'下肢力量',color:'peach',stage:'MVP已支持',available:true},
    {id:'high_knee',name:'高抬腿',short:'抬',target:30,unit:'次',type:'心肺与节奏',color:'blue',stage:'算法评审中',available:false},
    {id:'jump_rope',name:'双脚跳绳',short:'跳',target:30,unit:'次',type:'协调与心肺',color:'pink',stage:'后续适配',available:false},
    {id:'push_up',name:'俯卧撑',short:'撑',target:8,unit:'次',type:'上肢力量',color:'mint',stage:'后续适配',available:false},
    {id:'sit_up',name:'仰卧起坐',short:'起',target:12,unit:'次',type:'核心力量',color:'pink',stage:'后续适配',available:false},
    {id:'plank',name:'平板支撑',short:'稳',target:30,unit:'秒',type:'核心稳定',color:'blue',stage:'后续适配',available:false}
  ],
  week:[{label:'一',value:12},{label:'二',value:20},{label:'三',value:8},{label:'四',value:25},{label:'五',value:18},{label:'六',value:30},{label:'日',value:22}],
  plan:{name:'基础体能 · 7天陪伴计划',summary:'适合8岁儿童，每次约15分钟',days:[
    {day:1,items:[{name:'开合跳',target:20,unit:'次'},{name:'深蹲起',target:12,unit:'次'}]},
    {day:2,items:[{name:'高抬腿',target:30,unit:'次'},{name:'平板支撑',target:20,unit:'秒'}]},
    {day:3,items:[{name:'轻松活动',target:10,unit:'分钟'}]},
    {day:4,items:[{name:'开合跳',target:25,unit:'次'},{name:'深蹲起',target:15,unit:'次'}]},
    {day:5,items:[{name:'高抬腿',target:40,unit:'次'}]},
    {day:6,items:[{name:'亲子挑战',target:15,unit:'分钟'}]},
    {day:7,items:[{name:'拉伸与复盘',target:10,unit:'分钟'}]}
  ]}
};

const S=JSON.parse(JSON.stringify(BASE));
const PAGES = {
  home:{tab:'首页',icon:'⌂',html:homeHTML},
  tasks:{tab:'任务',icon:'☰',html:tasksHTML},
  ai:{tab:'AI',icon:'✦',html:aiHTML},
  growth:{tab:'成长',icon:'★',html:growthHTML},
  mine:{tab:'我的',icon:'☻',html:mineHTML},
  device:{tab:null,html:deviceHTML},
  library:{tab:null,html:libraryHTML},
  records:{tab:null,html:recordsHTML},
  analysis:{tab:null,html:analysisHTML},
  posture:{tab:null,html:postureHTML},
  profile:{tab:null,html:profileHTML}
};
const TABKEYS=['home','tasks','ai','growth','mine'];
let current='home';

function esc(s){return (s==null?'':String(s));}

// 线性小图标（状态行用，描边跟随文字颜色）
const svgBatt='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="2" y="8" width="17" height="9" rx="2.5"/><path d="M22 11v3"/><rect x="4.5" y="10.5" width="9" height="4" rx="1" fill="currentColor" stroke="none"/></svg>';
const svgWifi='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 9.5a14 14 0 0 1 18 0"/><path d="M6.5 13a9 9 0 0 1 11 0"/><path d="M10 16.5a4.5 4.5 0 0 1 4 0"/><circle cx="12" cy="19.5" r="1.2" fill="currentColor" stroke="none"/></svg>';
const svgLock='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5" y="10.5" width="14" height="9.5" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/></svg>';

// ---- page builders ----
function homeHTML(){
  const TASK_ICON={'开合跳':'jack','深蹲起':'squat'};
  const tasks=S.tasks.map(t=>`<div class="list-item"><div class="task-icon"><img src="assets/icons/${TASK_ICON[t.name]||'eq'}.png" alt=""></div><div class="grow"><div class="strong">${t.name} ${t.target}${t.unit}</div><div class="small muted">${t.time} · ${t.status}</div></div><text>›</text></div>`).join('');
  return `<div class="page">
    <div class="home-top"><span class="teamo-logo">TEAMO<text>✦</text></span><img class="ic" src="assets/icons/bell.png" alt="通知"></div>
    <div class="home-greet">晚上好，${S.profile.parentName}</div>
    <div class="home-slogan">一起动，更靠近</div>
    <div class="card hero-device"><div class="hd-info"><div class="hd-title">${S.profile.childName}的运动伙伴</div><div class="small muted">${S.device.name}</div><div class="hd-status"><span class="dot"></span>${S.device.online?'在线':'设备离线'}</div><div class="hd-line">${svgBatt}${S.device.battery}%</div><div class="hd-line">${svgLock}隐私盖已打开</div><div class="hd-link" onclick="open('device')">管理设备 ›</div></div><div class="hd-visual"><img src="assets/teamo-product.png" alt="Teamo 设备"></div></div>
    <button class="ai-cta"><span class="ai-mark"><img class="ic" src="assets/icons/sparkle.png" alt=""></span><div class="grow"><div class="strong">AI 运动计划助手</div><div class="small" style="color:#636366">安排今天的运动，陪伴每一步</div></div><text>制定计划 ›</text></button>
    <div class="shortcut-grid"><div class="shortcut" onclick="open('library')"><span class="tile-ic"><img class="ic" src="assets/icons/run-green.png" alt=""></span><div><div class="strong">快速训练</div><div class="small muted">科学动作，立即开始</div></div><text>›</text></div><div class="shortcut" onclick="open('growth')"><span class="tile-ic"><img class="ic" src="assets/icons/bars-green.png" alt=""></span><div><div class="strong">学伴成长</div><div class="small muted">记录进步，看见变化</div></div><text>›</text></div></div>
    <div class="section-title"><text>今日运动</text><text class="link" onclick="open('records')">查看详情</text></div>
    <div class="card split"><div class="metric"><b>${S.todayMinutes}<i>分钟</i></b><span>今日运动</span></div><div class="metric"><b>50<i>%</i></b><span>任务进度</span></div><div class="metric"><b>${S.streak}<i>天</i></b><span>连续运动</span></div></div>
    <div class="section-title"><text>今日任务</text><text class="link" onclick="open('tasks')">全部任务</text></div>
    <div class="list">${tasks}</div>
    <div class="privacy-note"><b>◉</b> 摄像头带物理遮挡，运动数据仅用于陪伴反馈</div>
  </div>`;
}

function deviceHTML(){
  return `<div class="page">
    <div class="devpage-head"><div class="devpage-title">${S.device.name}</div><div class="devpage-sub">${S.profile.childName}的运动伙伴</div></div>
    <div class="devpage-hero"><img src="assets/teamo-product.png" alt="Teamo 设备"></div>
    <div class="devpage-status"><div>${svgBatt}<b>${S.device.battery}%</b><span>电量</span></div><div>${svgWifi}<b>${S.device.online?'在线':'离线'}</b><span>${S.device.wifi}</span></div><div>${svgLock}<b>已打开</b><span>隐私盖</span></div></div>
    <div class="card devpage-workout"><div class="dw-head"><div class="strong">当前运动</div><span class="dw-chip">❚❚ 已暂停</span></div><div class="dw-body"><span class="task-icon"><img src="assets/icons/jack.png" alt=""></span><div class="grow"><div class="strong">开合跳 <b class="dw-count">12</b> / 20 次</div><div class="small muted">进度已保留</div></div><div class="dw-btns"><button class="btn btn-primary">继续运动</button><button class="btn btn-line">结束运动</button></div></div></div>
    <div class="list">
      <div class="list-item"><div class="grow"><div class="strong">设备设置</div><div class="small muted">名称、网络等设备信息</div></div><text>›</text></div>
      <div class="list-item" onclick="open('posture')"><div class="grow"><div class="strong">隐私与儿童数据</div><div class="small muted">数据使用与隐私保护</div></div><text>›</text></div>
    </div>
    <div class="privacy-note"><b>◉</b> 摄像头带物理遮挡，运动数据仅用于陪伴反馈</div>
  </div>`;
}

function libraryHTML(){
  const cards=S.actions.map(a=>`<div class="move-card ${a.color} ${a.available?'':'unavailable'}" onclick="selLib('${a.id}')"><div class="move-top"><div class="symbol">${a.short}</div><div class="stage-tag ${a.available?'ready':''}">${a.stage}</div></div><div class="strong">${a.name}</div><div class="small muted">${a.type}</div><div class="target-label">建议 ${a.target}${a.unit}</div></div>`).join('');
  return `<div class="page">
    <div class="brand-kicker">MOVE LIBRARY <text>7 ACTIONS</text></div><div class="hero-title">今天想练什么？</div><div class="hero-sub">选择动作后，可调整目标并直接发送给设备</div>
    <div class="library-grid">${cards}</div>
    <div class="detail-card"><div class="detail-head"><div><div class="small muted">动作说明</div><div class="detail-title">开合跳</div></div><text>×</text></div><div class="guide">双脚打开时双手举过头顶，合拢时回到身体两侧。</div><div class="hint"><b>陪伴提示</b>　手脚同步，动作打开到位</div><div class="form-label" style="display:block;font-size:12px;color:var(--muted);margin:14px 0 6px">本次目标</div><div class="stepper"><button>−</button><div>20<span>次</span></div><button>＋</button></div><button class="btn btn-primary full">立即发送到设备</button></div>
  </div>`;
}
function selLib(){}

function tasksHTML(){
  const list=S.tasks.map((t,i)=>`<div class="list-item"><div class="round">${i+1}</div><div class="grow"><div class="strong">${t.name}</div><div class="small muted">${t.source} · ${t.target}${t.unit} · ${t.time}</div><div class="task-receipt">${t.receipt}</div></div><div class="task-side"><div class="pill">${t.status}</div>${t.status==='待执行'?'<button class="pill cancel-btn">取消</button>':''}</div></div>`).join('');
  return `<div class="page">
    <div class="brand-kicker">PARENT JOURNEY <text>01</text></div><div class="hero-title">运动邀请</div><div class="hero-sub">发出邀请，Teamo 陪孩子完成挑战</div>
    <div class="journey"><div class="journey-item active"><text>1</text>发出邀请</div><div class="journey-line"></div><div class="journey-item"><text>2</text>设备提醒</div><div class="journey-line"></div><div class="journey-item"><text>3</text>完成得星</div></div>
    <div class="tabs"><button class="active">待进行</button><button>计划中</button><button>历史</button></div>
    <button class="btn btn-primary create">＋ 创建运动邀请</button>
    <div class="receipt-banner"><text>✓</text><div><div class="strong">设备已确认接收</div><div class="small">开合跳 · 今晚 19:00 已布置</div></div></div>
    <div class="section-title">任务列表</div>
    <div class="list">${list}</div>
  </div>`;
}

function aiHTML(){
  const rec=S.records[0];
  const days=S.plan.days.map(d=>`<div class="list-item"><div class="day">D${d.day}</div><div class="grow"><div class="strong">${d.items.map(e=>`${e.name} ${e.target} ${e.unit}`).join(' · ')}</div></div><text>›</text></div>`).join('');
  return `<div class="page">
    <div class="home-head"><div><div class="home-title">AI 运动助手</div><div class="home-sub">先看懂运动，再提供适度建议</div></div></div>
    <div class="insight-entry" onclick="open('analysis')"><span class="tile-ic"><img class="ic" src="assets/icons/doc.png" alt=""></span><div class="grow"><div class="strong">最近一次运动分析</div><div class="small muted">${rec.name} · ${rec.date}</div></div><text>›</text></div>
    <div class="module-title"><div><div class="strong">7 天运动计划</div><div class="small muted">循序渐进，帮你建立运动习惯</div></div><text class="link" onclick="open('tasks')">查看方案</text></div>
    <div class="plan-card"><div class="plan-head"><span class="tile-ic"><img class="ic" src="assets/icons/calendar.png" alt=""></span><div class="grow"><div class="strong">${S.plan.name}</div><div class="small muted">${S.plan.summary}</div></div></div><div class="plan-days day-list">${days}</div><div class="plan-actions"><button class="btn btn-line">调整条件</button><button class="btn btn-primary">确认今天计划</button></div></div>
    <div class="section-title">问问 AI</div>
    <div class="ask-card"><div class="ask-input"><span class="tile-ic ask-ic"><img class="ic" src="assets/icons/chat.png" alt=""></span><input placeholder="输入你的问题…" readonly><button class="ask-send" aria-label="发送"><img class="ic" src="assets/icons/send.png" alt=""></button></div><div class="quick-questions"><button>今天运动量够吗？</button><button>动作不标准怎么办？</button><button>如何坚持更久？</button></div><div class="ai-answer"><b>AI建议</b>　今天已累计 22 分钟，节奏稳定，明后天可保持类似安排，注意动作做到位。</div></div>
    <div class="ai-note">AI 建议仅用于日常运动陪伴，不替代医疗或专业训练意见。</div>
  </div>`;
}

function growthHTML(){
  const maxWeek=Math.max(...S.week.map(w=>w.value));
  const bars=S.week.map(w=>`<div class="bar-wrap"><div class="bar"><div style="height:${Math.max(10,Math.round(w.value/maxWeek*74))}px"></div></div><span>周${w.label}</span></div>`).join('');
  const rec=S.records[0];
  const totalValid=S.records.reduce((s,r)=>s+r.valid,0);
  return `<div class="page">
    <div class="home-head"><div><div class="home-title">成长</div><div class="home-sub">让每一次运动都有迹可循</div></div></div>
    <div class="buddy-card"><div class="buddy-face"><div class="buddy-eye"></div><div class="buddy-eye"></div></div><div class="grow"><div class="buddy-top"><div class="strong">学伴成长</div><text>›</text></div><div class="buddy-star-row"><b>${S.stars}</b><span>运动星</span><small>下一个目标 60</small></div><div class="buddy-progress"><div style="width:${Math.round(S.stars/60*100)}%"></div></div></div></div>
    <div class="card split overview"><div class="metric"><b>${S.todayMinutes}<i>分钟</i></b><span>今日运动</span></div><div class="metric"><b>${S.streak}<i>天</i></b><span>连续运动</span></div><div class="metric"><b>${S.stars}</b><span>运动星</span></div></div>
    <div class="section-title"><text>本周运动</text><text class="chart-unit">单位：分钟</text></div>
    <div class="card chart">${bars}</div>
    <div class="section-title"><text>记录与分析</text><text class="link" onclick="open('records')">全部记录</text></div>
    <div class="row-card" onclick="open('analysis')"><span class="tile-ic"><img class="ic" src="assets/icons/eq.png" alt=""></span><div class="grow"><div class="strong">运动分析 · 最近一次 ${rec.name}</div><div class="small muted">查看运动记录与完成情况</div></div><text>›</text></div>
    <div class="row-card" onclick="open('posture')"><span class="tile-ic"><img class="ic" src="assets/icons/bell.png" alt=""></span><div class="grow"><div class="strong">日常姿态提醒</div><div class="small muted">坐姿、低头与距离提醒 · 今天 ${S.postureAlerts} 次</div></div><text>›</text></div>
    <div class="section-title">本周亮点</div>
    <div class="highlight-grid"><div><b>${rec.score}</b><span>最近得分</span></div><div><b>${totalValid}</b><span>累计有效动作</span></div><div><b>${S.records.length}</b><span>完成记录</span></div></div>
    <div class="section-title">本周小结</div>
    <div class="row-card"><span class="tile-ic"><img class="ic" src="assets/icons/doc.png" alt=""></span><div class="grow"><div class="strong">稳定完成，循序渐进</div><div class="small muted">保持每次 10–15 分钟的轻量运动节奏</div></div></div>
  </div>`;
}

function mineHTML(){
  return `<div class="page">
    <div class="brand-kicker">TEAMO FAMILY <text>PROFILE</text></div>
    <div class="profile-card"><div class="avatar">夏</div><div><div class="name">${S.profile.parentName}</div><div class="small">${S.profile.childName}的家长 · 一起见证成长</div></div></div>
    <div class="family-switch"><div class="small muted">当前孩子</div><div class="child-pill"><text>${S.profile.childName}</text><text>${S.profile.age}岁</text></div><div class="switch-action">单孩子模式</div></div>
    <div class="section-title">家庭与设备</div>
    <div class="list">
      <div class="list-item" onclick="open('profile')"><div class="icon">童</div><div class="grow"><div class="strong">孩子信息</div><div class="small muted">${S.profile.childName} · ${S.profile.age}岁 · ${S.profile.goal}</div></div><text>›</text></div>
      <div class="list-item" onclick="open('device')"><div class="icon dark">器</div><div class="grow"><div class="strong">我的设备</div><div class="small muted">1 台 · ${S.device.name} · 在线</div></div><text>›</text></div>
    </div>
    <div class="section-title">设置</div>
    <div class="list">
      <div class="list-item"><div class="grow"><div class="strong">消息提醒</div><div class="small muted">任务完成、设备离线与姿态提醒</div></div><div class="pill">已开启</div></div>
      <div class="list-item" onclick="open('posture')"><div class="grow"><div class="strong">隐私与儿童数据</div><div class="small muted">查看采集范围和数据保存规则</div></div><text>›</text></div>
      <div class="list-item"><div class="grow"><div class="strong">使用帮助</div><div class="small muted">连接设备、布置任务与查看结果</div></div><text>›</text></div>
      <div class="list-item"><div class="grow"><div class="strong danger">重置演示数据</div></div><text>›</text></div>
    </div>
  </div>`;
}

function recordsHTML(){
  const total=S.records.length;
  const avg=Math.round(S.records.reduce((s,r)=>s+r.score,0)/total);
  const list=S.records.map(r=>`<div class="record-item" onclick="open('analysis')"><div class="score">${r.score}</div><div class="grow"><div class="record-title"><div class="strong">${r.name}</div><div class="record-status ${r.status==='已完成'?'':'warn'}">${r.status}</div></div><div class="small muted">${r.date} · ${r.actual}/${r.target} · ${r.duration}秒</div><div class="source">${r.source} · ${r.deviceName}</div></div><text>›</text></div>`).join('');
  return `<div class="page"><div class="brand-kicker">MOVE HISTORY <text>PROGRESS</text></div><div class="hero-title">运动记录</div><div class="hero-sub">每一次完成，都值得被看见</div>
    <div class="record-summary"><div><b>${total}</b><span>累计记录</span></div><div><b>${avg}</b><span>平均得分</span></div><div><b>${S.records[0].valid}</b><span>最近有效动作</span></div></div>
    <div class="section-title">全部记录</div>
    <div class="list record-list">${list}</div>
  </div>`;
}

function analysisHTML(){
  const r=S.records[0];
  const completion=Math.round(r.actual/r.target*100);
  const validRate=Math.round(r.valid/r.target*100);
  const issues=r.issues.map(i=>`<div class="list-item"><div class="warn">!</div><div class="grow"><div class="strong">${i}</div><div class="small muted">下一次运动时，设备会继续提醒</div></div></div>`).join('');
  return `<div class="page">
    <div class="brand-kicker">MOVE REPORT <text>AI INSIGHT</text></div>
    <div class="analysis-hero"><div class="small">最近一次运动</div><div class="hero-row"><div><div class="title">${r.name}</div><div class="small">${r.date} · 用时 ${r.duration} 秒</div><div class="record-meta">${r.status} · ${r.source} · ${r.deviceName}</div></div><div class="score">${r.score}</div></div></div>
    <div class="section-title">完成情况</div>
    <div class="card split"><div class="metric"><b>${completion}%</b><span>任务完成</span></div><div class="metric"><b>${r.valid}</b><span>有效动作</span></div><div class="metric"><b>${validRate}%</b><span>动作有效率</span></div></div>
    <div class="section-title">动作质量</div>
    <div class="card quality"><div class="quality-row"><span>动作完整度</span><div class="progress"><div style="width:${validRate}%"></div></div><span>${validRate}%</span></div><div class="quality-row"><span>节奏稳定性</span><div class="progress"><div style="width:88%"></div></div><span>88%</span></div><div class="quality-row"><span>站位情况</span><div class="progress"><div style="width:92%"></div></div><span>92%</span></div></div>
    <div class="section-title">本次姿态提醒</div>
    <div class="list">${issues}</div>
    <div class="section-title">AI 建议</div>
    <div class="ai-advice"><div class="ai">AI</div><div class="grow"><div class="advice-label">根据本次计数与动作事件生成</div>这次完成情况不错。下次可以保持速度，动作做到位后再加快节奏，不需要追求过快。</div></div>
    <div class="privacy">分析结果用于日常运动反馈，不作为医疗判断。</div>
  </div>`;
}

function postureHTML(){
  return `<div class="page">
    <div class="brand-kicker">POSTURE CARE <text>DAILY</text></div><div class="hero-title">日常姿态提醒</div><div class="hero-sub">温和提醒，不做医疗判断</div>
    <div class="posture-demo"><div class="row"><div class="posture-tag">坐姿</div><div class="grow small muted">提醒孩子背部挺直、不瘫坐</div></div><div class="row"><div class="posture-tag">低头</div><div class="grow small muted">低头过久时轻轻提示抬 head</div></div><div class="row"><div class="posture-tag">距离</div><div class="grow small muted">设备过近时提醒保持安全距离</div></div></div>
    <div class="card" style="margin-top:14px"><div class="strong">使用范围说明</div><div class="small muted" style="margin-top:6px;line-height:1.6">姿态提醒用于日常习惯引导，不能替代专业医疗或视力检查。如有持续不适，请咨询医生。</div></div>
  </div>`;
}

function profileHTML(){
  const p=S.profile;
  return `<div class="page">
    <div class="brand-kicker">CHILD PROFILE <text>EDIT</text></div><div class="hero-title">孩子资料</div>
    <div class="profile-card"><div class="avatar" style="width:50px;height:50px;font-size:18px">${p.childName[0]}</div><div><div class="name">${p.childName}</div><div class="small">${p.grade} · ${p.goal}</div></div></div>
    <div class="list" style="margin-top:14px">
      <div class="list-item"><div class="grow"><div class="strong">年龄</div></div><div class="pill">${p.age} 岁</div></div>
      <div class="list-item"><div class="grow"><div class="strong">运动目标</div></div><div class="pill">${p.goal}</div></div>
      <div class="list-item"><div class="grow"><div class="strong">年级</div></div><div class="pill">${p.grade}</div></div>
    </div>
  </div>`;
}


return {base:BASE,render(page,data){Object.assign(S,JSON.parse(JSON.stringify(BASE)),data);const builder=PAGES[page]||PAGES.home;return builder.html().replace(/onclick="(?:open|go)\('([^']+)'\)"/g,(_,p)=>`data-flow="nav-${p}"`).replace(/onclick="selLib\('([^']+)'\)"/g,(_,id)=>`data-flow="move-${id}"`);}};
})();

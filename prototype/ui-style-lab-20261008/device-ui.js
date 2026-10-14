/* Device UE adapter: shared task/session facts, device-only preparation state. */
let deviceUE={phase:'idle',present:false,countdown:3,epoch:0,timer:null,note:'本地模拟 · 未接真实视觉'};
function deviceStopTimer(){deviceUE.epoch++;if(deviceUE.timer!==null)clearTimeout(deviceUE.timer);deviceUE.timer=null;}
function devicePrepare(){const s=flow.getState();if(!s.privacyOpen){deviceUE.note='请先打开隐私盖';render();return;}if(s.task?.status!=='ready'&&s.session?.status!=='paused'){deviceUE.note='请先接收运动任务';render();return;}deviceStopTimer();deviceUE.phase='entry';deviceUE.present=false;deviceUE.note='请站入画面';render();}
function deviceTick(){const e=deviceUE.epoch;deviceUE.timer=setTimeout(()=>{if(e!==deviceUE.epoch||deviceUE.phase!=='countdown')return;deviceAdvance();},1000);}
function deviceAdvance(){const s=flow.getState();if(deviceUE.phase!=='countdown')return;if(!s.privacyOpen||!deviceUE.present){deviceStopTimer();deviceUE.phase='entry';render();return;}deviceUE.countdown--;if(deviceUE.countdown<=0){deviceStopTimer();deviceUE.phase='running';flow.dispatch({type:s.session?.status==='paused'?'RESUME':'START'});}else{render();deviceTick();}}
function deviceAction(a){const s=flow.getState();
 if(a==='receive'){if(s.task?.status==='waiting'){flow.dispatch({type:'DEVICE_ACK',commandId:s.task.commandId});deviceUE.note='任务已收到，可开始或稍后进行';}render();return;}
 if(a==='prepare'){devicePrepare();return;}
 if(a==='present'){deviceUE.present=true;if(deviceUE.phase==='away')deviceUE.phase='entry';deviceUE.note='站位已确认（模拟）';render();return;}
 if(a==='countdown'){if(deviceUE.phase!=='entry'||!deviceUE.present||!s.privacyOpen)return;deviceStopTimer();deviceUE.phase='countdown';deviceUE.countdown=3;render();deviceTick();return;}
 if(a==='away'){deviceStopTimer();deviceUE.present=false;deviceUE.phase='away';autoCount=false;if(s.session?.status==='running')flow.dispatch({type:'PAUSE'});else render();return;}
 if(a==='pause'){deviceStopTimer();deviceUE.phase='paused';autoCount=false;flow.dispatch({type:'PAUSE'});return;}
 if(a==='count'){if(!deviceUE.present||!s.privacyOpen||s.session?.status!=='running')return;flow.dispatch({type:'COUNT',amount:1});if(flow.getState().session.count>=s.session.target){deviceUE.phase='result';flow.dispatch({type:'FINISH'});}return;}
 if(a==='finish'){deviceStopTimer();autoCount=false;deviceUE.phase='result';flow.dispatch({type:'FINISH'});return;}
 if(a==='privacy'){deviceStopTimer();deviceUE.present=false;deviceUE.phase='entry';autoCount=false;flow.dispatch({type:'PRIVACY',open:!s.privacyOpen});return;}
 if(a==='online'){flowAction('online');return;}
 if(a==='sync'){flowAction('sync');return;}
 if(a==='later'){deviceStopTimer();deviceUE.phase='idle';deviceUE.note='任务留在待办，不自动开始';render();return;}
 if(a==='idle'){if(s.session&&['running','paused'].includes(s.session.status)){deviceUE.note='请先结束本次运动';render();return;}deviceStopTimer();deviceUE.phase='idle';render();return;}
}

/* ════ 屏内 UI（移植自 Teamo设备端UE展示.html：Rev3 表情系统 + Rev4 手绘 SVG 屏内图标） ════
   视图只做「共享状态 → 屏上内容」映射；交互动作仍由上方 deviceAction 状态机承担。
   强调色走 var(--dev-brand)，跟随手机端皮肤；方屏(rect)整体收一档。 */
const DEV_INK='#F6F8F2';
function devSvg(vb,inner,w,alt){return `<svg width="${w}" height="${w}" viewBox="0 0 ${vb} ${vb}" fill="none" role="img" aria-label="${alt||''}">${inner}</svg>`}
function svgCamOff(w){return devSvg(96,`<g stroke="${DEV_INK}" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 30h8l6-9h20l6 9h20v42a6 6 0 0 1-6 6H24a6 6 0 0 1-6-6z" fill="rgba(246,248,242,.08)"/><circle cx="48" cy="52" r="13"/><path d="M14 86 82 14" stroke-width="8"/></g>`,w,'摄像头已遮挡')}
function svgPersonFrame(w){return devSvg(96,`<g stroke="var(--dev-brand)" stroke-width="6.5" stroke-linecap="round" fill="none"><path d="M14 30V20a6 6 0 0 1 6-6h10"/><path d="M66 14h10a6 6 0 0 1 6 6v10"/><path d="M82 66v10a6 6 0 0 1-6 6H66"/><path d="M30 82H20a6 6 0 0 1-6-6V66"/></g><g fill="${DEV_INK}"><circle cx="48" cy="39" r="11.5"/><path d="M22 82v-1.5C22 65 33.5 56 48 56s26 9 26 24.5V82z"/></g>`,w,'站位引导')}
function svgCheck(w){return devSvg(96,`<path d="M24 52 42 70 74 30" stroke="var(--dev-brand)" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`,w,'完成')}
function devEyes(cls){
  const BARS='<i class="f-bar"></i><i class="f-bar"></i>';
  if(cls==='happy')return `<div class="eyes happy"><i class="f-arc"></i><i class="f-arc"></i><i class="f-smile"></i></div>`;
  if(cls==='celebrate')return `<div class="eyes celebrate"><i class="f-arc"></i><i class="f-arc"></i><span class="f-spark s1">✦</span><span class="f-spark s2">✦</span></div>`;
  if(cls==='alert')return `<div class="eyes alert">${BARS}<i class="f-dot"></i></div>`;
  return `<div class="eyes ${cls}">${BARS}</div>`;
}
function deviceScreen(kind){
  const s=flow.getState(),t=s.task,q=s.session;
  const sm=kind==='rect';
  const b=(a,n,p)=>`<button type="button" class="${p?'primary':''}" data-device="${a}">${n}</button>`;
  const unitOf=a=>/平板/.test(a||'')?'秒':'次';
  const view=inner=>`<div class="device-view">${inner}</div>`;
  /* 隐私盖关闭：摄像头遮挡 + 停止计数（图标+文字，不靠颜色单表意） */
  if(!s.privacyOpen)return view(`${svgCamOff(sm?60:78)}<b class="screen-title" style="font-size:${sm?14:16}px">隐私盖已关闭</b><p class="screen-copy">摄像头已遮挡，计数已停止</p>`);
  /* 倒计时 */
  if(deviceUE.phase==='countdown')return view(`<div class="countdown-num">${deviceUE.countdown}</div><p class="screen-copy">准备开始</p><div class="screen-btns">${b('later','取消准备')}</div>`);
  /* 站位引导 / 离开画面 */
  if(deviceUE.phase==='entry')return deviceUE.present
    ? view(`${svgPersonFrame(sm?76:94)}<b class="screen-title">很好，就站这里！</b><p class="screen-copy">马上准备开始</p><div class="screen-btns">${b('countdown','开始倒计时',1)}</div>`)
    : view(`${svgPersonFrame(sm?76:94)}<b class="screen-title">让我看到完整的你</b><p class="screen-copy">站到我前面，再往后一点点</p><div class="screen-btns">${b('present','我已入镜',1)}</div>`);
  if(deviceUE.phase==='away')return view(`${devEyes('look-left')}<b class="screen-title">我在等你～</b><p class="screen-copy">已经帮你记住 ${q?q.count:0} ${unitOf(q&&q.action)}</p><div class="screen-btns">${b('present','我回来了',1)}</div>`);
  /* 运动中：大数字 + 细进度条 + 分段鼓励语（数值来自手机端共享会话） */
  if(q&&q.status==='running'){
    const pct=Math.min(100,q.count/q.target*100);
    const fb=q.count>=q.target?'完成！':q.count>=Math.ceil(q.target*.75)?'快完成啦！':q.count>=Math.ceil(q.target*.5)?'一半啦！':q.count>=5?'做得不错！':'';
    return view(`<div class="screen-kicker">${q.action}</div><div class="big-count">${q.count}<small> / ${q.target}</small></div><div class="progress-bar"><i style="width:${pct}%"></i></div><div class="feedback">${fb}</div><div class="screen-btns">${b('pause','暂停')}${b('finish','结束')}</div>`);
  }
  /* 已暂停 */
  if(q&&q.status==='paused')return view(`${devEyes('sleepy')}<b class="screen-title">休息一下～</b><p class="screen-copy">${q.count} / ${q.target}，我帮你记住啦</p><div class="screen-btns">${b('prepare','继续',1)}${b('finish','结束')}</div>`);
  /* 完成：达标庆祝（笑眼+星星+运动星）/ 未达标结果回执 */
  if(q&&q.status==='finished'&&deviceUE.phase!=='idle'){
    if(q.count>=q.target)return view(`${devEyes('celebrate')}<b class="screen-title">太棒啦！</b><p class="screen-copy">${q.count} / ${q.target} · <span class="celebrate-points">+8 运动星</span></p><div class="screen-btns">${b('idle','回到待机',1)}</div>`);
    return view(`<div class="screen-kicker">这次运动</div>${svgCheck(sm?42:52)}<b class="screen-title">${q.action}</b><p class="screen-copy">${s.online?'结果已经同步给家长':'结果已保存在本机'}</p><div class="screen-btns">${b('idle','回到待机',1)}</div>`);
  }
  /* 新任务到达（家长下发，手机端 CREATE→ACCEPTED 后等待设备确认） */
  if(t&&t.status==='waiting')return view(`${devEyes('alert')}<b class="screen-title">你有新任务啦！</b><p class="screen-copy">家长发来 · ${t.action} ${t.target} ${unitOf(t.action)}</p><div class="screen-btns">${b('receive','接收任务',1)}</div>`);
  /* 待办运动（设备已确认，待孩子开始） */
  if(t&&t.status==='ready')return view(`<div class="screen-kicker">待办运动</div><b class="screen-title">${t.action} × ${t.target} ${unitOf(t.action)}</b><p class="screen-copy">设备已确认，随时可以开始</p><div class="screen-btns">${b('prepare','准备运动',1)}${b('later','稍后')}</div>`);
  /* 离线：结果本机保存、联网自动同步 */
  if(!s.online)return view(`${devEyes('alert')}<b class="screen-title">网络暂时断开</b><p class="screen-copy">运动结果已保存在本机<br>连接恢复后会自动同步</p><div class="screen-btns">${b('online','重新连接',1)}</div>`);
  /* 待机：表情 + 时钟 + 今日完成数 */
  const doneN=(s.records||[]).length;
  const now=new Date(),hh=String(now.getHours()).padStart(2,'0'),mm=String(now.getMinutes()).padStart(2,'0');
  return view(`${devEyes('rest')}<div class="big-count" style="font-size:${sm?20:26}px;letter-spacing:1px">${hh}:${mm}</div><p class="screen-copy">今天已完成 ${doneN} 项 · 加油！</p>`);
}
function devicePanel(){const s=flow.getState();return `<div class="device-demo-controls"><p>${deviceUE.note}</p><button data-device="count">模拟动作 +1</button><button data-device="away">模拟离开画面</button><button data-device="privacy">${s.privacyOpen?'关闭':'打开'}隐私盖</button><button data-device="online">${s.online?'模拟离线':'恢复联网'}</button><button data-device="sync">模拟补传</button></div>`;}
function bindDevice(){document.querySelectorAll('[data-device]').forEach(b=>b.addEventListener('click',()=>deviceAction(b.dataset.device)));}
let devicePrevSession=null;
flow.subscribe(s=>{if(!s.privacyOpen){deviceStopTimer();deviceUE.present=false;}if(s.session?.status==='finished'&&devicePrevSession!=='finished'){deviceStopTimer();deviceUE.phase='result';}devicePrevSession=s.session?s.session.status:null;if(!s.task){deviceStopTimer();deviceUE.phase='idle';deviceUE.present=false;}});

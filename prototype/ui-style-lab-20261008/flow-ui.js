const originalDemoData=JSON.parse(JSON.stringify(S));

function originalFlowScreen(B,dir,page,mod){
 const s=flow.getState(),t=s.task,q=s.session,r=s.records.find(x=>x.id===selectedRecord)||s.records[0],cls={clear:'eb',warm:'cl',arena:'kp'}[dir];
 Object.assign(S,JSON.parse(JSON.stringify(originalDemoData)));Object.assign(rec0,originalDemoData.records[0]);RATE.completion=100;RATE.valid=Math.round(rec0.valid/rec0.target*100);
 S.device.online=s.online;if(extras.deviceName)S.device.name=escapeHTML(extras.deviceName);if(extras.childName)S.profile.childName=escapeHTML(extras.childName);
 S.tasks=[];
 if(t&& !['finished','cancelled'].includes(t.status))S.tasks=[{name:t.action,target:t.target,unit:'次',source:'家长邀请',time:'本次演示',status:labels[t.status],receipt:t.status==='ready'?'设备已确认':labels[t.status]}];
 if(r){Object.assign(rec0,{name:r.action,date:'本次演示',actual:r.count,target:r.target,valid:'—',duration:'—',score:'—',status:r.completed?'目标完成':'提前结束',source:'家长邀请',deviceName:S.device.name});RATE.completion=Math.round(r.count/r.target*100);RATE.valid=0;}
 const btn=(act,label)=>`<button type="button" class="${cls}-btn flow-button" data-flow="${act}">${label}</button>`;
 const navIcon={home:'home-green',tasks:'check',ai:'sparkle',growth:'bars-green',mine:'person'};
 const nav=`<nav class="flow-nav" aria-label="手机导航">${[['home','首页'],['tasks','任务'],['ai','AI'],['growth','成长'],['mine','我的']].map(([p,n])=>`<button type="button" class="${p==='ai'?'flow-nav-ai':''}" data-flow="${'nav-'+p}" aria-current="${page===p?'page':'false'}"><img class="nav-ic" src="assets/icons/${navIcon[p]}.png" alt="" aria-hidden="true"><span>${n}</span></button>`).join('')}</nav>`;
 if(page==='tasks'&&filter==='history')S.tasks=s.records.map(x=>({name:x.action,target:x.target,unit:'次',source:'家长邀请',time:'本次演示',status:x.completed?'已完成':'提前结束',receipt:x.sync==='synced'?'已同步':'待同步'}));
 if(page==='tasks'&&filter==='planned')S.tasks=extras.plans.map(x=>({name:x.action,target:x.target,unit:'次',source:'本地计划',time:x.time.replace('T',' '),status:'计划中',receipt:'尚未发送到设备'}));
 let content=mvpScreen(page),tailExtras='';
 if(page==='tasks')tailExtras+=`<div class='flow-inline-state' role='status'>${escapeHTML(s.notice)}<br>${S.tasks.length?'':filter==='history'?'还没有运动记录':filter==='planned'?'还没有计划，可以创建定时邀请':'暂无进行中的任务'}</div>`+(filter==='planned'?extras.plans.map((x,i)=>btn('plan-send-'+i,'发送 '+x.action)+btn('plan-delete-'+i,'删除该计划')).join(''):filter==='history'?s.records.map(x=>btn('record-'+x.id,x.action+' '+x.count+'/'+x.target+'次 · 查看详情')).join(''):'');
 if(page==='tasks'&&!creating&&t&&['waiting','sending','ready','retry'].includes(t.status))tailExtras+=btn('cancel','取消当前任务');
 const receipt=t?(labels[t.status]||'等待确认'):'尚未创建本次任务';
 content=content.replaceAll('设备已确认接收',receipt).replaceAll('开合跳 · 今晚 19:00 已布置',t?`${t.action} · ${t.target}次 · 本次演示`:'点击创建运动邀请开始演示');
 if(page==='device'){
  const controls=`<div class="flow-original-controls"><div class="flow-inline-state">${escapeHTML(s.notice)}${q?`<br><b>${q.action} ${q.count}/${q.target}次 · ${q.status==='paused'?'已暂停':q.status==='finished'?'已结束':'运动中'}</b>`:''}</div>${t?.status==='sending'?btn('reject','模拟发送失败'):''}${t?.status==='waiting'?btn('ack','模拟设备确认'):''}${t?.status==='retry'?btn('retry','重试发送'):''}${q&&['running','paused'].includes(q.status)?btn(q.status==='running'?'pause':'resume',q.status==='running'?'暂停运动':'继续运动')+btn('count','模拟动作 +1')+btn('auto',autoCount?'停止自动计数':'自动演示计数')+btn('finish','结束并保存'):''}${btn('privacy',s.privacyOpen?'模拟关闭隐私盖':'模拟打开隐私盖')}</div>`;
  content=content.replace('<div class="page">','<div class="page">'+controls);
  content=content.replaceAll('在线待机',!s.online?'离线':q?labels[t.status]:'在线待机').replaceAll('真实状态','演示状态');tailExtras+=btn('panel-settings','家庭与设备设置');
 }
 if(page==='analysis')content=(r?`<div class="flow-inline-state">${r.action} ${r.count}/${r.target}次 · 设备已保存 · ${{pending:'待同步',syncing:'同步中',synced:'已同步'}[r.sync]}</div>`:'')+(r&&r.sync!=='synced'?btn('sync','模拟补传确认'):'')+content;
 if(tailExtras)content=content.replace(/<\/div><\/div><\/div>$/,tailExtras+'</div></div></div>');
 const modal=creating?`<section class="flow-modal" role="dialog" aria-modal="true" aria-label="创建运动邀请">${flowPage(dir,'tasks')}</section>`:'';
 return content+nav+modal+auxiliaryModal(dir);
}
function bindOriginalControls(){
 const root=document.querySelector('.sc');if(!root)return;
 const activate=(el,act)=>{el.setAttribute('role','button');el.setAttribute('tabindex','0');el.addEventListener('click',()=>flowAction(act));el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();flowAction(act);}});};
 root.querySelectorAll('.eb-btn,.cl-btn,.kp-btn,.mvp .btn,.mvp .ai-cta').forEach(el=>{if(el.hasAttribute('data-flow'))return;const label=el.textContent.trim();if(label.includes('AI 运动计划助手'))activate(el,'nav-ai');else if(label.includes('创建运动邀请'))activate(el,'create');else if(label.includes('模拟离线')){el.textContent=flow.getState().online?'模拟离线':'恢复联网';activate(el,'online');}else if(label.includes('开始开合跳')){el.textContent=flow.getState().task?.status==='ready'?'开始运动':'查看当前任务';activate(el,flow.getState().task?.status==='ready'?'start':'nav-tasks');}});
 root.querySelectorAll('.eb-tag,.cl-sub,.kp-sub').forEach(el=>{if(el.textContent.trim()==='取消')activate(el,'cancel');});
 root.querySelectorAll('.eb-tabs span,.cl-tabs span,.kp-tabs span,.mvp .tabs button').forEach(el=>{const f=el.textContent.trim()==='历史'?'history':el.textContent.trim()==='计划中'?'planned':'active';el.classList.toggle('on',filter===f);el.classList.toggle('active',filter===f);el.setAttribute('aria-pressed',String(filter===f));activate(el,'filter-'+f);});
 const linkCard=(text,act)=>{const node=Array.from(root.querySelectorAll('b,.eb-lbl,.cl-kick,.kp-kick,.eb-cell')).find(el=>el.textContent.trim()===text);const card=node?.closest('.eb-cell,.cl-clay,.cl-stat,.kp-card')||Array.from(root.querySelectorAll('.eb-cell,.cl-clay,.cl-stat,.kp-card')).find(el=>el.textContent.trim().startsWith(text));if(card&&!card.hasAttribute('role'))activate(card,act);};
 if(STATE.page==='home'){[['AI 运动计划助手','panel-assistant'],['快速训练','panel-training'],['学伴成长','panel-growth'],['姿态提醒','panel-posture'],['我的设备','nav-device'],['今日运动','nav-analysis'],['今日任务','nav-tasks'],['最近运动','nav-analysis']].forEach(([x,a])=>linkCard(x,a));root.querySelectorAll('b').forEach(el=>{if(el.textContent.trim()===S.device.name)activate(el.closest('.eb-cell,.cl-clay,.kp-card')||el,'nav-device');if(el.textContent.trim()===rec0.name)activate(el.closest('.eb-row,.cl-clay,.kp-row')||el,'nav-analysis');});}
 root.querySelectorAll('.mv-privacy-note,.mvp .privacy-note').forEach(el=>activate(el,'panel-privacy'));
 root.querySelectorAll('.eb-spec').forEach(el=>{if(el.textContent.includes('设备名称'))activate(el,'panel-settings');});
 root.querySelectorAll('.flow-modal').forEach(el=>el.addEventListener('keydown',e=>{if(e.key==='Escape'){creating=false;panel=null;render();}if(e.key==='Tab'){const a=Array.from(el.querySelectorAll('button,input,select,[tabindex="0"]')).filter(x=>!x.disabled);if(!a.length)return;const first=a[0],last=a[a.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}}));
}

/* UI controllers consume the shared flow; all three skins use this layer. */
let storage;try{storage=window.localStorage;}catch(_){}
const flow=TeamoFlow.createStore({storage});
let draft={action:'开合跳',target:20,time:''},filter='active',creating=false,autoCount=false;
let panel=null,selectedRecord=null;
let extras={plans:[],reminders:true};try{Object.assign(extras,JSON.parse(storage?.getItem('teamo-mobile-extras-v1')||'{}'));}catch(_){}
function saveExtras(){try{storage?.setItem('teamo-mobile-extras-v1',JSON.stringify(extras));}catch(_){}}
const labels={sending:'发送中',waiting:'等待设备确认',ready:'待开始',running:'运动中',paused:'已暂停',finished:'已结束',cancelled:'已取消',retry:'发送失败'};
const escapeHTML=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function flowPage(dir,page){
 const s=flow.getState(),t=s.task,q=s.session,r=s.records[0],cls={clear:'eb',warm:'cl',arena:'kp'}[dir];
 const button=(action,label,disabled=false)=>`<button type="button" class="${cls}-btn flow-button" data-flow="${action}" ${disabled?'disabled':''}>${label}</button>`;
 const box=inner=>`<div class="flow-block">${inner}</div>`;
 const title=word=>`<div class="${cls}-h1">${word}</div>`;
 const state= t?labels[t.status]:'暂无任务';
 const summary=()=>box(t?`<b>${t.action} · ${t.target}次</b><p>${state}</p><p>${q?q.count+'/'+q.target+' 次 · '+(q.status==='running'?'正在运动':'计数已保存'): '开始后显示运动计数'}</p>`:'还没有运动任务');
 const main=()=>!t||['finished','cancelled'].includes(t.status)?button('create','＋ 创建运动邀请'):['sending','waiting'].includes(t.status)?button('device','查看设备确认'):t.status==='retry'?button('retry','重试发送'):t.status==='ready'?button('start','开始运动'):button('device','查看运动进度');
 const navIcon={home:'home-green',tasks:'check',ai:'sparkle',growth:'bars-green',mine:'person'};
 const tabs=`<nav class="flow-nav" aria-label="手机底部导航">${[['home','首页'],['tasks','任务'],['ai','AI'],['growth','成长'],['mine','我的']].map(([p,n])=>`<button type="button" class="${p==='ai'?'flow-nav-ai':''}" data-flow="${'nav-'+p}" aria-current="${page===p?'page':'false'}"><img class="nav-ic" src="assets/icons/${navIcon[p]}.png" alt="" aria-hidden="true"><span>${n}</span></button>`).join('')}</nav>`;
 let body='';
 if(page==='home')body=title('和小宇，一起动起来')+box(`<b>客厅运动伙伴</b><p>${s.online?'设备在线':'设备离线'} · ${s.privacyOpen?'隐私盖打开':'隐私盖关闭'}</p>`)+summary()+main()+(r?box(`<b>最近一次 · ${r.action}</b><p>${r.count}/${r.target}次 · ${r.completed?'目标完成':'提前结束'} · ${r.sync==='synced'?'已同步':'待同步'}</p>`)+button('analysis','查看运动记录'):'');
 if(page==='tasks'){
  body=title('运动邀请');
  if(creating)body+=`<form id="flow-task-form"><label for="flow-action">运动项目</label><select id="flow-action" name="action">${['开合跳','深蹲起'].map(a=>`<option ${draft.action===a?'selected':''}>${a}</option>`).join('')}</select><label for="flow-target">目标次数（1–200）</label><input id="flow-target" name="target" type="number" min="1" max="200" step="1" required value="${draft.target}"><label for="flow-time">计划时间（可选，留空立即发送）</label><input id="flow-time" name="time" type="datetime-local" value="${escapeHTML(draft.time||'')}"><p class="flow-muted">定时计划仅保存在本机，需手动发送。发送后先等待后台受理，再等待设备确认。</p><button type="submit" class="${cls}-btn flow-button">发送到设备</button>${button('close-create','返回任务列表')}</form>`;
  else body+=`<div class="flow-filters">${[['active','进行中'],['history','历史']].map(([v,n])=>`<button type="button" data-flow="filter-${v}" aria-pressed="${filter===v}">${n}</button>`).join('')}</div>`+(filter==='active'?summary()+main()+(t&&['waiting','ready','retry','sending'].includes(t.status)?button('cancel','取消任务'):''):s.records.map(x=>box(`<b>${x.action}</b><p>${x.count}/${x.target} 次 · ${x.completed?'目标完成':'提前结束'} · ${x.sync==='synced'?'已同步':'待同步'}</p>`)).join('')||box('还没有运动记录'));
 }
 if(page==='device'){
  body=title('客厅运动伙伴')+box(`<b>${s.online?'设备在线':'设备离线'}</b><p>${state} · ${s.privacyOpen?'隐私盖打开':'隐私盖关闭'}</p>`)+button('online',s.online?'模拟断网':'恢复联网')+button('privacy',s.privacyOpen?'模拟关闭隐私盖':'模拟打开隐私盖');
  if(t&&t.status==='waiting')body+=button('ack','模拟设备确认',!s.online);
  if(t&&t.status==='retry')body+=button('retry','重试发送');
  if(t&&t.status==='ready')body+=button('start','开始运动',!s.privacyOpen);
  if(q&&['running','paused'].includes(q.status))body+=box(`<p>${q.action}</p><div class="flow-count">${q.count}<small> / ${q.target}</small></div><progress max="${q.target}" value="${q.count}"></progress><p>${q.status==='running'?'运动中':'已暂停'} · 模拟计数</p>`)+button(q.status==='running'?'pause':'resume',q.status==='running'?'暂停运动':'继续运动',!s.privacyOpen)+button('count','模拟一个动作 +1',q.status!=='running')+button('auto',autoCount?'停止自动演示':'自动演示计数',q.status!=='running')+button('finish','结束并保存');
  else if(q&&q.status==='finished')body+=summary()+button('analysis','查看结果');
  else if(!t)body+=button('create','先创建运动任务');
 }
 if(page==='analysis')body=title('运动记录')+(r?box(`<b>${r.action}</b><div class="flow-count">${r.count}<small> / ${r.target}</small></div><p>${r.completed?'目标已完成':'运动提前结束'}</p><dl><dt>设备保存</dt><dd>已保存（演示）</dd><dt>云端同步</dt><dd>${{pending:'待同步',syncing:'同步中',synced:'已同步'}[r.sync]}</dd></dl><p class="flow-muted">只展示计数事实；质量评分与AI建议尚未接入。</p>`)+(r.sync==='synced'?'':button('sync','模拟补传确认',!s.online||r.sync==='syncing'))+button('create','再创建一次运动'):box('完成一次运动后，这里会显示结果。')+button('create','创建运动任务'));
 return pg(cls,`<div class="flow-notice" role="status">${escapeHTML(s.notice)}</div>${body}${tabs}`);
}
function sendCurrent(){
 const t=flow.getState().task;if(!t||t.status!=='sending')return;
 // Replace this mock with backend command admission; DEVICE_ACK remains a separate device event.
 setTimeout(()=>flow.dispatch({type:'ACCEPTED',commandId:t.commandId}),500);
}
function flowAction(action){
 if(action==='ask'){panel='ai-answer';render();return;}
 if(action==='close-panel'){panel=null;render();return;}
 if(action.startsWith('panel-')){panel=action.slice(6);render();return;}
 if(action==='reminders'){extras.reminders=!extras.reminders;saveExtras();render();return;}
 if(action==='use-plan'){panel=null;draft={action:'开合跳',target:20,time:''};flowAction('create');return;}
 if(action.startsWith('record-')){selectedRecord=action.slice(7);STATE.page='analysis';render();return;}
 if(action.startsWith('plan-delete-')){extras.plans.splice(Number(action.slice(12)),1);saveExtras();render();return;}
 if(action.startsWith('plan-send-')){const i=Number(action.slice(10)),p=extras.plans[i];if(!p)return;const before=flow.getState().task;flow.dispatch({type:'CREATE',id:'task-'+Date.now(),action:p.action,target:p.target});if(flow.getState().task?.id!==before?.id){extras.plans.splice(i,1);saveExtras();filter='active';sendCurrent();}render();return;}
 if(action.startsWith('nav-')){STATE.page=action.slice(4);creating=false;panel=null;render();return;}
 if(action.startsWith('filter-')){filter=action.slice(7);render();return;}
 const s=flow.getState();
 if(action.startsWith('move-')){const a=MVPViews.base.actions.find(x=>x.id===action.slice(5));if(!a?.available){panel='unsupported';render();return;}draft={action:a.name,target:a.target,time:''};flowAction('create');return;}
 if(action==='ai-today'){draft={action:'开合跳',target:20,time:''};flowAction('create');return;}
 if(['device','analysis'].includes(action)){STATE.page=action;render();return;}
 if(action==='create'){STATE.page='tasks';panel=null;creating=true;render();return;}
 if(action==='close-create'){creating=false;render();return;}
 if(action==='auto'){if(s.session?.status!=='running')return;autoCount=!autoCount;render();return;}
 if(action==='reset'){autoCount=false;creating=false;panel=null;selectedRecord=null;extras={plans:[],reminders:true};saveExtras();flow.dispatch({type:'RESET'});return;}
 if(action==='online'){flow.dispatch({type:'ONLINE',online:!s.online});return;}
 if(action==='privacy'){autoCount=false;flow.dispatch({type:'PRIVACY',open:!s.privacyOpen});return;}
 if(action==='reject'&&s.task){flow.dispatch({type:'REJECTED',commandId:s.task.commandId});return;}
 if(action==='ack'&&s.task){flow.dispatch({type:'DEVICE_ACK',commandId:s.task.commandId});return;}
 if(action==='sync'){
  flow.dispatch({type:'SYNC'});const ids=flow.getState().records.filter(r=>r.sync==='syncing').map(r=>r.id);
  setTimeout(()=>ids.forEach(id=>flow.dispatch({type:'SYNC_ACK',recordId:id})),650);return;
 }
 const map={start:'START',pause:'PAUSE',resume:'RESUME',count:'COUNT',finish:'FINISH',cancel:'CANCEL',retry:'RETRY'};
 if(map[action]){if(['pause','finish','cancel'].includes(action))autoCount=false;if(action==='finish'){STATE.page='analysis';selectedRecord=null;}flow.dispatch({type:map[action],amount:1});if(action==='retry')sendCurrent();}
}
function bindFlow(){
 bindOriginalControls();
 document.querySelectorAll('[data-flow]').forEach(b=>{const s=flow.getState(),a=b.dataset.flow;if(['count','auto'].includes(a))b.disabled=s.session?.status!=='running';if(a==='ack')b.disabled=!s.online;if(a==='sync')b.disabled=!s.online||s.records.some(r=>r.sync==='syncing');b.addEventListener('click',()=>flowAction(a));});
 const settings=document.getElementById('flow-settings');if(settings)settings.addEventListener('submit',e=>{e.preventDefault();if(!settings.reportValidity())return;extras.deviceName=settings.elements.deviceName.value.trim();extras.childName=settings.elements.childName.value.trim();saveExtras();panel=null;render();});
 const dialog=document.querySelector('.flow-modal');if(dialog)dialog.querySelector('input,select,button')?.focus({preventScroll:true});
 const form=document.getElementById('flow-task-form');
 if(form){form.addEventListener('input',()=>{form.elements.time.setCustomValidity('');draft={action:form.elements.action.value,target:Number(form.elements.target.value),time:form.elements.time.value};});form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;draft={action:form.elements.action.value,target:Number(form.elements.target.value),time:form.elements.time.value};if(draft.time){if(new Date(draft.time).getTime()<=Date.now()){form.elements.time.setCustomValidity('请选择未来时间');form.reportValidity();return;}extras.plans.push({...draft});saveExtras();creating=false;filter='planned';draft.time='';render();return;}const before=flow.getState().task;const id='task-'+Date.now()+'-'+Math.random().toString(36).slice(2,7);creating=false;flow.dispatch({type:'CREATE',id,...draft});const after=flow.getState().task;if(after&&after.id!==before?.id)sendCurrent();});}
}
function refreshFlow(){if(flow.getState().session?.status!=='running')autoCount=false;const s=flow.getState();D.action=s.task?.action||'开合跳';D.target=s.task?.target||20;D.current=s.session?.count||0;STATE.deviceState=s.session?.status==='finished'?'done':s.session?'run':'idle';render();}
flow.subscribe(refreshFlow);
setInterval(()=>{const s=flow.getState();if(autoCount&&s.session?.status==='running'){flow.dispatch({type:'COUNT',amount:1});const q=flow.getState().session;if(q.count>=q.target){autoCount=false;STATE.page='analysis';flow.dispatch({type:'FINISH'});}}},850);

const restored=flow.getState();D.action=restored.task?.action||"开合跳";D.target=restored.task?.target||20;D.current=restored.session?.count||0;STATE.deviceState=restored.session?.status==="finished"?"done":restored.session?"run":"idle";

function auxiliaryModal(dir){
 if(!panel)return '';const cls={clear:'eb',warm:'cl',arena:'kp'}[dir];
 const button=(a,n)=>`<button type="button" class="${cls}-btn flow-button" data-flow="${a}">${n}</button>`;
 const records=flow.getState().records,total=records.reduce((n,r)=>n+r.count,0);
 const sections={
 assistant:['运动计划助手',`<p>示例方案：开合跳 20 次。家长确认后才会创建邀请。</p>${button('use-plan','采用方案并编辑')}`],
 training:['快速训练',`<p>当前可演示开合跳、深蹲起两种动作；其余动作等待算法确认。</p>${button('use-plan','选择动作与次数')}`],
 growth:['学伴成长',`<p>本机演示累计完成 ${records.length} 次运动，共 ${total} 次动作。</p><p>目标达成 ${records.filter(r=>r.completed).length} 次。</p>`],
 posture:['姿态提醒',`<p>尚未接入姿态检测，不生成真实提醒记录。</p>${button('reminders',extras.reminders?'关闭提醒偏好':'开启提醒偏好')}<p>当前偏好：${extras.reminders?'开启':'关闭'}（仅本机保存）</p>`],
 privacy:['隐私与数据',`<p>演示只保存任务、计数和设置，不采集或保存视频。</p><p>关闭隐私盖会暂停会话，重新打开后需手动继续。</p>${button('privacy',flow.getState().privacyOpen?'模拟关闭隐私盖':'模拟打开隐私盖')}${button('panel-reset','清除本机演示数据')}`],
 settings:['家庭与设备设置',`<form id="flow-settings"><label>孩子昵称<input name="childName" required maxlength="20" value="${escapeHTML(extras.childName||originalDemoData.profile.childName)}"></label><label>设备名称<input name="deviceName" required maxlength="30" value="${escapeHTML(extras.deviceName||originalDemoData.device.name)}"></label><button class="${cls}-btn flow-button" type="submit">保存设置</button></form><p>仅修改本机演示信息，不更改真实设备。</p>`],
 'ai-answer':['AI演示回答','<p>保持规律运动，动作做到位，疲劳时休息。当前是固定演示回答，不分析真实孩子数据，也未调用AI服务。</p>'],
 unsupported:['动作待适配','<p>该动作尚未接入演示计数，当前可选择开合跳或深蹲起。</p>'],
 help:['使用帮助','<p>从动作库或AI页创建邀请，进入设备页模拟确认，再开始、计数和结束。联网后可补传记录。</p>'],
 reset:['清除演示数据',`<p>将删除本机任务、运动记录、计划和设置。</p>${button('reset','确认清除')}`]
 };const [title,body]=sections[panel]||['功能说明','此功能尚未接入服务。'];
 return `<section class="flow-modal" role="dialog" aria-modal="true" aria-label="${title}">${pg(cls,`<h2>${title}</h2>${body}${button('close-panel','关闭')}`)}</section>`;
}
const MOBILE_ONLY=typeof location!=='undefined'&&new URLSearchParams(location.search).get('mobile')==='1';
function renderMobile(){
 const d=DIRS.find(x=>x.k===STATE.direction)||DIRS[0],v=[d.restore,...d.variants][STATE.version]||d.restore;
 document.body.classList.add('mobile-only');
 const app=document.getElementById('app'),old=app.querySelector('.sc-scroll'),scroll=lastRenderedPage===STATE.page&&old?old.scrollTop:0;
 app.innerHTML=`<header class="mobile-toolbar"><label>风格<select id="mobile-theme">${DIRS.map(x=>`<option value="${x.k}" ${x.k===d.k?'selected':''}>${x.name}</option>`).join('')}</select></label><button data-flow="panel-settings">设置</button></header><main class="mobile-app">${screenHTML(v.skin,d.k,STATE.page,v.mod)}</main>`;
 lastRenderedPage=STATE.page;const sc=app.querySelector('.sc-scroll');if(sc)sc.scrollTop=scroll;
 bindFlow();document.getElementById('mobile-theme').addEventListener('change',e=>{STATE.direction=e.target.value;STATE.version=0;render();});
}

function mvpScreen(page){
 const state=flow.getState(),task=state.task,records=state.records;
 const convert=r=>({id:r.id,name:r.action,date:new Date(r.endedAt).toLocaleString('zh-CN'),actual:r.count,target:r.target,valid:0,duration:'—',score:'—',status:r.completed?'已完成':'提前结束',source:'家长邀请',deviceName:S.device.name,issues:['质量识别尚未接入']});
 const rows=records.map(convert),record=records.find(r=>r.id===selectedRecord)||records[0];
 const data={profile:{...MVPViews.base.profile,...S.profile},device:S.device,tasks:S.tasks,records:record?[convert(record),...rows.filter(r=>r.id!==record.id)]:MVPViews.base.records};
 let html=MVPViews.render(page,data);
 html=html.replaceAll('小宇',S.profile.childName).replace('抬 head','抬头');
 html=html.replace('class="notice"','class="notice" data-flow="nav-ai"').replace('class="device-card"','class="device-card" data-flow="nav-device"');
 html=html.replace('class="card device-card"','class="card device-card" data-flow="nav-device"');
 html=html.replace('class="ai-cta"','class="ai-cta" data-flow="nav-ai"');
 html=html.replace(/<div class="action-card ([^"]+)">/g,((i)=>function(_,c){return `<div class="action-card ${c}" data-flow="move-${MVPViews.base.actions[i++].id}">`;})(0));
 
 if(page==='tasks')html=html.replace('class="pill cancel-btn"','class="pill cancel-btn" data-flow="cancel"');
 if(page==='ai'){
  html=html.replace('>调整条件</button>',' data-flow="create">调整条件</button>').replace('>确认今天计划</button>',' data-flow="ai-today">确认今天计划</button>');
  html=html.replace('readonly','id="mvp-question" maxlength="200"').replace('class="ask-send"','class="ask-send" data-flow="ask"');
  html=html.replace(/<button>(今天运动量够吗？|动作不标准怎么办？|如何坚持更久？)<\/button>/g,'<button data-flow="ask">$1</button>');
 }
 if(page==='mine'){
  html=html.replace('data-flow="nav-posture"','data-flow="panel-privacy"');
  for(const [text,action] of [['消息提醒','reminders'],['使用帮助','panel-help'],['重置演示数据','panel-reset']])html=html.replace(new RegExp('<div class="list-item">(?=<div class="grow"><div class="strong(?: danger)?">'+text+')'),`<div class="list-item" data-flow="${action}">`);
  html=html.replace('已开启',extras.reminders?'已开启':'已关闭');
 }
 if(page==='profile')html+=`<button class="btn btn-primary full" data-flow="panel-settings">编辑孩子资料</button>`;
 if(page==='growth'){const total=records.reduce((n,r)=>n+r.count,0);html=html.replace('<div class="section-title"><text>本周运动</text>',`<div class="section-title">本机运动记录</div><div class="card split"><div class="metric"><b>${records.length}</b><span>运动次数</span></div><div class="metric"><b>${total}</b><span>累计计数</span></div><div class="metric"><b>${records.filter(r=>r.completed).length}</b><span>目标达成</span></div></div><div class="section-title"><text>本周运动</text>`);}
 if(page==='records')html=`<div class="page"><div class="hero-title">运动记录</div><div class="hero-sub">本机演示 · ${records.length} 条</div><div class="list">${rows.map(r=>`<div class="list-item" data-flow="record-${r.id}"><div class="grow"><div class="strong">${r.name} · ${r.actual}/${r.target}次</div><div class="small muted">${r.date} · ${r.status}</div></div><span>›</span></div>`).join('')||'<div class="list-item">还没有运动记录</div>'}</div></div>`;
 const back=['home','tasks','ai','growth','mine'].includes(page)?'':`<button class="back-link" data-flow="nav-${page==='device'||page==='profile'?'mine':'growth'}">‹ 返回</button>`;
 html=html.replace('<div class="page">','<div class="page">'+back);
 return `<div class="sc-scroll"><div class="mvp">${html}</div></div>`;
}

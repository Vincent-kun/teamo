/* Shared UI domain model. No DOM, skin or network dependency. */
(function(root,factory){if(typeof module==='object'&&module.exports)module.exports=factory();else root.TeamoFlow=factory();})(typeof globalThis!=='undefined'?globalThis:this,function(){
 const fresh=()=>({version:1,online:true,privacyOpen:true,task:null,session:null,records:[],notice:'创建一项运动任务，开始演示。'});
 const copy=x=>JSON.parse(JSON.stringify(x));
 function reduce(previous,event){
  const s=copy(previous),task=s.task,session=s.session;
  const refuse=text=>{s.notice=text;return s;};
  switch(event.type){
   case 'CREATE':
    if(task&&!['cancelled','finished'].includes(task.status))return refuse('请先结束或取消当前任务。');
    if(!['开合跳','深蹲起'].includes(event.action)||!Number.isInteger(event.target)||event.target<1||event.target>200)return refuse('请选择支持的动作，目标为1–200次整数。');
    s.task={id:event.id,commandId:event.id+'-create',action:event.action,target:event.target,status:'sending'};s.session=null;s.notice='发送中：尚未收到设备确认。';break;
   case 'ACCEPTED':
    if(!task||task.commandId!==event.commandId||task.status!=='sending')return s;
    task.status='waiting';s.notice='后台已受理，等待设备确认。';break;
   case 'REJECTED':
    if(task&&task.commandId===event.commandId&&task.status==='sending'){task.status='retry';s.notice='发送失败，可用同一命令ID重试。';}break;
   case 'RETRY':
    if(task&&task.status==='retry'){task.status='sending';s.notice='正在重试同一命令。';}break;
   case 'DEVICE_ACK':
    if(!task||task.commandId!==event.commandId||task.status!=='waiting'||!s.online)return s;
    task.status='ready';s.notice='设备已确认接收，等待孩子开始。';break;
   case 'START':
    if(!task||task.status!=='ready')return refuse('请等待设备确认任务后再开始。');
    if(!s.privacyOpen)return refuse('隐私盖已关闭，请先打开再开始。');
    s.session={id:task.id+'-session',taskId:task.id,count:0,target:task.target,action:task.action,status:'running',startedAt:event.now||Date.now()};task.status='running';s.notice='运动中：计数为模拟输入。';break;
   case 'COUNT':
    if(!session||session.status!=='running'||!s.privacyOpen)return s;
    session.count=Math.min(session.target,session.count+Math.max(0,event.amount||1));break;
   case 'PAUSE':if(session&&session.status==='running'){session.status='paused';task.status='paused';s.notice='已暂停，计数保持。';}break;
   case 'RESUME':
    if(!s.privacyOpen)return refuse('隐私盖关闭时不能恢复识别。');
    if(session&&session.status==='paused'){session.status='running';task.status='running';s.notice='已恢复运动。';}break;
   case 'PRIVACY':
    s.privacyOpen=!!event.open;
    if(!s.privacyOpen&&session&&session.status==='running'){session.status='paused';task.status='paused';}
    s.notice=s.privacyOpen?'隐私盖已打开；恢复运动需主动确认。':'隐私盖已关闭，采集与计数停止。';break;
   case 'ONLINE':s.online=!!event.online;s.notice=s.online?'设备已联网，可确认任务与补传记录。':'设备离线：本地模拟运动可继续，结果等待补传。';break;
   case 'FINISH':
    if(!session||!['running','paused'].includes(session.status))return refuse('没有可结束的运动会话。');
    session.status='finished';task.status='finished';
    s.records.unshift({id:session.id+'-record',sessionId:session.id,taskId:task.id,action:session.action,count:session.count,target:session.target,completed:session.count>=session.target,saved:true,sync:'pending',endedAt:event.now||Date.now()});s.notice='运动已结束，设备已保存，等待同步。';break;
   case 'SYNC':
    if(!s.online)return refuse('当前离线，记录保留在设备，联网后重试。');
    s.records.forEach(r=>{if(r.sync!=='synced')r.sync='syncing';});s.notice='正在补传，尚未获得云端确认。';break;
   case 'SYNC_ACK':
    if(!s.online)return s;
    s.records.forEach(r=>{if(r.id===event.recordId&&r.sync==='syncing')r.sync='synced';});s.notice='云端已确认记录。';break;
   case 'CANCEL':
    if(task&&['sending','waiting','ready','retry'].includes(task.status)){task.status='cancelled';s.notice='演示任务已取消，旧回执不会再次启动。';}else return refuse('运动进行中请使用结束运动。');break;
   case 'RESET':return fresh();
  }
  return s;
 }
 function createStore(options={}){
  let state=fresh(),listeners=[];
  if(options.storage){try{const cached=JSON.parse(options.storage.getItem('teamo-ui-flow-v1'));if(cached&&cached.version===1&&Array.isArray(cached.records)&&typeof cached.online==='boolean'){state=cached;if(state.session&&state.session.status==='running'){state.session.status='paused';if(state.task)state.task.status='paused';state.notice='恢复了本地演示，运动已暂停。';}state.records.forEach(r=>{if(r.sync==='syncing')r.sync='pending';});if(state.task&&state.task.status==='sending')state.task.status='retry';}}catch(_){}}
  return {getState:()=>copy(state),subscribe(fn){listeners.push(fn);return ()=>listeners=listeners.filter(x=>x!==fn);},dispatch(event){state=reduce(state,event);if(options.storage){try{options.storage.setItem('teamo-ui-flow-v1',JSON.stringify(state));}catch(_){state.notice='浏览器保存失败，刷新后可能丢失本次演示。';}}listeners.forEach(fn=>fn(copy(state)));return copy(state);}};
 }
 return {fresh,reduce,createStore};
});

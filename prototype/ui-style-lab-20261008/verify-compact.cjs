const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const code=[...html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)].map(m=>{const src=m[1].match(/src="([^"]+)"/);return src?fs.readFileSync(__dirname+'/'+src[1],'utf8'):m[2];}).join('\n');
let active=[];
const app={innerHTML:'',querySelectorAll(selector){
 if(selector==='[data-control]'){
 active=[...this.innerHTML.matchAll(/<button[^>]*data-control="([^"]+)"[^>]*data-value="([^"]+)"[^>]*>/g)].map(m=>({dataset:{control:m[1],value:m[2]},addEventListener(_,fn){this.click=fn;}}));return active;
 }return [];
},querySelector(){return {focus(){}};}};
const document={getElementById(id){return id==='app'?app:null;},documentElement:{style:{setProperty(){}}}};
document.querySelector=()=>null;document.querySelectorAll=()=>[];const window={};
const context=vm.createContext({document,console,window,setInterval:()=>0,setTimeout:()=>0,clearTimeout:()=>0});vm.runInContext(code,context);
function snapshot(){assert.equal((app.innerHTML.match(/class="phone"/g)||[]).length,1);assert.equal((app.innerHTML.match(/class="dev-unit"/g)||[]).length,1);assert(!app.innerHTML.includes('undefined'));}
snapshot();
active.find(x=>x.dataset.control==='page'&&x.dataset.value==='growth').click();
active.find(x=>x.dataset.control==='direction'&&x.dataset.value==='clear').click();
assert.equal(vm.runInContext('STATE.page',context),'growth');
active.find(x=>x.dataset.control==='version'&&x.dataset.value==='1').click();
assert.equal(vm.runInContext('STATE.version',context),1);snapshot();
let count=0;
for(const direction of ['clear'])for(let version=0;version<3;version++)for(const page of ['home','tasks','device','analysis']){
 vm.runInContext(`Object.assign(STATE,${JSON.stringify({direction,version,page})});render()`,context);snapshot();count++;
}
for(const direction of ['clear'])for(let version=0;version<3;version++)for(const shape of ['round'])for(const deviceState of ['idle','run','done']){
 vm.runInContext(`Object.assign(STATE,${JSON.stringify({direction,version,shape,deviceState})});render()`,context);snapshot();count++;
}
console.log(JSON.stringify({passed:true,renderCases:count,phoneCount:1,deviceCount:1,skinSwitchPreservesPage:true,note:'Node VM structural/control checks; no browser visual or layout verification'},null,2));

vm.runInContext("flow.dispatch({type:'CREATE',id:'ui',action:'开合跳',target:2});flow.dispatch({type:'ACCEPTED',commandId:'ui-create'});flowAction('device');flowAction('ack');flowAction('start');flowAction('count');flowAction('pause');flowAction('count');",context);
assert.equal(vm.runInContext('flow.getState().session.count',context),1);
vm.runInContext("flowAction('resume');flowAction('count');flowAction('finish');",context);
assert.equal(vm.runInContext('STATE.page',context),'analysis');assert.equal(vm.runInContext('flow.getState().records[0].count',context),2);snapshot();console.log('PASS: UI controllers drive task ACK/start/count/pause/resume/finish and route to results');

for(const panel of ['assistant','training','growth','posture','privacy','settings','reset']){
 vm.runInContext(`flowAction('panel-${panel}')`,context);assert(app.innerHTML.includes('role="dialog"'));assert(!app.innerHTML.includes('undefined'));vm.runInContext("flowAction('close-panel')",context);
}
vm.runInContext("flowAction('filter-planned');extras.plans.push({action:'深蹲起',target:3,time:'2030-01-01T19:00'});flowAction('nav-tasks');render();",context);
assert(app.innerHTML.includes('plan-send-0'));vm.runInContext("flowAction('plan-send-0')",context);
assert.equal(vm.runInContext('extras.plans.length',context),0);assert.equal(vm.runInContext('flow.getState().task.action',context),'深蹲起');
vm.runInContext("extras.plans.push({action:'开合跳',target:2,time:'2030-01-01T19:00'});flowAction('plan-send-0')",context);
assert.equal(vm.runInContext('extras.plans.length',context),1);vm.runInContext("flowAction('plan-delete-0')",context);assert.equal(vm.runInContext('extras.plans.length',context),0);
document.body={classList:{add(){}}};const baseGet=document.getElementById;document.getElementById=id=>id==='mobile-theme'?{addEventListener(){}}:baseGet(id);
for(const direction of ['clear'])for(const page of ['home','tasks','device','analysis']){vm.runInContext(`Object.assign(STATE,${JSON.stringify({direction,page})});renderMobile()`,context);assert(app.innerHTML.includes('mobile-app'));assert(!app.innerHTML.includes('class="dev-unit"'));assert(!app.innerHTML.includes('undefined'));}
vm.runInContext("flowAction('panel-reset');flowAction('reset')",context);assert.equal(vm.runInContext('flow.getState().records.length',context),0);
console.log('PASS: auxiliary panels, planned task send/delete/admission guard, 12 standalone mobile screens, reset');

for(const direction of ['clear'])for(const page of ['home','tasks','ai','growth','mine','device','library','records','analysis','posture','profile']){
 vm.runInContext(`Object.assign(STATE,${JSON.stringify({direction,page})});render()`,context);snapshot();
 const navigation=[...app.innerHTML.matchAll(/data-flow="nav-(home|tasks|ai|growth|mine)" aria-current/g)].map(m=>m[1]);assert.deepEqual(navigation,['home','tasks','ai','growth','mine']);
}
vm.runInContext("STATE.page='home';render()",context);
for(const label of ['运动伙伴','AI 运动计划助手','快速训练','学伴成长','今日运动','立即开始','今日任务','管理设备'])assert(app.innerHTML.includes(label));
vm.runInContext("flowAction('nav-ai')",context);for(const label of ['7 天运动计划','基础体能','问问 AI','最近一次运动分析'])assert(app.innerHTML.includes(label));
console.log('PASS: MVP baseline 11 pages × 3 skins, five-tab order, home module presence and AI full page');

vm.runInContext("flowAction('nav-growth')",context);assert.equal(vm.runInContext('STATE.page',context),'growth');for(const text of ['本机运动记录','本周运动','日常姿态提醒','本周亮点','本周小结','nav-records','nav-posture'])assert(app.innerHTML.includes(text));console.log('PASS: growth navigation, complete MVP growth modules and secondary links');

vm.runInContext("flowAction('reset');flow.dispatch({type:'CREATE',id:'dev-ue',action:'开合跳',target:2});flow.dispatch({type:'ACCEPTED',commandId:'dev-ue-create'});deviceAction('receive');deviceAction('prepare');deviceAction('countdown');",context);
assert.equal(vm.runInContext('deviceUE.phase',context),'entry');
vm.runInContext("deviceAction('present');deviceAction('countdown');deviceAdvance();deviceAdvance();deviceAdvance();deviceAction('count');deviceAction('away');deviceAction('count');",context);
assert.equal(vm.runInContext('flow.getState().session.count',context),1);assert.equal(vm.runInContext('flow.getState().session.status',context),'paused');
vm.runInContext("deviceAction('prepare');deviceAction('present');deviceAction('countdown');deviceAction('privacy');deviceAdvance();",context);assert.equal(vm.runInContext('flow.getState().session.status',context),'paused');
vm.runInContext("deviceAction('privacy');deviceAction('prepare');deviceAction('present');deviceAction('countdown');deviceAdvance();deviceAdvance();deviceAdvance();deviceAction('online');deviceAction('count');",context);
assert.equal(vm.runInContext('flow.getState().records[0].count',context),2);assert.equal(vm.runInContext('flow.getState().records[0].sync',context),'pending');
console.log('PASS: device receipt, entry guard, countdown, away pause, privacy cancellation, offline finish');

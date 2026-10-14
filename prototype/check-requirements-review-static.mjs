import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const output = path.join(dir, 'requirements-review-evidence');
fs.mkdirSync(output, { recursive: true });
const html = fs.readFileSync(path.join(dir, 'requirements-review-workbench.html'), 'utf8');
const model = JSON.parse(fs.readFileSync(path.join(dir, 'requirements-review-model.json'), 'utf8'));
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
new vm.Script(script); // Syntax validation of the generated, embedded model and all handlers.
const checks=[];
const check=(label,value)=>{assert.ok(value,label);checks.push(label);};
const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
check('Static HTML identifiers are unique',new Set(ids).size===ids.length);
check('Generated page has four named semantic tab panels', ['trace','state','decision','delivery'].every(x=>ids.includes('view-'+x)&&ids.includes('tab-'+x)));
for(const [key,p] of Object.entries(model.files))check(`Source document exists: ${key}`,fs.existsSync(path.join(dir,'..',p)));
for(const r of model.requirements){
  check(`${r.id} software references exist`,r.software.every(s=>model.software.some(x=>x.id===s)));
  check(`${r.id} decision references exist`,r.decisions.every(d=>model.decisions.some(x=>x.id===d)));
}
check('Original first-version seven actions remain in model',model.requirements.filter(r=>/^R0[2-8]$/.test(r.id)).length===7);
check('No requirement is marked approved or verified by generation',model.requirements.every(r=>r.reviewStatus==='待确认'&&r.evidenceStatus==='未登记'));
check('All transition endpoints refer to real state nodes',model.transitions.every(t=>model.states.some(s=>s[0]===t[0])&&model.states.some(s=>s[0]===t[1])));
check('Every transition carries event, guard and action',model.transitions.every(t=>t.length===5&&t.every(v=>typeof v==='string'&&v.length)));

// Isolated code execution uses minimal element stubs. It is not a browser,
// DOM/layout implementation, click test or screenshot/visual acceptance.
const elements=new Map();
function element(id){
  if(!elements.has(id))elements.set(id, {id,innerHTML:'',textContent:'',value:'',hidden:false,style:{},attributes:{},listeners:{},
    elements:Object.fromEntries(['scope','owner','notes','choice'].map(k=>[k,{value:''}])),
    addEventListener(type,fn){this.listeners[type]=fn;},setAttribute(k,v){this.attributes[k]=v;},appendChild(){},scrollIntoView(){},remove(){},focus(){},click(){},
  });
  return elements.get(id);
}
for(const id of ids)element(id);
for(const x of ['scope','owner','notes','choice'])element(x);
element('req-module').value='all';
const tabs=['start','trace','state','decision','delivery'].map(k=>Object.assign(element('tab-'+k),{dataset:{tab:k}}));
const groups=['open','base'].map(k=>Object.assign(element('group-'+k),{dataset:{decisionGroup:k}}));
const document={ getElementById:element,querySelectorAll:selector=>selector==='[role=tab][data-tab]'?tabs:selector==='[data-decision-group]'?groups:[],querySelector:selector=>selector==='[role=tablist]'?element('tablist'):null,addEventListener(){},createElement:()=>element('created'),activeElement:tabs[0] };
const context=vm.createContext({document,console,Blob,URL:{createObjectURL:()=> 'blob:local-test',revokeObjectURL(){}},setTimeout:()=>0,Date,Set,Map,JSON,encodeURI});
vm.runInContext(script.replace(/\n}\s*$/, '\nglobalThis.reviewEval = code => eval(code);\n}'),context);
const run = code => context.reviewEval(code);
check('Default entry explains one workout instead of opening the engineering ledger',element('view-start').hidden===false&&element('view-trace').hidden===true);
check('Reader entry includes all eight detailed stages', (element('story-steps').innerHTML.match(/data-story=/g)||[]).length===8);
check('Every stage separates concrete operations, alternatives and verification',model.stageDesign.every(s=>s.operations.length===3&&s.options.length>=2&&s.verify&&s.refs.length));
run('storyIndex=6;renderStory()');
check('Save design distinguishes durable local commit, streaming and acknowledgement',element('story-detail').innerHTML.includes('Outbox')&&element('story-detail').innerHTML.includes('流式')&&element('story-detail').innerHTML.includes('ACK'));
run('storyIndex=4;renderStory()');
check('Count example is clearly illustrative and retains pause recovery explanation',element('story-detail').innerHTML.includes('非真实识别数据')&&element('story-detail').innerHTML.includes('记13'));
check('All view renderers execute without undefined identifiers',element('req-detail').innerHTML.includes('R03')&&element('state-detail').innerHTML.includes('SPORT_ACTIVE')&&element('decision-detail').innerHTML.includes('OPEN-001')&&element('acceptance-table').innerHTML.includes('S25'));
run("selectedReq='R08';renderReqDetail()");
check('Effective hold time survives source-to-view rendering',element('req-detail').innerHTML.includes('不能用会话用时充当成绩'));
run("selectedReq='R30';renderReqDetail()");
check('Offline recognition renders as existing PRD requirement',element('req-detail').innerHTML.includes('PRD已有明确要求'));
run("selectedState='pause';renderStates()");
check('Pause rendering retains progress and pending recovery decision',element('state-detail').innerHTML.includes('13')&&element('transition-table').innerHTML.includes('OPEN-006'));
run("selectedDecision='OPEN-001';decisionGroup='open';selectedOption=2;renderDecisions()");
check('Option preview keeps decision unaccepted',element('decision-detail').innerHTML.includes('未改变范围或方案状态')&&element('decision-detail').innerHTML.includes('非已接受 ADR'));
run("draft.requirements.R03={scope:'建议本次纳入',owner:'<script>unsafe</script>',notes:'草稿'};selectedReq='R03';renderReqDetail()");
check('Draft preserves all three authority/evidence axes',element('req-detail').innerHTML.includes('REVIEW / 未批准')&&element('req-detail').innerHTML.includes('证据未登记'));
check('HTML encoding blocks executable content in rendered string',run("escapeHTML('<script>unsafe</script>')")==='&lt;script&gt;unsafe&lt;/script&gt;');
element('req-search').value='R23';run('renderReqList()');
check('Search resolves school requirement rather than dropping it from scope',element('req-list').innerHTML.includes('R23')&&element('list-count').textContent==='1 / 45');
run("switchView('state')");
check('View switch separates semantic panels',element('view-trace').hidden&&element('view-state').hidden===false);
const evidence={ checkedAt:new Date().toISOString(),status:'passed',checks,limitations:[
  'Static data/reference integrity, JavaScript compilation and isolated renderer logic only.',
  'No real DOM click, download/upload, screenshot, responsive layout or real hardware verification.',
  'Headless browser launch failed in the sandbox; application browser policy explicitly blocks tool access to file URLs. No workaround attempted after the policy rejection.',
]};
fs.writeFileSync(path.join(output,'static-review.json'),JSON.stringify(evidence,null,2)+'\n');
fs.writeFileSync(path.join(output,'browser-review.json'),JSON.stringify({status:'not-run',reason:'Headless browser launch unavailable; subsequent file:// tool access rejected by browser policy. Browser layout and interaction acceptance remain pending.',checks:[],realHardwareAcceptance:false},null,2)+'\n');
console.log(JSON.stringify({status:'passed',checks:checks.length,browserAcceptance:'pending',evidence:'prototype/requirements-review-evidence/static-review.json'}));

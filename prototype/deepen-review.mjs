import fs from 'node:fs';
const p='prototype/requirements-review-template.html';
let t=fs.readFileSync(p,'utf8');
t=t.replace('repeat(7,minmax(0,1fr))','repeat(4,minmax(0,1fr))');
t=t.replace('storyIndex=4','storyIndex=0');
t=t.replace('1. 孩子怎样完成一次运动？','1. 每一步怎样操作，为什么选这个方案？');
t=t.replace('点击任一步查看说明','点击步骤查看操作、方案与软硬件需求');
t=t.replace('这条主线要先跑通：收到目标 → 站好 → 开始运动 → 计数 → 保存 → 家长查看。孩子自己选运动是另一条入口，是否本次展示还需确定。','先看具体操作，再比较实现方案。下列推荐均待确认；每一步分别列出软件、硬件、异常和验收要求。');
const start=t.indexOf('const story=['),end=t.indexOf('function titleText',start);
if(start<0||end<0)throw Error('Renderer boundaries');
t=t.slice(0,start)+`const story=MODEL.stageDesign;
function renderStory(){
  byId('story-steps').innerHTML=story.map((s,i)=>\`<button class="story-step" data-story="\${i}" aria-pressed="\${i===storyIndex}"><small>第 \${i+1} 步</small><strong>\${escapeHTML(s.title)}</strong><small>操作 → 方案 → 需求</small></button>\`).join('');
  const s=story[storyIndex];
  const table=(headers,rows)=>'<div class="table-wrap"><table><thead><tr>'+headers.map(h=>'<th>'+h+'</th>').join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+r.map(c=>'<td>'+escapeHTML(c)+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>';
  byId('story-detail').style.display='block';
  byId('story-detail').innerHTML=\`<h3>\${escapeHTML(s.title)}</h3><p style="margin:12px 0"><strong>推荐候选，待评审：</strong>\${escapeHTML(s.recommendation)}</p><h3>具体怎样操作</h3>\${table(['操作','用户动作','屏幕 / 声音 / 异常反馈','对应软件需求','对应硬件需求'],s.operations)}<h3 style="margin-top:22px">形式与实现方案比较</h3>\${table(['方案','优势','代价与限制','软件增加什么','硬件增加什么'],s.options)}<div class="plain-facts" style="margin-top:20px"><div><strong>数据与控制怎样交接</strong><p>\${escapeHTML(s.flow)}</p></div><div><strong>怎样验证选得对</strong><p>\${escapeHTML(s.verify)}</p></div>\${s.extra?'<div><strong>保存、流式与器件选择的区别</strong><p>'+escapeHTML(s.extra)+'</p></div>':''}</div><div class="tools" style="margin-top:16px">\${s.refs.map(id=>\`<button class="btn small" data-go="\${id.startsWith('R')?'trace':'decision'}" data-target="\${id}">\${id.startsWith('R')?'回查PRD':'待讨论'} \${id}</button>\`).join('')}</div>\`;
  byId('plain-questions').innerHTML=[['本次开放哪些动作？','D02'],['孩子在远处怎样开始/暂停/继续？','OPEN-006'],['什么程度的站位和计数才算通过？','D07'],['示范媒体用什么形式？','OPEN-001'],['掉电、断网和存储满怎样保住成绩？','D10']].map(q=>\`<button class="discussion-item" data-go="decision" data-target="\${q[1]}"><strong>\${q[0]}</strong><span>讨论 →</span></button>\`).join('');
}
`+t.slice(end);
fs.writeFileSync(p,t);
const test='prototype/check-requirements-review-static.mjs';
let c=fs.readFileSync(test,'utf8').replace('all seven use steps','all eight detailed stages').replace('length===7','length===8');
c=c.replace("includes('非真实识别数据')","includes('非真实识别数据')");
fs.writeFileSync(test,c);

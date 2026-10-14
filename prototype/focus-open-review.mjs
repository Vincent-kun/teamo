import fs from 'node:fs';
const p='prototype/requirements-review-template.html';let t=fs.readFileSync(p,'utf8');
const items=[
['待确认范围','11月15日到底演示哪些真实功能？','手机端初步方案沿用。需要确认两种动作是否都能实机演示，以及AI、学校、成长等功能本次做到哪一步。','D02'],
['待确认操作','孩子在远处怎样开始、暂停和继续？','机身按键、语音或手势尚需收口；按键后怎样回位、恢复是否再倒计时也要明确。','OPEN-006'],
['待确认表达','小屏怎样教动作、提示站位和显示计数？','图标加语音、动画还是视频？“姿态展示”是站位轮廓、动作反馈还是日常体态？不能当作同一个功能。','OPEN-003'],
['需要实测','怎样才算站好了、数对了？','需要确定全身动态覆盖、稳定时间、误计漏计、反馈延迟，以及样本和环境；不是重新讨论要不要计数。','D07'],
['待验证实现','断网继续运动，候选主控能否做到？','离线执行已有要求；要验证本地识别、显示、声音同时运行时的性能、发热和稳定性。','D03'],
['待确认保存','断电、存储满、上传失败时怎样保住成绩？','建议本地可靠保存再补传。仍需明确检查点、允许损失、保留期、失败提示与删除规则。','D10'],
['已有口径冲突','手机端离线发送和设备接收怎样统一？','页面写离线后自动同步，代码却拦截发送；模拟返回也不能代表真实设备已收到。只核对这处差异。','D11'],
['已有口径冲突','视频是否允许写入设备存储？','产品边界是原始视频不持久化，部分文档写不长期保存；需要统一措辞，并区分教学素材与孩子相机视频。','D08'],
['待落实安排','谁负责、什么时候确认、怎样验收？','每项留下承接人、确认日期与通过条件。没有证据就记录待验证，不因已有页面标记完成。','D15']
];
const rows=items.map(([kind,title,why,id])=>`<tr><td>${kind}</td><td><strong>${title}</strong><p class="muted">${why}</p></td><td><button class="btn small" data-go="decision" data-target="${id}">查看并记录</button></td></tr>`).join('');
const marker='<section id="view-start" role="tabpanel" aria-labelledby="tab-start">';
if(t.includes('id="open-agenda"'))throw Error('Already focused');
t=t.replace(marker,marker+`<section class="panel" id="open-agenda"><h2>今天只讲还没有确定的部分</h2><p style="margin:12px 0">已有UE和小程序手机端沿用，不重复汇报。以下为根据现有资料整理的未收口项；如团队已有新结论，补充依据后移出本次议程。</p><div class="table-wrap"><table><thead><tr><th>类型</th><th>需要解决什么</th><th>讨论记录</th></tr></thead><tbody>${rows}</tbody></table></div><p style="margin-top:16px">每次讨论只需留下：结论或验证任务、负责人、确认日期、通过条件。</p></section><details><summary>查阅已有方案与完整流程（无需重复汇报）</summary>`);
const next='      <section id="view-trace"';
const pos=t.indexOf(next);const before=t.slice(0,pos);const closing=before.lastIndexOf('</section>');
t=before.slice(0,closing)+'</details>'+before.slice(closing)+t.slice(pos);
t=t.replace('>先看完整流程</button>','>当前未决事项</button>');
t=t.replace("start:['先看懂一次运动，再决定做什么','先点下面的流程：看用户怎么用、设备要做什么，以及哪些事情还没决定。']","start:['现在还有什么没有确定？','只讨论未决项、口径冲突和验证任务。已有方案在下方折叠查阅。']");
fs.writeFileSync(p,t);

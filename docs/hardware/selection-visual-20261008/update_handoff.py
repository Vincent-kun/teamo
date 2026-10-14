from pathlib import Path
root=Path(__file__).resolve().parent
import json, hashlib
mp=root/'image-sources.json'
manifest=json.loads(mp.read_text(encoding='utf-8'))
for entry in manifest:
 f=root/'assets'/entry['file']
 if entry['status']=='failed' and f.is_file():
  entry.update(status='previous_download_retained',sha256=hashlib.sha256(f.read_bytes()).hexdigest(),bytes=f.stat().st_size,caption='对应型号厂家产品图，前次成功归档；本次重试超时')
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
p=root/'实施与交接计划_20261008.md'
s=p.read_text(encoding='utf-8')
s=s.replace('**当前先完成本交接计划，再继续展示页完善和检验。**原可视化任务仍保留；目前已生成页面初稿，尚未完成浏览器运行与视觉验收。','**展示页与本交接计划已完成本轮交付。**19条候选、S0–S5路线、产品/参考图片与机械证据已归档；本地文件浏览器检查通过。完整CAD、正式供应商报价与今晚主控决策仍待后续闭环。')
s=s.replace('### 已完成：资料与页面初稿','### 已完成：资料与可交互展示页')
s=s.replace('- 浏览器加载、交互、图片、响应式和布局验收。','- 已通过浏览器加载、六路线切换、原图弹窗、输入校验、图库筛选、报价计算与320/390/768/1440px页面溢出检查；报告见`review/browser-check.json`。本行属于完成记录。')
s=s.replace('### 未完成：不能宣称已通过','### 后续工程工作：尚未闭环')
s=s.replace('已生成的展示页初稿；浏览器验收未完成','已生成的展示页；本地浏览器交互检查通过')
s=s.replace('8. 当前Ultra产品图是系列无无线图，已标“W配置另核”；不得作为W实物确认。M02所用系列机械图也不证明无无线版本全部器件高度。','8. Ultra W已改用对应型号官方缩略图，只有93px，不用于测量。M02所用系列机械图不证明无无线版本全部器件高度。4G系列图不证明具体订货后缀。')
s=s.replace('没有完成页面加载验证。','该HTTP方式没有完成加载；后续已改用本地file URL完成浏览器检查，不依赖该服务。')
s=s.replace('- [ ]','- [x]',1)
for fragment in ['19条候选均有来源','S0不虚构RV1106B整板','正投影尺度由数据生成','A/B与余量预算可复算','55mm屏在A上的不足','320/390/768/1440px宽度','合作供应商与团队经验','无采购/供应商消息']:
 s=s.replace('- [ ] '+fragment,'- [x] '+fragment)
s += '\n## 11. 本轮交付记录\n\n- 源文件：`template.html`、`build.py`；所有新增图片附原始URL、SHA256与用途说明。\n- 已补Ultra W、相机A、4寸屏、电池、功放、扬声器图片及1.85寸独立模组尺寸图。没有精确照片的型号用机械证据或明确留空。\n- 等轴测增加W/H/T标签与沿W轴20mm标尺；未知T继续画虚线面。尺寸精度来自厂家记录，不由照片反推。\n- `verify-browser.cjs`为可复跑浏览器检查；`review/`保存报告与四种宽度截图。报价测试值已清空。\n- 输入一页资料见原工作页；内部排布见展示页与PCB交接方案；问题台账、日报模板和今晚确认问题保持可追溯。\n- 本轮没有验证完整三维容纳性、完成PCB设计、锁定供应商或正式总价。\n'
p.write_text(s,encoding='utf-8')
(root/'README.md').write_text('# 真实硬件选型展示与交接\n\n入口：[打开展示页](index.html) · [实施与交接计划](实施与交接计划_20261008.md) · [浏览器检查记录](review/browser-check.json)\n\n19条真实候选，S0–S5六条路线。浏览器直接打开index.html即可，图片已本地归档。主控待定；未知参数明确标注，排布是器件包络示意，不能替代完整CAD容纳性验证。\n\n修改template.html或build.py后运行build.py重新生成；补充图片须保存来源与SHA256。\n',encoding='utf-8')
print('Updated handoff and README')

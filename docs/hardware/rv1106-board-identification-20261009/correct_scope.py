from pathlib import Path
root=Path(__file__).resolve().parent
hardware=root.parent
notice='2026-10-09范围更新：开发板仅作算法/驱动/接口验证平台，产品由团队自研主板。旧Core＋载板组合只保留为尺寸案例，未选为最终架构；P4不再是产品机身候选，开发板尺寸不反推产品PCB。'
# 修改本轮创建的方案源，保留此前尺寸推导作为历史案例。
p=hardware/'screen-size-discussion-20261008'/'build.py'
s=p.read_text(encoding='utf-8')
if notice not in s:
 s=s.replace('<main><small>','<main><div class="warning">'+notice+' <a href="../rv1106-board-identification-20261009/index.html">开发平台辨认图册</a></div><small>')
 s=s.replace("title='开发板 · 工程壳'","title='开发平台 · 非产品尺寸'")
p.write_text(s,encoding='utf-8')
p=hardware/'selection-visual-20261008'/'template.html'
s=p.read_text(encoding='utf-8')
if notice not in s:s=s.replace('<main class="wrap">','<main class="wrap"><div class="result">'+notice+' <a href="../rv1106-board-identification-20261009/index.html">平台辨认图册</a></div>')
p.write_text(s,encoding='utf-8')
p=hardware/'屏幕与整机尺寸方案_20261008_V0.1.md'
s=p.read_text(encoding='utf-8')
if '## 2026-10-09架构范围更正' not in s:
 s=s.replace('\n\n> 2026-10-08。','\n\n> **2026-10-09用户补充：开发板仅是开发平台，最终产品自研主板。下文P4退出产品尺寸比较，P1–P3的Core＋载板属于历史计算案例，不代表已选产品架构。**\n\n> 2026-10-08。')
 s+='\n\n## 2026-10-09架构范围更正\n\n用户明确产品自研主板。下一轮应以RV1106具体后缀＋存储/电源/无线/音频等真实器件预布局估算主板面积与双面限高，再联合屏、电池、镜头和结构决定机身。现有42×55×10载板占位保持为历史假设，不能直接下发PCB；开发板SDK/驱动/参考电路可作为工程输入。\n\n[开发平台辨认与原图](rv1106-board-identification-20261009/index.html)。\n'
p.write_text(s,encoding='utf-8')
print('Corrected scope: development platform separate from custom product PCB')

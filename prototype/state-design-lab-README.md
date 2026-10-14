# 状态与架构可视化工作台 V0.2

入口：[state-design-lab-prototype.html](state-design-lab-prototype.html)。双击打开；若旧页面已打开，重新加载文件。

按“一次运动泳道 → 完整能力树 → 概念职责架构 → 局部状态”阅读。局部图可展开全部转移，点击节点看条件，导出SVG。情境页提供8条预设推演，范围页由PM标记11/15范围，刷新前需导出。

这是候选设计与预设情境，不连接真实摄像头、设备或后台；图形不等于已完成页面/算法。圆屏和技术路线仍需评审，PM范围默认全部待决定。

配套研究：`docs/product/design/专业状态与架构图作图方法研究_20261008.md`。重绘与验证：`docs/product/design/状态图可读性重绘与验收记录_V0.2_20261008.md`。

源数据为state-atlas-model.json；成熟Graphviz引擎由build-state-atlas.mjs预生成SVG并内嵌。state-atlas-view.js是页面图谱逻辑源；网页本身没有运行时网络依赖。state-atlas-assets保留DOT/SVG、静态校验与样例PNG；不是线上部署目录。

静态验证：25图节点重叠0、节点文字越界0、采样边穿其他节点0。尚未做实际浏览器与读者理解验收。效果确认后再沉淀技能。

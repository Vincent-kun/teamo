# Change Impact — AGENTS.md v0.2.0 → v0.2.1

- Section: §9 默认视觉配色规则（新增"不使用蓝色强调字体颜色"标准）。
- Before: 仅规定"跟随系统浅色/深色、使用系统语义色或平台原生颜色变量、不使用花哨配色/大面积强调色块/渐变、颜色仅用于必要的选中/焦点/错误等状态"。未对"蓝色作为强调字体颜色"作限制；链接默认蓝（`LinkText`）、焦点描边默认蓝（`Highlight`）未被约束。
- After: 增补「不使用蓝色作为强调字体颜色」：链接/引用等默认蓝色改为跟随正文色（`CanvasText`）或系统语义色，仅保留下划线等结构区分；焦点描边蓝（`Highlight`）改为中性灰（`GrayText`）。蓝色仅可用于必要的选中/焦点/错误等状态，不用于正文强调。明确该规则同样适用于本文档族导出的 HTML 渲染（如设备端软件功能大纲）。
- Change Type: Patch（格式/描述修正，无产品方向、功能取舍或架构变化）。
- Affected:
  - AGENTS.md §9 默认视觉配色规则。
  - 本文档族导出的 HTML 渲染（如 `Teamo_MVP_设备端软件功能大纲_v0.5_UE功能同步评审_20261012.html`）的链接与焦点配色。
  - DOCUMENT_REGISTER.md 中 AGENTS.md 版本号同步为 v0.2.1。
- Risk: Low。纯样式/文档规范补充，不改变产品边界、功能范围或审批状态；不影响既有导航与业务规则。
- Backup: `docs/governance/backups/agents-v021-20261012/AGENTS.md`（SHA256 `0d6e8fded6593e984a7c9ddc7adc809a13db311c5d3ef93ccb5552dd640a3a28`）。
- Next Action: Owner/Reviewer 待指派；无业务待评审项。本次无产品/架构决策。

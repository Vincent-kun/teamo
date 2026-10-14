# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Project Documentation |
| Current Version | v1.4.1 |
| Status | Draft |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-09 |
| Last Updated | 2026-10-12 |

> 文档控制版本以本表为准；原文件名和正文版本标识保留为历史业务版本。Draft/Review 为本次治理提交状态，非产品审批结论。创建日期取自原标识，待 Owner 核实。

# 手机端 UI 维护约束

开始修改本目录前读取 `../../docs/product/design/视觉圣经_家长端_V1.0_20261009.md`。

- 提示文字纪律（视觉圣经 V1.4）：不得在页面渲染用户命令原话或实现说明类小字（"视觉示例""本机测试"等一律不上屏）。

- 使用同一 MVP 模板，两个入口不得分叉。
- 主导航：首页/任务/AI/成长/我的；不得改变结构来补功能。
- 默认冻结当前视觉。补事件/数据/状态时不改布局、主题、图标和卡片。
- 当前三套皮肤为候选，不等于最终选型；不得自动择优淘汰。
- 用户明确请求的视觉变更可实施；无明确请求的视觉改动先展示具体方案并获得授权。
- 不需要为无视觉变化的逻辑修复重复请求批准。
- visual-baseline-20261009.json 是冻结证据，不可为了让检查通过而静默更新。已授权视觉变更后记录原因再更新基线。
- 检查脚本不替代浏览器视觉验收，不得宣称未执行的验证。


---

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.4.0 | 待核实 | 原作者待核实 | 待核实 | 登记导入前现存正文基线；已有版本标识，既有版本记录仍保留在正文；不推断历史修改或批准 |
| v1.4.1 | 2026-10-12 | Codex（AI，执行用户指令） | Draft | 新增 Document Control、标准 Version History、Change Impact 与 Decision Log；保留既有业务正文及历史记录 |

> 本表仅登记已验证的现存基线与本次修改。历史日期、作者和状态待核实；原有版本记录是补录证据入口，不能据文件名编造缺失版本。

# Change Impact

### Modified Sections

- Section: 文档顶部与治理附录。
- Before: 缺少统一的文档控制表和标准版本记录。
- After: 增加控制表、基线与 Patch 历史、影响分析和决策记录入口；原业务正文保留。

### Impact Scope

Affected:
- 本文及引用本文的项目文档；本次无业务要求变更。
- 逐文件版本、备份和修改报告见 docs/governance/CHANGELOG-20261012.md。

### Risk

Low。Owner、Reviewer、历史审批状态仍待确认；本次结构治理不冻结产品需求。

# Decision Log

本次未修改产品方向、功能取舍或系统架构。既有决策及待决事项保留在正文，尚未逐条验证迁入；后续涉及这些事项时按 docs/governance/DOCUMENT_VERSION_POLICY.md 记录，建议与已批准决策必须区分。

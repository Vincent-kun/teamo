# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Hardware Requirement / Research |
| Current Version | v0.1.1 |
| Status | Draft |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-08 |
| Last Updated | 2026-10-12 |

> 文档控制版本以本表为准；原文件名和正文版本标识保留为历史业务版本。Draft/Review 为本次治理提交状态，非产品审批结论。创建日期取自原标识，待 Owner 核实。

# 真实硬件选型展示与交接

入口：[打开展示页](index.html) · [实施与交接计划](实施与交接计划_20261008.md) · [浏览器检查记录](review/browser-check.json)

19条真实候选，S0–S5六条路线。浏览器直接打开index.html即可，图片已本地归档。主控待定；未知参数明确标注，排布是器件包络示意，不能替代完整CAD容纳性验证。

修改template.html或build.py后运行build.py重新生成；补充图片须保存来源与SHA256。


---

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | 待核实 | 原作者待核实 | 待核实 | 登记导入前现存正文基线；无版本标识，治理初始化编号，不代表历史首次发布；不推断历史修改或批准 |
| v0.1.1 | 2026-10-12 | Codex（AI，执行用户指令） | Draft | 新增 Document Control、标准 Version History、Change Impact 与 Decision Log；保留既有业务正文及历史记录 |

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

# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Hardware Requirement / Research |
| Current Version | v0.1.1 |
| Status | Draft |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 待核实（无可靠创建日期） |
| Last Updated | 2026-10-12 |

> 文档控制版本以本表为准；原文件名和正文版本标识保留为历史业务版本。Draft/Review 为本次治理提交状态，非产品审批结论。创建日期取自原标识，待 Owner 核实。

# 显示屏物料库 UI 调整

以企业库存应用的数据操作习惯为参考，保留真实选型数据的状态与来源。

参考来源：

- [SAP Fiori 元素说明](https://www.sap.com/design-system/fiori-design-web/v1-96/discover/get-started/ui-elements-overview)：统一应用框架与控件层级。
- [SAP 库存概览](https://learning.sap.com/courses/inventory-management-in-sap-cloud-erp/using-analytical-apps-for-inventory-management-2)：概览、筛选与明细的组织方式。
- [IBM Carbon 数据表组件](https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/DataTable/DataTable.mdx)：表格工具栏与搜索。

本页采用浅灰底、白色面板、深蓝应用栏与蓝色动作色。默认显示清单，产品图独立切换；行内产品图、采购与验证说明可展开。增加型号/控制器搜索、CSV导出入口与关联硬件方案导航。

候选数与图片数表示研究资料覆盖，不表示库存。未知尺寸、驱动和版本继续明确标注。

检查：脚本执行、默认筛选、触控筛选、搜索、重置、视图切换、无效阈值清空及本地图片存在性通过。浏览器自动化初始化失败，尚未视觉复核布局。


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

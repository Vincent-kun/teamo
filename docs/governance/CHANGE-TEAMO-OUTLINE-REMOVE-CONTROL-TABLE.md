# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Documentation Change Record |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认 |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# 去除设备端功能大纲顶部控制表

# Change Impact

- Section: 两份大纲顶部Document Control表。
- Before: 显示类型、版本、状态、Owner、Reviewer、创建及更新日期。
- After: 按用户本次明确要求去除整张表和空置标题，保留正文版本与历史；格式Patch v2.1.0→v2.1.1。
- Affected: 稳定大纲、原交付文件（路径不变）、登记表v1.5.1→v1.5.2。
- Risk: Low；无功能变更。用户本次指令优先于治理规范顶部控制表要求，此例外仅限本次两份大纲；检查器将报缺少控制表，非遗漏。
- 基线：[manifest](backups/teamo-outline-remove-control-table-20261013/manifest.json)。此影响记录先于正文修改保存。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 登记两份大纲顶部控制表删除、治理例外及格式Patch |

# Decision Log

本次无产品或架构决策。用户明确要求去除顶部表格；保留历史与正文版本，治理例外不推广到其他文档。

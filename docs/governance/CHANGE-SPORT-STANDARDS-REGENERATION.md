# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Standard Reference Document Control |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认 |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# Change Impact

- Section: Sport_Standards_Research.md 全部正文及登记名称。
- Before: v0.1.0 为来源索引，包含产品用途、项目年龄分组和功能范围关系。
- After: v0.2.0 重建为《儿童运动能力评价相关国家标准资料库》；只保留官方标准基本信息、范围、指标、测试项目及评价规则。增加国民体质2023幼儿部分与国家体育锻炼标准儿童/少年部分；未核验字段明确标记。
- Change Type: Minor；资料库模块结构重建。
- Affected Documents: 本资料库、DOCUMENT_REGISTER.md；不修改其他业务正文。
- Risk: 官方原附件未确认的学生标准字段不得作为已核验数据引用。
- Baseline: [原文备份](backups/sport-standards-regeneration-20261013/Sport_Standards_Research.md)；[SHA256](backups/sport-standards-regeneration-20261013/sha256.json)。
- 用户本次明确“只允许记录官方标准事实”；资料库正文不放治理附录，治理结构在本独立文件维护。此为本次用户指令优先于AGENTS.md内置治理结构的例外，校验脚本对该正文的缺项须单独辨识。

## 资料库文档控制

| 字段 | 内容 |
|---|---|
| Document Type | Official Standards Reference |
| Current Version | v0.2.0 |
| Status | Review |
| Owner | 待确认 |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

## 资料库 Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | 2026-10-13 | Codex（AI） | Draft | 原来源索引基线；原文完整留存备份 |
| v0.2.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 删除非标准事实内容；重建三个标准条目、适用范围、官方分类、测试表和评价规则；未核验字段明确标记 |

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 新增重建影响分析、完整备份索引、资料库外置文档控制及版本记录 |

# Decision Log

本次无产品/架构决策。资料整理范围与正文仅含官方事实由用户明确指定。

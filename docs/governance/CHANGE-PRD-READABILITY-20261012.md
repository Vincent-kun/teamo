# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | PRD Readability Change |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Change Impact

- Section: PRD正文与独立RTM、HTML及登记导航。
- Before: 47张需求卡在正文重复Function/PAGE/State/Test引用，影响人类阅读。
- After: 正文以18个二级业务模块呈现场景、目标、流程、页面、规则、异常和验收；原47张详细卡与69项映射进入独立RTM，保留原问题编号与状态。
- Change Type: Minor（v1.0.0→v1.1.0，文档结构重组）；不新增/删除需求或更改优先级。
- Compatibility: PRD既有Markdown/HTML路径保持；控制版本更新为v1.1.0，文件名版次为历史路径标识。旧HTML锚点兼容保留。
- Risk: Medium；移出追踪可能导致信息遗漏，需核对47核心、20候选、2停用与全部原待确认事项。
- Baseline: backups/prd-readability-20261012/baseline.zip及sha256.json。
- Source: 用户本次可读性/RTM分离规则；四份需求来源不变。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录正文重组、追踪迁出、兼容路径、备份和验证计划 |

# Decision Log

无产品/架构决策；只改变文档呈现和追踪组织。TBD、候选和OQ/UE-OQ不转为批准内容。

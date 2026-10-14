# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Feature Specification Render and UE Navigation Fix |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Change Impact

- Section: 功能表分隔行、UE功能导航及绑定职责表述、HTML转换。
- Before: 8列表头对应7列分隔行，转换后显示原始Markdown；已有绑定及20候选在后部难以定位。
- Evidence: 用户截图及实际HTML回归失败；最小8列表格修正分隔行后能渲染。最新UE PAGE-00已要求呈现绑定/连接及平台认可上下文，PAGE-08明确身份/设置分组。
- After: 修复分隔行；新增0.6 UE同步导航，绑定/二维码/儿童切换/解绑等现有编号显式可查；保留47核心、20候选、2停用与所有原P0/TBD状态。绑定核心描述对齐UE既有职责，不选择二维码方案或增加实现。
- Version: 功能大纲v0.5.3→v0.5.4，Patch（格式与现有职责澄清），不增删范围或重编号。
- Affected: 功能大纲Markdown/HTML、登记入口与HTML转换器。PRD/RTM业务范围不改写，仍保留已有功能追踪。
- Risk: Low；候选仍待评审，核心绑定能力与方案细化区别明确。
- Baseline: backups/feature-render-ue-entry-20261012/baseline.zip及sha256.json。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录表格渲染根因、UE入口与绑定职责修复影响及回归计划 |

# Decision Log

本次无产品/架构决策。用户要求补显最新UE功能；已有核心及候选完整展示，不把候选视为批准。MVP演示三动作的既有确认保持。

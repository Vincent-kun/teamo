# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Change Record |
| Current Version | v1.1.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

# Change Impact

### Modified Sections

- Section: 六模块功能说明、补充功能、范围说明及追踪附录。
- Before: 功能表混入展示方式、操作流程、实现依赖和验收讨论；学校任务仅P2候选，电池为条件项，存储为占位；未覆盖训练计划、体态、主动提醒、免打扰及装扮。
- After: 保留四列格式，说明仅定义功能用途；参照用户提供小程序V1.0与硬件V1.1补齐设备侧功能，标记范围差异为待评审建议；移除设计流程、技术依赖和验收问题，保留源图88节点及需求来源映射。
- Change Type: Minor，功能大纲v1.0.1 → v1.1.0（新增功能）；登记表v1.1.1 → v1.2.0。

### Impact Scope

Affected:
- docs/product/requirements/Teamo_Device_Function_Outline.md
- docs/governance/DOCUMENT_REGISTER.md

原始DOCX、现行Feature Specification、PRD、UE IA与硬件资料不修改。参考文档中的页面、参数和验收要求留待后续细化。备份与SHA256见backups/teamo-outline-functional-scope/manifest.json。

### 旧口径—新证据—建议修改

| 事项 | 旧口径 | 新证据 | 建议修改 |
|---|---|---|---|
| 首版动作 | 本稿仅引用MVP演示动作，首发清单待定 | 小程序2.2、硬件0.1明确首版开合跳、深蹲、高抬腿 | 按参考首版三动作写入本稿，正式基线仍待对齐；“深蹲起/深蹲”术语待确认 |
| 学校任务 | P2扩展 | 小程序2.3、硬件5.6明确首版家校需求 | 本稿建议P0，列为跨文档范围评审项，不静默改现行PRD |
| 供电与存储 | 电池条件项、存储占位 | 硬件9.17、9.20明确双供电、电量和本地保存 | 补齐供电状态、低电量处理与空间管理，建议P0；不写芯片与参数 |
| 日常陪伴与装扮 | 源图未列 | 小程序5.6、5.9、8.5；硬件9.14～9.15 | 新增体态、主动提醒、免打扰、装扮识别等设备功能 |
| 排行榜 | 小范围排行候选P2 | 小程序2.3明确不做竞技排名；项目边界禁止全站排名 | 原编号保留追溯，标记本轮不纳入、TBD；不将其换成新增竞赛 |

### Risk

Medium。两份新增来源均为评审稿，功能范围和优先级提议需责任人对齐后批准；本稿不是新批准基线。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.1.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增两份DOCX功能范围对照与功能层改写影响，记录学校/供电/存储/排行差异 |

# Decision Log

Date: 2026-10-12

Problem: 当前仅确认功能，需要补齐设备与小程序联动范围，并处理新参考与旧稿差异。

Options Considered: 沿用设计细节；保留表格格式，只抽取设备功能和业务边界。

Decision: 提议采用两份参考的设备功能范围，按功能层重写；不自行批准范围差异。

Reason: 用户要求此阶段只确定功能，并明确提供两份参考。

Impact: 本稿新增功能、调整建议优先级；原PRD等不变。

Owner: 待确认。

Status: Proposed

Evidence: 用户请求、小程序V1.0、硬件V1.1及现行项目边界。

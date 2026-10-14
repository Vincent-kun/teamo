# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Change Request |
| Current Version | v1.0.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# Change Impact

本单先于正文修改建立。大纲 v1.1.0 → v2.0.0，Major：用户指定评审版本并新增软件责任架构映射；不表示产品定位、实现架构或MVP范围获批。登记表 v1.2.2 → v1.2.3（Patch，同步入口）。

| Section | Before | After |
|---|---|---|
| 产品定义与架构 | 六类原功能分组，设备责任简述 | 保留六类及二级结构，新增七模块责任映射与设备/家长/云端分工 |
| 功能表 | 74条四列功能 | 保留全部ID、原优先级及需求，统一五列；新增5条TBD候选，标记Pending Review |
| 来源与能力 | DOCX/XMind来源对照 | 新增BodyPark章节引用、逐条追踪和Confirmed/Candidate/TBD能力映射 |
| 闭环与MVP | 分组清单及优先级数量 | 补齐运动闭环、完整P0/P1/P2/TBD范围及冲突评审清单 |
| 隐私与未决事项 | 视频不上传、不持久化 | 保持既定边界；回放为冲突事项，不纳入P2 |
| 治理 | v1.1.0 Review | v2.0.0 Review，补齐本次历史、影响、决策记录及登记 |

## 旧口径—新证据—建议修改

| 事项 | 旧口径 | 新证据 | 建议修改 |
|---|---|---|---|
| 待机陪伴 | 3.3.3角色反馈、4.3.2电量，未独立描述待机 | BodyPark §2.1描述时间/状态脸 | 增补待机状态、时间与待机角色回应为TBD候选；保留原P0角色反馈 |
| 运动流程 | 今日任务与AI陪练分散在既有条目 | BodyPark §2.6–2.15提供训练闭环参考 | 映射已有功能，不复制成人课程与负重/组数指标 |
| 日常提醒 | 3.4.1–3.4.4原P0建议 | 提示词P1示例与原稿不一致；竞品有专注模式 | 保留原P0并列Pending Review；新增专注计时为TBD候选 |
| 宠物成长 | 成长星、成就P1，未定义宠物养成 | BodyPark连续打卡与Teamo成长方向 | 仅新增TBD宠物成长候选，不引入独立养成循环 |
| 视频回放 | 禁止原始视频持久化、上传与回放 | 竞品报告建议录制复盘 | 不迁移；若提出边界变更需另行评审，不设P2 |

## Impact Scope

修改大纲、全局登记表及managed-documents.json；新增本变更单。PRD、UE IA、功能规格、云端对齐稿、硬件资料、竞品原报告和部署目录不修改。后续跨文档同步须在范围批准后执行。

## Risk

Medium：竞品拆解为Draft，部分AI能力仅推断或待验证；原大纲也是Review。优先级不是批准排期，候选不得转为交付承诺。完整基线及SHA256见[manifest](backups/teamo-outline-bodypark-review/manifest.json)。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 新增大纲v2.0.0修订前影响分析、原口径与竞品证据差异、备份及同步范围 |

# Decision Log

## Decision TEAMO-BODYPARK-REVIEW-001

Date: 2026-10-13

Problem: 借鉴竞品时需要保留需求追踪并避免将参考能力当作已确认能力。

Context: 用户确认保留ID、稳定路径、原优先级及视频不持久化边界。

Options Considered: 重编七模块编号；保留原分组并建立责任架构映射。

Decision: 执行用户确认的映射和治理方式；新增功能范围仅为Proposed。

Reason: 保留原74条需求和88节点证据，同时支持后续UE IA与PRD评审。

Impact: 五条新增候选不进入已批准MVP，未决差异不改写其他权威资料。

Owner: 待确认（项目协调：魏子奇）。

Status: Proposed（文档处理方式已获用户授权；功能取舍未批准）。

Evidence: 本次用户指令、现行大纲v1.1.0、BodyPark拆解v1.0.0及现行产品边界。

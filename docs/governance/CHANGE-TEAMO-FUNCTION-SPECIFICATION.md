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

本单先于规格正文生成。来源为设备端功能大纲v2.0.0 / Review，目标v2.1.0 / Review。Change Type: Minor，新增状态与异常功能职责说明，分离能力域与功能清单；不改变产品定位、已有功能优先级或批准MVP。

| Section | Before | After |
|---|---|---|
| 文档组织 | 功能、研究、治理混排 | 规格主文为产品、边界、能力、功能、MVP、状态、AI边界、异常、成长；来源与治理移至附录 |
| 功能规格 | 79条、ID/名称/说明/优先级/来源 | 保留79条、原ID/名称/优先级/分组；来源移附录，新增Status列；AI-C-001仅为识别异常处理Candidate |
| 状态与异常 | 分散在中断恢复功能 | 建立8状态及正确分支，补充识别、网络、电源、存储响应，关联已有ID；未验证故障诊断不得冒充确定能力 |
| MVP | 以优先级清单为主 | Must Work / Supporting / Phase 2+按交付职责归类；分类不覆盖原优先级，装扮等P0差异仍待评审 |
| AI与成长 | 竞品与需求混合 | 需求确认与能力实现分开，真实运动奖励及重复同步不重复奖励保持 |
| 引用与版本 | 大纲稳定路径 | 用户明确指定新的Teamo_Device_Function_Specification_v2.1.0.md输出路径；源大纲保留不改写，登记为派生Review稿，不自动替代既有Feature Specification或PRD |

## 旧口径—新证据—建议修改

| 事项 | 旧口径 | 新证据 | 建议修改 |
|---|---|---|---|
| Status | 部分描述注明Pending Review，未统一状态列 | 用户要求Confirmed/Candidate/Pending Review | 基础职责可记Confirmed（仅来源明确），范围冲突保持Pending Review，候选保留Candidate/TBD；不表示人工审批 |
| 识别异常 | 2.2.2、2.3.1–2.3.7、3.3.1已有通用恢复 | 用户指定失败场景 | 汇总AI-C-001候选细化，不自动加入P0；既有无效计数保护不降低 |
| 装扮与提醒 | 原稿部分P0 | 用户提出Phase 2+增强示例 | 保留P0和Pending Review，归类增强提案，不能自动延期或降级 |
| 状态转换 | 提示词为串行示例，Completed后列Error | 用户要求状态模型 | Error作为异常分支、Paused可续练；正常完成不必经过Error |

## Impact Scope

新增规格正文、本变更单；更新全局登记v1.2.3→v1.3.0和managed-documents.json。源v2.0.0、现行PRD、UE IA、另一份Feature Specification、云端对齐稿及硬件资料不修改。审批后再对齐后续文档。

## Risk

Medium。正式规格格式不等于Approved；范围、硬件和算法仍有未决项。《功能大纲v4.0》未提供可定位文件，工作区按文件名检索未定位，仅按用户已给定结构/表格执行，不声称已读模板。完整来源备份及SHA256见[manifest](backups/teamo-functional-specification/manifest.json)。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 新增v2.1.0规格升级影响分析、状态解释、MVP冲突处理、命名例外及基线记录 |

# Decision Log

## Decision TEAMO-SPEC-001

Date: 2026-10-13

Problem: 功能大纲需形成跨产品、UE、研发、算法、测试使用的规格结构。

Context: 用户明确要求保留全部资产与优先级，使用指定输出文件名；模板仅为格式参考。

Options Considered: 改写源大纲并批准范围；保留源大纲，新增派生Review规格，明确需求确认不等于实现。

Decision: 采用派生Review规格；新增候选仅为异常职责细化，原功能不删除、不重编、不升格TBD。

Reason: 保留可恢复证据及未决状态，满足指定输出与正式规格组织要求。

Impact: 后续评审可用该文档作为输入，发布研发基线仍须批准范围与解决Open Questions。

Owner: 待确认（项目协调：魏子奇）。

Status: Proposed（文档整理已授权，范围/交付取舍待评审）。

Evidence: 用户本次请求、源大纲v2.0.0及治理规范。

# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Documentation Reference |
| Current Version | v0.2.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇） |
| Reviewer | 待指派 |
| Created Date | 2026-10-13 |
| Last Updated | 2026-10-13 |

# Teamo 设备端软件功能架构映射

> 版本：v0.2.0；日期：2026-10-13；状态：Review。
> 来源：功能大纲v2.1.1原0.3节；仅分离文档，不重新设计架构。
> 功能定义：[设备端软件功能大纲](Teamo_Device_Function_Outline.md)。

## 软件功能架构映射

本稿从功能大纲v2.1.1原0.3节提取，仅记录已有七模块与功能编号的对应关系。功能定义以独立功能大纲为准；本稿不新增技术架构设计、菜单或重编号方案。

```text
Teamo Device Software
├── 1. Companion State（陪伴状态）
├── 2. Exercise（运动执行）
├── 3. AI Recognition（AI识别）
├── 4. Growth Feedback（成长反馈）
├── 5. Daily Companion（日常陪伴）
├── 6. Device Management（设备管理）
└── 7. Cloud Sync（云端同步）
```

| 架构模块 | 软件责任 | 对应原功能ID/分组 |
|---|---|---|
| Companion State | 【修改】表达待机、准备、运动、暂停及异常等角色状态；3.6.1–3.6.2为P0 | 3.3.3、3.6.1–3.6.2；时间3.6.3待确认；引用4.3.2/4.3.3/4.3.6/4.4.1/6.1状态，不重复创建功能 |
| Exercise | 任务、自主运动、目标、开始、中断恢复及结果 | 2.1–2.5；2.2.2/2.2.3/2.3.1调用AI识别责任 |
| AI Recognition | 【修改】设备本地姿态识别、动作判断及次数统计；云端不重新识别 | 2.2.2/2.2.3/2.3.1/3.3.1；3.3.2承接语音指导，不等于生成式AI |
| Growth Feedback | 【修改】设备产生成长星奖励结果，云端同步保存，评定规则待确认；保留个人进步与成就；无宠物功能，3.1.4仅作废弃编号追溯 | 3.1–3.2、3.3.3；3.1.3排行保留追溯但不纳入 |
| Daily Companion | 授权提醒、免打扰、装扮互动及候选专注计时 | 3.4–3.5；体态检测能力仍需验证 |
| Device Management | 绑定、网络、供电、状态、隐私、维护与更新 | 1.1、4.1–4.4、6.1 |
| Cloud Sync | 获授权安排与结构化结果同步、离线保存和补传 | 5.1–5.2、2.2.7/2.5.2/3.4.2/3.5.3/4.3.10 |

跨模块引用表示协作，不重复计数。保留原一级、二级结构，不将“AI Recognition”序号3解释为原“反馈”编号3。

拆分记录：[修改报告](../../governance/CHANGE-TEAMO-OUTLINE-SEPARATE-MAPPING.md)。

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 拆分既有架构映射与功能大纲，保留功能编号与职责内容 |

| v0.2.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步角色状态P0、无宠物范围及成长星命名，映射模块不变 |

# Change Impact

- Section: 大纲原0.3软件功能架构映射。
- Before: 七模块映射混在功能大纲。
- After: 独立存放并引用稳定功能大纲；大纲仅保留功能分类与说明。
- Risk: Low；既有映射提取，未设计新架构或改变功能范围。

# Decision Log

Date: 2026-10-13

Decision: 按用户明确要求将架构映射作为独立文档；不扩展实现、接口或算法。

Reason: 功能大纲与架构映射承担不同文档用途。

Impact: 文档职责分离，79条功能与原优先级保持不变。

Owner: 文档审核责任待确认。

Status: 用户文档拆分要求已执行；既有映射保持Review，非已批准架构。

## Change Impact / Decision — v0.2.0

按用户本次明确范围同步功能大纲v2.2.0：角色状态P0、无宠物功能、成长星命名；原七模块保持。无技术架构设计，[修改报告](../../governance/CHANGE-TEAMO-OUTLINE-SCOPE-CONFIRMED.md)。

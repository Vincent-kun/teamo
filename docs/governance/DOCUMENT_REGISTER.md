# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Documentation Governance |
| Current Version | v1.8.0 |
| Status | Review |
| Owner | 魏子奇（项目协调；文档审核责任待确认） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-13 |

# 文档登记表与现行入口

本表登记治理范围；设备端文档已按批准映射迁移，旧路径兼容快照保留。规范树/现行规范的原权威顺序仍生效。下表“最新修订入口”按同族版本号推导，仅用于定位最新稿，不表示获批或取代现行 PRD；各文件 Document Control 是其治理版本来源。

## 已识别的多版本文档族

| 文档族 | 最新修订入口 | 历史文件 | 审批说明 |
|---|---|---|---|
| Teamo MVP设备端功能大纲 | [Teamo_Device_Feature_Specification_v0.6.0.md](../../docs/product/requirements/Teamo_Device_Feature_Specification_v0.6.0.md) | [Teamo_MVP_设备端软件功能大纲_PRD前置文档_v0.1_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_PRD前置文档_v0.1_20261012.md)；[Teamo_MVP_设备端软件功能大纲_v0.2_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.2_20261012.md)；[Teamo_MVP_设备端软件功能大纲_v0.3_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.3_20261012.md)；[Teamo_MVP_设备端软件功能大纲_v0.4_冻结候选_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.4_冻结候选_20261012.md) | 最新稿为候选/研究入口，批准状态以审查证据为准；旧文件保留用于追溯，后续在最新入口内迭代 |
| Teamo MVP设备端UE信息架构 | [Teamo_Device_UE_IA_v0.3.1.md](../product/requirements/Teamo_Device_UE_IA_v0.3.1.md) | v0.1、v0.2、v0.3原位保留，详见[目录登记表](../product/requirements/DOCUMENT_REGISTER.md) | Review；不代表批准 |
| Teamo设备端PRD | [Teamo_Device_PRD_v1.0.0_Draft.md](../product/requirements/Teamo_Device_PRD_v1.0.0_Draft.md) | [v0.6.0 Draft](../product/requirements/Teamo_Device_PRD_v0.6.0_Draft.md)保留原位 | Review；四份指定输入，不代表批准或取代整体PRD |
| Teamo圆形屏设计系统 | [Teamo_Circular_Display_Design_System.md](../product/design/Teamo_Circular_Display_Design_System.md) | [v1.0.0 基线备份](../governance/backups/teamo-circular-ds-v110/Teamo_Circular_Display_Design_System_v1.0.0.md)，变更单 [CHANGE-TEAMO-CIRCULAR-DS-V1.1.0](CHANGE-TEAMO-CIRCULAR-DS-V1.1.0.md) | v1.1.0 Review（Review Candidate）；硬件参数为参考基线待确认，阈值/亮度/S5 均为 Pending，未经评审不得冻结 |
| Teamo整体UI逻辑框架 | [Teamo_最新UI整体逻辑框架_V1.2_整合稿_20260923.md](../../AI运动伙伴/00_现行研究与规范_20260918/Teamo_最新UI整体逻辑框架_V1.2_整合稿_20260923.md) | [Teamo_UI整体逻辑框架_V1.1_评审记录_20260923.md](../../AI运动伙伴/00_现行研究与规范_20260918/Teamo_UI整体逻辑框架_V1.1_评审记录_20260923.md) | 最新稿为候选/研究入口，批准状态以审查证据为准；旧文件保留用于追溯，后续在最新入口内迭代 |

planning 下 Teamo_DeviceSoftware 功能大纲为另一份功能梳理稿，不自动与 requirements 文档合并。docs/product/requirements 下现行 HTML PRD 继续保持原权威。既有旧文件名包含“最新”等字样属于历史兼容保留，后续不新建这种名称。

## 核心 Markdown 清单

| 文档 | 治理版本 | 提交状态 | 历史缺口 |
|---|---|---|---|
| [00-INDEX.md](../../00-INDEX.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AGENTS.md](../../AGENTS.md) | v0.2.1 | Draft | 已有正文历史，作者/日期/审批待逐条核实 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_4G物联网与端云模型架构研究_20260923.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_4G物联网与端云模型架构研究_20260923.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_C端用户流程与一体换装硬件框架_V0.2.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_C端用户流程与一体换装硬件框架_V0.2.md) | v0.2.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_MVP用户旅程与交互框架_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_MVP用户旅程与交互框架_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_家长付费与儿童使用的双用户价值平衡评估_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_家长付费与儿童使用的双用户价值平衡评估_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_成长型运动宠物与长期陪伴机制_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_成长型运动宠物与长期陪伴机制_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_玩法互动排行榜与模块化移动扩展机制_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_玩法互动排行榜与模块化移动扩展机制_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_硬件尺寸与屏幕选型研究_20260923.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_硬件尺寸与屏幕选型研究_20260923.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_硬件选型工作介绍_20260924.md](../../AI运动伙伴/00_现行研究与规范_20260918/AI运动伙伴_硬件选型工作介绍_20260924.md) | v1.1.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/README.md](../../AI运动伙伴/00_现行研究与规范_20260918/README.md) | v3.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/Sweekar_AI实体成长陪伴案例卡_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/Sweekar_AI实体成长陪伴案例卡_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/Teamo_UI整体逻辑框架_V1.1_评审记录_20260923.md](../../AI运动伙伴/00_现行研究与规范_20260918/Teamo_UI整体逻辑框架_V1.1_评审记录_20260923.md) | v1.1.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/Teamo_屏幕与摄像头真实产品链接及白底图_20260923.md](../../AI运动伙伴/00_现行研究与规范_20260918/Teamo_屏幕与摄像头真实产品链接及白底图_20260923.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/Teamo_最新UI整体逻辑框架_V1.2_整合稿_20260923.md](../../AI运动伙伴/00_现行研究与规范_20260918/Teamo_最新UI整体逻辑框架_V1.2_整合稿_20260923.md) | v1.2.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/今晚硬件选型确认问题清单_20261008.md](../../AI运动伙伴/00_现行研究与规范_20260918/今晚硬件选型确认问题清单_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/儿童AI运动陪伴机器人_产品定义定位与边界规范_V1.0.md](../../AI运动伙伴/00_现行研究与规范_20260918/儿童AI运动陪伴机器人_产品定义定位与边界规范_V1.0.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/形态排布与PCB交接方案_20261008_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/形态排布与PCB交接方案_20261008_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/TEAMO_Design_Brief与Camera_Architecture探索框架_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/TEAMO_Design_Brief与Camera_Architecture探索框架_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/儿童AI运动伙伴_摄像头需求与产品形态初稿_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/儿童AI运动伙伴_摄像头需求与产品形态初稿_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/儿童AI运动伙伴_摄像模组技术方案_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/儿童AI运动伙伴_摄像模组技术方案_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/摄像模组_HTML展示方法研究_20260921.md](../../AI运动伙伴/00_现行研究与规范_20260918/摄像头方案与产品形态_20260921/摄像模组_HTML展示方法研究_20260921.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/机身尺寸黄金比例推导_20261008_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/机身尺寸黄金比例推导_20261008_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/真实硬件候选与五套组合_20261008_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/真实硬件候选与五套组合_20261008_V0.1.md) | v0.1.1 | Draft | 已有正文历史，作者/日期/审批待逐条核实 |
| [AI运动伙伴/00_现行研究与规范_20260918/硬件推进工作页_20261008_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/硬件推进工作页_20261008_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/竞品分析方法论与竞品池_研究底稿_V1.0_20260918.md](../../AI运动伙伴/00_现行研究与规范_20260918/竞品分析方法论与竞品池_研究底稿_V1.0_20260918.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/竞品分析输出规范_V3.0_决策版.md](../../AI运动伙伴/00_现行研究与规范_20260918/竞品分析输出规范_V3.0_决策版.md) | v3.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/竞品软件体验观察记录_V1.0_20260918.md](../../AI运动伙伴/00_现行研究与规范_20260918/竞品软件体验观察记录_V1.0_20260918.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/00_现行研究与规范_20260918/首版3D打印_硬件包络与误差预算_20261008_V0.1.md](../../AI运动伙伴/00_现行研究与规范_20260918/首版3D打印_硬件包络与误差预算_20261008_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [AI运动伙伴/会议与纪要/2026-09-29_项目开发相关工作安排讨论/会议分析_2026-09-29.md](../../AI运动伙伴/会议与纪要/2026-09-29_项目开发相关工作安排讨论/会议分析_2026-09-29.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [apps/wechat-mini-program/README.md](../../apps/wechat-mini-program/README.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [apps/wechat-mini-program/小程序产品与UI整改说明_V0.8.md](../../apps/wechat-mini-program/小程序产品与UI整改说明_V0.8.md) | v0.8.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [apps/wechat-mini-program/接口对接说明.md](../../apps/wechat-mini-program/接口对接说明.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [CONTEXT.md](../../CONTEXT.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/battery-selection-20261009/电池选型与功耗结构输入.md](../../docs/hardware/battery-selection-20261009/电池选型与功耗结构输入.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/display-protocol-filter-20261009/UI设计说明.md](../../docs/hardware/display-protocol-filter-20261009/UI设计说明.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/display-protocol-filter-20261009/产品图片缺项与供应商补图清单.md](../../docs/hardware/display-protocol-filter-20261009/产品图片缺项与供应商补图清单.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/display-protocol-filter-20261009/图片补齐记录_20261009.md](../../docs/hardware/display-protocol-filter-20261009/图片补齐记录_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/display-protocol-filter-20261009/默认初筛结果_20261009.md](../../docs/hardware/display-protocol-filter-20261009/默认初筛结果_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/rv1106-board-identification-20261009/RV1106开发平台辨认_20261009.md](../../docs/hardware/rv1106-board-identification-20261009/RV1106开发平台辨认_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/RV1106其他开发板排查_20261009.md](../../docs/hardware/RV1106其他开发板排查_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/selection-visual-20261008/README.md](../../docs/hardware/selection-visual-20261008/README.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/selection-visual-20261008/实施与交接计划_20261008.md](../../docs/hardware/selection-visual-20261008/实施与交接计划_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/SPI显示屏市场候选池_20261009.md](../../docs/hardware/SPI显示屏市场候选池_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/system-layout-20261009/整机排布与尺寸决策.md](../../docs/hardware/system-layout-20261009/整机排布与尺寸决策.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/system-layout-20261009/方案速览_通俗版.md](../../docs/hardware/system-layout-20261009/方案速览_通俗版.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/全品类补全_20261009/A_摄像头.md](../../docs/hardware/全品类补全_20261009/A_摄像头.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/全品类补全_20261009/C_网络与天线.md](../../docs/hardware/全品类补全_20261009/C_网络与天线.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/全品类补全_20261009/D_电源.md](../../docs/hardware/全品类补全_20261009/D_电源.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/全品类补全_20261009/E_声学与采集.md](../../docs/hardware/全品类补全_20261009/E_声学与采集.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/全品类补全_20261009/F_连接器与结构.md](../../docs/hardware/全品类补全_20261009/F_连接器与结构.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/全品类补全_20261009/全品类补全总览.md](../../docs/hardware/全品类补全_20261009/全品类补全总览.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/喇叭选型与音腔空间决策_20261009.md](../../docs/hardware/喇叭选型与音腔空间决策_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/天线选型与布置依据_20261009.md](../../docs/hardware/天线选型与布置依据_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/屏幕与整机尺寸方案_20261008_V0.1.md](../../docs/hardware/屏幕与整机尺寸方案_20261008_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/屏幕候选官方复核_20261008.md](../../docs/hardware/屏幕候选官方复核_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/显示屏协议与筛选规则_20261009.md](../../docs/hardware/显示屏协议与筛选规则_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/电池国内厂家复核_20261009.md](../../docs/hardware/电池国内厂家复核_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/硬件全品类选型与整机排布执行规范_V1.0_20261009.md](../../docs/hardware/硬件全品类选型与整机排布执行规范_V1.0_20261009.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/hardware/硬件选型_Agent分工与现状交接_20261009.md](../../docs/hardware/硬件选型_Agent分工与现状交接_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/MVP方向确认与技术评估_20261010.md](../../docs/product/design/MVP方向确认与技术评估_20261010.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/UE与小程序初步基线衔接_20261010.md](../../docs/product/design/UE与小程序初步基线衔接_20261010.md) | v7.4.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/ui-audit-20261008/Teamo_UI资产与交互复用审计_V0.1.md](../../docs/product/design/ui-audit-20261008/Teamo_UI资产与交互复用审计_V0.1.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/ui-audit-20261008/三方向参考实看与设计规则.md](../../docs/product/design/ui-audit-20261008/三方向参考实看与设计规则.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/ui-reference-trace-20261008/参考到UI的对应关系_V0.2.md](../../docs/product/design/ui-reference-trace-20261008/参考到UI的对应关系_V0.2.md) | v0.2.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/UI参考方向与审美研究_20261008.md](../../docs/product/design/UI参考方向与审美研究_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/UI风格实验室_源码评审与紧凑优化_20261009.md](../../docs/product/design/UI风格实验室_源码评审与紧凑优化_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/专业状态与架构图作图方法研究_20261008.md](../../docs/product/design/专业状态与架构图作图方法研究_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/专业需求基线与可视化评审方法研究_20261010.md](../../docs/product/design/专业需求基线与可视化评审方法研究_20261010.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/状态图可读性重绘与验收记录_V0.2_20261008.md](../../docs/product/design/状态图可读性重绘与验收记录_V0.2_20261008.md) | v0.2.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/视觉圣经_家长端_V1.0_20261009.md](../../docs/product/design/视觉圣经_家长端_V1.0_20261009.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/设备端UE参考与视觉边界_20261009.md](../../docs/product/design/设备端UE参考与视觉边界_20261009.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/软件全量状态框架与分轮设计_V0.1_20261008.md](../../docs/product/design/软件全量状态框架与分轮设计_V0.1_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/运动主流程_操作方案与软硬件需求拆解_V0.1_20261010.md](../../docs/product/design/运动主流程_操作方案与软硬件需求拆解_V0.1_20261010.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/design/需求评审工作台_快速上手.md](../../docs/product/design/需求评审工作台_快速上手.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/MVP关键问题与决策台账_V0.1_20261010.md](../../docs/product/planning/MVP关键问题与决策台账_V0.1_20261010.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/MVP软件演示范围与逐步细化_V0.1_20261010.md](../../docs/product/planning/MVP软件演示范围与逐步细化_V0.1_20261010.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/PRD到1115演示功能对应矩阵_V0.1_20261010.md](../../docs/product/planning/PRD到1115演示功能对应矩阵_V0.1_20261010.md) | v0.1.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/Teamo_DeviceSoftware_功能大纲_v0.2_Review_20261012.md](../../docs/product/planning/Teamo_DeviceSoftware_功能大纲_v0.2_Review_20261012.md) | v0.2.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/UI资产对齐与分轮设计执行计划_交接版_V0.1_20261008.md](../../docs/product/planning/UI资产对齐与分轮设计执行计划_交接版_V0.1_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/今日计划_2026-10-09.md](../../docs/product/planning/今日计划_2026-10-09.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/软件与UI路线_依据0929会议修订_V1.1_20261008.md](../../docs/product/planning/软件与UI路线_依据0929会议修订_V1.1_20261008.md) | v1.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/软件与UI首阶段交接清单_V0.1_20261008.md](../../docs/product/planning/软件与UI首阶段交接清单_V0.1_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/软件架构与UI交付路线_现状评估与建议_V1.0_20261008.md](../../docs/product/planning/软件架构与UI交付路线_现状评估与建议_V1.0_20261008.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/planning/需求基线导航与评审入口_20261010.md](../../docs/product/planning/需求基线导航与评审入口_20261010.md) | v0.1.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/product/requirements/Teamo_MVP_设备端UE信息架构_v0.1_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端UE信息架构_v0.1_20261012.md) | v0.1.1 | Review | 已有正文历史，作者/日期/审批待逐条核实 |
| [docs/product/requirements/Teamo_MVP_设备端UE信息架构_v0.2_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端UE信息架构_v0.2_20261012.md) | v0.2.1 | Review | 已有正文历史，作者/日期/审批待逐条核实 |
| [docs/product/requirements/Teamo_MVP_设备端软件功能大纲_PRD前置文档_v0.1_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_PRD前置文档_v0.1_20261012.md) | v0.1.1 | Review | 已有正文历史，作者/日期/审批待逐条核实 |
| [docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.2_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.2_20261012.md) | v0.2.1 | Review | 已有正文历史，作者/日期/审批待逐条核实 |
| [docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.3_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.3_20261012.md) | v0.3.1 | Review | 已有正文历史，作者/日期/审批待逐条核实 |
| [docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.4_冻结候选_20261012.md](../../docs/product/requirements/Teamo_MVP_设备端软件功能大纲_v0.4_冻结候选_20261012.md) | v0.4.1 | Review | 已有正文历史，作者/日期/审批待逐条核实 |
| [docs/product/requirements/Teamo_Device_Feature_Specification_v0.6.0.md](../../docs/product/requirements/Teamo_Device_Feature_Specification_v0.6.0.md) | v0.6.0 | Review | 已有正文历史，作者/日期/审批待逐条核实 |
| [docs/product/requirements/Teamo_Device_Requirement_Baseline_v0.1.1.md](../../docs/product/requirements/Teamo_Device_Requirement_Baseline_v0.1.1.md) | v0.1.2 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/README.md](../../docs/README.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/research/bodypark-teardown/README.md](../../docs/research/bodypark-teardown/README.md) | v1.0.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/research/bodypark-teardown/路线.md](../../docs/research/bodypark-teardown/路线.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [docs/research/competitive/bodypark/BodyPark_ATOM_设备端软件拆解_V1.0.md](../../docs/research/competitive/bodypark/BodyPark_ATOM_设备端软件拆解_V1.0.md) | v1.0.0 | Draft | 新增文档；基于设备端实拍帧拆解，待Owner补录历史 |
| [prototype/teamo-form-explorer/AGENTS.md](../../prototype/teamo-form-explorer/AGENTS.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [prototype/teamo-ui-flow-html/AGENTS.md](../../prototype/teamo-ui-flow-html/AGENTS.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [prototype/ui-style-lab-20261008/AGENTS.md](../../prototype/ui-style-lab-20261008/AGENTS.md) | v1.4.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [README.md](../../README.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [SECURITY_REVIEW_20261008.md](../../SECURITY_REVIEW_20261008.md) | v0.1.1 | Review | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [双周周报_20260927-20261010.md](../../双周周报_20260927-20261010.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [工作总结_20261008.md](../../工作总结_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [项目推进汇报_20261008.md](../../项目推进汇报_20261008.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |
| [项目文件分类.md](../../项目文件分类.md) | v0.1.1 | Draft | 缺少历史变更序列；已登记现存基线，待Owner补录 |

## 未改写范围

archive、部署/工具缓存、prototype 的非 AGENTS 文档、PPOS 模板及旧树非现行规范/会议纪要等保持原样；原始审计结果也包含未改写文档。未来修改这些可编辑 Markdown 时仍执行版本规则；模板内容应使用占位字段，历史快照不回写。旧树会议纪要已纳入治理结构，原会议内容保留。

# Change Impact

### Modified Sections

- Section: 文档入口登记。
- Before: 同族多个版本缺少统一登记。
- After: 登记核心文档及已识别版本族的最新修订入口，保留历史路径。

### Impact Scope

Affected:
- 文档查找与后续版本修改。

### Risk

Low。入口选择基于文件版本，不推断审批或范围冻结；同名不同用途不合并。


# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增105份核心文档登记、三组多版本修订入口及历史补录缺口 |

| v1.0.1 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步设备端命名、UE v0.3.1入口、功能v0.5.2及目录登记；无需求变更 |

| v1.0.2 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 登记Teamo设备端PRD v1.0.0 Draft/Review为当前评审入口，保留v0.6.0历史草稿和固定四份输入 |


| v1.0.3 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步PRD控制版本v1.1.0与独立RTM入口，保持旧PRD路径；无需求变更 |

| v1.0.4 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步MVP演示三动作确认后的控制版本和导航；既有路径保留 |

| v1.0.5 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步功能大纲v0.5.4表格修复及UE功能入口，路径不变 |

| v1.0.6 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 登记独立Feature Specification v0.6.0、RTM及治理日志，保留旧入口快照 |
| v1.1.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 新增XMind源图整理功能大纲入口，标明独立用途、88节点覆盖与未批准范围；保留现行规格入口 |

| v1.1.1 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步源图整理大纲v1.0.1参考格式修订；保留现行规格入口与范围 |

| v1.2.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 同步功能大纲v1.1.0：按小程序/硬件参考补齐设备功能并移除设计细节；保留原权威入口 |

| v1.2.1 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 新增导出稿云端对齐大纲v1.1.0和功能变更说明入口，区分原XMind大纲，不替换现行PRD或批准范围 |
| v1.2.2 | 2026-10-13 | WorkBuddy（AI，执行用户指令） | Review | 登记新增竞品拆解文档 `BodyPark_ATOM_设备端软件拆解_V1.0.md`；不改变产品范围 |


| v1.2.3 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步功能大纲v2.0.0评审入口及BodyPark修订变更单，不批准功能范围 |

| v1.3.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 登记由大纲v2.0.0派生的功能规格v2.1.0，Owner魏子奇，原规格/PRD入口不自动替换 |

| v1.3.1 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步规格控制版本v2.1.1及实际模板参考，保留原路径与范围 |

| v1.4.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 登记规格v2.2.0优先级调整与两项P0日志记录/平台同步，原路径与其他文档入口保持 |

| v1.4.1 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步规格v2.2.1字段说明精简，功能范围和路径不变 |

| v1.5.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 新增四份功能范围对齐阶段文档入口，隔离运动标准资料与技术设计 |


| v1.5.1 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步原设备功能大纲v2.1.0增量合并及同源完整Markdown交付入口，保留旧稿追溯 |

| v1.5.2 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步大纲v2.1.1与用户指定删除顶部控制表的治理例外，原路径保留 |

| v1.6.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 登记独立设备端架构映射v0.1.0，大纲v2.1.2移出映射并保留功能定义 |

| v1.7.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 登记大纲v2.2.0已确认功能取舍、删减章节与映射v0.2.0职责同步 |

| v1.7.1 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步三端责任范围规范v0.1.1及新增功能架构线框图，稳定路径不变 |

| v1.7.2 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 同步标准资料库v0.2.0名称及外置治理入口，正文仅记录官方标准事实 |

| v1.8.0 | 2026-10-13 | Codex（AI，执行用户指令） | Review | 登记硬件软件缺口分析v1.0.0，固定软件v2.2.1及V1.4附件输入，不改业务基线 |

# Decision Log

本次文档治理决策见 DOCUMENT_VERSION_POLICY.md 的 DOC-001；无新增产品或架构决定。

## Device Migration Register Update

[设备端登记表](../product/requirements/DOCUMENT_REGISTER.md)；新增PRD、UE工程参考及UE v0.3.1现行入口。旧路径与历史原样备份可恢复；本次无产品/架构决策。

| 文档 | 治理版本 | 提交状态 |
|---|---|---|
| [Teamo_Device_UE_IA_v0.3.1.md](../product/requirements/Teamo_Device_UE_IA_v0.3.1.md) | v0.3.2 | Review |
| [Teamo_Device_UE_Engineering_Reference_v0.1.0.md](../product/requirements/Teamo_Device_UE_Engineering_Reference_v0.1.0.md) | v0.1.1 | Review |
| [Teamo_Device_PRD_v0.6.0_Draft.md](../product/requirements/Teamo_Device_PRD_v0.6.0_Draft.md) | v0.6.0 | Draft |

## PRD v1.0 Draft Review Entry

[Teamo_Device_PRD_v1.0.0_Draft.md](../product/requirements/Teamo_Device_PRD_v1.0.0_Draft.md)为当前设备端PRD评审入口；Status Review，未批准或冻结。v0.6.0 Draft原路径保留历史草稿，不作为本次需求来源。四份输入版本不变，审批权威顺序不变。

### PRD Review Register

| 文档 | 治理版本 | 提交状态 | 角色 |
|---|---|---|---|
| [Teamo_Device_PRD_v1.0.0_Draft.md](../product/requirements/Teamo_Device_PRD_v1.0.0_Draft.md) | v1.1.1 | Review | 当前设备端PRD评审材料；未冻结 |

### Change Impact — PRD Review Entry

- Section: 当前PRD导航/登记。
- Before: 指向v0.6.0 Draft。
- After: 指向v1.0.0 Review，旧草稿保留；只更新文档入口，不更改产品范围。
- Risk: Low；[变更单](CHANGE-DEVICE-PRD-REVIEW-20261012.md)。

## PRD正文与RTM入口

[PRD正文](../product/requirements/Teamo_Device_PRD_v1.0.0_Draft.md)控制版本v1.1.0；[RTM](../product/requirements/Teamo_Device_Requirement_Traceability_Matrix.md)控制版本v1.0.0；正文按业务阅读，完整内部编号与逐项来源在RTM。

### Change Impact — Readability

当前入口同步控制版本及RTM；不改变范围、优先级与历史。详见[变更单](CHANGE-PRD-READABILITY-20261012.md)。

## MVP演示动作已确认

仅演示开合跳、深蹲起、高抬腿；整体产品追踪与其他未决项保留。各文件控制表为最新版本来源。

### Change Impact / Decision Log

同步用户已确认演示范围与文档版本，无编号/优先级调整；详见[变更单](CHANGE-MVP-THREE-ACTIONS-CONFIRMED-20261012.md)。

### Change Impact — 功能大纲预览修复

入口同步v0.5.4；不变更产品范围。绑定/二维码/儿童切换/解绑等已有条目现可在UE同步入口定位。

## 文档类型隔离入口

- [功能规格](../product/requirements/Teamo_Device_Feature_Specification_v0.6.0.md)：PM/设计/研发阅读评审。
- [RTM](../product/requirements/Teamo_Device_Requirement_Traceability_Matrix.md)：内部追踪，Excel为同源导出。
- [治理日志](Teamo_Device_Governance_Log.md)：完整问题、变更、影响与决策。

### Change Impact — 文档类型隔离

入口重组，无需求/编号/优先级变化；旧路径保留。

## XMind源图整理入口

[Teamo设备端软件功能大纲](../product/requirements/Teamo_Device_Function_Outline.md)，v2.2.0 / Review：保留79个原编号，其中1条已废弃；按用户明确范围调整角色P0、儿童切换与下一代方向，移除节点索引；按用户提供的88节点XMind和表格式参考文档整理，供源图范围评审；不替代现行Feature Specification、PRD或UE IA。该稳定路径后续在文件内迭代。

### Change Impact — 源图功能大纲

新增独立来源整理入口，不修改既有产品要求。[独立变更单](CHANGE-TEAMO-FUNCTION-OUTLINE.md)记录备份、源证据、影响与待评审事项。本次无已批准的产品/架构决策。

### Change Impact — 功能大纲格式

同步大纲v1.0.1格式修订，功能范围不变；[变更单](CHANGE-TEAMO-OUTLINE-FORMAT.md)。本次无产品/架构决策。

### Change Impact — 功能范围参考对齐

大纲v1.1.0按两份DOCX补齐功能，设计留待后续；[变更单](CHANGE-TEAMO-FUNCTION-SCOPE.md)记录学校、供电、存储与排行提案，不自动覆盖现行PRD。

## 导出稿云端对齐入口

| 文档 | 治理版本 | 提交状态 | 角色 |
|---|---|---|---|
| [设备端云端对齐大纲](../product/requirements/Teamo_Device_Function_Outline_Cloud_Alignment.md) | v1.1.0 | Review | 以2026-10-13归档的v1.0导出稿为基线，保持原4个一级功能与9项编号；独立补充稿，与XMind源图大纲编号不同 |
| [v1.0→v1.1功能变更说明](CHANGE-TEAMO-CLOUD-ALIGNMENT.md) | v1.0.0 | Review | 新增范围、来源、冲突、备份及后续同步事项 |

### Change Impact — 云端对齐登记

- Section: 文档入口登记。
- Before: 只有原XMind源图大纲入口。
- After: 新增独立导出稿云端对齐入口，现行功能规格、PRD和UE入口不变。
- Risk: Low（登记本身）；内容范围冲突为Medium，详见[变更说明](CHANGE-TEAMO-CLOUD-ALIGNMENT.md)。

### Decision Log — 云端对齐登记

本次仅新增文档入口，无新增已批准产品/架构决策；独立修订及冲突处理提案见变更说明TEAMO-CLOUD-ALIGNMENT-001/002。

### Change Impact / Decision Log — BodyPark参考评审修订

原大纲入口v1.1.0更新为v2.0.0 / Review，路径不变；新增候选与范围差异待评审，既有PRD、UE及功能规格不修改。无新增已批准产品决策；详见[变更单](CHANGE-TEAMO-BODYPARK-REVIEW.md)。

## Teamo派生功能规格评审入口

| 文档 | 版本 | 状态 | Owner | 关系 |
|---|---|---|---|---|
| [Teamo_Device_Function_Specification_v2.1.0.md](../product/requirements/Teamo_Device_Function_Specification_v2.1.0.md) | v2.2.1 | Review | 魏子奇 | 由Function Outline v2.0.0派生，既有80个ID保留；按用户最新指令调整优先级，新增两项P0异常日志闭环，共82条；不自动替换其他规格或PRD |

### Change Impact / Decision Log — 派生规格登记

原大纲保持v2.0.0，本次新增独立Review入口与Owner责任分配；文件名按用户明确要求，后续在登记路径内维护。范围和实现架构未批准，详见[变更单](CHANGE-TEAMO-FUNCTION-SPECIFICATION.md)。登记表Minor v1.2.3→v1.3.0。

### Change Impact / Decision Log — 模板表达对齐

规格路径不变，控制版本v2.1.1 / Review；Owner魏子奇。格式Patch，不改变功能取舍或实现架构；详见[变更单](CHANGE-TEAMO-SPEC-TEMPLATE-FORMAT.md)。

### Change Impact / Decision Log — MVP优先级与日志闭环

规格控制版本v2.2.0 / Review；本次用户明确优先级与状态语音边界，新增日志记录与平台同步P0，详见[变更单](CHANGE-TEAMO-MVP-PRIORITIES-LOGGING.md)。源大纲和其他PRD/UE/硬件未静默更新。

### Change Impact / Decision Log — 字段说明精简

规格控制版本v2.2.1 / Review，纯文案Patch，无产品/架构决策；[变更单](CHANGE-TEAMO-SPEC-FIELD-DESCRIPTION.md)。

## Function Scope Alignment 阶段入口

当前按用户指令进行功能范围与多端边界整理。三端责任范围规范为v0.1.1 / Draft，其他三份为v0.1.0 / Draft；原大纲、规格、PRD保持原位，登记不构成批准。

- [Teamo MVP 三端责任范围规范 v0.1.1](../../docs/product/requirements/Teamo_MVP_Multi_End_Function_Scope.md)
- [Teamo MVP 云端-设备端功能对应关系表 v0.1](../../docs/product/requirements/Teamo_MVP_Cloud_Device_Function_Mapping.md)
- [Teamo 设备端功能大纲修订清单 v0.1](../../docs/product/requirements/Teamo_Device_Function_Outline_Revision_List.md)
- [儿童运动能力评价相关国家标准资料库](../../docs/research/Sport_Standards_Research.md)

### Change Impact / Decision Log — 阶段入口

新增四个独立入口；登记表Minor v1.4.1→v1.5.0。既有产品正文不改写；阶段定位为用户明确要求，功能内容待评审。[变更单](CHANGE-TEAMO-FUNCTION-SCOPE-ALIGNMENT.md)。

## 设备端大纲增量合并交付

- [稳定维护入口](../product/requirements/Teamo_Device_Function_Outline.md)：v2.2.0 / Review；后续PRD、UE与排期输入评审基线。
- [Teamo MVP 设备端软件功能大纲 v2.1.0.md](../product/requirements/Teamo%20MVP%20设备端软件功能大纲%20v2.1.0.md)：完整同源交付快照，后续在稳定入口迭代，不独立维护。

### Change Impact / Decision Log — 增量合并入口

Patch v1.5.0→v1.5.1；同步当前大纲入口，登记不批准整份MVP范围。运动星分工按用户本次明确要求；规则待确认，其他文档后续同步。[修改报告](CHANGE-TEAMO-OUTLINE-INCREMENTAL-MERGE.md)。

### Change Impact / Decision Log — 去除大纲顶部控制表

用户明确要求删除两份设备端功能大纲顶部控制表，v2.1.1 / Review；导出文件名保留v2.1.0用于链接兼容，正文版本为v2.1.1。功能不变，无产品/架构决策。[变更单](CHANGE-TEAMO-OUTLINE-REMOVE-CONTROL-TABLE.md)。检查器对两份大纲的控制表缺失报错为用户授权例外。

## 架构映射独立入口

[Teamo设备端软件功能架构映射](../product/requirements/Teamo_Device_Function_Architecture_Mapping.md)，v0.2.0 / Review；从大纲原0.3提取，独立维护。功能大纲v2.1.2不再包含七模块映射；交付文件路径保持不变，正文版本为v2.1.2。

### Change Impact / Decision Log — 架构映射拆分

按用户明确要求分离文档，无新增功能或架构设计。登记表Minor新增入口；大纲Patch移出映射。[修改报告](CHANGE-TEAMO-OUTLINE-SEPARATE-MAPPING.md)。

### Change Impact / Decision Log — 本次范围确认

大纲v2.2.0，独立映射v0.2.0，均Review；两份同源大纲同步。用户明确儿童切换、角色P0、无宠物/骨架/回放，投屏/手表/语音输入为下一代升级方向，成长星与深蹲起统一。原PRD/UE/规格后续同步。[修改报告](CHANGE-TEAMO-OUTLINE-SCOPE-CONFIRMED.md)。

### Change Impact / Decision Log — 三端规范插图

三端责任范围规范v0.1.1 / Draft新增用户选定图示，职责表述按已有结论同步，非技术架构设计。[修改报告](CHANGE-TEAMO-THREE-END-SCOPE-DIAGRAM.md)。


### Change Impact — 标准资料库重新生成

- Before: 运动标准资料调研v0.1.0。
- After: 儿童运动能力评价相关国家标准资料库v0.2.0 / Review，路径保留；文档控制与历史外置于[修改报告](CHANGE-SPORT-STANDARDS-REGENERATION.md)。
- Risk: 未核验字段不可作为已核验标准数据。
- Decision Log: 无产品/架构决策。

## 硬件→软件需求缺口分析入口

| 文档 | 版本 | 状态 | Owner | 角色 |
|---|---|---|---|---|
| [Teamo_Hardware_Software_Gap_Analysis.md](../product/requirements/Teamo_Hardware_Software_Gap_Analysis.md) | v1.0.0 | Review | 魏子奇 | 以指定软件v2.2.1和用户V1.4综合需求附件为固定输入，区分确认/潜在缺口、无需独立功能、已覆盖及范围冲突；不修改原软件或硬件 |

### Change Impact / Decision Log — 缺口分析登记

新增独立评审入口，Minor v1.7.2→v1.8.0；不改变年龄、优先级、功能ID或批准状态。详见[变更单](CHANGE-TEAMO-HARDWARE-SOFTWARE-GAP-REVIEW.md)。

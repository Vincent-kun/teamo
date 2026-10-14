# Teamo 设备端需求追踪矩阵 RTM

# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Requirement Traceability Matrix |
| Current Version | v1.1.0 |
| Status | Review |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-12 |
| Last Updated | 2026-10-12 |

## 使用规则

本矩阵与PRD v1.1.0配套。Requirement ID仅引用需求基线已有FR号，不新增REQ号；其关联为已有意图整理，正式FR映射仍待评审。Function ID与Priority唯一来源是功能规格；UI ID使用UE的PAGE号，不新增UI号；State为原沟通标签，不定义实现枚举；Test Case未建立均TC-TBD，不虚构编号。

版本、范围与状态分开管理。47核心P0 / Pending Review、20候选优先级TBD、2停用追溯保持不变。候选不能因为进入矩阵被当作MVP。正文链接指向稳定PRD路径及新章节。

[阅读PRD](Teamo_Device_PRD_v1.0.0_Draft.md) · [评审HTML](Teamo_Device_PRD_v1.0.0_Draft.html)

## MVP演示范围确认（2026-10-12）

MVP演示确定仅包含开合跳、深蹲起、高抬腿三个动作。OQ-01及UE-OQ-03的“演示动作范围”部分已解决；整体七动作产品追踪保留，目标范围、有效规则、高抬腿计数单位仍TBD。文档全文仍Review，本次范围确认不等于全部需求冻结。

## 1. 核心需求追踪

| Requirement ID（已有意图） | 需求描述 | PRD章节 | Function ID | UI ID / PAGE关系 | State | Test Case ID | Priority | 状态 | Behavior Owner |
|---|---|---|---|---|---|---|---|---|---|
| FR-DEVICE-001 | 开机与初始化 | 5.1.1 | 1.1.1 | PAGE-00/01启动路由支撑，无新增启动PAGE | 启动/恢复（非INIT） | TC-TBD | P0 | Pending Review | 设备启动与运行；人员TBD |
| FR-DEVICE-001 | 恢复启动状态 | 5.1.1 | 1.1.2 | PAGE-00/01启动路由支撑，无新增启动PAGE | 启动/恢复（非INIT） | TC-TBD | P0 | Pending Review | 设备启动与运行；人员TBD |
| FR-DEVICE-001、FR-DEVICE-003 | 设备运行状态管理 | 5.1.2 | 1.2.1 | PAGE-00–08状态与异常支撑 | 设备/故障展示 | TC-TBD | P0 | Pending Review | 设备启动与运行；人员TBD |
| FR-DEVICE-001、FR-DEVICE-003 | 设备故障处理 | 5.1.2 | 1.2.2 | PAGE-00–08状态与异常支撑 | 设备/故障展示 | TC-TBD | P0 | Pending Review | 设备启动与运行；人员TBD |
| FR-DEVICE-001、FR-DEVICE-003 | 查看设备软件版本 | 5.1.2 | 1.2.3 | PAGE-08设备状态 | 设备/故障展示 | TC-TBD | P0 | Pending Review | 设备启动与运行；人员TBD |
| FR-DEVICE-001、FR-DEVICE-003 | 故障信息记录 | 5.1.2 | 1.2.4 | 后台记录支撑，无独立页面承诺 | 设备/故障展示 | TC-TBD | P0 | Pending Review | 设备启动与运行；人员TBD |
| FR-DEVICE-001、FR-DEVICE-003 | 设备重启 | 5.1.2 | 1.2.5 | PAGE-08系统设置 | 设备/故障展示 | TC-TBD | P0 | Pending Review | 设备启动与运行；人员TBD |
| FR-DEVICE-001、FR-DEVICE-002 | 运动入口 | 5.2.1 | 2.1.1 | PAGE-01/02/03 | 首页/运动状态回应 | TC-TBD | P0 | Pending Review | 设备交互；人员TBD |
| FR-DEVICE-001、FR-DEVICE-002 | 显示角色状态表情 | 5.2.1 | 2.1.2 | PAGE-01；PAGE-04–07按已有运动事件回应，承载TBD | 首页/运动状态回应 | TC-TBD | P0 | Pending Review | 设备交互；人员TBD |
| FR-DEVICE-001、FR-SPORT-004、FR-SPORT-006 | 设备状态提示 | 5.2.2 | 2.2.1 | PAGE-00–08通用支撑 | 操作反馈/状态展示 | TC-TBD | P0 | Pending Review | 设备交互；人员TBD |
| FR-DEVICE-001、FR-SPORT-004、FR-SPORT-006 | 操作接收与确认 | 5.2.2 | 2.2.2 | PAGE-00–08通用支撑 | 操作反馈/状态展示 | TC-TBD | P0 | Pending Review | 设备交互；人员TBD |
| FR-TASK-001、FR-SPORT-001 | 接收并检查运动任务 | 5.3.1 | 3.1.1 | PAGE-03消费后台接收事实，不新增接收页面 | INIT / 任务有效性 | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-TASK-001、FR-SPORT-001 | 反馈任务接收结果 | 5.3.1 | 3.1.2 | PAGE-03消费后台接收事实，不新增接收页面 | INIT / 任务有效性 | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-TASK-001、FR-SPORT-001 | 展示任务内容与执行状态 | 5.3.1 | 3.1.3 | PAGE-03 | INIT / 任务有效性 | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-TASK-001、FR-SPORT-001 | 动作与目标确认 | 5.3.1 | 3.1.4 | PAGE-02/03 | INIT / 任务有效性 | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-SPORT-002、FR-SPORT-003、FR-SPORT-004 | 动作说明 | 5.3.2 | 3.2.1 | PAGE-04 | READY / COUNTDOWN | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-SPORT-002、FR-SPORT-003、FR-SPORT-004 | 入镜准备引导 | 5.3.2 | 3.2.2 | PAGE-04；PAGE-09仅候选复用依据 | READY / COUNTDOWN | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-SPORT-002、FR-SPORT-003、FR-SPORT-004 | 开始确认与倒计时 | 5.3.2 | 3.2.3 | PAGE-04/05 | READY / COUNTDOWN | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-SPORT-006、FR-SPORT-007 | 暂停与成绩保留 | 5.3.3 | 3.3.1 | PAGE-06/04；再次经过PAGE-05与否TBD | RUNNING / PAUSED / FINISHED | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-SPORT-006、FR-SPORT-007 | 恢复运动 | 5.3.3 | 3.3.2 | PAGE-06/04；再次经过PAGE-05与否TBD | RUNNING / PAUSED / FINISHED | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-SPORT-006、FR-SPORT-007 | 达标与提前结束 | 5.3.3 | 3.3.3 | PAGE-06 → PAGE-07 | FINISHED | TC-TBD | P0 | Pending Review | 设备任务与执行；人员TBD |
| FR-SPORT-003、FR-SPORT-005、FR-SPORT-006 | 人体与画面可用性检测 | 5.4.1 | 4.1.1 | PAGE-04/05/06；PAGE-09仅候选复用依据 | READY / COUNTDOWN / RUNNING / PAUSED | TC-TBD | P0 | Pending Review | 设备识别能力；人员TBD |
| FR-SPORT-003、FR-SPORT-005、FR-SPORT-006 | 有效动作计数 | 5.4.1 | 4.1.2 | PAGE-06，异常准备原因由PAGE-04承接 | READY / COUNTDOWN / RUNNING / PAUSED | TC-TBD | P0 | Pending Review | 设备识别能力；人员TBD |
| FR-SPORT-003、FR-SPORT-005、FR-SPORT-006 | 判定运动识别异常 | 5.4.1 | 4.1.3 | PAGE-06，异常准备原因由PAGE-04承接 | READY / COUNTDOWN / RUNNING / PAUSED | TC-TBD | P0 | Pending Review | 设备识别能力；人员TBD |
| FR-SPORT-005 | 开合跳动作判定 | 5.4.2 | 4.2.1 | PAGE-06计数依据，不新增动作范围 | RUNNING | TC-TBD | P0 | Pending Review | 设备识别能力；人员TBD |
| FR-SPORT-005 | 深蹲起动作判定 | 5.4.2 | 4.2.2 | PAGE-06计数依据，不新增动作范围 | RUNNING | TC-TBD | P0 | Pending Review | 设备识别能力；人员TBD |
| FR-SPORT-005 | 高抬腿动作判定 | 5.4.2 | 4.2.3 | PAGE-06计数依据，不新增动作范围 | RUNNING | TC-TBD | P0 | Pending Review | 设备识别能力；人员TBD |
| FR-SPORT-005、FR-DEVICE-002 | 次数与进度反馈 | 5.5.1 | 5.1.1 | PAGE-06 | RUNNING / FINISHED | TC-TBD | P0 | Pending Review | 设备反馈呈现；人员TBD |
| FR-SPORT-005、FR-DEVICE-002 | 动作反馈与调整提示 | 5.5.1 | 5.1.2 | PAGE-06 | RUNNING / FINISHED | TC-TBD | P0 | Pending Review | 设备反馈呈现；人员TBD |
| FR-SPORT-005、FR-DEVICE-002 | 完成鼓励 | 5.5.1 | 5.1.3 | PAGE-07 | RUNNING / FINISHED | TC-TBD | P0 | Pending Review | 设备反馈呈现；人员TBD |
| FR-SPORT-007 | 运动结果查看 | 5.5.2 | 5.2.1 | PAGE-07 | FINISHED / SAVED / SYNCING / SYNCED | TC-TBD | P0 | Pending Review | 设备反馈呈现；人员TBD |
| FR-SPORT-007 | 保存与同步提示 | 5.5.2 | 5.2.2 | PAGE-07；必要同步提示PAGE-01 | FINISHED / SAVED / SYNCING / SYNCED | TC-TBD | P0 | Pending Review | 设备反馈呈现；人员TBD |
| FR-SPORT-007 | 记录创建与归属 | 5.6.1 | 6.1.1 | PAGE-02/03/06/07共用事实支撑，无重复记录系统 | 创建时机TBD / FINISHED | TC-TBD | P0 | Pending Review | 设备记录与同步；人员TBD |
| FR-SPORT-007 | 生成运动结果记录 | 5.6.1 | 6.1.2 | PAGE-02/03/06/07共用事实支撑，无重复记录系统 | 创建时机TBD / FINISHED | TC-TBD | P0 | Pending Review | 设备记录与同步；人员TBD |
| FR-SPORT-007、FR-DEVICE-001 | 本地保存 | 5.6.2 | 6.2.1 | PAGE-01/03/06/07消费保存恢复事实；后台处理 | 保存维度：SAVED / 未保存 | TC-TBD | P0 | Pending Review | 设备记录与同步；人员TBD |
| FR-SPORT-007、FR-DEVICE-001 | 已保存记录恢复 | 5.6.2 | 6.2.2 | PAGE-01/03/06/07消费保存恢复事实；后台处理 | 保存/恢复：SAVED或失败 | TC-TBD | P0 | Pending Review | 设备记录与同步；人员TBD |
| FR-SPORT-007、FR-DEVICE-001 | 保存失败处理 | 5.6.2 | 6.2.3 | PAGE-01/03/06/07消费保存恢复事实；后台处理 | 保存/恢复：SAVED或失败 | TC-TBD | P0 | Pending Review | 设备记录与同步；人员TBD |
| FR-SPORT-007 | 上传结果并更新同步状态 | 5.6.3 | 6.3.1 | PAGE-07/01消费独立同步状态，后台处理 | SAVED / SYNCING / SYNCED | TC-TBD | P0 | Pending Review | 设备记录与同步；人员TBD |
| FR-SPORT-007 | 补传失败结果并防重复 | 5.6.3 | 6.3.2 | PAGE-07/01消费独立同步状态，后台处理 | SAVED / SYNCING / SYNCED | TC-TBD | P0 | Pending Review | 设备记录与同步；人员TBD |
| FR-TASK-001、FR-SPORT-007 | 网络连接管理 | 5.7.1 | 7.1.1 | PAGE-00/08；PAGE-01必要状态提示 | 在线/离线（独立维度） | TC-TBD | P0 | Pending Review | 设备联网与使用者管理；人员TBD |
| FR-TASK-001、FR-SPORT-007 | 联网状态提示 | 5.7.1 | 7.1.2 | PAGE-00/08；PAGE-01必要状态提示 | 在线/离线（独立维度） | TC-TBD | P0 | Pending Review | 设备联网与使用者管理；人员TBD |
| FR-TASK-001、FR-DEVICE-003 | 设备状态同步 | 5.7.2 | 7.2.1 | 后台同步支撑，非独立页面 | 绑定/儿童/设备状态 | TC-TBD | P0 | Pending Review | 设备联网与使用者管理；人员TBD |
| FR-TASK-001、FR-DEVICE-003 | 绑定状态与当前儿童确认 | 5.7.2 | 7.2.3 | PAGE-00/08；PAGE-01使用有效上下文 | 绑定/儿童/设备状态 | TC-TBD | P0 | Pending Review | 设备联网与使用者管理；人员TBD |
| FR-SPORT-003、FR-SPORT-006、FR-DEVICE-003 | 检查授权并阻断不允许的采集 | 5.8.1 | 8.1.1 | PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守 | 隐私准入/采集状态 | TC-TBD | P0 | Pending Review | 设备隐私与权限；人员TBD |
| FR-SPORT-003、FR-SPORT-006、FR-DEVICE-003 | 摄像头状态提示与关闭 | 5.8.1 | 8.1.2 | PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守 | 隐私准入/采集状态 | TC-TBD | P0 | Pending Review | 设备隐私与权限；人员TBD |
| FR-DEVICE-002、FR-DEVICE-003 | 处理设备数据权限与删除请求 | 5.8.2 | 8.2.2 | 后台执行与回执；PAGE-08设备端入口TBD | 权限/提醒约束 | TC-TBD | P0 | Pending Review | 设备隐私与权限；人员TBD |
| FR-DEVICE-002、FR-DEVICE-003 | 提醒时段与频率控制 | 5.8.2 | 8.2.3 | PAGE-01/06/07等提示输出约束；PAGE-08设置入口TBD，不等于声音控制 | 权限/提醒约束 | TC-TBD | P0 | Pending Review | 设备隐私与权限；人员TBD |

## 2. 历史候选与停用追踪

| Requirement ID | 需求描述 | PRD章节 | Function ID | UI ID / State | Test Case ID | Priority | 状态 |
|---|---|---|---|---|---|---|---|
| TBD（不补造需求号） | 查看设备基本信息 | 5.9 | 1.2.6 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 恢复设备出厂状态 | 5.9 | 1.2.7 | PAGE-08/PAGE-00；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 检查设备软件更新 | 5.9 | 1.2.8 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 展示今日运动与任务摘要 | 5.9 | 2.1.3 | PAGE-01；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 调整设备提示音量 | 5.9 | 2.2.3 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 设置运动提示音开关 | 5.9 | 2.2.4 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 查看今日家长任务列表 | 5.9 | 3.1.5 | PAGE-03；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 查看家长任务详情 | 5.9 | 3.1.6 | PAGE-03；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 启动与退出独立动作辅助检测 | 5.9 | 4.3.1 | PAGE-09；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 显示姿态关键点辅助信息 | 5.9 | 4.3.2 | PAGE-09；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 更换设备连接网络 | 5.9 | 7.1.3 | PAGE-08/PAGE-00；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 检查设备联网情况 | 5.9 | 7.1.4 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 引导首次设备绑定 | 5.9 | 7.2.4 | PAGE-00；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 展示设备绑定二维码 | 5.9 | 7.2.5 | PAGE-00；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 更新失效绑定二维码 | 5.9 | 7.2.6 | PAGE-00；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 提供设备绑定帮助 | 5.9 | 7.2.7 | PAGE-00；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 切换当前使用儿童 | 5.9 | 7.2.8 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 执行设备解绑请求 | 5.9 | 7.2.9 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 设置本地摄像头使用状态 | 5.9 | 8.1.3 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| TBD（不补造需求号） | 查看设备数据使用说明 | 5.9 | 8.2.4 | PAGE-08；State TBD | TC-TBD | TBD | Candidate / Pending Review |
| 原追溯，不新增 | 运动结果通信（历史） | 1.3 / 5.9 | 7.2.2 | 沿用6.3.1 / 同步维度 | TC-TBD（不重复用例） | 历史P0，不计核心 | Deprecated / 保留追溯 |
| 原追溯，不新增 | 儿童视频不保存（历史） | 1.3 / 5.9 | 8.2.1 | 全部PAGE / 全局约束 | TC-TBD（不重复用例） | 历史P0，不计核心 | Deprecated / 保留追溯 |

### 停用源条目完整记录

| 编号 | 功能点 | 行为 | 用户价值 | 原优先级 | 状态 | 行为归属 | 原历史说明 |
|---|---|---|---|---|---|---|---|
| 7.2.2 | 运动结果通信（历史） | 已合并到6.3.1，不重复实现。 | 保留追溯。 | 历史P0，不计有效范围 | 已停用（保留追溯） | 6.3结果同步 | v0.3已合并 |
| 8.2.1 | 儿童视频不保存（历史） | 移为8.3全局约束。 | 保护隐私。 | 历史P0，不计有效范围 | 已停用（保留追溯） | 全局约束 | v0.3已移为约束 |

## 3. 固定来源

- [Teamo_Device_Requirement_Baseline_v0.1.1.md](Teamo_Device_Requirement_Baseline_v0.1.1.md)；SHA256 `3f7fa857e14d8a849e05ec755e40e522f91b4cca007950f93a7fb89dd34e6aa8`。
- [Teamo_Device_Function_Specification_v0.5.2.md](Teamo_Device_Function_Specification_v0.5.2.md)；SHA256 `cf0e09aebc83594cce7b3f92372f99bbff0f5219590f901f82dc3e68bc1db040`。
- [Teamo_Device_UE_IA_v0.3.1.md](Teamo_Device_UE_IA_v0.3.1.md)；SHA256 `4d2cf7e0a1f9f7c6dadee2320dcecfa9c82395298ac20b9feb1f471d7b328ee5`。
- [Teamo_Device_UE_Engineering_Reference_v0.1.0.md](Teamo_Device_UE_Engineering_Reference_v0.1.0.md)；SHA256 `0a850435a8ddc3638c40f9429e40f8b8f80c215b4073389664bc2ab10f9323ab`。

## 4. 完整逐项需求卡（从旧正文迁入）

以下保留原47张核心卡及候选/停用原记录，以便核对完整输入、输出、前置、异常、验收和追踪。其中原5.x标题是迁入来源标识，不是新PRD章节；新章节以矩阵为准。

## 5. 功能需求

### 5.0 阅读与验收约定

本章以F的一级→二级→Function ID展开47项核心需求，20项历史候选单列，2项停用另记。每卡有场景、描述、价值、输入/输出、前置、状态、异常、页面、验收和来源。描述继承F；基于用户价值整理场景，不增加行为。卡片的验收检查仅检视输入中的业务不变量，正式量化验收及Test Case仍TC-TBD。

F为Priority和Function唯一来源；U §6为PAGE/State原关系，包含支持而非独立页面承诺。待确认内容完整保留，原条目“—”不等于所有工程细则已确认。


### 5.1 一级功能：设备启动与运行管理

#### 二级功能 1.1：启动与运行

##### Function 1.1.1：开机与初始化

**用户场景**：在设备启动与运行管理的开机与初始化环节，家庭需要“让家庭知道设备能否开始使用。”。

**需求描述**：设备应启动软件并验证必要运行条件，进入可用或明确异常状态。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 让家庭知道设备能否开始使用。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备启动与运行；人员Owner TBD |
| 输入 | 上电/重启事件、必要运行条件 |
| 输出 | 可用状态或已确认启动异常 |
| 前置条件 | 设备上电或重启；隐私状态未明不得采集 |
| 状态 | 启动/恢复（非INIT）；仅业务/展示语义，工程枚举TBD |
| 异常 | 启动/必要服务不可用，按1.2.2处理；范围与时限TBD |
| 关联页面 | PAGE-00/01启动路由支撑，无新增启动PAGE |
| 验收标准（评审检查点） | 验证必要运行条件后进入可用或明确异常状态；启动时长TBD。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 启动时长待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 1.1.1 开机与初始化；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §1.1。
- PAGE: PAGE-00/01启动路由支撑，无新增启动PAGE；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 启动/恢复（非INIT）；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 1.1.2：恢复启动状态

**用户场景**：在设备启动与运行管理的恢复启动状态环节，家庭需要“重启后回到正确状态，不自动续计或伪称完成。”。

**需求描述**：设备应根据6.2.2恢复的任务、结果和隐私状态，输出待机、恢复提示或异常；不重复负责读取记录。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 重启后回到正确状态，不自动续计或伪称完成。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备启动与运行；人员Owner TBD |
| 输入 | 6.2.2给出的可恢复任务、记录、隐私与同步事实 |
| 输出 | 待机、恢复提示或异常去向 |
| 前置条件 | 启动后已取得恢复结果；恢复状态TBD |
| 状态 | 启动/恢复（非INIT）；仅业务/展示语义，工程枚举TBD |
| 异常 | 无法确认的进度不补造，具体不可恢复处理TBD |
| 关联页面 | PAGE-00/01启动路由支撑，无新增启动PAGE |
| 验收标准（评审检查点） | 只恢复可确认事实，不自动续计、不将未完成会话表示为完成。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 恢复进入哪个状态待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 1.1.2 恢复启动状态；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §1.1。
- PAGE: PAGE-00/01启动路由支撑，无新增启动PAGE；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 启动/恢复（非INIT）；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 1.2：状态与异常

##### Function 1.2.1：设备运行状态管理

**用户场景**：在设备启动与运行管理的设备运行状态管理环节，家庭需要“状态一致，避免同一操作在不同入口产生冲突。”。

**需求描述**：设备应统一维护当前运行状态和允许的操作；运动过程的暂停、恢复与结束由第3章定义。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 状态一致，避免同一操作在不同入口产生冲突。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备启动与运行；人员Owner TBD |
| 输入 | 启动、任务、运动、保存、同步及异常业务事实 |
| 输出 | 当前可执行操作和一致的业务状态 |
| 前置条件 | 相应状态事实可用；各守卫由所属功能维护 |
| 状态 | 设备/故障展示；仅业务/展示语义，工程枚举TBD |
| 异常 | 故障、权限或识别异常按所属分支，恢复契约TBD |
| 关联页面 | PAGE-00–08状态与异常支撑 |
| 验收标准（评审检查点） | 同一业务操作在不同入口遵循相同状态约束；执行、保存、同步分别表达。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 1.2.1 设备运行状态管理；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §1.2。
- PAGE: PAGE-00–08状态与异常支撑；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 设备/故障展示；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 1.2.2：设备故障处理

**用户场景**：在设备启动与运行管理的设备故障处理环节，家庭需要“故障时能够理解原因并恢复使用。”。

**需求描述**：设备应处理启动失败、运行服务不可用等设备级故障，给出重试、返回或重启入口；识别异常由4.1.3判断。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 故障时能够理解原因并恢复使用。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备启动与运行；人员Owner TBD |
| 输入 | 已确认启动失败或必要运行服务不可用原因 |
| 输出 | 原因说明及约定重试、返回或必要重启去向 |
| 前置条件 | 已判定为设备级故障 |
| 状态 | 设备/故障展示；仅业务/展示语义，工程枚举TBD |
| 异常 | 原因未知如实说明不可确认；故障范围/恢复时限TBD |
| 关联页面 | PAGE-00–08状态与异常支撑 |
| 验收标准（评审检查点） | 只展示可确认故障，恢复后重新验证；不替代4.1.3识别异常判定。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 故障范围与恢复时限待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 1.2.2 设备故障处理；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §1.2。
- PAGE: PAGE-00–08状态与异常支撑；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 设备/故障展示；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 1.2.3：查看设备软件版本

**用户场景**：在设备启动与运行管理的查看设备软件版本环节，家庭需要“便于核对设备版本和定位兼容问题。”。

**需求描述**：设备应提供当前软件版本，供家长或维护人员核对；属于维护支撑，不扩展OTA或远程运维。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 便于核对设备版本和定位兼容问题。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备启动与运行；人员Owner TBD |
| 输入 | 当前设备软件版本事实 |
| 输出 | 供家长/维护人员核对的真实版本 |
| 前置条件 | 可读取软件版本；展示入口按UE映射 |
| 状态 | 设备/故障展示；仅业务/展示语义，工程枚举TBD |
| 异常 | 读取失败表达规则TBD，不补造版本 |
| 关联页面 | PAGE-08设备状态 |
| 验收标准（评审检查点） | 展示与设备事实一致的软件版本；不由版本查看引入OTA或远程运维。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 1.2.3 查看设备软件版本；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §1.2。
- PAGE: PAGE-08设备状态；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 设备/故障展示；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 1.2.4：故障信息记录

**用户场景**：在设备启动与运行管理的故障信息记录环节，家庭需要“故障可定位、可复盘。”。

**需求描述**：设备应记录必要的故障原因和发生时间，供诊断使用。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 故障可定位、可复盘。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备启动与运行；人员Owner TBD |
| 输入 | 必要故障原因和发生时间 |
| 输出 | 供诊断使用的必要故障记录 |
| 前置条件 | 发生可记录故障；日志范围/周期TBD |
| 状态 | 设备/故障展示；仅业务/展示语义，工程枚举TBD |
| 异常 | 记录失败处理TBD；日志不得包含原始儿童摄像帧 |
| 关联页面 | 后台记录支撑，无独立页面承诺 |
| 验收标准（评审检查点） | 故障记录限必要信息，原始帧不进入日志；记录字段与周期TBD。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 日志内容与保存周期待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 1.2.4 故障信息记录；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §1.2。
- PAGE: 后台记录支撑，无独立页面承诺；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 设备/故障展示；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 1.2.5：设备重启

**用户场景**：在设备启动与运行管理的设备重启环节，家庭需要“无法正常使用时有恢复入口。”。

**需求描述**：设备应提供必要重启操作，重启后按1.1.2恢复状态。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 无法正常使用时有恢复入口。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备启动与运行；人员Owner TBD |
| 输入 | 获准的重启操作 |
| 输出 | 设备重启及1.1.2恢复结果 |
| 前置条件 | 重启触发方式与适用权限TBD |
| 状态 | 设备/故障展示；仅业务/展示语义，工程枚举TBD |
| 异常 | 重启失败与恢复不足按1.2.2/6.2.2；细则TBD |
| 关联页面 | PAGE-08系统设置 |
| 验收标准（评审检查点） | 重启后进入启动/恢复检查，不直接续计或伪造完成记录。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 重启触发方式待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 1.2.5 设备重启；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §1.2。
- PAGE: PAGE-08系统设置；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 设备/故障展示；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


### 5.2 一级功能：运动入口与操作

#### 二级功能 2.1：运动入口与角色回应

##### Function 2.1.1：运动入口

**用户场景**：在运动入口与操作的运动入口环节，家庭需要“减少寻找入口和开练阻力。”。

**需求描述**：设备应提供任务与自主运动入口，显示必要可用状态。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 减少寻找入口和开练阻力。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备交互；人员Owner TBD |
| 输入 | 当前任务/自主能力及必要设备可用状态 |
| 输出 | 任务与自主运动可理解入口 |
| 前置条件 | 设备进入可用首页；动作与身份按对应功能检查 |
| 状态 | 首页/运动状态回应；仅业务/展示语义，工程枚举TBD |
| 异常 | 不可用状态说明原因，不将候选入口默认开放 |
| 关联页面 | PAGE-01/02/03 |
| 验收标准（评审检查点） | 任务和自主运动入口均可理解，进入共用准备路径；不新增独立运动闭环。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-DEVICE-002；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 2.1.1 运动入口；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §2.1。
- PAGE: PAGE-01/02/03；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 首页/运动状态回应；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 2.1.2：显示角色状态表情

**用户场景**：在运动入口与操作的显示角色状态表情环节，家庭需要“运动中获得一致且适度的角色回应。”。

**需求描述**：设备应按已有运动状态显示固定表情，输出一致的角色回应；鼓励及提示内容由第5章决定。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 运动中获得一致且适度的角色回应。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备交互；人员Owner TBD |
| 输入 | 已有运动状态与固定表情资源 |
| 输出 | 与运动事实一致的固定角色回应 |
| 前置条件 | 状态事件已确认；事件/资源清单TBD |
| 状态 | 首页/运动状态回应；仅业务/展示语义，工程枚举TBD |
| 异常 | 资源不可用与降级表达TBD，不承诺新增AI对话 |
| 关联页面 | PAGE-01；PAGE-04–07按已有运动事件回应，承载TBD |
| 验收标准（评审检查点） | 角色回应与真实状态一致；原P0保留，表情丰富度和运动星/PB深度另评审。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 表情事件与资源待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-DEVICE-002；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 2.1.2 显示角色状态表情；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §2.1。
- PAGE: PAGE-01；PAGE-04–07按已有运动事件回应，承载TBD；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 首页/运动状态回应；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 2.2：状态提示与操作确认

##### Function 2.2.1：设备状态提示

**用户场景**：在运动入口与操作的设备状态提示环节，家庭需要“知道设备当前是否可用，以及怎样处理问题。”。

**需求描述**：设备应呈现设备不可用、操作不可执行等通用状态；任务内容、实时成绩和结束结果分别由第3章和第5章定义。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 知道设备当前是否可用，以及怎样处理问题。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备交互；人员Owner TBD |
| 输入 | 设备不可用或操作不可执行的已确认状态 |
| 输出 | 状态、当前影响及可处理原因 |
| 前置条件 | 设备状态事实可用；表达方式TBD |
| 状态 | 操作反馈/状态展示；仅业务/展示语义，工程枚举TBD |
| 异常 | 原因未确认时说明不可确认，不编造故障 |
| 关联页面 | PAGE-00–08通用支撑 |
| 验收标准（评审检查点） | 提示说明是否可用及可行去向；任务、成绩、结果由各主功能提供。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 表达方式待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-SPORT-004、FR-SPORT-006；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 2.2.1 设备状态提示；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §2.2。
- PAGE: PAGE-00–08通用支撑；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 操作反馈/状态展示；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 2.2.2：操作接收与确认

**用户场景**：在运动入口与操作的操作接收与确认环节，家庭需要“清楚操作是否生效。”。

**需求描述**：设备应接收选择、开始、取消、暂停、继续、结束及返回操作，并告知是否接受；各操作业务结果由所属功能负责。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 清楚操作是否生效。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备交互；人员Owner TBD |
| 输入 | 选择、开始、取消、暂停、继续、结束、返回意图 |
| 输出 | 操作是否被接受的反馈 |
| 前置条件 | 所属业务状态允许该操作；实际输入方式TBD |
| 状态 | 操作反馈/状态展示；仅业务/展示语义，工程枚举TBD |
| 异常 | 不允许/未接受须区分；业务失败由所属功能说明 |
| 关联页面 | PAGE-00–08通用支撑 |
| 验收标准（评审检查点） | 接收确认与业务执行结果分别表达；不默认触控、语音或手势。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 触控、按键或其他输入方式待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-001、FR-SPORT-004、FR-SPORT-006；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 2.2.2 操作接收与确认；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §2.2。
- PAGE: PAGE-00–08通用支撑；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 操作反馈/状态展示；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


### 5.3 一级功能：运动任务与执行

#### 二级功能 3.1：任务接收与查看

##### Function 3.1.1：接收并检查运动任务

**用户场景**：在运动任务与执行的接收并检查运动任务环节，家庭需要“收到可执行而非无效任务。”。

**需求描述**：设备应检查送达任务的儿童归属、支持动作、目标和有效条件，输出接受资格或拒绝原因；最终接收回执由3.1.2负责。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 收到可执行而非无效任务。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 送达任务的儿童归属、支持动作、目标、有效条件 |
| 输出 | 接受资格或拒绝原因 |
| 前置条件 | 收到任务，相关规则可检查；细则TBD |
| 状态 | INIT / 任务有效性；仅业务/展示语义，工程枚举TBD |
| 异常 | 归属/动作/目标/有效性不满足则给可确认原因 |
| 关联页面 | PAGE-03消费后台接收事实，不新增接收页面 |
| 验收标准（评审检查点） | 未通过检查不称可执行；任务到达不自动开始或开启摄像头。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 任务检查规则待确认 |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-SPORT-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.1.1 接收并检查运动任务；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.1。
- PAGE: PAGE-03消费后台接收事实，不新增接收页面；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: INIT / 任务有效性；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 3.1.2：反馈任务接收结果

**用户场景**：在运动任务与执行的反馈任务接收结果环节，家庭需要“家长知道任务是否真实送达。”。

**需求描述**：设备应检查通过并由6.2.1保存后确认接收；失败说明原因；重复任务返回同一接收结果。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 家长知道任务是否真实送达。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 3.1.1检查结果、6.2.1任务保存事实 |
| 输出 | 真实接收结果或失败原因 |
| 前置条件 | 检查通过且保存成功才确认接收 |
| 状态 | INIT / 任务有效性；仅业务/展示语义，工程枚举TBD |
| 异常 | 检查/保存失败说明原因；重复任务沿用同一接收结果 |
| 关联页面 | PAGE-03消费后台接收事实，不新增接收页面 |
| 验收标准（评审检查点） | 检查并成功保存后才确认接收；重复投递不产生多条不同接收事实。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-SPORT-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.1.2 反馈任务接收结果；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.1。
- PAGE: PAGE-03消费后台接收事实，不新增接收页面；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: INIT / 任务有效性；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 3.1.3：展示任务内容与执行状态

**用户场景**：在运动任务与执行的展示任务内容与执行状态环节，家庭需要“儿童明白为什么做、做多少。”。

**需求描述**：设备应提供动作、目标与来源，呈现设备执行状态；平台任务撤销等有效规则另行确认，不由设备自建发布规则。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 儿童明白为什么做、做多少。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 任务动作、目标、来源和设备执行状态 |
| 输出 | 儿童可理解任务内容与状态 |
| 前置条件 | 存在可查看任务事实；列表/详情拆分TBD |
| 状态 | INIT / 任务有效性；仅业务/展示语义，工程枚举TBD |
| 异常 | 无任务/任务无效如实表达；撤销/过期细则TBD |
| 关联页面 | PAGE-03 |
| 验收标准（评审检查点） | 动作、目标、来源及执行状态一致，不静默改家长目标或自建发布规则。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 任务状态及撤销规则待确认 |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-SPORT-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.1.3 展示任务内容与执行状态；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.1。
- PAGE: PAGE-03；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: INIT / 任务有效性；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 3.1.4：动作与目标确认

**用户场景**：在运动任务与执行的动作与目标确认环节，家庭需要“运动目标清楚，自主运动与家长任务不混淆。”。

**需求描述**：设备应执行任务时确认已下发动作和目标；自主运动时选择支持动作及允许目标，不擅自修改家长任务。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 运动目标清楚，自主运动与家长任务不混淆。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 自主选择的支持动作/允许目标，或已下发任务动作/目标 |
| 输出 | 明确的运动目标、来源与归属上下文 |
| 前置条件 | 当前儿童及目标有效；自主目标范围TBD |
| 状态 | INIT / 任务有效性；仅业务/展示语义，工程枚举TBD |
| 异常 | 不支持动作或无效目标不伪装可开始 |
| 关联页面 | PAGE-02/03 |
| 验收标准（评审检查点） | 自主与任务来源区分；家长任务只确认原目标，自主目标允许范围另评审。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 自主目标范围待确认 |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-SPORT-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.1.4 动作与目标确认；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.1。
- PAGE: PAGE-02/03；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: INIT / 任务有效性；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 3.2：运动准备与开始

##### Function 3.2.1：动作说明

**用户场景**：在运动任务与执行的动作说明环节，家庭需要“减少不理解动作造成的失败。”。

**需求描述**：设备应开始前提供经审核、儿童可理解的动作与安全说明。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 减少不理解动作造成的失败。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 已确认动作、经审核动作与安全说明 |
| 输出 | 儿童可理解的动作/安全说明 |
| 前置条件 | 开始前已选定动作；媒体形态和跳过规则TBD |
| 状态 | READY / COUNTDOWN；仅业务/展示语义，工程枚举TBD |
| 异常 | 资源缺失/加载失败规则TBD，安全前置不能自行省略 |
| 关联页面 | PAGE-04 |
| 验收标准（评审检查点） | 说明有审核依据；不将AI生成示范当成有效动作规则或默认视频方案。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 媒体形态/可跳过规则待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-002、FR-SPORT-003、FR-SPORT-004；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.2.1 动作说明；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.2。
- PAGE: PAGE-04；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: READY / COUNTDOWN；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 3.2.2：入镜准备引导

**用户场景**：在运动任务与执行的入镜准备引导环节，家庭需要“知道如何站好，准备完成后再开练。”。

**需求描述**：设备应根据第4章识别结果提示调整站位；准备不足时不开始运动。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 知道如何站好，准备完成后再开练。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 4.1.1画面/人体可用性与准备原因 |
| 输出 | 主要站位调整提示及准备状态 |
| 前置条件 | 目标与归属明确，隐私允许才识别准备 |
| 状态 | READY / COUNTDOWN；仅业务/展示语义，工程枚举TBD |
| 异常 | 无人、身体不完整、画面不可用则调整并复核 |
| 关联页面 | PAGE-04；PAGE-09仅候选复用依据 |
| 验收标准（评审检查点） | 准备不足不得开始；提示依据检测事实，不默认视频预览或骨架显示。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 准备完成条件待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-002、FR-SPORT-003、FR-SPORT-004；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.2.2 入镜准备引导；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.2。
- PAGE: PAGE-04；PAGE-09仅候选复用依据；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: READY / COUNTDOWN；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 3.2.3：开始确认与倒计时

**用户场景**：在运动任务与执行的开始确认与倒计时环节，家庭需要“有时间准备，避免突然计数。”。

**需求描述**：设备应儿童明确开始且准备满足后倒计时，结束再检查开始条件。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 有时间准备，避免突然计数。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 儿童明确开始意愿、准备满足与隐私事实 |
| 输出 | 倒计时与结束后的开始资格复核 |
| 前置条件 | 准备满足、隐私允许、儿童明确开始 |
| 状态 | READY / COUNTDOWN；仅业务/展示语义，工程枚举TBD |
| 异常 | 取消/离画回准备；隐私失效阻断；时长TBD |
| 关联页面 | PAGE-04/05 |
| 验收标准（评审检查点） | 准备/倒计时不计数；倒计时结束仍须复核；恢复是否再倒计时TBD。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 输入方式待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-002、FR-SPORT-003、FR-SPORT-004；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.2.3 开始确认与倒计时；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.2。
- PAGE: PAGE-04/05；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: READY / COUNTDOWN；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 3.3：暂停、继续与结束

##### Function 3.3.1：暂停与成绩保留

**用户场景**：在运动任务与执行的暂停与成绩保留环节，家庭需要“已完成努力不因中断消失。”。

**需求描述**：设备应主动暂停或离画/识别异常时停止新增成绩，保留已确认次数。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 已完成努力不因中断消失。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 主动暂停或已判定需暂停的离画/识别异常 |
| 输出 | 暂停状态、原因及已确认次数 |
| 前置条件 | 运动正在执行；暂停触发判定按所属功能 |
| 状态 | RUNNING / PAUSED / FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 单个不确定事件不一律暂停；异常阈值TBD |
| 关联页面 | PAGE-06/04；再次经过PAGE-05与否TBD |
| 验收标准（评审检查点） | 暂停停止新增成绩并保留已确认次数，不清零努力。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-SPORT-006、FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.3.1 暂停与成绩保留；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.3。
- PAGE: PAGE-06/04；再次经过PAGE-05与否TBD；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING / PAUSED / FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 3.3.2：恢复运动

**用户场景**：在运动任务与执行的恢复运动环节，家庭需要“安全且连贯地继续运动。”。

**需求描述**：设备应重新检查隐私和准备，明确恢复后从已确认成绩继续。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 安全且连贯地继续运动。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 继续意愿、已确认成绩、隐私与准备复核结果 |
| 输出 | 获准恢复或仍需处理原因 |
| 前置条件 | 重新检查隐私/准备并明确恢复 |
| 状态 | RUNNING / PAUSED / FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 隐私或准备不足不能恢复；恢复确认/再倒计时TBD |
| 关联页面 | PAGE-06/04；再次经过PAGE-05与否TBD |
| 验收标准（评审检查点） | 从保留成绩继续，重新判断动作起点/重置半周期；不能直接绕过准备恢复。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 恢复时重新判断动作起点；恢复确认方式待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-006、FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.3.2 恢复运动；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.3。
- PAGE: PAGE-06/04；再次经过PAGE-05与否TBD；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING / PAUSED / FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 3.3.3：达标与提前结束

**用户场景**：在运动任务与执行的达标与提前结束环节，家庭需要“不强迫继续，不伪造达标。”。

**需求描述**：设备应达标停止确认动作；主动结束保留实际与真实未完成状态。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 不强迫继续，不伪造达标。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备任务与执行；人员Owner TBD |
| 输入 | 真实成绩、目标、主动结束意愿或已确认中断规则 |
| 输出 | 真实达标或提前结束事实 |
| 前置条件 | 达标、主动结束或已确认规则生效 |
| 状态 | FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 自动超时结束规则TBD，不凭空结束并声称达标 |
| 关联页面 | PAGE-06 → PAGE-07 |
| 验收标准（评审检查点） | 结束停止新增计数；提前结束保留实际成绩和真实未达标状态。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 自动超时结束规则待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-006、FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 3.3.3 达标与提前结束；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §3.3。
- PAGE: PAGE-06 → PAGE-07；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


### 5.4 一级功能：动作识别与计数

#### 二级功能 4.1：识别状态与有效计数

##### Function 4.1.1：人体与画面可用性检测

**用户场景**：在动作识别与计数的人体与画面可用性检测环节，家庭需要“避免在看不清动作时开始计数。”。

**需求描述**：设备应判断是否有人、身体是否完整及画面是否满足识别条件，输出准备状态和原因；引导由3.2.2负责。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 避免在看不清动作时开始计数。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备识别能力；人员Owner TBD |
| 输入 | 有效授权下的人体和画面输入 |
| 输出 | 有人/完整性/画面可用状态及主要原因 |
| 前置条件 | 授权及本地隐私允许且状态可确认 |
| 状态 | READY / COUNTDOWN / RUNNING / PAUSED；仅业务/展示语义，工程枚举TBD |
| 异常 | 无人、身体不完整、遮挡/画面不可用；多人/距离TBD |
| 关联页面 | PAGE-04/05/06；PAGE-09仅候选复用依据 |
| 验收标准（评审检查点） | 检测结果提供给准备与异常处理，不在画面不满足条件时开始可信计数。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 多人处理及适用距离待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-003、FR-SPORT-005、FR-SPORT-006；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 4.1.1 人体与画面可用性检测；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §4.1。
- PAGE: PAGE-04/05/06；PAGE-09仅候选复用依据；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: READY / COUNTDOWN / RUNNING / PAUSED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 4.1.2：有效动作计数

**用户场景**：在动作识别与计数的有效动作计数环节，家庭需要“孩子和家长得到可信成绩。”。

**需求描述**：设备应依据审核规则仅累计完整有效周期，未完成、重复或不确定事件不计。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 孩子和家长得到可信成绩。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备识别能力；人员Owner TBD |
| 输入 | 审核动作规则和已判定完整有效周期事件 |
| 输出 | 已确认有效次数 |
| 前置条件 | RUNNING且隐私/识别准入有效；规则阈值TBD |
| 状态 | READY / COUNTDOWN / RUNNING / PAUSED；仅业务/展示语义，工程枚举TBD |
| 异常 | 不完整、重复、不确定事件不计；异常由4.1.3判定 |
| 关联页面 | PAGE-06，异常准备原因由PAGE-04承接 |
| 验收标准（评审检查点） | 一次完整有效周期只计一次，未完成/重复/不确定事件不增加成绩；量化阈值TBD。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 阈值待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-003、FR-SPORT-005、FR-SPORT-006；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 4.1.2 有效动作计数；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §4.1。
- PAGE: PAGE-06，异常准备原因由PAGE-04承接；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: READY / COUNTDOWN / RUNNING / PAUSED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 4.1.3：判定运动识别异常

**用户场景**：在动作识别与计数的判定运动识别异常环节，家庭需要“知道如何调整，而非被错误指责。”。

**需求描述**：设备应根据4.1.1画面状态和4.2动作判定输出无人、遮挡、识别不确定或不可用原因；暂停由3.3.1处理，提示由5.1.2呈现。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 知道如何调整，而非被错误指责。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备识别能力；人员Owner TBD |
| 输入 | 4.1.1画面状态和4.2动作判定 |
| 输出 | 无人、遮挡、识别不确定或不可用原因 |
| 前置条件 | 识别事实可确认 |
| 状态 | READY / COUNTDOWN / RUNNING / PAUSED；仅业务/展示语义，工程枚举TBD |
| 异常 | 单次不确定与需暂停异常分开，判定阈值TBD |
| 关联页面 | PAGE-06，异常准备原因由PAGE-04承接 |
| 验收标准（评审检查点） | 只输出已判定原因；暂停交3.3.1，调整提示交5.1.2，低置信度不作确定纠错。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-SPORT-003、FR-SPORT-005、FR-SPORT-006；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 4.1.3 判定运动识别异常；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §4.1。
- PAGE: PAGE-06，异常准备原因由PAGE-04承接；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: READY / COUNTDOWN / RUNNING / PAUSED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 4.2：三种动作识别

##### Function 4.2.1：开合跳动作判定

**用户场景**：在动作识别与计数的开合跳动作判定环节，家庭需要“完整开合跳被可信记录。”。

**需求描述**：设备应判断并拢、打开、回收是否形成完整有效周期，供4.1.2累计次数。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 完整开合跳被可信记录。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备识别能力；人员Owner TBD |
| 输入 | 开合跳阶段事实及审核有效规则 |
| 输出 | 供4.1.2使用的完整有效周期间事实 |
| 前置条件 | 当前动作是开合跳且处于RUNNING；幅度/规则TBD |
| 状态 | RUNNING；仅业务/展示语义，工程枚举TBD |
| 异常 | 半周期/不确定判定不作有效事件 |
| 关联页面 | PAGE-06计数依据，不新增动作范围 |
| 验收标准（评审检查点） | 并拢→打开→回收符合审核规则才构成周期；不自定幅度阈值。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 有效幅度与规则待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-005；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 4.2.1 开合跳动作判定；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §4.2。
- PAGE: PAGE-06计数依据，不新增动作范围；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 4.2.2：深蹲起动作判定

**用户场景**：在动作识别与计数的深蹲起动作判定环节，家庭需要“完整深蹲被可信记录。”。

**需求描述**：设备应判断站立、有效下蹲、回站立是否形成完整周期，供4.1.2累计次数。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 完整深蹲被可信记录。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备识别能力；人员Owner TBD |
| 输入 | 站立、下蹲、回站立阶段及审核规则 |
| 输出 | 供4.1.2使用的完整有效周期事实 |
| 前置条件 | 当前动作是深蹲起且处于RUNNING；安全/幅度TBD |
| 状态 | RUNNING；仅业务/展示语义，工程枚举TBD |
| 异常 | 未完整回站立或不确定事件不作有效周期 |
| 关联页面 | PAGE-06计数依据，不新增动作范围 |
| 验收标准（评审检查点） | 站立→有效下蹲→回站立按审核规则判定；不自定安全或角度标准。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 安全与有效幅度规则待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-005；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 4.2.2 深蹲起动作判定；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §4.2。
- PAGE: PAGE-06计数依据，不新增动作范围；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 4.2.3：高抬腿动作判定

**用户场景**：在动作识别与计数的高抬腿动作判定环节，家庭需要“目标与实际成绩使用一致口径。”。

**需求描述**：设备应判断有效抬腿与落下事件，按统一左右侧规则供4.1.2累计次数。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 目标与实际成绩使用一致口径。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备识别能力；人员Owner TBD |
| 输入 | 抬腿/落下及左右侧事件、审核计数口径 |
| 输出 | 按一致左右规则供4.1.2使用的事件 |
| 前置条件 | 当前动作是高抬腿且处于RUNNING；单/双侧口径TBD |
| 状态 | RUNNING；仅业务/展示语义，工程枚举TBD |
| 异常 | 目标与成绩口径未确认不得写成固定规则 |
| 关联页面 | PAGE-06计数依据，不新增动作范围 |
| 验收标准（评审检查点） | 目标与结果采用同一已确认左右侧规则；本稿不选择单侧一次或双侧一轮。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 单侧一次或双侧一轮待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-005；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 4.2.3 高抬腿动作判定；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §4.2。
- PAGE: PAGE-06计数依据，不新增动作范围；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


### 5.5 一级功能：运动反馈与结果展示

#### 二级功能 5.1：即时反馈

##### Function 5.1.1：次数与进度反馈

**用户场景**：在运动反馈与结果展示的次数与进度反馈环节，家庭需要“看见实际努力和距目标的差距。”。

**需求描述**：设备应呈现设备已确认次数与目标进度，必要短语音与数字保持一致。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 看见实际努力和距目标的差距。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备反馈呈现；人员Owner TBD |
| 输入 | 设备已确认次数、目标与识别状态 |
| 输出 | 一致的次数、进度与必要短语音 |
| 前置条件 | 存在真实已确认成绩；反馈频率TBD |
| 状态 | RUNNING / FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 未确认事件不进入显示成绩；异常依5.1.2 |
| 关联页面 | PAGE-06 |
| 验收标准（评审检查点） | 数字和短语音基于同一设备成绩，不由页面/App另行递增。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 频率待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-005、FR-DEVICE-002；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 5.1.1 次数与进度反馈；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §5.1。
- PAGE: PAGE-06；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING / FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 5.1.2：动作反馈与调整提示

**用户场景**：在运动反馈与结果展示的动作反馈与调整提示环节，家庭需要“得到可理解指导且减少挫败。”。

**需求描述**：设备应有效动作给正向回应；无效或识别不确定给一个可处理原因。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 得到可理解指导且减少挫败。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备反馈呈现；人员Owner TBD |
| 输入 | 有效/无效/不确定动作及已判定主要原因 |
| 输出 | 正向回应或一个可处理调整提示 |
| 前置条件 | 反馈依据已确认识别事实 |
| 状态 | RUNNING / FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 低置信度如实说明不确定，不确定纠错或责备 |
| 关联页面 | PAGE-06 |
| 验收标准（评审检查点） | 有效动作获得适度回应，异常提示具体且可处理；不作医疗/身材评价。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-SPORT-005、FR-DEVICE-002；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 5.1.2 动作反馈与调整提示；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §5.1。
- PAGE: PAGE-06；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING / FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 5.1.3：完成鼓励

**用户场景**：在运动反馈与结果展示的完成鼓励环节，家庭需要“获得尊重真实努力的反馈。”。

**需求描述**：设备应真实结束后提供适度鼓励，区分达标和提前结束。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 获得尊重真实努力的反馈。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备反馈呈现；人员Owner TBD |
| 输入 | 真实结束、达标或提前结束事实 |
| 输出 | 尊重真实努力的适度完成鼓励 |
| 前置条件 | 运动确已结束；运动星/PB深度TBD |
| 状态 | RUNNING / FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 提前结束不得表达为达标；候选成长深度不默认开放 |
| 关联页面 | PAGE-07 |
| 验收标准（评审检查点） | 达标与提前结束分别表达，保留原P0基础鼓励，不扩展成长体系。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 运动星/PB深度待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-005、FR-DEVICE-002；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 5.1.3 完成鼓励；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §5.1。
- PAGE: PAGE-07；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: RUNNING / FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 5.2：结果查看与保存提示

##### Function 5.2.1：运动结果查看

**用户场景**：在运动反馈与结果展示的运动结果查看环节，家庭需要“儿童结束后能理解本次努力。”。

**需求描述**：设备应在设备端显示动作、目标、实际次数、用时和达标或提前结束状态；家长端展示不属于此项。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 儿童结束后能理解本次努力。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备反馈呈现；人员Owner TBD |
| 输入 | 已保存的动作、目标、实际次数、用时、结束原因 |
| 输出 | 设备端简要真实结果 |
| 前置条件 | 本地结果保存事实可确认；用时是否含暂停TBD |
| 状态 | FINISHED / SAVED / SYNCING / SYNCED；仅业务/展示语义，工程枚举TBD |
| 异常 | 保存失败与同步状态分别说明，不称未确认结果完成 |
| 关联页面 | PAGE-07 |
| 验收标准（评审检查点） | 儿童能辨认实际与目标以及达标/提前结束；用时定义不在本稿冻结。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 用时是否含暂停待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 5.2.1 运动结果查看；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §5.2。
- PAGE: PAGE-07；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: FINISHED / SAVED / SYNCING / SYNCED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 5.2.2：保存与同步提示

**用户场景**：在运动反馈与结果展示的保存与同步提示环节，家庭需要“不把运动结束误解为已回传。”。

**需求描述**：设备应分别说明本地已保存、等待同步、同步成功或失败。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 不把运动结束误解为已回传。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备反馈呈现；人员Owner TBD |
| 输入 | 本地保存结果与独立平台同步确认 |
| 输出 | 未保存/已保存/待同步/成功或失败提示 |
| 前置条件 | 相应保存或同步事实可确认 |
| 状态 | FINISHED / SAVED / SYNCING / SYNCED；仅业务/展示语义，工程枚举TBD |
| 异常 | 保存失败不称已记录；发送完成不称平台已收到 |
| 关联页面 | PAGE-07；必要同步提示PAGE-01 |
| 验收标准（评审检查点） | 运动结束、本地保存、业务接收各自表达，可以同时呈现提前结束/已保存/待同步。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 5.2.2 保存与同步提示；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §5.2。
- PAGE: PAGE-07；必要同步提示PAGE-01；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: FINISHED / SAVED / SYNCING / SYNCED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


### 5.6 一级功能：运动记录与同步

#### 二级功能 6.1：运动记录

##### Function 6.1.1：记录创建与归属

**用户场景**：在运动记录与同步的记录创建与归属环节，家庭需要“每次运动可以追溯到正确儿童。”。

**需求描述**：设备应建立唯一运动记录并关联儿童、任务或自主来源及动作目标。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 每次运动可以追溯到正确儿童。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备记录与同步；人员Owner TBD |
| 输入 | 当前儿童、任务或自主来源、动作与目标上下文 |
| 输出 | 唯一运动记录归属 |
| 前置条件 | 来源和归属明确；创建时机TBD |
| 状态 | 创建时机TBD / FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 归属不明不得错分成绩；重复操作不重建同一结果 |
| 关联页面 | PAGE-02/03/06/07共用事实支撑，无重复记录系统 |
| 验收标准（评审检查点） | 同一运动可追溯至正确儿童及来源；不把INIT等同记录已创建。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 开始记录时机待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 6.1.1 记录创建与归属；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §6.1。
- PAGE: PAGE-02/03/06/07共用事实支撑，无重复记录系统；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 创建时机TBD / FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 6.1.2：生成运动结果记录

**用户场景**：在运动记录与同步的生成运动结果记录环节，家庭需要“可信查看真实完成情况。”。

**需求描述**：设备应汇总已确认次数、目标、用时与结束原因，输出唯一记录内容；本地写入归6.2.1。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 可信查看真实完成情况。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备记录与同步；人员Owner TBD |
| 输入 | 已确认次数、目标、用时、真实结束原因 |
| 输出 | 同一运动的唯一结果内容 |
| 前置条件 | 真实结束且事实可汇总；用时定义TBD |
| 状态 | 创建时机TBD / FINISHED；仅业务/展示语义，工程枚举TBD |
| 异常 | 不完整/未知内容不伪造；写入由6.2.1执行 |
| 关联页面 | PAGE-02/03/06/07共用事实支撑，无重复记录系统 |
| 验收标准（评审检查点） | 输出真实结果及同一记录内容，提前结束不伪称达标。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 6.1.2 生成运动结果记录；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §6.1。
- PAGE: PAGE-02/03/06/07共用事实支撑，无重复记录系统；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 创建时机TBD / FINISHED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 6.2：本地保存与记录恢复

##### Function 6.2.1：本地保存

**用户场景**：在运动记录与同步的本地保存环节，家庭需要“离线可使用、不丢记录。”。

**需求描述**：设备应保存已缓存任务、实际结果和必要待同步信息。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 离线可使用、不丢记录。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备记录与同步；人员Owner TBD |
| 输入 | 已缓存任务、实际结果、必要待同步信息 |
| 输出 | 本地保存成功或失败事实 |
| 前置条件 | 需保存的任务/结果存在；容量/周期TBD |
| 状态 | 保存维度：SAVED / 未保存；仅业务/展示语义，工程枚举TBD |
| 异常 | 保存失败交6.2.3，未经保存不按已保存结果同步 |
| 关联页面 | PAGE-01/03/06/07消费保存恢复事实；后台处理 |
| 验收标准（评审检查点） | 本地保存状态有真实依据；原始摄像帧不写入记录、日志或缓存。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 存储容量/保留周期待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-007、FR-DEVICE-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 6.2.1 本地保存；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §6.2。
- PAGE: PAGE-01/03/06/07消费保存恢复事实；后台处理；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 保存维度：SAVED / 未保存；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 6.2.2：已保存记录恢复

**用户场景**：在运动记录与同步的已保存记录恢复环节，家庭需要“重启后不产生重复或虚假的运动记录。”。

**需求描述**：设备应读取可恢复的任务、运动记录及待同步信息，保持真实已确认成绩，向1.1.2提供恢复结果。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 重启后不产生重复或虚假的运动记录。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备记录与同步；人员Owner TBD |
| 输入 | 本地可恢复的任务、运动记录、待同步信息 |
| 输出 | 可恢复真实事实供1.1.2使用 |
| 前置条件 | 启动/重启需恢复；保存频率与断电范围TBD |
| 状态 | 保存/恢复：SAVED或失败；仅业务/展示语义，工程枚举TBD |
| 异常 | 不可恢复部分如实说明，不补造成绩或重复记录 |
| 关联页面 | PAGE-01/03/06/07消费保存恢复事实；后台处理 |
| 验收标准（评审检查点） | 仅恢复可确认成绩与同步事实，不自动续计；断电可恢复保证TBD。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 保存频率及断电可恢复范围待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-007、FR-DEVICE-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 6.2.2 已保存记录恢复；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §6.2。
- PAGE: PAGE-01/03/06/07消费保存恢复事实；后台处理；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 保存/恢复：SAVED或失败；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 6.2.3：保存失败处理

**用户场景**：在运动记录与同步的保存失败处理环节，家庭需要“不误导家长或静默丢失。”。

**需求描述**：设备应明确未保存并保留可恢复结果供重试。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 不误导家长或静默丢失。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备记录与同步；人员Owner TBD |
| 输入 | 保存失败事实及仍可恢复的结果 |
| 输出 | 尚未保存说明与可恢复结果重试 |
| 前置条件 | 本地写入失败已判定 |
| 状态 | 保存/恢复：SAVED或失败；仅业务/展示语义，工程枚举TBD |
| 异常 | 恢复保证、退出/不可恢复处理TBD |
| 关联页面 | PAGE-01/03/06/07消费保存恢复事实；后台处理 |
| 验收标准（评审检查点） | 失败不称保存成功，保留可恢复结果供重试；不承诺未经验证的零丢失保证。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 失败恢复保证待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-007、FR-DEVICE-001；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 6.2.3 保存失败处理；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §6.2。
- PAGE: PAGE-01/03/06/07消费保存恢复事实；后台处理；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 保存/恢复：SAVED或失败；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 6.3：结果同步

##### Function 6.3.1：上传结果并更新同步状态

**用户场景**：在运动记录与同步的上传结果并更新同步状态环节，家庭需要“家长查看同一真实记录。”。

**需求描述**：设备应发送已保存结果，依据平台业务接收确认更新同步状态；不把网络发送完成视为成功接收。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 家长查看同一真实记录。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备记录与同步；人员Owner TBD |
| 输入 | 已保存结果、原记录标识、平台业务接收确认 |
| 输出 | 独立上传/同步状态 |
| 前置条件 | 记录已保存且允许上传；协议TBD |
| 状态 | SAVED / SYNCING / SYNCED；仅业务/展示语义，工程枚举TBD |
| 异常 | 发送/上传失败或无业务确认保持待确认/待补传 |
| 关联页面 | PAGE-07/01消费独立同步状态，后台处理 |
| 验收标准（评审检查点） | 仅平台业务接收确认后表示SYNCED；网络发送完成不作为成功接收。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 协议待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 6.3.1 上传结果并更新同步状态；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §6.3。
- PAGE: PAGE-07/01消费独立同步状态，后台处理；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: SAVED / SYNCING / SYNCED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 6.3.2：补传失败结果并防重复

**用户场景**：在运动记录与同步的补传失败结果并防重复环节，家庭需要“没有重复记录或虚假成长。”。

**需求描述**：设备应设备沿用原记录标识补传；平台按同一标识去重。设备不重复生成结果或发放已批准奖励。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 没有重复记录或虚假成长。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备记录与同步；人员Owner TBD |
| 输入 | 原记录标识及失败待补传记录 |
| 输出 | 同一记录补传及防重复结果 |
| 前置条件 | 同一结果已保存但未获确认；重试/冲突TBD |
| 状态 | SAVED / SYNCING / SYNCED；仅业务/展示语义，工程枚举TBD |
| 异常 | 失败按契约继续待补传，不重建记录 |
| 关联页面 | PAGE-07/01消费独立同步状态，后台处理 |
| 验收标准（评审检查点） | 设备沿用原标识，平台按标识去重，不重复生成结果或发放已批准奖励。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 重试/冲突策略待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 6.3.2 补传失败结果并防重复；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §6.3。
- PAGE: PAGE-07/01消费独立同步状态，后台处理；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: SAVED / SYNCING / SYNCED；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


### 5.7 一级功能：联网与使用者管理

#### 二级功能 7.1：网络连接与状态提示

##### Function 7.1.1：网络连接管理

**用户场景**：在联网与使用者管理的网络连接管理环节，家庭需要“可完成连接并理解故障。”。

**需求描述**：设备应提供必要联网配置及连接状态，失败给出可操作原因。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 可完成连接并理解故障。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备联网与使用者管理；人员Owner TBD |
| 输入 | 允许的联网配置及真实连接状态 |
| 输出 | 连接状态或可处理失败原因 |
| 前置条件 | 需要完成联网；流程/责任端TBD |
| 状态 | 在线/离线（独立维度）；仅业务/展示语义，工程枚举TBD |
| 异常 | 连接失败如实说明，不能由断网解除绑定 |
| 关联页面 | PAGE-00/08；PAGE-01必要状态提示 |
| 验收标准（评审检查点） | 必要配置和连接状态可理解，不默认新增网络诊断工具。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 配网流程及责任端待确认 |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 7.1.1 网络连接管理；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §7.1。
- PAGE: PAGE-00/08；PAGE-01必要状态提示；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 在线/离线（独立维度）；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 7.1.2：联网状态提示

**用户场景**：在联网与使用者管理的联网状态提示环节，家庭需要“理解联网状态与当前可用能力。”。

**需求描述**：设备应显示在线、离线或恢复连接；离线继续运动由第3章支持，本地保存与补传由第6章负责。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 理解联网状态与当前可用能力。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备联网与使用者管理；人员Owner TBD |
| 输入 | 在线/离线/恢复连接事实 |
| 输出 | 与本地可用能力一致的网络提示 |
| 前置条件 | 连接状态可确认 |
| 状态 | 在线/离线（独立维度）；仅业务/展示语义，工程枚举TBD |
| 异常 | 断网影响新任务/同步，不等同暂停或解绑 |
| 关联页面 | PAGE-00/08；PAGE-01必要状态提示 |
| 验收标准（评审检查点） | 离线提示区分已缓存任务和未送达任务；允许本地运动、保存与后续补传保持。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-SPORT-007；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 7.1.2 联网状态提示；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §7.1。
- PAGE: PAGE-00/08；PAGE-01必要状态提示；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 在线/离线（独立维度）；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 7.2：平台状态同步与使用者确认

##### Function 7.2.1：设备状态同步

**用户场景**：在联网与使用者管理的设备状态同步环节，家庭需要“家长端了解设备可用状态。”。

**需求描述**：设备应向平台同步必要的在线状态、运行状态及软件版本；任务接收确认由3.1.2负责，运动结果由6.3负责。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 家长端了解设备可用状态。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备联网与使用者管理；人员Owner TBD |
| 输入 | 必要在线/运行状态及软件版本 |
| 输出 | 供平台传递/保存的必要设备状态 |
| 前置条件 | 状态来源真实；内容/时机/连接方式TBD |
| 状态 | 绑定/儿童/设备状态；仅业务/展示语义，工程枚举TBD |
| 异常 | 状态发送失败处理TBD，不代替任务/结果回执 |
| 关联页面 | 后台同步支撑，非独立页面 |
| 验收标准（评审检查点） | 只同步必要设备事实；任务接收归3.1.2，结果同步归6.3。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 同步内容、时机与连接方式待确认 |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 7.2.1 设备状态同步；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §7.2。
- PAGE: 后台同步支撑，非独立页面；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 绑定/儿童/设备状态；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 7.2.3：绑定状态与当前儿童确认

**用户场景**：在联网与使用者管理的绑定状态与当前儿童确认环节，家庭需要“避免记录分配给错误儿童。”。

**需求描述**：设备应读取并确认设备绑定关系及当前儿童身份，供任务和运动记录关联使用；不默认以人脸识别确认身份。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 避免记录分配给错误儿童。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备联网与使用者管理；人员Owner TBD |
| 输入 | 平台有效绑定关系与当前儿童上下文 |
| 输出 | 供任务/记录使用的确认归属 |
| 前置条件 | 有效绑定和儿童事实需确认；流程/切换TBD |
| 状态 | 绑定/儿童/设备状态；仅业务/展示语义，工程枚举TBD |
| 异常 | 绑定失败或儿童不明按准入分支；断网不自动解绑 |
| 关联页面 | PAGE-00/08；PAGE-01使用有效上下文 |
| 验收标准（评审检查点） | 成绩归属正确儿童，不默认人脸识别，不自行创建账号或云端关系。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 绑定流程、多儿童切换待确认 |

**Traceability**

- Baseline: B §3，FR-TASK-001、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 7.2.3 绑定状态与当前儿童确认；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §7.2。
- PAGE: PAGE-00/08；PAGE-01使用有效上下文；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 绑定/儿童/设备状态；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


### 5.8 一级功能：隐私控制与数据管理

#### 二级功能 8.1：摄像头使用控制

##### Function 8.1.1：检查授权并阻断不允许的采集

**用户场景**：在隐私控制与数据管理的检查授权并阻断不允许的采集环节，家庭需要“家长边界可控且可解释。”。

**需求描述**：设备应检查有效授权及本地隐私状态，输出允许或阻断；未授权、关闭或未知禁止采集，不负责家长账号授权流程。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 家长边界可控且可解释。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备隐私与权限；人员Owner TBD |
| 输入 | 有效授权及真实本地隐私/硬件状态 |
| 输出 | 允许采集或阻断事实 |
| 前置条件 | 采集前及继续识别时需满足授权/隐私条件 |
| 状态 | 隐私准入/采集状态；仅业务/展示语义，工程枚举TBD |
| 异常 | 未授权、关闭、撤权或未知均阻断 |
| 关联页面 | PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守 |
| 验收标准（评审检查点） | 所有采集入口遵守同一守卫；远程任务无法绕过本地关闭。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | — |

**Traceability**

- Baseline: B §3，FR-SPORT-003、FR-SPORT-006、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 8.1.1 检查授权并阻断不允许的采集；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §8.1。
- PAGE: PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 隐私准入/采集状态；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 8.1.2：摄像头状态提示与关闭

**用户场景**：在隐私控制与数据管理的摄像头状态提示与关闭环节，家庭需要“知道摄像头是否工作，并能停止采集。”。

**需求描述**：设备应显示真实采集状态；运动退出或授权撤销后停止采集，不能通过远程任务绕过本地关闭状态。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 知道摄像头是否工作，并能停止采集。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备隐私与权限；人员Owner TBD |
| 输入 | 真实采集状态、运动退出或撤权事实 |
| 输出 | 摄像头状态提示及停止采集事实 |
| 前置条件 | 状态可确认；提示方式与撤权响应TBD |
| 状态 | 隐私准入/采集状态；仅业务/展示语义，工程枚举TBD |
| 异常 | 撤权/关闭或状态未知先阻断；响应时限TBD |
| 关联页面 | PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守 |
| 验收标准（评审检查点） | 退出/结束或撤权停止采集；显示真实状态，不由远程请求强制开启。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 状态提示方式与撤权响应待确认 |

**Traceability**

- Baseline: B §3，FR-SPORT-003、FR-SPORT-006、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 8.1.2 摄像头状态提示与关闭；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §8.1。
- PAGE: PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 隐私准入/采集状态；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


#### 二级功能 8.2：数据权限与提醒控制

##### Function 8.2.2：处理设备数据权限与删除请求

**用户场景**：在隐私控制与数据管理的处理设备数据权限与删除请求环节，家庭需要“可管理设备数据的使用和清理。”。

**需求描述**：设备应执行设备本地访问权限和规定的数据清理，反馈执行结果；不负责账号注销、云端全量删除或授权关系创建。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 可管理设备数据的使用和清理。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备隐私与权限；人员Owner TBD |
| 输入 | 有效家长权限、设备本地访问或规定清理请求 |
| 输出 | 本地执行结果回执 |
| 前置条件 | 权限有效且设备处置范围已明确；范围/离线响应TBD |
| 状态 | 权限/提醒约束；仅业务/展示语义，工程枚举TBD |
| 异常 | 权限不足不执行；删除及离线队列处置细则TBD |
| 关联页面 | 后台执行与回执；PAGE-08设备端入口TBD |
| 验收标准（评审检查点） | 仅执行设备本地权限和规定清理；不把本地删除当账号注销或云端全量删除。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 删除范围与离线响应待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-002、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 8.2.2 处理设备数据权限与删除请求；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §8.2。
- PAGE: 后台执行与回执；PAGE-08设备端入口TBD；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 权限/提醒约束；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。


##### Function 8.2.3：提醒时段与频率控制

**用户场景**：在隐私控制与数据管理的提醒时段与频率控制环节，家庭需要“减少重复催促和夜间打扰。”。

**需求描述**：设备应按已设定时段和频率限制输出提醒，抑制重复提示；提示内容由第5章提供。

| 字段 | 产品需求与边界 |
|---|---|
| 用户价值 | 减少重复催促和夜间打扰。 |
| Priority | P0（继承F；不调整） |
| Requirement Status | Pending Review（源状态：待评审） |
| Behavior Owner | 设备隐私与权限；人员Owner TBD |
| 输入 | 已设定提醒时段/频率与第5章提示内容 |
| 输出 | 受时段/频率约束的提醒 |
| 前置条件 | 存在有效提醒策略；设置责任端/参数TBD |
| 状态 | 权限/提醒约束；仅业务/展示语义，工程枚举TBD |
| 异常 | 重复/夜间打扰受策略抑制，不默认设备声音设置入口 |
| 关联页面 | PAGE-01/06/07等提示输出约束；PAGE-08设置入口TBD，不等于声音控制 |
| 验收标准（评审检查点） | 按已确认策略限制输出与抑制重复；未冻结时段和频率不填入数值。 正式测试方法/指标/用例TC-TBD。 |
| 原待确认项（保留） | 设置责任端、时段与频率待确认 |

**Traceability**

- Baseline: B §3，FR-DEVICE-002、FR-DEVICE-003；属需求意图/约束关联，正式FR逐项映射待评审。
- Function: 8.2.3 提醒时段与频率控制；Source: [Function Specification v0.5.2](Teamo_Device_Function_Specification_v0.5.2.md) §8.2。
- PAGE: PAGE-01/06/07等提示输出约束；PAGE-08设置入口TBD，不等于声音控制；Source: [UE IA v0.3.1](Teamo_Device_UE_IA_v0.3.1.md) §6。
- State: 权限/提醒约束；Source: U §6、[UE Engineering Reference v0.1.0](Teamo_Device_UE_Engineering_Reference_v0.1.0.md) A/B。
- Test Case: TC-TBD；没有新增测试编号或通过证据。

### 5.9 历史候选：不纳入默认MVP交付

以下20项沿用F已有编号和描述，均Candidate / Pending Review / 优先级TBD。输入、输出、守卫、异常及验收细则未冻结；表中的行为只在候选获准时成立。PAGE只记录F §14.2的候选关系，不代表U已批准独立功能或入口。不得为候选补造State/API/Test Case。Source: F §1–8/14.2；U §5/6；E D/E。

| Function ID | 功能 | 候选行为（保留） | 用户价值 | Behavior Owner | 待确认内容 | PAGE / State |
|---|---|---|---|---|---|---|
| 1.2.6 | 查看设备基本信息 | 提供设备名称和设备标识（如SN），便于家长辨识设备。 | 便于绑定及支持定位。 | 设备运行管理；人员TBD | 名称/SN展示必要性与来源待确认 | PAGE-08；State TBD；Candidate |
| 1.2.7 | 恢复设备出厂状态 | 经有效家长授权执行已确认的本地重置，说明清理范围并反馈结果；不等同账号注销或云端解绑。 | 支持重新配置设备。 | 设备运行管理；人员TBD | 清理范围、授权及绑定关系处理待确认 | PAGE-08/PAGE-00；State TBD；Candidate |
| 1.2.8 | 检查设备软件更新 | 若OTA能力获准，查询并反馈可用更新状态；不自动承诺下载安装。 | 了解软件维护状态。 | 设备运行管理；人员TBD | 是否纳入、提供端与OTA优先级待确认 | PAGE-08；State TBD；Candidate |
| 2.1.3 | 展示今日运动与任务摘要 | 显示当前儿童今日任务数量和已确认运动完成摘要。 | 快速理解今天还需要做什么。 | 设备交互；人员TBD | 日期、次数、跨端聚合口径及信息来源待确认 | PAGE-01；State TBD；Candidate |
| 2.2.3 | 调整设备提示音量 | 在授权范围内调整设备声音音量，并反馈生效状态。 | 适应家庭环境，减少打扰。 | 设备交互；人员TBD | 操作端、范围和必要提示规则待确认 | PAGE-08；State TBD；Candidate |
| 2.2.4 | 设置运动提示音开关 | 按允许策略开启或关闭提示音，反馈当前设置。 | 控制声音打扰。 | 设备交互；人员TBD | 安全必要提示能否关闭、授权与操作端待确认 | PAGE-08；State TBD；Candidate |
| 3.1.5 | 查看今日家长任务列表 | 汇总当前儿童可查看的家长任务，显示动作、目标与执行状态。 | 找到要完成的任务。 | 设备任务管理；人员TBD | 今日口径、任务顺序及离线列表范围待确认 | PAGE-03；State TBD；Candidate |
| 3.1.6 | 查看家长任务详情 | 提供单项任务的动作、目标、来源和执行条件；创建时间/名称是否显示待确认。 | 理解家长任务要求。 | 设备任务管理；人员TBD | 已有3.1.3呈现的细化提议，列表/详情是否分开待确认 | PAGE-03；State TBD；Candidate |
| 4.3.1 | 启动与退出独立动作辅助检测 | 若独立工具获准，经明确授权开始检测、提供已验证站位提示，退出停止采集；不生成运动计数或健康评分。 | 可单独理解站位与动作准备。 | 设备识别能力；人员TBD | 区别于3.2.2运动准备；独立场景、提示范围待确认 | PAGE-09；State TBD；Candidate |
| 4.3.2 | 显示姿态关键点辅助信息 | 若显示方案获准，呈现用于理解站位或动作的必要关键点信息。 | 帮助理解动作姿态。 | 设备识别呈现；人员TBD | 屏幕可理解性、是否必要及隐私边界待确认 | PAGE-09；State TBD；Candidate |
| 7.1.3 | 更换设备连接网络 | 提供经允许的网络重新配置流程，反馈连接或失败状态。 | 搬动或网络变化后可继续使用。 | 设备联网管理；人员TBD | 沿用7.1.1能力，家长端/设备端操作归属待确认 | PAGE-08/PAGE-00；State TBD；Candidate |
| 7.1.4 | 检查设备联网情况 | 在已有连接能力范围内报告是否联网及可处理失败原因。 | 理解联网问题。 | 设备联网管理；人员TBD | 7.1.1/7.1.2细化；不默认新增网络诊断工具 | PAGE-08；State TBD；Candidate |
| 7.2.4 | 引导首次设备绑定 | 未绑定时引导家长完成联网、家庭关联和当前儿童确认，再反馈有效绑定状态。 | 第一次使用能完成必要配置。 | 设备使用者管理；人员TBD | 绑定方案和联网先后依赖待确认 | PAGE-00；State TBD；Candidate |
| 7.2.5 | 展示设备绑定二维码 | 仅在二维码方案获准时展示有效绑定凭据；凭据由哪端签发待确认。 | 家长可扫码关联设备。 | 设备使用者管理；人员TBD | 新提议，不默认设备生成唯一凭据 | PAGE-00；State TBD；Candidate |
| 7.2.6 | 更新失效绑定二维码 | 若二维码方案获准，在凭据过期或失效后取得有效凭据，反馈可重试状态。 | 绑定失败后有恢复路径。 | 设备使用者管理；人员TBD | 若为唯一绑定路径，优先级与核心绑定共同评审，不默认P1 | PAGE-00；State TBD；Candidate |
| 7.2.7 | 提供设备绑定帮助 | 说明家长如何完成当前采用的绑定步骤及失败恢复。 | 减少首次配置困难。 | 设备使用者管理；人员TBD | 帮助范围与是否独立功能待确认 | PAGE-00；State TBD；Candidate |
| 7.2.8 | 切换当前使用儿童 | 执行经家长端/平台确认的儿童切换并反馈身份，不修改账号关系。 | 记录归属正确儿童。 | 设备使用者管理；人员TBD | 授权、切换端及运动中是否允许待确认 | PAGE-08；State TBD；Candidate |
| 7.2.9 | 执行设备解绑请求 | 处理有效解绑指令，更新设备本地绑定状态；数据清理由8.2.2按规则协调。 | 家庭可转移或停止使用设备。 | 设备使用者管理；人员TBD | 平台授权、离线响应和本地数据处置待确认 | PAGE-08；State TBD；Candidate |
| 8.1.3 | 设置本地摄像头使用状态 | 在有效授权范围内请求开启或关闭采集允许状态，真实结果仍以8.1.1守卫与硬件状态为准。 | 设备使用者可明确控制采集。 | 设备隐私控制；人员TBD | 输入方式、家长权限与硬件关闭优先级待确认 | PAGE-08；State TBD；Candidate |
| 8.2.4 | 查看设备数据使用说明 | 说明设备采集用途、结构化记录及原始视频不保存边界。 | 家庭理解隐私和数据用途。 | 设备权限管理；人员TBD | 呈现位置、内容及是否独立条目待确认 | PAGE-08；State TBD；Candidate |

每项候选的Traceability为本行Function（F §14.2）、本行候选PAGE关系（F/U）、State TBD（E），Test Case TC-TBD。候选无独立已批准验收承诺；输入/输出/前置/异常全部待其范围获准后在FR细化，不以需求卡模板填满而创造实现要求。

### 5.10 停用编号与原P1/未决范围

| 原编号 | 去向 | 本稿处理 |
|---|---|---|
| 7.2.2 运动结果通信（历史） | 合并至6.3.1 | 保留追溯，不重复实现/计数 |
| 8.2.1 儿童视频不保存（历史） | 移为F §8.3全局约束 | 原约束仍适用于全部功能和PAGE |

Source: F §7.2/8.2/14；U §6历史追踪。原P1四类与学校/体态/OTA/诊断的原追踪按§1.3保持，不新增编号。B FR-POSTURE-001是已有更广场景，当前F的独立辅助候选不与其自动合并；非运动体态范围仍按OQ-06/16、UE-OQ-08评审。


## 5. 状态、异常与问题映射

## 6. 状态模型

### 6.1 会话、保存与同步状态

Source: E A §5.1；U §4.2；F §11.3。全部Pending Review；下表保留原详细进入、行为、退出及PAGE关系，不定义客户端实现枚举。

| 状态 | 进入条件 | 可执行行为 | 退出条件 / 去向 | 关联PAGE |
|---|---|---|---|---|
| INIT | 已进入自主选择或任务确认上下文；不等于设备开机 | 确认儿童、来源、支持动作与目标；返回 | 上下文有效进入准备；取消退出，记录创建时机TBD | PAGE-02/03，儿童确认PAGE-00/08 |
| READY | 有效动作、目标和归属进入准备阶段 | 看说明、隐私检查、必要时调整站位、明确开始或取消 | 条件满足且明确开始→COUNTDOWN；不足停留；恢复路线TBD | PAGE-04 |
| COUNTDOWN | 开始意愿明确且准备满足 | 等待、取消；禁止计数 | 完成后复核通过→RUNNING；取消/离画→READY；隐私失效阻断 | PAGE-05 |
| RUNNING | 初次开始或恢复获准，隐私及准备有效 | 可信计数与反馈、暂停、提前结束 | 暂停/判定异常→PAUSED；达标或明确结束→FINISHED | PAGE-06 |
| PAUSED | 主动暂停或离画/识别异常已判定需暂停 | 保留次数，说明原因，继续或结束；不累计 | 继续→READY重新检查；结束→FINISHED；超时TBD | PAGE-06→04 |
| FINISHED | 达标、主动结束或已确认中断规则生效 | 停止采集/计数，生成真实结果并交给保存 | 执行事实保持结束；保存成功增加SAVED事实，失败走异常分支 | PAGE-06→07保存衔接 |
| SAVED | 6.2.1确认本地结果保存成功 | 看真实结果、返回首页；允许时后台上传 | 已保存事实保持；同步进SYNCING，或离线待同步 | PAGE-07；PAGE-01提示承载 |
| SYNCING | 已保存且正在上传/补传，尚未获平台业务接收确认 | 查看状态；按契约重试，沿用原记录标识 | 业务确认→SYNCED；失败→待补传；重试参数TBD | PAGE-07/01；后台状态 |
| SYNCED | 平台确认接收同一结果记录 | 查看已同步状态，不重复生成结果或奖励 | 终态事实保持；冲突处理契约TBD | PAGE-07/01；后台状态 |

INIT为任务/自主上下文确认，不能用于设备开机；READY包含准备检查，不等于已满足开始。准备/倒计时/暂停不累计成绩。PAUSED恢复重新检查隐私和准备、明确恢复并重置半周期；是否再次COUNTDOWN TBD。

### 6.2 三个独立维度

| 维度 | 事实 | 不得混同 |
|---|---|---|
| 执行 | RUNNING/PAUSED/FINISHED等真实运动过程 | FINISHED不代表已保存 |
| 保存 | 待保存/保存中/失败/SAVED | SAVED不代表平台已收到；未保存不作为已保存记录上传 |
| 同步 | 待同步/SYNCING/失败待补传/SYNCED | 只有平台业务接收确认才SYNCED，发送完成不能代替 |

可同时表达“提前结束 / 已保存 / 待同步”；返回首页不改变成绩、归属或同步事实，不要求等待上传后才能进行允许的本地运动。Source: E A §5.3；F §6/11；U §4.2/5。

### 6.3 绑定、网络与隐私

绑定展示为未绑定→等待绑定→处理中→成功→当前儿童确认→正常使用，解绑/失败是有依据的分支。断网不解除有效绑定；扫码和请求发送不等于成功；儿童归属未知不能分配成绩。网络、隐私、绑定与运动状态分别维护，不强套运动标签。具体绑定方式、超时、撤权响应、实际状态枚举TBD。（Source: E A §5.2；U §4.2；F §7/8）

## 8. 异常流程

每个异常先确认原因与影响，再表达可行去向；原因未知如实说明。所有处理仍Pending Review，工程细则TBD / FR阶段定义。Source: E B（详细业务依据）及U §4.3；对应原Function与PAGE见表。State是发生阶段/业务去向，不新增状态枚举。

| 异常 / 原因 | 发生阶段 | 用户影响 | 页面 / 功能依据 | 用户反馈 | 处理与恢复路径 |
|---|---|---|---|---|---|
| 初始化或必要运行服务不可用 | 启动/运行 | 无法进入可用状态 | PAGE-00/01；1.1、1.2.2 | 说明当前启动/服务不可用，具体原因可确认才显示 | 约定重试/返回/必要重启→重新初始化；故障范围/时限TBD |
| 网络断开 | 首页/任务/结果 | 新任务获取或结果同步受影响 | PAGE-01/03/07/08；7.1、6.3 | 说明离线与记录真实同步状态 | 保留有效绑定；继续允许的缓存/本地能力；连接恢复按契约补传 |
| 绑定请求失败或关系不可确认 | 首次使用/启动 | 无法完成有效绑定准入 | PAGE-00；7.2.3 | 区分未绑定、处理中失败、关系失效；不称成功 | 回等待/引导或既有有效关系状态；恢复契约TBD，不静默解绑 |
| 当前儿童归属不明确 | 任务/自主确认 | 不能正确关联成绩 | PAGE-00/08，承载TBD；7.2.3、6.1.1 | 说明儿童未确认，需完成归属确认 | 按有效上下文确认后回原任务/自主准备；不默认人脸识别 |
| 动作/目标/任务有效条件不满足 | 选择/任务详情 | 无法开始该运动 | PAGE-02/03；3.1.1、3.1.3、3.1.4 | 给出已验证的不支持动作、目标无效或任务无效原因 | 自主重新选择允许目标，任务返回列表；撤销/过期细则TBD，不静默改家长目标 |
| 隐私关闭、未授权、撤权或状态未知 | 准备/倒计时/运动 | 无法采集或继续识别 | PAGE-04/05/06/08；8.1 | 真实说明采集已阻断/停止及对应隐私原因 | 停止采集和新增成绩；有效授权及本地条件恢复后重新准备并确认，响应时限TBD |
| 无人、身体不完整或画面不可用 | 准备/倒计时 | 未满足开始条件 | PAGE-04/05；4.1.1、3.2.2 | 给一个主要站位/入镜原因 | 调整后重新检查；倒计时离画回PAGE-04，不提前计数 |
| 离画、遮挡或识别不可用需暂停 | 运动中 | 暂停新增成绩 | PAGE-06；4.1.3、3.3.1、5.1.2 | 说明已判定原因及成绩保留 | 暂停→调整→选择继续→PAGE-04重新准入；可按原规则结束 |
| 单个动作事件不完整/不确定 | 运动中 | 该事件不计 | PAGE-06；4.1.2、5.1.2 | 必要时说明当前无法确认，不作确定纠错 | 不计该事件，不必一律暂停；若判定识别异常，按暂停分支处理；阈值TBD |
| 本地保存失败 | 结束保存 | 结果尚未可靠记录 | PAGE-07；6.2.3、5.2.2 | 说明尚未保存，不能称已记录 | 保留可恢复结果供重试；成功后展示已保存，失败恢复保证/退出规则TBD |
| 上传失败或缺少业务接收确认 | 同步 | 家长端尚未确认收到 | PAGE-07/01；6.3、5.2.2 | 保持已保存，说明待同步/失败待补传 | 按契约重试，沿用原记录标识；平台去重，不阻断允许本地运动 |
| 重启/断电后恢复范围不足 | 日常启动 | 本次进度或记录可能不完整 | PAGE-01/06/07，承载TBD；1.1.2、6.2.2 | 仅说明可恢复真实成绩和不能确认部分 | 恢复已保存事实，不自动续计或伪造完成；不可恢复处理TBD |
| 家长权限不满足/不可确认 | 受限设备管理 | 不能执行该管理操作 | PAGE-08；7.2.3、8.2.2 | 说明需有效家长权限，未执行 | 保持原有效状态，按责任端重新完成权限确认；入口及方式TBD |
| 候选绑定二维码凭据失效 | 仅二维码获准后 | 无法继续该绑定路径 | PAGE-00；候选能力 / Pending Review / 优先级TBD | 区分凭据过期与已有关系失败 | 按获准方案重取或替代路径；当前不承诺此技术方案 |

无人/遮挡在准备中意味着未满足开始条件；在运动中只有被判定需暂停才进入PAUSED。单次动作不完整/不确定仅不计该事件，不能自动等同所有识别失败。保存失败不伪称已记录，同步失败不改变达标事实；不解绑、不清零、不重建结果。（Source: F 3.3/4.1/6；U §4.3；E B）


### 原OQ与UE-OQ完整关联

### 13.2 与UE评审问题的关联

|UE问题|功能大纲关联|需形成的结论|
|---|---|---|
|UE-OQ-01 绑定链路|7.1、7.2.3–7.2.7|先后依赖、成功确认、异常恢复；二维码仍候选|
|UE-OQ-02 页面/输入承载|OQ-02、2.2.2、3.1.3/3.1.5/3.1.6|逻辑PAGE到实际承载，列表/详情是否拆分；不决定硬件|
|UE-OQ-03 动作/目标|OQ-01/03、3.1.4、4.2|三/七动作、目标范围与计数单位|
|UE-OQ-04 任务/儿童|OQ-04/09、3.1、7.2.3/7.2.8/7.2.9|有效性、重复投递、切换与记录归属|
|UE-OQ-05 开始/恢复|OQ-07、3.2/3.3、4.1.1|准备、跳过、超时和再倒计时|
|UE-OQ-06 保存/同步|OQ-08/09、5.2、6章|用时、失败/断电恢复、业务确认与防重复|
|UE-OQ-07 角色/鼓励|OQ-05、2.1.2、5.1.3|最小深度，原P0不变，不扩成长体系|
|UE-OQ-08 独立辅助|OQ-06、4.3.1/4.3.2候选|明确用户任务与必要性，授权/退出；当前不开放入口|
|UE-OQ-09 候选设置|1.2.6–1.2.8、2.1.3、2.2.3/2.2.4、7.1.3/7.1.4、7.2.5–7.2.7、8.2.4等|逐项必要性/责任/去向，不批量批准|
|UE-OQ-10 跨端管理|OQ-11、7章/8章/12章|发起、权限、设备回执、离线与本地/云端边界|
|UE-OQ-11 责任/引用|OQ-12、全部功能及14章|Owner、Reviewer、引用版本及批准/延期记录|

完整问题可在UE IA第8章展开，背景与输入在工程附录E。建议参与方不等于已指派Owner；候选合并/纳入均须评审，TC-TBD不得当验收通过。



### 来源差异与工程未决

### 9.4 输入差异与评审处理

| 差异 | 固定输入证据 | 本稿保留状态 | 原问题入口 |
|---|---|---|---|
| 七动作与三动作 | B §2/FR-SPORT-001/005保留七动作；F §4.2列三动作提议，U §5未冻结关系 | 不扩动作号或删除上游追踪；演示/产品范围TBD | OQ-01/03、UE-OQ-03 |
| 倒计时数值 | B FR-SPORT-004写3/2/1；U §4.2写时长TBD，E恢复是否再倒计时TBD | 不把三秒写成冻结验收值；时间与恢复路径TBD | OQ-07、UE-OQ-05 |
| API字段与部署 | B §3列字段/版本线索；F §0.5与E不定义API结构、枚举或算法实现 | 作为业务信息，不生成已批准字段规范、部署方案或数值 | OQ-09/10/12、UE-OQ-06/11 |
| 维护/体态较广表述 | B FR-DEVICE-003/FR-POSTURE-001含广范围；F §9/10、U §5保持OTA/体态等未决 | 原追踪保留，本稿不纳入默认MVP，也不删除 | OQ-06/15/16、UE-OQ-08/09 |
| 交付细化顺序 | F §0.5写UE→UI Flow→FR；§13.1另有FR/TR表述 | 按用户本次要求展示PRD→FR→UI Flow→Test Case，交付物互相校验，次序不构成范围批准 | OQ-12、UE-OQ-11 |

没有新增OQ编号；差异复用现有未决项。待评审决定必须按“旧口径—新证据—建议修改”记录；未提供新证据时不能修改既有产品/功能口径。上述表是差异登记，不是已批准决策。



## Feature Specification v0.6 — 完整源条目

| 编号 | 功能点 | 功能描述 | 用户价值 | 优先级 | 状态 | 行为归属 | 待确认 |
|---|---|---|---|---|---|---|---|
| 1.1.1 | 开机与初始化 | 启动软件并验证必要运行条件，进入可用或明确异常状态。 | 让家庭知道设备能否开始使用。 | P0 | 待评审 | 设备启动与运行 | 启动时长待确认 |
| 1.1.2 | 恢复启动状态 | 根据6.2.2恢复的任务、结果和隐私状态，输出待机、恢复提示或异常；不重复负责读取记录。 | 重启后回到正确状态，不自动续计或伪称完成。 | P0 | 待评审 | 设备启动与运行 | 恢复进入哪个状态待确认 |
| 1.2.1 | 设备运行状态管理 | 统一维护当前运行状态和允许的操作；运动过程的暂停、恢复与结束由第3章定义。 | 状态一致，避免同一操作在不同入口产生冲突。 | P0 | 待评审 | 设备启动与运行 | — |
| 1.2.2 | 设备故障处理 | 处理启动失败、运行服务不可用等设备级故障，给出重试、返回或重启入口；识别异常由4.1.3判断。 | 故障时能够理解原因并恢复使用。 | P0 | 待评审 | 设备启动与运行 | 故障范围与恢复时限待确认 |
| 1.2.3 | 查看设备软件版本 | 提供当前软件版本，供家长或维护人员核对；属于维护支撑，不扩展OTA或远程运维。 | 便于核对设备版本和定位兼容问题。 | P0 | 待评审 | 设备启动与运行 | — |
| 1.2.4 | 故障信息记录 | 记录必要的故障原因和发生时间，供诊断使用。 | 故障可定位、可复盘。 | P0 | 待评审 | 设备启动与运行 | 日志内容与保存周期待确认 |
| 1.2.5 | 设备重启 | 提供必要重启操作，重启后按1.1.2恢复状态。 | 无法正常使用时有恢复入口。 | P0 | 待评审 | 设备启动与运行 | 重启触发方式待确认 |
| 1.2.6 | 查看设备基本信息 | 提供设备名称和设备标识（如SN），便于家长辨识设备。 | 便于绑定及支持定位。 | 待确认 | 待评审 | 设备运行管理 | 名称/SN展示必要性与来源待确认 |
| 1.2.7 | 恢复设备出厂状态 | 经有效家长授权执行已确认的本地重置，说明清理范围并反馈结果；不等同账号注销或云端解绑。 | 支持重新配置设备。 | 待确认 | 待评审 | 设备运行管理 | 清理范围、授权及绑定关系处理待确认 |
| 1.2.8 | 检查设备软件更新 | 若OTA能力获准，查询并反馈可用更新状态；不自动承诺下载安装。 | 了解软件维护状态。 | 待确认 | 待评审 | 设备运行管理 | 是否纳入、提供端与OTA优先级待确认 |
| 2.1.1 | 运动入口 | 提供任务与自主运动入口，显示必要可用状态。 | 减少寻找入口和开练阻力。 | P0 | 待评审 | 设备交互 | — |
| 2.1.2 | 显示角色状态表情 | 按已有运动状态显示固定表情，输出一致的角色回应；鼓励及提示内容由第5章决定。 | 运动中获得一致且适度的角色回应。 | P0 | 待评审 | 设备交互 | 表情事件与资源待确认 |
| 2.1.3 | 展示今日运动与任务摘要 | 显示当前儿童今日任务数量和已确认运动完成摘要。 | 快速理解今天还需要做什么。 | 待确认 | 待评审 | 设备交互 | 日期、次数、跨端聚合口径及信息来源待确认 |
| 2.2.1 | 设备状态提示 | 呈现设备不可用、操作不可执行等通用状态；任务内容、实时成绩和结束结果分别由第3章和第5章定义。 | 知道设备当前是否可用，以及怎样处理问题。 | P0 | 待评审 | 设备交互 | 表达方式待确认 |
| 2.2.2 | 操作接收与确认 | 接收选择、开始、取消、暂停、继续、结束及返回操作，并告知是否接受；各操作业务结果由所属功能负责。 | 清楚操作是否生效。 | P0 | 待评审 | 设备交互 | 触控、按键或其他输入方式待确认 |
| 2.2.3 | 调整设备提示音量 | 在授权范围内调整设备声音音量，并反馈生效状态。 | 适应家庭环境，减少打扰。 | 待确认 | 待评审 | 设备交互 | 操作端、范围和必要提示规则待确认 |
| 2.2.4 | 设置运动提示音开关 | 按允许策略开启或关闭提示音，反馈当前设置。 | 控制声音打扰。 | 待确认 | 待评审 | 设备交互 | 安全必要提示能否关闭、授权与操作端待确认 |
| 3.1.1 | 接收并检查运动任务 | 检查送达任务的儿童归属、支持动作、目标和有效条件，输出接受资格或拒绝原因；最终接收回执由3.1.2负责。 | 收到可执行而非无效任务。 | P0 | 待评审 | 设备任务与执行 | 任务检查规则待确认 |
| 3.1.2 | 反馈任务接收结果 | 检查通过并由6.2.1保存后确认接收；失败说明原因；重复任务返回同一接收结果。 | 家长知道任务是否真实送达。 | P0 | 待评审 | 设备任务与执行 | — |
| 3.1.3 | 展示任务内容与执行状态 | 提供动作、目标与来源，呈现设备执行状态；平台任务撤销等有效规则另行确认，不由设备自建发布规则。 | 儿童明白为什么做、做多少。 | P0 | 待评审 | 设备任务与执行 | 任务状态及撤销规则待确认 |
| 3.1.4 | 动作与目标确认 | 执行任务时确认已下发动作和目标；自主运动时选择支持动作及允许目标，不擅自修改家长任务。 | 运动目标清楚，自主运动与家长任务不混淆。 | P0 | 待评审 | 设备任务与执行 | 自主目标范围待确认 |
| 3.1.5 | 查看今日家长任务列表 | 汇总当前儿童可查看的家长任务，显示动作、目标与执行状态。 | 找到要完成的任务。 | 待确认 | 待评审 | 设备任务管理 | 今日口径、任务顺序及离线列表范围待确认 |
| 3.1.6 | 查看家长任务详情 | 提供单项任务的动作、目标、来源和执行条件；创建时间/名称是否显示待确认。 | 理解家长任务要求。 | 待确认 | 待评审 | 设备任务管理 | 已有3.1.3呈现的细化提议，列表/详情是否分开待确认 |
| 3.2.1 | 动作说明 | 开始前提供经审核、儿童可理解的动作与安全说明。 | 减少不理解动作造成的失败。 | P0 | 待评审 | 设备任务与执行 | 媒体形态/可跳过规则待确认 |
| 3.2.2 | 入镜准备引导 | 根据第4章识别结果提示调整站位；准备不足时不开始运动。 | 知道如何站好，准备完成后再开练。 | P0 | 待评审 | 设备任务与执行 | 准备完成条件待确认 |
| 3.2.3 | 开始确认与倒计时 | 儿童明确开始且准备满足后倒计时，结束再检查开始条件。 | 有时间准备，避免突然计数。 | P0 | 待评审 | 设备任务与执行 | 输入方式待确认 |
| 3.3.1 | 暂停与成绩保留 | 主动暂停或离画/识别异常时停止新增成绩，保留已确认次数。 | 已完成努力不因中断消失。 | P0 | 待评审 | 设备任务与执行 | — |
| 3.3.2 | 恢复运动 | 重新检查隐私和准备，明确恢复后从已确认成绩继续。 | 安全且连贯地继续运动。 | P0 | 待评审 | 设备任务与执行 | 恢复时重新判断动作起点；恢复确认方式待确认 |
| 3.3.3 | 达标与提前结束 | 达标停止确认动作；主动结束保留实际与真实未完成状态。 | 不强迫继续，不伪造达标。 | P0 | 待评审 | 设备任务与执行 | 自动超时结束规则待确认 |
| 4.1.1 | 人体与画面可用性检测 | 判断是否有人、身体是否完整及画面是否满足识别条件，输出准备状态和原因；引导由3.2.2负责。 | 避免在看不清动作时开始计数。 | P0 | 待评审 | 设备识别能力 | 多人处理及适用距离待确认 |
| 4.1.2 | 有效动作计数 | 依据审核规则仅累计完整有效周期，未完成、重复或不确定事件不计。 | 孩子和家长得到可信成绩。 | P0 | 待评审 | 设备识别能力 | 阈值待确认 |
| 4.1.3 | 判定运动识别异常 | 根据4.1.1画面状态和4.2动作判定输出无人、遮挡、识别不确定或不可用原因；暂停由3.3.1处理，提示由5.1.2呈现。 | 知道如何调整，而非被错误指责。 | P0 | 待评审 | 设备识别能力 | — |
| 4.2.1 | 开合跳动作判定 | 判断并拢、打开、回收是否形成完整有效周期，供4.1.2累计次数。 | 完整开合跳被可信记录。 | P0 | 待评审 | 设备识别能力 | 有效幅度与规则待确认 |
| 4.2.2 | 深蹲起动作判定 | 判断站立、有效下蹲、回站立是否形成完整周期，供4.1.2累计次数。 | 完整深蹲被可信记录。 | P0 | 待评审 | 设备识别能力 | 安全与有效幅度规则待确认 |
| 4.2.3 | 高抬腿动作判定 | 判断有效抬腿与落下事件，按统一左右侧规则供4.1.2累计次数。 | 目标与实际成绩使用一致口径。 | P0 | 待评审 | 设备识别能力 | 单侧一次或双侧一轮待确认 |
| 4.3.1 | 启动与退出独立动作辅助检测 | 若独立工具获准，经明确授权开始检测、提供已验证站位提示，退出停止采集；不生成运动计数或健康评分。 | 可单独理解站位与动作准备。 | 待确认 | 待评审 | 设备识别能力 | 区别于3.2.2运动准备；独立场景、提示范围待确认 |
| 4.3.2 | 显示姿态关键点辅助信息 | 若显示方案获准，呈现用于理解站位或动作的必要关键点信息。 | 帮助理解动作姿态。 | 待确认 | 待评审 | 设备识别呈现 | 屏幕可理解性、是否必要及隐私边界待确认 |
| 5.1.1 | 次数与进度反馈 | 呈现设备已确认次数与目标进度，必要短语音与数字保持一致。 | 看见实际努力和距目标的差距。 | P0 | 待评审 | 设备反馈呈现 | 频率待确认 |
| 5.1.2 | 动作反馈与调整提示 | 有效动作给正向回应；无效或识别不确定给一个可处理原因。 | 得到可理解指导且减少挫败。 | P0 | 待评审 | 设备反馈呈现 | — |
| 5.1.3 | 完成鼓励 | 真实结束后提供适度鼓励，区分达标和提前结束。 | 获得尊重真实努力的反馈。 | P0 | 待评审 | 设备反馈呈现 | 运动星/PB深度待确认 |
| 5.2.1 | 运动结果查看 | 在设备端显示动作、目标、实际次数、用时和达标或提前结束状态；家长端展示不属于此项。 | 儿童结束后能理解本次努力。 | P0 | 待评审 | 设备反馈呈现 | 用时是否含暂停待确认 |
| 5.2.2 | 保存与同步提示 | 分别说明本地已保存、等待同步、同步成功或失败。 | 不把运动结束误解为已回传。 | P0 | 待评审 | 设备反馈呈现 | — |
| 6.1.1 | 记录创建与归属 | 建立唯一运动记录并关联儿童、任务或自主来源及动作目标。 | 每次运动可以追溯到正确儿童。 | P0 | 待评审 | 设备记录与同步 | 开始记录时机待确认 |
| 6.1.2 | 生成运动结果记录 | 汇总已确认次数、目标、用时与结束原因，输出唯一记录内容；本地写入归6.2.1。 | 可信查看真实完成情况。 | P0 | 待评审 | 设备记录与同步 | — |
| 6.2.1 | 本地保存 | 保存已缓存任务、实际结果和必要待同步信息。 | 离线可使用、不丢记录。 | P0 | 待评审 | 设备记录与同步 | 存储容量/保留周期待确认 |
| 6.2.2 | 已保存记录恢复 | 读取可恢复的任务、运动记录及待同步信息，保持真实已确认成绩，向1.1.2提供恢复结果。 | 重启后不产生重复或虚假的运动记录。 | P0 | 待评审 | 设备记录与同步 | 保存频率及断电可恢复范围待确认 |
| 6.2.3 | 保存失败处理 | 明确未保存并保留可恢复结果供重试。 | 不误导家长或静默丢失。 | P0 | 待评审 | 设备记录与同步 | 失败恢复保证待确认 |
| 6.3.1 | 上传结果并更新同步状态 | 发送已保存结果，依据平台业务接收确认更新同步状态；不把网络发送完成视为成功接收。 | 家长查看同一真实记录。 | P0 | 待评审 | 设备记录与同步 | 协议待确认 |
| 6.3.2 | 补传失败结果并防重复 | 设备沿用原记录标识补传；平台按同一标识去重。设备不重复生成结果或发放已批准奖励。 | 没有重复记录或虚假成长。 | P0 | 待评审 | 设备记录与同步 | 重试/冲突策略待确认 |
| 7.1.1 | 网络连接管理 | 提供必要联网配置及连接状态，失败给出可操作原因。 | 可完成连接并理解故障。 | P0 | 待评审 | 设备联网与使用者管理 | 配网流程及责任端待确认 |
| 7.1.2 | 联网状态提示 | 显示在线、离线或恢复连接；离线继续运动由第3章支持，本地保存与补传由第6章负责。 | 理解联网状态与当前可用能力。 | P0 | 待评审 | 设备联网与使用者管理 | — |
| 7.1.3 | 更换设备连接网络 | 提供经允许的网络重新配置流程，反馈连接或失败状态。 | 搬动或网络变化后可继续使用。 | 待确认 | 待评审 | 设备联网管理 | 沿用7.1.1能力，家长端/设备端操作归属待确认 |
| 7.1.4 | 检查设备联网情况 | 在已有连接能力范围内报告是否联网及可处理失败原因。 | 理解联网问题。 | 待确认 | 待评审 | 设备联网管理 | 7.1.1/7.1.2细化；不默认新增网络诊断工具 |
| 7.2.1 | 设备状态同步 | 向平台同步必要的在线状态、运行状态及软件版本；任务接收确认由3.1.2负责，运动结果由6.3负责。 | 家长端了解设备可用状态。 | P0 | 待评审 | 设备联网与使用者管理 | 同步内容、时机与连接方式待确认 |
| 7.2.2 | 运动结果通信（历史） | 已合并到6.3.1，不重复实现。 | 保留追溯。 | 历史P0，不计有效范围 | 已停用（保留追溯） | 6.3结果同步 | v0.3已合并 |
| 7.2.3 | 绑定状态与当前儿童确认 | 呈现真实连接/绑定状态，执行平台认可的家庭绑定上下文并确认当前儿童，失败说明真实原因；供任务和运动记录关联使用，不在设备创建账号或默认人脸识别。 | 避免记录分配给错误儿童。 | P0 | 待评审 | 设备联网与使用者管理 | 绑定流程、多儿童切换待确认 |
| 7.2.4 | 引导首次设备绑定 | 未绑定时引导家长完成联网、家庭关联和当前儿童确认，再反馈有效绑定状态。 | 第一次使用能完成必要配置。 | 待确认 | 待评审 | 设备使用者管理 | 绑定方案和联网先后依赖待确认 |
| 7.2.5 | 展示设备绑定二维码 | 仅在二维码方案获准时展示有效绑定凭据；凭据由哪端签发待确认。 | 家长可扫码关联设备。 | 待确认 | 待评审 | 设备使用者管理 | 新提议，不默认设备生成唯一凭据 |
| 7.2.6 | 更新失效绑定二维码 | 若二维码方案获准，在凭据过期或失效后取得有效凭据，反馈可重试状态。 | 绑定失败后有恢复路径。 | 待确认 | 待评审 | 设备使用者管理 | 若为唯一绑定路径，优先级与核心绑定共同评审，不默认P1 |
| 7.2.7 | 提供设备绑定帮助 | 说明家长如何完成当前采用的绑定步骤及失败恢复。 | 减少首次配置困难。 | 待确认 | 待评审 | 设备使用者管理 | 帮助范围与是否独立功能待确认 |
| 7.2.8 | 切换当前使用儿童 | 执行经家长端/平台确认的儿童切换并反馈身份，不修改账号关系。 | 记录归属正确儿童。 | 待确认 | 待评审 | 设备使用者管理 | 授权、切换端及运动中是否允许待确认 |
| 7.2.9 | 执行设备解绑请求 | 处理有效解绑指令，更新设备本地绑定状态；数据清理由8.2.2按规则协调。 | 家庭可转移或停止使用设备。 | 待确认 | 待评审 | 设备使用者管理 | 平台授权、离线响应和本地数据处置待确认 |
| 8.1.1 | 检查授权并阻断不允许的采集 | 检查有效授权及本地隐私状态，输出允许或阻断；未授权、关闭或未知禁止采集，不负责家长账号授权流程。 | 家长边界可控且可解释。 | P0 | 待评审 | 设备隐私与权限 | — |
| 8.1.2 | 摄像头状态提示与关闭 | 显示真实采集状态；运动退出或授权撤销后停止采集，不能通过远程任务绕过本地关闭状态。 | 知道摄像头是否工作，并能停止采集。 | P0 | 待评审 | 设备隐私与权限 | 状态提示方式与撤权响应待确认 |
| 8.1.3 | 设置本地摄像头使用状态 | 在有效授权范围内请求开启或关闭采集允许状态，真实结果仍以8.1.1守卫与硬件状态为准。 | 设备使用者可明确控制采集。 | 待确认 | 待评审 | 设备隐私控制 | 输入方式、家长权限与硬件关闭优先级待确认 |
| 8.2.1 | 儿童视频不保存（历史） | 移为8.3全局约束。 | 保护隐私。 | 历史P0，不计有效范围 | 已停用（保留追溯） | 全局约束 | v0.3已移为约束 |
| 8.2.2 | 处理设备数据权限与删除请求 | 执行设备本地访问权限和规定的数据清理，反馈执行结果；不负责账号注销、云端全量删除或授权关系创建。 | 可管理设备数据的使用和清理。 | P0 | 待评审 | 设备隐私与权限 | 删除范围与离线响应待确认 |
| 8.2.3 | 提醒时段与频率控制 | 按已设定时段和频率限制输出提醒，抑制重复提示；提示内容由第5章提供。 | 减少重复催促和夜间打扰。 | P0 | 待评审 | 设备隐私与权限 | 设置责任端、时段与频率待确认 |
| 8.2.4 | 查看设备数据使用说明 | 说明设备采集用途、结构化记录及原始视频不保存边界。 | 家庭理解隐私和数据用途。 | 待确认 | 待评审 | 设备权限管理 | 呈现位置、内容及是否独立条目待确认 |

<a id="feature-state-reference"></a>

## Feature-State Mapping

### 11.3 UE业务状态引用

|UE标签|业务含义 / 关联|展示PAGE|约束|
|---|---|---|---|
|INIT|自主/任务上下文确认，3.1.4|PAGE-02/03；儿童确认PAGE-00/08|不等于设备开机；6.1.1创建时机TBD|
|READY|运动准备，3.2.1/3.2.2|PAGE-04|不是单凭标签允许开始，隐私/准备需满足|
|COUNTDOWN|明确开始时机，3.2.3|PAGE-05|不计数，结束复核条件|
|RUNNING|有效计数/反馈，第3–5章|PAGE-06|不确定事件不计，低置信度不确定纠错|
|PAUSED|暂停与成绩保留，3.3.1/3.3.2|PAGE-06；继续回PAGE-04|不新增/清零，恢复准入和再倒计时TBD|
|FINISHED|真实结束，3.3.3/6.1.2|PAGE-06/07|区分达标和提前结束，不代表保存|
|SAVED|本地已保存，6.2.1|PAGE-07/01|不代表已同步，保证/周期TBD|
|SYNCING|正在上传/补传，6.3|PAGE-07/01，后台|记录独立状态，不阻断允许本地运动|
|SYNCED|平台业务确认，6.3.1|PAGE-07/01，后台|发送成功不等于业务接收|

英文标签仅为UE沟通语义，不定义API字段、数据结构或客户端枚举。执行、保存、同步是不同维度；完成运动≠已保存，已保存≠已同步。绑定/网络/隐私各有独立状态，不强行套入运动标签。准备/倒计时/暂停不累计成绩，恢复重查隐私与准备；具体阈值、时长、重试、断电和撤权响应TBD。

详细状态与PAGE线框见UE工程附录A，异常业务依据见附录B；已有第11.2状态规则保留，工程细则TBD / FR阶段定义。


### 14.2 历史候选与UE页面关联

以下为v0.5已登记的20个候选/细化号，全部Candidate / Pending Review / 优先级TBD，不是本次新增、不是已批准独立功能，也不计入UE原47项核心映射。合并或停用须另评审，不擅自改号或状态。

|功能编号|页面编号|处理类型|既有功能关系/边界|UE问题|Test Case|
|---|---|---|---|---|---|
|1.2.6|PAGE-08|独立候选|1.2.3仅版本，不含名称/SN|UE-OQ-09|TC-TBD|
|1.2.7|PAGE-08/PAGE-00|独立候选|1.2.5仅重启；重置不等于解绑|UE-OQ-09/10|TC-TBD|
|1.2.8|PAGE-08|独立候选|9章OTA追踪，不承诺下载/安装|UE-OQ-09|TC-TBD|
|2.1.3|PAGE-01|独立呈现候选|3.1.3/5.2已有事实，聚合未确认|UE-OQ-09|TC-TBD|
|2.2.3|PAGE-08|独立设置候选|8.2.3提醒约束不等于音量控制|UE-OQ-09/10|TC-TBD|
|2.2.4|PAGE-08|独立设置候选|8.2.3不证明提示音开关获准|UE-OQ-09/10|TC-TBD|
|3.1.5|PAGE-03|已有呈现细化待审|3.1.3负责任务内容/状态；今日聚合候选|UE-OQ-02/04|TC-TBD|
|3.1.6|PAGE-03|已有呈现细化待审|3.1.3/3.1.4主功能；列表/详情拆分TBD|UE-OQ-02/04|TC-TBD|
|7.1.3|PAGE-08/PAGE-00|已有联网细化待审|7.1.1主功能；更换网络入口候选|UE-OQ-09/10|TC-TBD|
|7.1.4|PAGE-08|已有联网细化待审|7.1.1/7.1.2主功能；非独立诊断承诺|UE-OQ-09/10|TC-TBD|
|7.2.4|PAGE-00|已有绑定细化待审|7.2.3主功能；不另建账号体系|UE-OQ-01/10|TC-TBD|
|7.2.5|PAGE-00|二维码方案候选|7.2.3不指定二维码|UE-OQ-01|TC-TBD|
|7.2.6|PAGE-00|二维码条件候选|仅二维码获准后适用，与绑定一并评审|UE-OQ-01|TC-TBD|
|7.2.7|PAGE-00|绑定帮助候选|7.2.3主功能；是否独立条目TBD|UE-OQ-01/09|TC-TBD|
|7.2.8|PAGE-08|已有儿童确认细化待审|7.2.3主功能；切换端/条件TBD|UE-OQ-04/10|TC-TBD|
|7.2.9|PAGE-08|既有关系处置细化待审|7.2.3/8.2.2主责任；不承诺本机入口|UE-OQ-04/10|TC-TBD|
|8.1.3|PAGE-08|既有隐私控制细化待审|8.1.1/8.1.2已有阻断/关闭；开关形式候选|UE-OQ-10|TC-TBD|
|8.2.4|PAGE-08|历史说明候选|UE3.1未将说明独立纳入；继续追踪|UE-OQ-09/10|TC-TBD|
|4.3.1|PAGE-09|独立辅助候选|4.1.1/3.2.2仅复用依据，不代表独立批准|UE-OQ-08|TC-TBD|
|4.3.2|PAGE-09|关键点显示候选|运动准备与独立显示均不默认支持|UE-OQ-08/09|TC-TBD|


### 14.3 变更管理结果

原47项P0保留，新增20项待评审候选，共67项在评审清单中；2项历史停用另列。新增不是已批准交付范围，独立姿态与更新查询不能据清单推断已支持。变更批准人、日期及优先级均待确认。原v0.4、UE v0.1及更早版本保持原样。

部分条目属于已有功能的显性细化，而非新能力；评审若决定合并，保留新号并标记停用去向，不重用编号。本文不定义UI位置、协议、算法或新增云端系统。


---


### 14.4 核心需求—功能—PAGE—状态—测试追踪

本表同步UE IA v0.3.1第6章，以v0.4原47项P0为核心基线，与本大纲原47项编号、行为、优先级一致。Requirement为已有需求意图，不是新Requirement ID；PAGE包括展示/触发和后台支撑，不将后台功能变成页面；State不是实现枚举；用例未建立/确认均TC-TBD。

|Requirement|Function|PAGE / 关系|State|Test Case|
|---|---|---|---|---|
|让家庭知道设备能否开始使用。|1.1.1 开机与初始化|PAGE-00/01启动路由支撑，无新增启动PAGE|启动/恢复（非INIT）|TC-TBD|
|重启后回到正确状态，不自动续计或伪称完成。|1.1.2 恢复启动状态|PAGE-00/01启动路由支撑，无新增启动PAGE|启动/恢复（非INIT）|TC-TBD|
|状态一致，避免同一操作在不同入口产生冲突。|1.2.1 设备运行状态管理|PAGE-00–08状态与异常支撑|设备/故障展示|TC-TBD|
|故障时能够理解原因并恢复使用。|1.2.2 设备故障处理|PAGE-00–08状态与异常支撑|设备/故障展示|TC-TBD|
|便于核对设备版本和定位兼容问题。|1.2.3 查看设备软件版本|PAGE-08设备状态|设备/故障展示|TC-TBD|
|故障可定位、可复盘。|1.2.4 故障信息记录|后台记录支撑，无独立页面承诺|设备/故障展示|TC-TBD|
|无法正常使用时有恢复入口。|1.2.5 设备重启|PAGE-08系统设置|设备/故障展示|TC-TBD|
|减少寻找入口和开练阻力。|2.1.1 运动入口|PAGE-01/02/03|首页/运动状态回应|TC-TBD|
|运动中获得一致且适度的角色回应。|2.1.2 显示角色状态表情|PAGE-01；PAGE-04–07按已有运动事件回应，承载TBD|首页/运动状态回应|TC-TBD|
|知道设备当前是否可用，以及怎样处理问题。|2.2.1 设备状态提示|PAGE-00–08通用支撑|操作反馈/状态展示|TC-TBD|
|清楚操作是否生效。|2.2.2 操作接收与确认|PAGE-00–08通用支撑|操作反馈/状态展示|TC-TBD|
|收到可执行而非无效任务。|3.1.1 接收并检查运动任务|PAGE-03消费后台接收事实，不新增接收页面|INIT / 任务有效性|TC-TBD|
|家长知道任务是否真实送达。|3.1.2 反馈任务接收结果|PAGE-03消费后台接收事实，不新增接收页面|INIT / 任务有效性|TC-TBD|
|儿童明白为什么做、做多少。|3.1.3 展示任务内容与执行状态|PAGE-03|INIT / 任务有效性|TC-TBD|
|运动目标清楚，自主运动与家长任务不混淆。|3.1.4 动作与目标确认|PAGE-02/03|INIT / 任务有效性|TC-TBD|
|减少不理解动作造成的失败。|3.2.1 动作说明|PAGE-04|READY / COUNTDOWN|TC-TBD|
|知道如何站好，准备完成后再开练。|3.2.2 入镜准备引导|PAGE-04；PAGE-09仅候选复用依据|READY / COUNTDOWN|TC-TBD|
|有时间准备，避免突然计数。|3.2.3 开始确认与倒计时|PAGE-04/05|READY / COUNTDOWN|TC-TBD|
|已完成努力不因中断消失。|3.3.1 暂停与成绩保留|PAGE-06/04；再次经过PAGE-05与否TBD|RUNNING / PAUSED / FINISHED|TC-TBD|
|安全且连贯地继续运动。|3.3.2 恢复运动|PAGE-06/04；再次经过PAGE-05与否TBD|RUNNING / PAUSED / FINISHED|TC-TBD|
|不强迫继续，不伪造达标。|3.3.3 达标与提前结束|PAGE-06 → PAGE-07|FINISHED|TC-TBD|
|避免在看不清动作时开始计数。|4.1.1 人体与画面可用性检测|PAGE-04/05/06；PAGE-09仅候选复用依据|READY / COUNTDOWN / RUNNING / PAUSED|TC-TBD|
|孩子和家长得到可信成绩。|4.1.2 有效动作计数|PAGE-06，异常准备原因由PAGE-04承接|READY / COUNTDOWN / RUNNING / PAUSED|TC-TBD|
|知道如何调整，而非被错误指责。|4.1.3 判定运动识别异常|PAGE-06，异常准备原因由PAGE-04承接|READY / COUNTDOWN / RUNNING / PAUSED|TC-TBD|
|完整开合跳被可信记录。|4.2.1 开合跳动作判定|PAGE-06计数依据，不新增动作范围|RUNNING|TC-TBD|
|完整深蹲被可信记录。|4.2.2 深蹲起动作判定|PAGE-06计数依据，不新增动作范围|RUNNING|TC-TBD|
|目标与实际成绩使用一致口径。|4.2.3 高抬腿动作判定|PAGE-06计数依据，不新增动作范围|RUNNING|TC-TBD|
|看见实际努力和距目标的差距。|5.1.1 次数与进度反馈|PAGE-06|RUNNING / FINISHED|TC-TBD|
|得到可理解指导且减少挫败。|5.1.2 动作反馈与调整提示|PAGE-06|RUNNING / FINISHED|TC-TBD|
|获得尊重真实努力的反馈。|5.1.3 完成鼓励|PAGE-07|RUNNING / FINISHED|TC-TBD|
|儿童结束后能理解本次努力。|5.2.1 运动结果查看|PAGE-07|FINISHED / SAVED / SYNCING / SYNCED|TC-TBD|
|不把运动结束误解为已回传。|5.2.2 保存与同步提示|PAGE-07；必要同步提示PAGE-01|FINISHED / SAVED / SYNCING / SYNCED|TC-TBD|
|每次运动可以追溯到正确儿童。|6.1.1 记录创建与归属|PAGE-02/03/06/07共用事实支撑，无重复记录系统|创建时机TBD / FINISHED|TC-TBD|
|可信查看真实完成情况。|6.1.2 生成运动结果记录|PAGE-02/03/06/07共用事实支撑，无重复记录系统|创建时机TBD / FINISHED|TC-TBD|
|离线可使用、不丢记录。|6.2.1 本地保存|PAGE-01/03/06/07消费保存恢复事实；后台处理|保存维度：SAVED / 未保存|TC-TBD|
|重启后不产生重复或虚假的运动记录。|6.2.2 已保存记录恢复|PAGE-01/03/06/07消费保存恢复事实；后台处理|保存/恢复：SAVED或失败|TC-TBD|
|不误导家长或静默丢失。|6.2.3 保存失败处理|PAGE-01/03/06/07消费保存恢复事实；后台处理|保存/恢复：SAVED或失败|TC-TBD|
|家长查看同一真实记录。|6.3.1 上传结果并更新同步状态|PAGE-07/01消费独立同步状态，后台处理|SAVED / SYNCING / SYNCED|TC-TBD|
|没有重复记录或虚假成长。|6.3.2 补传失败结果并防重复|PAGE-07/01消费独立同步状态，后台处理|SAVED / SYNCING / SYNCED|TC-TBD|
|可完成连接并理解故障。|7.1.1 网络连接管理|PAGE-00/08；PAGE-01必要状态提示|在线/离线（独立维度）|TC-TBD|
|理解联网状态与当前可用能力。|7.1.2 联网状态提示|PAGE-00/08；PAGE-01必要状态提示|在线/离线（独立维度）|TC-TBD|
|家长端了解设备可用状态。|7.2.1 设备状态同步|后台同步支撑，非独立页面|绑定/儿童/设备状态|TC-TBD|
|避免记录分配给错误儿童。|7.2.3 绑定状态与当前儿童确认|PAGE-00/08；PAGE-01使用有效上下文|绑定/儿童/设备状态|TC-TBD|
|家长边界可控且可解释。|8.1.1 检查授权并阻断不允许的采集|PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守|隐私准入/采集状态|TC-TBD|
|知道摄像头是否工作，并能停止采集。|8.1.2 摄像头状态提示与关闭|PAGE-04/05/06/08，PAGE-01必要提示；PAGE-09获准后亦须遵守|隐私准入/采集状态|TC-TBD|
|可管理设备数据的使用和清理。|8.2.2 处理设备数据权限与删除请求|后台执行与回执；PAGE-08设备端入口TBD|权限/提醒约束|TC-TBD|
|减少重复催促和夜间打扰。|8.2.3 提醒时段与频率控制|PAGE-01/06/07等提示输出约束；PAGE-08设置入口TBD，不等于声音控制|权限/提醒约束|TC-TBD|

7.2.2已停用并归6.3.1，8.2.1已停用并移8.3全局约束，不重复实现；约束适用于全部PAGE，测试引用TC-TBD。PAGE-09候选不与已批准独立功能绑定，4.3.1/4.3.2只在14.2候选层追踪。其他P1/未决追踪继续第9章，不虚构PAGE或测试编号。

当前同步结果：47项原P0 / Pending Review、20项历史候选 / 优先级TBD、2项历史停用追溯；本次新增功能数为0。UE IA仍明确以v0.4核心作为引用基线，本大纲v0.5.2是核心与候选的同步评审清单，不代替范围批准。原始UI/FR/TR与测试未改写，后续引用应明确版本。


# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v1.0.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 从PRD迁入69项追踪、47详细卡、状态/异常及问题关联，新增对应PRD业务章节；不新增需求编号或范围 |

| v1.0.1 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 记录用户确认MVP演示仅开合跳、深蹲起、高抬腿；保留整体七动作追踪与其他未决项，编号及优先级不变 |

| v1.1.0 | 2026-10-12 | Codex（AI，执行用户指令） | Review | 接收功能规格原69项完整条目与功能状态/页面追踪，新增Excel同源导出；原PRD追踪保留 |

# Change Impact

原正文内部管理信息独立维护；来源、编号、优先级和未决项不变。风险Medium，需检查迁移完整性。详见[变更单](../../governance/CHANGE-PRD-READABILITY-20261012.md)。

# Decision Log

无产品/架构决策；用户要求正文与追踪分离，既有ID继续沿用，无实际Test Case则TC-TBD。

### Change Impact — MVP演示三动作确认

演示动作范围从待确认改为用户已确认；其他范围/规则未变。详见[变更单](../../governance/CHANGE-MVP-THREE-ACTIONS-CONFIRMED-20261012.md)。

### Decision Log — MVP演示三动作

2026-10-12用户确认MVP仅演示开合跳、深蹲起、高抬腿；这是已确认演示范围，整体产品七动作追踪及动作规则/单位仍未被本次决策删改。确认来源：用户本轮消息；具体执行Owner待指定。

### Change Impact — Feature separation

从功能大纲迁入机器追踪信息，功能与状态不变；[变更单](../../governance/CHANGE-FEATURE-DOCUMENT-SEPARATION-20261012.md)。

### Excel同源导出

[RTM Excel v0.1.0](Teamo_Device_Requirement_Traceability_Matrix_v0.1.xlsx)为当前69项记录的固定导出，RTM Markdown是维护入口；修改后重新导出，不独立裁决范围。

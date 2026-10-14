# BodyPark ATOM 设备端截图归档 · v1.0

> 本文件是「Raw Evidence → Feature Cluster → Analysis Document」流程中的 **Feature Cluster（特征聚类归档）** 层。
> 上游原始证据：`00_Raw_Source/`（112 张连续实拍帧，原名保留，未删改）。
> 下游分析文档：`BodyPark_ATOM_设备端软件拆解_V1.0.md`（页面级拆解）。

## Document Control
| 字段 | 值 |
|---|---|
| 文档版本 | v1.0.0 |
| 状态 | Draft（待目视复核） |
| 生成日期 | 2026-10-13 |
| 方法 | 像素级特征提取（亮度/方差/暗像素/肤色占比/主色相/逐帧差异）+ 序列分段，非人工目视 |
| 重要限制 | 当前环境无法目视读取 JPG；页面级身份（当前页面）为**推断+待验证**，仅模块级（摄像头 vs UI）有数据支撑 |

## 1. 文件夹结构
```
00_Raw_Source/  (0 png)
01_Device_State_待机环境/  (0 png)
  ├─ Idle待机/  (0 png)
  ├─ 开机动画/  (0 png)
  ├─ 电量时间/  (0 png)
  ├─ 表情状态/  (0 png)
02_Onboarding_首次使用/  (0 png)
  ├─ 开机引导/  (0 png)
  ├─ 用户初始化/  (0 png)
  ├─ 设备绑定/  (0 png)
  ├─ 配网/  (0 png)
03_Home_首页导航/  (0 png)
  ├─ 主菜单/  (0 png)
  ├─ 快捷入口/  (0 png)
  ├─ 首页/  (0 png)
04_System_Settings_系统设置/  (0 png)
  ├─ WiFi/  (0 png)
  ├─ 亮度/  (0 png)
  ├─ 关于设备/  (0 png)
  ├─ 控制中心/  (0 png)
  ├─ 日期时间/  (0 png)
  ├─ 软件更新/  (0 png)
  ├─ 音量/  (0 png)
05_Training_运动训练/  (0 png)
  ├─ AI识别准备/  (0 png)
  ├─ 推荐课程/  (0 png)
  ├─ 暂停结束/  (0 png)
  ├─ 模式选择/  (0 png)
  ├─ 训练中/  (0 png)
  ├─ 训练入口/  (0 png)
  ├─ 训练结果/  (0 png)
  ├─ 课程详情/  (0 png)
06_AI_Capability_AI能力/  (37 png)
  ├─ AI反馈/  (0 png)
  ├─ 人体检测/  (0 png)
  ├─ 动作计数/  (0 png)
  ├─ 姿态识别/  (0 png)
  ├─ 摄像头取景/  (37 png)
07_Growth_Record_成长记录/  (0 png)
  ├─ 历史记录/  (0 png)
  ├─ 成就/  (0 png)
  ├─ 数据统计/  (0 png)
  ├─ 连续打卡/  (0 png)
08_Accessories_Ecosystem_生态扩展/  (0 png)
  ├─ 手机连接/  (0 png)
  ├─ 手表/  (0 png)
  ├─ 投屏/  (0 png)
  ├─ 摆放说明/  (0 png)
  ├─ 耳机/  (0 png)
99_Unclassified_待确认/  (75 png)
  ├─ 无法判断页面/  (75 png)
```

## 2. 分类统计（按模块）
| 模块 | 截图数量 | 说明 |
|---|---|---|
| 06_AI_Capability_AI能力 | 37 | 肤色占比≥0.08+逐帧高变化→实时摄像头/人体检测画面（数据支撑，中置信） |
| 99_Unclassified_待确认 | 75 | 设备UI浏览序列，页面身份待目视细分 |
| 01/02/03/04/05/07/08 | 0 | 已预建文件夹；本批112帧在逐页判定前暂统一挂在 99，待目视复核后下沉到对应模块 |

**总截图数：112**

## 3. 页面流程地图（数据支撑版）
```
[启动/待机]
   │
   ▼
(521–545) AI 摄像头实时取景 / 人体检测 / 训练中  —— 视频段，25帧，肤色0.10–0.18
   │
   ▼
(546–620) 设备 UI 浏览序列  —— 75帧，绿底/浅底主题，逐帧小幅变化
           （顺序/具体页面待目视确认：可能含 首页·设置·训练菜单·课程详情·结果·成长·生态）
   │
   ▼
(621–632) 摄像头实时画面（收尾/第二段）  —— 12帧，肤色0.08–0.15
   │
   ▼
[结束]
```
> 说明：连续帧的「逐帧高变化」是实时视频（摄像头）的特征；「逐帧小幅变化」是翻页/滑动浏览 UI 的特征。
> 据此可确定两段摄像头视频（521–545、621–632）夹一段 UI 浏览（546–620），但 **UI 段内部页面顺序无法由数据判定**。

## 4. 待确认页面列表（置信度=低，共 75 张）
以下帧已归入 `99_Unclassified_待确认/无法判断页面`，并给出「建议细分模块（按主色相推断，待验证）」供目视复核时参考：
| 截图(新名) | 原帧 | 主色相 | 建议细分模块(待验证) |
|---|---|---|---|
| 99_Unclassified_UIBrowse_Unknown_001.png | #546 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_002.png | #547 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_003.png | #548 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_004.png | #549 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_005.png | #550 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_006.png | #551 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_007.png | #552 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_008.png | #553 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_009.png | #554 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_010.png | #555 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_011.png | #556 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_012.png | #557 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_013.png | #558 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_014.png | #559 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_015.png | #560 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_016.png | #561 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_017.png | #562 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_018.png | #563 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_019.png | #564 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_020.png | #565 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_021.png | #566 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_022.png | #567 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_023.png | #568 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_024.png | #569 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_025.png | #570 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_026.png | #571 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_027.png | #572 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_028.png | #573 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_029.png | #574 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_030.png | #575 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_031.png | #576 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_032.png | #577 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_033.png | #578 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_034.png | #579 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_035.png | #580 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_036.png | #581 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_037.png | #582 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_038.png | #583 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_039.png | #584 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_040.png | #585 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_041.png | #586 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_042.png | #587 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_043.png | #588 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_044.png | #589 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_045.png | #590 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_046.png | #591 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_047.png | #592 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_048.png | #593 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_049.png | #594 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_050.png | #595 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_051.png | #596 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_052.png | #597 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_053.png | #598 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_054.png | #599 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_055.png | #600 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_056.png | #601 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_057.png | #602 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_058.png | #603 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_059.png | #604 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_060.png | #605 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_061.png | #606 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_062.png | #607 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_063.png | #608 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_064.png | #609 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_065.png | #610 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_066.png | #611 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_067.png | #612 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_068.png | #613 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_069.png | #614 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_070.png | #615 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_071.png | #616 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_072.png | #617 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_073.png | #618 | green | 05_Training/07_Growth_Record/03_Home(绿色主题页) |
| 99_Unclassified_UIBrowse_Unknown_074.png | #619 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |
| 99_Unclassified_UIBrowse_Unknown_075.png | #620 | blue/purple | 03_Home/04_System_Settings/05_Training(列表类浅底页) |

## 5. 逐帧分类总表（112 行）
| 截图编号 | 当前页面(推断) | 所属模块 | 目标文件夹 | 判断依据 | 置信度 |
|---|---|---|---|---|---|
| #521 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #522 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #523 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.11)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #524 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.16)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #525 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.10)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #526 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.08)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #527 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.09)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #528 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.11)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #529 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.11)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #530 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.11)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #531 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.11)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #532 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.12)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #533 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.13)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #534 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.12)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #535 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.12)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #536 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.12)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #537 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #538 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #539 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.14)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #540 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.14)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #541 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #542 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.18)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #543 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.10)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #544 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.11)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #545 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #546 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.01)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #547 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.01)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #548 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #549 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #550 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #551 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #552 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #553 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #554 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #555 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #556 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.05)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #557 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #558 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #559 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #560 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #561 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #562 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #563 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #564 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #565 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.01)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #566 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #567 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #568 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #569 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #570 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #571 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #572 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #573 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #574 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #575 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #576 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #577 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #578 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #579 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #580 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.01)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #581 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #582 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #583 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #584 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #585 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #586 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #587 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #588 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #589 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #590 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.01)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #591 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.05)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #592 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #593 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #594 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #595 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #596 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #597 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.01)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #598 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #599 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.06)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #600 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.01)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #601 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #602 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #603 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #604 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #605 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #606 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #607 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.06)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #608 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.02)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #609 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.03)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #610 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.06)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #611 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.06)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #612 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #613 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #614 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.04)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #615 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.06)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #616 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.07)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #617 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.07)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #618 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.07)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #619 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.07)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #620 | 待确认(UI页面) | 99_Unclassified_待确认 | 99_Unclassified_待确认/无法判断页面 | 肤色占比低(skin=0.07)+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定 | 低 |
| #621 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.08)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #622 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.08)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #623 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.09)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #624 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.11)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #625 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.12)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #626 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.13)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #627 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #628 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #629 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #630 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #631 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.14)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |
| #632 | AI摄像头实时画面(取景/倒计时/训练中·待细分) | 06_AI_Capability_AI能力 | 06_AI_Capability_AI能力/摄像头取景 | 肤色占比高(skin=0.15)+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分 | 中 |

## 6. 方法学与限制（务必阅读）
1. **证据来源**：每帧用 Python(Pillow+numpy) 提取 64×64 下采样的亮度均值、亮度标准差、暗像素占比(<20)、肤色像素占比（R>G>B 且 R-B>15 的近似规则）、主色相、文件体积；并算相邻帧灰度平均差以检测状态切换。
2. **摄像头判定规则**：肤色占比 ≥ 0.08 且相邻帧差异大 → 判定为「实时摄像头/人体检测」画面（module 06）。该规则对「画面中有人」敏感，对纯 UI/插画不敏感，故置信度标「中」。
3. **UI 段处理**：肤色占比低、主题稳定、逐帧小幅变化 → 判定为设备 UI 浏览，但**无法区分具体页面**，故全部暂挂 99_Unclassified，并附主色相推断的「建议细分模块」。**未**将其臆测填入 03/04/05/07/08，以避免误导 PRD 溯源。
4. **未做 OCR**：圆形小屏中文字号小、且为实拍照片，OCR 可靠性低，本轮未执行；如后续需要，建议人工目视或换多模态模型。
5. **下一步（目视复核）**：用多模态模型或人工打开 `00_Raw_Source/` 与已归类文件，将 99 中的 75 帧按真实页面下沉到 03/04/05/07/08 对应子文件夹，并把 06 中 37 帧细分到 摄像头取景/人体检测/姿态识别/动作计数/AI反馈，更新本表置信度至「高」。

## 7. 文件名命名规范（已应用）
格式：`模块_功能_页面_序号.png`（例：`06_AI_Capability_Camera_Live_001.png`、`99_Unclassified_UIBrowse_Unknown_001.png`）。
模块前缀用英文代码（06_AI_Capability / 99_Unclassified），与文件夹前缀一致，便于 PRD 引用与跨文档检索。

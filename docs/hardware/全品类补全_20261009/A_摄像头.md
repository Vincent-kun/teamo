# Document Control

| 字段 | 内容 |
|---|---|
| Document Type | Hardware Requirement / Research |
| Current Version | v0.1.1 |
| Status | Draft |
| Owner | 待确认（项目协调：魏子奇；不等同文档审批责任人） |
| Reviewer | 待指派 |
| Created Date | 2026-10-09 |
| Last Updated | 2026-10-12 |

> 文档控制版本以本表为准；原文件名和正文版本标识保留为历史业务版本。Draft/Review 为本次治理提交状态，非产品审批结论。创建日期取自原标识，待 Owner 核实。

# A 工作包 · 摄像头扩充研究记录（RV1106 生态）

- 执行日期：2026-10-09（所有 sources.date 均为当日核查日期）
- 执行者：硬件选型研究子代理（工作包 A）
- 项目约束：儿童 AI 运动陪伴机器人；主控暂沿 RV1106 系列（Rockchip）；MVP 掌心设备（约 60×90mm 级）；摄像头目标：有效视场约 120–130° 广角（**目标，未确认**）；MVP 死线 2026-11-15，先开发板验证、后自研 PCB。
- 红线遵守：只写 `A_摄像头.json`、`A_摄像头.md` 与 `assets/` 子目录；未知数值一律 null，未编造。

---

## 1. 检索范围与方法

| 渠道 | 用途 |
|---|---|
| Luckfox SDK 官方仓库（GitHub raw + DeepWiki 转录） | 核内核驱动文件存在性、官方 dts 传感器节点、IQ/模组配置 |
| Rockchip rkbin 官方仓库（DeepWiki 转录） | RV1106 HPMCU Thunderboot 传感器固件矩阵（GC2093/GC3003 等） |
| Rockchip 官网模组页 / Rockchip Linux IPC SDK 文档 | 官方认证模组 FOV、新增传感器流程 |
| GalaxyCore 官网 (en.gcoreinc.com) | GC3003 传感器官方参数 |
| 思特威传感器参数页（光电查 oe1.com / GoPhotonics / 联视 yelens 转录） | SC530AI / SC4336 传感器级参数 |
| 模组厂产品页（vanxoak 万象奥科、cameramodule.hk DGZX） | 模组级尺寸/FOV/接口 |
| 经销/商城页（frbiz、Alibaba 泰国站、一牛网 16rd） | 仅补价格与供货，不作规格主证 |
| OmniVision 产品简报（DigiKey 镜像 PDF） | OV5695 传感器级参数 |

核查手段：WebSearch 检索 → WebFetch 逐页取证 → 受管 Python（urllib）抓取产品图 → Read 工具人工核图。

既有 5 条（研究输入，未重复新增）：C01/C02 MIS5001 5MP（Luckfox B口/A口）、C03/C04 SC3336 3MP（A/B）、C05 IMX415-8MP-USB。

---

## 2. 逐条证据摘要（新增 6 条：C06–C11）

### C06 GC2093 模组（HD-CSI-2093，武汉万象奥科）
- 厂家页：1920×1080，1/2.9"，EFL 4.35mm，F2.2，**视场角 74°**，畸变 <-0.1%，40Pin MIPI，0~55℃；模组尺寸未给（null）。
- 驱动证据：Luckfox SDK `sysdrv/source/kernel/drivers/media/i2c/gc2093.c`（raw HTTP 200，compatible `galaxycore,gc2093`）；Rockchip rkbin RV1106 固件矩阵含 `rv1106_hpmcu_tb_gc2093`；CSDN 有 RV1106 dts 适配实例（module SIDA209300469 / lens 60IRC_F20）。Luckfox 默认 dts 未启用。
- 图片：vanxoak 页 https 超时、http 页无图片标签 → 无图（失败日志见 §5）。

### C07 SC530AI 模组（DGZX-AGIA8A035M1-29.6×20，DGZX/Dogoozx）
- 厂家页：5MP 2884×1624@60fps，1/2.7"，MIPI，AF/FF 可选，PCB 29.6×20mm；宣称镜头 5°–240° 可选（**无具体广角配置确认 FOV → 冲突未闭环**）。
- 传感器官方参数（SmartSens，经 oe1.com 转录）：CRA 15°，HDR 100dB，CSP 41pin 6.55×4.27mm，2.8/1.5/1.8V。
- 驱动证据：Luckfox SDK `sc530ai.c`（HTTP 200）；官方 dts `rv1103-luckfox-pico-ipc.dtsi` 含 `sc530ai@30` 节点（2lane，module CMK-OT2115-PC1 / lens 30IRC-F16）；Rockchip IPC SDK 官方文档以 SC530AI 为 RV1106 新增传感器示例。
- 图片：`assets/C07.jpg`（实物照，白底单摄模组+FPC，Read 核验与型号页对应）。

### C08 SC530AI 模组（TYS-HTWAI-S1，TOLUCKY）
- 经销页：FOV(D) 74°，模组 21.9×13.2×8.4mm，MIPI CSI-2，FF，AVDD2.8/DVDD1.5/IOVDD1.8，$14.99–24.99。
- 冲突未闭环：同款 Alibaba 泰国站页 Interface 写 DVP（与 MIPI 冲突）；TV Distortion 字段"1,000"含义不明（按 null）。
- 仅经销页可查、无原厂官网页 → 淘汰倾向，作为同传感器不同配置记录保留。
- 图片：frbiz 页 HTTP 503 → 无图。

### C09 SC4336（传感器级 + Luckfox SDK 配置）
- 传感器：4MP 2568×1448（2560×1440@30fps），1/3.06"，MIPI 1/2lane，CRA 15°，2.8/1.8V，CSP 35pin 5.75×3.872mm。
- 驱动证据：Luckfox SDK dts 含 `sc4336@30` 节点（module OT01 / lens 40IRC_F16，2lane）；`sc4336.c` HTTP 200。
- 模组厂家/尺寸/FOV 全部 null；FOV 无法与 120–130° 目标量化比较。
- 图片：oe1 超时、yelens 无图 → 无图。

### C10 GC3003（传感器级，GalaxyCore 官方）
- 官方页：3MP，1/2.8"，2.45µm FSI，RAW，Full@30fps，MIPI，CSP；定位 3MP smart IoT / 2K 行车记录。
- 驱动证据：Rockchip rkbin RV1106 固件矩阵含 GC3003（2304×1296@30fps）；Luckfox SDK `gc3003.c`（compatible `galaxycore,gc3003`，HTTP 200）。
- 无成品模组证据；与 SC3336 同规格，可作二供方向。FOV 取决于选配镜头。
- 图片：gcoreinc JS 渲染无图；camemake 仅透明占位图（已删除）→ 无图。

### C11 OV5695 模组（Rockchip 官方认证 OV5695-GA4A / 一牛网在售件）
- Rockchip 官方模组页：5M，MIPI，**AF**，FOV D84.0°/H56.6°/V71.5°，30Pin B2B。
- 一牛网在售件：77°、F2.4、AF、30fps@full、供电 2.8/1.2/1.8V —— 与官方 84° 为不同镜头版本，**冲突并列保留**。
- OmniVision 简报：1/4"，2592×1944@30fps / 1080p@60，2-lane MIPI，active 155mW，模组参考 8.5×8.5mm z≈4.4mm。
- 驱动证据：Luckfox SDK `ov5695.c`（compatible `ovti,ov5695`，HTTP 200）；但 RV1106 无默认 dts/IQ 适配证据 → 模组级适配待核。
- 图片：`assets/C11.jpg`（实物照，一牛网商城图，图内明确标注 OV5695 500W MIPI 模组；rock-chips 官网图 403 无法下载）。

---

## 3. 传感器族统计

| # | 传感器族 | 厂家 | 记录 | 新增? | 驱动证据 |
|---|---|---|---|---|---|
| 1 | MIS5001 内置传感器 | 未确认 (null) | C01/C02（既有） | — | SDK mis5001.c 在 |
| 2 | SC3336 | SmartSens | C03/C04（既有） | — | SDK dts+驱动 |
| 3 | IMX415 | Sony | C05（既有，USB） | — | UVC，不走 CSI 驱动 |
| 4 | **GC2093** | GalaxyCore | C06 | ✅ | SDK gc2093.c + rkbin 固件 |
| 5 | **SC530AI** | SmartSens | C07、C08 | ✅ | SDK dts+sc530ai.c |
| 6 | **SC4336** | SmartSens | C09 | ✅ | SDK dts+sc4336.c |
| 7 | **GC3003** | GalaxyCore | C10 | ✅ | SDK gc3003.c + rkbin 固件 |
| 8 | **OV5695** | OmniVision | C11 | ✅ | SDK ov5695.c |

- 全类合计 **11 条记录**（5 既有 + **6 新增**，≥8 达标）；**8 个传感器族**（新增 5 族，≥3 达标；其中 7 族型号明确，MIS5001 内置传感器仍为 null）。
- 说明：SC530AI 与 SC3336、SC4336 同属思特威但为不同传感器型号，按规范各计一族；相同传感器不同镜头/版本（SC530AI 的 DGZX/TOLUCKY 两版、OV5695 的 84°/77° 两版）按配置记录分列。

---

## 4. 覆盖结论（是否达标）

**结论：广角目标（120–130°）当前未达标。**

- 已确认 FOV 的候选中最高为 **OV5695 官方 AF 模组 DFOV 84°**（距目标差 36–46°）；其余确认值 74°（GC2093、TOLUCKY SC530AI），均在目标下限以下 46–56°。
- 唯一可能触及广角的线索是 DGZX 宣称"镜头 5°–240° 可选"，但无具体广角型号与确认 FOV → 冲突未闭环，不能据此升级任何候选为符合目标的产品相机。
- Luckfox 生态内（GC2093/SC2336 类、SC3336/SC4336/SC530AI、MIS5001、OV5695 驱动均在 SDK）选型空间充足，**瓶颈不在驱动与接口，而在广角镜头 + ISP 调优（LSC/CAC/去畸变）**。120–130° 通常意味着鱼眼级镜头（TTL 与畸变大），需定制模组并重做 IQ，且 RV1106 ISP3.2 的 CAC 资源有限，需评估去畸变后有效视场与画质。
- USB 路线（C05 IMX415）提醒：USB 摄像头须核 UVC/主机资源/带宽，不能当 CSI 无代价替换；本轮新增均为 MIPI CSI 2lane 路线。
- MVP 掌心尺寸（60×90mm）对模组外形（如 29.6×20mm、含 AF 马达高度）与镜头突出深度敏感，C07/C11 的厚度/完整镜头深度数据仍缺（null），结构评估前必须补齐。

## 5. 检索缺口与失败日志

| 项 | URL | 失败情况 |
|---|---|---|
| C06 产品图 | https://www.vanxoak.com/camera/hd-csi-2093.html | https 直连超时（Windows 10060，两次）；http 回退可取页但无图片标签（疑似 JS 懒加载）→ 无图，未用近似图 |
| C08(TOLUCKY) 页面与图 | https://usb-cameramodule.company.frbiz.com/p121876991-... | HTTP 503 Service Unavailable → 规格以搜索结果快照记录，图片失败 |
| C09 传感器页图 | http://m.oe1.com/product/6983714281336885248.html | 连接超时（10060）；yelens 转录页无图片标签 → 无图 |
| C10 官方页图 | https://en.gcoreinc.com/products/index?cid=14&subcid=19 | JS 渲染无可抓取图片；camemake.eu 仅透明占位图（已删除）→ 无图 |
| C11 官方图 | https://www.rock-chips.com/uploads/allimg/... | HTTP 403 Forbidden → 改用一牛网实物照（已在图内标注型号） |
| ov5695.c（rockchip-linux 主线） | https://raw.githubusercontent.com/rockchip-linux/kernel/.../ov5695.c | 404（该主线分支不含此路径）；改以 Luckfox SDK ov5695.c（HTTP 200）为准 |
| GitHub API 目录列表 | api.github.com/repos/LuckfoxTECH/luckfox-pico/contents/... | 返回空内容，改用 raw 文件逐一 HEAD 核验（全部 200） |
| RV1106 已确认 120–130° 广角成品模组 | — | 多轮检索未找到厂家页明确标注 120–130°+ 的 RV1106 CSI 模组 → 记为检索缺口（与 §4 结论一致） |
| MIS5001 内置传感器型号 | — | 未能在公开资料确认，维持 null（C01/C02 既有记录） |

## 6. 给涛哥的问题

1. **120–130° 的口径**：指对角 DFOV 还是水平 HFOV？可接受的畸变上限？能否接受鱼眼 + ISP 去畸变（去畸变后有效视场会缩水，需按算后视场复核目标）？
2. **是否接受定制广角模组**：DGZX 等厂宣称可配广角镜头（5°–240° 可选话术），若走定制，MOQ/NRE/打样周期是否可接受（死线 2026-11-15）？
3. **ISP 调优资源**：广角镜头需重做 LSC/CAC/畸变校正 IQ 文件（Luckfox meta 分区机制），调优由我方、模组厂还是 Luckfox/瑞芯微支持？有无预算？
4. **MIS5001 的内置传感器型号**：可否向 Luckfox 索取（影响传感器族统计与二供策略）？
5. **AF 需求**：运动陪伴场景儿童在 0.5–2m 动态范围，OV5695 AF 版（唯一确认 AF）是否值得引入，还是全系定焦 + 大景深镜头？
6. **USB vs CSI 路线收敛**：C05（IMX415 USB）是否继续并行验证，还是 CSI 全押以省主机带宽？


---

# Version History

| Version | Date | Author | Status | Change Summary |
|---|---|---|---|---|
| v0.1.0 | 待核实 | 原作者待核实 | 待核实 | 登记导入前现存正文基线；无版本标识，治理初始化编号，不代表历史首次发布；不推断历史修改或批准 |
| v0.1.1 | 2026-10-12 | Codex（AI，执行用户指令） | Draft | 新增 Document Control、标准 Version History、Change Impact 与 Decision Log；保留既有业务正文及历史记录 |

> 本表仅登记已验证的现存基线与本次修改。历史日期、作者和状态待核实；原有版本记录是补录证据入口，不能据文件名编造缺失版本。

# Change Impact

### Modified Sections

- Section: 文档顶部与治理附录。
- Before: 缺少统一的文档控制表和标准版本记录。
- After: 增加控制表、基线与 Patch 历史、影响分析和决策记录入口；原业务正文保留。

### Impact Scope

Affected:
- 本文及引用本文的项目文档；本次无业务要求变更。
- 逐文件版本、备份和修改报告见 docs/governance/CHANGELOG-20261012.md。

### Risk

Low。Owner、Reviewer、历史审批状态仍待确认；本次结构治理不冻结产品需求。

# Decision Log

本次未修改产品方向、功能取舍或系统架构。既有决策及待决事项保留在正文，尚未逐条验证迁入；后续涉及这些事项时按 docs/governance/DOCUMENT_VERSION_POLICY.md 记录，建议与已批准决策必须区分。

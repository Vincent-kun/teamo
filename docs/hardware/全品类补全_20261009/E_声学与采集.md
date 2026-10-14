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

# E 工作包 · 功放与麦克风/音频采集补全（2026-10-09）

项目：儿童 AI 运动陪伴机器人 | 主控：RV1106（Rockchip RV1106G2）| MVP 开发板验证
本文件只新增条目，不重复既有 A01（PAM8302）、AMP02（MAX98357A）、AUD01（TLV320AIC3104）、MIC01（SPH0645LM4H-B）。
配套结构化数据：`E_声学与采集.json`；产品图：`assets/`。

---

## 1. 功放路线对照（含既有，合计 4 条 ≥3 达标）

| ID | 型号 | 输入方式 | 供电 | 额定输出（额定口径，THD 注明） | 8Ω 适配 | 控制方式 | 嘉立创/得捷可得性 |
|----|------|---------|------|------------------------------|---------|----------|------------------|
| A01 | PAM8302（Adafruit #2130） | 模拟 Class-D | 5V | 2.5W@4Ω（THD 10% 口径） | 8Ω 待核 | SHUTDOWN 引脚 | 模块易得 |
| AMP02 | MAX98357A（既有） | I²S 数字 Class-D | 2.5–5.5V | 3.2W@4Ω / 约1.4W@8Ω（5V，THD10%） | ✓ | SD 引脚增益档 | 渠道充足 |
| **AMP03** | **NS4168（新增）** | **I²S 数字 Class-D** | 3.0–5.5V | 2.5W@4Ω（VDD=5V，额定）；THD+N 0.2%@1W | ⚠ 8Ω 规格书未给，按 4Ω 折算约 1.2–1.5W 待实测 | CTRL 单线脉冲（选声道/音量衰减最大 -10dB/关断） | 嘉立创 C5246378（永阜康版） |
| **AMP04** | **NS4150（新增）** | **模拟差分 Class-D** | 3.0–5.25V | **@5V/8Ω：1.3W@THD1% / 1.7W@THD10%；@5V/4Ω：2.0W@THD1% / 2.8W@THD10%** | ✓ 8Ω 数据齐全 | CTRL 高电平工作 | 渠道有售（原厂 Nsiway；矽源特兼容版已标停产） |

**结论**：不同路线 ≥3 条成立 —— 模拟 Class-D ×2（PAM8302 / NS4150）+ I²S 数字 Class-D ×2（MAX98357A / NS4168）。
- 任务书要求"MAX98357 以外真实 I2S 型号"：**NS4168 经原厂 PDF 核实为真 I²S 数字输入**（BCLK/LRCLK/SDATA 三线、内置 DAC + D 类调制、8–96kHz），非模拟功放，任务书中"NS4168 为模拟"的猜测不成立（佐证：szczkjgs 官方 PDF 标题"I²S 数字输入、防失真、2.5W 单声道 D 类音频功放"）。
- 与 8Ω 1–2W 喇叭的匹配：**首选 NS4150**（8Ω 额定 1.3W@1% / 1.7W@10%，落在喇叭 1–2W 区间）；NS4168 数字链路省一路 DAC 但 8Ω 数据缺。
- 跨型号功率比较口径：以上均为 datasheet 电气特性表 THD 条件下额定值，非营销"3W"口径（NS4150 官网 3W 即 THD10%@4Ω/5V=2.8W 的约整）。

**AEC 关联差异**：数字功放（AMP02/AMP03）从 I²S 取音，回采参考需走 I2STDM loopback 或软件回环；模拟功放（A01/AMP04）直挂内置 codec LINEOUT，链路最短、回采由 codec 提供（见 §3）。

---

## 2. 音频采集路线对照（含既有，采集 4 条 + codec 1 条 ≥3 达标）

| ID | 型号 | 类型 | 灵敏度 | SNR | 供电/偏置 | 进声 | 接入 RV1106 方式 |
|----|------|------|--------|-----|-----------|------|------------------|
| MIC01 | SPH0645LM4H-B（既有） | I²S 数字 MEMS | -26dBFS | 65dB(A) | 1.62–3.63V，无偏置 | 顶进声 | 直挂 I²S0 从机 |
| **MIC02** | **MSM261S4030H0R（新增）** | **数字 MEMS，输出 I2S**（渠道一致标注；PDM 说法待原厂终核） | -26dB ±1dB | 61dB | 1.8V，0.75–1mA，无偏置 | 前进声 | 同 SPH0645：直挂 I²S0 作从机（主模式出 BCLK/LRCLK） |
| **MIC03** | **IM69D130（新增）** | **PDM 数字 MEMS** | -36dBFS ±1dB | **69dB(A)**@3.072MHz | 1.62–3.6V，980µA，无偏置 | 底进声 | **不可直连**：RV1106 无 PDM 控制器（§3.3），需 PDM 输入 codec 桥接或弃用 |
| **MIC04** | **CMM-2718AT-38164W-TR（新增）** | **模拟 MEMS** | -38dBV ±1dB@94dB SPL | 64dB(A) | 1.5–3.6V（额定 1.8V），175µA；自带输出偏置，无需 MICBIAS | 顶进声 | AC 耦合入内置 codec 差分 MICP/MICN（ADC Mode 差分/单端可配） |
| AUD01 | TLV320AIC3104（既有） | 外置 codec（I2S） | — | — | — | — | 挂 I²S0，作为多路模拟输入/输出的可选增强 |

**三路线对照结论**：
1. **模拟 MEMS → 内置 codec（推荐 MVP 首选）**：MIC04 单点 BOM 最简（免外置 codec、免时钟），RV1106 codec 2×24bit ADC（90dB SNR）+ MICBIAS 可编程（0.8–0.975×VREF，可关），61–64dB 麦克风 SNR 不构成瓶颈；国产兼容件（聆麦 2718 系列，立创在售）可降本。
2. **I²S 数字 MEMS 直挂（备选）**：MIC01/MIC02 直挂 I²S0，抗板级噪声好；但与数字功放共用 I²S0 时声道/时隙规划复杂（I2S0_8ch 有 8 时隙，资源够但 dts 路由要写对），且 RV1106 作为 I²S 主机需输出正确 BCLK/LRCLK 给 MEMS 麦（SPH0645 类 64×fs）。
3. **PDM（受限路线）**：IM69D130 性能最优（69dB SNR + 130dB AOP + 相位匹配适合阵列），但 **RV1106 官方 datasheet 无 PDM 控制器**，直连不可行；除非确认 TRM 隐藏支持或增加桥接芯片，否则本项目不推荐。

---

## 3. RV1106 内置 codec 与 AEC 查证结论（附证据链）

### 3.1 内置 Audio Codec 能力（可省掉外置 codec）
| 项目 | 规格 | 证据 |
|------|------|------|
| ADC | 2×24bit，90dB SNR，支持差分/单端 MIC 或 Line 输入 | RV1106 Brief Datasheet（rock-chips.com 官方 PDF）Audio Codec 节 |
| DAC | 1×24bit，90dB SNR（LINEOUT 输出） | 同上 + Luckfox Pico Ultra wiki（rv-acodec 声卡、LINEOUT Volume 控件实测） |
| 采样率 | 8/12/16/24/32/44.1/48/96 kHz | ScenSmart 转载 RV1106 Datasheet 音频节 |
| MICBIAS | 可编程 VREF×0.80–0.975，可开/关（`ADC MICBIAS Voltage`、`ADC Main MICBIAS` 控件） | Luckfox Pico Ultra wiki amixer 实测输出 |
| 处理 | ADC 自带 ALC/AGC（左右声道增益 0–3、ALC 目标音量、HPF 截止可配） | 同上 wiki `rk_mpi_amix_test --list_contents` 输出 |
| I²S | I2S0_TDM 8 通道（8TX+8RX），16–32bit，最高 192kHz，主/从，3 种 I2S 格式 + 4 种 PCM 模式 | RV1106 Brief Datasheet |

**结论：模拟麦 + 模拟功放场景下，RV1106 内置 codec 完全够用，外置 codec（AUD01 TLV320AIC3104）降级为可选** —— 仅当需要多路模拟输入、更高采样率 ADC 阵列或 PDM 桥接时才上。
注意：Luckfox Pico Pro/Max 未引出音频引脚，音频功能需在 MVP 自研板/扩展板上从核心板引出（Pico Ultra W 已验证 acodec 链路可用）。

### 3.2 AEC 算法在哪一层
**结论：RV1106 无独立音频协处理器/DSP，AEC 在 Cortex-A7 主控软件层（Rockchip SDK 算法库）运行。**

证据链：
1. **Rockchip RKMedia 官方开发指南**（github.com/rockchip-linux 系中文文档）：「音频算法 目前支持对讲场景 AEC 算法，录音场景 ANR 算法」，AI 通道集成、算法后输出 PCM —— 算法在 CPU 用户态库。
2. **RV1106 SDK common_algorithm 库**（libRKAP_Common.so，RKAPPLUS 框架）：含 AEC/ANR/AGC 模块，CMake 开关 `AEC_ANR_AGC_ENABLE` / `ANR_ENABLE`；RV1106 平台编译配置中未显式置 TRUE（RK3588/RV1126 才显式开启），且关闭 NN 唤醒、保留 AED —— **RV1106 SDK 内 AEC 的实际可用性/默认开关待核**（DeepWiki jetkvm/rv1106-system 源码级摘录）。
3. **厂商方案宣传**（EEPW，RV1106/RV1103 低功耗 AOV 方案）：「智能音频方案，支持回声消除、语音降噪、哭声检测、异常声音检测」—— 印证能力存在，但为营销口径，不作规格依据。
4. **硬件回采参考（AEC 前提）**：codec/I2STDM 支持 Digital Loopback —— Mode1（4ch：1-2 声道 MIC 拾音、3-4 声道回采）、Mode2（2ch：左声道 MIC、右声道为播放回采），`I2STDM Digital Loopback Mode` 控件实测于 Luckfox wiki —— 即 RV1106 硬件链路专门为 AEC 提供回声参考通道。

**MVP 建议**：Mode2 回采 + RKMedia/RKAPPLUS AEC 软件方案先跑通；主要风险是 A7 单核 1.2GHz 同时承载 AEC + ASR/交互的 CPU 余量，需实测（给涛哥问题 #2）。

### 3.3 PDM 接口查证结论
- RV1106 官方 Brief Datasheet「Audio Interface」仅列 I2S0（8ch，I2S/TDM/PCM）与 Audio Codec 两项，**无 PDM 控制器**；
- Luckfox wiki（Pico Ultra 音频教程）仅演示模拟 MIC 经 acodec 采集，未提 PDM；
- 第三方 Luckfox issue（#22）讨论 I²S 外接 codec，官方回复路线为 MIC/LINEOUT + 未来引出麦克风接口，未提 PDM。
- **结论：PDM 数字麦（MIC03 IM69D130）不能直连 RV1106，列为受限路线；Rockchip TRM 是否有未公开支持标"待核"。**

---

## 4. 声孔/麦克风位置约束（给结构 WF 的输入）

依据工作包规范「麦克风远离出音口、声孔进排布图」要求，输出以下约束：

### 4.1 硬约束
1. **麦克风声孔必须远离喇叭出音口**：同面布置时直线距离 ≥100mm，或用隔断墙 + 密封泡棉隔离；目的：降低近场直达声耦合（减轻 AEC 收敛负担）并防啸叫。AEC 虽在软件层，但近场耦合过强（>15dB 回声/拾音比）会显著劣化双讲性能。
2. **所有声孔进结构排布图**：喇叭出音孔、麦克风进声孔均需在结构 WF 排布图上标注孔位/孔径/密封方式，禁止模具开孔后追加。
3. **声孔规格**：麦克风进声孔 φ1.0–1.5mm，孔道尽量短（<1mm 距振膜），进声孔与外壳间加防尘网/防水网（IP 等级由结构定）。
4. **密封与腔体**：喇叭必须带后腔（密闭或泄漏受控），喇叭腔体漏气路径不得直通麦克风声孔；喇叭与麦克风之间如有连通腔体，需加隔墙。

### 4.2 逐器件输入（方向性）
| 器件 | 进声方向 | 结构注意 |
|------|----------|----------|
| MIC04 CMM-2718AT | **顶进声（AT）** | 孔正对膜面；国产替代聆麦 2718 有下进声版本，替换时方向要改 |
| MIC02 MSM261S4030H0R | 前进声（顶） | 同上 |
| MIC03 IM69D130 | **底进声** | 需 PCB 开孔/导声通道，孔道密封圈必需 |
| MIC01 SPH0645（既有） | 顶进声 | 同 MIC04 |
| 喇叭（既有 8Ω 1–2W 两档） | 出音口 | 出音口避免朝向手部握持遮挡位（儿童场景）；与麦孔隔断 |

### 4.3 板级伴随约束（给硬件 WF）
麦克风（尤其模拟 MIC04）远离 DC-DC 电感、马达驱动、WiFi 天线馈点；模拟麦偏置走差分对 + 就近 RC；数字麦 I²S 走线远离喇叭功率环路。

---

## 5. 给涛哥的问题

1. **MSM261S4030H0R 输出类型渠道冲突**（嘉立创/德方均标 I2S，部分网络页标 PDM 且内容互相矛盾）：能否通过敏芯原厂 FAE 拿规格书终核？若确为 PDM 则该条降级、RV1106 不可直连。
2. **RV1106 SDK 里 RKAPPLUS（libRKAP_Common.so）的 AEC/ANR/AGC 在 Luckfox 等公开 SDK 中是否默认编译开启？** 有无 AEC 时延与 CPU 占用实测数据（A7 单核 1.2GHz 跑 AEC + ASR 并行余量）？
3. **NS4168 8Ω 功率规格书未给**：接受按 4Ω 折算、上板实测，还是直接选 NS4150（8Ω 数据齐全）作为数字链路备选前的默认模拟功放？
4. **I²S0 声道分配**：若走"数字麦直挂 + 数字功放"同总线方案，I2S0_8ch 的时隙规划（麦克风 64×fs vs 功放 32×fs BCLK 兼容性）需要 dts 层确认，是否有参考案例？

---

## 附：本次查证覆盖与缺项汇总

- 新增 5 条：AMP03（NS4168，I²S 数字）、AMP04（NS4150，模拟 Class-D）、MIC02（MSM261S4030H0R，数字 MEMS）、MIC03（IM69D130，PDM）、MIC04（CMM-2718AT-38164W-TR，模拟 MEMS）。
- 产品图：成功 3（AMP04 电路图 / MIC03 官方实物 / MIC04 实物），失败 2（NS4168：渠道页 JS 动态加载 + LCSC API 502；MSM261：仅拿到占位图，弃用）。
- 主要待核项：MSM261 输出类型终核、RV1106 TRM PDM 支持、IM69D130 替代型号（原厂标 not for new design）、NS4168 8Ω 额定、各条目价格。


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

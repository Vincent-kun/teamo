# C 工作包：网络与天线补全 · 2026-10-09

子代理执行记录。配套数据：[C_网络与天线.json](C_网络与天线.json)。前置输入沿用 [天线候选池_20261009.json](../天线候选池_20261009.json)、[天线选型与布置依据_20261009.md](../天线选型与布置依据_20261009.md) 与交接文档中的 N01–N06，不重复展开。

## 1. 检索范围与方法

- 核查日期统一 2026-10-09；技术事实以厂家规格书/型号页/FCC 档案为准，经销/电商页只作价格供货与芯片旁证（并明确标注"待核"）。
- 新增检索面：RV1106/Luckfox 生态 Wi-Fi 驱动证据（Luckfox 官网/wiki、LuckfoxTECH luckfox-pico SDK）、乐鑫协处理器官方文档（规格书、ESP-Hosted-MCU）、2.4GHz FPC/PCB 天线（Molex/Taoglas）。
- 红线执行：未知写 null；"UART AT 存在≠支持目标联网方式"；SDIO 模组必须核到驱动证据才写"支持"，否则标"驱动待核"；库存/样件美元价不计入 BOM。

## 2. Wi-Fi/BLE 独立路线：三条路线全部成池（N07–N12 新增 6 条）

### 路线 A：SDIO Linux 无线模组（主推验证路线）

| ID | 型号 | 频段 | BLE | 接口/驱动证据 | 尺寸 mm | 供电 | 认证 |
|---|---|---|---|---|---|---|---|
| N07 | AIC8800DC（Luckfox Pico Ultra W 板载） | 2.4G Wi-Fi 6 (11ax 1T1R) | BT5.2/BLE | SDIO(Wi-Fi)+UART/PCM(BT)；**Luckfox Pico SDK 官方支持**（aic8800 驱动+固件+wifi_bt_init.sh） | 模组独立尺寸未公开 | 待核 | 待核 |
| N08 | 亿佰特 E103-RTL8189FTV（RTL8189FTV-VC-CG） | 2.4G 11b/g/n 150M | 无 | SDIO 2.0；**驱动待核**（SDK 实测列表是 RTL8189FS/RTL8188FTV，与 RTL8189FTV 不同驱动） | 12×12×1.9 | 3.3V（VDDIO 3.3/1.8） | SRRC（厂商声明） |
| N09 | Ampak AP6256 | 2.4G+5G 11a/b/g/n/ac（Wi-Fi 5） | BT5.0（官网新版写 5.4） | SDIO 3.0+UART/PCM；**Luckfox Pico SDK 支持 AP6256** | 12×12×1.65（带罩 max） | VBAT 3.2~3.6V | FCC RPJAP6256/CE/TELEC/SRRC/BQB |

RV1106/Luckfox 生态证据链：Luckfox Pico SDK 支持列表含 AP6256、AIC8800（W 系列）、RTL8188FTV、RTL8189FS、ATBM、SSV6115（[SDK 网络配置文档](https://deepwiki.com/LuckfoxTECH/luckfox-pico/6.1-networking-configuration)，源自 LuckfoxTECH/luckfox-pico 仓库）；Pico Ultra W 官方 wiki 有完整 wpa_supplicant/bluetoothctl 流程（[Wi-Fi/BT](https://wiki.luckfox.com/Luckfox-Pico-Ultra/WiFi-BT/)）。正基 AP6212 本轮未单独复核（AP6256 已覆盖双频+BT5 需求且驱动证据更直接），留作后续补充。

### 路线 B：USB WiFi dongle（临时验证，不进 BOM）

| ID | 型号 | 频段 | BLE | 尺寸 mm | 说明 |
|---|---|---|---|---|---|
| N10 | TP-LINK TL-WN725N 免驱版 | 2.4G 11b/g/n 150M，20dBm | 无 | 18.6×15×7.1（整壳） | 芯片 RTL8188EU 为电商标注（待核）；官方仅列 Windows，Linux 靠主线 rtl8xxxu/r8188eu，RV1106 下**驱动待核**；SDK 已支持 RTL8188FTV（USB），可作替代芯片方向 |

### 路线 C：UART/SDIO 协处理器（对 N06 ESP32-C3 的扩展）

| ID | 型号 | 频段 | BLE | 尺寸 mm | 峰值电流 | 主机接口要点 |
|---|---|---|---|---|---|---|
| N11 | ESP32-C6-MINI-1-N4 | 2.4G Wi-Fi 6 (11ax) | BLE 5.3 | 13.2×16.6×2.4 | TX 峰值 382mA @11b 20.5dBm；RX 78mA（规格书） | **可作 SDIO 从机**（ESP-Hosted 仅 ESP32/C6 可当 SDIO slave，官方 P4+C6 组合）；UART 仅 ~0.68Mbps 不适合跑流量 |
| N12 | ESP32-S3-MINI-1-N4 | 2.4G 11b/g/n | BLE 5.0 | 15.4×20.5×2.4（第三方口径，官方书待复核；N4R2 有 15.4×15.4 冲突口径） | TX 355mA/RX 95mA（立创摘要） | **不能作 SDIO 从机**，只能 SPI（~24Mbps）或 UART；RF 能力与 C3 同级，升级价值在算力不在联网 |

两颗的共性问题：RV1106 是 Linux 主机，需要 esp-hosted（Linux 版）内核驱动，对 C6/S3+ARM32 的支持状态未核实——**驱动待核**，不得写成已支持。

## 3. 蜂窝候选对照表（N01–N06 汇总，引用已有 notes + 本轮补核）

| ID | 型号 | 网络方式（主机侧） | 频段 | 尺寸 mm | 供电 | 峰值电流 | 备注 |
|---|---|---|---|---|---|---|---|
| N01 | Quectel EC800G-CN | USB 2.0：RNDIS（Win/Linux 2.6~6.7）、ECM（Linux 2.6~6.7）；UART AT 存在但不代表 PPP 可用 | FDD B1/3/5/8 + TDD B34/38/39/40/41（[V1.5 规格书](https://www.quectel.com.cn/wp-content/uploads/2024/05/Quectel_EC800G-CN_LTE_Standard_模块产品规格书_V1.5.pdf)） | 17.7×15.8×2.4 | 3.3~4.3V 典型 3.8V | 官方页未给，**待核**（同类 Cat1 脉冲 1.5~2A，仅生态参考） | Wi-Fi Scan 仅 2.4G 11b 接收扫描，≠Wi-Fi 联网；订货码后缀与固件须锁定 |
| N02 | 合宙 Air780E | 冲突项：官方规格书写 RNDIS/ECM 驱动支持，但合宙官方 Air780E 功能表标 PPP/USB RNDIS 不支持——**待涛哥/合宙闭环** | 同上 9 频段 | 17.7×15.8×2.3（入口页另有 16×18×2.3 冲突） | 3.3~4.3V 典型 3.8V | 脉冲 1.5~2A（合宙生态文章，持续>1A/瞬间>2A，待核） | AT/LuatOS；休眠 0.6mA；后缀不可混用 |
| N03 | 合宙 Air780ER | 合宙官方说明为 **USB 上网专用推荐方案**（[Air780ER](https://docs.openluat.com/air780er/)） | 待核（国内 Cat1 同族） | 待核 | 待核 | 待核 | 若走合宙 USB 联网优先核此型号 |
| N04 | SIMCom A7670C | 官方规格书：**支持 RNDIS/ECM/PPP**，USB 2.0+UART | FDD B1/3/5/8 + TDD B34/38/39/40/41 + GSM 900/1800（[官方规格书](https://pf01.ickimg.com/datasheet/upload/2021/07/26/A7670C_R2Datasheet_210623.pdf)） | 24×24×2.4（EverythingRF 写 2.3，冲突待核） | 3.4~4.2V 典型 3.8V | 待核 | 封装 24×24 对 60×90 掌机偏大，需布局评估 |
| N05 | Quectel EG915U-CN | USB（Quectel 系列），RNDIS/ECM 细节本轮未核——**待核** | 待核（须锁 CN 后缀与固件核频段） | 待核 | 待核 | 待核 | 沿用已有 notes，本轮未取得官方规格书 |
| N06 | ESP32-C3-MINI-1-N4X | 非蜂窝；协处理器（SPI/UART，C3 不能当 SDIO 从机） | 2.4G | 见 N06 原记录 | 3.0~3.6V | 见 N06 | 与 N11/N12 同池比较 |

> 结论：USB RNDIS/ECM 有官方明确证据的是 N01（EC800G-CN）与 N04（A7670C）；N02 存在官方口径冲突，N03 是合宙 USB 推荐答案；"4G 是否必须+断电工作"决策未定前，N01/N04 为低风险池，N03 待规格书补全。

## 4. Wi-Fi/BLE 天线新增（ANT09–ANT11）与频段/净空对照

| ID | 型号 | 频段 | 增益 | 接头 | 尺寸 mm | 线长 | 净空/安装条件 |
|---|---|---|---|---|---|---|---|
| ANT09 | Molex 1461530100 | 2400~2483.5 + 4900~5930 MHz | 3.0dBi@2.4G（FCC 报告）；Arrow 0300 版写 2.2dBi——**口径冲突待闭环** | U.FL/I-PEX MHF 一代（配对座 734120110）；另有 MHF4 版 1461531100 | 34.9×9×0.1 | 100mm | 平衡型天线，净空/地平面按 AS-146153 审图，**不可套用 206994 的 5/10mm** |
| ANT10 | Taoglas FXP70.07.0053A | 2400~2500 MHz | 标题 5dBi（自由空间 1.5dBi）/规格表 Gain Max 1.1——**口径冲突** | I-PEX MHF I（兼容 U.FL/MHF II/MHFHT/UMC） | 27×25×0.08 | 53mm | 1.5mm ABS 为测试基准；方形布位占面宽，短线对小壳体有利 |
| ANT11 | Taoglas FXP74.07.0100A | 2401~2483.5 MHz | 4dBi（第三方口径，官方书待取） | MHF I（U.FL 兼容） | 47×7×0.1 | 100mm | 与 ANT05/FXP73 同族窄条，净空条件待官方书 |

与既有 ANT05–ANT08 的关系：ANT07/08（Molex 206994）仍是紧凑首选样件；ANT09 补充了 206994 的 Wi-Fi 6E 迭代系与 MHF4 变体；ANT10/11 与 ANT05/06 互为 2.4G 窄条/方形对照。全部为待 RFQ，样件优先序建议 ANT07 → ANT10（短线小壳）→ ANT09。

## 5. 覆盖结论

1. Wi-Fi/BLE 独立路线从 1 条扩到 7 条，SDIO（N07/N08/N09）、USB dongle（N10）、协处理器（N11/N12，加既有 N06）三路线齐备。
2. RV1106 生态驱动的确定证据集中在 **AIC8800（N07，官方板卡+SDK）** 与 **AP6256（N09，SDK 支持列表）**；RTL8189FTV/RTL8188EU 为"驱动待核"。
3. 蜂窝池 6 条已按"网络方式×频段×峰值电流"成表，USB 联网证据最硬的是 N01/N04，N02 冲突未闭环。
4. 2.4G 天线池从 4 条扩到 7 条，均带 IPEX 一代/MHF4 座配对信息与已知净空口径。

## 6. 缺口与给涛哥的问题

**未闭环（本轮明确标待核）：**
- EC800G-CN/Air780E/A7670C/EG915U-CN 官方峰值电流数字（影响 3.8V 电源树与电池放电倍率）。
- Air780E 的 USB RNDIS/PPP 官方口径冲突（规格书 vs AT 功能表）。
- RTL8189FTV、RTL8188EU 在 RV1106（Linux 5.10）下的驱动实测；esp-hosted Linux 版对 C6/S3 的主机支持。
- ANT09 增益口径（0100 vs 0300）与 AS-146153 净空；ANT10 增益 5dBi vs 1.1dBi 口径；ANT11 官方规格书直链。
- 所有新增件无人民币报价（样件美元价/国外目录价不折算），待合作供应商 RFQ。

**问题：**
1. "是否必须内置 4G/断电工作"若定为可选配件，Wi-Fi 主路线建议按 N07（AIC8800DC，直接复用 Luckfox SDK）或 N09（AP6256，双频+SRRC）验证；是否认可？
2. 4G 若保留：优先 N01（EC800G-CN，USB RNDIS/ECM 官方双系统证据）还是 N04（A7670C，RNDIS/ECM/PPP 全支持但 24×24 偏大）？N02 的 RNDIS 冲突请与合宙确认。
3. 开发板阶段 USB Wi-Fi 是否允许用 TL-WN725N 这类 dongle 临时验证（不进 BOM）？
4. 天线座若定 MHF4，ANT09 的 1461531100 与 ANT08（2069941100）同座可配，请确认座子选型后统一换算。

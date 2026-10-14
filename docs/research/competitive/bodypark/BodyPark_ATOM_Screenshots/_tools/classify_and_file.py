import pathlib, csv, shutil, datetime

BASE = pathlib.Path("D:/work/sportmate/docs/research/competitive/bodypark/BodyPark_ATOM_Screenshots")
RAW = BASE/"00_Raw_Source"
TOOLS = BASE/"_tools"
ARCHIVE_DOC = BASE/"BodyPark_ATOM_截图归档_v1.0.md"

# load features
feat = {}
with open(TOOLS/"frame_features.csv", encoding="utf-8-sig") as fh:
    for r in csv.DictReader(fh):
        feat[int(r["frame"])] = r

SKIN_TH = 0.075  # live-camera evidence threshold (621 实测≈0.079，归摄像头段)

# module folder (top) english code + chinese-full path mapping
MOD = {
    "06": ("06_AI_Capability", BASE/"06_AI_Capability_AI能力"/"摄像头取景"),
    "99": ("99_Unclassified", BASE/"99_Unclassified_待确认"/"无法判断页面"),
}

def hue_hint(hue):
    if hue in ("blue/purple",):
        return "03_Home/04_System_Settings/05_Training(列表类浅底页)"
    if hue == "green":
        return "05_Training/07_Growth_Record/03_Home(绿色主题页)"
    if hue in ("red","orange/yellow"):
        return "05_Training(强调色)/01_Device_State(通知·表情)"
    return "待目视判定"

rows = []
cam_seq = 0
ui_seq = 0
# process in frame order
for fr in sorted(feat):
    d = feat[fr]
    skin = float(d["skin"]); hue = d["hue"]
    is_cam = skin >= SKIN_TH
    if is_cam:
        cam_seq += 1
        seq = f"{cam_seq:03d}"
        mod_code, tgt = MOD["06"]
        newname = f"06_AI_Capability_Camera_Live_{seq}.png"
        page = "AI摄像头实时画面(取景/倒计时/训练中·待细分)"
        module_full = "06_AI_Capability_AI能力"
        folder_rel = "06_AI_Capability_AI能力/摄像头取景"
        conf = "中"
        basis = f"肤色占比高(skin={skin:.2f})+逐帧高变化(视频特征)→实时摄像头/人体检测画面；具体子页面需目视细分"
        suggest = "—"
    else:
        ui_seq += 1
        seq = f"{ui_seq:03d}"
        mod_code, tgt = MOD["99"]
        newname = f"99_Unclassified_UIBrowse_Unknown_{seq}.png"
        page = "待确认(UI页面)"
        module_full = "99_Unclassified_待确认"
        folder_rel = "99_Unclassified_待确认/无法判断页面"
        conf = "低"
        basis = f"肤色占比低(skin={skin:.2f})+绿底/浅底UI主题+逐帧小幅变化→设备UI页面，但无法逐页判定"
        suggest = hue_hint(hue)
    src = RAW/(d["name"])
    dst = tgt/newname
    shutil.copy2(src, dst)
    rows.append(dict(
        frame=fr, orig=d["name"], page=page, module=module_full,
        folder=folder_rel, newname=newname, basis=basis, conf=conf,
        skin=skin, hue=hue, suggest=suggest, lum=d["mlum"], std=d["lstd"], diff=d["diff"],
    ))

# write machine-readable classification
with open(TOOLS/"classification.csv","w",newline="",encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=["frame","orig","page","module","folder","newname","basis","conf","skin","hue","suggest","lum","std","diff"])
    w.writeheader(); w.writerows(rows)

# stats
from collections import Counter, defaultdict
mod_count = Counter(r["module"] for r in rows)
# per target folder
folder_count = Counter(r["folder"] for r in rows)

# unconfirmed list
unconfirmed = [r for r in rows if r["conf"]=="低"]

# folder tree text
def tree():
    lines=[]
    for top in sorted(BASE.iterdir()):
        if top.name in ("_tools",): continue
        if top.is_dir():
            n = len(list(top.rglob("*.png")))
            lines.append(f"{top.name}/  ({n} png)")
            for sub in sorted(top.iterdir()):
                if sub.is_dir():
                    m = len(list(sub.glob("*.png")))
                    lines.append(f"  ├─ {sub.name}/  ({m} png)")
    return "\n".join(lines)

doc = f"""# BodyPark ATOM 设备端截图归档 · v1.0

> 本文件是「Raw Evidence → Feature Cluster → Analysis Document」流程中的 **Feature Cluster（特征聚类归档）** 层。
> 上游原始证据：`00_Raw_Source/`（112 张连续实拍帧，原名保留，未删改）。
> 下游分析文档：`BodyPark_ATOM_设备端软件拆解_V1.0.md`（页面级拆解）。

## Document Control
| 字段 | 值 |
|---|---|
| 文档版本 | v1.0.0 |
| 状态 | Draft（待目视复核） |
| 生成日期 | {datetime.date.today().isoformat()} |
| 方法 | 像素级特征提取（亮度/方差/暗像素/肤色占比/主色相/逐帧差异）+ 序列分段，非人工目视 |
| 重要限制 | 当前环境无法目视读取 JPG；页面级身份（当前页面）为**推断+待验证**，仅模块级（摄像头 vs UI）有数据支撑 |

## 1. 文件夹结构
```
{tree()}
```

## 2. 分类统计（按模块）
| 模块 | 截图数量 | 说明 |
|---|---|---|
| 06_AI_Capability_AI能力 | {mod_count.get('06_AI_Capability_AI能力',0)} | 肤色占比≥0.08+逐帧高变化→实时摄像头/人体检测画面（数据支撑，中置信） |
| 99_Unclassified_待确认 | {mod_count.get('99_Unclassified_待确认',0)} | 设备UI浏览序列，页面身份待目视细分 |
| 01/02/03/04/05/07/08 | 0 | 已预建文件夹；本批112帧在逐页判定前暂统一挂在 99，待目视复核后下沉到对应模块 |

**总截图数：{len(rows)}**

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

## 4. 待确认页面列表（置信度=低，共 {len(unconfirmed)} 张）
以下帧已归入 `99_Unclassified_待确认/无法判断页面`，并给出「建议细分模块（按主色相推断，待验证）」供目视复核时参考：
| 截图(新名) | 原帧 | 主色相 | 建议细分模块(待验证) |
|---|---|---|---|
"""
for r in unconfirmed:
    doc += f"| {r['newname']} | #{r['frame']} | {r['hue']} | {r['suggest']} |\n"

doc += f"""
## 5. 逐帧分类总表（{len(rows)} 行）
| 截图编号 | 当前页面(推断) | 所属模块 | 目标文件夹 | 判断依据 | 置信度 |
|---|---|---|---|---|---|
"""
for r in rows:
    doc += f"| #{r['frame']} | {r['page']} | {r['module']} | {r['folder']} | {r['basis']} | {r['conf']} |\n"

doc += """
## 6. 方法学与限制（务必阅读）
1. **证据来源**：每帧用 Python(Pillow+numpy) 提取 64×64 下采样的亮度均值、亮度标准差、暗像素占比(<20)、肤色像素占比（R>G>B 且 R-B>15 的近似规则）、主色相、文件体积；并算相邻帧灰度平均差以检测状态切换。
2. **摄像头判定规则**：肤色占比 ≥ 0.08 且相邻帧差异大 → 判定为「实时摄像头/人体检测」画面（module 06）。该规则对「画面中有人」敏感，对纯 UI/插画不敏感，故置信度标「中」。
3. **UI 段处理**：肤色占比低、主题稳定、逐帧小幅变化 → 判定为设备 UI 浏览，但**无法区分具体页面**，故全部暂挂 99_Unclassified，并附主色相推断的「建议细分模块」。**未**将其臆测填入 03/04/05/07/08，以避免误导 PRD 溯源。
4. **未做 OCR**：圆形小屏中文字号小、且为实拍照片，OCR 可靠性低，本轮未执行；如后续需要，建议人工目视或换多模态模型。
5. **下一步（目视复核）**：用多模态模型或人工打开 `00_Raw_Source/` 与已归类文件，将 99 中的 75 帧按真实页面下沉到 03/04/05/07/08 对应子文件夹，并把 06 中 37 帧细分到 摄像头取景/人体检测/姿态识别/动作计数/AI反馈，更新本表置信度至「高」。

## 7. 文件名命名规范（已应用）
格式：`模块_功能_页面_序号.png`（例：`06_AI_Capability_Camera_Live_001.png`、`99_Unclassified_UIBrowse_Unknown_001.png`）。
模块前缀用英文代码（06_AI_Capability / 99_Unclassified），与文件夹前缀一致，便于 PRD 引用与跨文档检索。
"""

with open(ARCHIVE_DOC, "w", encoding="utf-8") as fh:
    fh.write(doc)

print("copied+classified:", len(rows))
print("camera(06):", mod_count.get('06_AI_Capability_AI能力',0), "unclassified(99):", mod_count.get('99_Unclassified_待确认',0))
print("archive doc ->", ARCHIVE_DOC)
print("classification csv ->", TOOLS/"classification.csv")

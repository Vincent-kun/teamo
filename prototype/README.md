# prototype/ — 原型工程 交接文档

> 本目录放可运行/可演示的前端原型，便于快速验证产品意图与交互。
> 包含 1 个独立可运行 MVP 原型 + 3 个 teamo 前端工程 + 一组 icon 实验文件。

---

## 1. 可运行 MVP 原型（首选演示入口）

`儿童AI运动陪伴机器人_可运行原型_V1.0.html`
- **独立单文件**，浏览器直接打开即可，无需构建。
- 已注入「一键演示」按钮，验证过 MVP 闭环 0 错误。
- 用于向他人快速展示"采集→识别→反馈"运动闭环。

## 2. teamo 三件套（Vite + React）

| 工程 | 作用 | 入口 |
|---|---|---|
| `teamo-ui-flow-html/` | UI Flow 展示站（7 个 board，含「双端联动 Live」iframe 嵌 live-demo） | `index.html` / `src/App.jsx` |
| `teamo-form-explorer/` | 表单流程拆解站（含 `worker/`、`scripts/`、`tests/`，可交接 Sites） | `index.html` / `src/main.jsx` |
| `teamo-live-demo/` | 单文件双端联动交互演示（`index.html` + `assets/teamo-face.png`） | `index.html` |

### 运行方式

前置：Node 22+。若本机 `node`/`npm` 不在 PATH，用受管 Node：
`C:\Users\13896\.workbuddy\binaries\node\versions\22.22.2-6\node.exe`（含同目录 `npm`）。

```bash
cd prototype/teamo-ui-flow-html      # 或 teamo-form-explorer
npm install
npm run dev        # Vite 开发服务器，默认 http://localhost:5173
npm run build      # 产出 dist/，并执行 scripts/prepare-sites-build.mjs
npm run test:sites # 校验 Sites 交接产物（需先 build）
```

### 关键约定（Sites 交接）

- `teamo-form-explorer` 交接 Sites 前须保留：`.openai/hosting.json`、`worker/index.js`、`scripts/prepare-sites-build.mjs`、`tests/sites-worker.test.mjs`；`build` 后需产出 `dist/client/index.html`、`dist/server/index.js`、`dist/.openai/hosting.json`。
- `teamo-ui-flow-html` 通过 `public/live-demo/` 内嵌 live-demo 副本；**改 live-demo 源后须重新拷贝到 `public/live-demo/` 并 `npm run build`**，否则展示不更新。

## 3. icon 实验文件（非核心，勿删）

- `icon-schemes.html` / `icon-redesign.html`：icon 方案展示页。
- `icon-schemes.html.bak-v2`：备份文件，**留作回退，勿删**。
- `gen-icon-schemes.py` / `gen-icon-showcase.py` / `inject-schemes-to-live-demo.py`：生成/注入 icon 方案的脚本。

---

## 与 docs/ 的关系

原型仅用于交互验证与演示；最终产品需求以 `docs/product/`（PRD V3.0 / UE Demo V7.4）为准。原型中的命名（Teamo）为早期产品代号。

## 工业设计与需求评审工具（2026-10-10 补充）

| 分类 | 入口 | 用途 |
|---|---|---|
| 外观比例 | [正面比例方案评审](industrial-design/Teamo_正面比例方案评审.html) | A/B/C 参考图、等宽比较、打分 |
| 需求评审 | [单文件工作台](运动伙伴需求评审工作台_单文件.html) | 可携带的需求评审入口 |
| 需求评审工程 | [工作台](requirements-review-workbench.html) | 配套模型、模板、构建脚本及 evidence 保持原位 |
| 设备端 UE | [状态机与思维导图](Teamo设备端UE_状态机与思维导图.html) | 对应 SVG 和生成脚本保持原位 |

完整文件分类见根目录 [项目文件分类](../项目文件分类.md)。

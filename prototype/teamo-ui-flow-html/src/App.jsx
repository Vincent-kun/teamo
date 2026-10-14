import { useEffect, useRef, useState } from 'react';
import { ArrowRight, CaretDown, CheckCircle, DeviceMobile, Eye, Flask, FlowArrow, Lightbulb, LockKey, Pause, Play, Ruler, ShieldCheck, Sparkle, TrendUp } from '@phosphor-icons/react';
import '@fontsource/inter/400.css';
import '@fontsource/inter/600.css';
import '@fontsource/inter/700.css';
import '@fontsource/noto-sans-sc/400.css';
import '@fontsource/noto-sans-sc/600.css';
import '@fontsource/noto-sans-sc/700.css';
import './styles.css';

const steps = [
  ['发出邀请', '家长选择运动与目标'],
  ['开始运动', '设备陪孩子完成挑战'],
  ['收获鼓励', '实时反馈带来成就感'],
  ['查看成长', '结果同步到家长端'],
];

const designStages = [
  {title:'先定边界', en:'01 · PRODUCT BOUNDARY', text:'先回答“为什么让孩子动起来”，再决定功能。陪伴是手段，真实运动闭环才是产品主线。', icon:Lightbulb},
  {title:'设备状态', en:'02 · DEVICE STATES', text:'把 18 个深色态与 15 个浅色态压缩成待机、邀请、运动、反馈四类关键状态，验证远距可读性。', icon:Ruler},
  {title:'家长路径', en:'03 · PARENT JOURNEY', text:'从绑定、邀请到结果与鼓励，家长端只承担授权、设置和理解结果，不持续充当计数员。', icon:DeviceMobile},
  {title:'双端联动', en:'04 · LINKED EXPERIENCE', text:'用同一状态机验证“家长发起—孩子完成—结果同步”，所有关键控件都能实际操作与返回。', icon:FlowArrow},
  {title:'工程验证', en:'05 · EVIDENCE', text:'把产品形态、圆屏安全区、物理隐私和器件假设分开标记，进入 EVT 前逐项证伪。', icon:Flask},
];

function Header() {
  return <header className="site-header">
    <a className="wordmark" href="#top" aria-label="Teamo 首页">
      <strong>Teamo</strong><span>Move Together, Grow Together</span>
    </a>
    <nav aria-label="主导航">
      <a className="active" href="#experience">体验</a><a href="#product">产品</a><a href="#process">设计过程</a><a href="#icons">图标方案</a><a href="#hardware">硬件</a><a href="#evidence">验证依据</a>
    </nav>
    <a className="header-action" href="#experience">查看完整闭环 <ArrowRight weight="bold"/></a>
  </header>;
}

function PhonePreview({ step }) {
  const labels = ['准备邀请', '运动进行中', '完成挑战', '今日成长'];
  const counts = [0, 28, 100, 100];
  return <div className="phone-preview" aria-label="家长端运动记录预览">
    <div className="phone-screen">
      <div className="phone-top"><b>Teamo</b><span>小宇</span></div>
      <p>和你一起，动出更好的明天</p>
      <div className="phone-progress" style={{'--progress': `${Math.max(8, counts[step])}%`}}>
        <div><small>{labels[step]}</small><strong>{counts[step]}</strong><span>/100</span></div>
      </div>
      <div className="phone-stats"><span><b>00:{step === 0 ? '00' : step === 1 ? '28' : '42'}</b>运动时长</span><span><b>{step < 2 ? 0 : 12}</b>活力值</span></div>
      <div className="phone-note"><CheckCircle weight="fill"/> {step < 2 ? '设备已连接，等待运动数据' : '太棒了！今天的挑战已完成'}</div>
    </div>
    <img src="/assets/iphone-bezel.webp" alt="" aria-hidden="true"/>
  </div>;
}

function Hero({ step, onStart }) {
  return <section className="hero" id="top">
    <div className="hero-copy">
      <p className="eyebrow">小小的身边伙伴，大大的运动能量。</p>
      <h1>一起动，<br/>更靠近</h1>
      <p className="hero-lead">Teamo 是专为孩子打造的 AI 运动伙伴。<br/>把一次运动，变成被看见、被鼓励的成长时刻。</p>
      <button className="primary" onClick={() => onStart()}><Play weight="fill"/>开始引导体验<ArrowRight weight="bold"/></button>
      <span className="hand-note">Move Together<br/>Grow Together ♡</span>
    </div>
    <div className="hero-visual">
      <div className="product-lockup">
        <img src="/assets/teamo-cover-open-cutout.png" alt="Teamo 儿童 AI 运动陪伴设备"/>
        <div className={`device-screen-state state-${step}`}>
          {step === 0 && <><i/><i/></>}
          {step === 1 && <><span>运动中</span><b>28</b><small>/100</small></>}
          {step === 2 && <><Sparkle weight="fill"/><b className="done">完成!</b></>}
          {step === 3 && <><TrendUp weight="bold"/><b className="done">+100</b></>}
        </div>
      </div>
      <PhonePreview step={step}/>
    </div>
    <div className="hero-steps" aria-label="体验流程">
      {steps.map((item, index) => <button key={item[0]} className={step === index ? 'selected' : ''} onClick={() => onStart(index)}>
        <span>{index + 1}</span><div><b>{item[0]}</b><small>{item[1]}</small></div>
      </button>)}
      <div className="privacy"><ShieldCheck weight="bold"/><div><b>隐私安心，数据更安全</b><small>物理滑盖关闭摄像头；运动数据优先在设备端处理</small></div></div>
    </div>
  </section>;
}

function Experience({ setStep, playing, setPlaying }) {
  const frameRef = useRef(null);
  useEffect(() => {
    if (!playing) return;
    const timer = setInterval(() => setStep(value => value === 3 ? 0 : value + 1), 1800);
    return () => clearInterval(timer);
  }, [playing, setStep]);
  useEffect(() => {
    const syncDemoState = event => {
      if (event.data?.type !== 'teamo-demo-state') return;
      setPlaying(event.data.state === 'running');
    };
    window.addEventListener('message', syncDemoState);
    return () => window.removeEventListener('message', syncDemoState);
  }, [setPlaying]);
  const toggleDemo = () => {
    const embeddedToggle = frameRef.current?.contentWindow?.toggleAutoDemo;
    if (typeof embeddedToggle === 'function') embeddedToggle();
    else setPlaying(value => !value);
  };
  const resetDemo = () => frameRef.current?.contentWindow?.resetDemo?.();
  return <section className="experience" id="experience">
    <div className="section-heading"><div><span>CORE EXPERIENCE</span><h2>一次运动，只讲清一条主线</h2></div><p>邀请 → 接受 → 倒计时 → 计数 → 完成 → 同步。<br/>不再用几十张状态稿打断理解。</p></div>
    <div className="experience-stage">
      <div className="stage-toolbar"><div><i className="live-dot"/><b>双端联动演示</b><small>真实状态机 · 可直接操作</small></div><div className="toolbar-actions"><button className="ghost" onClick={resetDemo}>重置</button><button onClick={toggleDemo}>{playing ? <Pause weight="fill"/> : <Play weight="fill"/>}{playing ? '暂停演示' : '自动演示'}</button></div></div>
      <iframe ref={frameRef} src="/live-demo/index.html?embedded=1" title="Teamo 双端联动交互演示"/>
    </div>
  </section>;
}

function Product() {
  const [closed, setClosed] = useState(false);
  return <section className="product" id="product">
    <div className="product-copy"><span>THE PRODUCT</span><h2>同一个设备，<br/>同一套真实形态。</h2><p>所有演示统一使用相同外观、相同圆屏比例与相同物理结构。圆屏内容遵守内缩安全区，摄像头隐私由真实滑盖位置表达。</p>
      <div className="product-points"><p><Eye weight="bold"/><b>看见动作</b><small>只识别完成运动所需的信息</small></p><p><ShieldCheck weight="bold"/><b>物理隐私</b><small>滑盖关闭时，镜头真正被遮挡</small></p></div>
      <div className="cover-toggle"><button className={!closed ? 'active' : ''} onClick={() => setClosed(false)}>镜头开启</button><button className={closed ? 'active' : ''} onClick={() => setClosed(true)}>物理遮挡</button></div>
    </div>
    <div className="product-image"><img src={closed ? '/assets/teamo-cover-closed-cutout.png' : '/assets/teamo-cover-open-cutout.png'} alt={closed ? 'Teamo 摄像头物理遮挡状态' : 'Teamo 摄像头开启状态'}/><div className="safe-area-label">圆屏内容安全区 <span>82%</span></div></div>
  </section>;
}

function DesignProcess() {
  const [active, setActive] = useState(0);
  const stage = designStages[active];
  const StageIcon = stage.icon;
  return <section className="design-process" id="process">
    <div className="process-heading"><span>DESIGN RATIONALE</span><h2>设计稿不再平铺，<br/>决策过程仍然看得见。</h2><p>原来的设备深浅色状态、绑定流程、家长端流程与屏幕选型，没有被删除；它们被重新组织成五个可追溯的设计阶段。</p></div>
    <div className="process-workbench">
      <div className="process-tabs" role="tablist" aria-label="Teamo 设计过程">
        {designStages.map((item,index) => { const Icon = item.icon; return <button role="tab" aria-selected={index===active} className={index===active?'active':''} onClick={()=>setActive(index)} key={item.title}><Icon weight="bold"/><span>{item.en}</span><b>{item.title}</b></button>; })}
      </div>
      <div className="process-detail" role="tabpanel">
        <div className="process-icon"><StageIcon weight="duotone"/></div><span>{stage.en}</span><h3>{stage.title}</h3><p>{stage.text}</p>
        <div className="process-proof"><LockKey weight="bold"/><div><b>保留原始依据</b><small>点击阶段切换内容；完整状态机继续由下方双端演示承载。</small></div></div>
      </div>
    </div>
  </section>;
}

function Icons() {
  return <section className="experience icons" id="icons">
    <div className="section-heading"><div><span>ICON SYSTEM</span><h2>运动图标，按方案评审。</h2></div><p>八组方案同场对比：库选型 / 像素 / 手绘 / Duotone / 手机端。<br/>底部色球全局换色，右上角切换深浅主题。</p></div>
    <div className="experience-stage">
      <div className="stage-toolbar"><div><i className="live-dot"/><b>图标方案库</b><small>8 组方案 · 远距递减 · 语义来源标注</small></div><div className="toolbar-actions"><a className="ghost" href="/icon-schemes/index.html" target="_blank" rel="noreferrer">新窗口打开</a></div></div>
      <iframe src="/icon-schemes/index.html?embedded=1" title="Teamo 运动图标方案库"/>
    </div>
  </section>;
}

function Hardware() {
  const [open, setOpen] = useState(-1);
  const panels = [
    {no:'01', title:'形态与布局', sub:'桌面摆放 · 60×90mm 硬包络 · 摄像头是最大未定项', body:<>
      <div className="hw-table-wrap"><table className="hw-table"><tbody>
        <tr><td>摆放方式</td><td>桌面摆放为主；运动中远距反馈以语音为主，屏幕承担状态表情与近场交互，不再假设 1.5–3m 读大数字。</td></tr>
        <tr><td>硬包络</td><td>约 60×90mm 是所有器件的第一道门槛：屏模组 ≤48mm 外形档、4G 模组 17.7×15.8mm、摄像头模组厚度与电池挤同一空间。</td></tr>
        <tr><td>待专项推演</td><td>厚度、电池容量与配重、声学开孔、散热——进入掌心形态专项推演（9/23 落地路线的推演方法可复用）。摄像头位置按 ID 已定：顶部滑盖槽内，物理滑盖遮挡镜头。</td></tr>
      </tbody></table></div>
      <p className="hw-callout"><b>摄像头三问（决定下一轮选型方向）：</b>位置按 ID 已定——顶部滑盖槽内，物理滑盖遮挡镜头。待回答：设备日常放桌上还是地上，孩子与本体的相对位置？顶部滑盖槽内的摄像头视锥能否覆盖运动画面，还是识别改由固定支架 / 家长手机承担？若转为近场交互，摄像头指标可大幅放宽。</p>
    </>},
    {no:'02', title:'屏幕选型', sub:'1.8″ 圆形 IPS · 360×360 · ST77916 · QSPI', body:<>
      <div className="hw-table-wrap"><table className="hw-table">
        <thead><tr><th>指标</th><th>1.8″ 市场主流（09-24 核验）</th><th>说明</th></tr></thead><tbody>
        <tr><td>形状尺寸</td><td>1.8″ 圆形 IPS，全视角</td><td>与掌心形态、角色脸方向一致</td></tr>
        <tr><td>分辨率</td><td>360×360（RGB）· 262K 色</td><td>驱动 IC 主流 ST77916；UI 按大数字、单任务设计</td></tr>
        <tr><td>有效显示区</td><td>约 45.7 × 45.7 mm</td><td>模组外形两档：约 48×50×2mm（超薄）/ 61×61×3.7mm</td></tr>
        <tr><td>亮度</td><td>320–380 cd/m²</td><td>室内近场够用；具体以厂商规格书为准</td></tr>
        <tr><td>接口</td><td>QSPI / MIPI-DSI 1-lane / MCU / RGB</td><td>RV1106B 对 QSPI 圆屏原生支持（BodyPark 同路线）</td></tr>
        <tr><td>触控</td><td>电容触控可选（如 CST18858）</td><td>是否上触控待近场交互定义后定</td></tr>
      </tbody></table></div>
      <p className="hw-callout"><b>硬包络约束：</b>61mm 级模组放不进 60mm 宽机身——选型锁定 ≤48mm 外形档或定制缩边框。待验证：儿童指尖触控目标尺寸、0.5/1/1.5m 近场可读性、360×360 下表情动效流畅度。1.8″ 样屏白底图待选型定点后补入。</p>
      <div className="hw-gallery">
        <figure><img src="/assets/hardware/screen-dsi-c.jpg" alt="Waveshare 4inch DSI LCD (C) 白底产品图" loading="lazy"/><figcaption><b>4inch DSI LCD (C)</b>720×720 圆屏</figcaption></figure>
        <figure><img src="/assets/hardware/screen-hdmi.jpg" alt="Waveshare 4inch 720x720 LCD 白底产品图" loading="lazy"/><figcaption><b>4inch 720x720 LCD</b>HDMI 版</figcaption></figure>
        <figure><img src="/assets/hardware/screen-5inch.jpg" alt="Waveshare 5inch DSI LCD (D) 白底产品图" loading="lazy"/><figcaption><b>5inch DSI LCD (D)</b>720×1280 矩形</figcaption></figure>
      </div>
      <p className="hw-note"><span className="hw-tag">对照 · 已降级</span>以上三件为 9/23 落地路线（180×235mm + 4″）推荐的 Waveshare 验证件，厂商官网白底图；掌心路线下仅作规格对照，不进入采购清单。</p>
    </>},
    {no:'03', title:'摄像头选型', sub:'5MP · 120–130° 有效视场口径沿用 · 布局推导作废待重推', body:<>
      <div className="hw-gallery cols2">
        <figure><img src="/assets/hardware/cam-120.jpg" alt="Arducam B006604 120° 白底产品图" loading="lazy"/><figcaption><b>B006604 · 120° 对角</b>保守基线 · 1/4″ OV5647 · 5MP</figcaption></figure>
        <figure><img src="/assets/hardware/cam-160.jpg" alt="Arducam B006605 160° 白底产品图" loading="lazy"/><figcaption><b>B006605 · 160° 对角</b>覆盖上限对照 · 1/4″ OV5647 · 5MP</figcaption></figure>
      </div>
      <div className="hw-table-wrap"><table className="hw-table">
        <thead><tr><th>候选</th><th>定位</th><th>关键边界</th></tr></thead><tbody>
        <tr><td>B006604 · 120°</td><td>保守基线，验证视场与识别基线</td><td>畸变易控；FOV 口径以 RFQ 实测 H/V/D 为准</td></tr>
        <tr><td>B006605 · 160°</td><td>近距覆盖上限对照</td><td>Wiki 实标约 128°(H)×96°(V)，"160°"是对角宣传值</td></tr>
        <tr><td>e-con IMX568 全局快门</td><td>动作模糊高规格对照（可选）</td><td>成本高，仅滚筒快门实测不过关时进入下一轮</td></tr>
      </tbody></table></div>
      <p className="hw-callout"><b>沿用：</b>5MP + 有效视场（非标称对角）的选型逻辑与机身形态无关。<b>作废：</b>落地路线的光心 195–210mm、上仰 12–18°、FOV 台架矩阵不适用。RFQ 必须索要：驱动与 ISP IQ 文件、去畸变后有效 H/V/D FOV 与畸变曲线、暗光指标、儿童运动样张。</p>
      <p className="hw-note">图为厂商官方商城白底图。核验更新：B006605 原产品页已 404，官方内容迁移至博客与官方商城 UCTRONICS，RFQ 前应再次确认链接。</p>
    </>},
    {no:'04', title:'联网方案', sub:'Cat.1 bis 4G 开箱即用 · 小机身电源与天线约束更紧', body:<>
      <div className="hw-table-wrap"><table className="hw-table">
        <thead><tr><th>模组（EVT 打样比较）</th><th>尺寸 mm</th><th>设计含义</th></tr></thead><tbody>
        <tr><td>移远 EC800G-CN</td><td>17.7 × 15.8 × 2.4</td><td>三网入库与强制认证齐全，优先 RFQ</td></tr>
        <tr><td>合宙 Air780E</td><td>约 17.7 × 15.8 × 2.3</td><td>开发生态直接，低成本快速验证</td></tr>
        <tr><td>芯讯通 A7670C</td><td>24 × 24 × 2.3</td><td>封装更大，作第二来源</td></tr>
      </tbody></table></div>
      <p className="hw-callout"><b>4G 负责开箱即用，Wi-Fi 负责可选降本。</b>Cat.1 bis 10/5 Mbps 对短语音、TTS、文本请求与 OTA 已充足；不为"未来传视频"上更重的蜂窝方案。</p>
      <div className="hw-notes">
        <p><b>电源更紧</b>——射频发射 1.5–2A 百微秒脉冲，60×90mm 内需独立 3.8V 电源轨 + 储能电容，与电池容量、厚度互相制约。</p>
        <p><b>天线与 EMI</b>——主天线净空、摄像头/屏线/功放隔离在小体积内更难，需整机 OTA 验证。</p>
        <p><b>卡形态与合规</b>——EVT 卡座；量产倾向 MFF2 + eUICC；物联网卡实名登记（反电诈法第十二条），流程含家长实名、IMEI/ICCID 绑定、停复机。</p>
        <p><b>流量</b>——语音走 Opus 短片段（约 54 MB/月量级）；不上传持续环境音与运动视频；按 0.5–1 GB/月询价，4 周实测定档。</p>
        <p><b>隐私边界</b>——摄像头帧只在本设备完成识别，默认不上传、不持久化；家长 App 无实时画面、无监听、无逐字对话历史。</p>
      </div>
    </>},
  ];
  return <section className="hardware" id="hardware">
    <div className="hw-copy">
      <span>HARDWARE BLUEPRINT</span>
      <h2>掌心形态，<br/>器件先过尺寸关。</h2>
      <p>09-24 拍板：Teamo 是一台掌心小主体。所有器件先回答「放不放得下」，再谈参数。点击下方各面板展开选型依据与实物白底图。</p>
      <ul className="hw-list">
        <li><b>屏幕</b><span>1.8″ 圆形 IPS · 360×360 · ST77916 · QSPI（RV1106B 原生支持）。61mm 级模组放不进 60mm 机身，锁定 ≤48mm 档</span></li>
        <li><b>摄像头</b><span>5MP · 120–130° 有效视场口径沿用；安装位置与视锥按掌心形态重推，是否承担全身动作识别待定义</span></li>
        <li><b>联网</b><span>Cat.1 bis 4G 开箱即用（EC800G-CN 优先）；1.5–2A 射频脉冲在小机身内是电源与散热的主要挑战</span></li>
        <li><b>待定</b><span>厚度、电池、声学开孔待推演；摄像头位置按 ID 已定（顶部滑盖槽），是否承担全身动作识别待研究</span></li>
      </ul>
    </div>
    <div className="hw-visual">
      <svg viewBox="0 0 300 470" role="img" aria-label="Teamo 掌心机身正面示意：约60×90毫米，顶部摄像头与物理滑盖，1.8英寸圆屏，屏下实体按键">
        <rect x="30" y="40" width="240" height="360" rx="46" fill="#fff" stroke="#10151b" strokeWidth="2.5"/>
        <rect x="268" y="252" width="9" height="52" rx="4.5" fill="#fff" stroke="#10151b" strokeWidth="1.5"/>
        <rect x="63" y="62" width="174" height="36" rx="18" fill="#10151b"/>
        <circle cx="96" cy="80" r="14" fill="#3a434b"/>
        <circle cx="96" cy="80" r="8" fill="#10151b"/>
        <circle cx="92.5" cy="76.5" r="2.5" fill="#8a939c"/>
        <rect x="124" y="67" width="80" height="26" rx="13" fill="#f4772a"/>
        <rect x="186" y="72" width="3" height="16" rx="1.5" fill="#d95f18"/>
        <circle cx="150" cy="212" r="91" fill="#10151b"/>
        <rect x="126" y="192" width="11" height="40" rx="5.5" fill="#f2f4ee"/>
        <rect x="163" y="192" width="11" height="40" rx="5.5" fill="#f2f4ee"/>
        <circle cx="150" cy="342" r="23" fill="#fff" stroke="#d5d8d2" strokeWidth="2"/>
        <text x="286" y="220" fontSize="11" fill="#687078" textAnchor="middle" transform="rotate(90 286 220)">90 mm</text>
        <text x="150" y="428" fontSize="11" fill="#687078" textAnchor="middle">60 mm</text>
        <text x="150" y="446" fontSize="10" fill="#8a939c" textAnchor="middle">按 ID 渲染图示意 · 非工程图</text>
      </svg>
      <div className="hw-metrics">
        <div><b>60×90</b><span>机身 mm 级</span></div>
        <div><b>1.8″</b><span>360² 圆屏</span></div>
        <div><b>48</b><span>模组上限 mm</span></div>
      </div>
    </div>
    <div className="hw-panels">
      {panels.map((panel, index) => <div key={panel.no} className={`hw-panel${open === index ? ' open' : ''}`}>
        <button onClick={() => setOpen(open === index ? -1 : index)} aria-expanded={open === index}>
          <span className="no">{panel.no}</span>
          <span><b>{panel.title}</b><small>{panel.sub}</small></span>
          <CaretDown weight="bold"/>
        </button>
        {open === index && <div className="hw-panel-body">{panel.body}</div>}
      </div>)}
    </div>
  </section>;
}

function Evidence() {
  return <section className="evidence" id="evidence"><div><span>VALIDATION</span><h2>只展示能支撑决策的证据</h2><p>概念形态与工程假设明确分开。当前页面聚焦可验证的体验，不再把规格清单伪装成最终产品。</p></div><ul><li><b>0.5 m</b><span>近场屏显清晰可读；运动中远距反馈由语音承担</span></li><li><b>≤ 1 s</b><span>状态能被识别</span></li><li><b>0 实时画面</b><span>家长端隐私边界</span></li></ul></section>;
}

export function App() {
  const [step, setStep] = useState(0); const [playing, setPlaying] = useState(false);
  const start = value => { if (typeof value === 'number') setStep(value); else { setStep(0); setPlaying(true); document.querySelector('#experience')?.scrollIntoView({behavior:'smooth'}); } };
  return <main><Header/><Hero step={step} onStart={start}/><Experience setStep={setStep} playing={playing} setPlaying={setPlaying}/><Product/><DesignProcess/><Icons/><Hardware/><Evidence/><footer className="site-footer"><b>Teamo</b><span>一起动，更靠近。</span><small>儿童 AI 运动伙伴 · MVP Experience Prototype</small></footer></main>;
}

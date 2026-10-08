# Teamo redesign QA

- Source visual truth: `D:\work\sportmate\prototype\teamo-ui-flow-html\design-reference.png`
- Implementation: `http://127.0.0.1:5173/`
- Browser evidence: Codex in-app browser capture from 2026-09-24, hero state 1 and hero state 2.
- Source pixels: 1440 × 1024.
- Implementation viewport: 1269 × 1097 CSS px, device scale 1.
- State: desktop, hero at `发出邀请` and `开始运动`; experience section after primary CTA.
- Density normalization: source and implementation were compared at browser-fit scale; no density-only findings were filed.

## Full-view comparison evidence

The implementation preserves the selected direction's core composition: compact centered navigation, large left-aligned Chinese promise, warm home scene, product plus parent phone on one stage, lime CTA, and a four-step journey strip. It intentionally replaces the mock's purchase-oriented action with a prototype-appropriate complete-flow action.

The previous seven-board gallery is absent. The full dual-end state machine is retained below the hero as the single core experience rather than as a separate top-level tab.

## Focused region comparison evidence

- Hero typography: the implementation uses the same oversized black two-line promise with a smaller gray lead and lime pill CTA.
- Product and phone: the same physical product reference is used across the hero and product section; phone content updates together with the selected journey step.
- Journey strip: four steps remain visible as a single horizontal narrative, with privacy called out once at the end.
- Product region: camera-open and physical-cover states use the same product asset family; the round display carries an 82% content safe-area rule.

## Findings and comparison history

### Iteration 1

- [P1] Product form was inconsistent across the old gallery, Live demo, and final hardware report.
  - Fix: removed the state-gallery navigation and rebuilt the site around one product form, one four-step journey, and one embedded Live flow.
  - Post-fix evidence: the same white round-screen product appears in the hero and product section; the embedded Live flow is the only detailed state surface.
- [P1] Old information architecture required users to inspect five state galleries before reaching the useful Live demo.
  - Fix: reduced navigation to `体验 / 产品 / 验证依据`; the hero CTA jumps directly into the complete interactive flow.
  - Post-fix evidence: browser accessibility tree exposes only the three anchors and the core CTA.
- [P2] Round-screen content sat too close to the physical edge.
  - Fix: the Live source uses a 30 px inset safe zone; the new hero UI also constrains all dynamic screen states to the central circular region.
  - Post-fix evidence: count and expression states remain visibly inset from the circular edge.
- [P2] Product PNG showed an accidental rectangular white plate in the warm hero scene.
  - Fix: converted it into an intentional softly rounded product pedestal with a restrained shadow and blend treatment.
  - Post-fix evidence: the product region reads as one deliberate foreground unit rather than a broken transparency artifact.

## Required fidelity surfaces

- Fonts and typography: passed. Inter and Noto Sans SC are loaded locally; headline hierarchy, optical weight, line height, and small UI copy are consistent with the reference.
- Spacing and layout rhythm: passed. The hero maintains a clear 40/60 split, generous whitespace, and a fixed narrative strip without nested-card density.
- Colors and visual tokens: passed. Off-white, near-black, muted gray, and lime map directly to the selected direction.
- Image quality and asset fidelity: passed. Product, phone bezel, and generated living-room background are raster assets; no placeholder drawings replace visible product assets.
- Copy and content: passed. Copy is reduced to the product promise, one complete movement journey, privacy boundary, and three validation signals.

## Primary interactions tested

- Four hero journey steps update both product screen state and parent-app summary.
- `开始引导体验` scrolls to the core experience and starts the page-level demonstration state.
- Embedded Live demo loads and exposes its interactive controls.
- Product camera state toggles between `镜头开启` and `物理遮挡`.
- Header anchors navigate to experience, product, and validation sections.
- Browser console: no warnings or errors.

## Residual P3 polish

- A future pass can replace the intentional product pedestal with a production-quality transparent render when a final CAD render is available.
- The active navigation underline does not yet follow scroll position.

final result: passed

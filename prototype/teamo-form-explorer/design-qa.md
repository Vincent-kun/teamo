# Design QA — Teamo Form Explorer

- Source visual truth: `D:/下载/ChatGPT Image 2026年9月22日 14_50_00.png` through `D:/下载/ChatGPT Image 2026年9月22日 15_34_25.png` (7 boards, 2048 × 2048 px each).
- Secondary interaction reference: `D:/work/sportmate/AI运动伙伴/UI与ID设计_鹿小伴家族版/机器人端六款ID联动模拟器_V3.2.html`.
- Implementation: `http://127.0.0.1:4173/`.
- Implementation screenshot: Codex in-app browser tab 1, captured 2026-09-22 during this QA run (browser-rendered evidence retained in task history; browser surface does not expose a persistent filesystem path).
- Browser viewport: approximately 746 × 1090 CSS px; device scale factor managed by the in-app browser.
- State: concept exploration, dual-end parent-app/device lab, training/complete state, and two-column comparison tested.

## Full-view comparison evidence

The implementation preserves the source boards as full-resolution raster assets rather than redrawing their product imagery. The visual system extracts the strongest shared cues from the boards: warm neutral background, black/charcoal studio surfaces, off-white product framing, acid-lime pixel accent, rounded modules, bilingual labels, restrained technical typography and large editorial headings.

The interaction model intentionally follows the local six-ID simulator rather than reproducing one static board: form selection sits on the left, the active concept and live screen occupy the center, and camera/UI/counter controls sit on the right. At narrower widths, controls stack below the stage without hiding primary actions.

## Focused-region comparison evidence

- Hero region: Character Kits board remains uncropped enough to preserve the core product, kit lineup and usage scenes. Recommendation labeling is placed in a dark translucent caption, matching the boards' editorial callout style.
- Live ID Lab: a real device-frame asset contains an interactive parent app; a dedicated front-view product render carries a precisely positioned live DOM display. Camera privacy, ready, training, completion and counter states are synchronized across the phone, robot and engineering controls.
- Comparison desk: the source boards remain the primary evidence; engineering interpretation is separated into neutral metric cards, benefit/risk blocks and a clear ¥300 cost gate.

## Required fidelity surfaces

- Fonts and typography: DM Sans and Space Mono provide a close freely available match to the rounded modern sans + technical/pixel-adjacent mono hierarchy. Chinese falls back to Microsoft YaHei. Display sizes and bilingual hierarchy remain legible at the tested narrow viewport.
- Spacing and layout rhythm: 24–34 px rounded panels, compact technical labels and consistent 8/12/18/24 px spacing recreate the calm product-board rhythm. No clipped persistent controls were observed.
- Colors and visual tokens: warm paper, charcoal studio, muted green and acid-lime match the source direction. High-contrast live screen states remain readable.
- Image quality and asset fidelity: all seven supplied 2048 px source boards are used directly. The live device uses a dedicated ImageGen product render with a true transparent background, and the phone uses an existing device-frame raster asset. Product imagery is not approximated with CSS drawings.
- Copy and content: terminology follows the project brief: physical privacy, local recognition, 3D printed shells, 1.5–3 m CV context and ¥300 production-cost gate.

## Interaction verification

- Switched between Pop Camera, Mono Camera Robot, Split Core and Character Kits.
- Switched six Character Kit labels.
- Selected exercises and targets in the parent app and sent a task to the robot.
- Toggled Camera Hidden / Camera Active.
- Switched Idle, Ready, Training and Complete states.
- Incremented/decremented training count and verified phone/robot/status synchronization (tested at 3/30).
- Added/removed concepts and verified two-column comparison.
- Browser console warnings/errors checked: none.
- Production build completed successfully with Vite 6.4.2.

## Findings

No actionable P0, P1 or P2 issues remain in the tested experience.

## Follow-up polish

- [P3] Generate individual transparent shell-kit variants so choosing Deer/Rabbit/Frog/etc. changes the physical silhouette, not only the UI identity.
- [P3] Add separate calibrated screen-overlay coordinates if future product variants use different display geometries.

## Comparison history

1. Initial implementation used a gallery/detail/comparison structure. It was functionally complete but did not match the interaction depth of the local ID simulator.
2. Added the Live ID Lab with form and role-kit selection, Camera mechanism states, four UI states, synchronized counter, dark studio treatment and responsive control reflow.
3. Replaced the concept-board-only stage with a parent-app phone model and dedicated front-view Teamo product asset. Added interactive task selection, task dispatch and synchronized phone/device progress.
4. The initial generated device asset contained a baked checkerboard background; regenerated it with true transparency and verified the revised browser render.
5. Post-fix browser evidence showed the dual-end simulator intact at the tested narrow viewport; 3/30 synchronized across both ends and the two-direction comparison rendered correctly.

final result: passed

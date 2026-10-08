import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const appPath = new URL('../src/App.jsx', import.meta.url);
const livePath = new URL('../public/live-demo/index.html', import.meta.url);

test('automatic demo exposes distinct play and pause product icons', async () => {
  const app = await readFile(appPath, 'utf8');
  assert.match(app, /Pause/);
  assert.match(app, /playing\s*\?\s*<Pause/);
});

test('embedded automatic demo supports pause and resume', async () => {
  const live = await readFile(livePath, 'utf8');
  assert.match(live, /setAutoButtonState/);
  assert.match(live, /token\.paused/);
  assert.match(live, /window\.toggleAutoDemo/);
});

test('parent top bar never renders a dead back button', async () => {
  const live = await readFile(livePath, 'utf8');
  assert.match(live, /back\s*\?/);
  assert.doesNotMatch(live, /pTop\('运动状态',''\)/);
  assert.doesNotMatch(live, /pTop\('运动结果',''\)/);
});

test('visible UI does not fall back to emoji glyphs', async () => {
  const app = await readFile(appPath, 'utf8');
  const live = await readFile(livePath, 'utf8');
  const visibleEmoji = /[👦📱🖥🎚📩🦶🏋️🏆⚙️🤖💤🛼🔥👍]/u;
  assert.doesNotMatch(app, visibleEmoji);
  assert.doesNotMatch(live, visibleEmoji);
});

test('hero and product use deterministic transparent cutouts', async () => {
  const app = await readFile(appPath, 'utf8');
  assert.match(app, /teamo-cover-open-cutout\.png/);
  assert.match(app, /teamo-cover-closed-cutout\.png/);
});


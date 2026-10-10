const fs = require('fs');
const path = require('path');
const dir = __dirname;

function read(p) { return fs.readFileSync(path.join(dir, p), 'utf8'); }
function b64(p) { return fs.readFileSync(path.join(dir, p)).toString('base64'); }

// 1) 收集 16 个图标 -> base64 data URI（键名不带 .png 扩展名）
const iconDir = path.join(dir, 'assets', 'icons');
const iconMap = {};
for (const f of fs.readdirSync(iconDir)) {
  if (f.endsWith('.png')) iconMap[f.replace(/\.png$/, '')] = 'data:image/png;base64,' + b64(path.join('assets', 'icons', f));
}
const ICON_JSON = JSON.stringify(iconMap);

// 1b) assets 根目录下的整图素材（如产品图）也内联
const rootAssetMap = {};
for (const f of fs.readdirSync(path.join(dir, 'assets'))) {
  const p = path.join(dir, 'assets', f);
  if (fs.statSync(p).isFile() && /\.(png|jpe?g|webp)$/.test(f)) {
    rootAssetMap['assets/' + f] = 'data:image/' + (f.endsWith('.jpg') || f.endsWith('.jpeg') ? 'jpeg' : f.endsWith('.webp') ? 'webp' : 'png') + ';base64,' + b64(path.join('assets', f));
  }
}

// 字面量引用（assets/icons/NAME.png）直接换 data URI
function inlineIconsLiteral(text) {
  for (const [name, uri] of Object.entries(iconMap)) {
    text = text.split('assets/icons/' + name + '.png').join(uri);
  }
  for (const [ref, uri] of Object.entries(rootAssetMap)) {
    text = text.split(ref).join(uri);
  }
  return text;
}

let html = read('index.html');

// 2) 内联 CSS <link>
html = html.replace(/<link rel="stylesheet" href="([^"]+)">/g, (m, file) => {
  return '<style>/* inlined: ' + file + ' */\n' + inlineIconsLiteral(read(file)) + '\n</style>';
});

// 3) 内联 JS <script src> （字面图标先内联，再转内联 <script>）
html = html.replace(/<script src="([^"]+)"><\/script>/g, (m, file) => {
  let js = read(file);
  js = inlineIconsLiteral(js);
  js = js.replace(/<\/script>/gi, '<\\/script>');
  return '<script>/* inlined: ' + file + ' */\n' + js + '\n</script>';
});

// 4) 动态拼接引用 assets/icons/${VAR}.png -> ${ICON_DATA[VAR]}
html = html.replace(/assets\/icons\/\$\{([^}]+)\}\.png/g, '${ICON_DATA[$1]}');
// 兜底字面量
html = inlineIconsLiteral(html);

// 5) 注入 ICON_DATA 映射（置于 #app 之后，先于所有脚本执行）
const iconScript = '<script>const ICON_DATA=' + ICON_JSON + ';</script>';
html = html.replace('<div id="app"></div>', '<div id="app"></div>' + iconScript);

// 6) 去掉指向本地文档的相对链接（部署后不可用，避免破链；保留文字）
html = html.replace(/<a href="\.\.\/\.\.\/docs[^"]*">/g, '<a href="#" onclick="return false">');

fs.mkdirSync(path.join(dir, 'deploy'), { recursive: true });
fs.writeFileSync(path.join(dir, 'deploy', 'index.html'), html, 'utf8');
console.log('standalone written: deploy/index.html');
console.log('size(bytes):', Buffer.byteLength(html));
const m = html.match(/src="[^"]*"/g) || [];
const bad = m.filter(s => !s.startsWith('src="data:'));
console.log('total src:', m.length, 'non-data src (should be 0):', bad.length);
if (bad.length) console.log(bad.join('\n'));

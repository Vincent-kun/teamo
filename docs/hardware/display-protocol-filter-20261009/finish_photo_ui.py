from pathlib import Path
import json
p=Path(__file__).resolve().parent/'template.html'
s=p.read_text(encoding='utf-8')
s=s.replace('图片来源页</a>`','图片来源页</a><br>${(p.other_views||[]).map(v=>`<a href="${esc(v.url)}" target="_blank" rel="noopener">${esc(v.caption)}</a>`).join("<br>")}`')
s=s.replace('${esc(p.photo_status)}${p.id', '${esc(p.missing_reason||p.photo_status)}${p.id')
s=s.replace('<p class="small" id="photo-summary"></p>','<p class="small" id="photo-summary"></p><p><a href="产品图片缺项与供应商补图清单.md">7条缺图原因与供应商补图清单</a> · <a href="photo-sources.json">图片原始URL与校验记录</a></p>')
p.write_text(s,encoding='utf-8')

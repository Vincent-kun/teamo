"""Regression check: all source Function rows must be real eight-column HTML rows."""
from pathlib import Path
from html.parser import HTMLParser
import re,sys
root=Path(__file__).resolve().parents[1]
src=root/'docs/product/requirements/Teamo_Device_Function_Specification_v0.5.2.md'
page=src.with_suffix('.html')
text=src.read_text(encoding='utf-8')
business=text[text.index('## 1 设备'):text.index('### 8.3 ')]
expected={re.match(r'\|\s*(\d+\.\d+\.\d+)\s*\|',l)[1] for l in business.splitlines() if re.match(r'\|\s*\d+\.\d+\.\d+\s*\|',l)}
class Rows(HTMLParser):
 def __init__(self):super().__init__();self.row=[];self.cell=None;self.rows=[]
 def handle_starttag(self,tag,attrs):
  if tag=='tr':self.row=[]
  if tag in ('td','th'):self.cell=''
 def handle_data(self,data):
  if self.cell is not None:self.cell+=data
 def handle_endtag(self,tag):
  if tag in ('td','th') and self.cell is not None:self.row.append(self.cell.strip());self.cell=None
  if tag=='tr':self.rows.append(self.row)
parser=Rows();parser.feed(page.read_text(encoding='utf-8'))
valid={row[0] for row in parser.rows if len(row)==8 and row[0] in expected}
missing=sorted(expected-valid)
if missing:
 print('FAIL: Function IDs are not rendered as eight-column table rows:',', '.join(missing));sys.exit(1)
assert len(expected)==69
assert all(x in valid for x in ['7.2.3','7.2.4','7.2.5','7.2.6','7.2.7','7.2.8','7.2.9'])
print('PASS: all 69 Function rows rendered; binding, QR, child switch and unbinding visible as structured cells')

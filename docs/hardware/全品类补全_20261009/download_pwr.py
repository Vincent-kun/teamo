# -*- coding: utf-8 -*-
"""工作包D：下载电源类候选的规格书PDF/首页图到 assets。失败记录到 download_log.txt。"""
import urllib.request, ssl, os, datetime

OUT = r"d:/work/sportmate/docs/hardware/全品类补全_20261009/assets"
LOG = os.path.join(OUT, "download_log.txt")

TARGETS = [
    ("PWR03_TP4056_datasheet.pdf", "https://www.toppwr.com/uploadfile/file/20230304/640301eae1260.pdf"),
    ("PWR04_SGM41513_datasheet.pdf", "https://atta.szlcsc.com/upload/public/pdf/source/20230915/4ED7FFAA41758E4642E8DE062114C033.pdf"),  # 占位将被替换
    ("PWR05_BQ25895_datasheet.pdf", "https://www.ti.com/lit/ds/symlink/bq25895.pdf"),
    ("PWR07_S8261_datasheet.pdf", "https://www.ablic.com/en/doc/datasheet/battery_protection_ic/S8261_E.pdf"),
    ("PWR08_TPS563201_datasheet.pdf", "https://www.ti.com/lit/ds/symlink/tps563201.pdf"),
    ("PWR10_ME6211_datasheet.pdf", "http://web.viewat.com.cn:6060/uploadfile_crs/ME6211+Series_E8.0.pdf"),
    ("PWR11_TPS61023_datasheet.pdf", "https://www.ti.com/lit/ds/symlink/tps61023.pdf"),
    ("PWR12_LC709203F_datasheet_lcsc.pdf", "https://atta.szlcsc.com/upload/public/pdf/source/20230915/4ED7FFAA41758E4642E8DE062114C033.pdf"),
    ("PWR13_MAX17048_datasheet.pdf", "https://www.analog.com/media/en/technical-documentation/data-sheets/MAX17048-MAX17049.pdf"),
    ("PWR15_NCP15XH103_spec_rs.pdf", "https://docs.rs-online.com/7c3e/0900766b8171bb68.pdf"),
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lines = []
for name, url in TARGETS:
    path = os.path.join(OUT, name)
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36",
            "Accept": "*/*",
        })
        with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
            data = r.read()
        if len(data) < 800:
            raise IOError("内容过短 %d 字节" % len(data))
        with open(path, "wb") as f:
            f.write(data)
        lines.append("OK   %s %d bytes %s" % (name, len(data), url))
    except Exception as e:
        if os.path.exists(path):
            os.remove(path)
        lines.append("FAIL %s %s :: %s" % (name, url, e))

with open(LOG, "w", encoding="utf-8") as f:
    f.write("下载核查日期: 2026-10-09\n" + "\n".join(lines) + "\n")
print("\n".join(lines))

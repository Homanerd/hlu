import sys
sys.stdout.reconfigure(encoding='utf-8')
from pypdf import PdfReader
import re
r = PdfReader(r'research\van-ban-phap-luat\60_2014_QH13_m_259727.pdf')
text = '\n'.join([p.extract_text() for p in r.pages])
for kw in ['trực tuyến', 'môi trường mạng']:
    matches = list(re.finditer(kw, text))
    print(f'\n=== "{kw}": {len(matches)} matches ===')
    for m in matches[:3]:
        s = m.start()
        print('---')
        print(text[max(0,s-300):s+200])

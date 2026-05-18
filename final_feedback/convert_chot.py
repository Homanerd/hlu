#!/usr/bin/env python3
"""Convert raw text extracted from PDF 'Cô sửa chốt' to markdown matching sua-1.md convention.

Adapted from feedback/convert_v3.py — same logic, paths repointed to final_feedback/ source
and thesis/khoa-luan-tot-nghiep-CHOT.md output.
"""
import re
from pathlib import Path

RAW = Path(__file__).parent / "v-chot-raw-flow.txt"
OUT = Path(__file__).parent.parent / "thesis" / "khoa-luan-tot-nghiep-CHOT.md"

P_CHAPTER = re.compile(r'^CHƯƠNG\s+\d+:')
P_KETLUAN_CHAPTER = re.compile(r'^KẾT LUẬN CHƯƠNG\s+\d+$')
P_KETLUAN = re.compile(r'^KẾT LUẬN$')
P_DANHMUC = re.compile(r'^DANH MỤC')
P_MODAU = re.compile(r'^MỞ ĐẦU$')
P_NOIDUNG = re.compile(r'^NỘI DUNG$')

P_H_SEC4 = re.compile(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)\.\s+(.+)$')
P_H_SEC3 = re.compile(r'^(\d+)\.(\d+)\.(\d+)\.\s+(.+)$')
P_H_SEC2 = re.compile(r'^(\d+)\.(\d+)\.\s+(.+)$')
P_H_MODAU_SUB = re.compile(r'^(\d+)\.(\d+)\s+(.+)$')
P_H_MODAU_TOP = re.compile(r'^(\d+)\.\s+(.+)$')

P_PAGE = re.compile(r'^\d{1,3}$')
P_ROMAN_PAGE = re.compile(r'^[ivx]{1,5}$')

MODAU_TOP_TITLES = {
    'Lý do chọn đề tài',
    'Tình hình nghiên cứu',
    'Mục đích và nhiệm vụ nghiên cứu',
    'Đối tượng và phạm vi nghiên cứu',
    'Phương pháp nghiên cứu',
    'Ý nghĩa lý luận và thực tiễn của đề tài',
    'Kết cấu của khóa luận',
}
MODAU_SUB_TITLES = {
    'Mục đích nghiên cứu', 'Nhiệm vụ nghiên cứu',
    'Đối tượng nghiên cứu', 'Phạm vi nghiên cứu',
}


def classify_line(line: str) -> str:
    s = line.strip()
    if not s:
        return 'blank'
    if P_PAGE.fullmatch(s) or P_ROMAN_PAGE.fullmatch(s):
        return 'page'
    if P_MODAU.fullmatch(s):
        return 'h1'
    if P_NOIDUNG.fullmatch(s):
        return 'h1'
    if P_KETLUAN.fullmatch(s):
        return 'h1'
    if P_DANHMUC.match(s):
        return 'h1'
    if P_CHAPTER.match(s):
        return 'h1'
    if P_KETLUAN_CHAPTER.match(s):
        return 'h2'
    if P_H_SEC4.match(s):
        return 'h4'
    if P_H_SEC3.match(s):
        return 'h3'
    if P_H_SEC2.match(s):
        return 'h2'
    m_ms = P_H_MODAU_SUB.match(s)
    if m_ms and len(s) < 80:
        title = m_ms.group(3).strip().rstrip('.')
        if title in MODAU_SUB_TITLES:
            return 'h3'
    m_top = P_H_MODAU_TOP.match(s)
    if m_top and len(s) < 80:
        title = m_top.group(2).strip().rstrip('.')
        if title in MODAU_TOP_TITLES:
            return 'h2'
    if s == '-':
        return 'bullet-marker'
    if s == '+':
        return 'subbullet-marker'
    if s.startswith('- '):
        return 'bullet'
    if s.startswith('+ '):
        return 'subbullet'
    return 'text'


def main():
    lines = RAW.read_text(encoding='utf-8').splitlines()
    kinds = [classify_line(l) for l in lines]

    out = []
    out += [
        '# KHÓA LUẬN TỐT NGHIỆP',
        '',
        '**Đề tài:** ĐĂNG KÝ KẾT HÔN THEO PHÁP LUẬT VIỆT NAM HIỆN HÀNH.',
        '',
        '**Sinh viên thực hiện:** Nguyễn Quang Linh',
        '**MSSV:** K22FCQ075',
        '**Chuyên ngành:** Luật',
        '**Giảng viên hướng dẫn:** TS. Bùi Thị Mừng',
        '',
        '**Trường Đại học Luật Hà Nội**',
        '',
        '**Hà Nội — 2026**',
        '',
        '> **Nguồn:** `final_feedback/QuangLinh Cô  sửa chốt _KLTN_DangKyKetHon.pdf` — bản GVHD sửa chốt.',
        '',
        '---',
        '',
    ]

    started = False
    para_buf = []

    def flush():
        if para_buf:
            joined = ' '.join(p.strip() for p in para_buf if p.strip())
            if joined:
                out.append(joined)
                out.append('')
            para_buf.clear()

    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        s = raw.strip()
        kind = kinds[i]

        if not started:
            if s == 'LỜI CAM ĐOAN':
                started = True
                out += ['## LỜI CAM ĐOAN', '']
                i += 1
                continue
            i += 1
            continue

        if s == 'LỜI CẢM ƠN':
            flush()
            out += ['---', '', '## LỜI CẢM ƠN', '']
            i += 1
            continue

        if s == 'MỤC LỤC':
            flush()
            out += ['---', '', '## MỤC LỤC', '', '_(Sẽ cập nhật khi hoàn thành toàn bộ)_', '']
            while i < n and lines[i].strip() != 'DANH MỤC CÁC TỪ VIẾT TẮT':
                i += 1
            continue

        if s == 'DANH MỤC CÁC TỪ VIẾT TẮT':
            flush()
            out += ['---', '', '## DANH MỤC CÁC TỪ VIẾT TẮT', '',
                    '| Viết tắt | Đầy đủ |',
                    '| -------- | ------ |']
            i += 1
            while i < n and lines[i].strip() != 'MỞ ĐẦU':
                term = lines[i].strip()
                if term and not P_ROMAN_PAGE.fullmatch(term) and not P_PAGE.fullmatch(term):
                    j = i + 1
                    while j < n and (not lines[j].strip() or P_ROMAN_PAGE.fullmatch(lines[j].strip())):
                        j += 1
                    if j < n:
                        defn = lines[j].strip()
                        if defn.startswith(':'):
                            defn = defn[1:].strip()
                        out.append(f'| {term} | {defn} |')
                        i = j + 1
                        continue
                i += 1
            out.append('')
            continue

        def merge_heading_continuations(start_i, base_text):
            merged = base_text
            j = start_i + 1
            while j < n:
                nxt_kind = kinds[j]
                nxt = lines[j].strip()
                if nxt_kind == 'blank' or nxt_kind == 'page':
                    j += 1
                    continue
                if nxt_kind == 'text' and len(nxt) < 35 and not nxt.endswith('.') and not re.match(r'^[A-Z]\.\s', nxt):
                    merged = merged.rstrip() + ' ' + nxt
                    j += 1
                    continue
                break
            return merged, j

        if kind == 'h1':
            flush()
            merged, next_i = merge_heading_continuations(i, s)
            out += ['---', '', f'# {merged}', '']
            i = next_i
            if 'DANH MỤC TÀI LIỆU THAM KHẢO' in merged:
                buf = []
                while i < n:
                    ss = lines[i].strip()
                    kk = kinds[i]
                    if kk == 'page' or kk == 'blank':
                        i += 1
                        continue
                    buf.append(ss)
                    i += 1
                full = ' '.join(buf)
                import re as _re
                full = _re.sub(r'\bA\.\s*Danh mục các văn bản pháp luật\s*', '\n@@A@@\n', full)
                full = _re.sub(r'\bB\.\s*Các tài liệu tham khảo khác\s*', '\n@@B@@\n', full)
                full = _re.sub(r'(?<=\s)(\d{1,3})\.\s+', r'\n@@\1@@', full)
                for part in full.split('\n'):
                    part = part.strip()
                    if not part:
                        continue
                    if part == '@@A@@':
                        out += ['## A. Danh mục các văn bản pháp luật', '']
                        continue
                    if part == '@@B@@':
                        out += ['', '## B. Các tài liệu tham khảo khác', '']
                        continue
                    m_item = _re.match(r'@@(\d+)@@(.+)$', part, _re.DOTALL)
                    if m_item:
                        num = m_item.group(1)
                        txt = m_item.group(2).strip()
                        txt = _re.sub(r'\s+(https?://)', r' \1', txt)
                        out.append(f'{num}. {txt}')
                    else:
                        out.append(part)
                out.append('')
            continue

        if kind == 'h2':
            flush()
            merged, next_i = merge_heading_continuations(i, s)
            out += [f'## {merged}', '']
            i = next_i
            continue

        if kind == 'h3':
            flush()
            merged, next_i = merge_heading_continuations(i, s)
            out += [f'### {merged}', '']
            i = next_i
            continue

        if kind == 'h4':
            flush()
            merged, next_i = merge_heading_continuations(i, s)
            out += [f'#### {merged}', '']
            i = next_i
            continue

        if kind == 'page':
            flush()
            i += 1
            continue

        if kind == 'blank':
            flush()
            i += 1
            continue

        if kind in ('bullet', 'subbullet', 'bullet-marker', 'subbullet-marker'):
            flush()
            prefix = '- ' if kind in ('bullet', 'bullet-marker') else '  - '
            if kind in ('bullet-marker', 'subbullet-marker'):
                text = ''
                j = i + 1
                while j < n and (kinds[j] == 'blank' or kinds[j] == 'page'):
                    j += 1
                if j < n and kinds[j] == 'text':
                    text = lines[j].strip()
                    j += 1
                else:
                    i += 1
                    continue
            else:
                text = s[2:].strip()
                j = i + 1
            while j < n:
                nxt_kind = kinds[j]
                nxt = lines[j].strip()
                if nxt_kind == 'blank' or nxt_kind == 'page':
                    break
                if nxt_kind == 'text':
                    text = text + ' ' + nxt
                    j += 1
                    continue
                break
            out.append(prefix + text)
            i = j
            continue

        para_buf.append(s)
        i += 1

    flush()

    OUT.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(f'Wrote {OUT} ({len(out)} lines)')


if __name__ == '__main__':
    main()

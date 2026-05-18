# HLU — Khóa Luận Tốt Nghiệp

## Thông tin chung

- **Trường**: Đại học Luật Hà Nội (HLU)
- **Sinh viên**: Nguyễn Quang Linh — K22FCQ075
- **GVHD**: TS. Bùi Thị Mừng
- **Đề tài**: ĐĂNG KÝ KẾT HÔN THEO PHÁP LUẬT VIỆT NAM HIỆN HÀNH
- **Lĩnh vực**: Luật Hôn nhân và Gia đình
- **Ngôn ngữ**: Tiếng Việt
- **Cấu trúc**: 2 chương + Mở đầu (7 mục) + Kết luận + TLTK

## ⚠️ Trạng thái hiện tại (cập nhật 14/05/2026)

- [x] Bản nộp GVHD lần 1 — `final_thesis/NguyenQuangLinh_KLTN_DangKyKetHon.pdf` (64 trang)
- [x] Bản sửa lần 1 (sinh viên) — `thesis/khoa-luan-tot-nghiep-sua-1.md` (đã apply 4 đợt feedback GVHD)
- [x] Bản GVHD sửa v3 — `feedback/NguyenQuangLinh Cô sửa 3 _KLTN_DangKyKetHon.pdf` (74 trang)
- [x] Bản công tác sua-2 — `thesis/khoa-luan-tot-nghiep-sua-2.md` (clone từ PDF GVHD sửa v3, snapshot lịch sử)
- [x] **🆕 BẢN GVHD SỬA CHỐT** — `final_feedback/QuangLinh Cô  sửa chốt _KLTN_DangKyKetHon.pdf` (54 trang, clean — đã chốt nội dung)
- [x] **BẢN CÔNG TÁC HIỆN TẠI** — `thesis/khoa-luan-tot-nghiep-CHOT.md` (clone từ PDF cô chốt qua `final_feedback/convert_chot.py`)
- [x] Bản gốc đã sync với PDF nộp lần 1 — `thesis/khoa-luan-tot-nghiep.md`
- [ ] Hoàn thiện MỤC LỤC + soát typo PDF extraction (vd: "đưng lý lết hôn", "tỏng quy định" ở mục 3.2 Nhiệm vụ NC)
- [ ] Bổ sung danh sách footnote (PDF extract ra footnote bị lẫn vào text)

### So với sua-2 → CHOT (thay đổi do cô chốt)
- **DANH MỤC VIẾT TẮT** rút từ 12 mục → 9 mục: bỏ `ĐKKH`, `DTTS`, `YTNN` (cô yêu cầu viết đầy đủ trong văn bản, không lạm dụng viết tắt)
- **1.2.1 & 1.2.2** GỘP, KHÔNG còn tách `.1` (trong nước) / `.2` (YTNN). Lý do: NĐ 120/2025 và Luật HT (sửa đổi) 2026 đã đồng nhất thẩm quyền & thủ tục về UBND cấp xã cho cả 2 trường hợp → viết văn xuôi liền với so sánh trước/sau
- **1.2.3.1** đổi tiêu đề: "đối với người yêu cầu đăng ký" → "đối với người kết hôn"
- Tổng độ dài giảm ~18% (30.4k → 24.9k từ; 74 → 54 trang)

## File structure

```
HLU/
├── CLAUDE.md                                 ← File này (context cho AI)
├── final_thesis/
│   └── NguyenQuangLinh_KLTN_DangKyKetHon.pdf ← Bản nộp GVHD lần 1
├── feedback/                                 ← Phản hồi GVHD đợt giữa
│   ├── NguyenQuangLinh Cô sửa 3 _KLTN_DangKyKetHon.pdf ← PDF GVHD sửa v3
│   ├── v3-raw-flow.txt / v3-raw-layout.txt   ← Raw text extract
│   └── convert_v3.py                         ← Script convert PDF→md (v3)
├── final_feedback/                           ← 🆕 BẢN CÔ CHỐT (đợt cuối)
│   ├── QuangLinh Cô  sửa chốt _KLTN_DangKyKetHon.pdf ← PDF cô chốt
│   ├── v-chot-raw-flow.txt / v-chot-raw-layout.txt   ← Raw text extract
│   └── convert_chot.py                       ← Script convert PDF→md (chốt)
├── thesis/
│   ├── khoa-luan-tot-nghiep.md               ← Bản sync PDF nộp 1
│   ├── khoa-luan-tot-nghiep-sua-1.md         ← Bản sửa lần 1 (markup ✏️ + <mark>)
│   ├── khoa-luan-tot-nghiep-sua-2.md         ← Bản công tác cũ (clone PDF v3) — snapshot lịch sử
│   └── khoa-luan-tot-nghiep-CHOT.md          ← 🆕 BẢN ĐANG CÔNG TÁC (clone PDF cô chốt)
├── research/
│   └── van-ban-phap-luat/
│       ├── 52_2014_QH13_m_238640.pdf         ← Luật HN&GĐ 2014
│       ├── 60_2014_QH13_m_259727.pdf         ← Luật Hộ tịch 2014
│       ├── 120_2025_ND-CP_m_660588.pdf       ← NĐ 120/2025/NĐ-CP
│       ├── du-thao-luat-ho-tich-2026-ban-trinh-qh.pdf ← Luật HT (sửa đổi) 2026
│       └── chế-định-kết-hôn-trong-Luật-HNGĐ-vấn-đề-lý-luận-và-thực-tiễn-ts-1.pdf
└── references/
    └── dang-ky-ket-hon-mai-hai-linh/         ← Khóa luận MHL (HLU 2024) tham khảo
```

## Cấu trúc khóa luận hiện tại (sau khi xử lý feedback)

```
MỞ ĐẦU
  1. Lý do chọn đề tài
  2. ✏️ Tình hình nghiên cứu                  ← THÊM MỚI theo feedback GVHD
  3. ✏️ Mục đích và nhiệm vụ nghiên cứu        ← (cũ là mục 2)
  4. ✏️ Đối tượng và phạm vi nghiên cứu        ← (cũ là mục 3)
  5. ✏️ Phương pháp nghiên cứu                 ← (cũ là mục 4)
  6. ✏️ Ý nghĩa lý luận và thực tiễn của đề tài
  7. ✏️ Kết cấu của khóa luận

CHƯƠNG 1: LÝ LUẬN VÀ PHÁP LUẬT VỀ ĐĂNG KÝ KẾT HÔN
  1.1. Một số vấn đề lý luận cơ bản về ĐKKH
    1.1.1. Khái niệm kết hôn và đăng ký kết hôn
      1.1.1.1. Khái niệm kết hôn (✏️ đã thêm khái niệm rõ ràng từ Từ điển HLU + Luật HN&GĐ 2000/2014)
      1.1.1.2. ✏️ Khái niệm đăng ký kết hôn (đã mở rộng từ ~150 từ → ~1.500 từ)
    1.1.2. Ý nghĩa của việc ĐKKH
  1.2. Nội dung quy định của PL HN&GĐ hiện hành về ĐKKH
    1.2.1. ✏️ Thẩm quyền ĐKKH (đã restructure từ "giai đoạn" → phân tích theo văn bản PL)
      1.2.1.1. Đối với việc kết hôn trong nước
      1.2.1.2. ✏️ Đối với việc kết hôn có YTNN
    1.2.2. ✏️ Trình tự, thủ tục ĐKKH (cùng cách restructure)
      1.2.2.1. Đối với việc kết hôn trong nước
      1.2.2.2. ✏️ Đối với việc kết hôn có YTNN
    1.2.3. Xử lý vi phạm pháp luật về ĐKKH

CHƯƠNG 2: THỰC TIỄN THỰC HIỆN PL VỀ ĐKKH VÀ MỘT SỐ KIẾN NGHỊ
  2.1. Thực tiễn thực hiện pháp luật
    2.1.1. Kết quả đạt được
    2.1.2. Tồn tại, vướng mắc (gồm ✏️ tiểu mục mới về vướng mắc sáp nhập đơn vị hành chính)
    2.1.3. Nguyên nhân
  2.2. Kiến nghị
```

## 📋 Marker convention (cho bản sửa-1)

- **`✏️`** — đánh dấu các section đã sửa (header, đoạn mở đầu)
- **`<mark>...</mark>`** — wrap nội dung đã sửa để render highlight vàng (VS Code Preview, GitHub)
- **`> ✏️ **[ĐÃ SỬA THEO FEEDBACK GVHD]** ...`** — blockquote tóm tắt thay đổi tại đầu mỗi section

## 📚 Văn bản pháp luật chính (CẬP NHẬT)

1. **Luật HN&GĐ 2014** (52/2014/QH13) — Đ.3 K.5 (định nghĩa kết hôn), Đ.8 (điều kiện), Đ.9 (đăng ký bắt buộc)
2. **Luật Hộ tịch 2014** (60/2014/QH13) — Đ.17 (thẩm quyền trong nước), Đ.37 (có YTNN)
3. **NĐ 123/2015/NĐ-CP** — Hướng dẫn Luật Hộ tịch
4. **NĐ 07/2025/NĐ-CP** (09/01/2025) — **Bãi bỏ yêu cầu Giấy xác nhận tình trạng hôn nhân** với ĐKKH trong nước
5. **Luật Tổ chức chính quyền địa phương 72/2025/QH15** (16/6/2025) — Bỏ cấp huyện, sang mô hình 2 cấp
6. **NĐ 120/2025/NĐ-CP** (hiệu lực 01/7/2025) — Chuyển giao thẩm quyền ĐKKH có YTNN từ cấp huyện → cấp xã; cá nhân được lựa chọn nơi đăng ký
7. **🆕 Luật Hộ tịch (sửa đổi) năm 2026** — Quốc hội khóa XVI thông qua 23/4/2026 (488/492 ĐB tán thành, 97,60%), **hiệu lực 01/3/2027**, thay thế Luật Hộ tịch 2014. Điểm mới: Đ.8 (đăng ký không phụ thuộc nơi cư trú), Đ.16 (UBND cấp xã có thẩm quyền cho cả ĐKKH có YTNN)
8. **BLDS 2015** — Đ.40 (nơi cư trú)
9. **BLTTDS 2015** — Đ.91 (giá trị chứng cứ của GCNKH)

## 🎯 Lịch sử feedback GVHD đã xử lý

### Feedback đợt 1 (đầu 4/2026)
- ✅ Sync file md với bản PDF GVHD đã duyệt
- ✅ Thống nhất chữ viết tắt (UBND, GCNKH, YTNN, DTTS, ĐKKH, HN&GĐ)
- ✅ Restructure 1.2.1 và 1.2.2 từ kiểu "giai đoạn lịch sử" sang phân tích theo từng văn bản PL
- ✅ Tăng cường chương 2 về vướng mắc sáp nhập đơn vị hành chính
- ✅ Tăng cường trích dẫn + bổ sung TLTK
- ✅ Khắc phục lỗi kỹ thuật (typo, format)

### Feedback đợt 2
- ✅ Bổ sung mục 2 "Tình hình nghiên cứu" — chỉ giữ tài liệu thực sự dùng (Luận án TS Bùi Thị Mừng + Khóa luận Mai Hải Linh + Giáo trình HLU + Báo cáo Cục Thống kê + Điều tra 53 DTTS); renumber các mục Mở đầu

### Feedback đợt 3 (1.1.1.1 Khái niệm kết hôn)
- ✅ "Sau khi phân tích phải đưa ra khái niệm" — đã bổ sung đoạn rút khái niệm từ Từ điển HLU + Luật HN&GĐ 2000/2014 (theo cách MHL làm)

### Feedback đợt 4 (1.1.1.2 Khái niệm ĐKKH)
- ✅ "Toàn bộ nội dung viết sơ sài, khái niệm chưa có. Bổ sung phân tích để đưa ra khái niệm. Dài thêm." — đã mở rộng từ ~150 từ → ~1.500 từ, dẫn 5 nguồn (Luật HN&GĐ 2014, Luật Hộ tịch 2014, Luật HT sửa đổi 2026, Từ điển Tiếng Việt, Từ điển HLU), khái niệm bold-italic ở câu kết

## 📐 Style guide (kế thừa từ Mai Hải Linh — HLU 2024)

- Văn xuôi liên tục, không bullet list ở phần khái niệm
- Liệt kê công trình theo dạng: *"Đề tài luận án... của tác giả X đã đi sâu phân tích..."*
- Khái niệm rút ra ở câu kết của section: *"Như vậy, [khái niệm]..."*
- Khi đưa ra khái niệm: dẫn 3 nguồn (Từ điển giải thích thuật ngữ Luật học HLU + Luật HN&GĐ 2000 + 2014) thay vì tự bịa
- Phân tích yếu tố cấu thành (2 hoặc 3 yếu tố) sau khi nêu khái niệm

## ⚠️ Lưu ý khi tiếp tục công việc

1. **File đang công tác:** `thesis/khoa-luan-tot-nghiep-CHOT.md` (KHÔNG sửa các file `khoa-luan-tot-nghiep.md`, `khoa-luan-tot-nghiep-sua-1.md`, `khoa-luan-tot-nghiep-sua-2.md` — đây là snapshot lịch sử)
2. **Bản CHOT.md được tạo bằng cách extract PDF cô chốt** (`pdftotext` → script `final_feedback/convert_chot.py`). Đây là bản clone clean, KHÔNG có markup ✏️/`<mark>` vì cô đã chốt nội dung — chỉ sửa typo và format khi cần
3. **Trước khi đề xuất khái niệm:** PHẢI dẫn nguồn (Từ điển HLU + Luật HN&GĐ + …) — KHÔNG tự bịa khái niệm
4. **Cập nhật Luật Hộ tịch (sửa đổi) 2026** ở mọi chỗ có thể (đã thông qua 23/4/2026, hiệu lực 01/3/2027)
5. **Sáp nhập đơn vị hành chính** (cấp tỉnh 63→34, cấp xã 10.035→3.321, hiệu lực 01/7/2025) — bối cảnh thực tiễn quan trọng
6. **Footnote trong sua-2.md** có thể bị lẫn vào text do PDF extraction (vd: `"đó.3"`, `"được.”2`). Khi sửa từng section sẽ clean up.

## Số liệu thực tế đã tích hợp

- 2 triệu+ ĐKKH giai đoạn 2021–2023; 734.900 trường hợp năm 2023
- 1.890.488 cặp ĐKKH mới giai đoạn 2021–2023, tỷ lệ kết hôn lần đầu 85,58%
- Tảo hôn 21,9% trong DTTS (Mông 51,5%, Cơ Lao 47,8%, Mảng 47,2%, Xinh Mun 44,8%)
- ĐKKH có YTNN: 2.000 (2021) → 19.000 (2023); 89,1% là phụ nữ VN
- Top quốc gia đối tác: Đài Loan 21,4%, Mỹ 19,9%, Hàn Quốc 18,1%, TQ 17,6%
- 3 triệu+ sổ hộ tịch, 100 triệu+ bản ghi đang số hóa (Đề án 06)
- Sáp nhập đơn vị HC: cấp tỉnh 63→34, cấp xã 10.035→3.321 (gần 67% sáp nhập)

## Git workflow

- Repo: `https://github.com/Homanerd/hlu.git`
- Branch: `main`
- File giáo trình PDF lớn (688MB) đã được loại khỏi history (commit `3dfed4b` thêm `.gitignore`)
- Commit mỗi đợt sửa lớn — message format: tiếng Việt, mô tả ngắn gọn thay đổi

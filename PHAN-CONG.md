# Phân công công việc · LAB 10 (Gate 1)

Bàn 4 người: **Vũ, Thành, Dung, Hải Anh**. README chia 3 vai; bàn có 4 người nên vai Kỹ sư cổng được tách làm hai.

## Phân vai

| Người | Vai | Phụ trách chính |
|---|---|---|
| **Vũ** | Kỹ sư cổng (chính) + trưởng nhóm | Repo, Git, `lab10/guards.py`, các lệnh `eval`, `trace`, `gate` |
| **Thành** | Kỹ sư cổng (phụ) | `lab10/monitors.py`, test, ticket hiểm `--adhoc`, kiểm hồi quy |
| **Dung** | Sản phẩm và kinh doanh | Tiêu chí chấp nhận, chi phí, ROI, quyết định v1/v2 |
| **Hải Anh** | Vận hành và pháp lý | Người trực, runbook, PII, checklist, `submission.json` |

## Việc theo mốc thời gian

| Mốc | Vũ | Thành | Dung | Hải Anh |
|---|---|---|---|---|
| **0–15** Cài đặt | Tạo repo Private đúng tên, mời team chấm, `git remote add upstream`, `git config`, chạy `Ran 13 tests OK` | Chạy lại test trên máy mình | Chọn eval card và PRD v1.1 từ Lab 9 | Điền bảng thành viên trong `TEAM.md` |
| **15–65** Phiếu A | Đọc khoảng tin cậy (câu 1.5) | Câu 1.3–1.4 (thước đo → dữ liệu → cách tính) | Câu 1.1–1.2 và 1.6, điền `acceptance_criteria.json` | Soát 4 câu tiêu chí và 2 câu ranh giới đầu ra |
| **60–65** Ký | Chạy `criteria sign`, commit và push | Kiểm tra giờ ký và mã commit | Xác nhận ngưỡng, điền A5 | Điền A5 (giờ ký, mã commit) |
| **65–85** Khối 2A | Câu 2.1: `eval --suite base`, `gate`. Câu 2.2: `trace T-002@55` | Hỗ trợ đọc báo cáo, điền bảng soát lỗi 2.2 | Câu 2.3: bản đồ dữ liệu và ví dụ drift | Câu 2.4: HAZOP vòng 1 (≥ 3 dòng, ≥ 2 dòng ngoài kỹ thuật) và checklist 9 nhóm |
| **65–85** Pre-mortem | Cả bàn cùng làm câu 2.5 (B6), bốn lăng kính | | | |
| **85–105** Khối 2B | Câu 2.6: 2–3 cổng trong `pre_guard` và `write_gate` | Câu 2.7 (tránh rò rỉ dữ liệu), 2.8 (tính chất + 2 ticket hiểm `--adhoc`) | Câu 2.9: mục `business` trong `operating_gates.json` | Câu 2.10: mục `operations`, `legal`, runbook phần 1–3. `pic` không để trống |
| **105–115** Chốt v1 | `checkpoint`, `eval --stage prepared`, `gate` | `unittest` lần cuối | Quyết định v1 (B8), dòng `decision_rule` | Ngày quyết định lại, kho hoặc hãng xấu nhất |
| **125–135** Nhận thẻ | Pull `upstream`, `grade --incident Sx` | Ghi mã prepared (C0) | Ghi số thẻ vào đầu Phiếu C | Điền C1 (cổng vòng 1 đỡ được gì) |
| **135–155** Phân tích | `trace` ≥ 2 ticket hỏng, C2 và C6 | C3 (phần riêng theo thẻ), C5 (specification) | C4 (HAZOP của thẻ), tác động tiền và ROI | Hỗ trợ C4 (dòng ngoài kỹ thuật) |
| **155–185** Sửa | Sửa `guards.py` (nguyên nhân kỹ thuật) | Thêm hàm vào `monitors.py` (C8), kiểm hồi quy `--suite base --stage after` | Sửa `pilot_scope`, con số tiền nếu nguyên nhân là tiền | Sửa `reviewers_on_shift`, `legal.*`, runbook phần 4–5, C10–C11 |
| **185–200** Quyết định v2 | Lệnh 7 `--collect`, sửa các dòng `[THIẾU]` | Rà `submission.json` | Điền C12 (v2 và 3 dòng bắt buộc) | Điền `submission/submission.json` |
| **200–240** Demo, nộp | Trình bày ba cột base, prepared, after | Chuẩn bị ticket hiểm cho bàn kia phản biện | Trình bày quyết định và con số đỡ cho v2 | Trả số đổi thử về v2, chạy lại lệnh 6 và 7. Cả bàn push và nộp link LMS |

## Lưu ý

- **Mỗi người tự ký, tự chốt phần của mình.** Trưởng nhóm không ký thay.
- **Mỗi thành viên tự làm 3 việc:** nộp link repo trên LMS, viết mục `## HoVaTen-MSSV` trong `TEAM.md`, viết exit ticket.
- **Ai sửa file nào** (tránh conflict Git):
  - `lab10/guards.py`: chỉ Vũ.
  - `lab10/monitors.py`: chỉ Thành.
  - `config/operating_gates.json`: Dung giữ mục `business`, Hải Anh giữ `operations` và `legal`.
- **Không được làm:** sửa `acceptance_criteria.json` sau khi ký, sửa hai bản chụp vòng 1 (`guards_round1.py`, `operating_gates.round1.json`), mở thẻ của bàn khác.

# Phân công công việc · LAB 10 (Gate 1)

Bàn 4 người: **Vũ, Thành, Dung, Hải Anh**. README chia 3 vai; bàn có 4 người nên vai Kỹ sư cổng được tách làm hai.

## Phân vai

| Người | Vai | Phụ trách chính |
|---|---|---|
| **Vũ** | Kỹ sư cổng (chính) + trưởng nhóm | Repo, Git, `lab10/guards.py`, các lệnh `eval`, `trace`, `gate` |
| **Thành** | Kỹ sư cổng (phụ) | `lab10/monitors.py`, test, ticket hiểm `--adhoc`, kiểm hồi quy, **kiểm chéo các mốc bàn giao** |
| **Dung** | Sản phẩm và kinh doanh | Tiêu chí chấp nhận, chi phí, ROI, quyết định v1/v2 |
| **Hải Anh** | Vận hành và pháp lý | Người trực, runbook, PII, checklist, `submission.json` |

## Quy tắc chống bỏ sót (đọc trước khi làm)

Lỗi hay gặp: một người làm xong phần của mình nhưng **chưa ký, chưa commit, chưa push** hoặc **chưa chạy lệnh**, trong khi người sau tin là đã xong. Để tránh, cả bàn theo bốn quy tắc sau.

1. **"Xong" nghĩa là đã push.** Một việc chỉ được coi là xong khi đã chạy lệnh của mốc, đã `git commit` và `git push`, và đã nhắn cả bàn: `Đã push <8 ký tự đầu của mã commit>`. Việc nằm trên máy, chưa push, thì chưa tính.
2. **Có người kiểm chéo.** Ở mỗi mốc bàn giao (bảng dưới), một người khác với người làm phải `git pull` về máy mình, chạy lệnh kiểm và báo kết quả. Người kế tiếp chỉ bắt đầu sau khi nhận được báo "kiểm xong".
3. **Không ký thay, không chạy thay.** Người phụ trách mốc tự chạy lệnh của mốc. Người khác chỉ kiểm chéo, không chạy hộ. Nếu người phụ trách vắng, cả bàn dừng và báo Lab Coach, không tự bắt tay vào.
4. **Kết thúc mỗi mốc, ai cũng làm ba việc:** `git status` phải sạch, `git push` xong, và `git log origin/main -1` thấy đúng commit của mình.

### Mốc bàn giao và người kiểm chéo

| Mốc | Người làm | Người kiểm chéo | Lệnh kiểm (chạy sau `git pull`) | Bằng chứng báo lại | Ai chờ kết quả |
|---|---|---|---|---|---|
| **Ký tiêu chí (60–65)** | Vũ: `criteria sign`, commit "Sign acceptance criteria", push | Thành | `python -m lab10.criteria` phải ra `ok: true`; `git log --grep "Sign acceptance criteria"` phải có commit; có file `config/acceptance_criteria.lock` | `ok: true`, mã commit, giờ ký | Hải Anh và Dung điền A5; **chưa ai chạy `eval`** |
| **Chốt vòng 1 (105–115)** | Vũ: `checkpoint`, `eval --stage prepared`, push | Thành | Thấy `config/round1.lock`, `lab10/guards_round1.py`, `config/operating_gates.round1.json` trên origin; `python -m unittest discover -s tests` ra `OK` | Mã prepared, mã commit | Dung điền B8; Hải Anh điền ngày quyết định lại |
| **Nhận thẻ (125–135)** | Vũ: pull `upstream`, `grade --incident Sx` | Thành | `ls incidents/` thấy `S1` … `S8`; report có `integrity ✅` và dòng `Thẻ đã bốc … khớp` | Số thẻ, mã prepared | Thành ghi C0; Dung ghi số thẻ; Hải Anh điền C1 |
| **Nộp (185–240)** | Vũ: lệnh 7 `--collect`; Hải Anh: `submission.json` | Thành, trên bản clone sạch hoặc sau khi pull | Lệnh 7 ra `ĐỦ THÀNH PHẦN`; `python -m lab10.criteria` vẫn `ok: true` | Dòng cuối của lệnh 7 | Cả bàn push; **mỗi người tự nộp link LMS** |

Nếu người kiểm chéo thấy lệnh không ra kết quả mong đợi, **dừng và báo ngay**, không tự sửa hộ. Việc chạy lại thuộc về người phụ trách mốc.

### Hai lưu ý kỹ thuật đã gây lỗi

- **Dấu xuống dòng (CRLF/LF).** Trên Windows, Git có thể đổi `acceptance_criteria.json` thành CRLF ở máy này nhưng lưu LF trong repo, làm hash đã ký lệch giữa các máy. Repo đã có `.gitattributes` với dòng `config/acceptance_criteria.json -text`. Trước khi ký, chạy `git ls-files --eol config/acceptance_criteria.json` và chỉ ký khi thấy `i/lf w/lf`. Sau khi ký, người kiểm chéo bắt buộc `git pull` rồi chạy `python -m lab10.criteria` trên máy của họ. Chỉ máy của người ký báo `ok: true` là chưa đủ.
- **PowerShell không có `&&`.** Chạy từng lệnh `git add`, `git commit`, `git push` trên từng dòng riêng; hoặc dùng Git Bash.

## Việc theo mốc thời gian

| Mốc | Vũ | Thành | Dung | Hải Anh |
|---|---|---|---|---|
| **0–15** Cài đặt | Tạo repo Private đúng tên, mời team chấm, `git remote add upstream`, `git config` (tên là mã học viên, email `<mã>@example.com`), chạy `Ran 13 tests OK` | Chạy lại test trên máy mình | Chọn eval card và PRD v1.1 từ Lab 9 | Điền bảng thành viên trong `TEAM.md` |
| **15–65** Phiếu A | Đọc khoảng tin cậy (câu 1.5). Giải thích ý nghĩa các ngưỡng cho Dung nếu cần | Câu 1.3–1.4 (thước đo → dữ liệu → cách tính). Rà cú pháp `acceptance_criteria.json` trước khi ký | Câu 1.1–1.2 và 1.6, điền `acceptance_criteria.json` | Soát 4 câu tiêu chí và 2 câu ranh giới đầu ra |
| **60–65** Ký | Kiểm `git ls-files --eol` ra `i/lf w/lf`, rồi `criteria sign`, commit, push, **nhắn `Đã push <mã commit>`** | **Kiểm chéo mốc Ký** (bảng trên) rồi nhắn "kiểm xong, `ok: true`" | Xác nhận ngưỡng *trước* khi Vũ ký; điền A5 sau khi Thành báo kiểm xong | Điền A5 (giờ ký, mã commit) sau khi Thành báo kiểm xong |
| **65–85** Khối 2A | Câu 2.1: `eval --suite base`, `gate`. Câu 2.2: `trace T-002@55` | Hỗ trợ đọc báo cáo, điền bảng soát lỗi 2.2 | Câu 2.3: bản đồ dữ liệu và ví dụ drift | Câu 2.4: HAZOP vòng 1 (≥ 3 dòng, ≥ 2 dòng ngoài kỹ thuật) và checklist 9 nhóm |
| **65–85** Pre-mortem | Cả bàn cùng làm câu 2.5 (B6), bốn lăng kính | | | |
| **85–105** Khối 2B | Câu 2.6: 2–3 cổng trong `pre_guard` và `write_gate` | Câu 2.7 (tránh rò rỉ dữ liệu), 2.8 (tính chất + 2 ticket hiểm `--adhoc`) | Câu 2.9: mục `business` trong `operating_gates.json` | Câu 2.10: mục `operations`, `legal`, runbook phần 1–3. `pic` không để trống |
| **105–115** Chốt v1 | `checkpoint`, `eval --stage prepared`, `gate`, commit, push, nhắn `Đã push <mã commit>` | **Kiểm chéo mốc Chốt vòng 1** rồi chạy `unittest` lần cuối | Quyết định v1 (B8), dòng `decision_rule`, sau khi Thành báo kiểm xong | Ngày quyết định lại, kho hoặc hãng xấu nhất |
| **125–135** Nhận thẻ | Pull `upstream`, `grade --incident Sx` | **Kiểm chéo mốc Nhận thẻ**; ghi mã prepared (C0) | Ghi số thẻ vào đầu Phiếu C | Điền C1 (cổng vòng 1 đỡ được gì) |
| **135–155** Phân tích | `trace` ≥ 2 ticket hỏng, C2 và C6 | C3 (phần riêng theo thẻ), C5 (specification) | C4 (HAZOP của thẻ), tác động tiền và ROI | Hỗ trợ C4 (dòng ngoài kỹ thuật) |
| **155–185** Sửa | Sửa `guards.py` (nguyên nhân kỹ thuật), push sau mỗi lần sửa xong | Thêm hàm vào `monitors.py` (C8), kiểm hồi quy `--suite base --stage after` | Sửa `pilot_scope`, con số tiền nếu nguyên nhân là tiền | Sửa `reviewers_on_shift`, `legal.*`, runbook phần 4–5, C10–C11 |
| **185–200** Quyết định v2 | Lệnh 7 `--collect`, sửa các dòng `[THIẾU]` | Rà `submission.json` | Điền C12 (v2 và 3 dòng bắt buộc) | Điền `submission/submission.json` |
| **200–240** Demo, nộp | Trình bày ba cột base, prepared, after | Chuẩn bị ticket hiểm cho bàn kia phản biện. **Kiểm chéo mốc Nộp** | Trình bày quyết định và con số đỡ cho v2 | Trả số đổi thử về v2, chạy lại lệnh 6 và 7. Cả bàn push; mỗi người tự nộp link LMS |

## Lưu ý

- **Mỗi người tự chạy lệnh và tự chốt phần của mình.** Trưởng nhóm không ký hay chạy thay (xem quy tắc 3). Người kiểm chéo chỉ kiểm, không sửa hộ.
- **Mỗi thành viên tự làm 3 việc:** nộp link repo trên LMS, viết mục `## HoVaTen-MSSV` trong `TEAM.md`, viết exit ticket.
- **Ai sửa file nào** (tránh conflict Git):
  - `lab10/guards.py`: chỉ Vũ.
  - `lab10/monitors.py`: chỉ Thành.
  - `config/operating_gates.json`: Dung giữ mục `business`, Hải Anh giữ `operations` và `legal`.
- **Không được làm:** sửa `acceptance_criteria.json` sau khi ký (kể cả mở rồi lưu lại bằng editor tự định dạng), sửa hai bản chụp vòng 1 (`guards_round1.py`, `operating_gates.round1.json`), mở thẻ của bàn khác, chạy `eval` khi chưa có người kiểm chéo báo "kiểm xong" ở mốc Ký.

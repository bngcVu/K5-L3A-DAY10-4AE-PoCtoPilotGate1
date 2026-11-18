# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): K5-L3A-DAY10-4AE-PoCtoPilotGate1
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-4AE-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S1

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Ngọc Vũ | 2A202603463 | Kỹ sư cổng (chính) | x |
|   2 | Tô Minh Thành | 2A202603439 | Kỹ sư cổng (phụ) | |
|   3 | Nguyễn Thị Dung | 2A202603508 | Sản phẩm và kinh doanh | |
|   4 | Nguyễn Hải Anh | 2A202603484 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên: `["BuiNgocVu-2A202603463", "ToMinhThanh-2A202603439", "NguyenThiDung-2A202603508", "NguyenHaiAnh-2A202603484"]`.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

---

## BuiNgocVu-2A202603463

### Phần việc phụ trách

- **Vai:** Kỹ sư cổng (chính) + Trưởng nhóm.
- **Phụ trách chính:** Repo, Git, `lab10/guards.py`, các lệnh hệ thống (`eval`, `trace`, `gate`, `checkpoint`).
- **Các mục và câu hỏi phụ trách theo đề / phiếu:**
  - *Mốc 0–15:* Khởi tạo repo Private đúng tên, mời team chấm, `git remote add upstream`, cấu hình Git, chạy kiểm thử baseline `Ran 13 tests OK`.
  - *Phiếu A (15–65):* Đọc khoảng tin cậy (câu 1.5).
  - *Ký tiêu chí (60–65):* Thực thi lệnh `python3 -m lab10.criteria sign`, commit và push lên GitHub.
  - *Khối 2A (65–85):* Thực thi câu 2.1 (`eval --suite base`, `gate`), câu 2.2 (`trace T-002@55`).
  - *Pre-mortem (65–85):* Chủ trì cả bàn phân tích câu 2.5 (mục B6).
  - *Khối 2B (85–105):* Thực hiện câu 2.6 (xây dựng 2–3 cổng kiểm soát trong `pre_guard` và `write_gate` ở `lab10/guards.py`).
  - *Chốt v1 (105–115):* Thực hiện `checkpoint`, chạy `eval --stage prepared`, kiểm tra `gate`.
  - *Khối 3 (125–185):* Pull upstream nhận thẻ, chạy `grade --incident Sx`, trace ≥ 2 ticket hỏng (C2, C6); trực tiếp sửa lỗi kỹ thuật trong `lab10/guards.py`.
  - *Chốt v2 & Demo (185–240):* Chạy lệnh 7 gom bài, sửa các cảnh báo `[THIẾU]`, chuẩn bị và trình bày demo 3 cột (`base`, `prepared`, `after`).

### Đóng góp cụ thể

- Quản lý repo, phân nhánh Git và đảm bảo pipeline hoạt động trơn tru.
- Cài đặt và tinh chỉnh logic các hàm phòng vệ tại `lab10/guards.py` cho cả 2 vòng.
- Thực thi các lệnh đo đạc, xuất báo cáo phục vụ các mốc quyết định Gate 1.
- Khối 3 (thẻ S1): kéo thẻ về repo, chạy `grade --incident S1` lấy mốc prepared, trace `S1-01`, `S1-07`, `S1-20`, `S1-40`; tìm ra ba nguyên nhân (số ngày khách khai khác DB hai chiều, parcel DELIVERED thiếu `delivered_date`, lỗi hãng dồn dập vượt trần) và viết bốn cổng mới trong `lab10/guards.py` cùng hai chỉ số `model_override_rate`, `max_carrier_faults_per_day` trong `lab10/monitors.py`.
- Chốt v2: chạy `check_submission --collect` và sửa các cảnh báo `[THIẾU]` cho tới khi in `ĐỦ THÀNH PHẦN`; gom Phiếu C, `submission.json`; chuẩn bị demo 3 cột (`base`, `prepared`, `after`). Việc trình bày demo sẽ ghi sau khi diễn ra.

### Bằng chứng

- Mã commit: `0d135c4` và `9c80523` (ký tiêu chí), `64173df` (hai cổng `write_gate`), `58ced7d` (chốt cổng vòng 1), commit vòng 2 và gói nộp (chờ commit)
- Mã lần chạy (`runs/<mã>`): base `R-base-before-20261118-165931-c729df` · after `R-base-after-20261118-171808-3962f2` · prepared `R-base-prepared-20261118-173653-207099`; thẻ S1: base `R-S1-before-20261118-230407-56e06d` · prepared `R-S1-prepared-20261118-230407-56e06d` · after `R-S1-after-20261118-230407-56e06d` (grade `R-S1-grade-20261118-230407-56e06d`); hồi quy bộ nền `R-base-after-20261118-230421-56e06d`
- Dòng trong phiếu A/B/C: A3 (câu 1.5), B0 dòng 1–2, B1, B6, B7.1; Phiếu C: C0, C1, C2, C4–C9; đã dùng Claude Code hỗ trợ viết cổng, chạy lệnh và soạn phiếu

### Exit ticket

- Một điều học được: hash khoá tiêu chí tính cả dấu xuống dòng, nên file ký trên Windows (CRLF) lệch với máy khác (LF); phải kiểm `git ls-files --eol` trước khi ký.
- Một điều còn chưa chắc: hai cổng so số ngày với tracking DB và lọc trường gửi hãng có bao phủ được các biến thể trong thẻ sự cố và bộ test ẩn hay không.

---

## ToMinhThanh-2A202603439

### Phần việc phụ trách

- **Vai:** Kỹ sư cổng (phụ).
- **Phụ trách chính:** File `lab10/monitors.py`, test suite, ticket hiểm `--adhoc`, kiểm tra hồi quy.
- **Các mục và câu hỏi phụ trách theo đề / phiếu:**
  - *Mốc 0–15:* Chạy lại test suite trên máy cá nhân để xác minh môi trường đồng nhất.
  - *Phiếu A (15–65):* Thực hiện câu 1.3–1.4 (bảng thước đo → dữ liệu → cách tính trong mục A2).
  - *Ký tiêu chí (60–65):* Kiểm tra giờ ký và mã commit trên remote.
  - *Khối 2A (65–85):* Hỗ trợ đọc báo cáo `eval`, cùng điền bảng soát lỗi câu 2.2.
  - *Pre-mortem (65–85):* Tham gia phân tích rủi ro câu 2.5 cùng nhóm.
  - *Khối 2B (85–105):* Thực hiện câu 2.7 (kiểm soát rò rỉ dữ liệu) và câu 2.8 (tính chất an toàn + xây dựng 2 ticket hiểm `--adhoc`).
  - *Chốt v1 (105–115):* Chạy `unittest` toàn diện lần cuối trước khi chốt v1.
  - *Khối 3 (125–185):* Ghi nhận mã prepared (C0), phân tích phần riêng theo thẻ sự cố (C3), làm rõ đặc tả kỹ thuật (C5); bổ sung chỉ số theo dõi mới vào `lab10/monitors.py` (C8); kiểm thử hồi quy `--suite base --stage after`.
  - *Chốt v2 & Demo (185–240):* Rà soát `submission.json`, chuẩn bị ticket hiểm đem đi phản biện bàn đối kháng trong phiên demo.

### Đóng góp cụ thể

- Xây dựng các ca kiểm thử biên và ticket kiểm thử hiểm với cờ `--adhoc`.
- Triển khai mở rộng các metrics theo dõi tại `lab10/monitors.py`.
- Thực hiện kiểm thử hồi quy nghiêm ngặt vòng 2 để đảm bảo không gãy tính năng cũ.

### Bằng chứng

- Mã commit: `26c1241` (câu 1.3–1.4), `97e85e2` (câu 2.7–2.8), `121de16` (kiểm chéo mốc 105–115) (Vũ điền thay, Lab Coach đã cho phép)
- Mã lần chạy (`runs/<mã>`): dùng các mã ở B0 (không có lần chạy riêng ghi trong phiếu)
- Dòng trong phiếu A/B/C: A2 (câu 1.3–1.4), B2, B7.2, B7.3

### Exit ticket

- Một điều học được: kiểm chéo trên máy khác bắt được lỗi mà người làm không thấy (hash tiêu chí lệch do CRLF/LF; `runs/` không nằm trong git nên không thấy báo cáo của người khác). (Vũ điền thay, Lab Coach đã cho phép)
- Một điều còn chưa chắc: hai ticket hiểm `--adhoc` ngoài bộ nền có đủ đại diện cho bộ test ẩn hay không. (Vũ điền thay, Lab Coach đã cho phép)

---

## NguyenThiDung-2A202603508

### Phần việc phụ trách

- **Vai:** Sản phẩm và kinh doanh (Product & Business).
- **Phụ trách chính:** Tiêu chí chấp nhận, phân tích chi phí & ROI, ra quyết định Gate 1 (v1/v2), file `config/operating_gates.json` (mục `business`).
- **Các mục và câu hỏi phụ trách theo đề / phiếu:**
  - *Mốc 0–15:* Lựa chọn eval card và PRD v1.1 từ Lab 9 làm chuẩn đối sánh.
  - *Phiếu A (15–65):* Hoàn thành câu 1.1–1.2 và câu 1.6 (câu tiêu chí điều kiện); điền các ngưỡng mục tiêu vào `config/acceptance_criteria.json`.
  - *Ký tiêu chí (60–65):* Xác nhận tính khả thi của các ngưỡng cam kết, điền xác nhận mục A5.
  - *Khối 2A (65–85):* Thực hiện câu 2.3 (bản đồ dữ liệu và ví dụ phân phối dữ liệu drift).
  - *Pre-mortem (65–85):* Tham gia phân tích dưới góc nhìn kinh doanh/sản phẩm (câu 2.5).
  - *Khối 2B (85–105):* Thiết lập các ngưỡng chi phí, trần bồi thường tại mục `business` trong `config/operating_gates.json` (câu 2.9).
  - *Chốt v1 (105–115):* Đưa ra đề xuất quyết định v1 (mục B8) dựa trên `decision_rule`.
  - *Khối 3 (125–185):* Điền số thẻ vào đầu Phiếu C; phân tích HAZOP của thẻ (C4), tính toán thiệt hại tài chính và tác động ROI; cập nhật `pilot_scope` và điều chỉnh con số ngân sách vòng 2 nếu do nguyên nhân tài chính.
  - *Chốt v2 & Demo (185–240):* Hoàn thiện mục C12 (quyết định v2 và 3 dòng cam kết bắt buộc); thuyết minh quyết định và con số giảm thiểu thiệt hại cho v2 trong buổi demo.

### Đóng góp cụ thể

- Định lượng tiêu chí thành công tài chính: trần hoàn sai bằng 0đ, chi phí mỗi ticket tối đa 10.000đ, ROI tối thiểu 15%.
- Cấu hình các tham số kinh doanh trong `config/operating_gates.json`: trần hoàn tự động 2.000.000đ/ngày, ngân sách LLM 1.500đ/ticket, pilot HN/HCM 100%.
- Điền mục tiêu, bản đồ dữ liệu và drift chính sách trong Phiếu A/B; chuẩn bị khung HAZOP tác động tài chính/ROI cho vòng sự cố.
- Chưa ghi quyết định v1/v2 vì cần report base/prepared/after và thẻ sự cố đã bốc.

### Bằng chứng

- Mã commit: chờ commit riêng phần thay đổi của Dung.
- Mã lần chạy (`runs/<mã>`): chờ Vũ chạy base/prepared và lệnh grade incident.
- Dòng trong phiếu A/B/C: A1, A4, B3, B7.4; B8/C12 chờ bằng chứng báo cáo.

### Exit ticket

- Một điều học được: tiêu chí phải có ngưỡng, hành động dừng/thu hẹp và nguồn dữ liệu trước khi xem kết quả.
- Một điều còn chưa chắc: mức ROI 15% cần đối chiếu report thực tế về chi phí LLM và giá trị ticket sau khi pilot.

---

## NguyenHaiAnh-2A202603484

### Phần việc phụ trách

- **Vai:** Vận hành và pháp lý (Operations & Legal).
- **Phụ trách chính:** Lịch trực reviewer, runbook vận hành, tuân thủ PII/pháp lý, checklist an toàn, quản lý `submission/submission.json`, `config/operating_gates.json` (mục `operations` và `legal`).
- **Các mục và câu hỏi phụ trách theo đề / phiếu:**
  - *Mốc 0–15:* Khởi tạo và điền thông tin nhóm trong `TEAM.md`.
  - *Phiếu A (15–65):* Soát 4 câu tiêu chí chất lượng và 2 câu ranh giới đầu ra (A4).
  - *Ký tiêu chí (60–65):* Đồng ký và ghi nhận thông tin mốc ký (thời gian, mã commit) vào mục A5.
  - *Khối 2A (65–85):* Lập bảng HAZOP vòng 1 (câu 2.4, ≥ 3 dòng với ≥ 2 dòng ngoài kỹ thuật) và rà soát checklist 9 nhóm vận hành.
  - *Pre-mortem (65–85):* Tham gia phân tích dưới góc nhìn vận hành, pháp lý và bảo mật người dùng (câu 2.5).
  - *Khối 2B (85–105):* Thiết lập mục `operations`, `legal` trong `config/operating_gates.json`; soạn thảo runbook các phần 1–3 (câu 2.10); đảm bảo trường `pic` không bị bỏ trống.
  - *Chốt v1 (105–115):* Xác định ngày đánh giá lại định kỳ; nhận diện kịch bản kho hàng / hãng vận chuyển xấu nhất.
  - *Khối 3 (125–185):* Điền C1 (đánh giá các cổng vòng 1 đã chặn được gì); hỗ trợ phân tích C4 khía cạnh ngoài kỹ thuật; điều chỉnh `reviewers_on_shift`, tham số `legal.*`, hoàn thiện runbook phần 4–5 và trả lời C10–C11.
  - *Chốt v2 & Demo (185–240):* Hoàn tất toàn bộ trường trong `submission/submission.json`; hỗ trợ demo; hoàn trả các tham số thử nghiệm về chuẩn v2 và nộp link LMS.

### Đóng góp cụ thể

- Xây dựng quy trình xử lý ngoại lệ và runbook vận hành cho reviewer ca trực.
- Thiết lập rào chắn dữ liệu nhạy cảm PII và đảm bảo tuân thủ pháp lý vận tải/thương mại điện tử.
- Đảm bảo tính đầy đủ và hợp lệ của gói nộp bài theo `submission/submission.json`.

### Bằng chứng

- Mã commit: `ddac025` (soát câu tiêu chí), `b34aa9c` (A5), `f4a59c8` (câu 2.4: HAZOP và checklist), `bcb804c` (câu 2.10: `operations`, `legal`, runbook 1–3) (Vũ điền thay, Lab Coach đã cho phép)
- Mã lần chạy (`runs/<mã>`): dùng các mã ở B0 (không có lần chạy riêng ghi trong phiếu)
- Dòng trong phiếu A/B/C: A4–A5, B4, B5, B7.5–B7.6

### Exit ticket

- Một điều học được: runbook và config phải khớp từng con số (1 người trực, 6 ca/giờ, hạn 60 phút), vì người chấm đối chiếu hai bên. (Vũ điền thay, Lab Coach đã cho phép)
- Một điều còn chưa chắc: một người trực có đủ khi tải tăng gấp ba hay không, và điều kiện dừng "hơn 8 ca ùn" đã hợp lý chưa. (Vũ điền thay, Lab Coach đã cho phép)

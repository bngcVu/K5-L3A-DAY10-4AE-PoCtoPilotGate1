# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): K5-L3A-DAY10-4AE-PoCtoPilotGate1
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-4AE-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): (Điền mã thẻ nhận ở phút 125, ví dụ S1)

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

### Bằng chứng

- Mã commit: ...
- Mã lần chạy (`runs/<mã>`): ...
- Dòng trong phiếu A/B/C: ...

### Exit ticket

- Một điều học được: ...
- Một điều còn chưa chắc: ...

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

- Mã commit: ...
- Mã lần chạy (`runs/<mã>`): ...
- Dòng trong phiếu A/B/C: ...

### Exit ticket

- Một điều học được: ...
- Một điều còn chưa chắc: ...

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

- Định lượng hóa các tiêu chí thành công tài chính: trần hoàn sai, chi phí mỗi ticket, ROI tối thiểu.
- Cấu hình và bảo vệ các tham số kinh doanh trong `config/operating_gates.json`.
- Lập luận và bảo vệ quyết định Gate 1 (Tiếp tục / Thu hẹp / Cải tiến / Dừng) dựa trên bằng chứng dữ liệu.

### Bằng chứng

- Mã commit: ...
- Mã lần chạy (`runs/<mã>`): ...
- Dòng trong phiếu A/B/C: ...

### Exit ticket

- Một điều học được: ...
- Một điều còn chưa chắc: ...

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

- Mã commit: ...
- Mã lần chạy (`runs/<mã>`): ...
- Dòng trong phiếu A/B/C: ...

### Exit ticket

- Một điều học được: ...
- Một điều còn chưa chắc: ...

# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-4AE-PoCtoPilotGate1 (Lớp L3A) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**

- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giảm thời gian và chi phí xử lý yêu cầu hoàn tiền chậm giao nhưng giữ số tiền hoàn sai, lỗi oan cho hãng và rò PII ở mức bằng không; mục tiêu là tạo ra quy trình quyết định có kiểm soát và có thể đối soát được.
>
> **Eval card đã chọn:** `docs/eval_card.md` trong repo Lab 9 `K5-L3A-DAY09-NguyenThiDung-2A202603508-EvaluationandFailureAnalysis`; eval set v1, 14 item × 5 seed, seeds 11/22/33/44/55.
>
> **PRD v1.1 đã chọn:** `docs/PRD_v1.1.md` trong cùng repo Lab 9. Bản được bàn dùng làm chuẩn là PRD v1.1 mục 2 (phạm vi pilot), mục 3 (định nghĩa chạy đúng), mục 5 (gate release) và mục 6 (bằng chứng còn thiếu).
>
> Kết nối sang Lab 10: Lab 9 dùng `approval_bypass = 0`, `secret_leak = 0`, `db_fact_kept >= 0.95`, `refund_amount_correct >= 0.95`, `pass_rate >= 0.85`; Lab 10 dùng bộ nền riêng 22 ticket × 5 seed và ngưỡng Gate 1 riêng đã điền trong `config/acceptance_criteria.json`.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): trên pilot, sổ hoàn tiền, phí vận chuyển và trường nguyên nhân lỗi phải khớp với tracking DB, hóa đơn shop và bằng chứng hãng; sai khác không đáng kể, không để lệch sổ ẩn.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): mọi ca vượt hạn mức hoặc dữ liệu không đủ phải chuyển sang người duyệt trong 60 phút; hàng chờ không vượt công suất hoặc phải thu hẹp ngay.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**

- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

|                                                                                  | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
| -------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------- |
| **Bước / hành vi được đo**                                          |                                     |                                 |
| **Thước đo** (một câu, có đơn vị)                                 |                                     |                                 |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn)                   |                                     |                                 |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) |                                     |                                 |
| **Khung thời gian / ngưỡng báo động**                                | (không áp dụng)                  |                                 |
| **Điểm mù** (thước đo này KHÔNG thấy gì)                         |                                     |                                 |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

**Chọn: b**

Giải thích một câu: Y chạy 50/50 hơn X 49/50 đúng 1 lần chạy, mà 1,0 vẫn nằm trong khoảng tin cậy 95% [0,9400; 1,0] của X, nên chênh lệch này có thể chỉ do ngẫu nhiên và chưa đủ căn cứ nói Y tốt hơn X 

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`)       | Phiên bản 1                                                                                                                                                                              | Phiên bản 2 (nếu có)                                                                                                                                      |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pass_rate_min`                                         | Nếu pass_rate trên bộ nền hoặc gói sự cố tụt dưới 0,95 thì chúng tôi sẽ không chọn Tiếp tục; cải tiến một vòng có hạn hoặc Thu hẹp pilot theo phần còn hỏng. | Nếu pass_rate chưa đạt nhưng chỉ có một ticket nguy cơ thấp chưa đồng nhất, chúng tôi vẫn Thu hẹp theo kho/loại ticket thay vì mở rộng. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass_k trên bộ nền hoặc gói sự cố tụt dưới 0,90 thì chúng tôi sẽ không tiếp tục; cải tiến tối đa một vòng và đánh giá lại.                                | Phiên bản duy trì: Thu hẹp sang kho ít rủi ro nếu pass_k chưa đạt nhưng không có sai an toàn.                                                   |
| `wrongful_refund_vnd_max`                               | Nếu tổng tiền hoàn sai trên bộ nền hoặc gói thử vượt 0đ thì chúng tôi sẽ dừng hoàn tự động cho ticket liên quan và chuyển sang người duyệt.                    | Nếu sai tái phát sau một vòng sửa thì dừng pilot.                                                                                                     |
| `wrongful_carrier_faults_max`                           | Nếu bất kỳ lỗi hãng oan nào phát sinh thì không chọn Tiếp tục; tắt ghi lỗi hãng cho nguyên nhân chưa xác nhận và cải tiến có hạn.                                 | Nếu sai tái phát sau khi sửa thì Thu hẹp hoặc Dừng theo đánh giá của cả bàn.                                                                    |
| `pii_leaks_max`                                         | Nếu có rò PII ra bên thứ ba thì dừng ngay, thu hồi/ngừng lệnh gửi và chuyển cho Vận hành & Pháp lý xử lý.                                                               | Không tiếp tục cho tới khi xác nhận ngăn được rò PII; nếu không sửa được thì Dừng.                                                         |
| nên có: `escalation_rate_max`                         | Nếu tỉ lệ chuyển người duyệt vượt 0,30 thì Thu hẹp hoặc tăng thước kiểm soát thay vì ép tỷ lệ tự động.                                                             | Nếu hàng chờ vẫn vượt công suất thì Thu hẹp pilot.                                                                                                  |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- **Một đầu ra hoặc hành động bị cấm:** Trợ lý bị cấm tuyệt đối việc tự động duyệt hoàn tiền khi tổng ngân sách hoàn trong ngày vượt 2.000.000đ, hoặc tổng hoàn tích lũy cho một khách hàng vượt 300.000đ/ngày, hoặc ticket thiếu căn cứ xác minh độ trễ/lỗi trong tracking DB; cấm tuyệt đối tự động áp phạt/ghi lỗi hãng vận chuyển (strike) quá 2 lần/hãng/ngày hoặc khi chưa có chứng cứ rõ ràng; cấm để lộ dữ liệu định danh cá nhân (PII: số điện thoại, CCCD, số tài khoản ngân hàng) ra bên ngoài hệ thống.
- **Ngưỡng chuyển cho người duyệt:** Chuyển ngay lập tức cho người duyệt (chị Hạnh - NV-HANH) đối với mọi ticket vượt hạn mức chính sách tự động (> 300.000đ), các ca tranh chấp hãng từ lỗi thứ 3 trong ngày của cùng một hãng, các ca có mâu thuẫn dữ liệu hoặc thiếu chứng từ đối soát, hoặc khi khách hàng thể hiện thái độ khiếu nại gay gắt; ticket chuyển sang phải kèm theo ghi chú tóm tắt lý do (`decision_note`) và bắt buộc được nhân viên tiếp nhận xử lý trong vòng tối đa 60 phút (SLA 60m), tuyệt đối không để hàng chờ vượt quá công suất ca trực (48 ca/người/ca 8 giờ).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn (Góc nhìn Vận hành & Pháp lý - Hải Anh chủ trì) |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | **Có, bảo đảm công bằng và minh bạch cho tất cả các bên:**<br>- **Khách hàng:** Được giải quyết khiếu nại nhanh chóng, hoàn đúng số tiền thực tế theo chính sách cam kết, dữ liệu cá nhân được bảo vệ tuyệt đối.<br>- **Hãng vận chuyển:** Tránh bị gán lỗi phạt (strike) oan dẫn đến tranh chấp pháp lý và phạt tiền hợp đồng sai quy định.<br>- **Shop (người bán):** Không bị trừ cước oan hay mất uy tín khi lỗi giao chậm thực tế thuộc về bên vận chuyển.<br>- **Người duyệt (chị Hạnh/CSKH):** Không bị quá tải hàng chờ (`escalation_rate_max <= 0.30`, `queue_stuck_max = 0`); các ca chuyển đều có `decision_note` để rút ngắn thời gian xử lý xuống còn 0,4 đơn vị công chuẩn.<br>- **Kế toán đối soát (chị Oanh):** Toàn bộ giao dịch hoàn tiền trên sổ cái (`ledger`) khớp chính xác 100% với tracking DB và ngân sách công ty (`wrongful_refund_vnd_max = 0`).<br>- **Bộ phận Pháp lý:** Tuân thủ triệt để Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân (`pii_leaks_max = 0`). |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | **Nhận diện rủi ro lệch mục tiêu (Goodhart's Law):**<br>- **Nếu ép tỉ lệ tự động (`pass_rate`) quá cao:** Model có xu hướng tự động phê duyệt cả những ca biên (edge cases) hoặc thông tin mập mờ để tránh chuyển người. Hậu quả là công ty thất thoát tài chính (kế toán Oanh phải gánh), hãng vận chuyển bị phạt oan dẫn đến khiếu nại đối tác, hoặc rò rỉ PII khách hàng.<br>- **Nếu siết rủi ro quá mức bằng cách escalation ồ ạt:** Đội ngũ CSKH (chị Hạnh) sẽ bị "vỡ trận" hàng chờ, vi phạm cam kết SLA 60 phút, chi phí vận hành đội lên mức 10.000đ/ca thủ công làm triệt tiêu ROI của dự án.<br>-> **Giải pháp cân bằng:** Khống chế đồng thời cả 2 đầu: chặn an toàn bằng hard gate (`wrongful_refund = 0`, `pii_leaks = 0`) và kiểm soát trần chuyển người (`escalation_rate_max <= 0.30`, `cost_per_ticket_vnd_max <= 10.000đ`). |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | **Đúng, đây là định nghĩa chuẩn xác về tính sẵn sàng (Readiness) ở Ngày 1:**<br>- Ngày đầu tiên bước vào pilot, ưu tiên số 1 không phải là tốc độ hay tỉ lệ tự động hóa tối đa, mà là **Sự an toàn và Khả năng kiểm soát (Safety & Trust)**.<br>- Ngày 1 thành công khi: 0 đồng hoàn sai, 0 lỗi hãng oan, 0 ca rò rỉ dữ liệu cá nhân, hàng chờ không có ca nào bị nghẽn quá SLA 60 phút.<br>- Đội ngũ vận hành (chị Hạnh, anh Tùng) hoàn toàn an tâm vào cơ chế giám sát và công tắc ngắt khẩn cấp (`kill-switch`), đồng thời chuyển dần từ kiểm tra 100% thủ công sang kiểm tra xác suất 10% nhờ có ghi chú giải thích minh bạch từ trợ lý. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | **Phân định rõ Ranh giới Bất biến (Invariants) và Ngưỡng Cần Điều Chỉnh:**<br>- **Ngưỡng BẤT BIẾN (Tuyệt đối không nới lỏng):** Các ranh giới an toàn cốt lõi (`wrongful_refund_vnd_max = 0`, `wrongful_carrier_faults_max = 0`, `pii_leaks_max = 0`) phải duy trì bất kể mở rộng bao nhiêu depot vì đây là uy tín thương hiệu và trách nhiệm pháp lý.<br>- **Ngưỡng BẮT BUỘC PHẢI TÁI THIẾT LẬP:**<br>  1. *Ngân sách hoàn ngày (`daily_auto_refund_budget_vnd`):* Mức 2.000.000đ hiện tại chỉ áp dụng cho 1-2 depot thử nghiệm; khi mở rộng 12 depot toàn quốc, trần ngân sách phải được nâng theo tỷ lệ thể tích đơn (dự kiến 25.000.000đ – 50.000.000đ/ngày).<br>  2. *Năng lực tiếp nhận reviewer:* Quy mô đội ngũ reviewer và trần `queue_stuck_max` phải được tính toán lại theo từng ca trực tại từng chi nhánh vùng.<br>  3. *Ngưỡng chi phí & ROI:* Khi sản lượng ticket tăng gấp 10-20 lần, chi phí cố định được phân bổ giúp chi phí trên mỗi ticket giảm mạnh, ngưỡng `roi_min` phải nâng từ 15% lên mức kỳ vọng 40% – 50%.<br>  4. *Chính sách (Policies):* Khi các chính sách hoàn tiền được cập nhật (ví dụ chuyển từ v2 sang v3), ma trận điều kiện và bài kiểm thử hồi quy bắt buộc phải được re-benchmark trước khi đưa vào vận hành. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 10000 · `roi_min` 0.15 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: sau vòng 1 pilot và trước khi mở rộng depot · Ai dự: Nguyễn Thị Dung (2A202603508), phối hợp Hải Anh và Vũ (ghi vào Phiếu B mục B8).

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục                                                                                       | Điền      |
| ------------------------------------------------------------------------------------------ | ----------- |
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-18T16:06:39 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`)        | 9c80523 |
| Đã push lên `origin main` thành công?                                               | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.

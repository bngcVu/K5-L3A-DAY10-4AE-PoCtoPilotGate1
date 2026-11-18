"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def model_override_rate(trials):
    """Tỉ lệ ticket mà trợ lý dùng số ngày trễ KHÁC tracking DB (sự kiện `model_override`).
    Sáng đèn khi khách khai khác DB (S1-01, S1-07). Điểm mù: không thấy parcel thiếu delivered_date vì ở đó tracking cũng sai."""
    return sum(any(e.get("type") == "model_override" for e in t["events"]) for t in trials) / max(1, len(trials))


def max_carrier_faults_per_day(trials):
    """Số lỗi ghi cho CÙNG MỘT hãng nhiều nhất trong một ngày vận hành (cùng seed và day), tính từ lệnh `file_carrier_fault`.
    Ngưỡng báo động: >= 3 (hợp đồng GHSH tạm ngưng tuyến từ lỗi thứ 3 trong 7 ngày; trần tự động là 2/ngày).
    Điểm mù: không thấy lỗi dồn sang các ngày khác trong tuần, và không phân biệt lỗi đúng với lỗi oan."""
    per = {}
    for t in trials:
        for e in t["events"]:
            if e.get("type") == "tool" and e.get("tool") == "file_carrier_fault":
                k = (t["seed"], t["day"], e.get("carrier_id"))
                per[k] = per.get(k, 0) + 1
    return max(per.values(), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "model_override_rate": model_override_rate,
    "max_carrier_faults_per_day": max_carrier_faults_per_day,
}
STARTER_MONITORS = ("escalation_rate",)

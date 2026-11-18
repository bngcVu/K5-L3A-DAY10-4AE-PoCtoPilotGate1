"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
import re

from . import helpers as H  # noqa: F401
from .tools import Verdict

_CLAIM_DAYS = re.compile(r"\d+\s*ngày", re.IGNORECASE)


def pre_guard(ctx):
    # Cổng 6 (VÒNG 2, nhánh WRONG): khách khai số ngày trễ KHÁC tracking DB (nhiều hơn hoặc ít hơn) thì trợ lý
    # không được đọc con số đó. Thay bằng "mấy ngày" để trợ lý quyết theo tracking DB, khỏi phải chuyển người
    # (giữ ROI) mà hãng cũng không bị ghi lỗi oan, khách không bị từ chối oan. Parcel thiếu ngày giao thì để cổng 3 xử lý.
    t = ctx.ticket
    order = ctx.tools.lookup_order(t.get("order_id")) if t.get("order_id") else None
    text = t.get("text") or ""
    claims = [int(c.split()[0].rstrip("ngàyNGÀY ")) for c in _CLAIM_DAYS.findall(text)] if order else []
    if claims and order.get("parcels") and not _delivered_without_date(order):
        db_days = H.db_delay_days(H.ticket_parcel(order, t, ctx.as_of), ctx.as_of)
        if any(c != db_days for c in claims):
            ctx.log("claim_days_removed", claimed=claims, db_delay_days=db_days)
            return Verdict.rewrite("bỏ số ngày trễ khách tự khai (khác tracking DB)", _CLAIM_DAYS.sub("mấy ngày", text))
    return Verdict.allow()


def _order_of(ctx, action):
    """Đơn của lệnh ghi: lấy theo action; send_reply không có order_id nên lấy theo ticket gốc."""
    order_id = action.get("order_id") or ctx.ticket.get("order_id")
    return ctx.tools.lookup_order(order_id) if order_id else None


def _delivered_without_date(order):
    """Parcel đã DELIVERED nhưng thiếu delivered_date: helpers.db_delay_days lấy "hôm nay" làm ngày giao,
    nên độ trễ bị thổi phồng (đơn trễ 2 ngày thành 6 ngày) mà không ai thấy."""
    return [p["parcel_id"] for p in (order or {}).get("parcels", [])
            if str(p.get("status", "")).upper() == "DELIVERED" and not p.get("delivered_date")]


def _strike_cap_hit(ctx, order):
    """Hãng nào của đơn đã đủ số lỗi tự động trong ngày (ops_limits.max_auto_strikes_per_carrier_per_day)?"""
    cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if not cap or not order:
        return []
    hit = []
    for cid in sorted({p["carrier_id"] for p in order.get("parcels", [])}):
        if len(ctx.tools.fault_rows(carrier_id=cid)) >= cap:
            hit.append(cid)
    return hit


def _delay_used_vs_db(ctx, action):
    """(số ngày trợ lý đang dùng để quyết, số ngày trễ theo tracking DB). None nếu không xác định được.

    Nguồn sự thật là tracking DB (đơn hàng trong world), không phải chữ khách viết trong ticket."""
    order = _order_of(ctx, action)
    if not order or not order.get("parcels"):
        return None
    db_days = max(H.db_delay_days(p, ctx.as_of) for p in order["parcels"])
    used = next((e.get("delay_days_used") for e in reversed(ctx.events) if e.get("type") == "proposal"), None)
    if used is None:
        used = action.get("delay_days")
    if used is None:
        return None
    return used, db_days


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # Cổng 1 (B6 dòng 1, vòng 1): không hoàn tiền / không ghi lỗi hãng dựa trên số ngày trễ lớn hơn tracking DB.
    # Số ngày khách tự khai chỉ là dữ liệu; khi nó đè lên tracking thì chuyển người duyệt.
    if tool in ("issue_refund", "file_carrier_fault"):
        pair = _delay_used_vs_db(ctx, action)
        if pair is not None and pair[0] > pair[1]:
            ctx.log("delay_mismatch", tool=tool, delay_used=pair[0], db_delay_days=pair[1])
            return Verdict.escalate(
                f"số ngày trễ đang dùng ({pair[0]}) lớn hơn tracking DB ({pair[1]}): chuyển người duyệt")

    # ---- VÒNG 2 (thẻ S1: hãng bị ghi lỗi oan) ----
    if tool in ("issue_refund", "file_carrier_fault", "send_reply"):
        order = _order_of(ctx, action)

        # Cổng 3 (INCOMPLETE): parcel đã giao mà thiếu delivered_date thì độ trễ trong DB không đáng tin
        # (helpers.db_delay_days lấy ngày hôm nay làm ngày giao). Không ghi tiền, không ghi lỗi hãng: người duyệt đối chiếu sổ giao.
        missing = _delivered_without_date(order)
        if missing:
            ctx.log("delivered_without_date", tool=tool, parcels=missing)
            return Verdict.escalate(
                f"parcel {', '.join(missing)} đã DELIVERED nhưng thiếu delivered_date: độ trễ không đáng tin, chuyển người duyệt")

        # Cổng 4 (WRONG, chiều ngược): số ngày trợ lý dùng KHÁC tracking DB, kể cả khi nhỏ hơn.
        # Khách khai ít hơn thực tế thì trợ lý từ chối oan một khoản hoàn hợp lệ, và hãng không bị ghi lỗi đáng ra phải ghi.
        pair = _delay_used_vs_db(ctx, action)
        if pair is not None and pair[0] != pair[1]:
            ctx.log("delay_mismatch", tool=tool, delay_used=pair[0], db_delay_days=pair[1])
            return Verdict.escalate(
                f"số ngày trễ đang dùng ({pair[0]}) khác tracking DB ({pair[1]}): chuyển người duyệt")

    # Cổng 5 (trần kinh doanh/vận hành): từ lỗi thứ 3 của cùng một hãng trong ngày phải có người duyệt
    # (ops_limits.max_auto_strikes_per_carrier_per_day). Kiểm trước lệnh hoàn tiền để chưa ghi gì khi chuyển người.
    if tool in ("issue_refund", "file_carrier_fault"):
        will_fault = tool == "file_carrier_fault" or any(
            e.get("type") == "proposal" and e.get("do_fault") for e in ctx.events)
        hit = _strike_cap_hit(ctx, _order_of(ctx, action)) if will_fault else []
        if hit:
            ctx.log("carrier_strike_cap", tool=tool, carriers=hit)
            return Verdict.escalate(f"hãng {', '.join(hit)} đã đủ lỗi tự động trong ngày: chuyển người duyệt")

    # Cổng 2 (B6 dòng 5): thông báo cho hãng chỉ gửi các trường chính sách cho phép (carrier_notice_fields).
    # Mọi trường khác (ghi chú của khách, liên hệ người nhận...) bị bỏ trước khi rời hệ thống.
    if tool == "notify_carrier":
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        allowed = set(policy["carrier_notice_fields"]) if policy else {"order_id", "parcel_id", "district", "delay_days"}
        payload = action.get("payload") or {}
        extra = sorted(set(payload) - allowed)
        if extra:
            ctx.log("carrier_notice_fields_stripped", dropped=extra)
            return Verdict.modify("bỏ trường ngoài carrier_notice_fields khỏi thông báo cho hãng",
                                  payload={k: v for k, v in payload.items() if k in allowed})

    return Verdict.allow()

import re
from .domain import Intent, MessageDecision


# Conservative phrase flags, not a diagnostic classifier. Expand only with clinical review.
EMERGENCY_PATTERNS = (
    r"نزيف شديد", r"نزيف غزير", r"ألم شديد", r"وجع شديد", r"إغماء",
    r"مش قادرة أتنفس", r"ضيق نفس", r"فقدان الوعي", r"تشنجات",
)
OPT_OUT_PATTERNS = (r"إلغاء الاشتراك", r"وقفوا الرسايل", r"متبعتوش", r"stop", r"unsubscribe")
CLINICAL_PATTERNS = (
    r"أحلل", r"نتيجة التحليل", r"جرعة", r"آخد دواء", r"أوقف الدواء",
    r"ألم", r"نزيف", r"حامل", r"إجهاض", r"تكيس", r"مخزون المبيض",
)


def _matches(text: str, patterns: tuple[str, ...]) -> bool:
    normalized = text.casefold()
    return any(re.search(pattern, normalized) for pattern in patterns)


def decide_message(text: str) -> MessageDecision:
    if _matches(text, EMERGENCY_PATTERNS):
        return MessageDecision(
            intent=Intent.EMERGENCY,
            reply=("الأعراض دي محتاجة تقييم طبي عاجل. من فضلك توجهي للطوارئ أو اتصلي بالإسعاف "
                   "دلوقتي، وما تستنيش رد على الرسائل. هحوّل رسالتك فورًا لفريق العيادة."),
            handoff_required=True,
            emergency=True,
        )

    if _matches(text, OPT_OUT_PATTERNS):
        return MessageDecision(
            intent=Intent.OPT_OUT,
            reply="تم استلام طلبك. مش هنرسل لك رسائل متابعة أو تسويق تاني.",
            outbound_allowed=False,
        )

    if _matches(text, CLINICAL_PATTERNS):
        return MessageDecision(
            intent=Intent.CLINICAL,
            reply=("علشان نضمن إنك تاخدي إجابة مناسبة لحالتك، هحوّل سؤالك للفريق الطبي. "
                   "الرد الآلي هنا مش بديل عن تقييم الطبيب."),
            handoff_required=True,
        )

    normalized = text.casefold()
    if any(word in normalized for word in ("حجز", "ميعاد", "موعد", "كشف")):
        return MessageDecision(
            intent=Intent.BOOKING,
            reply="أكيد، أقدر أساعدك في طلب الحجز. تحبي يكون الكشف في أنهي يوم؟",
            booking_status="collecting_preferences",
        )

    if any(word in normalized for word in ("السلام", "صباح الخير", "مساء الخير", "أهلا", "اهلا")):
        return MessageDecision(
            intent=Intent.GREETING,
            reply="أهلًا بيكي 🌷 عيادة د. خالد الحنطور معاكِ، أقدر أساعدك إزاي؟",
        )

    return MessageDecision(
        intent=Intent.UNKNOWN,
        reply="أهلًا بيكي. ممكن توضحيلي محتاجة تعرفي إيه، أو أقدر أحوّل سؤالك لفريق العيادة؟",
        handoff_required=True,
    )

from app.domain import Intent
from app.policy import decide_message


def test_emergency_escalates_immediately():
    result = decide_message("عندي نزيف شديد")
    assert result.intent == Intent.EMERGENCY
    assert result.emergency is True
    assert result.handoff_required is True
    assert "الطوارئ" in result.reply


def test_clinical_question_hands_off():
    result = decide_message("آخد دواء إيه؟")
    assert result.intent == Intent.CLINICAL
    assert result.handoff_required is True


def test_booking_does_not_claim_confirmation():
    result = decide_message("عايزة حجز كشف")
    assert result.intent == Intent.BOOKING
    assert result.booking_status == "collecting_preferences"
    assert "اتحجز" not in result.reply


def test_opt_out_is_respected():
    result = decide_message("وقفوا الرسايل")
    assert result.intent == Intent.OPT_OUT
    assert result.outbound_allowed is False

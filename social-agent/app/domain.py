from enum import StrEnum
from pydantic import BaseModel, Field


class Intent(StrEnum):
    GREETING = "greeting"
    CLINIC_FAQ = "clinic_faq"
    BOOKING = "booking"
    CLINICAL = "clinical"
    EMERGENCY = "emergency"
    OPT_OUT = "opt_out"
    UNKNOWN = "unknown"


class IncomingMessage(BaseModel):
    channel: str = Field(min_length=1, max_length=40)
    external_message_id: str = Field(min_length=1, max_length=200)
    conversation_id: str = Field(min_length=1, max_length=200)
    text: str = Field(min_length=1, max_length=8000)
    consent_to_follow_up: bool = False


class MessageDecision(BaseModel):
    intent: Intent
    reply: str
    handoff_required: bool = False
    emergency: bool = False
    outbound_allowed: bool = True
    booking_status: str | None = None

from fastapi import FastAPI
from .domain import IncomingMessage, MessageDecision
from .policy import decide_message

app = FastAPI(
    title="KH AI Social Reception Agent",
    version="0.1.0",
    description="Administrative reception demo. Not a medical advice service.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "scaffold"}


@app.post("/v1/messages/preview", response_model=MessageDecision)
def preview_message(message: IncomingMessage) -> MessageDecision:
    """Local policy preview only; does not send a message or create a booking."""
    return decide_message(message.text)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_preview_endpoint():
    response = client.post("/v1/messages/preview", json={
        "channel": "demo",
        "external_message_id": "msg-001",
        "conversation_id": "conv-001",
        "text": "عايزة حجز كشف",
    })
    assert response.status_code == 200
    assert response.json()["intent"] == "booking"

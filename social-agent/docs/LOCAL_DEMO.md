# Local demo

Requires Python 3.11+.

```bash
cd social-agent
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
make install
make test
make run
```

Open `http://127.0.0.1:8000/docs`.

Try `POST /v1/messages/preview` with a synthetic message:
```json
{
  "channel": "demo",
  "external_message_id": "demo-001",
  "conversation_id": "demo-conversation",
  "text": "عايزة حجز كشف"
}
```

This preview endpoint only classifies and drafts a response. It does not send messages, persist patient data, connect to Claude, or create appointments. The phrase rules are intentionally conservative and require clinical review before production use.

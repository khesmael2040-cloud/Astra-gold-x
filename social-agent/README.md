# KH AI Social Reception & Booking Agent

An isolated clinic social-inbox and appointment orchestration service. This project lives under `social-agent/` on the dedicated branch `feature/kh-ai-social-agent`; it does not modify ASTRA X core or the repository root.

## Product goals
- Receive and route inbound messages through official platform APIs and webhooks.
- Use Claude behind a provider adapter for Egyptian-Arabic conversation, intent detection, and tool selection.
- Answer only from an approved clinic knowledge base.
- Qualify leads and coordinate real appointment availability through a scheduling adapter.
- Escalate clinical, urgent, uncertain, and complaint cases to a human.
- Maintain consent-aware, minimal patient/lead records and auditable actions.

## Non-goals / hard boundaries
- No scraping, browser automation against social platforms, credential harvesting, or unofficial APIs.
- No autonomous diagnosis, prescribing, treatment changes, or pregnancy/success guarantees.
- Never claim an appointment is booked until the scheduling system confirms it.
- No outbound marketing messages without applicable consent, platform policy, approved templates, and messaging-window checks.
- No real patient data in tests, fixtures, logs, or development environments.

## Initial architecture
`webhooks -> channel adapters -> message router -> policy/safety gate -> conversation orchestrator -> Claude adapter + approved knowledge retrieval -> tool adapters (CRM / scheduling) -> audit log`

Human handoff is a first-class outcome, not an error path.

## Status
Foundation / implementation handoff. No live social channel, Claude key, CRM, or booking system is connected by this scaffold.

## Build
See [docs/BUILD_PLAN.md](docs/BUILD_PLAN.md), [docs/SAFETY_AND_PRIVACY.md](docs/SAFETY_AND_PRIVACY.md), and [docs/CODEX_HANDOFF.md](docs/CODEX_HANDOFF.md).

# Build plan

## Phase 0 — foundation
- Establish typed domain contracts, configuration validation, health endpoint, structured logging, database migrations, and test harness.
- Keep all external integrations behind interfaces.
- Add CI for formatting, lint, type-check, unit tests, dependency/security checks.

## Phase 1 — conversation core
- Inbound message normalization and idempotency.
- Conversation state machine and intent classification.
- Claude provider adapter with strict structured outputs, timeout/retry budgets, redaction, and prompt versioning.
- Retrieval from an explicitly approved, versioned clinic knowledge base; cite internal article IDs in traces.
- Safety policy: urgent symptom detection, clinical-advice refusal boundaries, uncertainty detection, human handoff.

## Phase 2 — lead and appointment workflow
- Consent capture and provenance.
- Minimal lead profile and configurable retention.
- Scheduling interface: list real slots, create/reschedule/cancel appointments, verify provider confirmation, idempotency keys.
- Never expose another patient's details or appointment information.
- Human review for ambiguous identity, conflicts, sensitive requests, and failed booking confirmation.

## Phase 3 — channel adapters
- Meta Messenger / Instagram through official Meta APIs and approved permissions.
- WhatsApp Business Platform through official Cloud API or approved BSP.
- TikTok only after confirming the currently available official messaging/business API and account eligibility; do not promise parity.
- Webhook signature verification, replay protection, rate limits, token rotation, subscription verification, delivery receipts.

## Phase 4 — operations
- Admin console with RBAC, conversation queue, handoff, audit search, knowledge approval, channel status, booking reconciliation.
- Metrics: first-response latency, handoff rate, unresolved conversations, booking conversion, failed booking attempts, opt-out rate.
- Backups, restore drills, incident response, data export/deletion workflow.

## Acceptance gates
1. All channel integrations use documented official APIs and pass webhook signature/replay tests.
2. No booking success response without a confirmed scheduler result.
3. Every outbound message passes consent, policy, and channel-window/template checks.
4. Medical red flags route to urgent human/ emergency guidance; no diagnosis or medication advice is generated.
5. Tenant/role isolation, encryption, retention, deletion, and audit tests pass.
6. Unit, integration, contract, and end-to-end tests pass with synthetic fixtures only.
7. A staging dry-run is signed off before any production credentials are enabled.

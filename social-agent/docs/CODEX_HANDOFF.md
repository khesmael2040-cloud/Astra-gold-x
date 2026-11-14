# Codex implementation brief

You are implementing **KH AI Social Reception & Booking Agent** in the isolated directory `social-agent/` only. Do not edit files outside this directory. Do not change ASTRA X or repository-level configuration unless explicitly requested.

## First task
Inspect the repository and this specification, then implement a production-minded MVP foundation in small, reviewable commits. Before choosing framework versions or provider endpoints, verify current official documentation. Do not invent API capabilities.

## Required engineering approach
1. Propose a concise architecture decision record and stack choice, then implement it.
2. Use a modular monolith initially; define interfaces for channel providers, LLM provider, knowledge retrieval, CRM, scheduler, and human handoff.
3. Provide a local developer environment, migrations, typed configuration, health/readiness endpoints, structured redacted logs, and CI.
4. Add unit, contract, and integration tests using synthetic data and mocked external adapters.
5. Implement safe failure behavior: retries only for idempotent operations, bounded timeouts, deduplication, dead-letter handling, and explicit human handoff.
6. Add a local demo channel adapter only for development. Clearly label it as simulated and never present it as a real social integration.
7. Do not enable real messaging or booking until official credentials, permissions, consent controls, and staging acceptance are configured.

## Mandatory conversation behavior
- Egyptian Arabic, warm, concise, respectful, and non-pressuring.
- Ask one question at a time when collecting booking details.
- Distinguish administrative intent from clinical intent.
- Answer clinic FAQs only from approved, versioned knowledge articles.
- For individual medical questions, route to staff; do not diagnose or prescribe.
- Emergency red flags trigger immediate emergency guidance and human escalation.
- Never claim a slot is reserved/booked without a successful scheduler confirmation.
- Never send proactive messages without valid consent and platform policy checks.

## MVP deliverables
- Working application with documented run commands.
- Domain models and conversation state machine.
- Provider interfaces and a safe simulated adapter.
- Knowledge base ingestion/approval model.
- Lead and appointment workflow with idempotency.
- Human handoff queue.
- Audit events and privacy controls.
- CI and automated tests.
- Threat model, deployment notes, and environment variable reference.

## Definition of done
The MVP must install, start, pass tests, and demonstrate end-to-end simulated conversations including: FAQ answer, lead qualification, available-slot lookup, confirmed booking, failed booking, opt-out, clinical handoff, and emergency escalation. Provide exact test output and list integrations that remain unconfigured. Never claim production readiness merely because the demo works.

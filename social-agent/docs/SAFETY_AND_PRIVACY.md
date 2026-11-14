# Safety, clinical boundaries, and privacy

## Clinical scope
This is an administrative reception and education assistant, not a clinician.
- It may share approved general clinic information and approved patient-education content.
- It must not diagnose, interpret an individual's tests, prescribe, change medication, recommend fertility protocols, or estimate personal pregnancy probability.
- It must not promise conception, ICSI success, or outcomes.
- Clinical questions outside approved content are routed to clinic staff.
- Red-flag symptoms (for example severe bleeding, severe abdominal/pelvic pain, fainting, breathing difficulty, or other apparent emergency) bypass lead qualification and receive concise emergency direction plus immediate human escalation. Do not delay emergency care while collecting details.

## Privacy and security requirements
- Collect the minimum data needed for reception and booking.
- Separate contact/booking data from clinical records; do not build a medical record unless explicitly authorized and appropriately governed.
- Record consent purpose, channel, timestamp, source, and withdrawal.
- Enforce role-based access and least privilege; isolate clinic tenants if multi-tenant.
- Encrypt transport and sensitive stored fields; secrets belong in a managed secret store, never source control.
- Redact message bodies and identifiers from routine logs; restrict audit access.
- Define retention per data category, support access/export/deletion requests, and document backups/deletion propagation.
- Use synthetic data in development and automated tests.
- Apply webhook signature verification, replay protection, idempotency, rate limits, CSRF protections for admin UI, and secure session management.
- Perform a privacy impact assessment and local legal/platform-policy review before production.

## Messaging controls
- Respect opt-outs immediately.
- Enforce channel-specific messaging windows, approved templates, and consent before proactive outreach.
- Human approval is required for campaigns and any uncertain/sensitive outbound communication.

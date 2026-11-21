# ASTRA X Dual-Agent Execution Bridge (v0.1)

Status: **isolated prototype / documentation-only integration**. This bridge delegates bounded code changes to Codex CLI while AntiGravity retains planning and independent review.

## Safety and integration boundary

- Built on a separate branch: `feature/astra-dual-agent-bridge`.
- All bridge assets live under `astra_dual_agent_bridge/`.
- No ASTRA X core/runtime files are changed.
- This package does not claim automatic tool connectivity, tests, or execution. The operator must run Codex CLI locally and inspect its evidence.
- Do not pass credentials, patient information, secrets, or private production data into prompts.

## Roles

1. **ASTRA Persistent Executive / AntiGravity**: classifies task, owns scope, architecture decisions, plan, acceptance criteria, budget/safety gates, and final approval.
2. **Codex CLI**: executes only the approved task; explores only as needed, edits scoped files, runs approved checks, and returns evidence.
3. **Independent Review**: AntiGravity checks the diff and evidence against the plan. Codex must not self-approve.

## Workflow

`INTAKE → PLAN → EXECUTION BRIEF → CODEX → EVIDENCE → AUDIT → (CORRECT | ACCEPT)`

### Gate 0 — classify
Use Codex for bounded, implementation-heavy tasks (code, tests, refactors inside a stated scope). AntiGravity handles planning, sensitive decisions, architectural design, high-risk actions, and final audit.

### Gate 1 — plan
Before execution, AntiGravity creates an execution brief containing:
- objective and non-goals
- allowed file/path scope
- forbidden scope
- approved decisions and assumptions
- implementation steps
- tests/checks to run
- acceptance criteria
- risk level and rollback plan

If scope or requirements are unclear, ask the user before delegating.

### Gate 2 — execute
Codex is invoked from the project root (or target working directory) with the brief and explicit constraints. Start with read-only analysis if the scope is not already verified. Do not use unrestricted approval settings or disable sandbox/security prompts.

Suggested read-only command:
```powershell
codex exec "Analyze the project structure and summarize relevant files. Do not modify files."
```

Implementation invocation template (replace placeholders; use a task-specific prompt):
```powershell
codex exec --sandbox workspace-write --ask-for-approval on-request "<TASK BRIEF>"
```
If your installed Codex CLI version does not support these exact flags, check `codex exec --help`; do not silently remove safety controls.

### Gate 3 — evidence
Codex must report:
- files changed (exact paths)
- concise change summary
- diff/stat
- commands run and exit codes
- test outcomes (including skipped/not run)
- unresolved issues, assumptions, risks
- any out-of-scope changes (must be disclosed and reverted unless explicitly approved)

### Gate 4 — audit
AntiGravity independently reviews:
- alignment with brief and acceptance criteria
- correctness, regressions, edge cases
- security/privacy and dependency changes
- tests quality and truthful reporting
- scope drift and accidental changes

Audit outcomes: `ACCEPT`, `REVISE`, or `BLOCK`. ACCEPT only with evidence. If REVISE, return a numbered, minimal correction brief. If BLOCK, stop and explain the risk.

### Gate 5 — correction loop
Maximum 2 correction rounds by default. If still failing, stop, summarize blockers, and ask for a decision. Each round must preserve scope and avoid rewriting unrelated code.

## Usage
1. Review `ANTIGRAVITY_GLOBAL_RULE.md` and add it to AntiGravity Global Rules (or project rules, if you prefer local scope).
2. Use `CODEX_EXECUTION_PROTOCOL.md` as the reusable execution prompt/template.
3. Use `AUDIT_CHECKLIST.md` for independent acceptance.
4. Start each delegated task by creating a fresh, task-specific brief. Do not blindly reuse old task scope.

## Task record template
Copy this for each job:
- Task ID:
- Objective:
- Non-goals:
- Allowed paths:
- Forbidden paths:
- Plan:
- Acceptance criteria:
- Risk:
- Backup/rollback:
- Codex result/evidence:
- AntiGravity audit:
- Final status:
- Correction rounds:

## Current limitations
- No live bridge/automation has been wired into AntiGravity or ASTRA runtime.
- Codex CLI is invoked by the operator; this package defines a safe handoff protocol.
- No CI or local test run is claimed.

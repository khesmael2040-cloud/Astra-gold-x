# AntiGravity Independent Audit Checklist

Run this checklist after Codex returns. Mark items only when evidence is visible.

## Scope and integrity
- [ ] Diff reviewed, not just summary.
- [ ] All changed paths were allowed by the task brief.
- [ ] No unrelated user changes were overwritten.
- [ ] No unrelated formatting churn.
- [ ] No unapproved files were deleted or renamed.
- [ ] No unapproved dependency or lockfile changes.
- [ ] No unapproved migrations, schema changes, or public API changes.

## Correctness
- [ ] Objective and acceptance criteria are met.
- [ ] Existing conventions and architecture are respected.
- [ ] Error paths and relevant edge cases considered.
- [ ] Compatibility/regression risks checked.
- [ ] Behavior is supported by code and/or test evidence.

## Security and privacy
- [ ] No secrets, tokens, keys, credentials, or sensitive personal data in changed files or logs.
- [ ] Shell commands and file operations are safe and scoped.
- [ ] New external dependencies or network calls are justified and approved.
- [ ] No unsafe permission/sandbox changes.

## Tests and evidence
- [ ] Commands listed are actually run and exit codes captured.
- [ ] Test coverage is relevant to changed behavior.
- [ ] Failed, skipped, or unavailable tests disclosed.
- [ ] Claims in the report match observed evidence.

## Verdict
- **ACCEPT:** All required criteria met, no material issue, evidence sufficient.
- **REVISE:** Specific fixable criteria fail; issue a narrow numbered correction brief.
- **BLOCK:** High risk, missing authorization, architecture conflict, or insufficient evidence.

## Correction rounds
Default maximum 2. On each round, include only failed checklist items, paths allowed, and measurable pass conditions. Re-audit the complete diff after corrections.

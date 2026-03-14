---
description: Run the full pre-commit quality checklist against staged changes
agent: pre-commit-check
subtask: true
---

**Canonical Contract**: Implements the workflow defined in `docs/workflows/pre-commit.md`.

<HARD-GATE>
Execute all quality gates defined in the canonical contract.
If any gate fails → output NOT READY with blockers first.
If commands unavailable → report NOT CONFIGURED explicitly.
Never recommend commit readiness when required gates fail.
</HARD-GATE>

**Execution**:
!`git diff --cached --stat`

Execute quality gates per canonical contract workflow. Use canonical contract output format and status vocabulary.

**References**:
- `docs/workflows/pre-commit.md` (authoritative workflow)
- `docs/PRE_COMMIT_CHECKLIST.md` (detailed checklist)

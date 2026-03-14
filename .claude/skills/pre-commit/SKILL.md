---
name: pre-commit
description: Run pre-commit readiness checks and summarize blockers before committing.
argument-hint: "[optional-target]"
disable-model-invocation: true
---

**Canonical Contract**: Implements the workflow defined in `docs/workflows/pre-commit.md`.

<HARD-GATE>
Execute all quality gates defined in the canonical contract.
If any required gate fails → output NOT READY with blockers listed first.
If commands unavailable → report NOT CONFIGURED explicitly.
Never create commits during validation.
</HARD-GATE>

**Implementation**:
1. Review staging area: `git diff --cached --stat`
2. Execute quality gates per canonical contract workflow
3. Include static-analysis via `static-analysis-gate` when configured
4. Use canonical contract output format and status vocabulary

**References**:
- `docs/workflows/pre-commit.md` (authoritative workflow)
- `docs/PRE_COMMIT_CHECKLIST.md` (detailed checklist)

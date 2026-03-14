---
description: Run the full pre-commit quality checklist against staged changes
agent: pre-commit-check
subtask: true
---

Run the pre-commit quality checklist against all currently staged changes.

**Canonical Contract**: This command implements the workflow defined in `docs/workflows/pre-commit.md`.

<HARD-GATE>
Follow the hard gates defined in the canonical contract:

1. Unit tests MUST pass (when a project test command exists)
2. Build MUST succeed (when a project build command exists)
3. Lint MUST pass (when a project lint command exists)
4. Static analysis MUST pass (when PMD/detekt/Checkstyle configured)

If a required gate fails, output NOT READY with blockers first.
If a command is unavailable, report NOT CONFIGURED explicitly.
Never recommend commit readiness when required gates fail.
</HARD-GATE>

**Execution**:
First check what's staged:
!`git diff --cached --stat`

Then execute the quality gates defined in the canonical contract, validating against `docs/PRE_COMMIT_CHECKLIST.md`.

**Required Output Format** (preserve exact ordering):
1. Status: `READY` or `NOT READY`
2. Blocking items (if any, most critical first)
3. Evidence (commands run and summarized outcomes)
4. Next actions (specific recommendations for addressing blockers)

**References**:
- `docs/workflows/pre-commit.md` (canonical contract)
- `docs/PRE_COMMIT_CHECKLIST.md` (detailed checklist)

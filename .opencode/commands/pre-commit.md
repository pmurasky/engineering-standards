---
description: Run the full pre-commit quality checklist against staged changes
agent: pre-commit-check
subtask: true
---

Run the pre-commit quality checklist against all currently staged changes.

<HARD-GATE>
Do NOT recommend commit readiness when any required quality gate fails.

Required quality gates:
1. Unit tests pass (when a project test command exists)
2. Build succeeds (when a project build command exists)
3. Lint passes (when a project lint command exists)

If a required gate fails, output NOT READY with blockers first.
If a command is unavailable, report NOT CONFIGURED explicitly.
</HARD-GATE>

First check what's staged:
!`git diff --cached --stat`

Then analyze each changed file against the engineering standards checklist defined in `docs/PRE_COMMIT_CHECKLIST.md`.

Output in this order:
1. Status: READY or NOT READY
2. Blocking issues (if any)
3. Evidence (commands run and summarized outcomes)
4. Recommendations and next actions

Report pass/fail for each checklist item and provide a final recommendation on whether it is safe to commit.

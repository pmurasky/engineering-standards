---
name: pre-commit
description: Run pre-commit readiness checks and summarize blockers before committing.
argument-hint: "[optional-target]"
disable-model-invocation: true
---

Run a pre-commit readiness pass for the current changes.

Checklist:
1. Review diffs and staged files.
2. Validate quality gates against `docs/PRE_COMMIT_CHECKLIST.md`.
3. Confirm test/build/lint expectations where commands are available.
4. Output READY or NOT READY with blocking items first.

Required references:
- `docs/PRE_COMMIT_CHECKLIST.md`
- `docs/AI_AGENT_WORKFLOW.md`

Do not create commits in this skill. Report readiness only.

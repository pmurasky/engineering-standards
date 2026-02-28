---
name: micro-commit
description: Create one production-ready micro-commit following repository standards.
argument-hint: "[scope-or-issue]"
disable-model-invocation: true
---

Create exactly one logical commit for the current change set.

Workflow:
1. Inspect staged and unstaged changes.
2. Confirm this commit contains one coherent logical change.
3. Run applicable unit tests if a test command exists.
4. Use Conventional Commits format and explain WHY in the body.

Required references:
- `docs/AI_AGENT_WORKFLOW.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

If no unit test command is configured in this repository, state that explicitly in your report.

---
name: refactoring-gate
description: Block refactoring when test coverage or test-health prerequisites are not met. Use before starting non-trivial refactoring work.
---

# Refactoring Gate

Verify that refactoring can proceed safely before any behavior-preserving structural change begins.

## Hard Gates

1. Unit-test coverage for the target code is >= 80%.
2. Coverage for critical paths is 100%.
3. Existing relevant tests must already pass before refactoring starts.
4. If target coverage is < 80% → stop and add tests first.

## Workflow

1. Identify the exact refactoring target.
2. Check coverage and existing test health for that target.
3. Confirm whether the change is a real refactor or a simple rename/formatting update.
4. Block unsafe refactoring and state the missing prerequisites clearly.

## Status Vocabulary

- `GO`: Refactoring prerequisites are satisfied.
- `STOP`: Coverage or test-health blockers prevent safe refactoring.

## References

- `docs/AI_AGENT_WORKFLOW.md` - Refactoring workflow and prerequisites
- `docs/PRE_COMMIT_CHECKLIST.md` - Refactoring gate checklist

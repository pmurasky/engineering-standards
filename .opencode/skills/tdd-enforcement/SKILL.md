---
name: tdd-enforcement
description: Enforce strict test-first sequencing with hard gates for RED → GREEN → REFACTOR. Use when the user wants TDD enforced rather than treated as a suggestion.
version: 1.0.0
category: workflow
---

# TDD Enforcement

Enforce one-test-at-a-time TDD with explicit proof of RED before GREEN work begins.

## Hard Gates

1. Never allow production code changes before a failing test is observed.
2. Keep exactly one failing test in the current RED → GREEN cycle.
3. If no failing test evidence is shown, stop and re-establish RED first.
4. Never commit while tests are failing.

## Workflow

1. Verify the current cycle is RED, GREEN, or REFACTOR.
2. Check that the current failing test proves the intended behavior gap.
3. Require minimal implementation to reach GREEN.
4. Allow refactoring only after tests are green again.

## Status Vocabulary

- `RED`: A valid failing test is driving the next implementation step.
- `GREEN`: The test passes and the behavior is implemented.
- `REFACTOR`: Code cleanup is safe because tests are green.
- `STOP`: TDD preconditions are broken and must be restored first.

## References

- `docs/workflows/tdd-enforcement.md` - Canonical TDD enforcement workflow
- `docs/AI_AGENT_WORKFLOW.md` - TDD micro-commit rules

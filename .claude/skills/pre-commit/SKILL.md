---
name: pre-commit
description: Run pre-commit readiness checks and report blockers using strict quality gates for tests, build, lint, and static analysis.
disable-model-invocation: true
---

# Pre-Commit Validation

## Use when

- User asks "ready to commit?"
- Staged changes need quality-gate validation
- You need explicit pass/fail evidence before commit

## Not for

- Early design discussions with no staged changes
- Post-push release validation
- Replacing TDD workflow decisions

## Hard Gates

- Unit tests must pass
- Build must succeed
- Lint must pass
- Static analysis MUST pass when configured

## Status Vocabulary

- `READY`: all required gates pass
- `NOT READY`: one or more gates failed
- `NOT CONFIGURED`: gate command/tool unavailable

## Example

Input: "run pre-commit checks".

Output: status + failing gates first + command evidence + concrete fix actions.

## Anti-patterns

- Declaring READY without running gates
- Hiding failing output behind summaries
- Recommending commit with unresolved blockers

## References

- `references/workflow.md`

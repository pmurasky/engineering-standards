---
name: micro-commit
description: Enforce one logical change per production-ready commit with required quality gates and Conventional Commits format.
---

# Micro-Commit Workflow

## Use when

- User asks to commit current work
- You need to split changes into safe, logical commits
- You want commit-readiness validation before committing

## Not for

- Planning roadmap priorities or issue triage
- Refactoring without existing test coverage
- Bypassing failed test/build/lint checks

## Hard Gates

- One logical change per commit
- Unit tests pass
- Build succeeds
- Lint passes
- Conventional Commit message format

## Output Status

- `READY`: one logical change + all gates green
- `NOT READY`: failed quality gate(s)
- `SPLIT REQUIRED`: multiple logical changes detected
- `MESSAGE INVALID`: commit message format invalid

## Example

Input: "commit these changes".

Output: classify change scope, run gates, return READY/NOT READY with evidence and next action.

## Anti-patterns

- Committing multiple unrelated changes together
- Creating commit before running quality gates
- Using vague commit messages (e.g., "update code")

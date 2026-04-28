---
name: micro-commit
description: Create one production-ready micro-commit following repository standards. Use when user asks to commit current work in one logical, test-verified step.
---

# Micro-Commit Workflow

Guide work into one logical, reviewable, production-ready commit.

## Hard Gates

1. Commit exactly one logical change.
2. Required tests MUST pass before commit.
3. Never commit during the RED phase of TDD.
4. Do not bundle unrelated refactoring, docs, and feature work into one commit.

## Workflow

1. Inspect the working tree and staged diff.
2. Confirm the change represents one logical unit of work.
3. Verify the relevant tests and quality gates are green.
4. Draft a conventional-commit message focused on the change intent.
5. If scope is too broad, split the work before proceeding.

## Status Vocabulary

- `READY`: One logical, production-ready commit is prepared.
- `NOT READY`: Scope or quality gates are blocking the commit.

## References

- `docs/AI_AGENT_WORKFLOW.md` - Authoritative micro-commit flow
- `docs/PRE_COMMIT_CHECKLIST.md` - Commit readiness gates

---
name: code-quality
description: Review code changes for SOLID, maintainability, and repository quality gates. Use when user asks for code quality review after requirement compliance is already satisfied.
version: 1.0.0
category: quality-gate
---

# Code Quality Review

Run a standards-focused review of changed code after spec compliance is already covered.

## Hard Gates

1. Review SOLID, DRY, and maintainability signals before approving the change.
2. Flag methods, classes, or dependency patterns that violate project standards.
3. Do not mark work as passing when there are clear code-quality blockers.

## Workflow

1. Inspect the changed files and their surrounding collaborators.
2. Check method size, class responsibility, duplication, and dependency direction.
3. Identify concrete blockers first, then list lower-severity improvements.
4. Summarize the review outcome using the required status vocabulary.

## Status Vocabulary

- `PASS`: No blocking quality issues found.
- `FLAG`: Non-blocking issues or follow-ups found.
- `BLOCK`: Quality issues must be fixed before accepting the change.

## References

- `docs/PRE_COMMIT_CHECKLIST.md` - Commit readiness quality gates
- `docs/CODING_PRACTICES.md` - SOLID, DRY, and maintainability standards
- `docs/TYPESCRIPT_STANDARDS.md` - Language-specific guidance when applicable

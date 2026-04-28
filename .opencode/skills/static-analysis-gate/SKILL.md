---
name: static-analysis-gate
description: Run PMD, detekt, and Checkstyle as a hard gate before commit readiness. Use when the repo has static-analysis tooling configured.
---

# Static Analysis Gate

Validate configured static-analysis tools before declaring code ready.

## Hard Gates

1. Run every configured static-analysis tool relevant to the project.
2. Treat PMD, detekt, and Checkstyle failures as blocking.
3. Do not waive violations silently or recommend suppression as the first response.

## Workflow

1. Detect which static-analysis tools are configured in the repository.
2. Run each applicable tool or project wrapper command.
3. Group failures by tool and severity.
4. Report blocking issues and any missing configuration explicitly.

## Status Vocabulary

- `PASS`: Configured static-analysis tools passed.
- `BLOCK`: Static-analysis failures require fixes.
- `NOT CONFIGURED`: No relevant static-analysis tooling is available.

## References

- `docs/STATIC_ANALYSIS_STANDARDS.md` - Tooling expectations and policy
- `docs/PRE_COMMIT_CHECKLIST.md` - Static-analysis commit gate

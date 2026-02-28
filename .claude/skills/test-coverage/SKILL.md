---
name: test-coverage
description: Assess test completeness and identify missing unit-test coverage for changed behavior.
argument-hint: "[component-or-path]"
---

Assess test coverage quality for the targeted changes.

Checks:
1. Identify changed behavior and existing unit tests.
2. Flag missing happy path, edge case, and error-path coverage.
3. Verify naming clarity and Given-When-Then structure where relevant.
4. Recommend minimal additional tests to satisfy standards.

Required references:
- `docs/CODING_PRACTICES.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

If no automated unit test command is configured, note that in the report.

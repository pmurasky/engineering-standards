---
name: test-coverage
description: Assess changed behavior for unit-test completeness and identify concrete coverage gaps before completion.
---

# Test Coverage

## Use when

- User requests coverage-focused review
- Refactoring or behavior changes need gap analysis
- You must confirm changed paths are test-backed

## Not for

- Full code-quality review across all concerns
- Replacing execution of tests/build/lint
- Coverage claims without changed-file analysis

## Hard Gates

1. Map changed behavior to test cases
2. Identify missing assertions and edge cases
3. Flag critical paths lacking unit coverage
4. Produce explicit gap list before completion claims

## Status Vocabulary

- `SUFFICIENT`
- `GAPS FOUND`
- `BLOCKED`

## Example

Input: "check test coverage for this change".

Output: per-file coverage assessment, missing tests list, and prioritized next tests.

## Anti-patterns

- Reporting aggregate percentages only
- Ignoring branch/error-path coverage
- Marking complete without gap disclosure

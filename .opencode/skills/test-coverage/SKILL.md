---
name: test-coverage
description: Assess test completeness and identify missing unit-test coverage for changed behavior. Use when you need coverage-focused review rather than a full quality audit.
---

# Test Coverage Review

Assess whether changed behavior has enough meaningful unit-test coverage.

## Hard Gates

1. Evaluate changed behavior, not just file count.
2. Minimum unit-test coverage target for changed code is 80%.
3. Critical paths should reach 100% unit-test coverage.
4. Do not recommend coverage padding with low-value tests.

## Workflow

1. Identify changed behavior and its risk level.
2. Inspect existing tests for that behavior.
3. Note missing branches, failure paths, or edge cases.
4. Summarize whether coverage is sufficient and what tests are still needed.

## Status Vocabulary

- `SUFFICIENT`: Coverage for changed behavior is adequate.
- `GAP`: Coverage exists but important scenarios are still missing.
- `CRITICAL GAP`: Coverage is below the required threshold or misses critical paths.

## References

- `docs/CODING_PRACTICES.md` - Coverage thresholds and testing standards
- `docs/PRE_COMMIT_CHECKLIST.md` - Test expectations before commit

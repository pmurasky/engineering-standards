---
name: spec-compliance
description: Verify requirement and acceptance-criteria compliance before code quality review. Use as the first review stage for feature or bug-fix work.
---

# Specification Compliance Review

Review whether the implementation actually satisfies the requested behavior before judging code quality.

## Hard Gates

1. Compare the implementation against the stated requirements and acceptance criteria.
2. Do not pass work that misses required behavior, edge cases, or user-visible outcomes.
3. Separate requirement gaps from code-quality suggestions.

## Workflow

1. Restate the expected behavior from the task, spec, or tests.
2. Inspect the implementation and its verification coverage.
3. Identify missing acceptance criteria or unverified behavior.
4. Produce a pass/flag/block result before any stage-2 code-quality review.

## Status Vocabulary

- `PASS`: The implementation satisfies the intended requirements.
- `FLAG`: Minor ambiguity or follow-up remains, but core behavior is present.
- `BLOCK`: Required behavior is missing or contradicted.

## References

- `docs/AI_AGENT_WORKFLOW.md` - Feature workflow and verification expectations
- `docs/CODING_PRACTICES.md` - Testing and acceptance-quality standards

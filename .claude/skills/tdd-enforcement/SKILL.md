---
name: tdd-enforcement
description: Enforce strict RED→GREEN→REFACTOR sequencing with evidence-based gates and one-test-at-a-time discipline.
---

# TDD Enforcement

## Use when

- User requests strict test-first execution
- New feature or bug fix must follow RED→GREEN→REFACTOR
- You need proof-based TDD gatekeeping

## Not for

- Final commit-readiness review (use pre-commit)
- Broad test policy/governance discussions
- Work where RED phase is intentionally skipped

## Hard Gates

Never allow production code changes before a failing test.

1. RED: add exactly one failing test
2. Verify RED with observed failure evidence
3. GREEN: minimal code to pass that test
4. Verify GREEN with passing test evidence
5. REFACTOR: improve structure only
6. Verify REFACTOR with tests still passing

## Status Vocabulary

- `READY FOR GREEN`
- `READY FOR REFACTOR`
- `READY FOR NEXT RED`
- `BLOCKED`

## Example

Input: "enforce TDD for this feature".

Output: current phase status, RED/GREEN evidence, scope of single behavior, and next smallest step.

## Anti-patterns

- If no failing test evidence is shown, declare BLOCKED.
- Writing production code before a failing test exists
- Advancing without RED failure evidence
- Adding multiple failing tests in one cycle

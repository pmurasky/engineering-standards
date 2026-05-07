---
name: code-quality
description: Stage-2 code quality review for SOLID, maintainability, and repository quality gates after spec-compliance passes.
disable-model-invocation: true
---

# Code Quality Review

## Use when

- Stage 1 (`spec-compliance`) has passed and stage-2 review is requested
- User asks for SOLID, maintainability, or code quality review
- You need a strict PASS/FLAG assessment before commit readiness

## Not for

- Initial requirement/acceptance validation (use `spec-compliance` first)
- Security-specific threat analysis
- Pure style or formatting-only checks without maintainability concerns

## Hard Gate

This is **stage 2 of review**.
- Run `spec-compliance` first and proceed only when stage 1 is PASS
- If stage 1 is FAIL or not run, output `BLOCKED`

## Review Targets

- SOLID compliance and SRP boundaries
- Method/class size limits and parameter count limits
- Duplication and coupling risks
- Clear naming and maintainability concerns

## Output Format

Return findings grouped by:
1. **Critical**: Must fix before commit
2. **Warning**: Should address soon
3. **Suggestion**: Optional improvements

## Example

Scenario: user says "spec-compliance passed, now run code quality review".

Expected behavior:
1. Confirm stage-1 passed.
2. Evaluate SOLID, method/class size, duplication, and coupling.
3. Return grouped findings: Critical, Warning, Suggestion.

## Anti-patterns

- Running this review before stage-1 validation
- Returning vague feedback without file-level evidence
- Marking READY while unresolved critical maintainability defects remain

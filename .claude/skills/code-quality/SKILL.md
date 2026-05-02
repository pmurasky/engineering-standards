---
name: code-quality
description: Review code changes for SOLID, maintainability, and repository quality gates. This is stage 2 of review - run spec-compliance first and proceed only when stage 1 is PASS.
---

# Code Quality Review

Perform a focused code quality review for SOLID compliance and maintainability.

## Trigger Conditions

- User requests code quality review after spec-compliance passes
- Stage 2 review in the two-stage review workflow
- Phrases: "code quality review", "review my code", "check SOLID", "maintainability review"

## Hard Gate

This is **stage 2 of review**.
- Run `spec-compliance` first and proceed only when stage 1 is PASS
- If stage 1 is FAIL or not run, output `BLOCKED`

## Review Targets

- SOLID compliance and SRP boundaries
- Method/class size limits and parameter count limits
- Duplication and coupling risks
- Clear naming and maintainability concerns

## Review Checklist

**SOLID Principles:**
- Single Responsibility: Each class has one reason to change
- Open/Closed: Open for extension, closed for modification
- Liskov Substitution: Subtypes substitutable for base types
- Interface Segregation: Focused interfaces over fat ones
- Dependency Inversion: Depend on abstractions, not concrete classes

**Code Metrics:**
- Methods ≤ 20 lines (language-specific limits apply)
- Classes ≤ 300 lines
- Parameters ≤ 5 per method
- No duplicated code (DRY principle)

## Output Format

Return findings grouped by:
1. **Critical**: Issues that must be fixed before commit
2. **Warning**: Issues that should be addressed
3. **Suggestion**: Improvements to consider

## Token Budget

- **Category**: On-demand workflow
- **Estimated usage**: 700-1000 tokens per invocation
- **Frequency**: Per review (typically 1-2 times per PR)
- **Optimization**: Focus on highest-impact issues first

## References

- `docs/CODING_PRACTICES.md` - Code quality standards
- `docs/SOLID_PRINCIPLES.md` - SOLID principles deep-dive
- `docs/PRE_COMMIT_CHECKLIST.md` - Quality checklist
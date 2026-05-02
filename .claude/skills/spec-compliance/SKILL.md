---
name: spec-compliance
description: Stage 1 review that verifies requirement and acceptance-criteria compliance before code quality checks. Run this before code-quality review.
---

# Spec Compliance Review

Run stage-1 spec compliance review to verify requirements before code quality checks.

## Trigger Conditions

- User requests review of implementation against requirements
- Before running code-quality review (stage 2)
- Phrases: "spec compliance", "requirement review", "acceptance criteria check", "stage 1 review"

## Hard Gate

Do not proceed to code-quality review while stage 1 is failing.
- If any acceptance criterion is missing, partial, or contradicted → output `FAIL`

## Review Scope

Check only:
1. **Requirement coverage**: Against stated acceptance criteria
2. **Behavioral match**: Between requested and implemented outcomes
3. **Scope drift**: Hidden missing required behavior

Do not include SOLID/style/maintainability issues in this stage.

## Output Format

1. **Status**: `PASS` or `FAIL`
2. **Requirement matrix** with evidence
3. **Blocking mismatches**: Expected vs found
4. **Next step**: Rerun stage 1 after fixes, or proceed to stage 2

## Two-Stage Review Process

**Stage 1 (This Skill)**: Spec Compliance
- Verify requirements are met
- Check acceptance criteria coverage
- Identify scope drift

**Stage 2**: Code Quality (run after this passes)
- SOLID compliance
- Maintainability review
- Code style checks

## Token Budget

- **Category**: On-demand workflow
- **Estimated usage**: 600-900 tokens per invocation
- **Frequency**: Per review (typically 1-2 times per PR)
- **Optimization**: Focus on requirement gaps first

## References

- `docs/AI_AGENT_WORKFLOW.md` - Workflow documentation
- `docs/PRE_COMMIT_CHECKLIST.md` - Quality checklist
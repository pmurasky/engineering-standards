---
name: spec-compliance
description: Stage 1 review that verifies requirement and acceptance-criteria compliance before code quality checks. Run this before code-quality review.
version: 1.0.0
category: review
---

# Spec Compliance Review

Run stage-1 spec compliance review to verify requirements before code quality checks.

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

## When to Use

Run this skill first when:
- Reviewing implementation against requirements
- Verifying acceptance criteria are met
- Before running code-quality checks

## References

- `docs/AI_AGENT_WORKFLOW.md` - Workflow documentation
- `docs/PRE_COMMIT_CHECKLIST.md` - Quality checklist

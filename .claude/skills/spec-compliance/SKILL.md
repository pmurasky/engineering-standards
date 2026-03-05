---
name: spec-compliance
description: Stage 1 review that verifies requirement and acceptance-criteria compliance before code quality checks.
argument-hint: "[requirement-or-target]"
disable-model-invocation: true
---

Run stage-1 spec compliance review for the provided scope.

Scope: $ARGUMENTS

<HARD-GATE>
Do not proceed to code-quality review while stage 1 is failing.
If any acceptance criterion is missing, partial, or contradicted, output FAIL.
</HARD-GATE>

Check only:
1. Requirement coverage against stated acceptance criteria
2. Behavioral match between requested and implemented outcomes
3. Scope drift that hides missing required behavior

Do not include SOLID/style/maintainability issues in this stage.

Output format:
1. Status: PASS or FAIL
2. Requirement matrix with evidence
3. Blocking mismatches with expected vs found
4. Next step: rerun stage 1 after fixes, or proceed to stage 2

Required references:
- `docs/AI_AGENT_WORKFLOW.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

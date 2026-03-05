---
name: refactoring-gate
description: Block refactoring when test coverage or test-health prerequisites are not met.
argument-hint: "[target-path-or-component]"
disable-model-invocation: true
---

Run a hard-gate readiness check before any refactoring begins.

Target: $ARGUMENTS

<HARD-GATE>
Do NOT allow refactoring to proceed until all mandatory prerequisites pass.

Mandatory prerequisites:
1. Unit-test coverage for the target code is >= 80%.
2. Coverage for critical paths is 100%.
3. All existing tests are currently passing before the first refactor step.

Blocking rules:
- If coverage evidence is missing, output BLOCKED and require a coverage report.
- If target coverage is < 80%, output BLOCKED and require tests before refactoring.
- If critical-path coverage is < 100%, output BLOCKED and require tests before refactoring.
- If any current test is failing, output BLOCKED and require GREEN first.

Unit tests are the only source for coverage thresholds; integration and E2E tests do not count toward these percentages.
</HARD-GATE>

Allowed exceptions (no coverage gate required):
1. Formatting-only changes (whitespace, lint-driven formatting, comment reflow)
2. Trivial file/package moves or renames with no behavior change

Even for exceptions:
- Verify no behavior change is introduced.
- Run relevant tests after the change.
- Keep one logical micro-commit per step.

Micro-commit integration:
1. STOP: Run this gate before any refactor edit.
2. If BLOCKED: Add tests first using RED -> GREEN and commit those test changes.
3. If READY: Execute one refactoring step only.
4. Run tests after that step and commit immediately.
5. Repeat gate + step cycle for the next refactoring increment.

Output format:
1. Status: READY, BLOCKED, or EXEMPT
2. Gate results:
   - Coverage result (target %, threshold %, evidence source)
   - Critical path result (if applicable)
   - Test health result (pass/fail with command evidence)
3. Required next action

Required references:
- `docs/AI_AGENT_WORKFLOW.md`
- `docs/CODING_PRACTICES.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

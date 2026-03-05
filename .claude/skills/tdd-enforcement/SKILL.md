---
name: tdd-enforcement
description: Enforce strict test-first TDD sequencing with hard gates for RED -> GREEN -> REFACTOR.
argument-hint: "[feature-or-scope]"
disable-model-invocation: true
---

Enforce strict TDD execution for the requested scope.

Scope: $ARGUMENTS

<HARD-GATE>
Never allow production code changes before a failing test is written and observed.

Mandatory sequencing (no reordering):
1. RED: Write exactly one failing test
2. VERIFY RED: Run the test and capture proof it failed for the expected reason
3. GREEN: Write the minimum production code to pass that one test
4. VERIFY GREEN: Run unit tests and confirm pass
5. REFACTOR: Improve structure without changing behavior
6. VERIFY REFACTOR: Run unit tests again and confirm pass

Blocking rules:
- If no failing test evidence is shown, output BLOCKED and stop.
- If more than one new failing test appears in a cycle, output BLOCKED and split work.
- If implementation includes behavior not required by the current failing test, output BLOCKED and remove extra logic.
- If RED failure reason is unrelated (wrong file, compile error, environment issue), output BLOCKED and fix the test first.

Do not recommend commit readiness from this skill.
</HARD-GATE>

Must-watch-it-fail verification:
1. Identify the exact test command used for RED (single test preferred).
2. Capture the failing assertion/error line.
3. Explain why the failure proves missing behavior.
4. Proceed to GREEN only after steps 1-3 are complete.

One-test-at-a-time protocol:
1. Add one failing test.
2. Make it pass with minimal code.
3. Refactor safely.
4. Repeat.

Rationalization defense (reject these patterns):
- "I know it will fail, so I skipped running it." -> Rejected. Must execute and show failure evidence.
- "I implemented first to save time, then wrote tests." -> Rejected. Test-first is mandatory.
- "I added two tests together because they are related." -> Rejected. One failing test per cycle.
- "The test failed due to setup, but that is close enough." -> Rejected. Failure must verify intended behavior gap.
- "I fixed unrelated code while I was here." -> Rejected. Keep scope to current RED->GREEN cycle.

Use `docs/AI_AGENT_WORKFLOW.md` section "Rationalization Defense Table (TDD Excuses -> Required Action)" as the canonical countermeasure matrix.

Output format:
1. Status: READY FOR GREEN, READY FOR REFACTOR, READY FOR NEXT RED, or BLOCKED
2. Evidence:
   - RED command and key failure line
   - GREEN command and pass summary
   - REFACTOR verification command and pass summary
3. Current cycle scope (single behavior)
4. Next smallest step

Required references:
- `docs/AI_AGENT_WORKFLOW.md`
- `docs/PRE_COMMIT_CHECKLIST.md`
- `docs/CODING_PRACTICES.md`

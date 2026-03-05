---
description: Enforce strict test-first TDD sequencing with hard gates
agent: standards-build
---

Enforce strict TDD for this scope: $ARGUMENTS

<HARD-GATE>
Never write production code before writing and running a failing test.

Required sequence (no exceptions):
1. RED: Write exactly one failing test
2. VERIFY RED: Run that test and show why it failed
3. GREEN: Write minimal production code to pass
4. VERIFY GREEN: Re-run tests and confirm pass
5. REFACTOR: Improve code structure without behavior changes
6. VERIFY REFACTOR: Re-run tests and confirm pass

Block progression when:
- No failing-test evidence is provided
- Multiple new failing tests are introduced in one cycle
- Failure reason is unrelated to intended behavior
- Implementation adds behavior not required by the current test
</HARD-GATE>

## Must-Watch-It-Fail Verification

For every RED phase:
1. Run a targeted test command (single test preferred)
2. Capture the key failing assertion/error line
3. Explain why failure proves missing behavior

Proceed to GREEN only after this evidence exists.

## One-Test-At-A-Time Rule

Repeat this micro-cycle:
1. One failing test
2. Minimal implementation
3. Safe refactor
4. Next failing test

## Rationalization Defense (Reject These)

- "I skipped running RED because the test obviously fails"
- "I coded first, then backfilled tests"
- "I added two failing tests because they were related"
- "A setup error is good enough as RED proof"
- "I fixed unrelated code in the same cycle"

If any appear, stop and return BLOCKED with corrective next steps.

Reference:
- `docs/AI_AGENT_WORKFLOW.md`
- `docs/PRE_COMMIT_CHECKLIST.md`
- `docs/CODING_PRACTICES.md`

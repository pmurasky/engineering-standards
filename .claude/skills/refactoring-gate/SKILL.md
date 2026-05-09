---
name: refactoring-gate
description: Block refactoring when test coverage or test-health prerequisites are not met. Run this gate before any refactoring begins.
disable-model-invocation: true
---

# Refactoring Gate

Run a hard-gate readiness check before any refactoring begins.

## Use when

- The user requests refactoring of existing production code
- You are about to perform behavior-preserving structural changes
- You need explicit go/no-go evidence before refactor edits

## Not for

- New feature implementation that changes behavior intentionally
- Formatting-only or trivial rename operations that are exempt
- Proceeding without coverage and test-health evidence

## Trigger Conditions

- User requests refactoring of existing code
- Before any refactoring operation begins
- Phrases: "refactor this", "clean up code", "improve structure", "refactoring"

## Hard Gate

Do NOT allow refactoring to proceed until all mandatory prerequisites pass.

**Mandatory Prerequisites:**
1. Unit-test coverage for the target code is >= 80%
2. Coverage for critical paths is 100%
3. All existing tests are currently passing before the first refactor step

**Blocking Rules:**
- If coverage evidence is missing → output `BLOCKED` and require coverage report
- If target coverage is < 80% → output `BLOCKED` and require tests before refactoring
- If critical-path coverage is < 100% → output `BLOCKED` and require tests before refactoring
- If any current test is failing → output `BLOCKED` and require GREEN first

Unit tests are the only source for coverage thresholds; integration and E2E tests do not count toward these percentages.

## Allowed Exceptions

No coverage gate required for:
1. Formatting-only changes (whitespace, lint-driven formatting, comment reflow)
2. Trivial file/package moves or renames with no behavior change

Even for exceptions:
- Verify no behavior change is introduced
- Run relevant tests after the change
- Keep one logical micro-commit per step

## Micro-Commit Integration

1. **STOP**: Run this gate before any refactor edit
2. **If BLOCKED**: Add tests first using RED -> GREEN and commit those test changes
3. **If READY**: Execute one refactoring step only
4. **Run tests** after that step and commit immediately
5. **Repeat** gate + step cycle for the next refactoring increment

## Output Format

1. **Status**: `READY`, `BLOCKED`, or `EXEMPT`
2. **Gate results**:
   - Coverage result (target %, threshold %, evidence source)
   - Critical path result (if applicable)
   - Test health result (pass/fail with command evidence)
3. **Required next action**

## Token Budget

- **Category**: On-demand workflow
- **Estimated usage**: 500-800 tokens per invocation
- **Frequency**: Per refactoring session (typically 1-5 times per session)
- **Optimization**: Cache coverage results between invocations

## Example

User asks: "Refactor this large service class."

Expected outcome:
- Check target unit-test coverage (>= 80%)
- Check critical-path coverage (100% where applicable)
- Confirm current tests are green
- Output `READY`, `BLOCKED`, or `EXEMPT` with required next action

## Anti-patterns

- Starting refactoring before proving coverage and test health
- Treating integration/E2E coverage as unit-test coverage for gate thresholds
- Mixing bug fixes and refactoring in one unscoped step

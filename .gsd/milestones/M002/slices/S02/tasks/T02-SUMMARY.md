---
id: T02
parent: S02
milestone: M002
verification_result: passed
blocker_discovered: false
---

# T02: Audit remaining 6 skills for compliance gaps

Audit scope completed for all required `.claude/skills/*/SKILL.md` targets listed in S02/T02.

## Gap List (no skill skipped)

| Skill | Frontmatter contract (`name`,`description`,`disable-model-invocation`) | `Use when / Not for` within first 30 lines | No `## References` to `docs/` paths | Line count < 500 | Status |
|---|---|---|---|---|---|
| code-quality | **FAIL** (missing `disable-model-invocation`) | **FAIL** (missing required section format) | **FAIL** (`docs/...` references present) | PASS (62) | Needs fixes in T03 |
| micro-commit | **FAIL** (missing `disable-model-invocation`) | **FAIL** (missing required section format) | **FAIL** (`docs/...` references present) | PASS (116) | Needs fixes in T03 |
| pre-commit | **FAIL** (missing `disable-model-invocation`) | **FAIL** (missing required section format) | **FAIL** (`docs/...` references present) | PASS (84) | Needs fixes in T03 |
| tdd-enforcement | **FAIL** (missing `disable-model-invocation`) | **FAIL** (missing required section format) | **FAIL** (`docs/...` references present) | PASS (116) | Needs fixes in T03 |
| static-analysis-gate | **FAIL** (missing `disable-model-invocation`) | **FAIL** (missing required section format) | **FAIL** (`docs/...` references present) | PASS (78) | Needs fixes in T03 |
| test-coverage | **FAIL** (missing `disable-model-invocation`) | **FAIL** (missing required section format) | **FAIL** (`docs/...` references present) | PASS (71) | Needs fixes in T03 |

## Verification Evidence

- Reviewed each target SKILL file directly and checked:
  - metadata contract
  - required trigger section placement/format
  - CSO reference rule
  - line-count threshold
- Produced explicit PASS/FAIL entry for all 6 required skills.

## Output for next task

T03 should apply the above fixes to both `.claude/skills/` and `.opencode/skills/` surfaces for the same 6 skills, then rerun enforcement tests.

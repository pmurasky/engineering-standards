---
name: tdd-strategies
description: >
  Use when implementing any feature or fixing a bug — TDD problem-solving strategies:
  incremental scaffolding (compile RED to real GREEN), failure verification, SRP for
  tests, GREEN strategies (Fake It, Obvious Implementation, Triangulation), and
  mandatory REFACTOR of both production and test code.
triggers:
  - "starting a new feature with test driven development"
  - "choosing between fake it and triangulation"
  - "figuring out how to begin red green cycle"
  - "planning the refactor phase after green"
not_for:
  - "final staged change review before commit"
  - "broad testing policy and coverage governance"
  - "work where red phase will be skipped"
disable-model-invocation: true
---

# TDD Strategies

**CRITICAL**: Never write production code without a failing test first. Compilation failure counts as RED.

## Use when

- When creating new classes, functions, or features from scratch
- When unsure how to start a TDD cycle
- When choosing between Fake It, Obvious Implementation, or Triangulation
- When planning the REFACTOR phase after reaching GREEN

## Not for

- Final staged-change review right before commit — use the pre-commit checklist for that
- Broad test-pyramid, coverage-policy, or flaky-test governance questions — use testing standards
- Work where you have already decided to skip RED and write production code first

---

## Incremental Scaffolding

Build new code from nothing in small, verifiable steps:

```
1. RED   — Test references non-existent class/function → compile failure
2. GREEN — Create empty skeleton → compiles
3. RED   — Test calls non-existent method → compile failure
4. GREEN — Create method, return fake value (null/0/-1/"") → compiles
5. ADD ASSERTIONS ONLY — Write only assert/verify; more logic = new test
6. RED   — Assertions fail against fake value → verify failure reason
7. GREEN — Write real production code → test passes
8. REFACTOR — Clean up production AND test code → tests stay green
9. COMMIT
```

Fake values MUST differ from expected assertion values (prevents false GREEN).

---

## Verify the Failure

Before going GREEN, confirm **why** the test is red:

| Expected (proceed) | Unexpected (fix test first) |
|---|---|
| Assertion: got `null`, expected `"Jane Doe"` | `NullPointerException` in production code |
| Assertion: got `0`, expected `42` | Wrong test method failing |
| Compile error for missing class/method | Test passes (fake matches expectation) |

---

## GREEN Strategies

| Strategy | When to use |
|---|---|
| **Fake It** | Behavior is complex or unclear — return hardcoded value; generalize later via Triangulation |
| **Obvious Implementation** | Answer is trivially clear — don't fake for ceremony |
| **Triangulation** | Add test cases with different inputs to force generalization from Fake It |

If Obvious Implementation fails → fall back to Fake It.

---

## REFACTOR Phase

After reaching final GREEN, always refactor before committing. Refactor BOTH production and test code.

**Production code:** Extract methods exceeding line limits; remove duplication; rename for clarity; delete dead scaffolding; apply SOLID.

**Test code:** Extract shared setup to helpers (e.g., `createDefaultCustomer()`); rename tests as documentation; remove duplication; improve assertion readability.

Refactoring must NOT change behavior — tests stay GREEN. If a bug is found: STOP, write failing test (RED), fix (GREEN), commit, then resume refactoring.

---

## Anti-Patterns

| ❌ Never | ✅ Always |
|---|---|
| Write production code before a failing test | RED first — no exceptions |
| Skip verifying the test actually fails | Run the test; confirm failure reason is correct |
| Jump straight to Obvious Implementation on complex logic | Use Fake It first, then Triangulate |
| Refactor while RED | Only refactor when GREEN |
| Leave test code unrefactored | Apply SRP and DRY to test code too |
| Defer tests to a separate commit | Every production-code commit includes its tests |

For complete reference material, see [REFERENCE.md](REFERENCE.md) in this skill directory.

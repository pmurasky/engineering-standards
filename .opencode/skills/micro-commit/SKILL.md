---
name: micro-commit-workflow
description: >
  Use when making any code change — enforces the STOP-RED-GREEN-COMMIT-REFACTOR-COMMIT
  cycle, commit patterns for features/refactoring/TDD, Conventional Commits format,
  common mistakes to avoid, self-verification questions, and real-world examples.
triggers:
  - "starting any code change with micro commit workflow"
  - "planning a multi step implementation or refactor"
  - "deciding proper commit granularity for code changes"
  - "following red green commit refactor cycle"
not_for:
  - "choosing issue trackers or sprint priorities"
  - "language specific coding conventions only"
  - "one big commit at the end workflows"
disable-model-invocation: false
---

# Micro-Commit Workflow

**CRITICAL**: AI agents MUST follow this workflow for ALL code changes. No exceptions.

Canonical owner: AI_AGENT_WORKFLOW (see STANDARDS_OWNERSHIP_MATRIX).

## Use when

- Before starting any code change
- When planning a multi-step implementation or refactoring
- When unsure about commit granularity

## Not for

- Issue trackers, sprint priorities, or work-selection decisions
- Language-specific coding conventions — pair with the appropriate language skill
- "One big commit at the end" workflows

---

## Contents

- [Core Principle](#core-principle)
- [Mandatory Workflow](#mandatory-workflow)
- [The Micro-Commit Cycle](#the-micro-commit-cycle)
- [Commit Message Format](#commit-message-format)
- [Common Mistakes](#common-mistakes)
- [Checklist](#checklist)
- [Refactoring Guidelines](#refactoring-guidelines)

---

## Core Principle

**Every logical change = One commit.** Never bundle multiple logical changes.

One logical change is: one refactoring step, one feature, one test update, one doc update.

Every commit MUST be production-ready: tests pass, build succeeds, no lint errors.

---

## Mandatory Workflow

1. `git pull`
2. Create a task list — break work into micro-commits
3. Execute one task at a time; commit after each
4. **Batch checkpoint every 3 tasks**: verify all pass, reassess remaining, then continue

---

## The Micro-Commit Cycle

**Feature with existing tests:**
1. REFACTOR (if needed) → COMMIT
2. RED: write one failing test — don't commit
3. GREEN: implement + run tests → COMMIT `feat: add X` (impl + test together)
4. REFACTOR → COMMIT

**New feature (TDD):**
1. RED: write one failing test — don't commit
2. GREEN: minimal code to pass → COMMIT `feat: add X with test`
3. REFACTOR → COMMIT

**Refactoring only:**
- Each step (extract, rename, move) = one COMMIT

---

## Commit Message Format

```
<type>(<scope>): <description>

[optional body: WHY, not WHAT]
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `perf`, `chore`

**Good:** `refactor: extract timestamp generation into separate method`
**Bad:** `fix stuff` / `update code` / `WIP`

---

## Commit Size Discipline

- Max **300 lines** of insertions per commit — verify with `git diff --cached --stat`
- Scaffolding/setup commits are exempt

---

## Tests-With-Code Gate

Every commit adding or modifying production code **MUST** include unit tests in the same commit. Production-only commits (no tests) are **FORBIDDEN**. Exception: pure refactoring may rely on existing tests.

---

## Common Mistakes

- ❌ Bundling multiple changes in one commit
- ❌ Committing with failing tests
- ❌ Vague commit messages ("update code")
- ❌ Writing new code on top of dead code — delete first (separate commit)

---

## Checklist (Before Each Commit)

- [ ] One logical change only
- [ ] Dead code deleted before writing new code?
- [ ] Tests run and passing
- [ ] Clear Conventional Commits message
- [ ] Task marked complete; batch checkpoint if task 3/6/9

---

## Refactoring Guidelines

**Never refactor without ≥ 80% unit test coverage first.**

Refactoring must be **behavior-preserving** — it targets code smells, complexity warnings, and duplication. Never mix refactoring with feature changes.

1. Establish baseline — verify coverage
2. Add characterization tests if needed — existing tests often cover only happy paths; complex branching, edge cases, and error paths need explicit coverage (see Feathers, *Working Effectively with Legacy Code*)
3. Refactor one step at a time; commit after each step
4. Run ALL tests after each step — must stay green

---

## Success Criteria

- Each commit described in one sentence
- Each commit passes all tests and is deployable
- Git history reads like a story
- Any commit can be reverted without breaking the build

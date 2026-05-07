---
name: pre-commit-checklist
description: >
  Use when about to commit — runs TDD micro-commit compliance, SOLID violation checks
  with code examples, design pattern anti-patterns, code metrics (15-20 line methods,
  300-line classes), testing requirements, documentation, secrets scanning, and
  breaking API change verification.
triggers:
  - "reviewing staged changes before making a commit"
  - "running a pre commit quality checklist"
  - "checking commit readiness against standards"
not_for:
  - "early design discussions before any code changes"
  - "language specific implementation guidance only"
  - "release or merge workflow after commit is made"
disable-model-invocation: false
argument-hint: "[staged|all]"
allowed-tools: "Bash(git diff*), Bash(git status*), Bash(git log*), Bash(wc*), Grep"
---

# Pre-Commit Checklist

**IMPORTANT**: Review before every commit. Every commit MUST be production-ready.

Canonical owner: PRE_COMMIT_CHECKLIST (see STANDARDS_OWNERSHIP_MATRIX).

> **Scope**: $ARGUMENTS

---

## Use when

- Before every commit (mandatory)
- When reviewing staged changes
- When the `/pre-commit` command is invoked

## Not for

- Early design or architecture discussions before actual changes to review
- Language-specific implementation guidance beyond quality gates
- Release, merge, or post-push workflows after the commit has been made

---

## TDD Micro-Commit Checklist (MANDATORY)

- [ ] **Coverage**: ≥80% unit test coverage (unit only); 100% for critical paths
- [ ] **Tests written**: Given-When-Then, edge cases covered
- [ ] **Tests pass**: All tests PASS
- [ ] **Build succeeds**
- [ ] **No lint errors**
- [ ] **Focused commit**: One logical change only
- [ ] **Commit message**: Conventional Commits format
- [ ] **Production-ready**: Deployable now

**Do NOT commit if:** tests fail, build fails, lint errors present, you're bundling multiple features.

---

## Refactoring Prerequisites (MANDATORY)

**Never refactor without tests.**

### Step 1: Establish a Behavioral Baseline

Run existing tests — all must pass. Verify ≥80% unit coverage; 100% for critical paths. If coverage < 80%: **STOP** — write tests first (`test(<scope>): add tests before refactoring`).

### Step 2: Add Characterization Tests (When Needed)

Characterization tests capture what the code *actually does*. Required when: coverage < 80%, only happy paths exist, complex branching, or behavior is unclear from tests alone. Commit separately before refactoring.

### Step 3: Refactor (Behavior-Preserving Only)

Target: code smells, warnings, complexity, SOLID violations, dead code. After each step: run ALL tests → verify build → commit immediately (`refactor(<scope>): <what improved>`).

---

## Quick Pre-Commit Checklist

- [ ] All unit tests pass, build succeeds, no lint errors
- [ ] TDD workflow followed (RED → GREEN → COMMIT or REFACTOR → COMMIT)
- [ ] No SOLID violations, no design pattern anti-patterns
- [ ] Methods ≤ 15-20 lines, classes ≤ 300 lines (body only), no duplicated code
- [ ] Public APIs documented, Conventional Commits message format

## Quick Pre-Push Checklist

- [ ] All unit tests pass, all integration tests pass

---

## SOLID Principles Quick Reference

| Principle | Violation Signal | Fix |
|-----------|-----------------|-----|
| **SRP** | "Manager/Handler/Utility"; method contains "And" | Split into focused classes |
| **OCP** | `when`/switch on type | Use Strategy pattern |
| **LSP** | Subclass throws what parent doesn't | Segregate interfaces |
| **ISP** | Interface > 5 methods; throwing implementations | Split interfaces |
| **DIP** | `val x = ConcreteClass()` in class body | Inject via constructor |

> 📖 Full SOLID checklists: `skills/pre-commit-checklist/references/solid-patterns-reference.md`

---

## Code Metrics / Testing / Docs / Secrets

**Metrics:** no method >3 nesting levels or >5 decision points; no class importing >10 packages.

**Testing:** 80% coverage for new code; no `@Disabled`/`.skip()` without justification; unit tests < 1s, isolated.

**Docs:** public APIs documented; complex logic has inline comments.

**Secrets:** no hardcoded API keys, passwords, tokens (`AKIA...`, `ghp_...`, `sk-...`); no `.env`/`*.key` staged.

**Breaking API changes:** no removed/renamed public methods without deprecation; use deprecate-then-remove.

---

## 🔴 RED LIGHT — DO NOT COMMIT IF:

Tests are failing · Build fails · Lint errors present · Method > 15-20 lines · Class > 300 lines · Direct dependency instantiation · Copy-pasted code · switch/when on types · Missing tests

## 🟢 GREEN LIGHT — OK TO COMMIT IF:

All tests pass · Build compiles · Methods within limit · Classes ≤ 300 lines · Deps injected · No duplication · SOLID principles followed · Tests present · Well-documented

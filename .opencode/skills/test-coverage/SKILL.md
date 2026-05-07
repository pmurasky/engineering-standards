---
name: testing-standards
description: >
  Use when writing tests, reviewing test quality, or setting up test infrastructure —
  cross-language testing standards: test pyramid (unit/integration/E2E ratios), coverage
  requirements (80% unit-only, 100% for critical paths), test doubles taxonomy (dummy/stub/
  fake/spy/mock), parameterized/table-driven tests (JUnit 5, pytest, Go, Vitest), test data
  management (object mother, fixtures, DB seeding), serialization round-trip tests (when to
  write, examples in Kotlin/Java/Python/Go), mutation testing (pitest, mutmut, Stryker),
  property-based testing (Hypothesis, jqwik), snapshot testing guidance, flaky test policy
  (tag, quarantine, fix within 2 sprints), and test execution tiers.
triggers:
  - "writing new tests in any language or stack"
  - "reviewing existing tests for quality gaps"
  - "setting up test infrastructure coverage and ci tiers"
  - "choosing correct test double or parameterized approach"
  - "handling flaky tests and quarantine policy"
not_for:
  - "language specific test syntax better handled elsewhere"
  - "small red green tactic decisions for one change"
  - "static analysis or code style work unrelated to tests"
disable-model-invocation: true
---

# Testing Standards

Cross-language testing conventions that apply regardless of the language or framework in use.

Canonical owner: TESTING_STANDARDS (see STANDARDS_OWNERSHIP_MATRIX).

---

## Table of Contents

- [Use when](#use-when)
- [Not for](#not-for)
- [1. Test Pyramid](#1-test-pyramid)
- [2. Coverage Requirements](#2-coverage-requirements)
- [3. Test Doubles Taxonomy](#3-test-doubles-taxonomy)
- [4. Test Naming and Structure](#4-test-naming-and-structure)
- [5. Flaky Test Policy](#5-flaky-test-policy)
- [6. Test Execution Tiers](#6-test-execution-tiers)
- [7. Core Rules](#7-core-rules)

## Use when

- Writing new tests (unit, integration, E2E) in any language
- Reviewing existing tests for quality or coverage gaps
- Setting up or configuring test infrastructure (CI tiers, coverage tools)
- Deciding which test double type to use (dummy vs. stub vs. fake vs. mock)
- Handling flaky tests — tagging, quarantining, or fixing them

## Not for

- Language-specific test framework syntax when a dedicated language skill would be more precise
- Step-by-step RED/GREEN tactics for one small change — use `tdd-strategies` for that
- Static-analysis or code-style enforcement unrelated to test quality

---

## 1. Test Pyramid

Unit (~70%) → Integration (~20%) → E2E (~10%). Anti-pattern — **Ice Cream Cone**: too many E2E, too few unit tests — suite takes >30 min, single change breaks 50+ tests.

## 2. Coverage Requirements

**Coverage is calculated from unit tests only.** Integration and E2E tests do NOT count toward coverage thresholds.

| Tier | Threshold |
|------|-----------|
| Overall | 80% minimum |
| Branch | 75% minimum |
| Critical paths (auth/authz, financial, pipelines) | 100% |

Coverage is a floor, not a goal.

## 3. Test Doubles Taxonomy

| Type | Use When |
|------|----------|
| **Dummy** | Satisfying a required parameter you don't care about |
| **Stub** | Controlling indirect inputs (e.g., what a repo returns) |
| **Fake** | Integration-style tests without real infrastructure |
| **Spy** | Verifying side effects while preserving real behavior |
| **Mock** | Verifying that specific interactions happened |

Prefer fakes over mocks for repositories. Mock at the boundary only — not internal collaborators. One mock per test.

## 4. Test Naming and Structure

Format: `should<ExpectedOutcome>When<Condition>`. Follow Given-When-Then (Arrange-Act-Assert). One logical behavior per test. No `if`/`for`/`try-catch` in test bodies. No shared mutable state. Test public API only. Use inline literals for simple data; Object Mother/builders for complex domain objects; DB seeding for integration tests.

## 5. Flaky Test Policy

When a test is identified as flaky: **tag it immediately**, **open a GitHub issue**, **quarantine** (separate CI job that does **not** block the pipeline), **fix within 2 sprints**. Zero tolerance: never add a new flaky test.

## 6. Test Execution Tiers

| When | What Runs | Mandatory? |
|------|-----------|------------|
| Before every commit | Unit tests | ✅ Yes — no exceptions |
| Before pushing | Unit + integration tests | ✅ Yes |
| CI pipeline (every push / PR) | Unit + integration + E2E | ✅ Yes — hard gate |

**CI is the hard gate.** CI failures block the PR — no exceptions.

## 7. Core Rules

- **Coverage**: 80% minimum unit test coverage overall; 100% for critical paths. Integration/E2E tests do **NOT** count toward coverage thresholds.
- **Never commit failing tests**: Every commit must be production-ready.
- **Test naming**: `should<ExpectedOutcome>When<Condition>` — never `test1`.
- **Given-When-Then**: Arrange-Act-Assert in every test.
- **No logic in tests**: No `if`, `for`, or `try/catch` in test bodies.
- **No shared mutable state**: Each test sets up its own data.

For complete reference material (parameterized tests, serialization round-trips, Object Mother examples, flaky test tagging in Java/Python/Go), see [REFERENCE.md](REFERENCE.md) in this skill directory.

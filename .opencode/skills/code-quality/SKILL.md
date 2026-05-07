---
name: coding-practices
description: >
  Use when writing, reviewing, or refactoring any code — language-agnostic coding
  practices: YAGNI, SRP, SOLID summary, 15-20 line method limit, domain-driven packaging,
  testing standards (80% unit test coverage, Given-When-Then, TDD), code review checklist,
  error handling, logging, security, and performance guidelines.
triggers:
  - "reviewing code against general engineering standards"
  - "starting a new project or module structure"
  - "learning coding conventions and quality thresholds"
  - "needing language agnostic code review guidance"
not_for:
  - "language specific syntax or framework conventions"
  - "deep security or logging specialist guidance"
  - "issue tracking or pull request workflow tasks"
disable-model-invocation: true
---

# Coding Practices

Language-agnostic engineering standards. Apply to ALL code regardless of language.

Canonical owner: CODING_PRACTICES (see STANDARDS_OWNERSHIP_MATRIX).

## Table of Contents

- [Use when](#use-when) | [Not for](#not-for)
- [General Principles](#general-principles) | [Code Quality](#code-quality) | [SRP](#single-responsibility-principle-srp)
- [SOLID Summary](#solid-principles-summary) | [Design Patterns](#design-patterns) | [Domain Structure](#domain-package-structure)
- [Testing](#testing-standards) | [Code Review](#code-review-checklist) | [Error Handling](#error-handling)
- [Logging](#logging) | [Security](#security-practices) | [Performance](#performance-guidelines)
- [Git Commits](#git-commit-standards) | [Anti-Patterns](#anti-patterns) | [Autonomous Execution](#autonomous-execution)

## Use when

- Before writing or reviewing any code
- When setting up a new project or module
- When unsure about coding conventions or quality thresholds

## Not for

- Language-specific syntax or framework conventions — use the matching language skill
- Deep specialist guidance for security or logging — use dedicated skills
- Issue tracking, sprint selection, or PR workflow tasks

---

## General Principles

- **YAGNI**: Only implement what is needed now.
- **Domain objects first**: Data classes and enums before services.
- **Only write code to create or pass a test** — no speculative code.
- **Build incrementally**: Small changes with tests for each.

---

## Code Quality

- Methods: max 15-20 lines (excluding blanks/braces)
- Classes: max 300 lines (body only)
- Parameters: max 5 — use parameter objects
- Private methods: max 0-2 per class
- No duplicated code (DRY), meaningful names

---

## Single Responsibility Principle (SRP)

Each class has one reason to change. Many private methods signals over-responsibility — extract into separate testable classes.

---

## SOLID Principles (Summary)

| Principle | Rule | Red Flag |
|-----------|------|----------|
| **SRP** | One reason to change | "Manager"/"Handler", 10+ methods |
| **OCP** | Open for extension, closed for modification | switch/when on types |
| **LSP** | Subtypes substitutable for base types | `UnsupportedOperationException` overrides |
| **ISP** | Focused interfaces (≤5 methods) | Empty stubs |
| **DIP** | Depend on abstractions | `new ConcreteClass()` in business logic |

For detailed examples, use the `solid-principles` skill.

---

## Design Patterns

- **Strategy**: Pluggable algorithms behind a common interface (enables OCP)
- **Dependency Injection**: Constructor injection for all dependencies (enables DIP)
- **Parameter Object**: Group related parameters to reduce parameter count

---

## Domain Package Structure

Package by domain: `order/`, `payment/`, `inventory/`, `config/`, `common/` (keep minimal).

---

## Testing Standards

- 80% unit coverage minimum (unit only — no integration/E2E); 100% for critical paths
- Never commit failing tests; Given-When-Then; descriptive names
- TDD: RED → GREEN → COMMIT → REFACTOR

---

## Code Review Checklist

- [ ] Requirements met, SOLID applied, methods within line limit, no duplication
- [ ] 80% unit coverage, no hardcoded secrets, input validation

---

## Error Handling / Logging / Security

- Specific exception types; catch at appropriate levels; never swallow silently
- Structured logging: timestamp, level, message, service, correlation_id; no PII
- Never commit secrets; validate external input; parameterize queries; audit deps

---

## Performance / Git Commits

- Correctness → readability → performance. Profile before optimizing.
- One change per commit. Conventional Commits. Every commit production-ready.

---

## Anti-Patterns

| ❌ Never | ✅ Always |
|---|---|
| Methods > 20 lines | Extract until one clear purpose |
| Classes > 300 lines | Split by responsibility |
| > 5 method parameters | Use parameter object |
| Duplicated logic | Extract to shared utility |
| Multiple changes in one commit | One change = one commit |
| Implementation before tests | RED → GREEN → REFACTOR |

---

## Autonomous Execution

Work through all planned steps without pausing. Stop only for blocking errors (3+ attempts), ambiguous requirements, or completion.

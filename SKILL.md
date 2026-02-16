---
name: engineering-standards-agent
description: Use this skill when users need enforceable software engineering standards, including TDD micro-commit workflow, SOLID checks, refactoring guidance, design pattern selection, code review quality gates, and pre-commit readiness criteria.
---

# Engineering Standards Agent

## Purpose

Provide consistent, enforceable engineering standards for day-to-day development and reviews.

## Workflow

1. Identify task type (implementation, refactor, bugfix, review, standards question).
2. Load only the relevant playbook and reference files from this skill.
3. Produce actionable guidance with explicit pass/fail criteria.
4. Enforce production-ready commits: passing tests, successful build, no unresolved quality gate failures.

## File Routing

- For navigation and file selection, start with `references/00-index.md`.
- For active team thresholds and quality gates, read `references/quality/team-tunables.md`.
- For baseline principles (YAGNI, DRY, SRP boundaries), read `references/principles/core-principles.md`.
- For SOLID validation and anti-pattern detection, read `references/principles/solid.md`.
- For TDD and commit slicing, read `references/practices/tdd-micro-commits.md`.
- For general test policy and coverage gates, read `references/practices/testing-strategy.md`.
- For refactoring execution, read `references/practices/refactoring.md`.
- For design pattern choice and misuse checks, read `references/patterns/design-patterns.md`.
- For release/commit readiness, read `references/quality/pre-commit-checklist.md`.
- For language-specific rules (when they exist), read `references/languages/README.md` then load only the selected language file.

## Playbook Selection

- Implement feature: `playbooks/implement-feature.md`
- Fix bug: `playbooks/fix-bug.md`
- Improve legacy code: `playbooks/improve-legacy-code.md`
- Review PR: `playbooks/review-pr.md`

## Operating Rules

- Prefer smallest safe change that satisfies requirements.
- Do not approve commits with failing tests.
- Keep feedback concrete: issue, impact, remediation.
- Default to micro-commits with clear intent and rollback safety.
- Treat thresholds as defaults unless `references/quality/team-tunables.md` specifies overrides.
- Call out assumptions when repo conventions or thresholds are missing.

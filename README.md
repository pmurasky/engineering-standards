# Engineering Standards

Enforceable software engineering standards for consistent, production-ready development.

## Overview

This repository provides a structured set of engineering standards designed for AI-assisted code review and development workflows. It enforces TDD micro-commits, SOLID principles, safe refactoring practices, and pre-commit quality gates.

**Philosophy**: Smallest safe changes, production-ready commits, concrete feedback.

## Quick Start

1. **Identify your task type**: feature, bugfix, refactor, or review
2. **Load the relevant playbook** from `playbooks/`
3. **Reference standards** from `references/` as needed
4. **Validate against quality gates** before committing

For navigation help, see [`references/00-index.md`](references/00-index.md).

## Repository Structure

```
engineering-standards/
├── SKILL.md                    # Skill definition and routing
├── playbooks/                  # Task-specific workflows
│   ├── implement-feature.md    # Feature development (TDD cycle)
│   ├── fix-bug.md              # Bug fixing with regression tests
│   ├── improve-legacy-code.md  # Safe legacy refactoring
│   └── review-pr.md            # PR review process
├── references/                 # Standards documentation
│   ├── 00-index.md             # Navigation guide
│   ├── principles/             # Core principles (YAGNI, SOLID)
│   ├── practices/              # TDD, testing, refactoring
│   ├── patterns/               # Design patterns and anti-patterns
│   ├── quality/                # Thresholds and checklists
│   └── languages/              # Language-specific standards
└── assets/
    └── templates/              # PR and ADR templates
```

## Core Standards

| Area | Document | Purpose |
|------|----------|---------|
| Principles | [`core-principles.md`](references/principles/core-principles.md) | YAGNI, readability, SRP |
| SOLID | [`solid.md`](references/principles/solid.md) | Validation checklist |
| TDD | [`tdd-micro-commits.md`](references/practices/tdd-micro-commits.md) | Red-Green-Refactor cycle |
| Testing | [`testing-strategy.md`](references/practices/testing-strategy.md) | Coverage policy (80% min) |
| Refactoring | [`refactoring.md`](references/practices/refactoring.md) | Safe refactoring moves |
| Patterns | [`design-patterns.md`](references/patterns/design-patterns.md) | Pattern selection |
| Quality Gates | [`pre-commit-checklist.md`](references/quality/pre-commit-checklist.md) | Go/no-go criteria |
| Thresholds | [`team-tunables.md`](references/quality/team-tunables.md) | Configurable limits |

## Default Thresholds

These defaults can be overridden in [`team-tunables.md`](references/quality/team-tunables.md):

| Metric | Default |
|--------|---------|
| Line coverage | 80% minimum |
| Method length | 15 lines soft limit |
| Class size | 300 lines soft limit |
| Cyclomatic complexity | 10 per method |
| Private methods | 2 per class guideline |

## Language Support

Language-specific standards extend core principles. See [`references/languages/README.md`](references/languages/README.md).

| Language | Status |
|----------|--------|
| Java | [Available](references/languages/java.md) |
| Kotlin | Planned |
| TypeScript | Planned |
| Python | Planned |
| Go | Planned |

## Playbook Selection

| Task | Playbook |
|------|----------|
| Implement new feature | [`implement-feature.md`](playbooks/implement-feature.md) |
| Fix a bug | [`fix-bug.md`](playbooks/fix-bug.md) |
| Refactor legacy code | [`improve-legacy-code.md`](playbooks/improve-legacy-code.md) |
| Review a PR | [`review-pr.md`](playbooks/review-pr.md) |

## Operating Rules

- Every committed state must be production-ready
- Tests pass, build succeeds, no unresolved lint failures
- Prefer micro-commits with clear intent and rollback safety
- Feedback is concrete: issue → impact → remediation
- Thresholds are defaults unless overridden in `team-tunables.md`

## Extending Standards

**Add a language pack**: Create `references/languages/<language>.md` following the structure in `java.md`, then register it in `references/languages/README.md`.

**Override thresholds**: Document overrides in `references/quality/team-tunables.md` with rationale and scope.

**Add a playbook**: Create `playbooks/<task-type>.md` following existing playbook structure, then register it in `SKILL.md`.
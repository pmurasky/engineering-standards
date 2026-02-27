---
description: Core engineering standards - TDD, micro-commits, SOLID, code quality
alwaysApply: true
---

# Engineering Standards

You MUST follow these standards for ALL code changes.

## TDD Micro-Commit Cycle
For ALL code changes, follow the STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT cycle. See `docs/AI_AGENT_WORKFLOW.md` for the full workflow.

## Code Quality Gates
Apply rules from `docs/CODING_PRACTICES.md`: methods ≤20 lines, classes ≤300 lines, ≤2 private methods, ≤5 params, DRY. Follow SOLID principles — see `docs/SOLID_PRINCIPLES.md` for the full guide with examples.

## Commits
- One logical change per commit
- Conventional Commits: `<type>(<scope>): <description>` — see `docs/AI_AGENT_WORKFLOW.md` for format
- Every commit production-ready (tests pass, builds, no lint errors)

## Red Flags - STOP and Ask
- Modifying 10+ files
- Breaking a public API
- Tests failing after your change
- Code has < 80% test coverage

## Detailed References
Read these files for detailed guidance when needed:
- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit workflow
- `docs/CODING_PRACTICES.md` - Language-agnostic practices, SOLID examples, and TDD
- `docs/CODING_STANDARDS.md` - Standards index (table of contents)
- `docs/PRE_COMMIT_CHECKLIST.md` - Pre-commit checklist
- `docs/DESIGN_PATTERNS.md` - Design patterns catalog and guidance
- `docs/SOLID_PRINCIPLES.md` - SOLID principles with multi-language examples
- `docs/JAVA_STANDARDS.md` - Java conventions (when working with Java)
- `docs/KOTLIN_STANDARDS.md` - Kotlin conventions (when working with Kotlin)

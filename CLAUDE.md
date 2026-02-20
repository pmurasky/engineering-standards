# Engineering Standards

You MUST follow these engineering standards for ALL code changes. No exceptions.

## Core Principles

### 1. Micro-Commit Workflow
Every logical change = one commit. Never bundle multiple logical changes into one commit.

- One refactoring step per commit
- One feature implementation per commit
- One test update per commit
- One documentation update per commit

### 2. TDD Micro-Commit Cycle
For ALL code changes, follow the STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT cycle. See `docs/AI_AGENT_WORKFLOW.md` for the full workflow.

### 3. Production-Ready Commits
Every commit MUST be production-ready:
- All tests pass
- Build succeeds
- No lint errors
- Code is deployable

### 4. Code Quality Rules
- Maximum method length: 15-20 lines (excluding blank lines and braces; see language-specific standards for exact limit)
- Maximum class length: 300 lines (consider refactoring if larger)
- Maximum 0-2 private methods per class (SRP guideline)
- Maximum 5 parameters per method (use parameter objects)
- No duplicated code (DRY principle)

### 5. SOLID Principles
- **SRP**: Each class has ONE reason to change
- **OCP**: Open for extension, closed for modification (use Strategy Pattern)
- **LSP**: Subtypes must be substitutable for base types
- **ISP**: Prefer focused interfaces over fat interfaces
- **DIP**: Depend on abstractions, not concrete classes (use dependency injection)

### 6. Commit Message Format
Use Conventional Commits:
```
<type>(<scope>): <description>

[body explaining WHY, not WHAT]
```

Types: feat, fix, refactor, test, docs, perf, chore

### 7. Testing Standards
- Minimum 80% unit test coverage overall (unit tests only -- integration/E2E tests do not count toward coverage)
- 100% unit test coverage for critical paths
- Use Given-When-Then structure
- Descriptive test names (e.g., `shouldSelectLatestVersionWhenAvailable`)
- Never commit failing tests (every commit must be production-ready, no exceptions)

### 8. Test Execution Tiers
- **Before every commit**: Run unit tests (mandatory, no exceptions)
- **Before pushing**: Run unit tests + integration tests
- **CI pipeline**: Runs all tests (unit + integration + E2E) as hard gate before merge

### 9. Refactoring Prerequisites
**Never refactor without tests. No exceptions.**
- Before refactoring, verify unit test coverage is at least 80% for the code being changed (unit tests only)
- If coverage is below 80%, STOP and write unit tests FIRST (separate commits)
- All tests MUST pass before starting any refactoring
- After each refactoring step, run ALL tests and commit immediately
- See `docs/AI_AGENT_WORKFLOW.md` and `docs/PRE_COMMIT_CHECKLIST.md` for full details

## Detailed Standards References

When you need detailed guidance, read the relevant file:

- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit workflow and AI agent instructions
- `docs/CODING_PRACTICES.md` - Language-agnostic coding practices, SOLID examples, testing, and TDD
- `docs/CODING_STANDARDS.md` - Standards index (table of contents)
- `docs/GO_STANDARDS.md` - Go-specific conventions (when working with Go)
- `docs/JAVA_STANDARDS.md` - Java-specific conventions (when working with Java)
- `docs/KOTLIN_STANDARDS.md` - Kotlin-specific conventions (when working with Kotlin)
- `docs/PYTHON_STANDARDS.md` - Python-specific conventions (when working with Python)
- `docs/TYPESCRIPT_STANDARDS.md` - TypeScript/JavaScript conventions (when working with TypeScript or JavaScript)
- `docs/PRE_COMMIT_CHECKLIST.md` - Pre-commit quality checklist
- `docs/DESIGN_PATTERNS.md` - Design patterns catalog and guidance
- `docs/SOLID_PRINCIPLES.md` - SOLID principles with multi-language examples
- `docs/STATIC_ANALYSIS_STANDARDS.md` - Static analysis standards (PMD, detekt, Checkstyle, CPD)
- `docs/CHECKSTYLE_STANDARDS.md` - Checkstyle style enforcement (Java only)
- `docs/ARCHUNIT_STANDARDS.md` - Architecture testing with ArchUnit (Java/Kotlin)
- `docs/SPOTBUGS_STANDARDS.md` - SpotBugs bytecode bug detection (Java only)
- `docs/ADR_STANDARDS.md` - Architecture Decision Records (ADR) guidance
- `docs/SECURITY_STANDARDS.md` - Security standards (auth, secrets, OWASP, API security)

Load these on a need-to-know basis, not all at once.

## Before Making ANY Code Changes

1. Pull latest changes: `git pull`
2. Read and acknowledge: "I will follow the micro-commit workflow"
3. Break work into a task list of micro-commits
4. Execute one task at a time, committing after each one
5. Run unit tests before every commit
6. Run unit tests + integration tests before pushing
7. Follow the pre-commit checklist

## Selecting Work

When asked what to work on next, consult GitHub Issues: `gh issue list --label "P1: should fix" --state open`. Prioritize P1 over P2. Reference issues in commits (e.g., `closes #2`). See `docs/AI_AGENT_WORKFLOW.md` for full details.

## Red Flags (Stop and Ask User)

If you encounter these situations, STOP and ask:

1. **Unclear scope**: Change requires modifying 10+ files
2. **Breaking change**: Change will break a public API
3. **Test failures**: Tests failing after your change
4. **Conflicting patterns**: Existing code doesn't follow SOLID
5. **Missing tests**: Code being changed has < 80% unit test coverage

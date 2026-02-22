# Conversion Plan Template

**PURPOSE**: Reusable plan template for converting/porting a project from one framework to another. Enforces "behavior first, then quality" via explicitly gated phases.

**CRITICAL**: Each phase has a gate. You MUST pass the gate before advancing to the next phase. Do not skip phases or reorder them.

---

## How to Use This Template

1. Copy this template into your workspace as `<PROJECT>-PLAN.md`
2. Fill in the project-specific details in the **Project Context** section
3. Execute phases in order, checking off items as you go
4. At each phase gate, verify ALL criteria before proceeding
5. Generate reports at the end

---

## Project Context (Fill In)

| Field | Value |
|-------|-------|
| Source project | `<source-project-name>` |
| Source framework | `<e.g., Ktor 1.x, Spring Boot 2.x>` |
| Target project | `<target-project-name>` |
| Target framework | `<e.g., Ktor 4.x, Spring Boot 3.x>` |
| Language | `<e.g., Kotlin, Java>` |
| Date started | `<YYYY-MM-DD>` |

---

## Phase 1: Pre-Work

### 1.1 Read Engineering Standards

- [ ] Read `./CODING_PRACTICES.md` — general practices, SOLID, TDD
- [ ] Read `./AI_AGENT_WORKFLOW.md` — micro-commit workflow
- [ ] Read `./PRE_COMMIT_CHECKLIST.md` — pre-commit quality checklist
- [ ] Read language-specific standards (e.g., `./KOTLIN_STANDARDS.md`)
- [ ] Acknowledge: "I will follow the micro-commit workflow and all code quality gates"

### 1.2 Capture Behavioral Baseline from Source Project

Before writing any code, document the source project's behavior:

- [ ] **Error response format**: Capture the exact JSON shape for error responses (field names, nesting, status codes)
- [ ] **Content-Type headers**: Document what each endpoint returns (e.g., `application/json`, `text/plain`)
- [ ] **Route inventory**: List all routes with HTTP method, path, and purpose
- [ ] **Authentication/authorization**: Document RBAC roles, permission model, and access rules
- [ ] **Health/status endpoints**: Document format, Content-Type, and response shape
- [ ] **Acceptance tests**: Identify existing acceptance/integration tests that verify behavior

Record the baseline in a `<PROJECT>-BEHAVIORAL-BASELINE.md` file.

### 1.3 Set Up Target Project

- [ ] Create target project repository/directory
- [ ] Initialize build system (Gradle, Maven, npm, etc.)
- [ ] Add dependencies for target framework
- [ ] Copy agent files and engineering standards into target project
- [ ] Verify build compiles with empty project structure
- [ ] Set up static analysis (Detekt, PMD, ESLint, etc.) from the start

### Phase 1 Gate

**ALL must be true before proceeding:**
- [ ] Engineering standards read and acknowledged
- [ ] Behavioral baseline documented
- [ ] Target project compiles with empty structure
- [ ] Static analysis configured and passing on empty project

---

## Phase 2: Port Behavior (Behavior First)

**Goal**: Get the converted project to behave identically to the source project. Follow all code quality gates during porting — do NOT accumulate technical debt.

### 2.1 Port Core Infrastructure

- [ ] Configuration/environment handling
- [ ] Database connectivity and migrations
- [ ] Authentication/authorization middleware
- [ ] Error handling and response formatting (MUST match source baseline)
- [ ] Health/status endpoints (MUST match source Content-Type and format)
- [ ] Logging setup

### 2.2 Port Business Logic

For each domain area in the source project:

- [ ] Port domain models / data classes
- [ ] Port service layer (follow SRP — decompose if source has god classes)
- [ ] Port routes/controllers
- [ ] Write unit tests (meet repo standard: minimum 80% overall unit test coverage, 100% for critical paths)
- [ ] Run acceptance tests from source project against converted project

**Quality rules during porting (NO EXCEPTIONS):**
- Every class <= 300 lines. If porting a class that would exceed 300 lines, decompose it NOW, not later.
- Every method <= language-specific limit (15-20 lines). Extract methods immediately.
- No `@Suppress` for structural violations. If the linter flags it, fix it.
- No `!!` in production Kotlin code. Fix nullability at the source.
- Constructor injection for all dependencies. No hard-coded instantiation.
- Follow TDD micro-commit cycle: STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT

### 2.3 Port Remaining Features

- [ ] Port any remaining routes/endpoints
- [ ] Port scheduled tasks, background jobs, etc.
- [ ] Port any middleware or filters

### Phase 2 Gate

**ALL must be true before proceeding:**
- [ ] All source project routes exist in converted project
- [ ] Error response format matches source baseline exactly
- [ ] Content-Type headers match source baseline
- [ ] RBAC/authorization behavior matches source
- [ ] Source project acceptance tests pass against converted project (target: 100%)
- [ ] Unit test coverage >= 80% (unit tests only)
- [ ] All unit tests pass
- [ ] Build succeeds
- [ ] Static analysis passes (Detekt/PMD/ESLint — zero violations)

---

## Phase 3: Quality Sweep

**Goal**: Verify and improve code quality beyond the minimums enforced during Phase 2.

### 3.1 Structural Quality Audit

- [ ] No class exceeds 300 lines
- [ ] No method exceeds language-specific limit (15-20 lines)
- [ ] No method has more than 5 parameters
- [ ] Zero `@Suppress` for structural violations (`LargeClass`, `TooManyFunctions`, `LongMethod`, `LongFunction`, `CyclomaticComplexity`, `CyclomaticComplexMethod`, `LongParameterList`, `TooGenericExceptionCaught`)
- [ ] Zero `!!` in production code
- [ ] Maximum 0-2 private methods per class (SRP)
- [ ] Interfaces used for dependency injection (DIP)

### 3.2 Documentation

- [ ] KDoc/Javadoc on all public classes and methods
- [ ] README updated with setup instructions
- [ ] Architecture decisions documented (ADR if significant)

### 3.3 Test Quality

- [ ] Unit test coverage >= 80% overall (unit tests only)
- [ ] 100% unit test coverage for critical paths
- [ ] All tests follow Given-When-Then structure
- [ ] Descriptive test names (e.g., `shouldReturnErrorWhenUserNotFound`)
- [ ] Mutation testing passes (if configured)

### Phase 3 Gate

**ALL must be true before proceeding:**
- [ ] All structural quality items pass
- [ ] All documentation items complete
- [ ] All test quality items pass
- [ ] Full Detekt/PMD/ESLint scan passes with zero violations
- [ ] All acceptance tests still pass (no regressions from quality improvements)

---

## Phase 4: Verification

**Goal**: Final verification that BOTH behavioral fidelity AND code quality are achieved.

### 4.1 Behavioral Verification

- [ ] Run source project acceptance tests against converted project
- [ ] Document pass rate: `___/___` tests passing
- [ ] For any failures, document root cause and resolution
- [ ] Compare error responses side-by-side with source baseline
- [ ] Verify all Content-Type headers match

### 4.2 Quality Verification

- [ ] Run full static analysis suite — zero violations
- [ ] Run full unit test suite — all pass
- [ ] Run coverage report — meets thresholds
- [ ] Run mutation testing (if configured) — meets thresholds
- [ ] Count `@Suppress` annotations — must be zero for structural violations
- [ ] Count `!!` in production code — must be zero
- [ ] Largest class line count: `___` (must be <= 300)
- [ ] Largest method line count: `___` (must be <= language limit)

### Phase 4 Gate

**ALL must be true to consider the conversion complete:**
- [ ] 100% acceptance test pass rate (or documented exceptions with user approval)
- [ ] Zero structural `@Suppress` annotations
- [ ] Zero `!!` in production code
- [ ] All quality metrics within thresholds
- [ ] Build passes
- [ ] Static analysis passes

---

## Phase 5: Reports

### 5.1 Generate Reports

- [ ] **Verification report**: Acceptance test results, pass rate, any failures with root cause
- [ ] **Comparison report**: Side-by-side metrics (source vs. converted) — LOC, test count, coverage, class count, largest class, etc.
- [ ] **Quality summary**: Static analysis results, coverage, mutation testing

### 5.2 Cleanup

- [ ] Stop any running services (app servers, database containers)
- [ ] Remove any temporary test data
- [ ] Update project status tracking or project management system (if used)

---

## Summary Metrics (Fill In When Complete)

| Metric | Source | Converted |
|--------|--------|-----------|
| Lines of code | | |
| Number of files | | |
| Unit tests | | |
| Acceptance tests | | |
| Unit test coverage | | |
| Largest class (lines) | | |
| Largest method (lines) | | |
| `@Suppress` count | | |
| `!!` count | | |
| Detekt/PMD violations | | |
| Acceptance test pass rate | | |

---

## Lessons Learned (Fill In)

Document what went well, what could be improved, and any patterns discovered during the conversion.

1. ...
2. ...
3. ...

---

**Last Updated**: February 2026
**Version**: 1.0

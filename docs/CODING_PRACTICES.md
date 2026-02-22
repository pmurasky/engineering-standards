# General Coding Practices and Standards

## Overview
This document outlines language-agnostic coding practices, testing expectations, and development principles.

## General Principles

### YAGNI (You Aren't Gonna Need It)
**Do not implement features, classes, methods, or infrastructure until you actually need them.**

- **Only create what is needed now**: Don't build for hypothetical future requirements
- **No speculative generality**: Don't add abstraction layers "just in case"
- **Create directories/packages when needed**: Don't create empty package structures upfront
- **Add dependencies when required**: Don't add libraries until you actually use them
- **Incremental development**: Build the simplest thing that works, then refactor when needed

**Benefits:**
- Less code to maintain
- Simpler codebase
- Faster development
- Easier to understand
- Reduced over-engineering

**Examples:**
- ✅ Create a `User` class when you need to store user data
- ❌ Create `User`, `UserFactory`, `UserBuilder`, `UserValidator` upfront "just in case"
- ✅ Add a package when you have classes to put in it
- ❌ Create all packages for the entire architecture before writing any code
- ✅ Add a dependency when you need its functionality
- ❌ Add every dependency you might possibly need

### Code Quality
- Write clean, readable, and maintainable code
- Follow SOLID principles
- Prefer composition over inheritance
- **Keep methods small and focused (single responsibility)**
- **Maximum method length: 15-20 lines of code** (excluding blank lines and braces; see language-specific standards for exact limit)
  - If a method exceeds the limit, extract helper methods
  - This enforces single responsibility and improves testability
  - Exception: Test methods may be longer if needed for clarity
- Avoid code duplication (DRY principle)
- Use meaningful names for variables, methods, and classes

### Single Responsibility Principle (SRP)
**Each class should have only one reason to change.**

- **Limit private methods**: If a class has many private methods, it's likely doing too much
  - Private methods often indicate hidden responsibilities that should be extracted
  - Extract complex private logic into separate, testable classes
  - Aim for 0-2 private methods per class; more suggests refactoring needed
- **Extract functionality into separate classes** when:
  - Logic becomes complex enough to need dedicated testing
  - A method or group of methods serves a distinct purpose
  - You find yourself wanting to test private methods directly
- **Prefer small, focused classes** over large classes with many private methods
- **Benefits**:
  - Easier to test (public interfaces instead of private methods)
  - Better separation of concerns
  - More reusable components
  - Clearer dependencies

**Examples:**
- ❌ **Bad**: `UserService` with private methods: `validateEmail()`, `hashPassword()`, `sendWelcomeEmail()`, `logActivity()`
  - Too many responsibilities (validation, security, email, logging)
  - Private methods can't be tested independently
- ✅ **Good**: Separate classes: `EmailValidator`, `PasswordHasher`, `EmailService`, `ActivityLogger`
  - Each class has single responsibility
  - All functionality is testable
  - Can be reused independently

- ❌ **Bad**: `DataProcessor` with private methods: `parseXml()`, `validateData()`, `transformData()`, `saveToDatabase()`
  - Parsing, validation, transformation, and persistence mixed together
- ✅ **Good**: `XmlParser`, `DataValidator`, `DataTransformer`, `DataRepository`
  - Clear separation of concerns
  - Each class easily testable

**When to use private methods:**
- Simple helper methods (1-3 lines) that aid readability
- Methods that truly only exist to support the single public responsibility
- If you have > 2 private methods, consider extraction

### SOLID Principles

Follow SOLID principles strictly. For the full guide with multi-language examples, real-world analogies, and detailed violation signals, see [SOLID_PRINCIPLES.md](./SOLID_PRINCIPLES.md). Before every commit, consult the [PRE_COMMIT_CHECKLIST.md](./PRE_COMMIT_CHECKLIST.md) for the detailed SOLID checklist.

**Summary:**

- **SRP** -- Each class has ONE reason to change. Extract responsibilities into focused classes.
- **OCP** -- Open for extension, closed for modification. Use Strategy pattern and polymorphism.
- **LSP** -- Subtypes must be substitutable for base types. No surprise exceptions or weakened contracts.
- **ISP** -- Prefer focused interfaces (5 methods max) over fat ones. No empty stubs.
- **DIP** -- Depend on abstractions, not concrete classes. Use constructor injection.

### Design Patterns

#### Strategy Pattern
- Pluggable algorithms behind a common interface
- **Benefit**: Open/Closed Principle compliance

#### Dependency Injection
- Constructor injection for all dependencies
- **Benefit**: Testability and flexibility

#### Parameter Object
- Group related parameters into a single object
- **Benefit**: Reduced parameter count, improved readability

#### Template Method
- Define algorithm skeleton in base class, let subclasses override steps
- **Benefit**: Code reuse and consistent flow

### Domain Package Structure

Follow **domain-driven package organization**:

```
com.example.project/
├── order/            # Order domain
├── payment/          # Payment processing
├── inventory/        # Inventory management
├── notification/     # Notification services
├── config/           # Configuration
└── common/           # Shared utilities (keep minimal)
```

See [KOTLIN_STANDARDS.md](./KOTLIN_STANDARDS.md#package-organization-domain-driven-design) or [JAVA_STANDARDS.md](./JAVA_STANDARDS.md#package-organization-domain-driven-design) for language-specific details.

### Documentation
- All public APIs must have comprehensive documentation
- Include examples in documentation where appropriate
- Document non-obvious implementation decisions with inline comments
- Keep README and other documentation up-to-date

### Error Handling
- Use specific exception types, not generic ones
- Document all thrown exceptions
- Catch exceptions at appropriate levels
- Provide meaningful error messages
- Log errors with appropriate context
- Don't swallow exceptions silently

### Logging
- Use appropriate log levels (ERROR, WARN, INFO, DEBUG, TRACE)
- Use structured logging with required fields (timestamp, level, message, service, correlation_id)
- Include context as structured key-value fields, not embedded in message strings
- No sensitive information in logs (passwords, tokens, PII)
- See [LOGGING_STANDARDS.md](./LOGGING_STANDARDS.md) for full standards on structured logging, correlation IDs, and PII handling

## Testing Standards

### Critical Rule: Never Commit Failing Tests
**ALL TESTS MUST PASS BEFORE COMMITTING CODE.**

This is a non-negotiable requirement for maintaining code quality and team productivity.

#### Why This Rule Exists
- **Build Stability**: Failing tests break CI/CD pipelines and block deployments
- **Team Productivity**: Other developers can't work effectively with a broken test suite
- **Code Confidence**: Tests are our safety net - broken tests mean no safety net
- **Technical Debt**: Ignoring test failures leads to accumulating technical debt
- **Debugging Difficulty**: Harder to identify which change broke which test

#### Pre-Commit Checklist
Before committing ANY code, you MUST:

1. **Run all tests locally**:
   ```bash
   # Run your project's test suite, e.g. one of:
   # ./gradlew test
   # npm test
   # pytest
   # go test ./...
   # dotnet test
   ```

2. **Verify all tests pass**:
   - Check output for all tests passing with zero failures
   - No skipped or ignored tests without justification

3. **Fix ALL failures** before committing:
   - If a test fails, FIX THE CODE or FIX THE TEST
   - Never commit with "TODO: fix test later"
   - Never skip or @Ignore tests to make the build pass

4. **Run tests again** after fixing:
   - Changes to fix one test might break another
   - Always verify the ENTIRE test suite passes

#### There Are No Acceptable Scenarios for Committing with Failing Tests

**Every commit must be production-ready with all tests passing. No exceptions.**

- **TDD RED phase**: Write failing tests, then implement until GREEN, then commit. Never commit during the RED phase.
- **Feature branches**: Every commit on every branch must have passing tests. Not just the merge commit.

#### What To Do When Tests Fail

**Option 1: Fix the code** (most common)
- The test is correct, your code has a bug
- Fix the implementation to make the test pass

**Option 2: Fix the test** (when test is wrong)
- Test has incorrect expectations
- Test doesn't match updated requirements
- Update the test to reflect current behavior

**Option 3: Remove obsolete tests**
- Functionality was intentionally removed/changed
- Test no longer relevant to current codebase
- Document WHY in commit message

**Option 4: Update tests for API changes**
- Public API was intentionally changed
- Update all affected tests to use new API
- Never leave old tests failing

#### CI/CD Integration
- All pull requests MUST have passing tests
- Automated builds will reject commits with failing tests
- No exceptions for "urgent" fixes - fix the tests too

#### Enforcement
Violations of this rule are considered serious quality issues:
- Pull requests with failing tests will be rejected
- Commits with failing tests may be reverted
- Repeated violations indicate need for additional training

### Test Coverage Requirements

**Coverage is calculated from unit tests only.** Integration tests, end-to-end tests, and other test types are valuable for quality assurance but do NOT count toward coverage thresholds. This ensures that core logic is verified in fast, isolated, deterministic tests.

- **Minimum Coverage**: 80% overall (unit tests only)
- **Critical Paths**: 100% coverage (unit tests only) for:
  - Core business logic and domain rules
  - Payment or financial calculations
  - Authentication and authorization flows
  - Data transformation and validation pipelines
- **Branch Coverage**: Minimum 75% (unit tests only)

### Test Types

**1. Unit Tests**
- Test individual classes/methods in isolation
- Mock all external dependencies
- Fast execution (< 1 second per test)
- Example: `OrderServiceTest`, `PaymentProcessorTest`

**2. Integration Tests**
- Test component interactions
- May use real implementations (with test doubles for external services)
- Example: `OrderCheckoutIntegrationTest`

**3. End-to-End Tests**
- Test complete workflows
- Use real projects as fixtures
- Example: `UserRegistrationE2ETest`

### Test Naming Convention
Use descriptive test names that explain what is being tested:

**Good examples:**
- `shouldSelectLatestNonVulnerableVersionWhenAvailable()`
- `shouldThrowExceptionWhenNoRepositoryIsConfigured()`
- `shouldParseGradleBuildFileCorrectly()`

**Avoid generic names:**
- `test1()`
- `testVersionSelection()`

### Test Structure (Given-When-Then)
```
@Test
public void shouldFilterOutVulnerableVersions() {
    // Given - Setup test data and mocks
    [setup test data and dependencies]

    // When - Execute the code under test
    [call the method being tested]

    // Then - Assert expected outcomes
    [verify results]
}
```

### Mocking Guidelines
- Mock external dependencies (HTTP clients, file system, databases)
- Don't mock value objects or simple data classes
- Verify important interactions with mocks
- Use realistic test data

### Test Data and Fixtures
- Store test data in `test/resources/fixtures/`
- Use realistic but minimal examples
- Document any non-obvious test data
- Consider using factories or builders for complex objects

### Assertions
- Use descriptive assertion messages
- Prefer specific assertions over generic ones
- Use assertion libraries for better readability

### Test Independence
- Each test must be independent and isolated
- No shared mutable state between tests
- Tests should pass when run individually or as a suite
- Clean up resources in teardown methods

### Performance Testing
- Mark slow tests with appropriate annotations
- Consider separate test suite for performance tests
- Document expected performance characteristics

### Test Execution Tiers

Different test types run at different stages. This balances fast feedback with thorough validation.

| When | What Runs | Why |
|------|-----------|-----|
| Before every commit | Unit tests | Fast, isolated, deterministic — no reason to skip |
| Before pushing (pre-push) | Unit tests + integration tests | Catch cross-component issues before they reach the team |
| CI pipeline (on every push/PR) | Unit tests + integration tests + E2E | Hard gate — enforces full validation before merge |

**Rules:**
- **Unit tests are mandatory before every commit.** No exceptions. If unit tests fail, do not commit.
- **Unit tests + integration tests are mandatory before pushing.** Use a pre-push hook or run manually. If either fails, fix locally before pushing.
- **CI is the hard gate.** Even if a developer skips pre-push hooks, CI catches failures before merge. CI failures block the PR.
- **Never skip tests to "push faster."** If integration tests are too slow to run pre-push, that's a signal to optimize the test suite, not to skip them.

**Example pre-push hook:**
```bash
# .git/hooks/pre-push
#!/bin/bash
echo "Running pre-push checks..."

# Run unit tests (should already pass from pre-commit)
# ./gradlew test || exit 1
# npm test || exit 1

# Run integration tests
# ./gradlew integrationTest || exit 1
# npm run test:integration || exit 1
# pytest tests/integration/ || exit 1

echo "All pre-push checks passed"
```

## Code Review Checklist

### Functionality
- [ ] Code meets requirements
- [ ] Edge cases are handled
- [ ] Error handling is appropriate
- [ ] No obvious bugs or logic errors

### Code Quality
- [ ] Follows coding standards
- [ ] No code duplication
- [ ] Appropriate use of design patterns
- [ ] SOLID principles applied
- [ ] **All methods are within language-specific line limit** (15-20 lines; see language standards)
- [ ] **Commit is focused on single logical change** (micro commit)

### Testing
- [ ] Adequate unit test coverage (minimum 80%, unit tests only)
- [ ] Tests are meaningful and not just for coverage
- [ ] Tests follow naming conventions
- [ ] Integration/E2E tests for new features

### Documentation
- [ ] Public APIs are documented
- [ ] Complex logic has explanatory comments
- [ ] README updated if needed
- [ ] Breaking changes noted

### Security
- [ ] No hardcoded secrets or credentials
- [ ] Input validation for external data
- [ ] Secure handling of sensitive information
- [ ] Dependencies have no known critical vulnerabilities

### Performance
- [ ] No obvious performance issues
- [ ] Appropriate use of caching
- [ ] Database queries are optimized
- [ ] No unnecessary object creation in loops

## Git Commit Standards

### Micro Commits Philosophy
**Practice micro commits** - commit early and often with small, focused changes:

- **Commit frequently**: After completing each small unit of work
- **One logical change per commit**: Each commit should represent a single, coherent change
- **Benefits**:
  - Easier code review
  - Simpler debugging and git bisect
  - Better project history and documentation
  - Easy to revert specific changes
  - Less risk of losing work

**Examples of micro commit granularity**:
- Add a single data class
- Implement one method
- Add tests for one method
- Refactor one function
- Update documentation for one component
- Fix one specific bug

**Avoid**:
- Large commits with multiple unrelated changes
- Batching many files into one commit
- Waiting until end of day to commit
- Committing broken/non-compiling code (every commit must be production-ready)

### Commit Message Format

Scope is recommended and may be omitted for trivial cross-cutting changes.

```
<type>(<scope>): <subject>
# or
<type>: <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring (no functionality change)
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Build process, dependencies, tooling

### Examples
```
feat(scanner): add support for GitHub Advisory Database

Integrate GitHub Advisory Database as an additional source for
vulnerability information. This provides more comprehensive coverage
for security issues.

Closes #123
```

```
fix(resolver): handle missing pom.xml gracefully

Previously, the resolver would crash when a dependency didn't have
a pom.xml file. Now it logs a warning and continues processing.
```

## Build and CI Standards

### Build Requirements
- All builds must pass before merging
- No compiler warnings allowed
- Code formatting must pass
- Static analysis must pass

### Pre-commit Checks
- Run unit tests locally before committing
- Format code according to standards
- Remove debug statements and commented code
- Update documentation if needed

### Pre-push Checks
- Run unit tests + integration tests before pushing
- Use a pre-push hook to automate this (see Test Execution Tiers above)
- If integration tests fail, fix locally before pushing

### Continuous Integration
- All tests must pass on CI (unit + integration + E2E)
- Unit test coverage must meet minimum threshold (unit tests only)
- Security scans must pass
- Build artifacts must be generated successfully
- CI is the hard gate — failures block the PR from merging

## Dependencies

### Dependency Management
- **Always use the latest stable (GA) release** when adding a new dependency — never intentionally start on an older version
- Avoid dependencies with known vulnerabilities — verify against [NVD](https://nvd.nist.gov/), [OSV](https://osv.dev/), or [GitHub Advisory Database](https://github.com/advisories) before adding
- Document the reason for each major dependency in the commit message
- Prefer well-maintained libraries (active releases, responsive maintainers)
- Check licenses for compatibility

### Version Pinning
- **Direct dependencies**: pin the exact latest stable version explicitly at the time of addition
- **BOM-managed ecosystems** (Spring Boot, Quarkus, Micronaut, etc.): trust the BOM — do NOT manually pin transitive dependency versions; the BOM ensures a patched, compatible set
- Update dependencies when vulnerabilities are disclosed, not just on a scheduled cadence
- Regular dependency review (monthly) to proactively catch newly disclosed CVEs

## Security Practices

### Secrets Management
- Never commit secrets, API keys, passwords
- Use environment variables for sensitive data
- Use secret management tools (e.g., Vault) in production
- Rotate credentials regularly

### Input Validation
- Validate all external input
- Sanitize data before use
- Use parameterized queries
- Avoid injection vulnerabilities

### Dependency Security
- **Before adding**: verify no known CVEs using NVD, OSV, or GitHub Advisory Database
- **When vulnerabilities are disclosed**: update immediately, do not wait for a scheduled review
- Integrate dependency scanning in CI (e.g., OWASP Dependency-Check, Dependabot, Snyk) — fail the build on critical/high CVEs
- Monitor security advisories for all production dependencies

## Performance Guidelines

### Optimization Priorities
1. Correctness first
2. Readability second
3. Performance third
4. Premature optimization is the root of all evil

### When to Optimize
- Profile before optimizing
- Focus on bottlenecks
- Measure improvements
- Document trade-offs

### Best Practices
- Use appropriate data structures
- Minimize I/O operations
- Cache expensive computations
- Use parallel processing where appropriate
- Close resources properly

## Accessibility and Usability

### CLI Output
- Clear, concise messages
- Consistent formatting
- Progress indicators for long operations
- Helpful error messages with suggested actions
- Color coding (with fallback for non-color terminals)

### Configuration
- Sensible defaults
- Clear configuration options
- Validation with helpful error messages
- Example configurations provided

## Maintenance

### Code Reviews
- All code must be reviewed before merging
- Address all review comments or discuss
- Reviewer should verify tests pass locally
- Approve only when all concerns resolved

### Technical Debt
- Document technical debt with TODO/FIXME comments
- Include ticket reference if applicable
- Schedule time to address technical debt
- Don't accumulate excessive debt

### Refactoring

**CRITICAL RULE: Always Follow TDD Before Refactoring**

Before refactoring ANY code, you MUST ensure comprehensive unit test coverage exists. This is a non-negotiable requirement. Coverage thresholds are measured from unit tests only.

#### Why TDD Before Refactoring?

Refactoring without tests is like surgery without anesthesia - dangerous and likely to cause pain. Tests are your safety net that proves refactoring didn't break functionality.

**Without tests:**
- ❌ No confidence that refactoring preserves behavior
- ❌ Bugs introduced silently without detection
- ❌ Fear of making changes leads to code rot
- ❌ Regression issues discovered in production

**With tests (TDD approach):**
- ✅ Immediate feedback if refactoring breaks functionality
- ✅ Confidence to make bold improvements
- ✅ Documentation of expected behavior
- ✅ Regression prevention

#### Mandatory TDD Micro-Commit Workflow

**The Micro-Commit Principle:**
Every commit must be **production-ready** (tests pass + builds + lint clean). Make small, frequent commits following the RED-GREEN-REFACTOR cycle.

**Step 1: STOP - Check Test Coverage**

Before touching ANY code, verify unit test coverage:

```bash
# Run unit tests to establish baseline, e.g. one of:
# ./gradlew test
# npm test
# pytest
# go test ./...
# dotnet test

# Check coverage report (unit tests only), e.g. one of:
# ./gradlew test jacocoTestReport
# npm run test:coverage
# pytest --cov
# go test -cover ./...

# For critical paths, consider mutation testing (e.g., pitest, stryker)
```

**Requirements (unit tests only -- integration/E2E tests do not count toward these thresholds):**
- **Minimum 80% line coverage** for code being refactored (unit tests only)
- **100% coverage for critical business logic** (scoring, analysis, report generation) (unit tests only)
- **All existing tests must pass** before starting

**Step 2: RED - Write Failing Test (DON'T COMMIT YET)**

Write a test that documents the behavior you need:

```kotlin
@Test
fun `should calculate correct score for class with violations`() {
    // Given - Setup test data
    val classInfo = createTestClass()
    val violations = listOf(
        createCheckstyleViolation(severity = "error"),
        createPmdViolation(priority = 1)
    )

    // When - Execute code under test
    val score = scorer.calculateScore(classInfo, violations)

    // Then - Assert expected behavior
    assertEquals(85.0, score, 0.01)
}
```

Run tests - they should **FAIL** (RED phase):
```bash
# Run your project's test suite - test fails, this is expected!
```

**Step 3: GREEN - Write Minimum Code to Pass → COMMIT**

Write the **minimum production code** to make the test pass:

```kotlin
fun calculateScore(classInfo: ClassInfo, violations: List<Violation>): Double {
    // Simplest implementation that makes test pass
    var score = 100.0
    violations.forEach { violation ->
        if (violation.severity == "error") score -= 5.0
    }
    return score
}
```

Run tests - they should **PASS**:
```bash
# Run your project's test suite and build, e.g. one of:
# ./gradlew test && ./gradlew build
# npm test && npm run build
# pytest && python -m build
# go test ./... && go build ./...
# All quality gates pass ✅
```

**Commit immediately (production-ready):**
```bash
git add src/test/ src/main/
git commit -m "feat: add basic score calculation for violations

- Calculate score starting at 100
- Deduct 5 points per error violation
- Test passes, build succeeds"
```

**Step 4: REFACTOR - Improve Code → COMMIT**

Look at the code. Can you improve it? Make logical improvements:

```kotlin
// Refactored: Extract magic numbers, improve readability
fun calculateScore(classInfo: ClassInfo, violations: List<Violation>): Double {
    val baseScore = 100.0
    val errorPenalty = 5.0

    val totalDeductions = violations
        .filter { it.severity == "error" }
        .size * errorPenalty

    return baseScore - totalDeductions
}
```

Run tests - they should **STILL PASS**:
```bash
# Run your project's test suite and build - all quality gates pass ✅
```

**Commit immediately (production-ready):**
```bash
git add src/main/
git commit -m "refactor: extract scoring constants and improve readability

- Extract baseScore and errorPenalty constants
- Use functional filter/size for clarity
- All tests still pass"
```

**Step 5: REPEAT - Add Next Feature**

Need to support more violation types? Start at Step 2 (RED) again:
- Write failing test for new behavior
- Make it pass with minimum code → COMMIT
- Refactor if needed → COMMIT

**Key Principles:**
1. **Never commit failing tests** - only commit when GREEN
2. **Every commit is production-ready** - tests pass, builds succeed, lint clean
3. **Commit frequently** - after each GREEN and REFACTOR phase
4. **Small commits** - one logical change per commit
5. **Run quality gates before every commit** - run your test suite and build

#### Real-World Example: Scorer Refactoring (Commit 5a07ef6)

This is how we successfully refactored Scorer using micro-commits:

**Cycle 1: Add Strategy Interface**
```bash
# RED - Write test for ScoringStrategy interface (don't commit)
@Test fun `should calculate score using strategy`() { ... }
# Run tests  # FAILS ✗

# GREEN - Create interface and make test pass
interface ScoringStrategy { fun calculateScore(...): Double }
# Run tests + build  # PASSES ✓
git commit -m "feat: add ScoringStrategy interface with test"

# REFACTOR - Improve interface documentation
// Add KDoc comments
# Run tests + build  # PASSES ✓
git commit -m "refactor: add documentation to ScoringStrategy interface"
```

**Cycle 2: Extract First Strategy**
```bash
# RED - Write test for CheckstyleScoringStrategy (don't commit)
@Test fun `should calculate Checkstyle score`() { ... }
# Run tests  # FAILS ✗

# GREEN - Create strategy class with minimum code
class CheckstyleScoringStrategy : ScoringStrategy { ... }
# Run tests + build  # PASSES ✓
git commit -m "feat: add CheckstyleScoringStrategy"

# REFACTOR - Extract helper method
private fun calculateDeduction(...) { ... }
# Run tests + build  # PASSES ✓
git commit -m "refactor: extract deduction calculation helper"
```

**Cycle 3-5: Extract Remaining Strategies**
```bash
# Repeat RED-GREEN-REFACTOR for each strategy
git commit -m "feat: add PmdScoringStrategy"
git commit -m "feat: add SonarScoringStrategy"
# ... etc
```

**Result (8 production-ready commits):**
- ✅ Fixed 2 CRITICAL violations (OCP + God Class)
- ✅ 47% code reduction (347 → 185 lines)
- ✅ 100% test pass rate maintained across ALL commits
- ✅ Zero regression bugs
- ✅ Every commit was production-ready and deployable

#### Common Refactoring Scenarios with Micro-Commits

**Scenario 1: Extracting a Method**

```kotlin
// Cycle 1: RED → GREEN → COMMIT
@Test
fun `should validate email format correctly`() {
    val result = userService.createUser(UserData(email = "invalid"))
    assertFalse(result.isValid)
}
// Write minimum code to pass, then:
git commit -m "feat: add email validation in createUser"

// Cycle 2: REFACTOR → COMMIT
class UserService {
    private fun isValidEmail(email: String): Boolean {
        return email.contains("@")  // Extracted method
    }
}
git commit -m "refactor: extract isValidEmail method"
```

**Scenario 2: Extracting a Class**

```kotlin
// Cycle 1: RED → GREEN → COMMIT
@Test
fun `should validate user data correctly`() {
    val validator = UserValidator()
    val result = validator.validate(invalidUserData)
    assertFalse(result.isValid)
}
// Create UserValidator class with minimum implementation
git commit -m "feat: add UserValidator class"

// Cycle 2: REFACTOR → COMMIT
// Move validation logic from UserService to UserValidator
git commit -m "refactor: move validation logic to UserValidator"

// Cycle 3: REFACTOR → COMMIT
// Clean up UserService to use new validator
git commit -m "refactor: update UserService to use UserValidator"
```

**Scenario 3: Applying Strategy Pattern**

```kotlin
// Cycle 1: Create interface
@Test
fun `should use scoring strategy`() { ... }
git commit -m "feat: add ScoringStrategy interface"

// Cycle 2-4: Extract each strategy (one at a time)
@Test
fun `should calculate Checkstyle score`() { ... }
git commit -m "feat: add CheckstyleScoringStrategy"

@Test
fun `should calculate PMD score`() { ... }
git commit -m "feat: add PmdScoringStrategy"

// Each strategy gets its own RED-GREEN-REFACTOR cycle
```

#### Exceptions (When You Can Skip TDD)

**NEVER skip TDD for:**
- ❌ Business logic changes
- ❌ Algorithm modifications
- ❌ Complex refactorings (Strategy Pattern, Extract Class)
- ❌ Critical paths (scoring, analysis, report generation)

**ONLY skip TDD for:**
- ✅ Simple renaming (variable, method, class names)
- ✅ Moving files between packages (IDE refactor)
- ✅ Formatting changes (whitespace, line breaks)
- ✅ Comment updates
- ✅ Import organization

**Even for simple changes, run tests after:**
```bash
# Run your project's test suite to verify nothing broke
```

#### Red Flags: Refactoring Without Tests

**WARNING SIGNS:**
- 🚨 "I'll add tests later" - NO! Tests first, always.
- 🚨 "The code is simple, I don't need tests" - Famous last words before production bugs
- 🚨 "I'm just moving code around" - Even simple moves can break dependencies
- 🚨 "Tests take too long to write" - Tests take less time than debugging production issues

**CONSEQUENCES:**
- Production bugs from "safe" refactorings
- Fear of improving code (leads to technical debt)
- Long debugging sessions to find regressions
- Loss of team confidence in codebase

#### Enforcement

**Code Review Requirements:**
- Pull requests MUST show micro-commits following RED-GREEN-REFACTOR cycle
- Every commit MUST be production-ready (tests pass + builds + lint clean)
- Reviewers MUST verify each commit is independently deployable
- CI/CD MUST enforce quality gates on EVERY commit
- Failing tests MUST block all commits

**Acceptable PR Pattern (Micro-Commits):**
```
Commit 1: feat: add email validation (RED → GREEN)
  - Test passes ✓
  - Build succeeds ✓
  - Production-ready ✓

Commit 2: refactor: extract email validation to helper method
  - Test still passes ✓
  - Build succeeds ✓
  - Production-ready ✓

Commit 3: feat: add password validation (RED → GREEN)
  - Test passes ✓
  - Build succeeds ✓
  - Production-ready ✓
```

**Unacceptable PR Pattern (Batch Commits):**
```
Commit 1: refactor: major changes to Feature X (tests failing ✗)
Commit 2: fix tests (tests passing now ✓)
Commit 3: fix lint errors (finally production-ready ✓)
```

**Why This Matters:**
- Each commit is a safe rollback point
- Easy to bisect and find bugs
- Continuous deployability maintained
- Clear intent in each commit

#### Summary: The TDD Micro-Commit Mantra

**Remember this workflow:**
1. **STOP** - Check existing unit test coverage (80% minimum required, unit tests only)
2. **RED** - Write failing test (don't commit yet)
3. **GREEN** - Write minimum code to pass → **COMMIT** (production-ready)
4. **REFACTOR** - Improve code structure → **COMMIT** (production-ready)
5. **REPEAT** - Start at step 2 for next feature

**Make it a habit:**
- 🟥 RED (failing test, no commit) → 🟢 GREEN (passing test) → ✅ **COMMIT** → 🔄 REFACTOR → ✅ **COMMIT**

**Critical Rules:**
- **Never commit failing tests** - only commit when GREEN
- **Every commit is production-ready** - tests pass, builds succeed, lint clean
- **Commit after GREEN phase** - don't batch multiple features
- **Commit after REFACTOR phase** - don't batch multiple refactorings
- **Small, frequent commits** - one logical change per commit

**Production-Ready Definition:**
```bash
# ✓ All tests pass (e.g., ./gradlew test, npm test, pytest, or go test ./...)
# ✓ Build succeeds (e.g., ./gradlew build, npm run build, or go build ./...)
# ✓ No lint errors
# ✓ Ready to deploy to production
```

**Never commit broken code. Every commit must be deployable. Period.**

---

### Legacy Refactoring Principles

- Refactor incrementally
- Keep refactoring separate from feature work
- Ensure tests pass after refactoring
- Document significant refactoring decisions

## Questions or Clarifications?

If anything in these standards is unclear or needs discussion, please:
1. Open an issue for discussion
2. Propose changes via pull request
3. Document decisions and update this file

---

**Last Updated**: February 16, 2026
**Version**: 1.1

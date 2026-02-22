# Pre-Commit Code Quality Checklist

**IMPORTANT**: Review this checklist before every commit. Every commit MUST be production-ready.

**CRITICAL**: Follow the TDD Micro-Commit workflow (see below).

---

## TDD Micro-Commit Checklist (MANDATORY)

**For ALL code changes, follow the STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT cycle.**
See [AI_AGENT_WORKFLOW.md](./AI_AGENT_WORKFLOW.md) for the full workflow.

### Checklist

- [ ] **Coverage verified**: Minimum 80% unit test coverage for code being changed, 100% for critical paths (unit tests only -- integration/E2E tests do not count toward coverage)
- [ ] **Tests written**: New/updated tests follow Given-When-Then structure with edge cases
- [ ] **Tests pass**: Run your project's unit test suite - all tests **PASS**
- [ ] **Build succeeds**: Run your project's build - **SUCCEEDS**
- [ ] **No lint errors**
- [ ] **Static analysis passes**: No PMD, detekt, or Checkstyle violations (see [STATIC_ANALYSIS_STANDARDS.md](./STATIC_ANALYSIS_STANDARDS.md))
- [ ] **Commit is focused**: One logical change per commit
- [ ] **Commit message**: Follows conventional commits format
- [ ] **Production-ready**: Code is deployable to production

### Red Flags - DO NOT COMMIT IF:

- Any tests are failing
- Build fails
- Lint errors present
- You're thinking "I'll fix this in the next commit"
- You're batching multiple features into one commit

---

## 🔧 Refactoring Prerequisites (MANDATORY)

**CRITICAL: Never refactor without tests. No exceptions.**

Before refactoring ANY code, you MUST complete ALL of the following:

- [ ] **Check unit test coverage**: Run your project's coverage tool (e.g., `./gradlew test jacocoTestReport`, `npm run test:coverage`, `pytest --cov`, `go test -cover ./...`)
- [ ] **Minimum 80% unit test line coverage** for the code being refactored (unit tests only -- integration/E2E tests do not count)
- [ ] **100% unit test coverage for critical paths** (business logic, scoring, analysis, report generation)
- [ ] **All existing tests pass** before starting any refactoring
- [ ] **Tests are meaningful**: Not just for coverage numbers -- tests verify actual behavior

### If Unit Test Coverage Is Below 80%

**STOP. Do NOT refactor.** Instead:

1. Write unit tests FIRST to reach 80% coverage (separate commits using TDD cycle)
2. Verify all new tests pass
3. Commit the tests: `test(<scope>): add tests for <component> before refactoring`
4. THEN proceed with refactoring

### After Each Refactoring Step

- [ ] Run ALL tests (not just the ones you think are affected)
- [ ] Verify build succeeds
- [ ] Verify no lint errors
- [ ] Commit immediately: `refactor(<scope>): <what was improved>`

### Refactoring Red Flags

- "I'll add tests later" -- NO. Tests FIRST, always.
- "The code is simple, I don't need tests" -- Tests are required regardless of perceived simplicity.
- "I'm just moving code around" -- Even simple moves can break dependencies. Tests required.
- Batching multiple refactoring steps into one commit -- each step is its own commit.

For the full refactoring workflow, see `./AI_AGENT_WORKFLOW.md`.

---

## 📋 Quick Pre-Commit Checklist

Before running `git commit`, verify:

- [ ] **Production-ready: All unit tests pass** (run your project's unit test suite)
- [ ] **Production-ready: Code compiles** (run your project's build)
- [ ] **Production-ready: No lint errors**
- [ ] **Production-ready: Static analysis passes** (PMD/detekt/Checkstyle -- see [STATIC_ANALYSIS_STANDARDS.md](./STATIC_ANALYSIS_STANDARDS.md))
- [ ] **Followed TDD micro-commit workflow** (RED → GREEN → COMMIT or REFACTOR → COMMIT)
- [ ] **No SOLID violations** (see detailed checklist below)
- [ ] **No design pattern anti-patterns** (see detailed checklist below)
- [ ] **Methods ≤ language-specific limit** (see language-specific standards; typically 15-20 lines, excluding data classes, comments, blank lines)
- [ ] **Classes ≤ 300 lines** (if larger, consider refactoring)
- [ ] **No duplicated code** (DRY principle)
- [ ] **Proper KDoc comments** on public APIs
- [ ] **Meaningful commit message** following conventional commits format

## 📋 Quick Pre-Push Checklist

Before running `git push`, verify:

- [ ] **All unit tests pass** (should already pass from pre-commit)
- [ ] **All integration tests pass** (run your project's integration test suite)
- [ ] **No failures introduced** — if integration tests fail, fix locally before pushing
- [ ] **CI is the hard gate** (unit + integration + E2E failures on CI must be fixed before merge)

---

## 🔍 SOLID Principles Detailed Checklist

For the full SOLID guide with multi-language examples and real-world analogies, see [SOLID_PRINCIPLES.md](./SOLID_PRINCIPLES.md).

### ✅ Single Responsibility Principle (SRP)

**Question**: Does each class/method have ONE reason to change?

**Check for violations:**
- [ ] Class name contains "Manager", "Handler", "Utility", "Helper" (often God classes)
- [ ] Class has > 10 methods (likely doing too much)
- [ ] Method does multiple unrelated things (e.g., validates AND saves AND sends email)
- [ ] Class mixes business logic with infrastructure (e.g., database access)
- [ ] Method name contains "And" (e.g., `validateAndSave()`)

**Red flags:**
- Class > 300 lines
- Method > language-specific limit (see language-specific standards; typically 15-20 lines)
- Class imports from > 5 different packages
- Methods that call methods from > 3 other classes (Feature Envy)

**Fix examples:**
```kotlin
// ❌ BAD - Multiple responsibilities
class UserManager {
    fun createUser(data: UserData) {
        validateUser(data)           // validation
        val user = User(data)        // domain logic
        database.save(user)          // persistence
        emailService.sendWelcome(user) // notification
        logger.log("User created")   // logging
    }
}

// ✅ GOOD - Single responsibility
class UserCreator {
    fun create(data: UserData): User {
        return User(data)
    }
}
class UserValidator { fun validate(data: UserData) }
class UserRepository { fun save(user: User) }
class WelcomeEmailSender { fun send(user: User) }
```

---

### ✅ Open/Closed Principle (OCP)

**Question**: Can I add new functionality WITHOUT modifying existing code?

**Check for violations:**
- [ ] Switch/when statements on type checks or enums
- [ ] If-else chains checking object types
- [ ] Hard-coded class instantiation (e.g., `val writer = MarkdownWriter()`)
- [ ] Adding new feature requires changing multiple existing classes
- [ ] Method contains list of concrete implementations

**Red flags:**
```kotlin
// ❌ BAD - Must modify to add new report type
fun generateReport(type: String) {
    when (type) {
        "markdown" -> MarkdownWriter().write()
        "json" -> JsonWriter().write()
        "html" -> HtmlWriter().write()
        // Adding PDF requires modifying this method
    }
}
```

**Fix with Strategy/Polymorphism:**
```kotlin
// ✅ GOOD - Can add new report types without modification
interface ReportWriter {
    fun write(data: Data)
}

class ReportGenerator(private val writers: List<ReportWriter>) {
    fun generateAll(data: Data) {
        writers.forEach { it.write(data) }
        // Adding PDF just requires creating PdfWriter, no changes here
    }
}
```

---

### ✅ Liskov Substitution Principle (LSP)

**Question**: Can I substitute any subclass for its parent without breaking functionality?

**Check for violations:**
- [ ] Subclass throws exceptions parent doesn't throw
- [ ] Subclass has stricter preconditions than parent
- [ ] Subclass has weaker postconditions than parent
- [ ] Subclass removes/doesn't implement parent functionality
- [ ] Type checking before casting (`is` checks)

**Red flags:**
```kotlin
// ❌ BAD - Violates LSP
open class Bird {
    open fun fly() { /* fly */ }
}
class Penguin : Bird() {
    override fun fly() {
        throw UnsupportedOperationException("Penguins can't fly!")
    }
}

// ✅ GOOD - Proper abstraction
interface Bird
interface FlyingBird : Bird {
    fun fly()
}
class Sparrow : FlyingBird
class Penguin : Bird
```

---

### ✅ Interface Segregation Principle (ISP)

**Question**: Are interfaces focused and cohesive, or fat and bloated?

**Check for violations:**
- [ ] Interface has > 5 methods
- [ ] Classes implement interface but throw "not implemented" for some methods
- [ ] Classes implement interface but leave some methods empty
- [ ] Clients depend on interfaces they don't use

**Red flags:**
```kotlin
// ❌ BAD - Fat interface
interface Worker {
    fun work()
    fun eat()
    fun sleep()
    fun getPaid()
    fun takeVacation()
    fun attendMeeting()
}

// ✅ GOOD - Segregated interfaces
interface Workable { fun work() }
interface Eatable { fun eat() }
interface Payable { fun getPaid() }
```

---

### ✅ Dependency Inversion Principle (DIP)

**Question**: Do high-level modules depend on abstractions, not concrete implementations?

**Check for violations:**
- [ ] Direct instantiation of dependencies inside classes (`val parser = CheckstyleParser()`)
- [ ] Importing concrete classes instead of interfaces
- [ ] No constructor injection
- [ ] Using `= ClassName()` in property declarations
- [ ] Cannot mock dependencies for testing

**Red flags:**
```kotlin
// ❌ BAD - Depends on concrete class
class Analyzer {
    private val parser = CheckstyleParser()  // Hard-coded dependency
    private val database = MySQLDatabase()   // Hard-coded dependency

    fun analyze() {
        val data = parser.parse()
        database.save(data)
    }
}

// ✅ GOOD - Depends on abstractions with injection
class Analyzer(
    private val parser: ViolationParser,     // Interface, injected
    private val database: Database           // Interface, injected
) {
    fun analyze() {
        val data = parser.parse()
        database.save(data)
    }
}
```

---

## 🎨 Design Patterns Checklist

### ✅ Use Appropriate Patterns

**Before committing, verify you're using patterns correctly:**

- [ ] **Strategy Pattern** - Used when you have multiple algorithms/implementations?
- [ ] **Factory Pattern** - Used when object creation is complex?
- [ ] **Template Method** - Used when algorithms share common structure?
- [ ] **Decorator Pattern** - Used when adding responsibilities dynamically?
- [ ] **Observer Pattern** - Used when one-to-many dependencies?

For the full catalog and usage guidance, see `./DESIGN_PATTERNS.md`.

### ❌ Avoid Anti-Patterns

**Check your code doesn't contain:**

#### **God Class / God Method**
- [ ] No class > 300 lines
- [ ] No method > language-specific limit (see language-specific standards; typically 15-20 lines)
- [ ] No class with > 10 methods
- [ ] No class doing > 3 different things

#### **Feature Envy**
- [ ] Methods primarily use data from OTHER classes
- [ ] Excessive getter calls on collaborator objects

#### **Primitive Obsession**
- [ ] Using primitives (String, Int, Double) instead of domain objects
- [ ] Example: Using `String userId` instead of `UserId` value class

#### **Long Parameter List**
- [ ] No method with > 5 parameters
- [ ] Use parameter objects/data classes instead

#### **Tight Coupling**
- [ ] Classes don't directly instantiate their dependencies
- [ ] Using interfaces, not concrete classes
- [ ] Can easily swap implementations

#### **Duplicated Code**
- [ ] No copy-pasted code blocks
- [ ] Common logic extracted to shared methods/classes
- [ ] Follow DRY (Don't Repeat Yourself)

---

## 📏 Code Metrics Checklist

Run these checks before committing:

### **Method Complexity**
```bash
# Count lines in methods (should be ≤ 15)
grep -A 20 "fun " YourFile.kt | grep -E "^\s*(fun |$)" | less
```

### **Class Size**
```bash
# Count lines per class (should be ≤ 300)
wc -l src/main/kotlin/**/*.kt
```

### **Cyclomatic Complexity**
- [ ] No method with > 3 levels of nesting
- [ ] No method with > 5 decision points (if/when/for/while)

### **Dependency Count**
- [ ] No class importing from > 10 packages
- [ ] No class depending on > 5 other classes

---

## 🧪 Testing Requirements

Before committing, ensure:

- [ ] **All tests pass**: run your project's test suite
- [ ] **New code has tests**: Minimum 80% unit test coverage for new classes (unit tests only)
- [ ] **No tests ignored**: No `@Disabled` or `.skip()` annotations
- [ ] **Tests are fast**: Unit tests run in < 1 second each
- [ ] **Tests are isolated**: No shared state between tests
- [ ] **Tests are clear**: Test names describe what's being tested

---

## 📝 Documentation Requirements

- [ ] **Public APIs documented**: All public classes/methods have KDoc
- [ ] **Complex logic explained**: Non-obvious code has inline comments
- [ ] **README updated**: If adding new features
- [ ] **Architecture docs updated**: If changing design patterns

---

## 🔒 Secrets & Credentials Check

**Scan staged files for leaked secrets before every commit.**

### Checklist

- [ ] **No hardcoded secrets**: No API keys, passwords, tokens, or private keys in source code
- [ ] **No credential files staged**: No `.env`, `credentials.json`, `*.pem`, `*.key` files
- [ ] **No connection strings**: No database URLs with embedded passwords
- [ ] **Environment variables used**: Sensitive values loaded from environment or secret manager

### Automated Scanning (Recommended)

Use a secrets scanner on staged files before committing:

```bash
# Option 1: gitleaks (recommended)
gitleaks protect --staged

# Option 2: detect-secrets
detect-secrets scan --list-all-secrets

# Option 3: git-secrets (AWS-focused)
git secrets --scan
```

### Common Patterns to Watch For

```
# These should NEVER appear in committed code:
AKIA...          # AWS access key
ghp_...          # GitHub personal access token
sk-...           # OpenAI/Stripe secret key
-----BEGIN RSA PRIVATE KEY-----
password = "..."
api_key = "..."
jdbc:postgresql://user:pass@host/db
```

### Pre-Commit Hook (Optional)

```bash
# Add to .git/hooks/pre-commit
gitleaks protect --staged --verbose || {
    echo "Secrets detected in staged files. Commit blocked."
    exit 1
}
```

---

## 🔀 Breaking API Changes Check

**Verify backward compatibility before committing changes to public APIs.**

### Checklist

- [ ] **Public method signatures unchanged**: No removed or renamed public methods without deprecation
- [ ] **Return types preserved**: No changes to return types of public methods
- [ ] **Parameter contracts maintained**: No added required parameters to existing public methods
- [ ] **Interface contracts stable**: No removed methods from public interfaces
- [ ] **Error behavior consistent**: No new exceptions thrown from existing methods without documentation
- [ ] **Deprecation used**: Breaking changes follow deprecate-then-remove strategy

### When Breaking Changes Are Necessary

If a breaking change is unavoidable:
1. **STOP and ask the user** before committing
2. Add `@Deprecated` annotation with migration guidance
3. Document the breaking change in the commit message footer: `BREAKING CHANGE: <description>`
4. Update all internal callers in the same commit or preceding commits
5. Consider providing a compatibility shim

### Red Flags

- Removing or renaming a public class, method, or field
- Changing a method's return type
- Adding required parameters to a public method
- Narrowing an input type or widening an output type (LSP violation)
- Changing default behavior of existing functionality

---

## ⚠️ Common Violations & Quick Fixes

### **Violation: Hard-coded Dependencies**
```kotlin
// ❌ BEFORE
class Orchestrator {
    private val parser = CheckstyleParser()
}

// ✅ AFTER
class Orchestrator(
    private val parser: ViolationParser = CheckstyleParser()
)
```

### **Violation: Switch on Type**
```kotlin
// ❌ BEFORE
fun process(violation: Violation): Double {
    return when (violation) {
        is CheckstyleViolation -> 2.0
        is PmdViolation -> 3.0
        is SonarViolation -> 5.0
    }
}

// ✅ AFTER
interface ScoredViolation {
    fun getPenalty(): Double
}
// Each violation type implements getPenalty()
```

### **Violation: God Class**
```kotlin
// ❌ BEFORE
class CodeHealthOrchestrator {
    fun analyze() { }
    fun parseReports() { }
    fun calculateScores() { }
    fun generateReports() { }
    fun findFiles() { }
    fun detectPackages() { }
    // ... 10 more methods
}

// ✅ AFTER
class CodeHealthOrchestrator(
    private val reportParser: ReportParser,
    private val scorer: Scorer,
    private val reportGenerator: ReportGenerator,
    private val fileFinder: FileFinder,
    private val packageDetector: PackageDetector
)
```

---

## 🚀 Automated Checks

### **Run Before Every Commit**
```bash
# 1. Run unit tests (use your project's test runner)
# e.g. one of: ./gradlew test, npm test, pytest, go test ./..., dotnet test

# 2. Check compilation / build
# e.g. one of: ./gradlew build, npm run build, go build ./..., dotnet build

# 3. Check for long methods (manual review - adapt paths to your project)
# find src/ -name "*.kt" -exec grep -n "fun " {} + | less
# grep -rn "function " src/ --include="*.ts" | less

# 4. Check for God classes (> 300 lines - adapt paths to your project)
# find src/ -name "*.kt" -exec wc -l {} + | awk '$1 > 300'
# find src/ -name "*.ts" -exec wc -l {} + | awk '$1 > 300'

# 5. Check imports (too many = high coupling)
# grep "^import" src/**/*.kt | sort | uniq -c | sort -rn | head -20
```

### **Run Before Every Push**

Before pushing commits to the remote, run integration tests in addition to unit tests. This catches cross-component issues before they reach the team.

```bash
# 1. Run unit tests (should already pass from pre-commit)
# e.g. one of: ./gradlew test, npm test, pytest, go test ./...

# 2. Run integration tests
# e.g. one of: ./gradlew integrationTest, npm run test:integration
# or one of: pytest tests/integration/, go test -tags=integration ./...

# If ANY test fails, fix locally before pushing.
```

### **Pre-Commit Hook** (Optional but Recommended)
```bash
# .git/hooks/pre-commit
#!/bin/bash
echo "Running pre-commit checks..."

# Run unit tests (replace with your project's test command)
# ./gradlew test || exit 1
# npm test || exit 1
# pytest || exit 1

# Check for long methods (adapt to your language/project structure)
# LONG_METHODS=$(find src/ -name "*.kt" | xargs grep -A 20 "fun " | grep -c "^--$")
# if [ $LONG_METHODS -gt 50 ]; then
#     echo "⚠️  Warning: Many potentially long methods detected"
# fi

echo "✅ Pre-commit checks passed"
```

### **Pre-Push Hook** (Optional but Recommended)
```bash
# .git/hooks/pre-push
#!/bin/bash
echo "Running pre-push checks..."

# Run unit tests (should already pass from pre-commit)
# ./gradlew test || exit 1
# npm test || exit 1
# pytest || exit 1

# Run integration tests
# ./gradlew integrationTest || exit 1
# npm run test:integration || exit 1
# pytest tests/integration/ || exit 1

echo "✅ Pre-push checks passed"
```

---

## 📚 Resources

- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID
- **Design Patterns**: Gang of Four patterns
- **Clean Code**: Robert C. Martin
- **Refactoring**: Martin Fowler
- **Kotlin Best Practices**: https://kotlinlang.org/docs/coding-conventions.html

---

## 🎯 Red Light / Green Light

### 🔴 **RED LIGHT - DO NOT COMMIT IF:**
- Tests are failing
- Code doesn't compile
- Method > language-specific limit (see language-specific standards; typically 15-20 lines)
- Class > 300 lines with multiple responsibilities
- Direct dependency instantiation in production classes (except composition roots/factories)
- Copy-pasted code
- Switch/when on types (OCP violation)
- Missing tests for new functionality

### 🟢 **GREEN LIGHT - OK TO COMMIT IF:**
- All tests pass
- Code compiles
- All methods ≤ language-specific limit (see language-specific standards; typically 15-20 lines)
- Classes ≤ 300 lines OR have single responsibility
- Dependencies injected via constructor
- No duplicated code
- Follows SOLID principles
- Has appropriate tests
- Well-documented

---

## 💡 When In Doubt

**Ask yourself:**
1. Can I explain what this class does in ONE sentence?
2. Can I add new functionality WITHOUT modifying this class?
3. Can I test this class in isolation?
4. Would my teammates understand this code in 6 months?
5. Is this the simplest solution that works?

If you answered **NO** to any question, consider refactoring before committing.

---

**Remember**: It's easier to write clean code initially than to refactor later. Take the extra 10 minutes to follow these principles—your future self (and teammates) will thank you!

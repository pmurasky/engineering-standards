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
- [ ] **One test at a time**: In TDD, write exactly one failing test, make it pass, refactor, then add the next test
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

**CRITICAL: Never refactor without tests. No exceptions.** See `docs/AI_AGENT_WORKFLOW.md` for the full refactoring workflow.

- [ ] **Check unit test coverage**: ≥80% for code being refactored, 100% for critical paths (unit tests only)
- [ ] **All existing tests pass** before starting any refactoring
- [ ] **If coverage < 80%**: STOP — write unit tests first (`test(<scope>): add tests for <component> before refactoring`)
- [ ] **After each step**: Run ALL tests, verify build, verify no lint errors, commit immediately

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

- [ ] Class name doesn't contain "Manager", "Handler", "Utility", "Helper" (often God classes)
- [ ] Class has ≤ 10 methods
- [ ] Method does ONE thing (no `validateAndSave()` style names)
- [ ] Class doesn't mix business logic with infrastructure
- [ ] Class ≤ 300 lines, method ≤ language-specific limit (typically 15-20 lines)

---

### ✅ Open/Closed Principle (OCP)

- [ ] No switch/when statements on type checks or enums
- [ ] No if-else chains checking object types
- [ ] No hard-coded class instantiation (e.g., `val writer = MarkdownWriter()`)
- [ ] Adding new feature doesn't require modifying existing classes

---

### ✅ Liskov Substitution Principle (LSP)

- [ ] Subclass doesn't throw exceptions parent doesn't throw
- [ ] Subclass doesn't have stricter preconditions than parent
- [ ] Subclass doesn't remove/stub parent functionality
- [ ] No type checking before casting (`is` checks)

---

### ✅ Interface Segregation Principle (ISP)

- [ ] Interface has ≤ 5 methods
- [ ] No classes implementing interface with empty stubs or "not implemented" throws
- [ ] Clients don't depend on interface methods they don't use

---

### ✅ Dependency Inversion Principle (DIP)

- [ ] No direct instantiation of dependencies inside classes (`val x = ConcreteClass()`)
- [ ] No `= ClassName()` in property declarations (use constructor injection)
- [ ] Dependencies are mockable for testing

For violation examples and fixes, see [SOLID_PRINCIPLES.md](./SOLID_PRINCIPLES.md).

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
- [ ] **New behavior has tests**: Minimum 80% unit test coverage for behavior-bearing new code (unit tests only)
- [ ] **Boilerplate-only types are not over-tested**: Skip direct unit tests for trivial `@Entity`/DTO/data classes, generated code, and config-only wiring unless they contain domain behavior
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

## 🚀 Automated Checks

### **Run Before Every Commit**

Run your project's unit test suite and build (e.g., `./gradlew test`, `npm test`, `pytest`, `go test ./...`). See `docs/CODING_PRACTICES.md` for pre-commit hook examples.

### **Run Before Every Push**

Run unit tests + integration tests before pushing. See `docs/CODING_PRACTICES.md` for pre-push hook examples.

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

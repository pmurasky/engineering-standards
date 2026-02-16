# AI Agent Workflow - Micro-Commit & Refactoring Instructions

**PURPOSE**: This document provides explicit instructions for AI coding agents (like OpenCode, Cursor, Copilot, etc.) to follow the project's micro-commit philosophy and refactoring standards.

**CRITICAL**: AI agents MUST follow this workflow for ALL code changes. No exceptions.

---

## 🎯 Core Principle: Micro-Commits

**Every logical change = One commit**

A "logical change" is:
- One refactoring step (extract method, rename variable)
- One feature implementation
- One test update
- One documentation update

**NEVER bundle multiple logical changes into one commit.**

### Production-Ready Commits

**Every commit MUST be production-ready. No exceptions.**

Before committing, ALL of the following must be true:
- All tests pass
- Build succeeds
- No lint errors
- Code is deployable to production

A commit with failing tests is **never** acceptable. If your change breaks tests, fix the tests in the same commit before committing.

---

## 📋 Mandatory Workflow for AI Agents

### Before Making ANY Code Changes

**Step 1: Read and Acknowledge**
```
AI Agent: I will follow the micro-commit workflow documented in docs/AI_AGENT_WORKFLOW.md
```

**Step 2: Create Task List**
Use the TodoWrite tool to break down the work:
```
Example for "Add timestamp to report filenames":
1. Extract timestamp generation into separate method (refactor)
2. Add timestamp to filename in buildReportPath method (implementation)
3. Update tests to verify timestamp format (test)
4. Update documentation (docs)
```

**Step 3: Execute One Task at a Time**
Complete tasks sequentially, committing after each one.

---

## 🔄 The Micro-Commit Workflow (Step-by-Step)

### Pattern 1: Feature Implementation (with existing tests)

**Example**: Modify existing code that already has tests

```
Step 1: REFACTOR (if needed) → COMMIT
├─ Extract helper methods
├─ Rename variables for clarity
├─ Add imports
├─ Run tests (must pass)
└─ Commit: "refactor: extract helper method for X"

Step 2: RED - Write/update failing test (DON'T COMMIT)
├─ Update existing tests to reflect new expected behavior
├─ Run tests (should fail - RED phase)
└─ Don't commit yet

Step 3: GREEN - Implement feature → COMMIT
├─ Make the actual behavior change
├─ Run tests (must pass - all tests green)
└─ Commit: "feat: add feature X"
   (Include both implementation and test updates in one commit)

Step 4: REFACTOR → COMMIT
├─ Improve code quality
├─ Run tests (must still pass)
└─ Commit: "refactor: improve feature X implementation"

Step 5: DOCUMENT → COMMIT
├─ Update README.md
├─ Update relevant docs
└─ Commit: "docs: update documentation for feature X"
```

### Pattern 2: New Feature (TDD approach)

**Example**: Add completely new functionality

```
Step 1: TEST (Red) - DON'T COMMIT
├─ Write failing test
├─ Run tests (should fail)
└─ Don't commit yet

Step 2: IMPLEMENT (Green) → COMMIT
├─ Write minimum code to pass test
├─ Run tests (must pass)
└─ Commit: "feat: add feature X with test"
   (Include both test and implementation in one commit)

Step 3: REFACTOR → COMMIT
├─ Improve code quality
├─ Run tests (must still pass)
└─ Commit: "refactor: improve feature X implementation"

Step 4: DOCUMENT → COMMIT
├─ Update README.md
├─ Update relevant docs
└─ Commit: "docs: document feature X"
```

### Pattern 3: Refactoring Only

**Example**: Improve existing code without changing behavior

```
Step 1: REFACTOR PART 1 → COMMIT
├─ Extract one method
├─ Run tests (must pass)
└─ Commit: "refactor: extract method Y from class X"

Step 2: REFACTOR PART 2 → COMMIT
├─ Rename variables
├─ Run tests (must pass)
└─ Commit: "refactor: rename variables in class X for clarity"

Step 3: REFACTOR PART 3 → COMMIT
├─ Move code to better location
├─ Run tests (must pass)
└─ Commit: "refactor: move helper method to utility class"
```

---

## ✅ Commit Message Format

**Use Conventional Commits format:**

```
<type>(<scope>): <description>

[optional body explaining WHY, not WHAT]

[optional footer with test status, performance metrics, etc.]
```

### Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code refactoring (no behavior change)
- `test:` - Test updates
- `docs:` - Documentation only
- `perf:` - Performance improvement
- `chore:` - Build/tooling changes

### Examples:

**Good commits:**
```
refactor: extract timestamp generation into separate method

- Add generateTimestamp() method to encapsulate timestamp formatting logic
- Import java.time classes for future timestamp usage
- No behavior change, pure refactoring to prepare for timestamped filenames
```

```
feat: add timestamp to report filenames

- Modify buildReportPath to include timestamp in filename format
- Report files now named: reportName_YYYYMMDD_HHMMSS.extension
- Example: segment_20260213_133500.md
- Each report generation creates a new file instead of overwriting
- Enables historical tracking of code health reports
- Update test assertions to use regex patterns matching timestamp format
```

**Bad commits (DON'T DO THIS):**
```
fix stuff
update code
WIP
tmp
changes
fix tests and update feature and refactor
```

---

## 🚫 Common Mistakes to Avoid

### ❌ Mistake 1: Bundling Multiple Changes

**BAD:**
```
Commit 1: "feat: add timestamp to reports"
- Modified ReportGenerator
- Updated ReportGeneratorTest
- Updated README.md
- Added helper method
```

**GOOD:**
```
Commit 1: "refactor: extract timestamp generation method"
Commit 2: "feat: add timestamp to report filenames"
  (includes updated tests - all tests pass)
Commit 3: "docs: update documentation for timestamped reports"
```

### ❌ Mistake 2: Committing Failing Tests

**NEVER commit code where tests fail.** Every commit must be production-ready with all tests passing. If your implementation breaks existing tests, update the tests in the same commit.

### ❌ Mistake 3: Committing Without Running Tests

**ALWAYS run tests before committing:**
```bash
# Run your project's test suite, e.g.:
# ./gradlew test | npm test | pytest | go test ./... | dotnet test
```

### ❌ Mistake 4: Vague Commit Messages

**BAD**: "update code"
**GOOD**: "refactor: extract validation logic to separate class"

---

## 🔧 AI Agent Checklist (Before Each Commit)

**Mandatory checks before EVERY commit:**

- [ ] **Read the task** - Understand what ONE logical change I'm making
- [ ] **Update todo list** - Mark current task as "in_progress"
- [ ] **Make the change** - ONE logical change only
- [ ] **Run tests** - Execute your project's test suite
- [ ] **Verify tests pass** - All tests green, no exceptions
- [ ] **Write commit message** - Clear, descriptive, follows format
- [ ] **Commit** - One logical change committed
- [ ] **Update todo list** - Mark current task as "completed"
- [ ] **Move to next task** - Start next micro-commit cycle

---

## 📝 AI Agent Self-Verification Questions

**Before committing, ask yourself:**

1. ✅ **Is this ONE logical change?**
   - Implementation + its tests = one logical change (commit together)
   - Implementation + docs + unrelated refactoring = split it

2. ✅ **Do all tests pass?**
   - If not, fix them in THIS commit before committing

3. ✅ **Can I describe this commit in one sentence?**
   - If not, it's probably too big

4. ✅ **Is this commit production-ready?**
   - Tests pass, build succeeds, no lint errors, deployable to production
   - If not, fix the issues before committing

5. ✅ **Is my commit message clear?**
   - Someone reading git log should understand what changed and why

---

## 🎯 Real Example: Timestamped Report Filenames

**User Request**: "Update reports to create files with timestamp at end of filename"

### AI Agent Response (GOOD):

**Step 1: Create Task List**
```markdown
I'll break this down into micro-commits:
1. Refactor: Extract timestamp generation into separate method
2. Feature: Add timestamp to filename in buildReportPath (with test updates)
3. Docs: Update documentation for new filename format
```

**Step 2: Execute Task 1 → COMMIT**
```bash
# Make refactoring change
# Run tests (pass)
git commit -m "refactor: extract timestamp generation into separate method"
```

**Step 3: Execute Task 2 → COMMIT**
```bash
# Write/update tests for new behavior (RED - tests fail)
# Implement feature (GREEN - tests pass)
# Run tests (all pass)
git commit -m "feat: add timestamp to report filenames"
```

**Step 4: Execute Task 3 → COMMIT**
```bash
# Update docs
git commit -m "docs: update documentation for timestamped report filenames"
```

**Result**: 3 clear, focused, production-ready commits with clean history

---

### AI Agent Response (BAD - Don't do this):

**Step 1: Make all changes at once**
```bash
# Changed ReportGenerator
# Changed ReportGeneratorTest  
# Changed README.md
# Changed config files
```

**Step 2: One big commit**
```bash
git commit -m "add timestamps to reports"
```

**Result**: One unclear commit, hard to review, hard to revert

---

## 🔄 Workflow Integration with Tools

### Using TodoWrite Tool

**ALWAYS use TodoWrite to track micro-commits:**

```kotlin
// At start of feature
todowrite([
  {id: "1", content: "Refactor: extract helper method", status: "pending"},
  {id: "2", content: "Feature: implement core logic", status: "pending"},
  {id: "3", content: "Test: update test assertions", status: "pending"},
  {id: "4", content: "Docs: update README", status: "pending"}
])

// Before starting each task
todowrite([
  {id: "1", content: "Refactor: extract helper method", status: "in_progress"},
  ...
])

// After committing each task
todowrite([
  {id: "1", content: "Refactor: extract helper method", status: "completed"},
  ...
])
```

### Using Bash Tool for Tests

**ALWAYS run tests before committing:**

```bash
# Run your project's test suite (optionally filter to relevant tests), e.g.:
# ./gradlew test --tests "RelevantTestClass"
# npm test -- --grep "RelevantTest"
# pytest tests/test_relevant.py
# go test ./path/to/package
# dotnet test --filter "RelevantTestClass"

# Check test output
   # If all pass → proceed to commit
   # If any fail → fix before committing
```

---

## 📚 Reference Documents

Before making changes, review:

1. **[PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md)** - SOLID principles, design patterns
2. **[CODING_STANDARDS.md](CODING_STANDARDS.md)** - Code quality standards
3. **[CODING_PRACTICES.md](CODING_PRACTICES.md)** - Language-agnostic best practices
4. **[JAVA_STANDARDS.md](JAVA_STANDARDS.md)** - Java-specific guidelines
5. **[KOTLIN_STANDARDS.md](KOTLIN_STANDARDS.md)** - Kotlin-specific guidelines

---

## 🎓 Training Examples

### Example 1: Extract Method Refactoring

**User**: "The buildReport method is too long, please refactor"

**AI Agent Process**:
```
1. Read method (identify 3 sub-responsibilities)
2. Create task list:
   - Refactor: Extract header generation → COMMIT
   - Refactor: Extract body generation → COMMIT  
   - Refactor: Extract footer generation → COMMIT
3. Execute each task separately with commit
```

### Example 2: Add New Feature

**User**: "Add support for PDF reports"

**AI Agent Process**:
```
1. Create task list:
   - Test: Add test for PdfReportWriter → COMMIT (with implementation)
   - Refactor: Extract common report logic if needed → COMMIT
   - Feature: Register PDF writer in ReportGenerator → COMMIT
   - Docs: Update README with PDF support → COMMIT
2. Execute each task separately with commit
```

### Example 3: God Class Refactoring

**User**: "The OrderProcessor class is doing too much. Please refactor it to follow Single Responsibility Principle."

**AI Agent Process**:
```
1. Check test coverage:
   # Run your project's test suite with coverage reporting, e.g.:
   # ./gradlew test jacocoTestReport | npm run test:coverage
   # pytest --cov | go test -cover ./...
   # Verify >80% coverage exists

2. Create task list:
   - Refactor: Extract payment logic to PaymentService → COMMIT
   - Refactor: Extract inventory logic to InventoryService → COMMIT  
   - Refactor: Extract notification logic to NotificationService → COMMIT
   - Refactor: Update OrderProcessor to use injected dependencies → COMMIT
   - Test: Update tests for new structure → COMMIT
   - Docs: Update architecture documentation → COMMIT

3. Execute EACH refactoring separately:
   
   Step 1: Extract PaymentService
   - Create PaymentService class with one responsibility
   - Run tests (must pass)
   - Commit: "refactor: extract payment logic to PaymentService class"
   
   Step 2: Extract InventoryService  
   - Create InventoryService class with one responsibility
   - Run tests (must pass)
   - Commit: "refactor: extract inventory logic to InventoryService class"
   
   ... continue for each extraction ...
   
   Final: Update OrderProcessor
   - Inject all extracted dependencies
   - Run tests (must pass)
   - Commit: "refactor: inject dependencies into OrderProcessor"
```

**Result**: 6 separate refactoring commits, each safe to revert

---

## ⚡ Quick Reference Card

**Before ANY code change:**
```
1. Create task list (TodoWrite)
2. For each task:
   a. Mark as "in_progress"
    b. Make ONE logical change
   c. Run your project's test suite
   d. Verify: all tests pass
   e. Commit with clear message
   f. Mark as "completed"
3. Update documentation (separate commit)
```

**Commit message template:**
```
<type>: <one-line description>

- Bullet points explaining what changed
- Why the change was made
- Any important context or rationale
```

**Test before commit:**
```bash
# Run your project's test suite, e.g.:
# ./gradlew test | npm test | pytest | go test ./... | dotnet test
```

---

## 🚨 Red Flags (Stop and Ask User)

If you encounter these situations, STOP and ask the user:

1. **Unclear scope**: "The feature requires changing 10+ files"
   → Ask: "This is a large change. Should I break it into multiple phases?"

2. **Breaking change**: "This change will break the public API"
   → Ask: "This is a breaking change. Should we maintain backward compatibility?"

3. **Test failures**: "Tests are failing after my change"
   → Ask: "Tests are failing. Should I fix the implementation or update the tests?"

4. **Conflicting patterns**: "The existing code doesn't follow SOLID"
   → Ask: "Should I refactor the existing code first?"

---

## 🔄 Special Section: Refactoring Guidelines

### CRITICAL: Never Refactor Without Tests

**Before refactoring ANY code:**

1. **Check Test Coverage**
   ```bash
   # Run your project's test suite with coverage reporting, e.g.:
   # ./gradlew test jacocoTestReport | npm run test:coverage
   # pytest --cov | go test -cover ./...
   ```
   
2. **Requirements:**
   - ✅ Minimum 80% line coverage for code being refactored
   - ✅ 100% coverage for critical paths (scoring, analysis, reports)
   - ✅ All existing tests must PASS

3. **If Coverage is Insufficient:**
   - STOP refactoring
   - Write tests FIRST
   - Use Pattern 2 (TDD approach) to add tests
   - Then proceed with refactoring

### Refactoring Micro-Commit Rules

**Each refactoring step = One commit**

Examples of ONE refactoring step:
- Extract one method
- Rename one variable/class
- Move one method to another class
- Introduce one parameter object
- Extract one interface

**DO NOT bundle multiple refactorings:**

❌ **BAD** - One commit with:
```
- Extract 3 methods
- Rename 2 classes
- Move code to new package
```

✅ **GOOD** - Three commits:
```
Commit 1: "refactor: extract calculateScore method from analyze"
Commit 2: "refactor: rename UserManager to UserCreator"  
Commit 3: "refactor: move validation logic to validators package"
```

### Refactoring Workflow

```
For Each Refactoring:
1. Verify tests exist and pass
2. Make ONE refactoring change
3. Run tests (must still pass)
4. Commit immediately
5. Repeat for next refactoring

NEVER:
- Skip running tests after refactoring
- Batch multiple refactorings into one commit
- Refactor code without test coverage
- Continue if tests fail after refactoring
```

### When to Refactor

**Proactive Refactoring (Do these automatically):**
- Method exceeds 15 lines → Extract methods
- Class exceeds 300 lines → Split responsibilities
- Duplicated code appears → Extract to shared method
- Hard-coded dependencies → Inject via constructor
- Long parameter list (>5 params) → Introduce parameter object

**Reactive Refactoring (Ask user first):**
- Large architectural changes
- Moving code between packages
- Changing public APIs
- Breaking backward compatibility

### Refactoring Commit Message Format

```
refactor: <what you refactored>

- Why: <reason for refactoring>
- Impact: <what improved>
- Tests: All pass, no behavior change
```

**Examples:**

```
refactor: extract timestamp generation into separate method

- Why: Prepare for adding timestamps to report filenames
- Impact: Single responsibility, easier to test
- Tests: All pass, no behavior change
```

```
refactor: replace long parameter list with config object

- Why: Method had 7 parameters, violating clean code principles
- Impact: Clearer method signature, easier to extend
- Tests: All pass, no behavior change
```

---

## ✅ Success Criteria

**You're following the workflow correctly if:**

- ✅ Each commit can be described in one sentence
- ✅ Each commit passes all tests
- ✅ Each commit is production-ready (tests pass, build succeeds, no lint errors)
- ✅ Commit messages are clear and follow format
- ✅ Git history reads like a story of the feature development
- ✅ Any commit can be reverted without breaking the build
- ✅ Each commit is a "save point" - code works at every commit

---

## 📞 When in Doubt

**If you're unsure about anything:**

1. **Check the checklist**: [PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md)
2. **Ask the user**: "I'm about to make X change. Should I split it into steps A, B, C?"
3. **Default to smaller commits**: When in doubt, make more commits rather than fewer

---

**Remember**: The goal is a clean, reviewable, revertable git history where each commit represents one logical change.

**AI Agent Pledge**: "I will follow this workflow for every code change, no exceptions. Every commit will be production-ready."

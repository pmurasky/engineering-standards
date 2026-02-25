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

## 🧪 Core TDD Rule: One Test at a Time

During TDD, write exactly one failing test, make that test pass with the minimal implementation, refactor safely, and only then add the next test.

- Do not queue multiple failing tests before implementing.
- Repeat RED → GREEN → REFACTOR as small cycles.
- Commit only when the suite is green and the current logical change is production-ready.

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

### Selecting Work

When the user asks what to work on next (or you need to suggest work), use the project's issue tracker.
If the repository is on GitHub and `gh` is available, consult **GitHub Issues**:

```bash
# List open issues by priority
gh issue list --label "P1: should fix" --state open
gh issue list --label "P2: nice to have" --state open

# View a specific issue
gh issue view <number>
```

If GitHub is not available, use the equivalent tracker queries for priority labels/status and apply the same prioritization rules.

**Priority order**: P1 issues before P2. Within a priority, prefer issues that unblock other work.

When starting work on an issue, reference it in your commit messages (e.g., `feat(python): add Python standards (closes #2)`).

### Closing Issues When Complete

**CRITICAL**: After completing work on an issue, you MUST close it in the active tracker.
If using GitHub with `gh`, use:

```bash
# Close issue with a summary comment
gh issue close <number> --comment "Completed in commit <hash>.

Implementation includes:
- Key feature 1
- Key feature 2
- Test coverage: X%
- All tests pass ✅
- Build succeeds ✅

All acceptance criteria met."
```

If GitHub is not available, close the issue/ticket in your tracker with an equivalent completion summary.

**Complete workflow for issues:**
1. ✅ Implement the feature/fix
2. ✅ Write tests and verify coverage
3. ✅ Commit the changes
4. ✅ Push to remote (`git push`) when remote write access is available
5. ✅ **Close the issue/ticket with a completion summary** (or provide closure-ready notes for a maintainer when you cannot close directly)

**Never forget step 5!** Closing issues keeps the project board clean and provides a clear audit trail of what was completed.

### Before Making ANY Code Changes

**Step 0: Pull Latest Changes**
```bash
git pull
```
Ensure you are working on the latest code before making any changes. This prevents merge conflicts and avoids duplicating work that has already been done.

**Step 1: Read and Acknowledge**
```
AI Agent: I will follow the micro-commit workflow documented in ./AI_AGENT_WORKFLOW.md
```

**Step 2: Create Task List**
Use your task tracking tool to break down the work:
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
├─ Write one failing test
├─ Run tests (should fail)
└─ Don't commit yet

Step 2: IMPLEMENT (Green) → COMMIT
├─ Write minimum code to pass that one test
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

Scope is recommended and may be omitted for trivial cross-cutting changes.

```
<type>(<scope>): <description>
# or
<type>: <description>

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
refactor(reporting): extract timestamp generation into separate method

- Add generateTimestamp() method to encapsulate timestamp formatting logic
- Import java.time classes for future timestamp usage
- No behavior change, pure refactoring to prepare for timestamped filenames
```

```
feat(reporting): add timestamp to report filenames

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
Commit 1: "refactor(reporting): extract timestamp generation method"
Commit 2: "feat(reporting): add timestamp to report filenames"
  (includes updated tests - all tests pass)
Commit 3: "docs: update documentation for timestamped reports"
```

### ❌ Mistake 2: Committing Failing Tests

**NEVER commit code where tests fail.** Every commit must be production-ready with all tests passing. If your implementation breaks existing tests, update the tests in the same commit.

### ❌ Mistake 3: Committing Without Running Tests

**ALWAYS run tests before committing:**
```bash
# Run your project's test suite, e.g. one of:
# ./gradlew test
# npm test
# pytest
# go test ./...
# dotnet test
```

### ❌ Mistake 4: Vague Commit Messages

**BAD**: "update code"
**GOOD**: "refactor(validation): extract validation logic to separate class"

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

### Using Task Tracking

**ALWAYS use your task tracking tool to track micro-commits:**

```
At start of feature, create a task list:
  1. Refactor: extract helper method        [pending]
  2. Feature: implement core logic          [pending]
  3. Test: update test assertions           [pending]
  4. Docs: update README                    [pending]

Before starting each task, mark it in progress:
  1. Refactor: extract helper method        [in_progress]
  ...

After committing each task, mark it complete:
  1. Refactor: extract helper method        [completed]
  ...
```

### Using Bash Tool for Tests

**ALWAYS run unit tests before committing:**

```bash
# Run your project's unit test suite (optionally filter to relevant tests), e.g.:
# ./gradlew test --tests "RelevantTestClass"
# npm test -- --grep "RelevantTest"
# pytest tests/test_relevant.py
# go test ./path/to/package
# dotnet test --filter "RelevantTestClass"

# Check test output
   # If all pass → proceed to commit
   # If any fail → fix before committing
```

**Run unit tests + integration tests before pushing:**

```bash
# Re-run unit tests and run integration tests before pushing, e.g. one of:
# ./gradlew test integrationTest
# npm run test:all
# pytest && pytest tests/integration/
# go test ./... && go test -tags=integration ./...

# If any fail → fix locally before pushing
```

**CI remains the hard gate** and runs the full test suite (unit + integration + E2E) on push/PR.

---

## 📚 Reference Documents

Before making changes, review:

1. **[PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md)** - SOLID principles, design patterns
2. **[CODING_STANDARDS.md](CODING_STANDARDS.md)** - Code quality standards
3. **[CODING_PRACTICES.md](CODING_PRACTICES.md)** - Language-agnostic best practices
4. **[GO_STANDARDS.md](GO_STANDARDS.md)** - Go-specific guidelines
5. **[JAVA_STANDARDS.md](JAVA_STANDARDS.md)** - Java-specific guidelines
6. **[KOTLIN_STANDARDS.md](KOTLIN_STANDARDS.md)** - Kotlin-specific guidelines
7. **[PYTHON_STANDARDS.md](PYTHON_STANDARDS.md)** - Python-specific guidelines

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
1. Check unit test coverage:
   # Run your project's test suite with coverage reporting, e.g. one of:
   # ./gradlew test jacocoTestReport
   # npm run test:coverage
   # pytest --cov
   # go test -cover ./...
   # Verify >80% unit test coverage exists (unit tests only)

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
1. Create task list (use your task tracking tool)
2. For each task:
   a. Mark as "in_progress"
    b. Make ONE logical change
   c. Run unit tests
   d. Verify: all unit tests pass
   e. Commit with clear message
   f. Mark as "completed"
3. Update documentation (separate commit)
4. Before pushing: run unit tests + integration tests
```

**Commit message template:**
```
<type>(<scope>): <one-line description>
# or
<type>: <one-line description>

- Bullet points explaining what changed
- Why the change was made
- Any important context or rationale
```

**Test before commit (unit tests):**
```bash
# Run your project's unit test suite, e.g. one of:
# ./gradlew test
# npm test
# pytest
# go test ./...
# dotnet test
```

**Test before push (unit + integration tests):**
```bash
# Re-run unit tests and run integration tests before pushing, e.g.:
# ./gradlew test integrationTest
# npm run test:all
# pytest && pytest tests/integration/
# go test ./... && go test -tags=integration ./...
```

---

## 🚨 Red Flags (Stop and Ask User)

If you encounter these situations, STOP and ask the user:

1. **Unclear scope**: "The feature requires changing 10+ files"
   → Ask: "This is a large change. Should I break it into multiple phases?"

2. **Breaking change**: "This change will break the public API"
   → Ask: "This is a breaking change. Should we maintain backward compatibility?"

3. **Test failures with unclear expected behavior**: "Tests are failing after my change and the requirement is ambiguous"
   → First action: diagnose and fix in the same branch (fix code when test is correct; update test when requirement changed)
   → Ask user only if expected behavior cannot be inferred from existing tests, docs, or acceptance criteria

4. **Conflicting patterns**: "The existing code doesn't follow SOLID"
   → Ask: "Should I refactor the existing code first?"

---

## 🔄 Special Section: Refactoring Guidelines

### CRITICAL: Never Refactor Without Tests

**Before refactoring ANY code:**

1. **Check Unit Test Coverage**
   ```bash
   # Run your project's test suite with coverage reporting, e.g. one of:
   # ./gradlew test jacocoTestReport
   # npm run test:coverage
   # pytest --cov
   # go test -cover ./...
   ```
   
2. **Requirements (unit tests only -- integration/E2E tests do not count toward these thresholds):**
   - ✅ Minimum 80% unit test line coverage for code being refactored
   - ✅ 100% unit test coverage for critical paths (scoring, analysis, reports)
   - ✅ All existing tests must PASS

3. **If Unit Test Coverage is Insufficient:**
   - STOP refactoring
   - Write unit tests FIRST
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
- Refactor code without unit test coverage
- Continue if tests fail after refactoring
```

### When to Refactor

**Proactive Refactoring (Do these automatically):**
- Method exceeds language-specific line limit (15-20 lines) → Extract methods
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
refactor(<scope>): <what you refactored>

- Why: <reason for refactoring>
- Impact: <what improved>
- Tests: All pass, no behavior change
```

**Examples:**

```
refactor(reporting): extract timestamp generation into separate method

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

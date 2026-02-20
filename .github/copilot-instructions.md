# Engineering Standards

Follow these engineering standards for ALL code changes in this repository.

## TDD Micro-Commit Cycle
For ALL code changes, follow the STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT cycle. See `docs/AI_AGENT_WORKFLOW.md` for the full workflow.

## Code Quality Rules
- Maximum method length: language-specific limit (typically 15-20 lines; Go: 25 lines)
- Maximum class length: 300 lines (consider refactoring if larger)
- Maximum 0-2 private methods per class (SRP guideline)
- Maximum 5 parameters per method (use parameter objects)
- No duplicated code (DRY principle)

## SOLID Principles
- **SRP**: Each class has ONE reason to change
- **OCP**: Open for extension, closed for modification (use Strategy Pattern)
- **LSP**: Subtypes must be substitutable for base types
- **ISP**: Prefer focused interfaces over fat interfaces
- **DIP**: Depend on abstractions, not concrete classes (use dependency injection)

## Commit Standards
- One logical change per commit
- Conventional Commits: `<type>(<scope>): <description>`
- Types: feat, fix, refactor, test, docs, perf, chore
- Every commit must be production-ready

## Testing Standards
- 80% minimum test coverage, 100% for critical paths
- Given-When-Then structure
- Descriptive test names (e.g., `shouldSelectLatestVersionWhenAvailable`)

## Detailed References
See `docs/` directory for comprehensive standards:
- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit workflow
- `docs/CODING_PRACTICES.md` - Language-agnostic practices, SOLID examples, and TDD
- `docs/CODING_STANDARDS.md` - Standards index (table of contents)
- `docs/PRE_COMMIT_CHECKLIST.md` - Pre-commit checklist
- `docs/DESIGN_PATTERNS.md` - Design patterns catalog and guidance
- `docs/SOLID_PRINCIPLES.md` - SOLID principles with multi-language examples
- `docs/JAVA_STANDARDS.md` - Java conventions (when working with Java)
- `docs/KOTLIN_STANDARDS.md` - Kotlin conventions (when working with Kotlin)
- `docs/TYPESCRIPT_STANDARDS.md` - TypeScript conventions (when working with TypeScript)
- `docs/NEXTJS_STANDARDS.md` - Next.js framework conventions (when working with Next.js)

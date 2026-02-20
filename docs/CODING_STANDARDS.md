# Coding Standards - Index

## Overview

This document serves as the table of contents for all coding standards and practices. Each topic has a dedicated document -- read the relevant file when you need detailed guidance.

## Standards Documents

### [CODING_PRACTICES.md](./CODING_PRACTICES.md)
**Language-agnostic coding practices and principles**
- YAGNI, Code Quality, SRP
- SOLID Principles (summary + link to dedicated guide)
- Design Patterns (summary + selection guidance)
- Domain Package Structure
- Testing Standards (unit, integration, E2E)
- Code Review Checklist
- Git Commit Standards (micro commits)
- Security, Performance, Error Handling, Logging
- TDD Micro-Commit Workflow (examples and enforcement)
- Refactoring guidelines

### [AI_AGENT_WORKFLOW.md](./AI_AGENT_WORKFLOW.md)
**TDD micro-commit workflow for AI coding agents**
- The authoritative STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT workflow
- Step-by-step patterns (existing tests, TDD, refactoring-only)
- Commit message format and examples
- AI agent checklists and self-verification
- Training examples and real-world scenarios
- Red flags (when to stop and ask)

### [PRE_COMMIT_CHECKLIST.md](./PRE_COMMIT_CHECKLIST.md)
**Pre-commit quality checklist**
- TDD micro-commit checklist
- SOLID principles violation checks (with code examples)
- Design patterns and anti-patterns checklist
- Code metrics (method length, class size, complexity)
- Testing, documentation, and security requirements

### [SOLID_PRINCIPLES.md](./SOLID_PRINCIPLES.md)
**SOLID principles deep-dive with multi-language examples**
- Real-world analogies and violation signals per principle
- Examples in Kotlin, Java, Python, and PHP
- How the principles relate to each other
- Common violations quick reference

### [DESIGN_PATTERNS.md](./DESIGN_PATTERNS.md)
**GoF design patterns catalog and usage guidance**
- Creational, structural, and behavioral patterns
- Use/avoid guidance and selection signals

### [JAVA_STANDARDS.md](./JAVA_STANDARDS.md)
**Java-specific conventions** (read when working with Java)

### [KOTLIN_STANDARDS.md](./KOTLIN_STANDARDS.md)
**Kotlin-specific conventions** (read when working with Kotlin)

### [PYTHON_STANDARDS.md](./PYTHON_STANDARDS.md)
**Python-specific conventions** (read when working with Python)

### [TYPESCRIPT_STANDARDS.md](./TYPESCRIPT_STANDARDS.md)
**TypeScript/JavaScript-specific conventions** (read when working with TypeScript or JavaScript)

### [GO_STANDARDS.md](./GO_STANDARDS.md)
**Go-specific conventions** (read when working with Go)

### [STATIC_ANALYSIS_STANDARDS.md](./STATIC_ANALYSIS_STANDARDS.md)
**Static analysis standards and configuration**
- PMD 7 configuration best practices and recommended thresholds
- CPD (Copy-Paste Detection) setup and DRY enforcement
- Suppression strategy and guidelines
- Tool-specific sections (PMD, Checkstyle, detekt, SpotBugs, ArchUnit, ESLint)
- Incremental adoption strategy for existing projects
- Metrics, reporting, and quality gates

### [ARCHUNIT_STANDARDS.md](./ARCHUNIT_STANDARDS.md)
**Architecture testing standards with ArchUnit**
- Enforces layer boundaries, package cycles, dependency direction, and module isolation
- Recommended rules by tier (critical, high value, advanced)
- Layered and onion/hexagonal architecture enforcement
- Java and Kotlin test examples
- Freezing arch rules for legacy codebase adoption
- Build integration (Maven/Gradle) and CI/CD guidance
- Incremental adoption strategy

### [SPOTBUGS_STANDARDS.md](./SPOTBUGS_STANDARDS.md)
**SpotBugs bytecode bug detection standards (Java only)**
- Bug categories (correctness, concurrency, security, bad practice, performance)
- Rank system (1-4 scariest through 15-20 of concern) and enforcement policy
- Effort/threshold configuration and exclusion filter syntax
- Find Security Bugs plugin (138 OWASP Top 10 detectors)
- `@SuppressFBWarnings` annotation usage with mandatory justification
- Maven and Gradle build integration
- CI/CD pipeline enforcement and incremental adoption strategy

### [CHECKSTYLE_STANDARDS.md](./CHECKSTYLE_STANDARDS.md)
**Checkstyle style enforcement standards (Java only)**
- Rule categories (Javadoc, naming, imports, formatting, size limits, coding practices, class design)
- Configuration walkthrough aligned to `config/checkstyle/checkstyle.xml`
- Suppression strategy (`@SuppressWarnings("checkstyle:...")` and filter files)
- Checkstyle vs. PMD overlap analysis and coordination
- IDE integration (IntelliJ, Eclipse, VS Code)
- Maven and Gradle build integration
- CI/CD pipeline enforcement and incremental adoption strategy

### [ADR_STANDARDS.md](./ADR_STANDARDS.md)
**Architecture Decision Records (ADR) guidance**
- ADR template with Status, Context, Decision, Alternatives, Consequences
- When to write an ADR (and when not to)
- ADR lifecycle: Proposed, Accepted, Deprecated, Superseded
- Maintenance over time (quarterly review, superseding, deprecating)
- Integration with development workflow and PR review process
- Example ADR with full template usage

### [LOGGING_STANDARDS.md](./LOGGING_STANDARDS.md)
**Logging standards and best practices**
- Structured logging (JSON format, required fields, parameterized logging)
- Log level definitions and selection rules (ERROR, WARN, INFO, DEBUG, TRACE)
- Correlation IDs for distributed tracing (propagation, header conventions)
- PII handling in logs (classification, masking strategies, deny-lists)
- Performance considerations (guarded evaluation, async logging)

### [SECURITY_STANDARDS.md](./SECURITY_STANDARDS.md)
**Comprehensive security standards and checklists**
- OWASP Top 10 reference and mitigation mapping
- Input validation and sanitization rules
- Authentication patterns (password hashing, MFA, token management)
- Authorization patterns (RBAC/ABAC, least privilege, IDOR prevention)
- Secrets management (vault, rotation, scanning)
- Supply chain security (dependency auditing, SBOMs)
- Encryption (TLS, data at rest, hashing algorithms)
- API security (rate limiting, CORS, payload limits)
- Security headers (CSP, HSTS, X-Frame-Options)
- Logging and PII handling (what to log, what to never log)
- SAST/DAST tooling and CI integration
- Secure error handling and severity classification

### [CONVERSION_PLAN_TEMPLATE.md](./CONVERSION_PLAN_TEMPLATE.md)
**Reusable plan template for framework conversion/porting projects**
- Gated phases: Pre-work, Port Behavior, Quality Sweep, Verification, Reports
- Behavioral baseline capture (error format, Content-Types, routes, RBAC)
- Quality gates enforced during porting (no deferred tech debt)
- @Suppress ban for structural violations, `!!` ban in production code
- Acceptance test pass rate tracking (target: 100%)
- Summary metrics and lessons learned

## Quick Reference

### For New Team Members
1. Start with [CODING_PRACTICES.md](./CODING_PRACTICES.md) for general philosophy
2. Read [SOLID_PRINCIPLES.md](./SOLID_PRINCIPLES.md) for SOLID principles with examples
3. Read [AI_AGENT_WORKFLOW.md](./AI_AGENT_WORKFLOW.md) for the micro-commit workflow
4. Review language-specific standards for your stack

### For Code Reviews
- Check [CODING_PRACTICES.md](./CODING_PRACTICES.md) Code Review Checklist
- Verify SOLID compliance using [PRE_COMMIT_CHECKLIST.md](./PRE_COMMIT_CHECKLIST.md)
- Review language-specific conventions

### Key Rules (Summary)
- **Methods**: 15-20 lines max (see language-specific standards)
- **Classes**: 300 lines max
- **Private methods**: 0-2 per class (SRP guideline)
- **Parameters**: 5 max per method
- **Test coverage**: 80% minimum, 100% for critical paths (unit tests only -- integration/E2E tests do not count toward coverage)
- **Commits**: One logical change per commit, production-ready
- **TDD**: STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT

## Questions or Updates?

If anything is unclear or needs discussion:
1. Open an issue for discussion
2. Propose changes via pull request
3. Update relevant document(s)

---

**Last Updated**: February 20, 2026
**Version**: 15.0 (Added CONVERSION_PLAN_TEMPLATE.md to index)

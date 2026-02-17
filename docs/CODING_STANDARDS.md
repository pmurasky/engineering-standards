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

### [TYPESCRIPT_STANDARDS.md](./TYPESCRIPT_STANDARDS.md)
**TypeScript-specific conventions** (read when working with TypeScript)

### [NEXTJS_STANDARDS.md](./NEXTJS_STANDARDS.md)
**Next.js framework conventions** (read when working with Next.js)

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
- **Methods**: 15 lines max
- **Classes**: 300 lines max
- **Private methods**: 0-2 per class (SRP guideline)
- **Parameters**: 5 max per method
- **Test coverage**: 80% minimum, 100% for critical paths
- **Commits**: One logical change per commit, production-ready
- **TDD**: STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT

## Questions or Updates?

If anything is unclear or needs discussion:
1. Open an issue for discussion
2. Propose changes via pull request
3. Update relevant document(s)

---

**Last Updated**: February 17, 2026
**Version**: 5.1 (Added TypeScript and Next.js standards to index)

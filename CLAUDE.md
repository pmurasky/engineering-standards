# Engineering Standards

You MUST follow these engineering standards for ALL code changes. No exceptions.

The full standards are defined in `AGENTS.md`. All principles apply equally to Claude Code.

## Context Hygiene

- Keep this file concise and broadly applicable across repositories.
- Move specialized, task-specific instructions into on-demand skills.
- Prefer scoped reads/searches and targeted verification over broad sweeps.
- Use fresh sessions between unrelated tasks to reduce stale context noise.

## Detailed Standards References

Load these on a need-to-know basis, not all at once.

- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit workflow and AI agent instructions
- `docs/CODING_PRACTICES.md` - Language-agnostic coding practices, SOLID examples, testing, and TDD
- `docs/CODING_STANDARDS.md` - Standards index (table of contents)
- `docs/DEVOPS_STANDARDS.md` - DevOps standards (CI/CD, deployment, and release workflows)
- `docs/NEXTJS_STANDARDS.md` - Next.js conventions for App Router projects
- `docs/TYPESCRIPT_STANDARDS.md` - TypeScript/JavaScript conventions (when working with TypeScript or JavaScript)
- `docs/PRE_COMMIT_CHECKLIST.md` - Pre-commit quality checklist
- `docs/ADR_STANDARDS.md` - Architecture Decision Records (ADR) guidance
- `docs/SECURITY_STANDARDS.md` - Security standards (auth, secrets, OWASP, API security)
- `docs/LOGGING_STANDARDS.md` - Logging standards (structured logging, log levels, correlation IDs, PII)
- `docs/CONVERSION_PLAN_TEMPLATE.md` - Conversion/porting plan template (gated phases, behavioral baseline, quality gates)

## Not Applicable to TypeScript/Next.js Projects

Do NOT load these files when working on a TypeScript or Next.js codebase:

- `docs/GO_STANDARDS.md`
- `docs/JAVA_STANDARDS.md`
- `docs/KOTLIN_STANDARDS.md`
- `docs/PYTHON_STANDARDS.md`
- `docs/ARCHUNIT_STANDARDS.md`
- `docs/CHECKSTYLE_STANDARDS.md`
- `docs/SPOTBUGS_STANDARDS.md`
- `docs/STATIC_ANALYSIS_STANDARDS.md`
- `docs/SOLID_PRINCIPLES.md` (SOLID summary is in `CODING_PRACTICES.md`)
- `docs/CONVERSION_PLAN_TEMPLATE.md` (only for language-porting tasks)
- `config/` (Java/Kotlin static analysis tool configs — not applicable)

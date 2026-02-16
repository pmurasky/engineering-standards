# Engineering Standards - Enhancement Backlog

Tracking document for improvements to the engineering standards project.

## P1 - Should Fix (Significant improvement)

- [ ] **Add TypeScript/JavaScript standards** -- Globs in all tool configs promise coverage for `*.ts, *.js` but no standards doc exists. Create `docs/TYPESCRIPT_STANDARDS.md`.

- [ ] **Add Python standards** -- Globs promise coverage for `*.py` but no standards doc exists. Create `docs/PYTHON_STANDARDS.md`.

- [ ] **Add Go standards** -- Globs promise coverage for `*.go` but no standards doc exists. Create `docs/GO_STANDARDS.md`.

- [ ] **Bring Cline rules to parity with other tools** -- `.clinerules/` has only one file. Add `code-review.md`, `java.md`, `kotlin.md` matching other tools. Cline supports `paths` frontmatter for path-scoped rules.

- [ ] **Fix AGENTS.md OpenCode-specific `TodoWrite` reference** -- Line 84 says "Create a task list using TodoWrite" which is OpenCode-specific. AGENTS.md is also read by GitHub Copilot and Cline. Use tool-agnostic phrasing.

## P2 - Nice to Have (Valuable additions)

### Additional Standards Topics

- [ ] **Add security standards** -- OWASP references, auth patterns, secrets management, supply chain security, rate limiting, CORS, CSP. Current coverage in CODING_PRACTICES.md is ~20 lines.

- [ ] **Add API design standards** -- REST, GraphQL, gRPC conventions. Endpoint naming, versioning, pagination, error response formats.

- [ ] **Add error handling patterns doc** -- Cross-language strategies: Result types, error codes vs exceptions, error boundaries, retry patterns.

- [ ] **Add logging standards** -- Structured logging, log levels, correlation IDs, PII handling, log aggregation guidance. Current coverage is ~8 lines.

- [ ] **Add database/SQL standards** -- Query optimization, migrations, ORM patterns, connection pooling, transaction management.

- [ ] **Add observability standards** -- Metrics, distributed tracing, health checks, alerting, SLOs/SLIs.

- [ ] **Add Docker/containerization standards** -- Dockerfile best practices, multi-stage builds, security scanning, image sizing.

- [ ] **Add CI/CD pipeline standards** -- Pipeline-as-code, deployment strategies (blue/green, canary), environment promotion, rollback.

- [ ] **Add git branching strategy** -- Trunk-based development vs GitFlow guidance, branch naming, PR conventions.

- [ ] **Add Architecture Decision Records (ADR) guidance** -- Template, when to write, how to maintain.

- [ ] **Add accessibility standards** -- WCAG compliance, semantic HTML, ARIA, CLI accessibility beyond current 6 lines.

### Additional Language Standards

- [ ] **Add C#/.NET standards** -- Globs cover `*.cs` but no doc exists.
- [ ] **Add Rust standards** -- Globs cover `*.rs` but no doc exists.
- [ ] **Add Swift standards** -- Globs cover `*.swift` but no doc exists.
- [ ] **Add Ruby standards** -- Globs cover `*.rb` but no doc exists.
- [ ] **Add C/C++ standards** -- Globs cover `*.c, *.cpp` but no doc exists.

### Inconsistencies to Fix

- [ ] **Verify Copilot reads CLAUDE.md** -- README compatibility matrix claims Copilot reads CLAUDE.md. May not be accurate.

---

**Last Updated**: February 16, 2026

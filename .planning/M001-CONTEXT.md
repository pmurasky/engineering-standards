# M001 — Ford Standards Integration

## Vision

Integrate the ford/ directory's docs and skills into the main engineering-standards project. This includes updating existing files with improved ford versions, adding net-new content, stripping all Ford-specific branding, and removing the ford/ directory.

## Background

A `ford/` directory was added to the repo containing ~45 docs and ~43 skill files (from a Ford Motor Company AI coding standards project). The ford files are a superset of this project's existing content — many files have grown significantly (+24 to +233 lines) and there are 18+ entirely new docs and 19+ entirely new skills not yet in this project.

## Success Criteria

1. All ford docs with improvements (ford version larger) are merged into `docs/`
2. All net-new ford docs are present in `docs/` with no Ford-specific branding
3. All ford skills updates are reflected in `.opencode/skills/`
4. All net-new ford skills are present in `.opencode/skills/` with no Ford-specific branding
5. `CODING_STANDARDS.md` index updated to reference all new docs
6. `ford/` directory deleted from repo
7. No remaining references to `ford-protech`, `AI Code Sentinel`, Ford automotive branding, or `ford-et.atlassian.net`
8. All commits follow conventional commits format and are production-ready

## Scope

### Docs — Update (ford version is newer/larger)
- `AI_AGENT_WORKFLOW.md` (+24L)
- `CODING_STANDARDS.md` (+75L, also needs new doc entries)
- `CONVERSION_PLAN_TEMPLATE.md` (+141L)
- `GO_STANDARDS.md` (+199L)
- `JAVA_STANDARDS.md` (+101L)
- `KOTLIN_STANDARDS.md` (+233L)
- `PRE_COMMIT_CHECKLIST.md` (+214L)
- `PYTHON_STANDARDS.md` (+111L)
- `SECURITY_STANDARDS.md` (+21L)
- `TYPESCRIPT_STANDARDS.md` (+171L)

### Docs — Add (net-new, strip ford branding)
- `CONTEXT_BUDGET_STANDARDS.md`
- `CONVERSION_PROMPT_TEMPLATE.md`
- `DEBUGGING_STANDARDS.md`
- `DESIGN_DOC_STANDARDS.md`
- `DESIGN_WORKFLOW.md`
- `FRONTEND_STANDARDS.md`
- `GIT_SETUP_STANDARDS.md`
- `IMPLEMENTATION_PLANNING.md`
- `SKILL_AUTHORING_STANDARDS.md`
- `STANDARDS_OWNERSHIP_MATRIX.md`
- `TDD_STRATEGIES.md`
- `TELEMETRY.md`
- `TESTING_STANDARDS.md`
- `VERIFICATION_STANDARDS.md`
- `templates/DESIGN_TEMPLATE.md`
- `templates/PLAN_TEMPLATE.md`
- `specs/skill-test-invariants.md`
- `specs/skill-test-promotion-rubric.md`

### Docs — SKIP (ford-internal)
- `PROJECT_PRESENTATION_DECK.md` — Ford branding
- `SUPERPOWERS_ANALYSIS.md` — ford-protech GitHub refs
- `README.md` — Ford routing index
- `go-testing-prompt-retirement.md` — housekeeping note
- `plans/` (3 files) — Ford-internal roadmap
- `superpowers/plans/` — Ford-internal

### Skills — Update existing (ford version is newer)
- `.opencode/skills/code-quality/` ← ford `coding-practices/`
- `.opencode/skills/micro-commit/` ← ford `micro-commit-workflow/` (add `references/refactoring-guidelines.md`)
- `.opencode/skills/pre-commit/` ← ford `pre-commit-checklist/` (add `references/solid-patterns-reference.md`)
- `.opencode/skills/tdd-enforcement/` ← ford `tdd-strategies/` (add REFERENCE.md)
- `.opencode/skills/test-coverage/` ← ford `testing-standards/` (add REFERENCE.md, strip ford-protech URL)
- `.opencode/skills/static-analysis-gate/` ← ford `static-analysis/` (add REFERENCE.md)

### Skills — Add net-new (strip ford branding)
- `solid-principles/` (NEW — no existing match)
- `design-patterns/` + REFERENCE.md
- `frontend-standards/` + REFERENCE.md
- `go-standards/` + REFERENCE.md
- `java-standards/` + REFERENCE.md
- `java-static-analysis/` + REFERENCE.md
- `kotlin-standards/` + REFERENCE.md
- `logging-standards/` + REFERENCE.md
- `python-standards/` + REFERENCE.md
- `security-standards/` + REFERENCE.md
- `typescript-standards/` + REFERENCE.md
- `context-budget/`
- `issue-workflow/`
- `multi-session-execution/`
- `progress-tracker/`
- `prompt-engineering/`
- `gitignore-bootstrap/`
- `github-pr-review-consumer/`
- `docusaurus-restructuring/`

### Skills — SKIP
- `ford-et-jira/` — Ford Enterprise Tooling + Jira (fully Ford-specific)
- `beads/` — Beads issue tracker (ford-specific tooling)
- `skills-index.json` — regenerate/adapt for this project

## Branding Cleanup Targets
- `testing-standards/REFERENCE.md` → strip `github.com/ford-protech/ai-code-sentinel/issues`
- Any file with `ford-protech`, `AI Code Sentinel`, `ford-et.atlassian.net`, Ford automotive brand

## Definition of Done
- [ ] All success criteria above met
- [ ] `ford/` directory deleted
- [ ] All tests pass (no test suite in this docs project — N/A)
- [ ] No lint errors in markdown
- [ ] All commits follow conventional commits

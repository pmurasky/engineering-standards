# M001 Roadmap — Ford Standards Integration

## Slices

### S01 — Update Existing Docs (ford versions are newer/larger)
**Goal:** Replace 10 existing docs with their improved ford counterparts.
**Files:** `AI_AGENT_WORKFLOW.md`, `CONVERSION_PLAN_TEMPLATE.md`, `GO_STANDARDS.md`, `JAVA_STANDARDS.md`, `KOTLIN_STANDARDS.md`, `PRE_COMMIT_CHECKLIST.md`, `PYTHON_STANDARDS.md`, `SECURITY_STANDARDS.md`, `TYPESCRIPT_STANDARDS.md`
**Risk:** Low — ford versions are strictly larger/improved. `CODING_PRACTICES.md` is skipped (ours is longer).
**After this:** 9 existing docs upgraded to ford-improved versions.

### S02 — Add Net-New Docs (strip ford branding)
**Goal:** Copy 18 net-new docs from ford/ into docs/, stripping any ford-specific references.
**Files:** `CONTEXT_BUDGET_STANDARDS.md`, `CONVERSION_PROMPT_TEMPLATE.md`, `DEBUGGING_STANDARDS.md`, `DESIGN_DOC_STANDARDS.md`, `DESIGN_WORKFLOW.md`, `FRONTEND_STANDARDS.md`, `GIT_SETUP_STANDARDS.md`, `IMPLEMENTATION_PLANNING.md`, `SKILL_AUTHORING_STANDARDS.md`, `STANDARDS_OWNERSHIP_MATRIX.md`, `TDD_STRATEGIES.md`, `TELEMETRY.md`, `TESTING_STANDARDS.md`, `VERIFICATION_STANDARDS.md`, `templates/DESIGN_TEMPLATE.md`, `templates/PLAN_TEMPLATE.md`, `specs/skill-test-invariants.md`, `specs/skill-test-promotion-rubric.md`
**Branding check:** Scan each for `ford-protech`, `AI Code Sentinel`, Ford automotive refs, `ford-et.atlassian.net` and remove.
**Risk:** Low — additive only.
**After this:** 18 new docs added, fully branded-neutral.

### S03 — Update Existing Skills (ford versions are newer)
**Goal:** Replace 6 existing .opencode/skills/ with ford counterparts, adding reference sub-files.
**Mappings:**
- `code-quality/` ← ford `coding-practices/`
- `micro-commit/` ← ford `micro-commit-workflow/` + `references/refactoring-guidelines.md`
- `pre-commit/` ← ford `pre-commit-checklist/` + `references/solid-patterns-reference.md`
- `tdd-enforcement/` ← ford `tdd-strategies/` + `REFERENCE.md`
- `test-coverage/` ← ford `testing-standards/` + `REFERENCE.md` (strip ford-protech URL)
- `static-analysis-gate/` ← ford `static-analysis/` + `REFERENCE.md`
**Risk:** Low — ford versions are improved; existing skill names and trigger descriptions preserved.
**After this:** 6 existing skills upgraded, reference files added.

### S04 — Add Net-New Skills (strip ford branding)
**Goal:** Add 19 net-new skills from ford/ into .opencode/skills/, stripping ford branding.
**Skills:**
- Language standards: `solid-principles`, `design-patterns`, `frontend-standards`, `go-standards`, `java-standards`, `java-static-analysis`, `kotlin-standards`, `logging-standards`, `python-standards`, `security-standards`, `typescript-standards`
- Workflow: `context-budget`, `issue-workflow`, `multi-session-execution`, `progress-tracker`, `prompt-engineering`
- Tooling: `gitignore-bootstrap`, `github-pr-review-consumer`, `docusaurus-restructuring`
**Skip:** `ford-et-jira` (fully Ford-specific), `beads` (ford-specific tracker), `skills-index.json` (adapt separately)
**Branding check:** Strip `ford-protech`, `AI Code Sentinel`, `ford-et.atlassian.net` from all skill files.
**Risk:** Low — additive only.
**After this:** 19 new skills added and available.

### S05 — Update CODING_STANDARDS.md Index
**Goal:** Update the standards index (TOC) to reference all newly added doc files.
**Changes:** Add entries for all 18 new docs in the appropriate sections.
**Risk:** Low — documentation only.
**After this:** Index is complete and accurate.

### S06 — Delete ford/ Directory
**Goal:** Remove the ford/ source directory from the repo.
**Risk:** Low — all valuable content already copied/integrated.
**After this:** `ford/` no longer exists in the repo.

## Commit Strategy

Each slice = one or more micro-commits following conventional commits format:
- S01: `docs(standards): update N files with ford improvements`
- S02: `docs(standards): add N net-new docs from ford integration`
- S03: `feat(skills): update 6 existing skills with ford improvements`
- S04: `feat(skills): add 19 net-new skills from ford integration`
- S05: `docs(standards): update CODING_STANDARDS index for new docs`
- S06: `chore: remove ford/ source directory`

## Dependencies

S01 → S05 (need to know what's being added to update index)
S02 → S05 (same)
S03, S04 — independent of S01/S02
S06 — depends on all of S01–S05 complete

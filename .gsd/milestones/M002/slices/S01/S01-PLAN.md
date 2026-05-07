# S01: Restructure Skill Directories

**Goal:** Create references/ subdirectories for the 3 workflow-heavy skills (pre-commit, micro-commit, tdd-enforcement) under both .claude/skills/ and .opencode/skills/, and populate each with the relevant workflow content extracted from docs/workflows/.
**Demo:** After this: each of the 3 workflow-heavy skills has a references/ directory with workflow.md content; other 6 skills directories are clean and ready for SKILL.md updates.

## Must-Haves

- references/ directories exist for pre-commit, micro-commit, tdd-enforcement under both surfaces. workflow.md content is present. All existing tests still pass. No SKILL.md broken.

## Proof Level

- This slice proves: Manual file inspection + test suite unchanged pass.

## Integration Closure

S02 depends on these directories being in place before editing SKILL.md files to reference them.

## Verification

- None — filesystem structural changes only. No runtime behavior affected.

## Tasks

- [x] **T01: Audit docs/workflows/ and create mapping** `est:15 min`
  List docs/workflows/ contents. Identify which workflow files map to which skill. Document the mapping:
- pre-commit-workflow.md → pre-commit references/
- tdd-workflow.md → tdd-enforcement references/
- micro-commit content → micro-commit references/
Verify whether references/ already partially exists in any skill.
  - Files: `docs/workflows/`, `.claude/skills/pre-commit/`, `.claude/skills/micro-commit/`, `.claude/skills/tdd-enforcement/`
  - Verify: ls docs/workflows/ and ls .claude/skills/*/references/ 2>/dev/null — inventory documented

- [x] **T02: Create references/ for .claude/skills workflow skills** `est:20 min`
  Create references/ directories and workflow.md files for pre-commit, micro-commit, and tdd-enforcement under .claude/skills/.
For each:
1. mkdir -p .claude/skills/<skill>/references/
2. Copy or extract relevant content from docs/workflows/ into references/workflow.md
3. Verify SKILL.md still parseable (no broken links)
Commit: `chore(skills): add references/ dirs for pre-commit, micro-commit, tdd-enforcement (.claude)`
  - Files: `.claude/skills/pre-commit/references/workflow.md`, `.claude/skills/micro-commit/references/workflow.md`, `.claude/skills/tdd-enforcement/references/workflow.md`
  - Verify: ls .claude/skills/pre-commit/references/ .claude/skills/micro-commit/references/ .claude/skills/tdd-enforcement/references/ — all 3 directories present with workflow.md

- [x] **T03: Create references/ for .opencode/skills workflow skills** `est:10 min`
  Mirror T02 for .opencode/skills/. Create references/ directories and workflow.md files for pre-commit, micro-commit, and tdd-enforcement under .opencode/skills/.
Commit: `chore(skills): add references/ dirs for pre-commit, micro-commit, tdd-enforcement (.opencode)`
  - Files: `.opencode/skills/pre-commit/references/workflow.md`, `.opencode/skills/micro-commit/references/workflow.md`, `.opencode/skills/tdd-enforcement/references/workflow.md`
  - Verify: ls .opencode/skills/pre-commit/references/ .opencode/skills/micro-commit/references/ .opencode/skills/tdd-enforcement/references/ — all 3 present

- [x] **T04: Verify enforcement tests still pass** `est:5 min`
  Run the enforcement integration test suite to confirm no regressions from directory additions.
python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v
Fix any regressions before moving to S02.
  - Files: `tests/enforcement_integration/test_enforcement_gates.py`
  - Verify: python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v — exit code 0, all green

## Files Likely Touched

- docs/workflows/
- .claude/skills/pre-commit/
- .claude/skills/micro-commit/
- .claude/skills/tdd-enforcement/
- .claude/skills/pre-commit/references/workflow.md
- .claude/skills/micro-commit/references/workflow.md
- .claude/skills/tdd-enforcement/references/workflow.md
- .opencode/skills/pre-commit/references/workflow.md
- .opencode/skills/micro-commit/references/workflow.md
- .opencode/skills/tdd-enforcement/references/workflow.md
- tests/enforcement_integration/test_enforcement_gates.py

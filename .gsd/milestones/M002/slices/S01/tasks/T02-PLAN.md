---
estimated_steps: 6
estimated_files: 3
skills_used: []
---

# T02: Create references/ for .claude/skills workflow skills

Create references/ directories and workflow.md files for pre-commit, micro-commit, and tdd-enforcement under .claude/skills/.
For each:
1. mkdir -p .claude/skills/<skill>/references/
2. Copy or extract relevant content from docs/workflows/ into references/workflow.md
3. Verify SKILL.md still parseable (no broken links)
Commit: `chore(skills): add references/ dirs for pre-commit, micro-commit, tdd-enforcement (.claude)`

## Inputs

- `docs/workflows/`
- `.claude/skills/pre-commit/SKILL.md`
- `.claude/skills/micro-commit/SKILL.md`
- `.claude/skills/tdd-enforcement/SKILL.md`

## Expected Output

- `.claude/skills/pre-commit/references/workflow.md`
- `.claude/skills/micro-commit/references/workflow.md`
- `.claude/skills/tdd-enforcement/references/workflow.md`

## Verification

ls .claude/skills/pre-commit/references/ .claude/skills/micro-commit/references/ .claude/skills/tdd-enforcement/references/ — all 3 directories present with workflow.md

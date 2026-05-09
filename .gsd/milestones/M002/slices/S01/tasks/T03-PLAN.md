---
estimated_steps: 2
estimated_files: 3
skills_used: []
---

# T03: Create references/ for .opencode/skills workflow skills

Mirror T02 for .opencode/skills/. Create references/ directories and workflow.md files for pre-commit, micro-commit, and tdd-enforcement under .opencode/skills/.
Commit: `chore(skills): add references/ dirs for pre-commit, micro-commit, tdd-enforcement (.opencode)`

## Inputs

- `.opencode/skills/pre-commit/SKILL.md`
- `.opencode/skills/micro-commit/SKILL.md`
- `.opencode/skills/tdd-enforcement/SKILL.md`
- `docs/workflows/`

## Expected Output

- `.opencode/skills/pre-commit/references/workflow.md`
- `.opencode/skills/micro-commit/references/workflow.md`
- `.opencode/skills/tdd-enforcement/references/workflow.md`

## Verification

ls .opencode/skills/pre-commit/references/ .opencode/skills/micro-commit/references/ .opencode/skills/tdd-enforcement/references/ — all 3 present

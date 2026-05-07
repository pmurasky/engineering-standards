---
estimated_steps: 5
estimated_files: 4
skills_used: []
---

# T01: Audit docs/workflows/ and create mapping

List docs/workflows/ contents. Identify which workflow files map to which skill. Document the mapping:
- pre-commit-workflow.md → pre-commit references/
- tdd-workflow.md → tdd-enforcement references/
- micro-commit content → micro-commit references/
Verify whether references/ already partially exists in any skill.

## Inputs

- `docs/workflows/`

## Expected Output

- `Mapping of docs/workflows/ files to target skill references/ paths documented in notes`

## Verification

ls docs/workflows/ and ls .claude/skills/*/references/ 2>/dev/null — inventory documented

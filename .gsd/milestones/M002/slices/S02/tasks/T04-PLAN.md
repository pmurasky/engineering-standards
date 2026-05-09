---
estimated_steps: 3
estimated_files: 1
skills_used: []
---

# T04: Full enforcement test suite green

Full test suite run to confirm all skills pass enforcement gates after all SKILL.md edits.
python3 -m pytest tests/enforcement_integration/ -v
If any skill fails, fix immediately before proceeding to S03.

## Inputs

- `.claude/skills/`
- `.opencode/skills/`

## Expected Output

- `All tests pass — exit code 0`

## Verification

python3 -m pytest tests/enforcement_integration/ -v — exit code 0, zero failures

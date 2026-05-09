---
estimated_steps: 4
estimated_files: 1
skills_used: []
---

# T04: Final verification and clean-up

Final check: run enforcement tests, validate no broken links to docs/workflows/ remain in updated docs, confirm all files updated are under size limits.

python3 -m pytest tests/enforcement_integration/ -v
grep -r 'docs/workflows' . --include='*.md' (should only appear in archive or historical context)

Commit any final touch-ups.

## Inputs

- `README.md`
- `CONTRIBUTING-SKILLS.md`
- `docs/SKILL_AUTHORING_STANDARDS.md`

## Expected Output

- `All tests pass`
- `Zero active docs/workflows/ references in updated docs`

## Verification

pytest exit code 0, grep shows no active docs/workflows/ references in updated docs

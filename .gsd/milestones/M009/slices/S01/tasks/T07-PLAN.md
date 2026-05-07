---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T07: Add Validation Coverage for Distribution Integrity

Add a validation test suite (in tests/validation/ or tests/distribution/) that checks: (1) every file listed in the install manifest actually exists in the repo, (2) README install section references files that exist, (3) .opencode/skills/ and .claude/skills/ are in sync per the source-of-truth rules from T04, (4) all referenced ADRs exist, (5) CI workflow file triggers validation on push. Tests should be runnable with a single command (e.g. `make validate` or `pytest tests/validation/`). Wire into the CI pipeline.

## Inputs

- `T05 implementation surface (file manifest)`
- `T04 skills sync rules`
- `T06 README`
- `Existing .github/workflows/ structure`

## Expected Output

- `tests/validation/ directory with test suite`
- `CI workflow step running validation`
- `make validate or equivalent single command`

## Verification

tests/validation/ exists with ≥4 validation checks; `make validate` or equivalent runs all checks; CI workflow includes validation step; all checks pass on current repo state.

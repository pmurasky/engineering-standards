---
estimated_steps: 9
estimated_files: 2
skills_used: []
---

# T03: Add .github/workflows/ci.yml and fix npm test

Create .github/workflows/ci.yml that:
- Triggers on: push to main, pull_request to main
- Checks out code
- Sets up Python (3.11 or 3.12)
- Installs dependencies (pip install pytest pyyaml)
- Runs: python3 -m pytest tests/enforcement_integration/ -v
- Runs: yamllint or python YAML validation on tests/skills/scenarios/**/*.yaml

Also fix the root package.json npm test placeholder to run the Python tests (via npx or a shell command).

Commit: `ci: add CI workflow to run enforcement tests on push and PR`

## Inputs

- `tests/enforcement_integration/README.md`
- `tests/enforcement_integration/test_enforcement_gates.py`

## Expected Output

- `.github/workflows/ci.yml`
- `root package.json npm test updated`

## Verification

Push branch to GitHub and confirm CI workflow appears in Actions tab and passes. Locally: cat .github/workflows/ci.yml and npm test both work.

## Observability Impact

GitHub Actions tab shows ci.yml run status on every push and PR; npm test now runs real tests locally

---
estimated_steps: 8
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

## Inputs

- `package.json`

## Expected Output

- `.github/workflows/ci.yml`
- `Updated package.json`

## Verification

Push branch to GitHub and confirm CI workflow appears in Actions tab and passes. Locally: cat .github/workflows/ci.yml and npm test both work.

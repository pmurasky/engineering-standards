---
estimated_steps: 1
estimated_files: 2
skills_used: []
---

# T03: Add Manifest Validation to CI

Add a CI workflow step (or update existing) that runs plugin manifest validation on every push and pull request. The step should: (1) install any required OpenCode CLI or validation tooling, (2) run validation against the manifest, (3) fail the build if the manifest is invalid. If no dedicated validation tool exists, write a lightweight JSON schema check script.

## Inputs

- `Manifest file from T01`
- `Existing .github/workflows/ structure`

## Expected Output

- `.github/workflows/ step or job for plugin manifest validation`
- `Validation passing on current state`

## Verification

CI workflow includes manifest validation step; step passes on current repo state; a deliberate manifest error causes step to fail (verified by dry-run or local test).

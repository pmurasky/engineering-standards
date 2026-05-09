---
estimated_steps: 1
estimated_files: 1
skills_used: []
---

# T03: Archive or delete docs/workflows/

Once zero active references remain, delete the docs/workflows/ directory. If any files have historical value, move them to an archive location (e.g., .archive/workflows/) with a README explaining why they were archived.

## Inputs

- `T02 completion (zero references)`

## Expected Output

- `docs/workflows/ removed from repository`

## Verification

Directory no longer exists at docs/workflows/. git status shows it as deleted.

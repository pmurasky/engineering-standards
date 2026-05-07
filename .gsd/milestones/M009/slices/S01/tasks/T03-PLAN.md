---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T03: Design One-Command Update Workflow

Design the surface of a one-command update workflow for existing consumers. Specify: how the tool detects the installed version (git tag, manifest file, SHA), what a dry-run shows (diff of changed files), how local customizations are preserved (merge strategy, user-owned sections, overwrite allowlist), rollback procedure if update breaks something, and whether updates are tag-based, branch-tracking, or manifest-driven. Document as docs/distribution/update-workflow.md.

## Inputs

- `docs/distribution/init-workflow.md (T02 output)`
- `docs/distribution/installation-modes.md (T01 output)`

## Expected Output

- `docs/distribution/update-workflow.md with version detection, dry-run, merge strategy, and rollback spec`

## Verification

docs/distribution/update-workflow.md exists; covers version detection, dry-run, local customization preservation, and rollback; update command surface is specified.

---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T02: Design One-Command Init Workflow

Design the surface of a one-command init workflow for first-time consumers. Specify: command name and args (e.g. `make init` or `scripts/init.sh`), what files it creates (AGENTS.md, .opencode/skills/*, .claude/skills/*, docs/ symlinks or copies), idempotency rules, conflict detection for pre-existing files (merge vs skip vs error), dry-run flag behavior, and post-init verification step. Document the decision as a spec in docs/distribution/init-workflow.md.

## Inputs

- `docs/distribution/installation-modes.md (T01 output)`
- `Existing scripts/ directory structure`
- `Current AGENTS.md and .opencode/ layout`

## Expected Output

- `docs/distribution/init-workflow.md with command spec, file manifest, conflict rules, and dry-run behavior`

## Verification

docs/distribution/init-workflow.md exists; covers command surface, file manifest, idempotency, conflict rules, and dry-run; ≥3 consumer scenarios documented.

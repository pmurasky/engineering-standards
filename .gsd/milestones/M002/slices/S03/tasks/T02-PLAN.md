---
estimated_steps: 1
estimated_files: 1
skills_used: []
---

# T02: Update or remove active docs/workflows/ references

For each reference found in T01: if it's a documentation link, update it to point to the new skill location (.claude/skills/ or .opencode/skills/). If it's a code reference, update the path. If it's obsolete, remove it. Commit each logical change separately.

## Inputs

- `T01 reference list`

## Expected Output

- `Updated files with no remaining docs/workflows/ references`

## Verification

Re-run grep from T01 — zero active references to docs/workflows/ should remain.

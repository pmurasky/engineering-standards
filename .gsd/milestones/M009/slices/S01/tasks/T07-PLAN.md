---
estimated_steps: 11
estimated_files: 3
skills_used: []
---

# T07: Add Validation Coverage for Distribution Integrity

Prevent future drift between docs, manifests, and actual packaged files.

Steps:
1. Add tests or validation scripts for installer manifest integrity.
2. Add checks ensuring README file lists match repo structure.
3. Add checks ensuring claimed OpenCode skills exist when documented.
4. Add tests for init/update dry-run behavior where practical.
5. Define minimal CI gates for packaging correctness.

Success Criteria:
- Packaging drift is test-detectable
- Docs-to-tree mismatches are caught automatically
- Installer/update behavior has regression protection

## Inputs

- `.planning/phases/09-standards-distribution-opencode-alignment/09-PLAN.md`

## Expected Output

- `Validation scripts and CI configuration`

## Verification

Validation scripts added and CI gates defined

---
estimated_steps: 11
estimated_files: 3
skills_used: []
---

# T03: Design One-Command Update Workflow

Specify how downstream repos safely adopt newer engineering-standards versions.

Steps:
1. Decide whether updates are tag-based, branch-based, or file-manifest-based.
2. Define how the update command detects installed provenance/version.
3. Define preview/dry-run behavior before overwriting files.
4. Define how local downstream customizations are preserved or flagged.
5. Define rollback expectations and failure behavior.

Success Criteria:
- Update flow is reviewable and safe
- Version/provenance tracking approach is chosen
- Dry-run or preview behavior is defined

## Inputs

- `.planning/phases/09-standards-distribution-opencode-alignment/09-PLAN.md`

## Expected Output

- `Update workflow specification document`

## Verification

Update workflow documented with safety rules and rollback plan

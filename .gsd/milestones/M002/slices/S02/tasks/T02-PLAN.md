---
estimated_steps: 6
estimated_files: 6
skills_used: []
---

# T02: Audit remaining 6 skills for compliance gaps

Audit the remaining 6 skills (code-quality, micro-commit, pre-commit, tdd-enforcement, static-analysis-gate, test-coverage) for compliance:
- Check frontmatter has only name + description (+ disable-model-invocation)
- Confirm Use when / Not for present within first 30 lines
- Confirm no ## References pointing to external docs/ paths
- Confirm line count under 500
Document any gaps found.

## Inputs

- `docs/SKILL_AUTHORING_STANDARDS.md`

## Expected Output

- `Gap list for remaining 6 skills — each skill marked PASS or list of specific fixes needed`

## Verification

Gap document written; no skill silently skipped

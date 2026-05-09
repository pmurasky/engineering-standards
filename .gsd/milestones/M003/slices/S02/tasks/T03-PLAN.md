---
estimated_steps: 5
estimated_files: 1
skills_used: []
---

# T03: Update SKILL_AUTHORING_STANDARDS.md §8

Update docs/SKILL_AUTHORING_STANDARDS.md §8:
1. Add or update the scenario test section with the exact basic.yaml format/template
2. Note that tests/skills/scenarios/<skill-name>/basic.yaml is mandatory for every skill (PR checklist item)
3. Add that CI enforces this on every push/PR via .github/workflows/ci.yml

Commit: `docs(standards): add scenario test template and CI enforcement notes to SKILL_AUTHORING_STANDARDS`

## Inputs

- `tests/skills/scenarios/code-quality/basic.yaml (as reference example)`

## Expected Output

- `docs/SKILL_AUTHORING_STANDARDS.md §8 updated with example template and CI note`

## Verification

Manual review: §8 has YAML example, mandatory requirement stated, CI reference present. File under 500 lines.

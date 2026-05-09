---
estimated_steps: 9
estimated_files: 1
skills_used: []
---

# T02: Create scenario tests for all 9 skills

Create tests/skills/scenarios/ directory and a basic.yaml scenario file for each of the 9 skills. Per SKILL_AUTHORING_STANDARDS.md §8 and the PR checklist §9.

Scenario file format:
```yaml
skill_name: <skill>
trigger: "<example user phrase that should invoke this skill>"
expected_behavior: "<what the skill should produce>"
not_for: "<example phrase that should NOT invoke this skill>"
```

Create for: code-quality, commit-review, micro-commit, pre-commit, refactoring-gate, spec-compliance, static-analysis-gate, tdd-enforcement, test-coverage.

## Inputs

- `SKILL_AUTHORING_STANDARDS.md`

## Expected Output

- `9 scenario YAML files in tests/skills/scenarios/`

## Verification

ls tests/skills/scenarios/ shows 9 directories, each with basic.yaml. yamllint tests/skills/scenarios/**/*.yaml (or python3 -c 'import yaml; yaml.safe_load(open(...))') validates all files are valid YAML

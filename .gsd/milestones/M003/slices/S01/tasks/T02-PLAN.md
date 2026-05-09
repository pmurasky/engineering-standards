---
estimated_steps: 10
estimated_files: 1
skills_used: []
---

# T02: Create scenario tests for all 9 skills

Create tests/skills/scenarios/ directory and a basic.yaml scenario file for each of the 9 skills. Per SKILL_AUTHORING_STANDARDS.md §8 and the PR checklist §9.

Scenario file format (derive from standard or establish if unspecified):
```yaml
skill_name: <skill>
trigger: "<example user phrase that should invoke this skill>"
expected_behavior: "<what the skill should produce>"
not_for: "<example phrase that should NOT invoke this skill>"
```

Create for: code-quality, commit-review, micro-commit, pre-commit, refactoring-gate, spec-compliance, static-analysis-gate, tdd-enforcement, test-coverage.

Commit: `test(skills): add scenario tests for all 9 skills per authoring standard §8`

## Inputs

- `docs/SKILL_AUTHORING_STANDARDS.md`
- `.claude/skills/*/SKILL.md (for trigger phrases and Use when content)`

## Expected Output

- `tests/skills/scenarios/code-quality/basic.yaml`
- `tests/skills/scenarios/commit-review/basic.yaml`
- `tests/skills/scenarios/micro-commit/basic.yaml`
- `tests/skills/scenarios/pre-commit/basic.yaml`
- `tests/skills/scenarios/refactoring-gate/basic.yaml`
- `tests/skills/scenarios/spec-compliance/basic.yaml`
- `tests/skills/scenarios/static-analysis-gate/basic.yaml`
- `tests/skills/scenarios/tdd-enforcement/basic.yaml`
- `tests/skills/scenarios/test-coverage/basic.yaml`

## Verification

ls tests/skills/scenarios/ shows 9 directories, each with basic.yaml. yamllint tests/skills/scenarios/**/*.yaml (or python3 -c 'import yaml; yaml.safe_load(open(...))') validates all files are valid YAML

## Observability Impact

None at runtime; test files serve as living documentation of expected skill invocation patterns

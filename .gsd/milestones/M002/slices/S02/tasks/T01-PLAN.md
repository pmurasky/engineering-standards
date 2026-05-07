---
estimated_steps: 10
estimated_files: 6
skills_used: []
---

# T01: Fix spec-compliance, commit-review, refactoring-gate

Fix the 3 most non-compliant skills first (highest ROI).

For each of spec-compliance, commit-review, refactoring-gate in BOTH .claude/skills/ and .opencode/skills/:
1. Remove legacy frontmatter fields (version, category)
2. Add `disable-model-invocation: true` after name/description
3. Add `## Use when` section within first 30 lines with 3-5 concrete trigger phrases
4. Add `## Not for` section immediately after with 2-3 exclusion cases
5. Remove any `## References` section that points to docs/ paths (CSO fix)
6. Add a `## Example` section with a short realistic scenario
7. Add an `## Anti-patterns` section with 2-3 common misuses

Commit per skill: `fix(skills): bring spec-compliance into Agent Skills compliance`

## Inputs

- `docs/SKILL_AUTHORING_STANDARDS.md`
- `.claude/skills/code-quality/SKILL.md (as compliant reference example)`

## Expected Output

- `.claude/skills/spec-compliance/SKILL.md (updated)`
- `.opencode/skills/spec-compliance/SKILL.md (updated)`
- `.claude/skills/commit-review/SKILL.md (updated)`
- `.opencode/skills/commit-review/SKILL.md (updated)`
- `.claude/skills/refactoring-gate/SKILL.md (updated)`
- `.opencode/skills/refactoring-gate/SKILL.md (updated)`

## Verification

python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -k 'spec_compliance or commit_review or refactoring_gate' -v OR full suite run — all 3 skills pass

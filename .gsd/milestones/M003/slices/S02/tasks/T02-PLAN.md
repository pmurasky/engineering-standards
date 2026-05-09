---
estimated_steps: 7
estimated_files: 2
skills_used: []
---

# T02: Update CONTRIBUTING-SKILLS.md

Update CONTRIBUTING-SKILLS.md (or CONTRIBUTING.md if that is where skill contribution guidance lives):
1. Add scenario test requirement: every new skill must include tests/skills/scenarios/<name>/basic.yaml
2. Add CI requirement: PRs must pass the CI workflow
3. Add the post-M002 frontmatter requirement (name + description + disable-model-invocation only)
4. Add Use when/Not for placement rule (within first 30 lines)
5. Remove references to canonical contract workflow

Commit: `docs(contributing): add scenario test, CI, and frontmatter requirements to contribution guide`

## Inputs

- `docs/SKILL_AUTHORING_STANDARDS.md`
- `.github/workflows/ci.yml`
- `tests/skills/scenarios/code-quality/basic.yaml (as example)`

## Expected Output

- `CONTRIBUTING-SKILLS.md updated with complete post-M002 requirements`

## Verification

Manual review: all 4 new requirements present. No mention of docs/workflows/ as active source.

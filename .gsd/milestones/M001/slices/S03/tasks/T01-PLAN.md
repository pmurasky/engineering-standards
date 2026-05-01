---
estimated_steps: 9
estimated_files: 3
skills_used: []
---

# T01: Proof of Concept - Migrate pre-commit Skill

Create the template for other skill migrations:
1. Create `.claude/skills/pre-commit/references/` directory
2. Copy `docs/workflows/pre-commit.md` to `references/workflow.md`
3. Update `SKILL.md` frontmatter (remove Claude-specific fields)
4. Update `SKILL.md` body with inline instructions
5. Ensure SKILL.md is under 500 lines
6. Validate structure matches Agent Skills spec
7. Run existing tests to ensure no breakage
8. Commit changes

## Inputs

- `docs/workflows/pre-commit.md`
- `.claude/skills/pre-commit/SKILL.md`

## Expected Output

- `Updated SKILL.md`
- `references/workflow.md`
- `Passing tests`

## Verification

SKILL.md has only name and description in frontmatter; references/ folder exists; all tests pass

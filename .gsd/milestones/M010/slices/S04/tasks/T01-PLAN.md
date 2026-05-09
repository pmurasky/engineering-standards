---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T01: Inventory Skills and Decide Source of Truth

List all skills in .opencode/skills/ and .claude/skills/. For each skill, record: SKILL.md presence, frontmatter completeness (name, description, triggers), and whether the skill is identical between the two directories or diverged. Determine per the M009/S01/T04 decision (or make the decision now if M009 is not yet complete) which directory is the source of truth for plugin exposure. Document as a skills inventory table.

## Inputs

- `ls .opencode/skills/ .claude/skills/`
- `M009/S01/T04 output if available`
- `Existing SKILL.md files`

## Expected Output

- `docs/skills-inventory.md with table: skill name, .opencode presence, .claude presence, frontmatter status, source-of-truth for plugin`

## Verification

docs/skills-inventory.md exists; all skills listed; source-of-truth directory designated; .claude/skills/ relationship stated.

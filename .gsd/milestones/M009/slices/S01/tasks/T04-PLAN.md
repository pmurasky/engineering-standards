---
estimated_steps: 11
estimated_files: 3
skills_used: []
---

# T04: Add OpenCode-Native Skills Packaging Plan

Bring the repo's OpenCode packaging in line with its documented portability story.

Steps:
1. Inventory which existing Claude skills should gain OpenCode-native counterparts.
2. Decide whether .opencode/skills/ should mirror, adapt, or index existing skill content.
3. Keep docs/ as source of truth where possible, avoiding unnecessary duplication.
4. Define how OpenCode skills relate to existing instructions, commands, and agents.
5. Set validation rules so docs never claim skills that are absent from the tree.

Success Criteria:
- .opencode/skills/ direction is explicit
- Relationship to .claude/skills/ is defined
- Source-of-truth rules avoid drift

## Inputs

- `.planning/phases/09-standards-distribution-opencode-alignment/09-PLAN.md`

## Expected Output

- `OpenCode skills packaging plan document`

## Verification

OpenCode packaging plan documented with skill inventory and source-of-truth rules

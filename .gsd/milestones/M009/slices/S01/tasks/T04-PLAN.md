---
estimated_steps: 1
estimated_files: 4
skills_used: []
---

# T04: Add OpenCode-Native Skills Packaging Plan

Inventory all skills in .opencode/skills/ and .claude/skills/. Decide and document: which directory is the source of truth, whether .opencode/skills/ and .claude/skills/ should be identical (symlinked, generated, or independently maintained), what happens during init/update for each. Note the M010 plugin model as an alternative and state explicitly whether file-based or plugin-based is the recommended path for skill delivery. Write the decision as an addition to the distribution ADR or a dedicated section.

## Inputs

- `Skill inventory (ls .opencode/skills/ .claude/skills/)`
- `M010 plugin context`
- `docs/distribution/installation-modes.md (T01 output)`

## Expected Output

- `docs/distribution/skills-packaging.md or ADR section documenting source-of-truth decision and sync rules`

## Verification

skills-packaging.md or ADR section exists; source-of-truth directory named; sync rules stated; M010 plugin model addressed explicitly.

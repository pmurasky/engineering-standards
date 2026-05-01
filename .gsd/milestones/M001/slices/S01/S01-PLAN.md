# S01: GSD Discuss Phase

**Goal:** Gather context and decisions for migrating from hybrid canonical-contract pattern to strict Agent Skills compliance
**Demo:** Decisions documented and ready for research

## Must-Haves

- Not provided.

## Proof Level

- This slice proves: Not provided.

## Integration Closure

Not provided.

## Verification

- Not provided.

## Tasks

- [ ] **T01: Gather Agent Skills context and decisions** `est:1 hour`
  Gather all context needed for the Agent Skills migration:
1. Understand current hybrid canonical-contract pattern
2. Identify target Agent Skills specification (agentskills.io)
3. Document key decisions: frontmatter changes, content strategy, migration approach
4. Identify all 9 skills to migrate
5. Map current structure to target structure
6. Document deferred items (Cursor/Copilot alignment, contract versioning, CI improvements)
  - Files: `.claude/skills/*/SKILL.md`, `docs/workflows/*.md`, `docs/CONTRIBUTING-SKILLS.md`
  - Verify: Context document captures all decisions, identifies all 9 skills, maps current→target structure, documents risks and deferred items

## Files Likely Touched

- .claude/skills/*/SKILL.md
- docs/workflows/*.md
- docs/CONTRIBUTING-SKILLS.md

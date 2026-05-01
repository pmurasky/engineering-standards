---
estimated_steps: 7
estimated_files: 3
skills_used: []
---

# T01: Gather Agent Skills context and decisions

Gather all context needed for the Agent Skills migration:
1. Understand current hybrid canonical-contract pattern
2. Identify target Agent Skills specification (agentskills.io)
3. Document key decisions: frontmatter changes, content strategy, migration approach
4. Identify all 9 skills to migrate
5. Map current structure to target structure
6. Document deferred items (Cursor/Copilot alignment, contract versioning, CI improvements)

## Inputs

- `.claude/skills/`
- `docs/workflows/`
- `docs/CONTRIBUTING-SKILLS.md`

## Expected Output

- `01-CONTEXT.md with complete decisions and context`

## Verification

Context document captures all decisions, identifies all 9 skills, maps current→target structure, documents risks and deferred items

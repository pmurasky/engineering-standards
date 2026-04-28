# Contributing to Agent Skills

## Overview

This guide explains how to create and maintain skills for the Agent Skills system. Our skills follow the [agentskills.io](https://agentskills.io) specification for maximum portability across AI agents (OpenCode, Claude, Kimi-code, and others).

## Agent Skills Specification

All skills must comply with the Agent Skills spec:

### File Structure
```
.claude/skills/{skill-name}/
├── SKILL.md              # Main skill file (required)
└── references/           # Additional reference materials (optional)
    └── workflow.md       # Detailed workflow documentation

.opencode/skills/{skill-name}/
└── SKILL.md              # OpenCode mirror of the same skill contract
```

Claude and OpenCode should expose the same skill catalog unless there is a documented tool-specific reason not to. Keep naming aligned across both surfaces.

### SKILL.md Format

**Frontmatter (YAML):**
```yaml
---
name: skill-name
description: Clear description of what this skill does and when to use it.
version: 1.0.0
category: quality-gate
---
```

**Requirements:**
- Required fields: `name`, `description`, `version`, `category`
- Optional fields: `dependencies`, `budget`
- No Claude-specific fields (no `argument-hint`, `disable-model-invocation`, etc.)
- Description should include trigger phrases (e.g., "Use when user asks...")
- Maximum 500 lines total
- Self-contained with inline instructions

**Metadata governance:** See [SKILL_METADATA_GOVERNANCE.md](./SKILL_METADATA_GOVERNANCE.md) for full spec.

### Content Structure

SKILL.md should include these sections:

1. **Title** (`# Skill Name`) - Clear, descriptive title
2. **Hard Gates** (`## Hard Gates`) - Non-negotiable prerequisites
3. **Workflow** (`## Workflow`) - Step-by-step instructions
4. **Status Vocabulary** (`## Status Vocabulary`) - Required output terms
5. **References** (`## References`) - Links to canonical docs and references/

### Example SKILL.md

```markdown
---
name: pre-commit
description: Run pre-commit readiness checks. Use when user asks "ready to commit", "pre-commit check", or "validate changes".
---

# Pre-Commit Validation

Validate that staged changes meet all required quality gates before committing.

## Hard Gates

Execute all quality gates. These are non-negotiable:

1. **Unit tests MUST pass** (when project test command exists)
2. **Build MUST succeed** (when project build command exists)
3. **Lint MUST pass** (when project lint command exists)
4. **Static analysis MUST pass** (when configured)

**Blocking rules:**
- If any required gate fails → output `NOT READY` with blockers listed first
- If command unavailable → report `NOT CONFIGURED` explicitly

## Workflow

1. Review staging area: `git diff --cached --stat`
2. Execute quality gates (tests, build, lint, static analysis)
3. Check coverage: Verify minimum 80% unit test coverage
4. Output assessment using status vocabulary

## Status Vocabulary

**Required output format:**
1. **Status**: `READY` or `NOT READY`
2. **Blocking items** (if any): List failures first
3. **Evidence**: Commands run and their outcomes
4. **Next actions**: Specific recommendations

**Status indicators:**
- `READY`: All quality gates pass
- `NOT READY`: One or more quality gates failed
- `NOT CONFIGURED`: Required tools/commands not available

## References

- [Full workflow details](references/workflow.md)
- `docs/PRE_COMMIT_CHECKLIST.md` - Comprehensive checklist
```

## When to Create references/

Create a `references/` folder when:
- The skill has detailed workflow documentation that would make SKILL.md too long
- You want to maintain canonical contract documentation separately
- The skill implements a complex multi-step process

Keep SKILL.md under 500 lines by moving detailed content to references/.

## Migration from Skills 2.0

If migrating from the old Skills 2.0 format:

1. Remove from frontmatter:
   - `argument-hint`
   - `disable-model-invocation`
   - Any other tool-specific fields

2. Replace XML tags with markdown:
   - Replace `<HARD-GATE>...</HARD-GATE>` with `## Hard Gates`
   - Replace `Canonical Contract: docs/workflows/X.md` with `## References` section

3. Move canonical contract content:
   - Copy `docs/workflows/{name}.md` to `references/workflow.md`
   - Update SKILL.md to reference it with relative link

4. Expand description:
   - Include trigger phrases in the description
   - Make it clear when the skill should be invoked

5. Add inline instructions:
   - Include essential workflow steps in SKILL.md
   - Don't rely solely on external references

## Testing

Run the enforcement tests to validate skill compliance:

```bash
python3 -m unittest discover -s tests/enforcement_integration -p "test_*.py"
```

Tests validate:
- Frontmatter has only name and description
- Skills are under 500 lines
- Hard Gates section exists
- Status Vocabulary section exists
- References/ folder exists (when applicable)
- OpenCode and Claude skill names stay in sync when mirrored

## Versioning

Skills use [Semantic Versioning](https://semver.org/) in the `version` frontmatter field:

- **MAJOR**: Breaking changes to hard gates, status vocabulary, or workflow steps
- **MINOR**: New features, additional references, non-breaking enhancements
- **PATCH**: Bug fixes, documentation updates, clarifications

When updating a skill:

1. Update SKILL.md with new behavior
2. Bump `version` according to SemVer rules
3. Update references/ if applicable
4. Run tests to ensure compliance
5. Commit with conventional commit message
6. Update documentation if behavior changes

## Quick Checklist

- [ ] Skill has required frontmatter: `name`, `description`, `version`, `category`
- [ ] Description includes trigger phrases
- [ ] Skill is under 500 lines
- [ ] Has `## Hard Gates` section
- [ ] Has `## Status Vocabulary` section
- [ ] Has `## References` section
- [ ] Uses relative paths for references
- [ ] Mirrored skill names stay aligned across `.claude/skills/` and `.opencode/skills/`
- [ ] All tests pass

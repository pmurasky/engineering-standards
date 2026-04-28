# Phase 2: Agent Skills Research - Findings

**Researched:** 2026-03-22
**Status:** Complete

## Agent Skills Specification Summary

Source: https://agentskills.io/specification

### Directory Structure

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files
```

### SKILL.md Format

**Frontmatter (YAML):**

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 chars, lowercase a-z/0-9/hyphens only, no leading/trailing hyphens, must match directory name |
| `description` | Yes | Max 1024 chars, non-empty, describe what and when |
| `license` | No | License name or file reference |
| `compatibility` | No | Max 500 chars, environment requirements |
| `metadata` | No | Key-value mapping for additional data |
| `allowed-tools` | No | Space-delimited pre-approved tools (experimental) |

**NO Claude-specific fields:**
- ❌ `argument-hint`
- ❌ `disable-model-invocation`
- ❌ `user-invocable`
- ❌ `context: fork`
- ❌ `agent`
- ❌ `hooks`

### Body Content Guidelines

- No format restrictions on Markdown body
- **Recommended: Keep under 500 lines**
- Include: step-by-step instructions, examples, edge cases
- Use progressive disclosure (split long content into references/)

### Progressive Disclosure Strategy

1. **Metadata** (~100 tokens): `name` + `description` loaded at startup
2. **Instructions** (< 5000 tokens recommended): Full `SKILL.md` loaded on activation
3. **Resources** (as needed): Files loaded only when required

### File References

- Use relative paths from skill root
- Keep references one level deep
- Avoid deeply nested chains

Example:
```markdown
See [the reference guide](references/REFERENCE.md) for details.
Run the extraction script: scripts/extract.py
```

### Validation

Use `skills-ref` tool to validate:
```bash
skills-ref validate ./my-skill
```

## Key Differences from Current Implementation

| Aspect | Current (Hybrid) | Agent Skills (Target) |
|--------|------------------|----------------------|
| Frontmatter | `name`, `description`, `argument-hint`, `disable-model-invocation` | `name`, `description` only |
| External refs | References `docs/workflows/` | Self-contained, uses `references/` |
| Architecture | Canonical contracts + adapters | Self-contained skills |
| Portability | Claude-optimized | Tool-agnostic |
| Line count | 20-30 lines (adapters) | Under 500 lines (full instructions) |

## Migration Requirements

### 1. Frontmatter Changes
- Remove `argument-hint` from all 9 skills
- Remove `disable-model-invocation` from all 9 skills
- Verify `name` matches directory name
- Verify `name` follows naming conventions
- Expand `description` to include "when to use" guidance

### 2. Content Migration
- Move canonical contract content from `docs/workflows/` to skill `references/`
- Update SKILL.md to include core instructions inline
- Add file references to `references/` content
- Keep SKILL.md under 500 lines

### 3. Directory Structure
- Add `references/` folder to each skill
- Optionally add `scripts/` or `assets/` if needed
- Remove external references

### 4. Testing Updates
- Remove contract reference validation
- Add Agent Skills structure validation
- Validate frontmatter compliance
- Validate file references exist

## Risks and Considerations

### Risk: Loss of Centralized Management
**Current:** Update canonical contract once, all adapters inherit changes  
**After:** Must update each skill individually  
**Mitigation:** Document that this is intentional for learning/compliance

### Risk: Content Duplication
**Current:** Single source of truth  
**After:** Workflow logic duplicated across skills  
**Mitigation:** Accept as trade-off for strict compliance

### Risk: Test Coverage
**Current:** Tests validate contract parity  
**After:** Need new validation approach  
**Mitigation:** Create Agent Skills validation tests

## Recommendations

1. **Migrate one skill first** as proof of concept (suggest `pre-commit`)
2. **Validate with `skills-ref`** tool if available
3. **Keep canonical contracts** in `docs/workflows/` for reference during migration
4. **Update tests incrementally** as skills are migrated
5. **Document the architectural change** clearly in README

## Next Steps

Proceed to Plan Phase to create detailed task breakdown.

---

*Phase: 02-agent-skills-research*
*Research completed: 2026-03-22*

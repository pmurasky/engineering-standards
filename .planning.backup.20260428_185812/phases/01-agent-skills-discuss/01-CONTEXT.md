# Phase 1: Agent Skills Compliance - Context

**Gathered:** 2026-03-22
**Status:** Ready for research

<domain>
## Phase Boundary

Refactor the Skills 2.0 architecture from a hybrid canonical-contract pattern to strict Agent Skills (agentskills.io) compliance. This involves:

1. Making skills self-contained (no external dependencies)
2. Removing Claude-specific frontmatter fields
3. Moving workflow content into skill `references/` folders
4. Updating tests and documentation

This phase delivers the **decisions and context** needed for downstream research and planning.

</domain>

<decisions>
## Implementation Decisions

### Target Specification
- **Agent Skills (agentskills.io)** - The open, vendor-neutral standard
- NOT Anthropic Skills (Claude-specific extensions)
- NOT hybrid canonical-contract pattern

### Primary Tools
- OpenCode (primary)
- Kimi-code (secondary)
- Future: Any Agent Skills-compliant tool

### Skill Structure
- Each skill: `SKILL.md` + optional `references/`, `scripts/`, `assets/`
- NO external references to `docs/workflows/`
- Self-contained and portable

### Frontmatter Changes
- KEEP: `name`, `description` (required by Agent Skills)
- REMOVE: `argument-hint`, `disable-model-invocation` (Claude-specific)
- Skill names: lowercase, hyphens, 1-64 chars
- Descriptions: 1-1024 chars, explain what and when

### Content Strategy
- SKILL.md body: Core instructions only (under 500 lines)
- Detailed content: Move to `references/` folder
- Progressive disclosure: Load details on demand

### Migration Approach
- Phase by phase (don't do everything at once)
- Maintain test coverage throughout
- Update documentation after skills are migrated

### Claude's Discretion
- Exact content organization within references/
- Whether to keep some canonical contracts for dev reference
- Test implementation details

</decisions>

<specifics>
## Specific Ideas

- "I want to learn the open standard, not proprietary formats"
- Skills should be "drop-in" portable to any compliant tool
- Keep it simple - this is for personal learning
- Follow the spec strictly as a learning exercise

</specifics>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Agent Skills Specification
- https://agentskills.io/specification - Official open standard
- https://agentskills.io/client-implementation/adding-skills-support - Client implementation guide
- https://agentskills.io/skill-creation/evaluating-skills - Skill evaluation guide

### Current Project Structure
- `docs/CONTRIBUTING-SKILLS.md` - Current contribution guidelines
- `docs/workflows/README.md` - Workflow contract documentation
- `docs/workflows/pre-commit.md` - Example canonical contract
- `docs/workflows/micro-commit.md` - Example canonical contract
- `docs/workflows/tdd-enforcement.md` - Example canonical contract
- `.claude/skills/pre-commit/SKILL.md` - Example skill adapter
- `.claude/skills/tdd-enforcement/SKILL.md` - Example skill adapter

### Enforcement Tests
- `tests/enforcement_integration/test_enforcement_gates.py` - Contract parity tests
- `tests/enforcement_integration/helpers.py` - Validation helpers

</canonical_refs>

<code_context>
## Existing Code Insights

### Current Skills (9 total)
Location: `.claude/skills/`
- code-quality/
- commit-review/
- micro-commit/
- pre-commit/
- refactoring-gate/
- spec-compliance/
- static-analysis-gate/
- tdd-enforcement/
- test-coverage/

### Current Pattern
Each skill has:
- `SKILL.md` with Claude-specific frontmatter
- References external `docs/workflows/{name}.md`
- Minimal adapter content (20-30 lines)

### Canonical Contracts (3 total)
Location: `docs/workflows/`
- pre-commit.md
- micro-commit.md
- tdd-enforcement.md

### Reusable Assets
- Enforcement test infrastructure
- Validation helper functions
- Fixture patterns for testing

### Integration Points
- Tests validate contract references (need updating)
- README documents workflow parity matrix (need updating)
- CONTRIBUTING-SKILLS.md explains current pattern (need updating)

</code_context>

<deferred>
## Deferred Ideas

- Cursor/Copilot adapter alignment (Issue #48) - separate phase
- Contract versioning (Issue #52) - future enhancement
- CI automation improvements (Issues #50, #51, #53) - separate phase

</deferred>

---

*Phase: 01-agent-skills-discuss*
*Context gathered: 2026-03-22*

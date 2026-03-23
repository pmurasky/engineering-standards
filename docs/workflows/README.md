# Canonical Workflow Contracts

This directory contains canonical workflow contracts that serve as the single source of truth for shared workflows across all tool adapters.

## Contract Format

Each canonical workflow contract follows this template:

```markdown
# [Workflow Name] Canonical Contract

## Purpose
Brief description of what this workflow accomplishes.

## Trigger Conditions
When this workflow should be invoked (specific phrases, conditions, contexts).

## Hard Gates
Non-negotiable blocking conditions that must be enforced.

## Workflow Steps
Ordered checklist of steps with clear success criteria.

## Status Vocabulary
Required output terms and status indicators that adapters must preserve.

## Fail/Fix/Rerun Loop
How failures are handled and recovery actions.

## Token Budget Intent
Whether this is always-on or on-demand, with estimated token usage.

## Required References
Links to detailed standards docs for full context.
```

## Tool Adapter Alignment

Each canonical contract maps to multiple tool adapters:

| Workflow | Canonical Contract | Claude Adapter | OpenCode Adapter | Cursor Rule | Copilot Instruction |
|----------|-------------------|----------------|------------------|-------------|-------------------|
| pre-commit | `docs/workflows/pre-commit.md` | `.claude/skills/pre-commit/SKILL.md` | `.opencode/commands/pre-commit.md` | `.cursor/rules/engineering-standards.md` | `.github/instructions/micro-commit.instructions.md` |
| micro-commit | `docs/workflows/micro-commit.md` | `.claude/skills/micro-commit/SKILL.md` | `.opencode/commands/micro-commit.md` | `.cursor/rules/engineering-standards.md` | `.github/instructions/micro-commit.instructions.md` |
| tdd-enforcement | `docs/workflows/tdd-enforcement.md` | `.claude/skills/tdd-enforcement/SKILL.md` | `.opencode/commands/tdd-enforcement.md` | `.cursor/rules/engineering-standards.md` | `.github/instructions/micro-commit.instructions.md` |

## Design Principles

1. **Concise**: Keep contracts focused on essential workflow logic
2. **Progressive Disclosure**: Link to detailed docs rather than duplicating content
3. **Tool-Agnostic**: Avoid tool-specific implementation details
4. **Testable**: Define clear success/failure criteria
5. **Stable**: Changes should be rare and well-communicated

## Contract Discovery

Contracts are discovered by convention: any `*.md` file in this directory is treated as a canonical contract, excluding `README.md` and `TEMPLATE.md`. Automated validation tests in `tests/enforcement_integration/` use this convention to verify that every contract has the required sections listed in the template above.

## Contributing

See [CONTRIBUTING-SKILLS.md](./CONTRIBUTING-SKILLS.md) for detailed contributor guidelines covering contract creation, adapter mapping, enforcement testing, and the end-to-end checklist.

**Quick reference — when updating a canonical contract:**

1. Update the canonical contract first
2. Update all tool adapters to reference the canonical contract
3. Update enforcement tests to validate parity
4. Test across all supported tools
5. Update the workflow mapping table above

**When adding a new workflow:**

1. Follow the contract template format (all eight required sections)
2. Start with one tool adapter to prove the pattern
3. Expand to other tools incrementally
4. Add enforcement tests and pressure fixtures
5. Add to the mapping table above
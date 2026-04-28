# Engineering Standards Skills Refactoring

## Vision
Refactor the Skills 2.0 architecture to achieve strict compliance with the Agent Skills open standard (agentskills.io), making skills self-contained, portable, and tool-agnostic.

## Current State
- Hybrid architecture with canonical contracts in `docs/workflows/`
- Claude-specific frontmatter (`argument-hint`, `disable-model-invocation`)
- Skills reference external canonical contracts
- Not strictly compliant with Agent Skills spec

## Target State
- Self-contained skills following Agent Skills spec
- Standard frontmatter (`name`, `description` only)
- Workflow content in `references/` folders
- Portable across OpenCode, Kimi-code, and other compliant tools

## Principles
1. **Spec Compliance**: Follow agentskills.io specification strictly
2. **Self-Contained**: Each skill is independent and portable
3. **Progressive Disclosure**: Use references/ for detailed content
4. **Under 500 Lines**: Keep SKILL.md focused and concise

## Non-Negotiables
- All skills must work with OpenCode (primary tool)
- Must maintain existing functionality
- Tests must pass after refactoring
- Documentation must be updated

# Roadmap: Skills Refactoring

## Milestone 1: Agent Skills Compliance
**Status:** In Progress

### Slice 1.1: GSD Discuss Phase
- **Goal:** Gather context and decisions for Agent Skills compliance refactoring
- **Status:** In Progress
- **Canonical refs:**
  - `docs/CONTRIBUTING-SKILLS.md` - Current contribution guidelines
  - `docs/workflows/README.md` - Workflow contract documentation
  - `docs/workflows/pre-commit.md` - Example canonical contract
  - `.claude/skills/pre-commit/SKILL.md` - Example skill adapter

### Slice 1.2: GSD Research Phase
- **Goal:** Research Agent Skills spec requirements and best practices
- **Status:** Pending
- **Canonical refs:**
  - agentskills.io specification
  - Existing skill implementations

### Slice 1.3: GSD Plan Phase
- **Goal:** Create detailed execution plan with tasks
- **Status:** Pending

## Milestone 2: Skills Restructuring
**Status:** Pending

### Slice 2.1: Execute - Restructure Directories
- **Goal:** Add references/ folders to all skills

### Slice 2.2: Execute - Update SKILL.md Files
- **Goal:** Remove Claude-specific frontmatter, update content

### Slice 2.3: Execute - Migrate Canonical Contracts
- **Goal:** Move workflow content to references/ folders

## Milestone 3: Testing and Documentation
**Status:** Pending

### Slice 3.1: Execute - Update Tests
- **Goal:** Update enforcement tests for Agent Skills compliance

### Slice 3.2: Execute - Update Documentation
- **Goal:** Update CONTRIBUTING-SKILLS.md and README

## Milestone 9: Standards Distribution & OpenCode Alignment
**Status:** In Progress

### Slice 9.1: Plan Distribution
- **Goal:** Plan and deliver install/update workflow and OpenCode packaging
- **Status:** In Progress
- **Canonical refs:**
  - `README.md` - Current install/update guidance
  - `opencode.json` - Current OpenCode instructions/plugins model
  - `docs/CONTRIBUTING-SKILLS.md` - Portable skill structure guidance
  - `docs/adr/0001-superpowers-upstream-sync-model.md` - Upstream sync constraints

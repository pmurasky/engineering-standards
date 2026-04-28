# Requirements: Agent Skills Compliance Refactoring

## Functional Requirements

### 1. Skill Structure Compliance
- Each skill MUST have `SKILL.md` in its directory
- Each skill MAY have `references/` folder for detailed docs
- Each skill MAY have `scripts/` folder for executables
- Each skill MAY have `assets/` folder for templates
- NO `README.md` inside skill folders

### 2. Frontmatter Compliance
- MUST include `name` field (1-64 chars, lowercase alphanum + hyphens)
- MUST include `description` field (1-1024 chars)
- MUST NOT include Claude-specific fields (`argument-hint`, `disable-model-invocation`, `user-invocable`)
- MUST NOT include XML tags in frontmatter
- MUST NOT use reserved words ("anthropic", "claude")

### 3. Content Requirements
- SKILL.md body MUST be under 500 lines
- MUST use progressive disclosure (references/ for details)
- MUST be self-contained (no external dependencies)
- MUST include core instructions inline

### 4. Migration Requirements
- Move canonical contracts from `docs/workflows/` to skill `references/`
- Update all 9 Claude skills
- Update enforcement tests
- Update documentation

## Success Criteria
- [ ] All skills validate against Agent Skills spec
- [ ] Skills work in OpenCode
- [ ] All tests pass
- [ ] Documentation reflects new structure
- [ ] No functionality lost in migration

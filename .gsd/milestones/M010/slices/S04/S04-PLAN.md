# S04: Expose Skills via Plugin

**Goal:** Expose all .opencode/skills/ skills through the plugin so consuming projects receive them automatically on install without manual file copying.
**Demo:** At least one skill (e.g. code-quality) is available in a consuming project without manual file copying after plugin install.

## Must-Haves

- All .opencode/skills/ skills registered in plugin manifest; skill loading verified via integration test or manual check; existing enforcement tests pass; .claude/skills/ relationship documented.

## Proof Level

- This slice proves: Integration test showing skill auto-loads in a clean consuming project after plugin install; all existing enforcement tests remain green.

## Integration Closure

Skills wired into S02 manifest scaffold; skill availability demonstrated in S05 documentation walkthrough test.

## Verification

- Skill load failures surface in consuming project's OpenCode session; enforcement tests updated to verify all skills discoverable via plugin.

## Tasks

- [ ] **T01: Inventory Skills and Decide Source of Truth** `est:30m`
  List all skills in .opencode/skills/ and .claude/skills/. For each skill, record: SKILL.md presence, frontmatter completeness (name, description, triggers), and whether the skill is identical between the two directories or diverged. Determine per the M009/S01/T04 decision (or make the decision now if M009 is not yet complete) which directory is the source of truth for plugin exposure. Document as a skills inventory table.
  - Files: `docs/skills-inventory.md`, `.opencode/skills/`, `.claude/skills/`
  - Verify: docs/skills-inventory.md exists; all skills listed; source-of-truth directory designated; .claude/skills/ relationship stated.

- [ ] **T02: Register Skills in Plugin Manifest** `est:1h`
  Register all .opencode/skills/ skills in the plugin manifest using the skill registration format from S01 research. Update opencode.json or package.json with the skills section. Verify manifest still validates. If skills require a specific directory structure or SKILL.md format to be discovered, adjust any non-conforming skills.
  - Files: `opencode.json`, `package.json`, `.opencode/skills/`
  - Verify: Manifest skills section present with all .opencode/skills/ entries; manifest validates; any adjusted skills still pass existing enforcement tests.

- [ ] **T03: Verify Skill Loading and Update Enforcement Tests** `est:1.5h`
  Run the existing enforcement test suite (tests/enforcement_integration/) to confirm all tests pass with the updated manifest and skill registrations. Then write a plugin skill loading integration test: install the plugin in a temp consuming project (or simulate with a local path install) and verify at least 2 skills are discoverable by OpenCode. Add an enforcement check that verifies every skill registered in the manifest has a valid SKILL.md.
  - Files: `tests/enforcement_integration/`, `tests/validation/`
  - Verify: All existing enforcement tests green; new integration test passes for ≥2 skills; SKILL.md existence check added to enforcement suite and passing.

- [ ] **T04: Document Skill Auto-Load vs Manual Config Requirement** `est:30m`
  Determine whether skills auto-load for consumers after plugin install or require explicit consumer-side OpenCode configuration (e.g. adding the plugin to .opencode/config.json). Document the answer clearly. If consumer-side config is required, write a minimal example config snippet. Add this finding to the docs/skills-inventory.md and ensure the S05 documentation task has this context.
  - Files: `docs/skills-inventory.md`
  - Verify: Auto-load vs manual config question answered with evidence; example config snippet present if needed; finding documented in skills-inventory.md.

## Files Likely Touched

- docs/skills-inventory.md
- .opencode/skills/
- .claude/skills/
- opencode.json
- package.json
- tests/enforcement_integration/
- tests/validation/

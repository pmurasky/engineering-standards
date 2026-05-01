# S03: GSD Plan Phase

**Goal:** Execute the migration plan: migrate 9 Claude skills from hybrid canonical-contract architecture to strict Agent Skills compliance
**Demo:** Execution plan with 13 tasks ready

## Must-Haves

- All 9 skills migrated to Agent Skills compliance. All tests pass. Documentation updated. No functionality lost. Project builds successfully.

## Proof Level

- This slice proves: validated

## Integration Closure

All skills use Agent Skills format with inline instructions and references/ folders. Tests validate compliance. Documentation reflects new architecture.

## Verification

- Test suite validates Agent Skills structure. Build passes. All skills load correctly.

## Tasks

- [ ] **T01: Proof of Concept - Migrate pre-commit Skill** `est:2 hours`
  Create the template for other skill migrations:
1. Create `.claude/skills/pre-commit/references/` directory
2. Copy `docs/workflows/pre-commit.md` to `references/workflow.md`
3. Update `SKILL.md` frontmatter (remove Claude-specific fields)
4. Update `SKILL.md` body with inline instructions
5. Ensure SKILL.md is under 500 lines
6. Validate structure matches Agent Skills spec
7. Run existing tests to ensure no breakage
8. Commit changes
  - Files: `.claude/skills/pre-commit/SKILL.md`, `.claude/skills/pre-commit/references/workflow.md`, `docs/workflows/pre-commit.md`
  - Verify: SKILL.md has only name and description in frontmatter; references/ folder exists; all tests pass

- [ ] **T02: Migrate micro-commit Skill** `est:1 hour`
  Apply proof-of-concept pattern to micro-commit skill:
1. Create `.claude/skills/micro-commit/references/` directory
2. Copy `docs/workflows/micro-commit.md` to `references/workflow.md`
3. Update `SKILL.md` frontmatter and body
4. Validate and test
5. Commit changes
  - Files: `.claude/skills/micro-commit/SKILL.md`, `.claude/skills/micro-commit/references/workflow.md`
  - Verify: Same success criteria as Task 1

- [ ] **T03: Migrate tdd-enforcement Skill** `est:1 hour`
  Apply pattern to tdd-enforcement skill. Same steps as Task 2.
  - Files: `.claude/skills/tdd-enforcement/SKILL.md`, `.claude/skills/tdd-enforcement/references/workflow.md`
  - Verify: Same success criteria as Task 1

- [ ] **T04: Migrate code-quality Skill** `est:1 hour`
  Migrate code-quality skill. Check if canonical contract exists in docs/workflows/. If yes, migrate as Tasks 2-3. If no, just update frontmatter and ensure self-contained.
  - Files: `.claude/skills/code-quality/SKILL.md`
  - Verify: SKILL.md updated with proper frontmatter and inline instructions

- [ ] **T05: Migrate commit-review Skill** `est:1 hour`
  Apply same migration pattern to commit-review skill.
  - Files: `.claude/skills/commit-review/SKILL.md`
  - Verify: Same success criteria as Task 1

- [ ] **T06: Migrate refactoring-gate Skill** `est:1 hour`
  Apply same migration pattern to refactoring-gate skill.
  - Files: `.claude/skills/refactoring-gate/SKILL.md`
  - Verify: Same success criteria as Task 1

- [ ] **T07: Migrate spec-compliance Skill** `est:1 hour`
  Apply same migration pattern to spec-compliance skill.
  - Files: `.claude/skills/spec-compliance/SKILL.md`
  - Verify: Same success criteria as Task 1

- [ ] **T08: Migrate static-analysis-gate Skill** `est:1 hour`
  Apply same migration pattern to static-analysis-gate skill.
  - Files: `.claude/skills/static-analysis-gate/SKILL.md`
  - Verify: Same success criteria as Task 1

- [ ] **T09: Migrate test-coverage Skill** `est:1 hour`
  Apply same migration pattern to test-coverage skill.
  - Files: `.claude/skills/test-coverage/SKILL.md`
  - Verify: Same success criteria as Task 1

- [ ] **T10: Update Enforcement Tests** `est:3 hours`
  Update test suite to validate Agent Skills compliance:
1. Review `tests/enforcement_integration/test_enforcement_gates.py`
2. Update `validate_contract_references()` - remove or modify
3. Update `validate_hard_gate_semantics()` - adapt for inline content
4. Add `validate_agent_skills_structure()` - check frontmatter compliance
5. Add `validate_skill_references()` - verify references/ folder files exist
6. Update test fixtures if needed
7. Run full test suite
8. Commit changes
  - Files: `tests/enforcement_integration/test_enforcement_gates.py`
  - Verify: Tests validate Agent Skills frontmatter, references/ folder structure, SKILL.md line count; all tests pass

- [ ] **T11: Update CONTRIBUTING-SKILLS.md** `est:2 hours`
  Update contribution guidelines for Agent Skills:
1. Read current `docs/CONTRIBUTING-SKILLS.md`
2. Update "Contract Structure" section to "Skill Structure"
3. Remove references to canonical contracts
4. Add Agent Skills frontmatter requirements
5. Add progressive disclosure guidelines
6. Update "Adapter Mapping" section
7. Update "Enforcement Testing" section
8. Commit changes
  - Files: `docs/CONTRIBUTING-SKILLS.md`
  - Verify: Guidelines reflect Agent Skills spec; no references to canonical contracts; clear frontmatter requirements documented

- [ ] **T12: Update README.md** `est:2 hours`
  Update project README to reflect new architecture:
1. Read current `README.md`
2. Update "What Gets Enforced" section if needed
3. Update "Project Structure" section
4. Update "Tool-Specific Features" section
5. Update "Workflow Parity Matrix"
6. Add note about Agent Skills compliance
7. Commit changes
  - Files: `README.md`
  - Verify: README accurately describes new structure; no outdated references to canonical contracts

- [ ] **T13: Deprecate or Archive Canonical Contracts** `est:1 hour`
  Handle old canonical contracts:
1. Decide on approach (recommend Option A: move to docs/archived-workflows/)
2. Execute chosen approach
3. Update any cross-references
4. Commit changes
  - Files: `docs/workflows/`
  - Verify: Old contracts properly archived or removed; cross-references updated

## Files Likely Touched

- .claude/skills/pre-commit/SKILL.md
- .claude/skills/pre-commit/references/workflow.md
- docs/workflows/pre-commit.md
- .claude/skills/micro-commit/SKILL.md
- .claude/skills/micro-commit/references/workflow.md
- .claude/skills/tdd-enforcement/SKILL.md
- .claude/skills/tdd-enforcement/references/workflow.md
- .claude/skills/code-quality/SKILL.md
- .claude/skills/commit-review/SKILL.md
- .claude/skills/refactoring-gate/SKILL.md
- .claude/skills/spec-compliance/SKILL.md
- .claude/skills/static-analysis-gate/SKILL.md
- .claude/skills/test-coverage/SKILL.md
- tests/enforcement_integration/test_enforcement_gates.py
- docs/CONTRIBUTING-SKILLS.md
- README.md
- docs/workflows/

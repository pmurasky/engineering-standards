# Phase 3: Agent Skills Migration - Execution Plan

**Planned:** 2026-03-22
**Status:** Ready for execution

## Overview

Migrate 9 Claude skills from hybrid canonical-contract architecture to strict Agent Skills compliance.

## Migration Strategy

**Approach:** Proof of concept first, then batch migration  
**Order:** Start with `pre-commit` (simplest), then migrate others  
**Validation:** After each skill, run tests to ensure no regressions

## Detailed Tasks

### Task 1: Proof of Concept - Migrate pre-commit Skill

**Objective:** Create the template for other skill migrations

**Steps:**
1. Create `.claude/skills/pre-commit/references/` directory
2. Copy `docs/workflows/pre-commit.md` to `references/workflow.md`
3. Update `SKILL.md`:
   - Remove `argument-hint` and `disable-model-invocation` from frontmatter
   - Expand `description` to include "when to use" guidance
   - Add inline instructions (hard gates, workflow steps)
   - Add reference to `references/workflow.md` for details
4. Ensure SKILL.md is under 500 lines
5. Validate structure matches Agent Skills spec
6. Run existing tests to ensure no breakage
7. Commit changes

**Success Criteria:**
- [ ] SKILL.md has only `name` and `description` in frontmatter
- [ ] `references/` folder exists with workflow content
- [ ] SKILL.md is self-contained with core instructions
- [ ] All tests pass
- [ ] Committed with clear message

---

### Task 2: Migrate micro-commit Skill

**Objective:** Apply proof-of-concept pattern to micro-commit skill

**Steps:**
1. Create `.claude/skills/micro-commit/references/` directory
2. Copy `docs/workflows/micro-commit.md` to `references/workflow.md`
3. Update `SKILL.md` frontmatter (remove Claude-specific fields)
4. Update `SKILL.md` body with inline instructions
5. Add reference to `references/workflow.md`
6. Validate and test
7. Commit changes

**Success Criteria:**
- [ ] Same as Task 1

---

### Task 3: Migrate tdd-enforcement Skill

**Objective:** Apply pattern to tdd-enforcement skill

**Steps:** Same as Task 2

---

### Task 4: Migrate code-quality Skill

**Objective:** Migrate code-quality skill

**Note:** This skill may not have a canonical contract - verify

**Steps:**
1. Check if canonical contract exists in `docs/workflows/`
2. If yes, migrate as Tasks 2-3
3. If no, just update frontmatter and ensure self-contained

---

### Task 5: Migrate commit-review Skill

**Objective:** Migrate commit-review skill

**Steps:** Same pattern as above

---

### Task 6: Migrate refactoring-gate Skill

**Objective:** Migrate refactoring-gate skill

**Steps:** Same pattern as above

---

### Task 7: Migrate spec-compliance Skill

**Objective:** Migrate spec-compliance skill

**Steps:** Same pattern as above

---

### Task 8: Migrate static-analysis-gate Skill

**Objective:** Migrate static-analysis-gate skill

**Steps:** Same pattern as above

---

### Task 9: Migrate test-coverage Skill

**Objective:** Migrate test-coverage skill

**Steps:** Same pattern as above

---

### Task 10: Update Enforcement Tests

**Objective:** Update test suite to validate Agent Skills compliance

**Steps:**
1. Review `tests/enforcement_integration/test_enforcement_gates.py`
2. Update `validate_contract_references()` - remove or modify
3. Update `validate_hard_gate_semantics()` - adapt for inline content
4. Add `validate_agent_skills_structure()` - check frontmatter compliance
5. Add `validate_skill_references()` - verify references/ folder files exist
6. Update test fixtures if needed
7. Run full test suite
8. Commit changes

**Success Criteria:**
- [ ] Tests validate Agent Skills frontmatter (name, description only)
- [ ] Tests validate references/ folder structure
- [ ] Tests validate SKILL.md line count (under 500)
- [ ] All tests pass
- [ ] Committed with clear message

---

### Task 11: Update CONTRIBUTING-SKILLS.md

**Objective:** Update contribution guidelines for Agent Skills

**Steps:**
1. Read current `docs/CONTRIBUTING-SKILLS.md`
2. Update "Contract Structure" section to "Skill Structure"
3. Remove references to canonical contracts
4. Add Agent Skills frontmatter requirements
5. Add progressive disclosure guidelines
6. Update "Adapter Mapping" section (remove or repurpose)
7. Update "Enforcement Testing" section
8. Commit changes

**Success Criteria:**
- [ ] Guidelines reflect Agent Skills spec
- [ ] No references to canonical contracts
- [ ] Clear frontmatter requirements documented
- [ ] Committed with clear message

---

### Task 12: Update README.md

**Objective:** Update project README to reflect new architecture

**Steps:**
1. Read current `README.md`
2. Update "What Gets Enforced" section if needed
3. Update "Project Structure" section
4. Update "Tool-Specific Features" section (Claude skills description)
5. Update "Workflow Parity Matrix" (remove or adapt)
6. Add note about Agent Skills compliance
7. Commit changes

**Success Criteria:**
- [ ] README accurately describes new structure
- [ ] No outdated references to canonical contracts
- [ ] Committed with clear message

---

### Task 13: Deprecate or Archive Canonical Contracts

**Objective:** Handle old canonical contracts

**Options:**
A. **Keep for reference** (recommended for learning)
   - Move `docs/workflows/` to `docs/archived-workflows/`
   - Add README explaining they're historical
   
B. **Remove entirely**
   - Delete `docs/workflows/` directory
   - Update any remaining references

**Steps:**
1. Decide on approach (recommend Option A for learning)
2. Execute chosen approach
3. Update any cross-references
4. Commit changes

---

## Task Dependencies

```
Task 1 (pre-commit PoC)
    ↓
Tasks 2-9 (other skills - can be parallel after PoC)
    ↓
Task 10 (tests - depends on all skills)
    ↓
Tasks 11-12 (documentation - depends on Task 10)
    ↓
Task 13 (archive - last)
```

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Tests break during migration | Run tests after each skill; fix immediately |
| Content too long for SKILL.md | Use progressive disclosure; move to references/ |
| Loss of centralized workflow updates | Document as intentional trade-off |
| User confusion about new structure | Update README and CONTRIBUTING clearly |

## Success Metrics

- All 9 skills migrated to Agent Skills compliance
- All tests pass
- Documentation updated
- No functionality lost
- Project builds successfully

## Rollback Plan

If issues arise:
1. Git history preserves old structure
2. Can revert individual skill commits
3. Canonical contracts preserved (Option A)

---

*Phase: 03-agent-skills-plan*
*Plan created: 2026-03-22*

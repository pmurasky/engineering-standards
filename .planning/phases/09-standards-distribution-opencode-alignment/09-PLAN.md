# Phase 9: Standards Distribution & OpenCode Alignment - Execution Plan

**Planned:** 2026-04-27
**Status:** Ready for execution

## Overview

Improve `engineering-standards` so downstream projects can adopt and update it with a simple, reviewable workflow while keeping the repo file-based rather than plugin-first. Align the OpenCode story with current repo reality by adding native skill-pack support where appropriate, correcting documentation, and making install/update ergonomics a first-class feature.

## Planning Basis

This plan is based on the completed audit and repo verification:

- `README.md` currently relies on copy, submodule, and symlink flows.
- `opencode.json` already treats standards as `instructions` and uses plugins only for executable tooling.
- `.claude/skills/` exists, but `.opencode/skills/` does not.
- `README.md` implies OpenCode skills in places that do not match the current tree.
- `Makefile` does not provide downstream bootstrap or update commands.
- Ecosystem research shows convergence on committed file packs, portable skills, and one-command init/update workflows.

## Strategy

**Primary model:** file-based standards pack committed into each consuming repo  
**Secondary model:** reviewable update path using versioned source sync or vendored refresh  
**Plugin role:** optional runtime behavior only, not primary standards distribution  
**Execution style:** ship automation first, then align OpenCode packaging and docs around that automation

## Detailed Tasks

### Task 1: Define Supported Consumer Installation Modes

**Objective:** Establish one canonical install path and clearly demote legacy/manual alternatives.

**Steps:**
1. Define the default downstream installation model for this repo.
2. Decide which alternatives remain supported: copy, submodule, subtree/vendor sync, symlink.
3. Document support tiers such as recommended, advanced, and legacy/manual.
4. Ensure the chosen model respects ADR constraints on upstream sync architecture.
5. Record decision points in docs or ADR-style notes if needed.

**Success Criteria:**
- [ ] One default install story is chosen
- [ ] Alternative flows have explicit support status
- [ ] No conflict with `0001-superpowers-upstream-sync-model.md`

---

### Task 2: Design One-Command Init Workflow

**Objective:** Specify the bootstrap command that installs standards into a downstream repo with minimal manual work.

**Steps:**
1. Define command surface, expected arguments, and target repo assumptions.
2. Decide which files are copied, generated, or linked during init.
3. Define behavior for empty repo vs existing repo.
4. Define idempotency rules and safe re-run behavior.
5. Define conflict handling for existing `AGENTS.md`, `opencode.json`, `.opencode/`, and `.claude/` content.

**Success Criteria:**
- [ ] Init command contract is explicit
- [ ] Existing-project merge behavior is defined
- [ ] Idempotency and conflict rules are documented

---

### Task 3: Design One-Command Update Workflow

**Objective:** Specify how downstream repos safely adopt newer `engineering-standards` versions.

**Steps:**
1. Decide whether updates are tag-based, branch-based, or file-manifest-based.
2. Define how the update command detects installed provenance/version.
3. Define preview/dry-run behavior before overwriting files.
4. Define how local downstream customizations are preserved or flagged.
5. Define rollback expectations and failure behavior.

**Success Criteria:**
- [ ] Update flow is reviewable and safe
- [ ] Version/provenance tracking approach is chosen
- [ ] Dry-run or preview behavior is defined

---

### Task 4: Add OpenCode-Native Skills Packaging Plan

**Objective:** Bring the repo’s OpenCode packaging in line with its documented portability story.

**Steps:**
1. Inventory which existing Claude skills should gain OpenCode-native counterparts.
2. Decide whether `.opencode/skills/` should mirror, adapt, or index existing skill content.
3. Keep `docs/` as source of truth where possible, avoiding unnecessary duplication.
4. Define how OpenCode skills relate to existing `instructions`, `commands`, and `agents`.
5. Set validation rules so docs never claim skills that are absent from the tree.

**Success Criteria:**
- [ ] `.opencode/skills/` direction is explicit
- [ ] Relationship to `.claude/skills/` is defined
- [ ] Source-of-truth rules avoid drift

---

### Task 5: Specify Installer/Updater Implementation Surface

**Objective:** Decide where the automation lives and how contributors invoke it.

**Steps:**
1. Choose implementation surface: `scripts/`, `Makefile`, both, or another minimal wrapper.
2. Define required runtime assumptions (shell, Python, Node, etc.).
3. Define manifest or file list used by install/update commands.
4. Decide whether generated wrapper files should be templated.
5. Define testability expectations for automation logic.

**Success Criteria:**
- [ ] Implementation surface chosen
- [ ] Runtime assumptions are minimal and documented
- [ ] File manifest strategy is defined

---

### Task 6: Rewrite Consumer Documentation Around the New Flow

**Objective:** Make README and related docs reflect the actual supported install/update story.

**Steps:**
1. Rewrite README install section around the canonical init/update workflow.
2. Fix the OpenCode skills mismatch in README and compatibility guidance.
3. Update project structure examples to include only files that actually exist.
4. Document advanced/manual alternatives separately from the default flow.
5. Add versioned update examples and troubleshooting guidance.

**Success Criteria:**
- [ ] README matches repo contents
- [ ] Recommended flow is obvious in first read
- [ ] OpenCode packaging claims are accurate

---

### Task 7: Add Validation Coverage for Distribution Integrity

**Objective:** Prevent future drift between docs, manifests, and actual packaged files.

**Steps:**
1. Add tests or validation scripts for installer manifest integrity.
2. Add checks ensuring README file lists match repo structure.
3. Add checks ensuring claimed OpenCode skills exist when documented.
4. Add tests for init/update dry-run behavior where practical.
5. Define minimal CI gates for packaging correctness.

**Success Criteria:**
- [ ] Packaging drift is test-detectable
- [ ] Docs-to-tree mismatches are caught automatically
- [ ] Installer/update behavior has regression protection

---

## Proposed Execution Order

1. Task 1 - installation model decision
2. Task 2 - init workflow contract
3. Task 3 - update workflow contract
4. Task 5 - implementation surface decision
5. Task 4 - OpenCode-native skills packaging decision
6. Task 7 - validation coverage
7. Task 6 - final documentation rewrite

## Dependency Notes

- Task 6 depends on Tasks 1-5 because docs should follow the actual supported model.
- Task 7 depends on Tasks 2-5 because validation must reflect real installer/update behavior.
- Task 4 should complete before final README rewrite so OpenCode claims are accurate.

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Installer overwrites consumer customizations | Add preview mode, explicit conflict handling, and provenance tracking |
| Docs drift from packaged files | Add validation for file manifests and README claims |
| OpenCode skills duplicate too much content | Keep `docs/` as source of truth where feasible and use clear generation/adaptation rules |
| Too many supported installation modes confuse users | Promote one canonical flow and label others advanced/manual |
| Update story conflicts with upstream sync ADR | Keep ADR scoped to upstream mirror architecture and use downstream sync only as consumer UX |

## Success Metrics

- A downstream repo can install standards with one documented command
- A downstream repo can update standards with one documented command or workflow
- OpenCode packaging is accurate and discoverable
- README matches the actual repo tree and supported behavior
- Validation catches future packaging/documentation drift

## Rollback Plan

If execution reveals flaws:
1. Revert installer/update automation independently from docs
2. Keep manual copy flow documented as fallback until automation is stable
3. Ship OpenCode packaging and installer changes in separate micro-commits for safe rollback

---

*Phase: 09-standards-distribution-opencode-alignment*
*Plan created: 2026-04-27*

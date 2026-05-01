# S01: Plan Distribution

**Goal:** Improve engineering-standards so downstream projects can adopt and update it with a simple, reviewable workflow while keeping the repo file-based rather than plugin-first.
**Demo:** Distribution plan documented and ready for execution

## Must-Haves

- Not provided.

## Proof Level

- This slice proves: Not provided.

## Integration Closure

Not provided.

## Verification

- Not provided.

## Tasks

- [ ] **T01: Define Supported Consumer Installation Modes** `est:2h`
  Establish one canonical install path and clearly demote legacy/manual alternatives.

Steps:
1. Define the default downstream installation model for this repo.
2. Decide which alternatives remain supported: copy, submodule, subtree/vendor sync, symlink.
3. Document support tiers such as recommended, advanced, and legacy/manual.
4. Ensure the chosen model respects ADR constraints on upstream sync architecture.
5. Record decision points in docs or ADR-style notes if needed.

Success Criteria:
- One default install story is chosen
- Alternative flows have explicit support status
- No conflict with 0001-superpowers-upstream-sync-model.md
  - Files: `docs/adr/`, `README.md`
  - Verify: Installation model documented and ADR constraints verified

- [ ] **T02: Design One-Command Init Workflow** `est:2h`
  Specify the bootstrap command that installs standards into a downstream repo with minimal manual work.

Steps:
1. Define command surface, expected arguments, and target repo assumptions.
2. Decide which files are copied, generated, or linked during init.
3. Define behavior for empty repo vs existing repo.
4. Define idempotency rules and safe re-run behavior.
5. Define conflict handling for existing AGENTS.md, opencode.json, .opencode/, and .claude/ content.

Success Criteria:
- Init command contract is explicit
- Existing-project merge behavior is defined
- Idempotency and conflict rules are documented
  - Files: `scripts/`, `Makefile`, `README.md`
  - Verify: Init workflow documented with command contract and conflict handling

- [ ] **T03: Design One-Command Update Workflow** `est:2h`
  Specify how downstream repos safely adopt newer engineering-standards versions.

Steps:
1. Decide whether updates are tag-based, branch-based, or file-manifest-based.
2. Define how the update command detects installed provenance/version.
3. Define preview/dry-run behavior before overwriting files.
4. Define how local downstream customizations are preserved or flagged.
5. Define rollback expectations and failure behavior.

Success Criteria:
- Update flow is reviewable and safe
- Version/provenance tracking approach is chosen
- Dry-run or preview behavior is defined
  - Files: `scripts/`, `Makefile`, `README.md`
  - Verify: Update workflow documented with safety rules and rollback plan

- [ ] **T04: Add OpenCode-Native Skills Packaging Plan** `est:2h`
  Bring the repo's OpenCode packaging in line with its documented portability story.

Steps:
1. Inventory which existing Claude skills should gain OpenCode-native counterparts.
2. Decide whether .opencode/skills/ should mirror, adapt, or index existing skill content.
3. Keep docs/ as source of truth where possible, avoiding unnecessary duplication.
4. Define how OpenCode skills relate to existing instructions, commands, and agents.
5. Set validation rules so docs never claim skills that are absent from the tree.

Success Criteria:
- .opencode/skills/ direction is explicit
- Relationship to .claude/skills/ is defined
- Source-of-truth rules avoid drift
  - Files: `.opencode/`, `.claude/`, `README.md`
  - Verify: OpenCode packaging plan documented with skill inventory and source-of-truth rules

- [ ] **T05: Specify Installer/Updater Implementation Surface** `est:2h`
  Decide where the automation lives and how contributors invoke it.

Steps:
1. Choose implementation surface: scripts/, Makefile, both, or another minimal wrapper.
2. Define required runtime assumptions (shell, Python, Node, etc.).
3. Define manifest or file list used by install/update commands.
4. Decide whether generated wrapper files should be templated.
5. Define testability expectations for automation logic.

Success Criteria:
- Implementation surface chosen
- Runtime assumptions are minimal and documented
- File manifest strategy is defined
  - Files: `scripts/`, `Makefile`, `package.json`
  - Verify: Implementation surface chosen with runtime assumptions and manifest strategy

- [ ] **T06: Rewrite Consumer Documentation Around the New Flow** `est:3h`
  Make README and related docs reflect the actual supported install/update story.

Steps:
1. Rewrite README install section around the canonical init/update workflow.
2. Fix the OpenCode skills mismatch in README and compatibility guidance.
3. Update project structure examples to include only files that actually exist.
4. Document advanced/manual alternatives separately from the default flow.
5. Add versioned update examples and troubleshooting guidance.

Success Criteria:
- README matches repo contents
- Recommended flow is obvious in first read
- OpenCode packaging claims are accurate
  - Files: `README.md`, `docs/`
  - Verify: README updated with accurate install/update flow and OpenCode claims

- [ ] **T07: Add Validation Coverage for Distribution Integrity** `est:3h`
  Prevent future drift between docs, manifests, and actual packaged files.

Steps:
1. Add tests or validation scripts for installer manifest integrity.
2. Add checks ensuring README file lists match repo structure.
3. Add checks ensuring claimed OpenCode skills exist when documented.
4. Add tests for init/update dry-run behavior where practical.
5. Define minimal CI gates for packaging correctness.

Success Criteria:
- Packaging drift is test-detectable
- Docs-to-tree mismatches are caught automatically
- Installer/update behavior has regression protection
  - Files: `tests/`, `.github/workflows/`, `scripts/`
  - Verify: Validation scripts added and CI gates defined

## Files Likely Touched

- docs/adr/
- README.md
- scripts/
- Makefile
- .opencode/
- .claude/
- package.json
- docs/
- tests/
- .github/workflows/

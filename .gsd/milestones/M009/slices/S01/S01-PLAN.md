# S01: Plan Distribution

**Goal:** Produce a complete, written distribution plan covering installation modes, init/update workflow design, OpenCode skills packaging decisions, implementation surface spec, documentation rewrites, and validation coverage.
**Demo:** Consumer can follow a single documented workflow to install or update engineering-standards in their project; validation tests confirm distribution integrity; README accurately reflects the file-based model.

## Must-Haves

- All 7 tasks completed and committed; ADR written for installation mode; init and update workflow specs exist; OpenCode skills source-of-truth decision documented; implementation surface defined; README updated; validation tests exist and pass in CI.

## Proof Level

- This slice proves: Documentation artifact review + green test run for validation coverage added in T07.

## Integration Closure

Single slice in M009; no cross-slice integration required. Outputs consumed by future execution milestones.

## Verification

- Validation tests created in T07 provide ongoing CI-level visibility into distribution integrity on every future commit.

## Tasks

- [ ] **T01: Define Supported Consumer Installation Modes** `est:2h`
  Identify every realistic way a downstream project can consume engineering-standards (git submodule, sparse-checkout, script-based copy, npm install, manual copy). For each mode, document: installation steps, update mechanism, tooling requirements, tradeoffs, and which consumer types (CI-only, developer workstation, agent-only) it suits. Write an ADR capturing the recommended mode with alternatives considered. Include support tiers: Recommended (first-class, documented, tested), Advanced (supported but not hand-held), Legacy (documented, not maintained).
  - Files: `docs/adr/`, `docs/distribution/installation-modes.md`, `README.md`
  - Verify: ADR file exists with status:Accepted; installation-modes.md lists ≥2 modes with tradeoffs; README references the canonical mode.

- [ ] **T02: Design One-Command Init Workflow** `est:2h`
  Design the surface of a one-command init workflow for first-time consumers. Specify: command name and args (e.g. `make init` or `scripts/init.sh`), what files it creates (AGENTS.md, .opencode/skills/*, .claude/skills/*, docs/ symlinks or copies), idempotency rules, conflict detection for pre-existing files (merge vs skip vs error), dry-run flag behavior, and post-init verification step. Document the decision as a spec in docs/distribution/init-workflow.md.
  - Files: `docs/distribution/init-workflow.md`, `scripts/`, `Makefile`
  - Verify: docs/distribution/init-workflow.md exists; covers command surface, file manifest, idempotency, conflict rules, and dry-run; ≥3 consumer scenarios documented.

- [ ] **T03: Design One-Command Update Workflow** `est:2h`
  Design the surface of a one-command update workflow for existing consumers. Specify: how the tool detects the installed version (git tag, manifest file, SHA), what a dry-run shows (diff of changed files), how local customizations are preserved (merge strategy, user-owned sections, overwrite allowlist), rollback procedure if update breaks something, and whether updates are tag-based, branch-tracking, or manifest-driven. Document as docs/distribution/update-workflow.md.
  - Files: `docs/distribution/update-workflow.md`, `scripts/`, `Makefile`
  - Verify: docs/distribution/update-workflow.md exists; covers version detection, dry-run, local customization preservation, and rollback; update command surface is specified.

- [ ] **T04: Add OpenCode-Native Skills Packaging Plan** `est:2h`
  Inventory all skills in .opencode/skills/ and .claude/skills/. Decide and document: which directory is the source of truth, whether .opencode/skills/ and .claude/skills/ should be identical (symlinked, generated, or independently maintained), what happens during init/update for each. Note the M010 plugin model as an alternative and state explicitly whether file-based or plugin-based is the recommended path for skill delivery. Write the decision as an addition to the distribution ADR or a dedicated section.
  - Files: `docs/distribution/skills-packaging.md`, `docs/adr/`, `.opencode/skills/`, `.claude/skills/`
  - Verify: skills-packaging.md or ADR section exists; source-of-truth directory named; sync rules stated; M010 plugin model addressed explicitly.

- [ ] **T05: Specify Installer/Updater Implementation Surface** `est:2h`
  Specify the implementation surface for the installer and updater: will they be shell scripts in scripts/, a Makefile, a Node.js CLI, or a combination? Document: runtime assumptions (bash version, git version, curl/wget, node optional), the complete file manifest (every file touched by init and every file touched by update), error handling expectations (exit codes, user-facing messages), and how the implementation will be tested (unit tests for scripts, integration test with a temp consuming project). Produce docs/distribution/implementation-surface.md.
  - Files: `docs/distribution/implementation-surface.md`, `scripts/`, `Makefile`
  - Verify: docs/distribution/implementation-surface.md exists; runtime assumptions listed; file manifest complete; testability plan present.

- [ ] **T06: Rewrite Consumer Documentation Around the New Flow** `est:3h`
  Rewrite the README install section to accurately reflect the new file-based distribution model. Remove or update any claims about OpenCode plugin installation that are inaccurate. Add: quick-start showing the one-command init, update section with the one-command update, versioning section linking to tags/releases, and a link to docs/distribution/ for deeper detail. Verify no dead links.
  - Files: `README.md`, `docs/distribution/`
  - Verify: README install section rewritten; quick-start present; update workflow documented; no dead links (run linkcheck or manual scan); content matches file-based model.

- [ ] **T07: Add Validation Coverage for Distribution Integrity** `est:3h`
  Add a validation test suite (in tests/validation/ or tests/distribution/) that checks: (1) every file listed in the install manifest actually exists in the repo, (2) README install section references files that exist, (3) .opencode/skills/ and .claude/skills/ are in sync per the source-of-truth rules from T04, (4) all referenced ADRs exist, (5) CI workflow file triggers validation on push. Tests should be runnable with a single command (e.g. `make validate` or `pytest tests/validation/`). Wire into the CI pipeline.
  - Files: `tests/validation/`, `.github/workflows/`, `Makefile`
  - Verify: tests/validation/ exists with ≥4 validation checks; `make validate` or equivalent runs all checks; CI workflow includes validation step; all checks pass on current repo state.

## Files Likely Touched

- docs/adr/
- docs/distribution/installation-modes.md
- README.md
- docs/distribution/init-workflow.md
- scripts/
- Makefile
- docs/distribution/update-workflow.md
- docs/distribution/skills-packaging.md
- .opencode/skills/
- .claude/skills/
- docs/distribution/implementation-surface.md
- docs/distribution/
- tests/validation/
- .github/workflows/

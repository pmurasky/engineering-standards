# S02: Create Plugin Manifest and Structure

**Goal:** Author the plugin manifest and establish the canonical plugin directory structure for engineering-standards based on S01 research findings.
**Demo:** opencode.json or equivalent manifest file exists and validates against the OpenCode plugin schema; directory structure matches plugin conventions.

## Must-Haves

- Plugin manifest file created and valid; directory structure matches OpenCode plugin spec from S01; no validation errors; CI validation step added.

## Proof Level

- This slice proves: Plugin manifest validation passes (opencode validate or npm pack dry-run); no schema errors.

## Integration Closure

Provides the plugin scaffold consumed by S03 (resources registration) and S04 (skills wiring).

## Verification

- Plugin manifest validation step added to CI — any future structural breakage surfaces immediately.

## Tasks

- [ ] **T01: Create Plugin Manifest File** `est:1h`
  Using the research doc from M010/S01, create or update the plugin manifest file (opencode.json or package.json with opencode fields). Populate all required fields: name (@pmurasky/engineering-standards), version, description, plugin type, entry points for skills/agents/commands/resources. Verify the manifest against the OpenCode plugin schema using whatever validation tool is available (opencode validate, JSON schema check, or manual review against docs).
  - Files: `opencode.json`, `package.json`, `.opencode/package.json`
  - Verify: Manifest file exists with all required fields populated; opencode validate (or equivalent) exits 0; no schema errors.

- [ ] **T02: Establish Canonical Plugin Directory Structure** `est:45m`
  Audit the current directory structure against the OpenCode plugin conventions documented in S01. Move, rename, or create directories as needed so the layout matches plugin expectations. Document any intentional deviations. Ensure .opencode/skills/, .opencode/agents/, .opencode/commands/ are all present and non-empty (or explicitly empty with a reason). Run a tree of the final structure and include it in the research doc or a new docs/plugin-structure.md.
  - Files: `.opencode/`, `docs/plugin-structure.md`
  - Verify: Directory structure matches plugin spec; docs/plugin-structure.md exists and shows the tree; no missing required directories.

- [ ] **T03: Add Manifest Validation to CI** `est:30m`
  Add a CI workflow step (or update existing) that runs plugin manifest validation on every push and pull request. The step should: (1) install any required OpenCode CLI or validation tooling, (2) run validation against the manifest, (3) fail the build if the manifest is invalid. If no dedicated validation tool exists, write a lightweight JSON schema check script.
  - Files: `.github/workflows/`, `scripts/validate-manifest.sh`
  - Verify: CI workflow includes manifest validation step; step passes on current repo state; a deliberate manifest error causes step to fail (verified by dry-run or local test).

## Files Likely Touched

- opencode.json
- package.json
- .opencode/package.json
- .opencode/
- docs/plugin-structure.md
- .github/workflows/
- scripts/validate-manifest.sh

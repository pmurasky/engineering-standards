# S03: Package Standards Documents as Plugin Resources

**Goal:** Wire all docs/ standards documents into the plugin as accessible resources so consuming projects can reference them via the OpenCode plugin API without manual file copying.
**Demo:** At least one standards doc (e.g. CODING_PRACTICES.md) is accessible via the plugin resource API in a consuming project.

## Must-Haves

- All docs/ files registered in plugin manifest; resource loading tested and confirmed working; enforcement tests updated to include resource reference checks; no broken resource references.

## Proof Level

- This slice proves: Integration test or manual verification that at least one resource loads from a consuming project after plugin install.

## Integration Closure

Resources registered in S02 manifest scaffold; resource availability verified in S05 documentation walkthrough.

## Verification

- Resource loading errors surface during plugin install; validation test added to enforcement suite to detect broken resource references.

## Tasks

- [ ] **T01: Inventory Standards Documents for Resource Registration** `est:45m`
  Enumerate every file in docs/ that should be exposed as a plugin resource. For each file, determine: (1) whether it should be exposed as a named resource or glob-included, (2) what the consumer-facing resource identifier should be (e.g. `engineering-standards/CODING_PRACTICES`), (3) whether any docs/ files should be excluded (drafts, templates that aren't consumer-facing). Produce a resource manifest inventory as a markdown table.
  - Files: `docs/resource-inventory.md`, `docs/`
  - Verify: docs/resource-inventory.md exists; all docs/ files accounted for; each file has a resource ID or an explicit exclusion reason.

- [ ] **T02: Register Standards Documents in Plugin Manifest** `est:30m`
  Register all included docs/ files in the plugin manifest as resources using the format documented in S01 (glob pattern, explicit list, or directory registration). Update opencode.json or package.json with the resources section. Verify the manifest still validates after additions.
  - Files: `opencode.json`, `package.json`
  - Verify: Manifest resources section present; all docs/ files from T01 inventory registered; manifest validation passes.

- [ ] **T03: Verify Resource Loading and Add Enforcement Tests** `est:1.5h`
  Write and run a resource loading test. Create a minimal test consuming project (or use a temp directory) that installs the plugin and attempts to access at least 3 resources by their plugin resource IDs. Document the access pattern in docs/resource-inventory.md. Add a resource reference integrity check to the enforcement test suite (tests/enforcement_integration/ or tests/validation/) that verifies every registered resource file actually exists on disk.
  - Files: `tests/enforcement_integration/`, `tests/validation/`, `scripts/test-resource-loading.sh`
  - Verify: Resource loading test passes; enforcement test for resource existence added and green; at least 3 resources verified accessible via plugin API.

## Files Likely Touched

- docs/resource-inventory.md
- docs/
- opencode.json
- package.json
- tests/enforcement_integration/
- tests/validation/
- scripts/test-resource-loading.sh

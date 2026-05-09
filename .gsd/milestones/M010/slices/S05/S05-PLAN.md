# S05: Create Installation and Usage Documentation

**Goal:** Write complete installation and usage documentation so consumers can install the plugin, access skills and standards docs, and understand the update workflow — all within 5 minutes of reading the README.
**Demo:** New developer can follow README to install plugin and access a skill and a standards doc within 5 minutes.

## Must-Haves

- README install section updated with accurate plugin install command; usage examples for skills and resources present; update workflow documented; no dead links; walkthrough in clean project succeeds.

## Proof Level

- This slice proves: Manual walkthrough of install steps in a clean test project; README matches actual plugin behavior end-to-end.

## Integration Closure

Ties together all prior slices (S01 research, S02 manifest, S03 resources, S04 skills) into a consumer-facing narrative. Final integration point before milestone completion.

## Verification

- None — documentation slice. Manual walkthrough serves as the observability check.

## Tasks

- [ ] **T01: Rewrite README Installation Section** `est:1h`
  Rewrite the README installation section to accurately describe plugin-based installation. Include: (1) the exact install command (npm install / opencode plugin install / git-based), (2) what the consumer gets after install (skills listed, resources listed), (3) any required consumer-side config (from S04/T04), (4) a quick verification step the consumer can run to confirm installation worked. Remove or correct any stale claims about the old manual copy workflow if they conflict with the plugin model.
  - Files: `README.md`
  - Verify: README install section present with exact command; post-install verification step included; consumer config documented if required; no stale references to old workflow.

- [ ] **T02: Add Skill and Resource Usage Examples** `est:45m`
  Add a usage examples section to the README (or a dedicated docs/usage-guide.md) showing: (1) how to invoke a skill from an OpenCode session after installing the plugin, (2) how to access a standards document via the plugin resource API, (3) how to reference an agent. Include at least 2 concrete examples with expected output or user-visible result.
  - Files: `README.md`, `docs/usage-guide.md`
  - Verify: Usage examples section present with ≥2 skill examples and ≥1 resource example; examples are concrete (not placeholder); examples match actual plugin behavior.

- [ ] **T03: Document Plugin Update Workflow and Versioning** `est:30m`
  Document the plugin update workflow: how consumers update to a new version (npm update, opencode plugin update, or manual), how to pin to a specific version, and what to do if an update breaks their local configuration. Also add a versioning section explaining the semantic versioning scheme used by the plugin. Link to the update docs from the README.
  - Files: `README.md`, `docs/update-workflow.md`
  - Verify: Update section present; specific update command documented; versioning policy stated; link from README.

- [ ] **T04: End-to-End Walkthrough and Documentation QA** `est:1h`
  Perform an end-to-end walkthrough: starting from a clean directory, follow the README instructions to install the plugin, verify skills are available, access a resource, and trigger an update. Document any discrepancies found between the README and actual behavior and fix them. Run a dead-link check on the README and all docs/ files added in this milestone.
  - Files: `README.md`, `docs/`
  - Verify: Walkthrough completes without errors; README matches actual behavior; dead-link check passes; any discrepancies fixed and committed.

## Files Likely Touched

- README.md
- docs/usage-guide.md
- docs/update-workflow.md
- docs/

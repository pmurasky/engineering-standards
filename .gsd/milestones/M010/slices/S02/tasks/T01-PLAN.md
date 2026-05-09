---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T01: Create Plugin Manifest File

Using the research doc from M010/S01, create or update the plugin manifest file (opencode.json or package.json with opencode fields). Populate all required fields: name (@pmurasky/engineering-standards), version, description, plugin type, entry points for skills/agents/commands/resources. Verify the manifest against the OpenCode plugin schema using whatever validation tool is available (opencode validate, JSON schema check, or manual review against docs).

## Inputs

- `docs/research/opencode-plugin-architecture.md (S01 output)`
- `Existing package.json and .opencode/package.json`

## Expected Output

- `opencode.json or updated package.json with complete plugin manifest fields`
- `Validation output showing no errors`

## Verification

Manifest file exists with all required fields populated; opencode validate (or equivalent) exits 0; no schema errors.

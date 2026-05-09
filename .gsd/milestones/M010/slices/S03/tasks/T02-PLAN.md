---
estimated_steps: 1
estimated_files: 2
skills_used: []
---

# T02: Register Standards Documents in Plugin Manifest

Register all included docs/ files in the plugin manifest as resources using the format documented in S01 (glob pattern, explicit list, or directory registration). Update opencode.json or package.json with the resources section. Verify the manifest still validates after additions.

## Inputs

- `docs/resource-inventory.md (T01 output)`
- `S02 manifest file`

## Expected Output

- `Plugin manifest updated with resources section listing all docs/ files`
- `Manifest validation still passing`

## Verification

Manifest resources section present; all docs/ files from T01 inventory registered; manifest validation passes.

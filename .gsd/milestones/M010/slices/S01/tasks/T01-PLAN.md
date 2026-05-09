---
estimated_steps: 1
estimated_files: 1
skills_used: []
---

# T01: Read OpenCode Plugin Documentation

Read the official OpenCode plugin documentation. Extract and document: (1) plugin manifest format (file name, required fields, optional fields, schema), (2) expected directory structure for a plugin repo, (3) how skills are discovered and loaded by OpenCode from a plugin, (4) how agents are discovered and loaded, (5) how commands are registered, (6) how resource files (docs) are made accessible to consuming projects, (7) the installation mechanism (npm install, git, local path), (8) any versioning or update mechanism.

## Inputs

- `OpenCode official docs (https://opencode.ai/docs or equivalent)`
- `Existing .opencode/package.json if present`

## Expected Output

- `docs/research/opencode-plugin-architecture.md section: Plugin Manifest Format`
- `docs/research/opencode-plugin-architecture.md section: Directory Structure`
- `docs/research/opencode-plugin-architecture.md section: Skill/Agent/Command Discovery`
- `docs/research/opencode-plugin-architecture.md section: Resource Loading`
- `docs/research/opencode-plugin-architecture.md section: Installation Mechanism`

## Verification

docs/research/opencode-plugin-architecture.md exists and covers all 8 listed topics with specific field names and examples where available.

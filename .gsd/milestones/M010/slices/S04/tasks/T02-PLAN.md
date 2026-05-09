---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T02: Register Skills in Plugin Manifest

Register all .opencode/skills/ skills in the plugin manifest using the skill registration format from S01 research. Update opencode.json or package.json with the skills section. Verify manifest still validates. If skills require a specific directory structure or SKILL.md format to be discovered, adjust any non-conforming skills.

## Inputs

- `docs/skills-inventory.md (T01 output)`
- `S01 research doc on skill discovery format`
- `S02 manifest file`

## Expected Output

- `Plugin manifest updated with skills section`
- `Any non-conforming skills adjusted to match plugin discovery format`
- `Manifest validation passing`

## Verification

Manifest skills section present with all .opencode/skills/ entries; manifest validates; any adjusted skills still pass existing enforcement tests.

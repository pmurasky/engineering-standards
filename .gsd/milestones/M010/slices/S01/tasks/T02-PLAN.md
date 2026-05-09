---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T02: Map Existing Files to Plugin Structure

Map every existing project file to its role in the plugin model. For each category, note whether the existing file is compatible, needs renaming/moving, or is a gap requiring new content: .opencode/skills/* → plugin skills; .opencode/agents/* → plugin agents; .opencode/commands/* → plugin commands; docs/*.md → plugin resources; .opencode/package.json → plugin manifest (check if exists and if fields are correct); .claude/skills/* → determine if these should also be exposed or are Claude-only. Produce a compatibility matrix.

## Inputs

- `T01 research doc (plugin structure understanding)`
- `ls .opencode/skills/ .opencode/agents/ .opencode/commands/ .claude/skills/ docs/`

## Expected Output

- `docs/research/opencode-plugin-architecture.md section: File Mapping and Compatibility Matrix`

## Verification

Compatibility matrix section present in research doc; every existing .opencode/ file category accounted for; gaps explicitly listed.

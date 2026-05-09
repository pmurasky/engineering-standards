# S01: Research OpenCode Plugin Architecture

**Goal:** Read official OpenCode plugin documentation and map existing project files to the plugin model; produce a research document that unblocks plugin manifest creation in S02.
**Demo:** Research doc exists at docs/research/opencode-plugin-architecture.md covering manifest format, directory structure, skill/agent/command discovery, resource loading, and installation mechanism.

## Must-Haves

- Research doc committed at docs/research/opencode-plugin-architecture.md; manifest format understood; existing .opencode/ files mapped to plugin structure; gaps between current structure and plugin requirements identified.

## Proof Level

- This slice proves: Artifact review — research doc readable, committed, and covers all required sections.

## Integration Closure

Output (research doc) is the primary input for S02 plugin manifest creation and S04 skills wiring decisions.

## Verification

- None — pure research slice. No runtime surfaces introduced.

## Tasks

- [ ] **T01: Read OpenCode Plugin Documentation** `est:30m`
  Read the official OpenCode plugin documentation. Extract and document: (1) plugin manifest format (file name, required fields, optional fields, schema), (2) expected directory structure for a plugin repo, (3) how skills are discovered and loaded by OpenCode from a plugin, (4) how agents are discovered and loaded, (5) how commands are registered, (6) how resource files (docs) are made accessible to consuming projects, (7) the installation mechanism (npm install, git, local path), (8) any versioning or update mechanism.
  - Files: `docs/research/opencode-plugin-architecture.md`
  - Verify: docs/research/opencode-plugin-architecture.md exists and covers all 8 listed topics with specific field names and examples where available.

- [ ] **T02: Map Existing Files to Plugin Structure** `est:15m`
  Map every existing project file to its role in the plugin model. For each category, note whether the existing file is compatible, needs renaming/moving, or is a gap requiring new content: .opencode/skills/* → plugin skills; .opencode/agents/* → plugin agents; .opencode/commands/* → plugin commands; docs/*.md → plugin resources; .opencode/package.json → plugin manifest (check if exists and if fields are correct); .claude/skills/* → determine if these should also be exposed or are Claude-only. Produce a compatibility matrix.
  - Files: `docs/research/opencode-plugin-architecture.md`, `.opencode/`, `.claude/skills/`
  - Verify: Compatibility matrix section present in research doc; every existing .opencode/ file category accounted for; gaps explicitly listed.

- [ ] **T03: Document Findings and Unblocking Plan** `est:20m`
  Write the findings summary and planning section of the research doc. Produce: (1) a clear statement of what needs to be created/modified to turn this repo into a valid OpenCode plugin, (2) open questions that S02–S05 will need to resolve, (3) a draft installation command for consuming projects (e.g. `opencode plugin install @pmurasky/engineering-standards` or npm-based), (4) notes on whether skills/agents/commands auto-load or require consumer-side config, (5) recommended approach for making docs/ accessible. Commit the complete research doc.
  - Files: `docs/research/opencode-plugin-architecture.md`
  - Verify: Findings and Plan section committed; open questions listed; draft install command written; auto-load vs manual config question answered or flagged; research doc is complete and self-contained.

## Files Likely Touched

- docs/research/opencode-plugin-architecture.md
- .opencode/
- .claude/skills/

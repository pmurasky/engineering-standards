---
estimated_steps: 1
estimated_files: 2
skills_used: []
---

# T02: Establish Canonical Plugin Directory Structure

Audit the current directory structure against the OpenCode plugin conventions documented in S01. Move, rename, or create directories as needed so the layout matches plugin expectations. Document any intentional deviations. Ensure .opencode/skills/, .opencode/agents/, .opencode/commands/ are all present and non-empty (or explicitly empty with a reason). Run a tree of the final structure and include it in the research doc or a new docs/plugin-structure.md.

## Inputs

- `docs/research/opencode-plugin-architecture.md (S01 output)`
- `Current .opencode/ directory tree`

## Expected Output

- `Directory structure matching OpenCode plugin spec`
- `docs/plugin-structure.md showing final layout with explanations`

## Verification

Directory structure matches plugin spec; docs/plugin-structure.md exists and shows the tree; no missing required directories.

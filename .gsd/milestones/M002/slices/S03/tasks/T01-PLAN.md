---
estimated_steps: 6
estimated_files: 5
skills_used: []
---

# T01: Grep all active references to docs/workflows/

Grep all active config paths for references to docs/workflows/:
- .claude/ (agents, rules, skills)
- .opencode/ (agents, commands, skills)
- AGENTS.md, CLAUDE.md, README.md
List every file that contains 'docs/workflows' and the line content.
Classify each as: ACTIVE (needs updating) vs INFORMATIONAL (ok to leave or delete).

## Inputs

- None specified.

## Expected Output

- `Full list of docs/workflows/ references with file:line and classification`

## Verification

grep -r 'docs/workflows' . --include='*.md' --include='*.json' -- shows full list; classification written

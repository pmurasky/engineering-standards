---
estimated_steps: 6
estimated_files: 1
skills_used: []
---

# T01: Update README.md

Update README.md:
1. Agent Skills Matrix section: verify all 9 skills listed; update 'references' column if any skills now have references/ folders
2. Remove or annotate any mention of docs/workflows/ as active source of truth; update to 'historical archive'
3. Add a 'Testing' or 'CI' section noting that push/PR triggers enforcement tests via GitHub Actions
4. Verify the Plugin Architecture section still accurate after M002

Commit: `docs(readme): update post-M002 Agent Skills Matrix and CI section`

## Inputs

- `.claude/skills/`
- `.opencode/skills/`
- `.github/workflows/ci.yml`

## Expected Output

- `README.md updated with accurate matrix, CI mention, archival note`

## Verification

Manual review: all 9 skills in matrix, CI section present, docs/workflows/ not referenced as active

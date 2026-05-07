---
estimated_steps: 1
estimated_files: 2
skills_used: []
---

# T06: Rewrite Consumer Documentation Around the New Flow

Rewrite the README install section to accurately reflect the new file-based distribution model. Remove or update any claims about OpenCode plugin installation that are inaccurate. Add: quick-start showing the one-command init, update section with the one-command update, versioning section linking to tags/releases, and a link to docs/distribution/ for deeper detail. Verify no dead links.

## Inputs

- `T02 init spec`
- `T03 update spec`
- `T04 skills packaging decision`
- `Current README.md`

## Expected Output

- `README.md with accurate install section, quick-start, update workflow, and versioning; no dead links`

## Verification

README install section rewritten; quick-start present; update workflow documented; no dead links (run linkcheck or manual scan); content matches file-based model.

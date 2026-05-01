---
estimated_steps: 11
estimated_files: 2
skills_used: []
---

# T01: Define Supported Consumer Installation Modes

Establish one canonical install path and clearly demote legacy/manual alternatives.

Steps:
1. Define the default downstream installation model for this repo.
2. Decide which alternatives remain supported: copy, submodule, subtree/vendor sync, symlink.
3. Document support tiers such as recommended, advanced, and legacy/manual.
4. Ensure the chosen model respects ADR constraints on upstream sync architecture.
5. Record decision points in docs or ADR-style notes if needed.

Success Criteria:
- One default install story is chosen
- Alternative flows have explicit support status
- No conflict with 0001-superpowers-upstream-sync-model.md

## Inputs

- `.planning/phases/09-standards-distribution-opencode-alignment/09-PLAN.md`

## Expected Output

- `Installation mode decision document`

## Verification

Installation model documented and ADR constraints verified

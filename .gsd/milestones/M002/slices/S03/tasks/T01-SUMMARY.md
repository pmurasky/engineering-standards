---
id: T01
parent: S03
milestone: M002
key_files:
  - (none)
key_decisions:
  - (none)
duration: 
verification_result: untested
completed_at: 2026-05-09T00:31:20.968Z
blocker_discovered: false
---

# T01: Grep'd all active references to docs/workflows/ and catalogued them across test infrastructure, scripts, schemas, CI, commands, and docs.

**Grep'd all active references to docs/workflows/ and catalogued them across test infrastructure, scripts, schemas, CI, commands, and docs.**

## What Happened

Ran comprehensive grep across the codebase to find all active references to docs/workflows/. Found references in:
- .opencode/commands/ (2 files)
- tests/enforcement_integration/ (5 test files + helpers.py + README)
- scripts/ (3 scripts + 2 baseline JSON files)
- schemas/ (2 JSON schema files)
- upstream/superpowers.lock.json
- .github/workflows/contract-adapter-impact.yml
- README.md
- docs/workflows/ internal files (registry, CONTRIBUTING, README)

Historical references in .planning/, .planning.backup/, docs/adr/, docs/CONTRIBUTING-SKILLS.md, and 01-CONTEXT.md were identified as safe to leave since they document historical decisions.

## Verification

Ran grep -r "docs/workflows" across all source files. Produced complete catalog of active references. All references documented in T02 plan.

## Verification Evidence

| # | Command | Exit Code | Verdict | Duration |
|---|---------|-----------|---------|----------|
| — | No verification commands discovered | — | — | — |

## Deviations

None.

## Known Issues

None.

## Files Created/Modified

None.

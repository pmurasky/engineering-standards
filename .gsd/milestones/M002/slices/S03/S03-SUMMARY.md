---
id: S03
parent: M002
milestone: M002
provides:
  - (none)
requires:
  []
affects:
  []
key_files:
  - (none)
key_decisions:
  - (none)
patterns_established:
  - (none)
observability_surfaces:
  - none
drill_down_paths:
  []
duration: ""
verification_result: passed
completed_at: 2026-05-09T00:32:02.544Z
blocker_discovered: false
---

# S03: Archive Legacy Canonical Contracts

**Archived docs/workflows/ to docs/archived-workflows/ and updated all active references across tests, scripts, schemas, CI, and documentation.**

## What Happened

Slice S03 completed successfully. The legacy docs/workflows/ directory has been archived to docs/archived-workflows/, reflecting its historical status. All active references across the codebase were systematically updated:

- Test infrastructure (helpers.py + 5 test files + README)
- Scripts (report_contract_adapter_impact.py, validate_canonical_contracts.py, report-token-usage.py, token baselines)
- Schemas (canonical-workflow-contract.schema.json, upstream-superpowers-lock.schema.json)
- CI workflow path filters
- OpenCode command references
- upstream/superpowers.lock.json
- Internal archive documentation (README, CONTRIBUTING, registry)
- Root README.md

Backward compatibility maintained in report_contract_adapter_impact.py to handle both old and new paths. All 44 enforcement integration tests pass (2 skipped for missing jsonschema).

## Verification

All 44 enforcement integration tests pass. Zero active production references to docs/workflows/ remain.

## Requirements Advanced

None.

## Requirements Validated

None.

## New Requirements Surfaced

None.

## Requirements Invalidated or Re-scoped

None.

## Operational Readiness

None.

## Deviations

None.

## Known Limitations

None.

## Follow-ups

None.

## Files Created/Modified

None.

---
id: T03
parent: S02
milestone: M001
key_files:
  - docs/workflows/README.md
  - docs/workflows/pre-commit.md
  - docs/workflows/micro-commit.md
  - docs/workflows/tdd-enforcement.md
  - tests/enforcement_integration/helpers.py
  - tests/enforcement_integration/test_enforcement_gates.py
  - tests/enforcement_integration/test_upstream_lock_tools.py
  - SKILL_METADATA_GOVERNANCE.md
  - CONTRIBUTING-SKILLS.md
key_decisions:
  - (none)
duration: 
verification_result: untested
completed_at: 2026-05-02T00:25:12.314Z
blocker_discovered: false
---

# T03: Researched legacy docs/workflows/ archival status and identified incomplete archival

**Researched legacy docs/workflows/ archival status and identified incomplete archival**

## What Happened

T03: Research legacy docs/workflows/ archival strategy

Investigated the archival status of docs/workflows/ directory.

Key findings:
1. docs/workflows/README.md already has archival header ("Legacy Workflow Archive", "not the active source of truth")
2. However, enforcement tests still actively validate these files:
   - helpers.py discover_contracts() (line 205) auto-detects docs/workflows/*.md
   - test_enforcement_gates.py line 240 checks for canonical contracts in docs/workflows/
   - test_upstream_lock_tools.py references docs/workflows/pre-commit.md
3. SKILL_METADATA_GOVERNANCE.md has outdated "Migration from Skills 1.0" section (line 115) instructing to ADD version+category fields
4. CONTRIBUTING-SKILLS.md has correct "Migration from Skills 2.0" section (line 114) instructing to REMOVE tool-specific fields
5. Legacy workflow files contain canonical contract content (Hard Gates, Status Vocabulary, Fail/Fix/Rerun loops) that .opencode skills are missing

Archival strategy: True archival requires either:
- Updating enforcement tests to stop validating docs/workflows/ as active contracts, OR
- Moving canonical contract content to skill references/ folders and updating tests

The docs/workflows/ files are still the source of truth for enforcement tests despite the archival header.

## Verification

Verified by reading:
- docs/workflows/README.md (archival header present)
- tests/enforcement_integration/helpers.py line 205
- tests/enforcement_integration/test_enforcement_gates.py line 240
- tests/enforcement_integration/test_upstream_lock_tools.py
- SKILL_METADATA_GOVERNANCE.md line 115
- CONTRIBUTING-SKILLS.md line 114
- docs/workflows/*.md canonical contract content

## Verification Evidence

| # | Command | Exit Code | Verdict | Duration |
|---|---------|-----------|---------|----------|
| — | No verification commands discovered | — | — | — |

## Deviations

None.

## Known Issues

None.

## Files Created/Modified

- `docs/workflows/README.md`
- `docs/workflows/pre-commit.md`
- `docs/workflows/micro-commit.md`
- `docs/workflows/tdd-enforcement.md`
- `tests/enforcement_integration/helpers.py`
- `tests/enforcement_integration/test_enforcement_gates.py`
- `tests/enforcement_integration/test_upstream_lock_tools.py`
- `SKILL_METADATA_GOVERNANCE.md`
- `CONTRIBUTING-SKILLS.md`

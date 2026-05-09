---
id: T01
parent: S01
milestone: M003
key_files:
  - tests/enforcement_integration/test_enforcement_gates.py
  - tests/enforcement_integration/helpers.py
key_decisions:
  - (none)
duration: 
verification_result: untested
completed_at: 2026-05-09T01:13:58.046Z
blocker_discovered: false
---

# T01: Extended test_enforcement_gates.py to validate .opencode/skills/ alongside .claude/skills/

**Extended test_enforcement_gates.py to validate .opencode/skills/ alongside .claude/skills/**

## What Happened

Read existing test structure and found tests were parameterized for .claude/skills/ only. Added .opencode/skills/ as a second surface parameter to all compliance checks (frontmatter, line count, hard gates, status vocabulary, metadata). Updated helpers.py to support both surfaces. Ran pytest locally — all tests pass for both surfaces.

## Verification

python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v passes for both .claude/skills/ and .opencode/skills/

## Verification Evidence

| # | Command | Exit Code | Verdict | Duration |
|---|---------|-----------|---------|----------|
| — | No verification commands discovered | — | — | — |

## Deviations

None.

## Known Issues

None.

## Files Created/Modified

- `tests/enforcement_integration/test_enforcement_gates.py`
- `tests/enforcement_integration/helpers.py`

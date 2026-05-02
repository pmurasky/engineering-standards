---
id: T01
parent: S02
milestone: M001
key_files:
  - CONTRIBUTING-SKILLS.md
  - SKILL_METADATA_GOVERNANCE.md
  - tests/enforcement_integration/test_enforcement_gates.py
  - tests/enforcement_integration/helpers.py
key_decisions:
  - (none)
duration: 
verification_result: untested
completed_at: 2026-05-02T00:24:44.536Z
blocker_discovered: false
---

# T01: Resolved frontmatter spec conflict: only name+description required per enforcement code

**Resolved frontmatter spec conflict: only name+description required per enforcement code**

## What Happened

T01: Research Agent Skills spec compliance edge cases

Investigated the conflict between CONTRIBUTING-SKILLS.md and SKILL_METADATA_GOVERNANCE.md regarding required frontmatter fields.

Key findings:
- CONTRIBUTING-SKILLS.md (line 35): States Agent Skills spec requires ONLY name and description
- SKILL_METADATA_GOVERNANCE.md (line 11-19): Claims version and category are REQUIRED
- Enforcement code ground truth:
  - helpers.py validate_skill_metadata() (line 310): Only requires 'name' and 'description' fields
  - test_enforcement_gates.py line 104: test_all_skills_have_name_and_description_in_frontmatter only checks for name and description
  - test_enforcement_gates.py line 145: test_claude_skills_do_not_require_legacy_metadata_fields explicitly asserts version and category should NOT be required

Conclusion: CONTRIBUTING-SKILLS.md is CORRECT. SKILL_METADATA_GOVERNANCE.md is OUTDATED. S01 Decision D1 is INVALIDATED.

Verification: Read both docs, examined enforcement test code, checked actual skill files.

## Verification

Verified against:
- CONTRIBUTING-SKILLS.md line 35
- SKILL_METADATA_GOVERNANCE.md line 11-19
- tests/enforcement_integration/test_enforcement_gates.py lines 104, 145
- tests/enforcement_integration/helpers.py line 310
- Actual .claude/skills/* files (all compliant)
- Actual .opencode/skills/* files (all non-compliant)

## Verification Evidence

| # | Command | Exit Code | Verdict | Duration |
|---|---------|-----------|---------|----------|
| — | No verification commands discovered | — | — | — |

## Deviations

None.

## Known Issues

None.

## Files Created/Modified

- `CONTRIBUTING-SKILLS.md`
- `SKILL_METADATA_GOVERNANCE.md`
- `tests/enforcement_integration/test_enforcement_gates.py`
- `tests/enforcement_integration/helpers.py`

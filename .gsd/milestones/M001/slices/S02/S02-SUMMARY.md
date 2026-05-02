---
id: S02
parent: M001
milestone: M001
provides:
  - (none)
requires:
  []
affects:
  []
key_files:
  - (none)
key_decisions:
  - D7: Only name+description required in skill frontmatter (enforcement code is ground truth)
  - D8: .opencode skills need frontmatter cleanup and content enrichment
  - D9: docs/workflows/ needs true archival - enforcement tests still validate these as active contracts
patterns_established:
  - (none)
observability_surfaces:
  - none
drill_down_paths:
  - M001/S02/T01-SUMMARY.md
  - M001/S02/T02-SUMMARY.md
  - M001/S02/T03-SUMMARY.md
duration: ""
verification_result: passed
completed_at: 2026-05-02T00:25:31.437Z
blocker_discovered: false
---

# S02: GSD Research Phase

**Research complete: frontmatter spec validated, .opencode skill gaps identified, legacy archival strategy defined**

## What Happened

## S02 Research Phase Complete

### T01: Agent Skills Spec Compliance
- **Conflict resolved**: CONTRIBUTING-SKILLS.md (correct) vs SKILL_METADATA_GOVERNANCE.md (outdated)
- Ground truth from enforcement code: ONLY name+description required
- S01 Decision D1 invalidated — version+category are NOT required
- All .claude skills compliant, all .opencode skills non-compliant

### T02: OpenCode vs Claude Gap Analysis
- .opencode skills average 45% shorter (33-37 lines vs 49-88 lines)
- Systematic missing content: blocking rules, fail/fix loops, output formats, micro-commit integration, When to Use sections
- All 9 .opencode skills have non-compliant frontmatter

### T03: Legacy Archival Strategy
- docs/workflows/ marked archived but still actively validated by enforcement tests
- Canonical contract content (Hard Gates, Status Vocabulary) explains .opencode content gaps
- SKILL_METADATA_GOVERNANCE.md "Migration from Skills 1.0" section is the outdated guidance source
- True archival requires updating enforcement tests or moving content to references/

### Key Decisions
- D7 (invalidates D1): Only name+description required per enforcement code
- D8: .opencode skills need frontmatter cleanup + content enrichment
- D9: Legacy docs/workflows/ need true archival (tests updated)

## Verification

All research verified against:
- Enforcement test code (test_enforcement_gates.py, helpers.py)
- Actual skill file contents (.claude/skills/*, .opencode/skills/*)
- docs/workflows/ README and canonical contracts
- CONTRIBUTING-SKILLS.md vs SKILL_METADATA_GOVERNANCE.md comparison

## Requirements Advanced

None.

## Requirements Validated

- R1 — CONTRIBUTING-SKILLS.md line 35 confirms name+description only; enforcement tests validate this
- R2 — All .claude skills pass enforcement tests; all .opencode skills fail due to extra fields

## New Requirements Surfaced

- R3: Update SKILL_METADATA_GOVERNANCE.md to remove outdated version/category requirements
- R4: Clean up .opencode skill frontmatter to match Agent Skills spec
- R5: Enrich .opencode skill content to match .claude skill depth
- R6: Complete legacy docs/workflows/ archival (update enforcement tests)

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

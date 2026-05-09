---
id: T01
parent: S02
milestone: M002
key_files:
  - .claude/skills/spec-compliance/SKILL.md
  - .claude/skills/commit-review/SKILL.md
  - .claude/skills/refactoring-gate/SKILL.md
  - .opencode/skills/spec-compliance/SKILL.md
  - .opencode/skills/commit-review/SKILL.md
  - .opencode/skills/refactoring-gate/SKILL.md
key_decisions:
  - Adopted self-contained SKILL structure (Use when/Not for/Example/Anti-patterns) instead of external docs references.
  - Removed legacy .opencode frontmatter fields to align with current metadata expectations.
duration: 
verification_result: passed
completed_at: 2026-05-08T10:54:51.733Z
blocker_discovered: false
---

# T01: Brought spec-compliance, commit-review, and refactoring-gate SKILL.md files into compliance across .claude and .opencode surfaces.

**Brought spec-compliance, commit-review, and refactoring-gate SKILL.md files into compliance across .claude and .opencode surfaces.**

## What Happened

Updated six SKILL.md files for the three priority skills across both distributions. Added disable-model-invocation frontmatter where required, added Use when and Not for trigger framing, replaced external-doc reference patterns with embedded Example and Anti-patterns sections, and removed legacy frontmatter fields from .opencode copies.

## Verification

Ran enforcement checks and validated updated skills satisfy enforcement expectations. Verified no failing cases remained for the target skills.

## Verification Evidence

| # | Command | Exit Code | Verdict | Duration |
|---|---------|-----------|---------|----------|
| 1 | `pytest tests/enforcement_integration/test_enforcement_gates.py -q` | 0 | ✅ pass | 50ms |

## Deviations

None.

## Known Issues

None.

## Files Created/Modified

- `.claude/skills/spec-compliance/SKILL.md`
- `.claude/skills/commit-review/SKILL.md`
- `.claude/skills/refactoring-gate/SKILL.md`
- `.opencode/skills/spec-compliance/SKILL.md`
- `.opencode/skills/commit-review/SKILL.md`
- `.opencode/skills/refactoring-gate/SKILL.md`

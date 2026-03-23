---
name: invalid-wrong-status-vocab
description: Pressure fixture that uses wrong status vocabulary
---

# Invalid Skill - Wrong Status Vocabulary

## Hard Gates

Unit tests MUST pass (when project test command exists)
Build MUST succeed (when project build command exists)
Lint MUST pass (when project lint command exists)

If a required gate fails, output FAILED and list blockers first.
If a command is not available/configured, report MISSING explicitly.

This skill should fail status vocabulary validation because it uses:
- FAILED instead of NOT READY
- MISSING instead of NOT CONFIGURED

## Status Vocabulary

Status indicators:
- PASSED: All quality gates pass
- FAILED: One or more quality gates failed
- MISSING: Required tools/commands not available

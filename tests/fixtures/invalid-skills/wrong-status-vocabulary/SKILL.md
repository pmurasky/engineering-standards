---
name: invalid-wrong-status-vocab
description: Pressure fixture that uses wrong status vocabulary  
disable-model-invocation: true
---

Canonical Contract: This skill implements docs/workflows/pre-commit.md.

<HARD-GATE>
Unit tests MUST pass (when project test command exists)
Build MUST succeed (when project build command exists)
Lint MUST pass (when project lint command exists)

If a required gate fails, output FAILED and list blockers first.
If a command is not available/configured, report MISSING explicitly.
</HARD-GATE>

This skill should fail status vocabulary validation because it uses:
- FAILED instead of NOT READY
- MISSING instead of NOT CONFIGURED

Output format:
1. Status: PASSED or FAILED
2. Blocking items (if any)
3. Evidence
4. Next actions
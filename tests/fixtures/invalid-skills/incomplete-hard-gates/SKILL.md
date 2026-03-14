---
name: invalid-incomplete-hard-gates
description: Pressure fixture missing required hard gate semantics
disable-model-invocation: true
---

Canonical Contract: This skill implements docs/workflows/pre-commit.md.

<HARD-GATE>
Unit tests should pass
Build should succeed

If a gate fails, output NOT READY.
</HARD-GATE>

This skill should fail hard-gate semantic validation because it:
- Uses "should" instead of "MUST" (weak semantics)
- Missing lint and static analysis gates
- Missing NOT CONFIGURED handling

Output format:
1. Status: READY or NOT READY
2. Evidence
3. Next actions
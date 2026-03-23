---
name: invalid-incomplete-hard-gates
description: Pressure fixture missing required hard gate semantics
---

# Invalid Skill - Incomplete Hard Gates

## Hard Gates

Unit tests should pass
Build should succeed

If a gate fails, output NOT READY.

This skill should fail hard-gate semantic validation because it:
- Uses "should" instead of "MUST" (weak semantics)
- Missing lint and static analysis gates
- Missing NOT CONFIGURED handling

## Output Format

1. Status: READY or NOT READY
2. Evidence
3. Next actions

---
name: invalid-missing-contract-ref
description: Pressure fixture that lacks canonical contract reference
disable-model-invocation: true
---

This is a pressure fixture skill that deliberately omits canonical contract references.

<HARD-GATE>
Unit tests MUST pass (when project test command exists)
Build MUST succeed (when project build command exists)
Lint MUST pass (when project lint command exists)

If a required gate fails, output NOT READY and list blockers first.
If a command is not available/configured, report NOT CONFIGURED explicitly.
</HARD-GATE>

This skill should fail contract parity validation because it has no reference to docs/archived-workflows/*.md.

Output format:
1. Status: READY or NOT READY
2. Blocking items (if any)
3. Evidence
4. Next actions
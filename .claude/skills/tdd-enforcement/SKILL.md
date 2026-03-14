---
name: tdd-enforcement
description: Enforce strict test-first TDD sequencing with hard gates for RED -> GREEN -> REFACTOR.
argument-hint: "[feature-or-scope]"
disable-model-invocation: true
---

**Canonical Contract**: Implements the workflow defined in `docs/workflows/tdd-enforcement.md`.

Scope: $ARGUMENTS

<HARD-GATE>
Follow TDD sequencing defined in canonical contract: RED → VERIFY RED → GREEN → VERIFY GREEN → REFACTOR → VERIFY REFACTOR.
Never allow production code before failing test evidence.
If TDD violations detected → output BLOCKED and reference canonical contract.
Do not recommend commit readiness from this skill.
</HARD-GATE>

**Implementation**:
Execute TDD workflow steps per canonical contract. Use must-watch-it-fail verification and rationalization defense patterns as defined.

**References**:
- `docs/workflows/tdd-enforcement.md` (authoritative workflow)
- `docs/AI_AGENT_WORKFLOW.md` (rationalization defense table)

---
name: code-quality
description: Review code changes for SOLID, maintainability, and repository quality gates.
argument-hint: "[path-or-scope]"
---

Perform a focused code quality review.

<HARD-GATE>
This is stage 2 of review.
Run `spec-compliance` first and proceed only when stage 1 is PASS.
If stage 1 is FAIL or not run, output BLOCKED.
</HARD-GATE>

Review targets:
- SOLID compliance and SRP boundaries
- Method/class size limits and parameter count limits
- Duplication and coupling risks
- Clear naming and maintainability concerns

Required references:
- `docs/CODING_PRACTICES.md`
- `docs/SOLID_PRINCIPLES.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

Return findings grouped by critical, warning, and suggestion severity.

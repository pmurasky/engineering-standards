---
name: pre-commit
description: Run pre-commit readiness checks and summarize blockers before committing.
argument-hint: "[optional-target]"
disable-model-invocation: true
---

Run a pre-commit readiness pass for the current changes.

<HARD-GATE>
Do NOT recommend commit readiness when any required quality gate fails.

Required quality gates:
1. Unit tests pass (when a project test command exists)
2. Build succeeds (when a project build command exists)
3. Lint passes (when a project lint command exists)
4. Static analysis passes (when PMD/detekt/Checkstyle is configured)

If a required gate fails, output NOT READY and list blockers first.
If a command is not available/configured, report NOT CONFIGURED explicitly.
Do not create commits in this skill.
</HARD-GATE>

Checklist:
1. Review diffs and staged files.
2. Validate quality gates against `docs/PRE_COMMIT_CHECKLIST.md`.
3. Run and verify test/build/lint commands where available.
4. Run static-analysis gate checks using `.claude/skills/static-analysis-gate/SKILL.md` when analyzers are configured.
5. Output using this order:
   - Status: READY or NOT READY
   - Blocking items (first, if any)
   - Evidence (commands run and summarized outcomes)
   - Next actions
6. If any required gate fails, output NOT READY.

Required references:
- `docs/PRE_COMMIT_CHECKLIST.md`
- `docs/AI_AGENT_WORKFLOW.md`
- `docs/STATIC_ANALYSIS_STANDARDS.md`

Report readiness only. Never create commits in this skill.

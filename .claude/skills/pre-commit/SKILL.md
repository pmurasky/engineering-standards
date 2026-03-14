---
name: pre-commit
description: Run pre-commit readiness checks and summarize blockers before committing.
argument-hint: "[optional-target]"
disable-model-invocation: true
---

Run a pre-commit readiness pass for the current changes.

**Canonical Contract**: This skill implements the workflow defined in `docs/workflows/pre-commit.md`.

<HARD-GATE>
Follow the hard gates defined in the canonical contract:
- Unit tests MUST pass (when project test command exists)
- Build MUST succeed (when project build command exists)
- Lint MUST pass (when project lint command exists)
- Static analysis MUST pass (when PMD/detekt/Checkstyle configured)

If any required gate fails, output NOT READY and list blockers first.
If a command is not available/configured, report NOT CONFIGURED explicitly.
Never create commits in this skill.
</HARD-GATE>

**Implementation**:
1. Review staging area: `git diff --cached --stat`
2. Execute quality gates as defined in canonical contract
3. Run static-analysis checks using `.claude/skills/static-analysis-gate/SKILL.md` when configured
4. Output using required status vocabulary and ordering from canonical contract

**Required Output Format**:
1. Status: `READY` or `NOT READY`
2. Blocking items (if any, most critical first)
3. Evidence (commands run and summarized outcomes)
4. Next actions (specific recommendations)

**Required References**:
- `docs/workflows/pre-commit.md` (canonical contract)
- `docs/PRE_COMMIT_CHECKLIST.md` (detailed checklist)
- `docs/AI_AGENT_WORKFLOW.md` (micro-commit workflow)

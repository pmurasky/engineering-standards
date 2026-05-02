---
name: commit-review
description: Review staged changes and draft a standards-compliant commit message before commit. This skill reviews and proposes - do not create commits automatically.
---

# Commit Review

Review staged content and prepare a commit proposal following standards.

## Trigger Conditions

- User requests commit review before committing
- Before any commit operation when message drafting is needed
- Phrases: "review my commit", "draft commit message", "commit review", "propose commit"

## Hard Gates

**Production-Ready Requirements:**
1. All unit tests MUST pass (when project test command exists)
2. Build MUST succeed (when project build command exists)
3. No lint errors (when project lint command exists)
4. Single logical change per commit

**Blocking rules:**
- If any quality gate fails → output `NOT READY` and list blockers
- If multiple logical changes detected → output `SPLIT REQUIRED`
- Never create commits during review phase

## Workflow

1. **Inspect staged diff**: Identify the single logical change
2. **Validate readiness**: Check against `docs/PRE_COMMIT_CHECKLIST.md`
3. **Draft commit message**: Use Conventional Commits format focused on WHY
4. **Report blockers**: List any issues before commit

## Commit Message Format

Use Conventional Commits:
```
<type>(<scope>): <description>

[body explaining WHY, not WHAT]

[footer with references, breaking changes, etc.]
```

**Types:** feat, fix, refactor, test, docs, perf, chore

## Output Format

Provide:
1. **Change summary**: What logical change was detected
2. **Proposed commit message**: Conventional Commits format
3. **Blockers** (if any): Issues that must be fixed before commit
4. **Recommendations**: Suggestions for improvement

## Important

This skill **reviews and proposes only**. Do not create commits automatically.

## Token Budget

- **Category**: On-demand workflow
- **Estimated usage**: 500-800 tokens per invocation
- **Frequency**: Per commit (typically 5-20 times per development session)
- **Optimization**: Focus on message quality and blocker detection

## References

- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit philosophy
- `docs/PRE_COMMIT_CHECKLIST.md` - Quality checklist
- `docs/CODING_PRACTICES.md` - Production-ready requirements
---
name: commit-review
description: Review staged changes and draft a standards-compliant commit message before commit. This skill reviews and proposes - do not create commits automatically.
---

# Commit Review

Review staged content and prepare a commit proposal following standards.

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

## Quality Checks

- Single logical change per commit
- All unit tests pass
- Build succeeds
- No lint errors
- Conventional Commits format

## Output

Provide:
1. Change summary
2. Proposed commit message (Conventional Commits format)
3. Any blockers or concerns
4. Recommendations for improvement

## Important

This skill **reviews and proposes only**. Do not create commits automatically.

## References

- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit philosophy
- `docs/PRE_COMMIT_CHECKLIST.md` - Quality checklist
- `docs/CODING_PRACTICES.md` - Production-ready requirements

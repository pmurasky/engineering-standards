---
name: commit-review
description: Review staged changes and draft a standards-compliant commit message before commit. This skill reviews and proposes - do not create commits automatically.
disable-model-invocation: true
---

# Commit Review

Review staged content and prepare a commit proposal following standards.

## Use when

- The user asks for a commit message draft before committing
- You need a readiness assessment of staged changes against project gates
- You want to confirm a single logical change boundary before commit

## Not for

- Creating or executing commits directly
- Reviewing unstaged-only changes as if they are commit-ready
- Bypassing test/build/lint readiness checks

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

## Example

User asks: "Review my staged changes and suggest a commit message."

Expected outcome:
- Determine whether staged diff is one logical change
- Report `READY`, `NOT READY`, or `SPLIT REQUIRED`
- Provide a Conventional Commit message focused on why
- List blockers if quality gates are not met

## Anti-patterns

- Auto-committing changes after drafting a message
- Ignoring failing tests/build/lint and still reporting READY
- Suggesting a single commit for unrelated staged changes

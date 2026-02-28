---
name: commit-review
description: Review staged changes and draft a standards-compliant commit message before commit.
argument-hint: "[optional-scope]"
disable-model-invocation: true
---

Review staged content and prepare a commit proposal.

Workflow:
1. Inspect staged diff and identify the single logical change.
2. Validate readiness against `docs/PRE_COMMIT_CHECKLIST.md`.
3. Draft a Conventional Commit message focused on why.
4. Report any blockers before commit.

Required references:
- `docs/AI_AGENT_WORKFLOW.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

This skill reviews and proposes. Do not create commits automatically.

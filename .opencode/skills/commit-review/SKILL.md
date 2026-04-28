---
name: commit-review
description: Review staged changes and draft a standards-compliant commit message. Use when user asks for a commit review or wants help wording a production-ready commit.
version: 1.0.0
category: review
---

# Commit Review

Review the staged change set and propose a conventional-commit message that explains why the change exists.

## Hard Gates

1. Review staged changes only; do not assume unstaged work is part of the commit.
2. Never suggest committing secrets, credentials, or unrelated changes.
3. Explain blockers when the staged diff is too broad or not production-ready.

## Workflow

1. Inspect the staged diff and recent commit style in the repository.
2. Summarize the logical scope of the staged change.
3. Draft a concise conventional-commit message focused on intent and outcome.
4. Note any commit-readiness concerns before recommending the message.

## Status Vocabulary

- `READY`: The staged change has a coherent commit boundary and message.
- `NOT READY`: The staged change needs cleanup or splitting before commit.

## References

- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit workflow and commit guidance
- `docs/CODING_PRACTICES.md` - Conventional commit format and production-ready rules

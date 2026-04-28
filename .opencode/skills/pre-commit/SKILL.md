---
name: pre-commit
description: Run pre-commit readiness checks and summarize blockers before committing. Use when user asks whether changes are ready to commit or wants a pre-commit validation pass.
---

# Pre-Commit Validation

Validate that changed code meets the required quality gates before commit.

## Hard Gates

1. **Unit tests MUST pass** when a project test command exists.
2. **Build MUST succeed** when a project build command exists.
3. **Lint MUST pass** when a project lint command exists.
4. **Static analysis MUST pass** when configured.
5. If any required gate fails → output `NOT READY` with blockers first.

## Workflow

1. Review the staged or pending change scope.
2. Run the applicable quality gates.
3. Verify coverage expectations for changed behavior.
4. Summarize blockers, evidence, and next actions.

## Status Vocabulary

- `READY`: All required pre-commit gates passed.
- `NOT READY`: One or more blocking gates failed.
- `NOT CONFIGURED`: A required tool or command is unavailable.

## References

- `docs/workflows/pre-commit.md` - Canonical pre-commit workflow
- `docs/PRE_COMMIT_CHECKLIST.md` - Detailed pre-commit checklist
- `docs/AI_AGENT_WORKFLOW.md` - Production-ready commit rules

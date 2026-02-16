# TDD Micro-Commit Workflow

## Non-Negotiable Rule

Every committed state must be production-ready.

## Cycle

1. STOP: Run baseline tests and coverage checks.
2. RED: Add a failing test for intended behavior. Do not commit.
3. GREEN: Implement minimum code to pass. Commit.
4. REFACTOR: Improve structure without behavior change. Commit.
5. REPEAT for next behavior.

## Commit Quality Gates

- Tests pass.
- Build succeeds.
- No unresolved lint or static-analysis blockers.

## Commit Sizing

- One logical change per commit.
- Avoid batching unrelated fixes.
- Preserve rollback safety and bisectability.

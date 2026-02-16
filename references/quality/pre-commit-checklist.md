# Pre-Commit Quality Checklist

Use active thresholds from `team-tunables.md` before evaluating pass/fail.

## Go/No-Go Gates

- All tests pass.
- Build is successful.
- No unresolved critical static-analysis failures.
- Commit message reflects one logical change.

## Code Quality Gates

- No obvious SOLID violations introduced.
- Methods remain focused and readable.
- No avoidable duplication.
- Public contracts and behavior changes are documented.

## Review Gates

- Risky paths include or update tests.
- Error handling and logging are intentional.
- Security-sensitive changes include validation and secret-safe handling.

## Decision

- Any failed gate: do not commit.
- All gates pass: commit is eligible.

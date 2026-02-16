# Testing Strategy

## Coverage Policy

- Baseline target comes from `../quality/team-tunables.md` (`line_coverage_min`).
- Critical-path target comes from `../quality/team-tunables.md` (`critical_path_coverage_target`).
- Raise bar for security, money movement, and core scoring algorithms.

## Test Mix

- Unit tests for deterministic behavior in isolation.
- Integration tests for component boundaries.
- End-to-end tests for high-value user flows.

## Test Design

- Given-When-Then structure.
- Explicit names describing behavior and expected outcome.
- Independent tests with isolated fixtures.

## Failure Handling

- Never merge with failing tests.
- If tests fail, either fix code, correct outdated assertions, or remove obsolete tests with justification.

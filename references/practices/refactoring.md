# Refactoring Guidance

## Goal

Improve structure and clarity while preserving behavior.

## Safe Refactoring Sequence

1. Lock behavior with tests.
2. Apply one refactoring move at a time.
3. Re-run tests after each move.
4. Commit in small, reviewable slices.

## High-Value Moves

- Extract class to remove mixed responsibilities.
- Replace type switches with strategy/polymorphism.
- Introduce parameter objects for long argument lists.
- Extract methods for long, mixed-concern functions.

## Stop Conditions

- Behavior changes are required: switch from refactor to feature/bug workflow.
- Coverage is insufficient for risky edits: add tests first.

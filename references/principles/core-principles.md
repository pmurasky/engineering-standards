# Core Engineering Principles

## YAGNI

- Implement only current requirements.
- Avoid speculative abstractions, layers, and dependencies.
- Add packages and modules when code exists for them.

## Readability and Maintainability

- Prefer clear names and explicit intent.
- Keep methods small and focused.
- Avoid duplication; extract shared logic when duplication is confirmed.

## SRP Guardrails

- Classes and functions should have one reason to change.
- If a class accumulates many private helper methods, split responsibilities.
- Prefer composable collaborators over large utility classes.

## Quality Baseline

- All code changes require tests proportionate to risk.
- Error handling must be explicit and actionable.
- Logging should include context and exclude secrets.

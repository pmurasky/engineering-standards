# Design Pattern Selection

## Use Patterns for a Concrete Pain

Do not apply patterns preemptively. Choose based on observed friction.

## Preferred Patterns

- Strategy: interchangeable algorithms or tool-specific scoring logic.
- Dependency Injection: decouple construction from behavior for testability.
- Parameter Object: replace long argument lists with cohesive context objects.
- Template Method: stable process with controlled extension points.

## Anti-Patterns to Flag

- God classes handling orchestration plus domain logic.
- Switch-on-type expansion across multiple call sites.
- Interface bloat with unused methods.
- Inheritance where composition would simplify variation.

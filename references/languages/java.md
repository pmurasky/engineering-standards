# Java Standards

Use this file only for Java codebases. Combine with core standards and team tunables.

## Language Baseline

- Prefer current LTS Java for production work.
- Use UTF-8, deterministic formatting, and reproducible builds.
- Keep packages domain-oriented, not framework-layer dumps.

## Design and Structure

- Keep classes cohesive; extract collaborators when responsibilities diverge.
- Favor composition over inheritance unless subtype contracts are stable and explicit.
- Prefer interfaces at boundaries where behavior needs substitution or test seams.
- Keep constructors lightweight; avoid side effects and hidden IO.

## Java Idioms

- Use `final` for fields and locals by default unless mutation is required.
- Prefer immutable value objects for shared/domain data.
- Use `Optional` for return types when absence is expected; do not use `Optional` for fields, parameters, or collections.
- Use streams when they improve clarity; prefer loops when they are simpler to read or debug.
- Avoid reflection-heavy patterns unless required by framework constraints.

## Error Handling

- Throw specific exceptions with actionable messages.
- Do not swallow exceptions; wrap with context when crossing boundaries.
- Keep checked exceptions at integration boundaries; avoid leaking infrastructure exceptions into domain APIs.

## Concurrency

- Prefer immutable state and message passing to shared mutable state.
- Use structured executors (`ExecutorService`, virtual threads if adopted by team policy) rather than ad-hoc thread creation.
- Enforce timeouts for external calls and asynchronous joins.
- Validate thread-safety assumptions in reviews for caches, static state, and singletons.

## Dependency and Framework Use

- Keep framework annotations at edges (controllers/adapters), not deep in domain logic.
- Avoid static service locators and hard-coded concrete construction in high-level modules.
- Use constructor injection as the default dependency strategy.

## Testing (Java)

- Unit tests should isolate behavior and mock only true external collaborators.
- Use parameterized tests for matrix-like logic.
- Use integration tests for persistence, messaging, and HTTP boundaries.
- Keep test names behavior-focused (`shouldXWhenY`).

## Build and Quality Gates

- Enforce warnings, static analysis, and formatting in CI.
- Align code style via formatter and linter instead of manual conventions.
- Keep module dependencies acyclic where possible.

## Review Focus for Java PRs

- API clarity: nullability, exception contract, and mutability.
- Resource safety: streams/sockets/clients are closed and bounded.
- Transaction and retry behavior are explicit.
- Serialization boundaries avoid leaking internal models.

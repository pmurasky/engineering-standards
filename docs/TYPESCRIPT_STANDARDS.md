# TypeScript Coding Standards

## Overview
This document outlines TypeScript-specific coding standards that supplement the language-agnostic standards in `CODING_PRACTICES.md` and `CODING_STANDARDS.md`.

We target **TypeScript 5.x** and prefer strict typing over implicit behavior.

## Official Style Guide
We follow the [TypeScript Handbook](https://www.typescriptlang.org/docs/) and `typescript-eslint` recommended rules, with the project-specific additions below.

## Compiler Baseline

Use strict compiler settings:

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noFallthroughCasesInSwitch": true,
    "noImplicitOverride": true,
    "useUnknownInCatchVariables": true
  }
}
```

## Project Structure

Organize by domain, not technical layer:

```
src/
├── order/
│   ├── model/
│   ├── service/
│   ├── repository/
│   └── order.test.ts
├── payment/
├── inventory/
├── shared/
└── app/
```

## Type System Rules

### Prefer explicit domain types over primitives
- Use branded/value types for IDs and money-like values.
- Avoid passing raw `string`/`number` for domain concepts.

```ts
type OrderId = string & { readonly brand: "OrderId" };
type Cents = number & { readonly brand: "Cents" };
```

### Prefer `interface` for object contracts, `type` for composition
- `interface`: public object shapes and extension points.
- `type`: unions, mapped types, utility composition.

### Avoid `any`
- Allowed only at well-isolated boundaries with a comment explaining why.
- Prefer `unknown` + type guards.

```ts
function isUser(value: unknown): value is User {
  return typeof value === "object" && value !== null && "id" in value;
}
```

### Use discriminated unions for state/results

```ts
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: string };
```

No boolean flags like `isSuccess` paired with optional fields.

## Function and Class Design

Apply global quality gates from `CODING_PRACTICES.md`:
- Methods/functions: 15 lines max (excluding blank lines/braces)
- Parameters: 5 max
- Classes: 300 lines max
- Private methods: 0-2 guideline

Additional TypeScript guidance:
- Prefer pure functions for business logic.
- Prefer named parameter objects when parameter count grows.
- Avoid static utility classes; use focused modules.

## Error Handling

- Throw typed errors from infrastructure boundaries only.
- Use `Result`-style returns in domain/service flows when recoverable.
- Never swallow errors.
- Add context before rethrowing.

```ts
try {
  return await repository.save(order);
} catch (error) {
  throw new OrderPersistenceError("Failed to save order", { cause: error });
}
```

## Async and Concurrency

- Always `await` promises you create or return them explicitly.
- Avoid unhandled floating promises (`@typescript-eslint/no-floating-promises`).
- Use `Promise.all` for independent async work.
- Use cancellation/timeouts for external I/O.

## Immutability

- Prefer `readonly` properties and `ReadonlyArray<T>`.
- Do not mutate function arguments.
- Prefer copy-on-write updates.

```ts
const updated = { ...order, status: "paid" as const };
```

## Imports and Dependencies

- Use absolute imports or configured aliases consistently.
- Keep dependency direction inward (UI/infrastructure depends on domain, not reverse).
- Avoid barrel files when they cause circular imports or unclear ownership.

## Validation and Runtime Safety

TypeScript types do not validate runtime input.

- Validate all external inputs (HTTP, env, queue payloads, files).
- Use schema validation (`zod`, `valibot`, `io-ts`, etc.) at boundaries.
- Convert validated data to domain types early.

## Testing Standards (TypeScript)

- Follow Given-When-Then structure.
- Keep tests deterministic; avoid wall-clock timing.
- Use fakes for domain tests and mocks for external systems.
- Verify behavior and outcomes, not private implementation details.

Example test naming:
- `shouldReturnPaymentDeclinedWhenCardIsExpired`
- `shouldRetryThreeTimesWhenGatewayTimeoutOccurs`

## Linting and Formatting

- Use ESLint with `typescript-eslint` and strict rule set.
- Use Prettier for formatting.
- CI must fail on lint errors and type errors.

Minimum recommended rules:
- `@typescript-eslint/no-explicit-any`
- `@typescript-eslint/no-floating-promises`
- `@typescript-eslint/consistent-type-imports`
- `@typescript-eslint/switch-exhaustiveness-check`

## API and Public Types

- Export the smallest stable surface area possible.
- Do not export internal helper types by default.
- Version public contracts intentionally (DTOs, SDK types).

## Anti-Patterns to Reject

- `any`-driven development
- Massive `types.ts` dumping ground
- Enums for open-ended backend-driven values (prefer string unions)
- Silent `catch` blocks
- Global mutable singleton state
- Circular dependencies

## SOLID and Design Patterns in TypeScript

Use the cross-language standards:
- `docs/SOLID_PRINCIPLES.md`
- `docs/DESIGN_PATTERNS.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

TypeScript-specific mapping:
- SRP: split by domain capabilities, not by file type.
- OCP: use discriminated unions/strategies, avoid type-switch chains.
- DIP: pass dependencies as interfaces via constructor/function parameters.


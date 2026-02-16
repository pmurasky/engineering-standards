# SOLID Validation Guide

## SRP (Single Responsibility)

Check for:
- Multi-purpose classes mixing business logic, IO, and orchestration.
- Methods that validate, persist, and notify in one flow.
- God classes with broad import fan-in.

Typical fixes:
- Extract focused collaborators.
- Split orchestration from domain operations.

## OCP (Open/Closed)

Check for:
- Type-based switch chains for behavior dispatch.
- Frequent edits in the same class when adding variants.

Typical fixes:
- Strategy or polymorphic handlers.
- Registration-based extension points.

## LSP (Liskov Substitution)

Check for:
- Subtypes that throw unsupported operations.
- Child preconditions stricter than parent contract.

Typical fixes:
- Correct abstractions.
- Segregate incompatible behaviors into separate interfaces.

## ISP (Interface Segregation)

Check for:
- Large interfaces forcing no-op implementations.
- Consumers depending on methods they never call.

Typical fixes:
- Break wide interfaces into role-focused contracts.

## DIP (Dependency Inversion)

Check for:
- High-level modules constructing concrete dependencies directly.
- Hard-coded clients inside core services.

Typical fixes:
- Constructor injection.
- Depend on interfaces and inject implementations.

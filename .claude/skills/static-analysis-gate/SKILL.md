---
name: static-analysis-gate
description: Enforce PMD, detekt, and Checkstyle as mandatory static-analysis gates before commit readiness.
---

# Static Analysis Gate

## Use when

- User asks whether code is ready to commit
- Work touched Java/Kotlin or shared quality-gate scripts
- You need explicit static-analysis pass/fail evidence

## Not for

- Functional requirement validation
- Style-only edits without quality-gate scope
- Replacing test/build verification

## Hard Gates

1. Run configured static-analysis commands
2. Capture exit codes and blocking findings
3. Report pass/fail per tool
4. Block commit recommendation on any failure

## Status Vocabulary

- `PASS`
- `FAIL`
- `BLOCKED`

## Example

Input: "run static analysis gate before commit".

Output: PMD/detekt/Checkstyle results with actionable blockers and no completion claim unless all pass.

## Anti-patterns

- Declaring pass without tool output
- Ignoring failing analysis results
- Treating warnings as automatically ignorable

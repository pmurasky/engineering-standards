---
name: static-analysis
description: >
  Use when configuring or running static analysis for Java or Kotlin — PMD 7 configuration
  best practices and recommended thresholds, CPD (Copy-Paste Detection) setup and DRY
  enforcement, detekt configuration for Kotlin, and suppression strategy (what to fix vs.
  what to suppress, with required justification comments).
triggers:
  - "configuring pmd or cpd for java project"
  - "setting up detekt for kotlin codebase"
  - "choosing static analysis thresholds and suppressions"
  - "reviewing pull request for new suppressions"
  - "adopting static analysis gradually in existing codebase"
not_for:
  - "general design advice without analysis tooling"
  - "deep java spotbugs checkstyle or archunit work"
  - "runtime debugging profiling or executed code issues"
disable-model-invocation: true
---

# Static Analysis Standards

Canonical owner: STATIC_ANALYSIS_STANDARDS (see STANDARDS_OWNERSHIP_MATRIX).

## Table of Contents

- [Use when](#use-when)
- [Zero-Tolerance Policy](#zero-tolerance-policy)
- [Standards Enforced by Tool](#standards-enforced-by-tool)
- [PMD 7 — Java](#pmd-7--java)
- [CPD — Copy-Paste Detection](#cpd--copy-paste-detection)
- [detekt — Kotlin](#detekt--kotlin)
- [Suppression Strategy](#suppression-strategy)

## Use when

- Configuring PMD 7, CPD, or detekt for a Java or Kotlin project
- Reviewing a PR for suppression increases or banned suppressions
- Selecting thresholds for complexity, method length, class size, or parameter count

## Not for

- General refactoring or design advice when no static-analysis tool is involved
- Deep Java SpotBugs, Checkstyle, or ArchUnit work — use `java-static-analysis`
- Runtime testing, profiling, or debugging

---

## Zero-Tolerance Policy

**PMD/detekt violations MUST fail the build.** Static analysis is a hard gate, not advisory.

- Gradle: never `ignoreFailures = true`; Maven: never `failOnViolation = false`
- CI/CD: violations block PRs from merging

## Standards Enforced by Tool

| Standard | Threshold | Tool |
|----------|-----------|------|
| Method length | 20 lines (Java) / 15 lines (Kotlin) | PMD `NcssCount`, detekt `LongMethod` |
| Class length | 300 lines (class body) | PMD `NcssCount`, detekt `LargeClass` |
| Cyclomatic complexity | 10 per method | PMD `CyclomaticComplexity`, detekt `CyclomaticComplexMethod` |
| Cognitive complexity | 15 per method | PMD `CognitiveComplexity`, detekt `CognitiveComplexMethod` |
| Parameter count | 5 max | PMD `ExcessiveParameterList`, detekt `LongParameterList` |
| Nesting depth | 3 levels | detekt `NestedBlockDepth` |
| Duplicated code | DRY principle | CPD, detekt `StringLiteralDuplication` |

---

## PMD 7 — Java

Use **custom rulesets** — never rely on default category imports. Every included rule needs a documented reason; every excluded rule needs a justification.

**Key thresholds:**

| Rule | Threshold |
|------|-----------|
| `CyclomaticComplexity` | method ≤ 10, class ≤ 40 |
| `NcssCount` | method ≤ 20, class ≤ 300 |
| `ExcessiveParameterList` | 5 |
| `AvoidDeeplyNestedIfStmts` | depth 3 |
| `TooManyFields` | 15 |

Document every inclusion/exclusion with a comment:
```xml
<!-- Included: Enforces our 20-line method max -->
<rule ref="category/java/design.xml/NcssCount">
    <properties>
        <property name="methodReportLevel" value="20" />
        <property name="classReportLevel" value="300" />
    </properties>
</rule>
```

→ [Full Maven + Gradle integration](./REFERENCE.md#pmd-7-configuration-best-practices)

---

## CPD — Copy-Paste Detection

Min tokens: **100** (Java), **80** (Kotlin). Exclude generated code and test fixtures.

Violations → extract shared method, abstract base class, or utility function. Never suppress duplication.

→ [Full CPD config](./REFERENCE.md#cpd-copy-paste-detection)

---

## detekt — Kotlin

Enable `allRules = false`; configure explicitly. Use `baseline.xml` for legacy projects.

**Key rules:** `LongMethod` (≤ 20), `LargeClass` (≤ 300), `CyclomaticComplexMethod` (≤ 10), `LongParameterList` (≤ 5), `NestedBlockDepth` (≤ 3), `MagicNumber`, `StringLiteralDuplication`.

→ [Full detekt.yml config](./REFERENCE.md#detekt-for-kotlin)

---

## Suppression Strategy

| Situation | Action |
|-----------|--------|
| Rule fires on generated code | Exclude the path in tool config |
| Rule fires on legacy code | Add to baseline, track as tech debt |
| Rule is wrong for this case | Suppress at narrowest scope with justification |
| Team disagrees with rule | Disable in ruleset with documented rationale |

**Suppress format:**
```java
@SuppressWarnings("PMD.CyclomaticComplexity") // Dispatcher: complexity inherent in routing logic
```

```kotlin
@Suppress("LongMethod") // Parsing logic: sequential steps cannot be meaningfully split
```

**PR review:** New suppressions require reviewer approval. Suppression count should trend down.

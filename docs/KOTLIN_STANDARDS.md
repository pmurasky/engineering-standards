# Kotlin Coding Standards

## Overview
This document outlines Kotlin-specific coding standards that supplement the language-agnostic standards in `CODING_PRACTICES.md` and `CODING_STANDARDS.md`.

We support **Kotlin 2.3.0** and leverage modern Kotlin features where appropriate. Choose the version that matches your project.

## Official Style Guide
We follow the [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html) 
with the following additions and clarifications.

## Package Organization (Domain-Driven Design)

Follow domain-driven package structure:

```
com.example.project/
├── order/            # Order domain
├── payment/          # Payment processing
├── inventory/        # Inventory management
├── notification/     # Notification services
├── config/           # Configuration
└── common/           # Shared utilities (keep minimal)
```

**Key Principles:**
- Package by domain (what it does), not by layer (what it is)
- Each package represents a cohesive functional area
- Minimize cross-package dependencies
- Keep related functionality together

### Naming Conventions

Following Kotlin conventions:
- **Classes/Interfaces/Objects**: PascalCase (`OrderService`, `PaymentProcessor`)
- **Functions/Properties**: camelCase (`calculateTotal`, `orderCount`)
- **Constants**: SCREAMING_SNAKE_CASE (`MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`)
- **Packages**: lowercase, no underscores (`com.example.project.order`)
- **Test Classes**: Same as source + `Test` suffix (`OrderServiceTest`)

### Immutability

**Prefer immutable data structures:**
- Use `val` over `var` whenever possible
- Use `data class` for immutable data transfer objects
- Use immutable collections: `listOf()`, `mapOf()`, `setOf()`
- When mutation needed, use mutable versions explicitly: `mutableListOf()`, etc.

**Example:**
```kotlin
// ✅ Good: Immutable
data class ScoreResult(
    val className: String,
    val score: Int,
    val penalties: List<Penalty>
)

// ❌ Bad: Mutable by default
data class ScoreResult(
    var className: String,
    var score: Int,
    val penalties: MutableList<Penalty>
)
```

### Null Safety

**Avoid `!!` operator:**
- Use safe calls `?.` for nullable access
- Use Elvis operator `?:` for default values
- Use `requireNotNull()` or `checkNotNull()` with descriptive messages
- Prefer non-nullable types in APIs

**Examples:**
```kotlin
// ✅ Good
val name = config.projectName ?: "unknown"
val dir = requireNotNull(projectDir) { "Project directory must be specified" }

// ❌ Bad
val name = config.projectName!!
```

### Function Design

Apply the same standards from CODING_PRACTICES.md:
- **Maximum 20 lines per function** (excluding blanks/braces)
- Prefer expression bodies for simple functions
- Use named arguments for functions with multiple parameters
- Default parameter values where appropriate

**Examples:**
```kotlin
// ✅ Good: Expression body for simple function
fun calculateScore(penalties: Int): Int = 
    (100 - penalties).coerceIn(0, 100)

// ✅ Good: Named arguments for clarity
fun generateReport(
    scores: List<Score>,
    outputDir: Path,
    format: ReportFormat = ReportFormat.MARKDOWN
)
```

### Extension Functions

**Use appropriately:**
- Enhance readability when operation is conceptually "on" the receiver
- Don't overuse - maintain discoverability
- Keep in appropriate util packages or companion objects
- Document well if not obvious

**Example:**
```kotlin
// ✅ Good: Natural extension
fun Path.ensureDirectory(): Path {
    if (!exists()) createDirectories()
    return this
}

// ❌ Bad: Unclear extension
fun String.process(): Result // What does this do?
```

### Data Classes and Sealed Classes

**Use data classes for:**
- DTOs (Data Transfer Objects)
- Configuration models
- Immutable value objects
- Automatically gets `equals()`, `hashCode()`, `toString()`, `copy()`

**Use sealed classes for:**
- Restricted type hierarchies
- Result types (Success/Failure patterns)
- Exhaustive `when` expressions

**Example:**
```kotlin
sealed class ParseResult {
    data class Success(val findings: List<Finding>) : ParseResult()
    data class Failure(val error: String) : ParseResult()
}
```

### Coroutines

**Use for async operations (if needed):**
- Parallel I/O operations
- Concurrent API calls
- Use structured concurrency
- Handle cancellation properly
- Prefer `suspend` functions over returning `Deferred`

### Collections and Sequences

**Prefer idiomatic collection operations:**
- Use `map`, `filter`, `fold`, etc. over manual loops
- Use sequences for large collections or chained operations
- Leverage `associateBy`, `groupBy`, `partition` for clarity

**Example:**
```kotlin
// ✅ Good: Idiomatic
val scoresByClass = findings
    .groupBy { it.className }
    .mapValues { (_, findings) -> calculateScore(findings) }

// ❌ Bad: Imperative
val scoresByClass = mutableMapOf<String, Int>()
for (finding in findings) {
    // manual grouping logic...
}
```

### Exception Handling

**Kotlin patterns:**
- Use `runCatching` for try-catch blocks that return Result
- Throw specific exception types
- Document thrown exceptions in KDoc
- Use `use` for auto-closeable resources (replaces try-with-resources)

**Example:**
```kotlin
fun readConfig(path: Path): Result<Config> = runCatching {
    path.toFile().inputStream().use { stream ->
        objectMapper.readValue(stream, Config::class.java)
    }
}
```

### Documentation (KDoc)

**Requirements:**
- All public classes, functions, and properties must have KDoc
- Use KDoc format (similar to Javadoc):
  ```kotlin
  /**
   * Calculates the quality score for a class based on findings.
   *
   * @param findings List of code quality findings
   * @param weights Scoring weights for each category
   * @return Score between 0 and 100
   * @throws IllegalArgumentException if weights are invalid
   */
  fun calculateScore(findings: List<Finding>, weights: Weights): Int
  ```
- Include examples for complex APIs
- Document non-obvious behavior

### Testing in Kotlin

**Framework:** JUnit 5
- Use `@Test` annotation
- Leverage Kotlin features in tests (named arguments, backticks for test names)
- Consider MockK for mocking (more Kotlin-friendly than Mockito)
- Data classes simplify test assertions

**Example:**
```kotlin
@Test
fun `should calculate correct score with multiple penalties`() {
    // Given
    val findings = listOf(
        Finding("Foo.java", 10, Severity.HIGH),
        Finding("Foo.java", 20, Severity.LOW)
    )
    
    // When
    val score = scorer.calculateScore(findings)
    
    // Then
    assertEquals(82, score)
}
```

### Architecture Testing with ArchUnit

ArchUnit enforces architectural constraints as standard JUnit 5 tests: layer boundaries, package cycles, dependency direction, and naming conventions. ArchUnit has first-class Kotlin support and analyzes compiled bytecode, so data classes, companion objects, and extension functions are all visible.

- **Full documentation**: [ARCHUNIT_STANDARDS.md](./ARCHUNIT_STANDARDS.md)
- **Configuration**: `config/archunit/archunit.properties`
- **Dependency**: `com.tngtech.archunit:archunit-junit5:1.4.1` (test scope)
- **Note**: Kotlin `internal` visibility compiles to `public` + `@JvmSynthetic` -- ArchUnit sees these as public. Be aware when writing visibility-based rules.

Use detekt for Kotlin code style (naming, complexity, formatting) and ArchUnit for architecture enforcement. They serve complementary purposes.

### Gradle Kotlin DSL

**Use `build.gradle.kts`:**
- Type-safe build configuration
- Leverage IDE support
- Use explicit types where ambiguity exists
- Organize dependencies logically

**Example:**
```kotlin
plugins {
    kotlin("jvm") version "2.3.0"
    application
}

dependencies {
    implementation("com.github.ajalt.clikt:clikt:4.2.1")
    implementation("com.fasterxml.jackson.module:jackson-module-kotlin:2.15.2")
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
}
```

## Code Quality Tools

For the overarching static analysis philosophy, zero-tolerance policy, suppression strategy, incremental adoption, and cross-language tool matrix, see [STATIC_ANALYSIS_STANDARDS.md](./STATIC_ANALYSIS_STANDARDS.md). This section covers Kotlin-specific configuration and integration.

**Static Analysis:**
- **detekt**: Primary Kotlin static analysis tool (comprehensive rule set)
- **PMD**: Supplementary analysis (limited Kotlin support: 2 rules)
- **ktlint**: Formatting and linting
- **ArchUnit**: Architecture testing as unit tests -- layer boundaries, package cycles, dependency direction (see [ARCHUNIT_STANDARDS.md](./ARCHUNIT_STANDARDS.md))

**Same rules apply:**
- 20-line method maximum
- 0-2 private method guideline
- 80%+ unit test coverage (unit tests only -- integration/E2E tests do not count toward coverage)
- No duplicated code

### detekt vs PMD: When to Use Each

| Concern | Tool | Why |
|---------|------|-----|
| Complexity (method length, class size, cyclomatic) | **detekt** | Full Kotlin AST support with configurable thresholds |
| Naming conventions | **detekt** | Understands Kotlin naming patterns (backtick tests, companion objects) |
| Style and idioms | **detekt** | Kotlin-specific rules (scope functions, expression bodies, etc.) |
| Performance | **detekt** | Detects spread operator misuse, `ForEachOnRange`, sequences |
| Potential bugs | **detekt** | Nullable type safety, unreachable code, mutable state issues |
| Exception handling | **detekt** | Swallowed exceptions, too-generic catch/throw |
| Coroutine correctness | **detekt** | `GlobalScope` usage, `sleep` vs `delay`, dispatcher injection |
| KDoc documentation | **detekt** | Undocumented public APIs, outdated docs |
| Function name length | **PMD** | `FunctionNameTooShort` (min 3 chars) |
| equals/hashCode contract | **PMD** | `OverrideBothEqualsAndHashcode` (catches manual overrides) |

**Recommendation**: Run both tools. detekt handles the vast majority of analysis; PMD catches two additional edge cases that detekt does not duplicate.

### detekt Configuration

This repo provides a curated detekt configuration at `config/detekt/detekt.yml`. Thresholds are aligned with our engineering standards.

**Key thresholds enforced:**

| Metric | Threshold | Standard Reference |
|--------|-----------|-------------------|
| Cyclomatic complexity | 10 per method | CODING_PRACTICES.md |
| Cognitive complexity | 15 per method | CODING_PRACTICES.md |
| Method length | 20 lines | KOTLIN_STANDARDS.md |
| Class size | 300 lines | CODING_PRACTICES.md |
| Parameter count | 5 max (5 triggers) | CODING_PRACTICES.md |
| Nesting depth | 3 levels | CODING_PRACTICES.md |
| Max return statements | 3 | CODING_PRACTICES.md |
| String literal duplication | 3 max | DRY principle |
| Max line length | 120 chars | Kotlin conventions |

**Rule sets enabled:**
- **Complexity** -- method length, class size, cyclomatic/cognitive complexity, parameter count, nesting depth
- **Coroutines** -- `GlobalScope` usage, dispatcher injection, `sleep` vs `delay`
- **Empty Blocks** -- empty catch/if/when/for/while/try blocks
- **Exceptions** -- too-generic catch/throw, swallowed exceptions, stack trace preservation
- **Naming** -- class/function/variable naming patterns, package naming, boolean prefixes
- **Performance** -- spread operator, `ForEachOnRange`, array primitives, sequences
- **Potential Bugs** -- null safety, unreachable code, mutable collections, platform types
- **Style** -- magic numbers, wildcard imports, unused code, expression bodies, idiomatic Kotlin
- **Comments** -- undocumented public APIs, outdated KDoc, deprecated block tags

### PMD 7 Kotlin Configuration

This repo provides a Kotlin PMD 7 ruleset at `config/pmd/kotlin-ruleset.xml`. PMD 7 has limited Kotlin support (2 rules across 2 categories):

- **Best Practices**: `FunctionNameTooShort` -- function names must be at least 3 characters
- **Error Prone**: `OverrideBothEqualsAndHashcode` -- must override both or neither

### Gradle Integration

```kotlin
// build.gradle.kts
plugins {
    kotlin("jvm") version "2.3.0"
    id("io.gitlab.arturbosch.detekt") version "1.23.8"
    pmd
}

// detekt configuration
detekt {
    config.setFrom("config/detekt/detekt.yml")
    buildUponDefaultConfig = true  // Use our config on top of defaults
    allRules = false               // Only activate rules marked active: true
    parallel = true                // Faster analysis on multi-core machines
}

tasks.withType<io.gitlab.arturbosch.detekt.Detekt>().configureEach {
    reports {
        html.required.set(true)
        xml.required.set(true)
        sarif.required.set(true)
    }
}

// PMD configuration (supplementary)
pmd {
    toolVersion = "7.21.0"
    ruleSetFiles = files("config/pmd/kotlin-ruleset.xml")
    ruleSets = listOf()  // Clear defaults -- use only our custom ruleset
    isIgnoreFailures = false
    isConsoleOutput = true
}

tasks.withType<Pmd> {
    // PMD needs the Kotlin module for Kotlin file analysis
    reports {
        xml.required.set(true)
        html.required.set(true)
    }
}
```

Run analysis:
```bash
./gradlew detekt           # Run detekt on all sources
./gradlew detektMain       # Run detekt on main sources only
./gradlew detektTest       # Run detekt on test sources only
./gradlew pmdMain          # Run PMD on main sources
./gradlew check            # Runs both as part of the check lifecycle
```

### Suppression Strategies

#### detekt Suppression

When a rule produces a false positive, suppress at the narrowest scope:

```kotlin
// Suppress a specific rule on a function
@Suppress("TooGenericExceptionCaught")  // Justified: top-level error handler
fun handleRequest(request: Request): Response {
    return try {
        processRequest(request)
    } catch (e: Exception) {
        Response.error(e.message ?: "Unknown error")
    }
}

// Suppress on a class
@Suppress("TooManyFunctions")  // Justified: test class with many test cases
class OrderServiceTest { ... }
```

**Guidelines:**
- Always include a justification comment explaining WHY the suppression is needed
- Suppress at the narrowest scope possible (function > class > file)
- Never suppress rules globally in `detekt.yml` to hide violations -- fix the code instead
- Use `@Suppress("RuleName")` (Kotlin standard annotation)
- Track suppressions in code reviews
- Consider `//noinspection` for IDE-level suppressions only

#### PMD Suppression

```kotlin
// Suppress with annotation
@SuppressWarnings("PMD.FunctionNameTooShort")  // Justified: domain-specific abbreviation
fun tx(): Transaction { ... }

// Suppress with NOPMD comment (use sparingly)
fun eq(other: Any?): Boolean = this == other  // NOPMD - intentional short name for DSL
```

#### Baseline Files

For existing projects adopting these standards, use detekt's baseline feature to track pre-existing issues without blocking CI:

```bash
# Generate baseline of current violations
./gradlew detektBaseline

# detekt will then only report NEW violations
```

Configure in `build.gradle.kts`:
```kotlin
detekt {
    baseline = file("config/detekt/baseline.xml")
}
```

**Important**: Baseline files are a migration tool, not a permanent suppression mechanism. Plan to eliminate baseline violations over time.

## Common Kotlin Idioms

**Scope Functions:**
- `apply`: Configure objects
- `let`: Transform or null-safe operations
- `run`: Execute block and return result
- `also`: Side effects
- Use appropriately - don't overuse

**Other Idioms:**
- Destructuring for data classes: `val (name, score) = result`
- `when` expressions instead of complex if-else chains
- String templates: `"Score: $score"` or `"Score: ${obj.score}"`
- Range expressions: `if (score in 0..100)`
- Elvis with return/throw: `val dir = projectDir ?: return`

## SOLID Principles Notes

Use the guide in `docs/SOLID_PRINCIPLES.md` and apply these Kotlin-specific practices:
- **SRP**: Use data classes for focused value objects; extract responsibilities into separate classes with constructor injection.
- **OCP**: Use sealed interfaces with `when` for known type hierarchies (compiler-enforced exhaustiveness); use interfaces + implementations for open extension.
- **LSP**: Sealed classes/interfaces help control substitution; avoid throwing `UnsupportedOperationException` in overrides -- redesign the hierarchy instead.
- **ISP**: Kotlin supports multiple interface implementation natively; keep interfaces small (1-3 methods) and compose them.
- **DIP**: Use constructor parameters with interface types; leverage default parameter values for production defaults while enabling test injection.

## Design Patterns Notes

Use the catalog in `docs/DESIGN_PATTERNS.md` and apply these Kotlin-specific practices:
- **Strategy/State**: Prefer sealed interfaces with `when` for exhaustive handling.
- **Builder**: Prefer named arguments and default parameters before introducing a builder.
- **Singleton**: Use `object` declarations; avoid global mutable state.
- **Decorator/Proxy**: Use delegation (`by`) to compose behavior cleanly.
- **Factory Method**: Use companion object factories for clarity and validation.

## Kotlin 2.3.0 Features

Leverage modern Kotlin features:
- Context receivers (if appropriate)
- Improved type inference
- Inline value classes for type safety
- Follow Kotlin 2.0+ idioms

## Related Documents

- [CODING_PRACTICES.md](./CODING_PRACTICES.md) -- Language-agnostic coding standards
- [SOLID_PRINCIPLES.md](./SOLID_PRINCIPLES.md) -- SOLID principles with multi-language examples
- [DESIGN_PATTERNS.md](./DESIGN_PATTERNS.md) -- Design patterns guidance
- [STATIC_ANALYSIS_STANDARDS.md](./STATIC_ANALYSIS_STANDARDS.md) -- Static analysis philosophy and cross-language tool matrix
- [ARCHUNIT_STANDARDS.md](./ARCHUNIT_STANDARDS.md) -- Architecture testing with ArchUnit (Java/Kotlin)

---

**Last Updated**: February 19, 2026  
**Version**: 1.2  
**Kotlin Version**: 2.3.0

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
- **Maximum 15 lines per function** (excluding blanks/braces)
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

**Static Analysis:**
- **ktlint**: Formatting and linting
- **detekt**: Static code analysis
- Configure to enforce these standards

**Same rules apply:**
- 15-line method maximum
- 0-2 private method guideline
- 80%+ test coverage

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

---

**Last Updated**: February 16, 2026  
**Version**: 1.1  
**Kotlin Version**: 2.3.0

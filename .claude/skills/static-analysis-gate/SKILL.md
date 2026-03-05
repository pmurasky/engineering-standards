---
name: static-analysis-gate
description: Run PMD, detekt, and Checkstyle as a hard gate before commit readiness.
argument-hint: "[optional-path-or-module]"
disable-model-invocation: true
---

Run static-analysis enforcement for the current repository or the requested scope.

Scope: $ARGUMENTS

<HARD-GATE>
Do NOT report pass status when any configured static-analysis tool reports violations.

Blocking policy:
1. BLOCKED (critical): Analyzer execution/configuration failed, report parsing failed, or security/error-prone violations are reported.
2. BLOCKED (important): Any PMD, detekt, Checkstyle, or CPD violation is reported.
3. NOT CONFIGURED: No supported analyzer is configured for the detected stack.

Zero-tolerance rule:
- PMD/detekt/Checkstyle violations are hard failures for commit readiness.
- CPD violations above configured thresholds are hard failures.
</HARD-GATE>

Detection and execution:
1. Detect available analyzers from repo signals:
   - PMD config: `config/pmd/` (for Java/Kotlin) and/or build tasks (`pmdMain`, `pmdCheck`)
   - detekt config: `config/detekt/detekt.yml` and/or build task (`detekt`)
   - Checkstyle config: `config/checkstyle/checkstyle.xml` and/or build tasks (`checkstyleMain`, `checkstyle`)
2. Detect build tool and run the smallest reliable command set:
   - Gradle: prefer targeted tasks (`./gradlew pmdMain detekt checkstyleMain`) then fall back to `./gradlew check`
   - Maven: prefer analyzer goals (`mvn pmd:check checkstyle:check`) and project-specific detekt plugin goal if configured
3. If a configured tool cannot be executed, mark BLOCKED (critical) with exact missing command/task details.

Severity classification output:
- critical: tool/config failures, parsing failures, or security/error-prone categories
- important: all other analyzer violations
- info: tool intentionally not configured for current stack

Pre-commit integration:
1. Run this gate as part of pre-commit readiness, alongside tests/build/lint.
2. If status is BLOCKED, pre-commit result must be NOT READY.
3. Report tool-by-tool evidence (command, outcome, key violation summary).
4. Only READY when static-analysis status is PASS or NOT CONFIGURED.

Output format:
1. Status: PASS, BLOCKED, or NOT CONFIGURED
2. Tool matrix:
   - Tool name
   - Detected config/task evidence
   - Command executed
   - Outcome (PASS/FAIL/NOT CONFIGURED)
   - Severity classification (critical/important/info)
3. Blocking findings first (if any)
4. Required next action

Required references:
- `docs/STATIC_ANALYSIS_STANDARDS.md`
- `docs/PRE_COMMIT_CHECKLIST.md`
- `docs/AI_AGENT_WORKFLOW.md`

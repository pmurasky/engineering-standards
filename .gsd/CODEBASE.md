# Codebase Map

Generated: 2026-04-28T22:59:43Z | Files: 176 | Described: 0/176
<!-- gsd:codebase-meta {"generatedAt":"2026-04-28T22:59:43Z","fingerprint":"4397fdd89d630283e93275cef5105f24df31906f","fileCount":176,"truncated":false} -->

### (root)/
- `.gitignore`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `devops-spec.md`
- `Makefile`
- `opencode.json`
- `README.md`

### .clinerules/
- `.clinerules/engineering-standards.md`
- `.clinerules/nextjs.md`
- `.clinerules/typescript.md`

### .github/
- `.github/CODEOWNERS`
- `.github/copilot-instructions.md`

### .github/instructions/
- `.github/instructions/code-quality.instructions.md`
- `.github/instructions/java.instructions.md`
- `.github/instructions/kotlin.instructions.md`
- `.github/instructions/micro-commit.instructions.md`
- `.github/instructions/nextjs.instructions.md`
- `.github/instructions/typescript.instructions.md`

### .github/workflows/
- `.github/workflows/upstream-lock-validation.yml`

### .opencode/
- `.opencode/.gitignore`
- `.opencode/package-lock.json`
- `.opencode/package.json`

### .opencode/agents/
- `.opencode/agents/pre-commit-check.md`
- `.opencode/agents/spec-compliance-review.md`
- `.opencode/agents/standards-build.md`
- `.opencode/agents/standards-review.md`

### .opencode/commands/
- `.opencode/commands/code-quality.md`
- `.opencode/commands/commit-review.md`
- `.opencode/commands/micro-commit.md`
- `.opencode/commands/new-feature.md`
- `.opencode/commands/pre-commit.md`
- `.opencode/commands/refactor-check.md`
- `.opencode/commands/review-solid.md`
- `.opencode/commands/tdd-enforcement.md`
- `.opencode/commands/test-coverage.md`
- `.opencode/commands/two-stage-review.md`

### .opencode/skills/code-quality/
- `.opencode/skills/code-quality/SKILL.md`

### .opencode/skills/commit-review/
- `.opencode/skills/commit-review/SKILL.md`

### .opencode/skills/micro-commit/
- `.opencode/skills/micro-commit/SKILL.md`

### .opencode/skills/pre-commit/
- `.opencode/skills/pre-commit/SKILL.md`

### .opencode/skills/refactoring-gate/
- `.opencode/skills/refactoring-gate/SKILL.md`

### .opencode/skills/spec-compliance/
- `.opencode/skills/spec-compliance/SKILL.md`

### .opencode/skills/static-analysis-gate/
- `.opencode/skills/static-analysis-gate/SKILL.md`

### .opencode/skills/tdd-enforcement/
- `.opencode/skills/tdd-enforcement/SKILL.md`

### .opencode/skills/test-coverage/
- `.opencode/skills/test-coverage/SKILL.md`

### config/archunit/
- `config/archunit/archunit.properties`

### config/checkstyle/
- `config/checkstyle/checkstyle.xml`

### config/detekt/
- `config/detekt/detekt.yml`

### config/pmd/
- `config/pmd/java-ruleset.xml`
- `config/pmd/kotlin-ruleset.xml`

### config/spotbugs/
- `config/spotbugs/spotbugs-exclude.xml`

### distribution/
- `distribution/standards-package.json`

### docs/
- *(24 files: 24 .md)*

### docs/adr/
- `docs/adr/0001-superpowers-upstream-sync-model.md`

### docs/diagrams/
- `docs/diagrams/pre-commit-workflow.dot`
- `docs/diagrams/tdd-workflow.dot`

### docs/workflows/
- `docs/workflows/micro-commit.md`
- `docs/workflows/pre-commit.md`
- `docs/workflows/README.md`
- `docs/workflows/tdd-enforcement.md`

### schemas/
- `schemas/upstream-superpowers-lock.schema.json`

### scripts/
- `scripts/install_standards.py`
- `scripts/render-diagrams.sh`
- `scripts/report-token-usage.py`
- `scripts/standards_distribution.py`
- `scripts/sync_superpowers_lock.py`
- `scripts/token-baseline-final.json`
- `scripts/token-baseline.json`
- `scripts/update_standards.py`
- `scripts/validate_upstream_lock.py`

### tests/enforcement_integration/
- `tests/enforcement_integration/helpers.py`
- `tests/enforcement_integration/README.md`
- `tests/enforcement_integration/test_bootstrap_hook.py`
- `tests/enforcement_integration/test_enforcement_gates.py`
- `tests/enforcement_integration/test_standards_distribution_tools.py`
- `tests/enforcement_integration/test_token_usage_report.py`
- `tests/enforcement_integration/test_upstream_lock_tools.py`

### tests/fixtures/claude-project-with-bootstrap/docs/
- `tests/fixtures/claude-project-with-bootstrap/docs/AGENT_BOOTSTRAP.md`

### tests/fixtures/invalid-contracts/empty-contract/
- `tests/fixtures/invalid-contracts/empty-contract/contract.md`

### tests/fixtures/invalid-contracts/missing-sections/
- `tests/fixtures/invalid-contracts/missing-sections/contract.md`

### tests/fixtures/invalid-skills/incomplete-hard-gates/
- `tests/fixtures/invalid-skills/incomplete-hard-gates/SKILL.md`

### tests/fixtures/invalid-skills/missing-contract-reference/
- `tests/fixtures/invalid-skills/missing-contract-reference/SKILL.md`

### tests/fixtures/invalid-skills/missing-hard-gate/
- `tests/fixtures/invalid-skills/missing-hard-gate/SKILL.md`

### tests/fixtures/invalid-skills/wrong-status-vocabulary/
- `tests/fixtures/invalid-skills/wrong-status-vocabulary/SKILL.md`

### upstream/
- `upstream/superpowers.lock.json`

### upstream/superpowers/
- `upstream/superpowers/.gitkeep`

### upstream/superpowers/agents/
- `upstream/superpowers/agents/code-reviewer.md`

### upstream/superpowers/commands/
- `upstream/superpowers/commands/brainstorm.md`
- `upstream/superpowers/commands/execute-plan.md`
- `upstream/superpowers/commands/write-plan.md`

### upstream/superpowers/docs/
- `upstream/superpowers/docs/README.codex.md`
- `upstream/superpowers/docs/README.opencode.md`
- `upstream/superpowers/docs/testing.md`

### upstream/superpowers/docs/plans/
- `upstream/superpowers/docs/plans/2025-11-22-opencode-support-design.md`
- `upstream/superpowers/docs/plans/2025-11-22-opencode-support-implementation.md`
- `upstream/superpowers/docs/plans/2025-11-28-skills-improvements-from-user-feedback.md`
- `upstream/superpowers/docs/plans/2026-01-17-visual-brainstorming.md`

### upstream/superpowers/docs/superpowers/plans/
- `upstream/superpowers/docs/superpowers/plans/2026-01-22-document-review-system.md`
- `upstream/superpowers/docs/superpowers/plans/2026-02-19-visual-brainstorming-refactor.md`
- `upstream/superpowers/docs/superpowers/plans/2026-03-11-zero-dep-brainstorm-server.md`

### upstream/superpowers/docs/superpowers/specs/
- `upstream/superpowers/docs/superpowers/specs/2026-01-22-document-review-system-design.md`
- `upstream/superpowers/docs/superpowers/specs/2026-02-19-visual-brainstorming-refactor-design.md`
- `upstream/superpowers/docs/superpowers/specs/2026-03-11-zero-dep-brainstorm-server-design.md`

### upstream/superpowers/docs/windows/
- `upstream/superpowers/docs/windows/polyglot-hooks.md`

### upstream/superpowers/hooks/
- `upstream/superpowers/hooks/hooks.json`
- `upstream/superpowers/hooks/run-hook.cmd`
- `upstream/superpowers/hooks/session-start`

### upstream/superpowers/skills/brainstorming/
- `upstream/superpowers/skills/brainstorming/SKILL.md`
- `upstream/superpowers/skills/brainstorming/spec-document-reviewer-prompt.md`
- `upstream/superpowers/skills/brainstorming/visual-companion.md`

### upstream/superpowers/skills/brainstorming/scripts/
- `upstream/superpowers/skills/brainstorming/scripts/frame-template.html`
- `upstream/superpowers/skills/brainstorming/scripts/helper.js`
- `upstream/superpowers/skills/brainstorming/scripts/server.js`
- `upstream/superpowers/skills/brainstorming/scripts/start-server.sh`
- `upstream/superpowers/skills/brainstorming/scripts/stop-server.sh`

### upstream/superpowers/skills/dispatching-parallel-agents/
- `upstream/superpowers/skills/dispatching-parallel-agents/SKILL.md`

### upstream/superpowers/skills/executing-plans/
- `upstream/superpowers/skills/executing-plans/SKILL.md`

### upstream/superpowers/skills/finishing-a-development-branch/
- `upstream/superpowers/skills/finishing-a-development-branch/SKILL.md`

### upstream/superpowers/skills/receiving-code-review/
- `upstream/superpowers/skills/receiving-code-review/SKILL.md`

### upstream/superpowers/skills/requesting-code-review/
- `upstream/superpowers/skills/requesting-code-review/code-reviewer.md`
- `upstream/superpowers/skills/requesting-code-review/SKILL.md`

### upstream/superpowers/skills/subagent-driven-development/
- `upstream/superpowers/skills/subagent-driven-development/code-quality-reviewer-prompt.md`
- `upstream/superpowers/skills/subagent-driven-development/implementer-prompt.md`
- `upstream/superpowers/skills/subagent-driven-development/SKILL.md`
- `upstream/superpowers/skills/subagent-driven-development/spec-reviewer-prompt.md`

### upstream/superpowers/skills/systematic-debugging/
- `upstream/superpowers/skills/systematic-debugging/condition-based-waiting-example.ts`
- `upstream/superpowers/skills/systematic-debugging/condition-based-waiting.md`
- `upstream/superpowers/skills/systematic-debugging/CREATION-LOG.md`
- `upstream/superpowers/skills/systematic-debugging/defense-in-depth.md`
- `upstream/superpowers/skills/systematic-debugging/find-polluter.sh`
- `upstream/superpowers/skills/systematic-debugging/root-cause-tracing.md`
- `upstream/superpowers/skills/systematic-debugging/SKILL.md`
- `upstream/superpowers/skills/systematic-debugging/test-academic.md`
- `upstream/superpowers/skills/systematic-debugging/test-pressure-1.md`
- `upstream/superpowers/skills/systematic-debugging/test-pressure-2.md`
- `upstream/superpowers/skills/systematic-debugging/test-pressure-3.md`

### upstream/superpowers/skills/test-driven-development/
- `upstream/superpowers/skills/test-driven-development/SKILL.md`
- `upstream/superpowers/skills/test-driven-development/testing-anti-patterns.md`

### upstream/superpowers/skills/using-git-worktrees/
- `upstream/superpowers/skills/using-git-worktrees/SKILL.md`

### upstream/superpowers/skills/using-superpowers/
- `upstream/superpowers/skills/using-superpowers/SKILL.md`

### upstream/superpowers/skills/using-superpowers/references/
- `upstream/superpowers/skills/using-superpowers/references/codex-tools.md`
- `upstream/superpowers/skills/using-superpowers/references/gemini-tools.md`

### upstream/superpowers/skills/verification-before-completion/
- `upstream/superpowers/skills/verification-before-completion/SKILL.md`

### upstream/superpowers/skills/writing-plans/
- `upstream/superpowers/skills/writing-plans/plan-document-reviewer-prompt.md`
- `upstream/superpowers/skills/writing-plans/SKILL.md`

### upstream/superpowers/skills/writing-skills/
- `upstream/superpowers/skills/writing-skills/anthropic-best-practices.md`
- `upstream/superpowers/skills/writing-skills/graphviz-conventions.dot`
- `upstream/superpowers/skills/writing-skills/persuasion-principles.md`
- `upstream/superpowers/skills/writing-skills/render-graphs.js`
- `upstream/superpowers/skills/writing-skills/SKILL.md`
- `upstream/superpowers/skills/writing-skills/testing-skills-with-subagents.md`

### upstream/superpowers/skills/writing-skills/examples/
- `upstream/superpowers/skills/writing-skills/examples/CLAUDE_MD_TESTING.md`

# Engineering Standards

Reusable engineering standards for AI coding agents. Enforces coding practices, SOLID principles, TDD micro-commit workflows, and code quality standards across any project.

**Works with**: OpenCode, Claude Code, Cursor, GitHub Copilot

## Quick Start

### OpenCode One-Line Install

Paste this prompt into OpenCode to install the recommended OpenCode profile into the current project:

> Clone https://github.com/pmurasky/engineering-standards.git and run `python3 engineering-standards/scripts/install_standards.py --target .` from this project's root. The default install should bring in the shared `docs/` knowledge base plus the OpenCode files (`AGENTS.md`, `opencode.json`, `.opencode/agents`, `.opencode/commands`, `.opencode/skills`, and the local OpenCode package files).

### Recommended: managed install/update workflow

The supported downstream flow is a **file-based standards pack committed into your repo**. The installer writes a manifest to `.engineering-standards/manifest.json`, so updates can detect local edits and stay reviewable.

#### Install the default OpenCode profile

```bash
git clone https://github.com/pmurasky/engineering-standards.git
python3 engineering-standards/scripts/install_standards.py --target your-project
```

This installs the default profiles:

- `core` - shared `docs/` knowledge base
- `opencode` - `AGENTS.md`, `opencode.json`, `.opencode/agents/`, `.opencode/commands/`, `.opencode/skills/`, and `.opencode` package files

#### Install other tool profiles

```bash
# Claude Code + shared docs
python3 engineering-standards/scripts/install_standards.py --target your-project --profile claude

# Cursor + shared docs
python3 engineering-standards/scripts/install_standards.py --target your-project --profile cursor

# GitHub Copilot + shared docs
python3 engineering-standards/scripts/install_standards.py --target your-project --profile copilot
```

Profiles are additive. For example, `--profile claude --profile copilot` installs `core` plus both tool surfaces.

#### Update an installed project

```bash
python3 engineering-standards/scripts/update_standards.py --target your-project
```

The updater:

- preserves the installed profile set by default
- refreshes managed files from the current standards checkout
- refuses to overwrite locally modified managed files unless you pass `--force`
- removes stale managed files that are no longer part of the selected profiles

Use `--dry-run` on either script to preview changes before writing them.

#### Pinning a version before install or update

```bash
git -C engineering-standards fetch --tags
git -C engineering-standards checkout v1.0.0
python3 engineering-standards/scripts/update_standards.py --target your-project
```

That keeps downstream updates reviewable without turning the repo into a plugin-only distribution model.

### Advanced/manual options

If you do not want the managed manifest workflow, you can still copy files manually or vendor the repo as a submodule. Those paths remain supported, but they are now considered advanced options because they are more manual to update safely.

#### Manual copy

Copy the `docs/` directory and the config files for your tool:

| Tool | Files to Copy |
|------|--------------|
| **OpenCode** | `AGENTS.md`, `opencode.json`, `.opencode/` |
| **Claude Code** | `CLAUDE.md`, `.claude/` |
| **Cursor** | `.cursor/rules/` (also reads `AGENTS.md`) |
| **GitHub Copilot** | `.github/copilot-instructions.md`, `.github/instructions/` (also reads `AGENTS.md`) |

#### Git submodule

```bash
cd your-project
git submodule add https://github.com/pmurasky/engineering-standards.git engineering-standards
```

Then create thin wrapper files at your project root that reference the submodule, or copy/symlink the relevant tool directories into your project root.

Symlinks keep configs in sync automatically but require that all contributors have the submodule initialized. If you use this path, document it in your project setup instructions.

To update the submodule:

```bash
git submodule update --remote engineering-standards
git add engineering-standards
git commit -m "chore: update engineering standards submodule"
```

## What Gets Enforced

### Code Quality Rules
- Maximum method length: 15-20 lines (see language-specific standards)
- Maximum class length: 300 lines
- Maximum 0-2 private methods per class
- Maximum 5 parameters per method
- No duplicated code (DRY)

### SOLID Principles
- **SRP**: Each class has one reason to change
- **OCP**: Open for extension, closed for modification
- **LSP**: Subtypes substitutable for base types
- **ISP**: Focused interfaces over fat interfaces
- **DIP**: Depend on abstractions, not concrete classes

### TDD Micro-Commit Workflow
Follow the STOP -> RED -> GREEN -> COMMIT -> REFACTOR -> COMMIT cycle for all code changes. See `docs/AI_AGENT_WORKFLOW.md` for the full workflow.

### Commit Standards
- One logical change per commit
- Conventional Commits format: `<type>(<scope>): <description>`
- Every commit is production-ready

## Project Structure

```
engineering-standards/
├── docs/                               # Knowledge base (tool-agnostic)
│   ├── ADR_STANDARDS.md               # Architecture Decision Records guidance
│   ├── AI_AGENT_WORKFLOW.md           # Micro-commit workflow for AI agents
│   ├── ARCHUNIT_STANDARDS.md          # Architecture testing with ArchUnit
│   ├── CHECKSTYLE_STANDARDS.md        # Checkstyle style enforcement (Java)
│   ├── CLAUDE_MEMORY_STRATEGY.md      # Claude memory hierarchy and token hygiene
│   ├── CODING_PRACTICES.md            # Language-agnostic practices, SOLID & TDD
│   ├── CODING_STANDARDS.md            # Standards index (table of contents)
│   ├── CONVERSION_PLAN_TEMPLATE.md    # Conversion/porting plan template
│   ├── DESIGN_PATTERNS.md             # GoF design patterns catalog and guidance
│   ├── GO_STANDARDS.md                # Go-specific conventions
│   ├── JAVA_STANDARDS.md              # Java-specific conventions
│   ├── KOTLIN_STANDARDS.md            # Kotlin-specific conventions
│   ├── LOGGING_STANDARDS.md           # Structured logging, levels, and PII rules
│   ├── NEXTJS_STANDARDS.md            # Next.js conventions and best practices
│   ├── PRE_COMMIT_CHECKLIST.md        # Pre-commit quality checklist
│   ├── PYTHON_STANDARDS.md            # Python-specific conventions
│   ├── SECURITY_STANDARDS.md          # Security standards (auth, OWASP, API)
│   ├── SOLID_PRINCIPLES.md            # SOLID principles deep-dive (multi-language)
│   ├── SPOTBUGS_STANDARDS.md          # SpotBugs bytecode bug detection (Java)
│   ├── STATIC_ANALYSIS_STANDARDS.md   # Static analysis (PMD, detekt, CPD)
│   ├── TYPESCRIPT_STANDARDS.md        # TypeScript/JavaScript conventions
│   └── diagrams/                      # GraphViz workflow diagrams
│       ├── pre-commit-workflow.dot
│       ├── pre-commit-workflow.svg
│       ├── tdd-workflow.dot
│       └── tdd-workflow.svg
│
├── config/                             # Static analysis configuration files
│   ├── archunit/
│   │   └── archunit.properties        # ArchUnit configuration
│   ├── checkstyle/
│   │   └── checkstyle.xml             # Checkstyle rules
│   ├── detekt/
│   │   └── detekt.yml                 # detekt (Kotlin) configuration
│   ├── pmd/
│   │   ├── java-ruleset.xml           # PMD Java ruleset
│   │   └── kotlin-ruleset.xml         # PMD Kotlin ruleset
│   └── spotbugs/
│       └── spotbugs-exclude.xml       # SpotBugs exclusion filters
│
├── .opencode/                          # OpenCode package, agents, commands, skills
│   ├── .gitignore                      # Keeps local node_modules untracked
 │   ├── agents/
 │   │   ├── spec-compliance-review.md   # Subagent: stage-1 requirement compliance
 │   │   ├── standards-build.md         # Primary: writes code following standards
 │   │   ├── standards-review.md        # Subagent: stage-2 code-quality review
 │   │   └── pre-commit-check.md        # Subagent: pre-commit validation
│   ├── bun.lock                        # Optional Bun lockfile for OpenCode package deps
 │   ├── commands/
 │   │   ├── code-quality.md            # /code-quality
│   │   ├── commit-review.md           # /commit-review
│   │   ├── micro-commit.md            # /micro-commit
│   │   ├── new-feature.md             # /new-feature
│   │   ├── pre-commit.md              # /pre-commit
│   │   ├── refactor-check.md          # /refactor-check
 │   │   ├── review-solid.md            # /review-solid
 │   │   ├── tdd-enforcement.md         # /tdd-enforcement
 │   │   ├── test-coverage.md           # /test-coverage
 │   │   └── two-stage-review.md        # /two-stage-review
│   ├── package-lock.json               # npm lockfile for reproducible plugin installs
│   ├── package.json                    # OpenCode local package manifest
│   └── skills/
│       ├── code-quality/SKILL.md
│       ├── commit-review/SKILL.md
│       ├── micro-commit/SKILL.md
│       ├── pre-commit/SKILL.md
│       ├── refactoring-gate/SKILL.md
│       ├── spec-compliance/SKILL.md
│       ├── static-analysis-gate/SKILL.md
│       ├── tdd-enforcement/SKILL.md
│       └── test-coverage/SKILL.md
│
├── .claude/                            # Claude Code config
│   ├── agents/
│   │   ├── spec-compliance-review.md   # Stage-1 requirement compliance
│   │   ├── standards-build.md         # Implementation-focused subagent
│   │   ├── standards-review.md        # Stage-2 code-quality subagent
│   │   └── pre-commit-check.md        # Commit readiness subagent
│   ├── hooks/
│   │   └── block-destructive-rm.sh    # Conservative Bash safety hook
│   ├── rules/
│   │   ├── code-review.md
│   │   ├── commit-message.md
│   │   ├── java.md
│   │   ├── kotlin.md
│   │   ├── micro-commit-workflow.md
│   │   ├── nextjs.md
│   │   ├── refactoring.md
│   │   ├── testing.md
│   │   └── typescript.md
│   ├── skills/
│   │   ├── code-quality/SKILL.md
│   │   ├── commit-review/SKILL.md
│   │   ├── micro-commit/SKILL.md
│   │   ├── pre-commit/SKILL.md
│   │   ├── refactoring-gate/SKILL.md
│   │   ├── spec-compliance/SKILL.md
│   │   ├── static-analysis-gate/SKILL.md
│   │   ├── tdd-enforcement/SKILL.md
│   │   └── test-coverage/SKILL.md
│   └── settings.json                   # Claude Code hook configuration
│
├── .clinerules/                        # Cline rules
│   ├── engineering-standards.md
│   ├── nextjs.md
│   └── typescript.md
│
├── .cursor/rules/                      # Cursor rules
│   ├── code-review.md
│   ├── engineering-standards.md
│   ├── java.md
│   ├── kotlin.md
│   ├── nextjs.md
│   └── typescript.md
│
├── .github/                            # GitHub Copilot instructions
│   ├── copilot-instructions.md
│   ├── instructions/
│   │   ├── code-quality.instructions.md
│   │   ├── java.instructions.md
│   │   ├── kotlin.instructions.md
│   │   ├── micro-commit.instructions.md
│   │   ├── nextjs.instructions.md
│   │   └── typescript.instructions.md
│
├── AGENTS.md                           # OpenCode / Copilot rules
├── CLAUDE.md                           # Claude Code rules
├── CONTRIBUTING.md                     # Contribution guidelines
├── distribution/
│   └── standards-package.json          # Install/update packaging manifest
├── .gitignore                          # Git ignore rules
├── opencode.json                       # OpenCode config
├── scripts/
│   ├── install_standards.py            # Managed downstream install entrypoint
│   ├── render-diagrams.sh              # Optional DOT -> SVG rendering helper
│   ├── report-token-usage.py           # Skill token-budget report script
│   ├── standards_distribution.py       # Shared install/update distribution logic
 │   ├── sync_superpowers_lock.py        # Update upstream lock commit + checksums
│   ├── update_standards.py             # Managed downstream update entrypoint
 │   └── validate_upstream_lock.py       # Validate lockfile against JSON schema
│
├── tests/
│   ├── enforcement_integration/
│   │   ├── README.md                   # How to run enforcement integration tests
│   │   ├── helpers.py                  # Test helpers for hook/skill validation
│   │   ├── test_bootstrap_hook.py      # Bootstrap hook integration tests
│   │   ├── test_enforcement_gates.py   # Pre-commit/TDD/refactor gate tests
│   │   └── test_token_usage_report.py  # Token usage script integration tests
│   └── fixtures/
│       ├── claude-project-with-bootstrap/
│       └── invalid-skills/
└── README.md                           # This file
```

Backlog tracking lives in GitHub Issues (use labels such as `P1: should fix` and `P2: nice to have`).

## Upstream Sync Governance

Use the lock tooling to keep upstream Superpowers ingestion explicit and reviewable:

```bash
# Make targets (preferred)
make validate-lock
make sync-lock

# Direct script entrypoints
# Validate lockfile structure and checksum paths
python3 scripts/validate_upstream_lock.py

# Refresh lockfile with latest upstream commit and mirror checksums
python3 scripts/sync_superpowers_lock.py
```

The lockfile is `upstream/superpowers.lock.json` and schema is `schemas/upstream-superpowers-lock.schema.json`.

## Tool-Specific Features

### OpenCode (Full Feature Set)
OpenCode gets the richest experience with specialized agents and custom commands:

**Agents** (switch with Tab or @mention):
- `standards-build` - Primary coding agent enforcing all standards
- `spec-compliance-review` - Stage 1 review for requirement and acceptance-criteria compliance
- `standards-review` - Stage 2 read-only code quality review against standards
- `pre-commit-check` - Validates staged changes

**Commands**:
- `/code-quality` - Quick code quality scan with scored report
- `/commit-review` - Audit recent commits against engineering standards
- `/micro-commit` - Guide through micro-commit workflow
- `/new-feature` - Guided TDD workflow for new feature implementation
- `/pre-commit` - Run pre-commit quality checklist
- `/refactor-check` - Verify test coverage before refactoring
- `/review-solid` - Check for SOLID violations
- `/tdd-enforcement` - Enforce strict test-first RED -> GREEN -> REFACTOR hard gates
- `/test-coverage` - Analyze test coverage and identify gaps
- `/two-stage-review` - Run stage 1 spec compliance, then stage 2 code quality

**Skills** (load on-demand with `skill` tool):
- `code-quality` - Stage-2 code quality review against repository standards
- `commit-review` - Review staged changes and draft a commit message
- `micro-commit` - Guide one logical, production-ready micro-commit
- `pre-commit` - Run pre-commit readiness checks
- `refactoring-gate` - Block unsafe refactoring when coverage/test prerequisites are missing
- `spec-compliance` - Stage-1 requirement and acceptance-criteria review
- `static-analysis-gate` - Enforce PMD/detekt/Checkstyle when configured
- `tdd-enforcement` - Enforce RED -> GREEN -> REFACTOR sequencing
- `test-coverage` - Review changed-behavior coverage and identify gaps

### Claude Code
Uses a layered model:
- `CLAUDE.md` for concise project-wide policy
- `.claude/rules/` for modular, path-scoped constraints
- `.claude/skills/` for on-demand workflows (slash-command compatible)
- `.claude/agents/` for specialized subagent execution
- `.claude/settings.json` + `.claude/hooks/` for conservative safety automation and session bootstrap context loading

See `docs/CLAUDE_MEMORY_STRATEGY.md` for memory hierarchy and token hygiene guidance.

### Cursor
Uses `.cursor/rules/` with `alwaysApply` and `globs` frontmatter for conditional rule activation. Also reads `AGENTS.md`.

### GitHub Copilot
Uses `.github/copilot-instructions.md` for repo-wide instructions and `.github/instructions/*.instructions.md` with `applyTo` frontmatter for path-scoped rules. Also reads `AGENTS.md`.

## Customization

### Adding Language-Specific Standards

1. Create a new file in `docs/` (e.g., `docs/PYTHON_STANDARDS.md`)
2. Add references to it in each tool's config files
3. For path-scoped tools (Cursor, Copilot, Claude Code), add a rule with the appropriate glob (e.g., `**/*.py`)

### Adding New Standards Documents

Add markdown files to `docs/` and reference them from the tool configs. The `docs/` directory is the single source of truth -- tool configs just point to it.

### Handling Conflicts with Existing Configs

If your project already has tool config files (e.g., an existing `.cursor/rules/` or `CLAUDE.md`), merge the standards content into your existing files rather than overwriting them. Strategies:

- **Append**: Add engineering standards references at the end of your existing config file.
- **Import pattern**: In your existing config, add a line like `For engineering standards, see docs/CODING_PRACTICES.md` and keep your project-specific rules separate.
- **Separate rules**: For tools that support multiple rule files (Claude Code, Cursor, Copilot), add the standards as additional rule files alongside your existing ones. They will not conflict.

If a project-specific rule contradicts an engineering standard (e.g., your project allows 20-line methods instead of 15), the project-specific rule takes precedence. Document the override in your project's config file so the intent is clear.

### Excluding Unneeded Language Files

If you only use a subset of languages, skip copying the files you do not need:

- **Language standards docs**: Only copy the `docs/*_STANDARDS.md` files for languages you use. The core docs (`CODING_PRACTICES.md`, `AI_AGENT_WORKFLOW.md`, etc.) are language-agnostic and always apply.
- **Path-scoped rules**: Only copy language-specific rule files (e.g., `.claude/rules/java.md`, `.cursor/rules/kotlin.md`) for languages present in your project.
- **Glob coverage**: The code-review and testing rules use broad globs (`**/*.{kt,java,ts,js,...}`). This is harmless -- rules only activate when matching files exist. No cleanup needed.

### Extending Standards for Your Project

To add project-specific standards on top of the shared ones:

1. Create a `docs/PROJECT_STANDARDS.md` (or similar) in your project with your additions.
2. Reference it from your tool configs alongside the shared standards.
3. For submodule setups, keep project-specific docs outside the submodule directory so they are not overwritten on update.

## Compatibility Matrix

| Feature | OpenCode | Claude Code | Cursor | Copilot |
|---------|----------|-------------|--------|---------|
| Project rules | AGENTS.md | CLAUDE.md | .cursor/rules/ | .github/copilot-instructions.md |
| Path-scoped rules | - | .claude/rules/ | globs frontmatter | applyTo frontmatter |
| Custom agents | .opencode/agents/ | .claude/agents/ | - | - |
| Custom commands | .opencode/commands/ | .claude/skills/ | - | - |
| Skills | .opencode/skills/ | .claude/skills/ | - | - |
| Reads AGENTS.md | Native | - | Fallback | Fallback |
| Reads CLAUDE.md | Fallback | Native | - | - |

## Agent Skills Matrix

This matrix shows the Agent Skills (agentskills.io compliant) available in this repository. The skill catalog is mirrored for Claude Code and OpenCode so both tools can load the same workflow-oriented capability set while `docs/` remains the canonical knowledge base.

| Skill | Claude | OpenCode | References |
|-------|--------|----------|------------|
| **pre-commit** | [`.claude/skills/pre-commit/`](.claude/skills/pre-commit/) | [`.opencode/skills/pre-commit/`](.opencode/skills/pre-commit/) | `references/workflow.md` on Claude, canonical docs on both |
| **micro-commit** | [`.claude/skills/micro-commit/`](.claude/skills/micro-commit/) | [`.opencode/skills/micro-commit/`](.opencode/skills/micro-commit/) | `references/workflow.md` on Claude, canonical docs on both |
| **tdd-enforcement** | [`.claude/skills/tdd-enforcement/`](.claude/skills/tdd-enforcement/) | [`.opencode/skills/tdd-enforcement/`](.opencode/skills/tdd-enforcement/) | `references/workflow.md` on Claude, canonical docs on both |
| **code-quality** | [`.claude/skills/code-quality/`](.claude/skills/code-quality/) | [`.opencode/skills/code-quality/`](.opencode/skills/code-quality/) | Canonical docs |
| **commit-review** | [`.claude/skills/commit-review/`](.claude/skills/commit-review/) | [`.opencode/skills/commit-review/`](.opencode/skills/commit-review/) | Canonical docs |
| **refactoring-gate** | [`.claude/skills/refactoring-gate/`](.claude/skills/refactoring-gate/) | [`.opencode/skills/refactoring-gate/`](.opencode/skills/refactoring-gate/) | Canonical docs |
| **spec-compliance** | [`.claude/skills/spec-compliance/`](.claude/skills/spec-compliance/) | [`.opencode/skills/spec-compliance/`](.opencode/skills/spec-compliance/) | Canonical docs |
| **static-analysis-gate** | [`.claude/skills/static-analysis-gate/`](.claude/skills/static-analysis-gate/) | [`.opencode/skills/static-analysis-gate/`](.opencode/skills/static-analysis-gate/) | Canonical docs |
| **test-coverage** | [`.claude/skills/test-coverage/`](.claude/skills/test-coverage/) | [`.opencode/skills/test-coverage/`](.opencode/skills/test-coverage/) | Canonical docs |

### Agent Skills Specification

All skills comply with [agentskills.io](https://agentskills.io):
- Frontmatter contains only `name` and `description`
- Description includes trigger phrases for invocation
- Maximum 500 lines (all skills are under 100 lines)
- Self-contained with inline instructions
- Optional `references/` folder for detailed documentation
- Hard Gates and Status Vocabulary sections

### Legacy Canonical Contracts

The `docs/workflows/` directory retains canonical contract documentation for reference:
- `docs/workflows/pre-commit.md`
- `docs/workflows/micro-commit.md`
- `docs/workflows/tdd-enforcement.md`

These are now referenced from skill `references/` folders where applicable.

### Enforcement Tests

All skills are validated by [`tests/enforcement_integration/test_enforcement_gates.py`](tests/enforcement_integration/test_enforcement_gates.py):
- Frontmatter compliance (name + description only)
- Line count under 500
- Hard Gates section present
- Status Vocabulary section present
- References folder exists (when applicable)

# Engineering Standards

Reusable engineering standards for AI coding agents. Enforces coding practices, SOLID principles, TDD micro-commit workflows, and code quality standards across any project.

**Works with**: OpenCode, Claude Code, Cursor, GitHub Copilot

## Quick Start

### OpenCode One-Line Install

Paste this prompt into OpenCode to install the standards into your current project:

> Clone https://github.com/pmurasky/engineering-standards.git, copy the `docs/` directory, `AGENTS.md`, `opencode.json`, and the `.opencode/` directory (including agents, commands, and skills) into this project's root.

### Option A: Copy files into your project

Copy the `docs/` directory and the config files for your tool:

```bash
# 1. Clone this repo
git clone https://github.com/pmurasky/engineering-standards.git

# 2. Copy the knowledge base (required for all tools)
cp -r engineering-standards/docs your-project/

# 3. Copy the config files for your tool (see table below)
```

| Tool | Files to Copy |
|------|--------------|
| **OpenCode** | `AGENTS.md`, `opencode.json`, `.opencode/` |
| **Claude Code** | `CLAUDE.md`, `.claude/` |
| **Cursor** | `.cursor/rules/` (also reads `AGENTS.md`) |
| **GitHub Copilot** | `.github/copilot-instructions.md`, `.github/instructions/` (also reads `AGENTS.md`) |


### Option B: Git submodule

```bash
cd your-project
git submodule add https://github.com/pmurasky/engineering-standards.git engineering-standards
```

Then create thin wrapper files at your project root that reference the submodule. Examples for each tool:

<details>
<summary><strong>OpenCode</strong> -- AGENTS.md + opencode.json</summary>

Create `AGENTS.md` at your project root:

```markdown
# Engineering Standards

See engineering-standards/AGENTS.md for the full standards.

Read these files for detailed guidance:
- engineering-standards/docs/AI_AGENT_WORKFLOW.md
- engineering-standards/docs/CODING_PRACTICES.md
- engineering-standards/docs/CODING_STANDARDS.md
- engineering-standards/docs/PRE_COMMIT_CHECKLIST.md
```

Create `opencode.json` at your project root:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "engineering-standards/docs/CODING_PRACTICES.md",
    "engineering-standards/docs/CODING_STANDARDS.md",
    "engineering-standards/docs/AI_AGENT_WORKFLOW.md",
    "engineering-standards/docs/PRE_COMMIT_CHECKLIST.md"
  ]
}
```

For agents and commands, copy (or symlink) the `.opencode/` directory since agents reference docs by relative path.

</details>

<details>
<summary><strong>Claude Code</strong> -- CLAUDE.md</summary>

Create `CLAUDE.md` at your project root:

```markdown
# Engineering Standards

See engineering-standards/CLAUDE.md for the full standards.

Read these files for detailed guidance:
- engineering-standards/docs/AI_AGENT_WORKFLOW.md
- engineering-standards/docs/CODING_PRACTICES.md
- engineering-standards/docs/CODING_STANDARDS.md
- engineering-standards/docs/PRE_COMMIT_CHECKLIST.md
```

Copy (or symlink) `.claude/` from the submodule (rules, agents, skills, hooks/settings) since Claude Code expects this directory at the project root.

</details>

<details>
<summary><strong>Cursor</strong> -- .cursor/rules/</summary>

Copy (or symlink) `.cursor/rules/` from the submodule. Cursor expects rule files at `.cursor/rules/` in the project root. Update any `docs/` references inside the copied rules to point to `engineering-standards/docs/`.

Alternatively, create a single `.cursor/rules/engineering-standards.md` wrapper:

```markdown
---
description: Engineering standards
alwaysApply: true
---

Follow the engineering standards in engineering-standards/docs/.
Read engineering-standards/docs/CODING_PRACTICES.md for detailed guidance.
```

</details>

<details>
<summary><strong>GitHub Copilot</strong> -- .github/</summary>

Create `.github/copilot-instructions.md`:

```markdown
Follow the engineering standards in engineering-standards/docs/.
Read engineering-standards/docs/CODING_PRACTICES.md for coding practices.
Read engineering-standards/docs/AI_AGENT_WORKFLOW.md for the micro-commit workflow.
```

Copy (or symlink) `.github/instructions/` from the submodule and update `docs/` references to `engineering-standards/docs/`.

</details>

#### Symlink alternative

Instead of copying tool config directories, you can symlink them:

```bash
# Example: symlink Claude Code rules
ln -s engineering-standards/.claude .claude

# Example: symlink Cursor rules
ln -s engineering-standards/.cursor .cursor
```

Symlinks keep configs in sync automatically but require that all contributors have the submodule initialized. Add a note to your project's setup instructions if using symlinks.

#### Updating the submodule

To pull the latest standards into your project:

```bash
# Update to the latest commit on the default branch
git submodule update --remote engineering-standards

# Review changes, then commit the updated submodule reference
git add engineering-standards
git commit -m "chore: update engineering standards submodule"
```

To pin a specific version, check out a tag or commit inside the submodule directory and commit the reference.

For new contributors cloning your project:

```bash
git clone --recurse-submodules <your-project-url>

# Or if already cloned without submodules:
git submodule update --init --recursive
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
│   └── TYPESCRIPT_STANDARDS.md        # TypeScript/JavaScript conventions
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
├── .opencode/                          # OpenCode agents and commands
│   ├── agents/
│   │   ├── standards-build.md         # Primary: writes code following standards
│   │   ├── standards-review.md        # Subagent: read-only code review
│   │   └── pre-commit-check.md        # Subagent: pre-commit validation
│   ├── commands/
│   │   ├── code-quality.md            # /code-quality
│   │   ├── commit-review.md           # /commit-review
│   │   ├── micro-commit.md            # /micro-commit
│   │   ├── new-feature.md             # /new-feature
│   │   ├── pre-commit.md              # /pre-commit
│   │   ├── refactor-check.md          # /refactor-check
│   │   ├── review-solid.md            # /review-solid
│   │   └── test-coverage.md           # /test-coverage
│
├── .claude/                            # Claude Code config
│   ├── agents/
│   │   ├── standards-build.md         # Implementation-focused subagent
│   │   ├── standards-review.md        # Review-focused subagent
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
├── .gitignore                          # Git ignore rules
├── opencode.json                       # OpenCode config
└── README.md                           # This file
```

Backlog tracking lives in GitHub Issues (use labels such as `P1: should fix` and `P2: nice to have`).

## Tool-Specific Features

### OpenCode (Full Feature Set)
OpenCode gets the richest experience with specialized agents and custom commands:

**Agents** (switch with Tab or @mention):
- `standards-build` - Primary coding agent enforcing all standards
- `standards-review` - Read-only code review against standards
- `pre-commit-check` - Validates staged changes

**Commands**:
- `/code-quality` - Quick code quality scan with scored report
- `/commit-review` - Audit recent commits against engineering standards
- `/micro-commit` - Guide through micro-commit workflow
- `/new-feature` - Guided TDD workflow for new feature implementation
- `/pre-commit` - Run pre-commit quality checklist
- `/refactor-check` - Verify test coverage before refactoring
- `/review-solid` - Check for SOLID violations
- `/test-coverage` - Analyze test coverage and identify gaps

**Skills** (load on-demand with `skill` tool):
- `coding-practices` - Language-agnostic coding practices and TDD
- `solid-principles` - SOLID principles with multi-language examples
- `design-patterns` - GoF design patterns catalog
- `pre-commit-checklist` - Pre-commit quality checklist
- `micro-commit-workflow` - TDD micro-commit workflow for AI agents
- `go-standards` - Go-specific conventions
- `java-standards` - Java-specific conventions
- `kotlin-standards` - Kotlin-specific conventions
- `python-standards` - Python-specific conventions

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
| Custom commands | .opencode/commands/ | via .claude/skills/ | - | - |
| Skills | .opencode/skills/ | .claude/skills/ | - | - |
| Reads AGENTS.md | Native | - | - | Yes |
| Reads CLAUDE.md | Fallback | Native | - | Yes |

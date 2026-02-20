# Contributing to Engineering Standards

Thank you for your interest in improving these engineering standards. This document explains how to contribute.

## Project Overview

This project provides reusable engineering standards for AI coding agents. The `docs/` directory is the single source of truth -- tool-specific config files (`.claude/rules/`, `.cursor/rules/`, `.github/instructions/`, `.opencode/`) reference docs but do not duplicate their content.

## How to Contribute

### Reporting Issues

Open a GitHub issue describing:

- What standard or config is affected
- The current behavior or gap
- Your proposed improvement

### Making Changes

1. **Fork and branch**: Create a feature branch from `main`.
2. **Make your changes**: Follow the conventions below.
3. **Test**: Verify that all tool configs still reference valid files and that markdown renders correctly.
4. **Submit a PR**: Describe what you changed and why.

## Conventions

### Directory Structure

- `docs/` -- Standards documents (language-agnostic and language-specific). This is the source of truth.
- `.claude/rules/` -- Claude Code path-scoped rules. Use `globs` frontmatter.
- `.cursor/rules/` -- Cursor rules. Use `alwaysApply` or `globs` frontmatter.
- `.github/instructions/` -- GitHub Copilot path-scoped instructions. Use `applyTo` frontmatter.
- `.github/copilot-instructions.md` -- GitHub Copilot repo-wide instructions.
- `.opencode/agents/` -- OpenCode agent definitions.
- `.opencode/commands/` -- OpenCode slash commands.
- `AGENTS.md` -- Read by OpenCode and GitHub Copilot.
- `CLAUDE.md` -- Read by Claude Code (and Copilot as fallback).

### Adding a New Standards Document

1. Create the markdown file in `docs/` (e.g., `docs/PYTHON_STANDARDS.md`).
2. Add it to the index in `docs/CODING_STANDARDS.md`.
3. Add references to it in all tool configs that should load it.
4. For language-specific standards, add path-scoped rules with the appropriate glob pattern in `.claude/rules/`, `.cursor/rules/`, and `.github/instructions/`.

### Adding a New Language

Follow the pattern established by Java and Kotlin:

1. Create `docs/<LANGUAGE>_STANDARDS.md`.
2. Create tool-specific rule files:
   - `.claude/rules/<language>.md` with `globs: "**/*.<ext>"`
   - `.cursor/rules/<language>.md` with `globs: "**/*.<ext>"`
   - `.github/instructions/<language>.instructions.md` with `applyTo: "**/*.<ext>"`
3. Update globs in existing code-review and testing rules if the file extension is not already included.
4. Update the project structure tree in `README.md`.

### Commit Messages

Use Conventional Commits format:

```
<type>(<scope>): <description>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `perf`, `chore`

Examples:

- `docs(python): add Python standards document`
- `feat(opencode): add test-coverage command`
- `fix(cursor): correct glob pattern in code-review rule`

### Tool Parity

When adding a new rule or capability, add it to all supported tools where possible. Check the compatibility matrix in `README.md` to understand what each tool supports.

## What Makes a Good Standards Document

- **Actionable**: Rules should be concrete and verifiable, not vague aspirations.
- **Concise**: AI agents have context limits. Be direct.
- **Examples**: Show good and bad code examples where helpful.
- **Language-agnostic where possible**: Put general principles in `docs/CODING_PRACTICES.md` and language-specific details in `docs/<LANGUAGE>_STANDARDS.md`.
- **Referenced, not duplicated**: Tool config files should point to `docs/` rather than repeating content.

## Backlog

Enhancements and known gaps are tracked as [GitHub Issues](https://github.com/pmurasky/engineering-standards/issues). Use the issue templates when filing new requests. If your contribution addresses an open issue, reference it in your PR description (e.g., `Closes #12`).

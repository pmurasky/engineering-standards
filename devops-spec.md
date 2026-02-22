# DevOps Spec (Repository-Specific)

## Purpose

This file defines the concrete DevOps contract for this repository.

- Global policy lives in `docs/DEVOPS_STANDARDS.md`.
- This file captures local implementation details.
- If any rule here conflicts with the standards document, standards take precedence.

## Repository Profile

- Repository type: standards/documentation
- Primary deliverable: Markdown standards documents
- CI platform: GitHub Actions

## CI Workflows

- Workflow file: `.github/workflows/ci.yml`
- Triggers:
  - `pull_request` against default branch
  - `push` to default branch
- Concurrency:
  - Cancel in-progress runs for the same branch/PR

## Build and Test Contract

- Required checks:
  - Markdown lint/format check (if configured)
  - Link validation (if configured)
  - Repository policy checks (if configured)
- Failure behavior:
  - Upload reports/artifacts on failure
  - Fail pipeline on any required check failure

## Security Contract

- `permissions` must be explicitly declared in workflows
- Default minimum: `contents: read`
- Third-party actions pinned to full commit SHA
- No hardcoded secrets in workflow files
- Use repository/environment secrets only when required

## Dependency and Supply Chain Contract

- Enable dependency review on pull requests
- Enable Dependabot updates for actions and dependencies
- Enable secret scanning and push protection

## Branch Protection Contract

- Require passing CI checks before merge
- Require review for `.github/workflows/**` changes
- Use CODEOWNERS for workflow path protections

## Docker and Runtime Contract

- Not applicable for this repository by default
- If Docker workflows are introduced, follow:
  - Multi-stage builds
  - Non-root runtime image
  - Build cache optimization and `.dockerignore`

## AI Usage Guardrails

- AI may propose workflow changes, but humans must verify:
  - least-privilege permissions
  - pinned actions
  - no unnecessary new services
  - reproducible behavior and clear failure diagnostics

## Change Log

- 2026-02-21: Initial repository DevOps spec

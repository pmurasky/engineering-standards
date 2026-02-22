# DevOps Standards

## Overview

This document defines language-agnostic DevOps standards for CI/CD, deployment safety, supply chain security, and operational readiness.

These standards are the baseline for all repositories using GitHub Actions.

**When to load this document:** Any change involving workflow files, build/deploy automation, Dockerfiles, release pipelines, environments, or operational controls.

## Scope and Precedence

- **`DEVOPS_STANDARDS.md`** defines cross-repository policy (must/should rules).
- **`devops-spec.md`** defines repository-specific implementation details.
- If there is a conflict, **this standards document wins**.

## Core Principles

### 1. AI-Assisted, Human-Verified

- Use AI to accelerate pipeline authoring and debugging.
- Treat AI output as a draft; maintainers must verify correctness, security, and least privilege.
- Reject AI changes that introduce unnecessary services, broad permissions, or speculative complexity (YAGNI).

### 2. Keep Pipelines Minimal and Deterministic

- Prefer a small number of clear jobs with explicit dependencies.
- Avoid hidden behavior and magic defaults.
- Pin versions for tools and actions to keep outcomes reproducible.

### 3. Security by Default

- Default to least privilege, deny-by-default permissions.
- Use short-lived credentials where possible (OIDC over long-lived secrets).
- Protect CI configuration with review gates.

## Repository DevOps Contract (`devops-spec.md`)

Each repository should include a root-level `devops-spec.md` that captures:

- Runtime and build toolchain versions (for example Java 21, Node 22)
- Required CI steps and exact commands
- Test tiers (unit, integration, optional E2E)
- Container build and runtime requirements
- Artifact and image publishing rules
- Environment model (dev/stage/prod)
- Security controls required for this repository

This file is intentionally concrete and implementation-specific so automation and AI output remain consistent.

### Documentation Repository Note

- In a standards-only repository (like this one), `devops-spec.md` serves as a reference template, not an executable pipeline contract.
- The authoritative `devops-spec.md` must live in each application repository (for example backend/frontend), where real build, test, container, and deploy commands run.
- Enforcement (required checks, branch protection, and workflow behavior) should be configured in those application repositories.

## GitHub Actions Standards

### Workflow Design

- Standard workflow naming:
  - `ci.yml` for continuous integration
  - `release.yml` for release/publish
  - `deploy.yml` for deployment (if used)
- CI must run on pull requests and pushes to the default branch.
- Use path filters only when needed; avoid accidentally skipping required checks.

### Required CI Behavior

- On pull request:
  - Run unit tests and build validation.
  - Run integration tests when configured in the repository spec.
  - Upload test reports/artifacts on failure.
- On default branch push:
  - Run the same validation as pull requests.
  - Publish artifacts only if explicitly defined by repository policy.

### Concurrency and Cost Control

- Use `concurrency` to avoid duplicate runs on stale commits.
- Prefer canceling in-progress runs for the same PR branch.
- Keep cache usage targeted and bounded to avoid cache thrashing.

### Reusable Workflows

- Prefer `workflow_call` reusable workflows for common CI patterns across repositories.
- Keep repository-specific logic in the caller workflow and repo-specific spec.
- Reusable workflows must not elevate permissions beyond caller intent.

## Actions and Dependency Hygiene

- Pin third-party actions to full commit SHAs in production workflows.
- Use trusted actions and review source before adoption.
- Keep actions updated with controlled automation (for example Dependabot).
- Avoid introducing third-party actions when native shell/script is simpler and safer.

## Token Permissions and Secrets

### GITHUB_TOKEN Permissions

- Always set explicit `permissions` at workflow or job scope.
- Start with `contents: read` and add only required scopes.
- Do not grant write scopes unless the job needs them.

### Secrets

- Never hardcode credentials in workflow files.
- Use repository/environment/organization secrets with least access.
- Prefer OIDC for cloud authentication to reduce long-lived static credentials.
- Do not print secrets; mask sensitive non-secret values with `::add-mask::`.

### Cache Safety

- Never cache files containing tokens, credentials, or private keys.
- Use deterministic cache keys derived from lockfiles and runner OS.

## Branch Protection and Change Control

- Protect default branches with required status checks.
- Require PR review for changes under `.github/workflows/**`.
- Use CODEOWNERS for workflow and deployment configuration paths.
- Do not allow automation to bypass PR review controls.

## Test and Quality Gates

- CI must fail the workflow on test/build failures.
- Unit tests are mandatory for every code change.
- Integration tests are mandatory before release/deploy.
- Enforce lint/static checks relevant to the repository stack.

## DevSecOps Baseline

At minimum, repositories should enable:

- Dependency review on pull requests
- Secret scanning and push protection
- Dependency vulnerability alerts/updates (for example Dependabot)

Recommended additions:

- Code scanning (for example CodeQL)
- Artifact attestations for published artifacts/images
- SBOM generation for release artifacts
- Container image scanning when images are produced

## Docker and Container Standards

- Use multi-stage Docker builds for production images.
- Use a minimal runtime image and run as non-root.
- Keep build context small with `.dockerignore`.
- Order layers for caching efficiency (dependencies before source where possible).
- Expose only required ports and avoid unnecessary packages/tools.

## Testcontainers in CI

- Integration tests using Testcontainers require a Docker-compatible runtime.
- On GitHub-hosted Linux runners, Docker support is typically available out of the box.
- Do not enable reusable containers in CI unless there is a documented reason.
- Capture diagnostics (test reports and selective Docker info/logs) on failure.

## Deployment Safety Standards

- Separate build and deploy concerns into distinct jobs/stages.
- Require explicit environment controls for production deployments.
- Support rollback strategy before enabling automated production deploys.
- Use progressive rollout strategies (canary/blue-green) when operationally justified.

## Pre-Merge, Pre-Deploy, Post-Deploy Checklists

### Pre-Merge

- [ ] Workflow changes reviewed by code owners
- [ ] Actions pinned and permissions minimized
- [ ] Required tests pass and failure artifacts are configured
- [ ] No new unmanaged secrets introduced

### Pre-Deploy

- [ ] Build artifacts are from trusted CI runs
- [ ] Required quality and security checks passed
- [ ] Deployment target and change scope are confirmed
- [ ] Rollback path is documented and tested

### Post-Deploy

- [ ] Smoke checks complete successfully
- [ ] Error rate and latency are within expected bounds
- [ ] Alerts and logs show no critical regressions
- [ ] Deployment record and follow-up actions are documented

## Anti-Patterns (Reject)

- Broad default permissions (for example unnecessary write scopes)
- Unpinned third-party actions in production workflows
- Skipping tests for speed without explicit emergency process
- Committing credentials or passing secrets through unsafe channels
- Adding deployment complexity before CI quality gates are stable

## References

- [GitHub Actions secure use](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax-for-github-actions)
- [Reusable workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)
- [Use GITHUB_TOKEN for authentication](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token)
- [Using secrets in workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
- [Dependency review action](https://github.com/actions/dependency-review-action)
- [Docker build cache optimization](https://docs.docker.com/build/cache/optimize/)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Testcontainers runtime requirements](https://java.testcontainers.org/supported_docker_environment/)

---

**Last Updated**: February 21, 2026
**Version**: 1.0

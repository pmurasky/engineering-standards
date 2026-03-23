---
name: pre-commit
description: Run pre-commit readiness checks and summarize blockers before committing. Use when user asks "ready to commit", "pre-commit check", "can I commit", or "validate changes" before committing code.
---

# Pre-Commit Validation

Validate that staged changes meet all required quality gates before committing.

## Hard Gates

Execute all quality gates. These are non-negotiable:

1. **Unit tests MUST pass** (when project test command exists)
2. **Build MUST succeed** (when project build command exists)
3. **Lint MUST pass** (when project lint command exists)
4. **Static analysis MUST pass** (when PMD/detekt/Checkstyle configured)

**Blocking rules:**
- If any required gate fails → output `NOT READY` with blockers listed first
- If command unavailable → report `NOT CONFIGURED` explicitly
- Never recommend commit readiness when required gates fail
- Never create commits during validation

## Workflow

1. Review staging area: `git diff --cached --stat`
2. Execute quality gates:
   - Run unit tests
   - Run build
   - Run lint
   - Run static analysis (if configured)
3. Check coverage: Verify minimum 80% unit test coverage for changed code
4. Verify TDD compliance: Ensure proper RED → GREEN → COMMIT cycle followed
5. Output assessment using status vocabulary

## Status Vocabulary

**Required output format:**
1. **Status**: `READY` or `NOT READY`
2. **Blocking items** (if any): List failures first, most critical to least critical
3. **Evidence**: Commands run and their summarized outcomes
4. **Next actions**: Specific recommendations for addressing blockers

**Status indicators:**
- `READY`: All quality gates pass, safe to commit
- `NOT READY`: One or more quality gates failed
- `NOT CONFIGURED`: Required tools/commands not available

## Fail/Fix/Rerun Loop

When validation fails:
1. Stop immediately - do not proceed to commit
2. Fix blockers in order of priority
3. Rerun pre-commit check after fixes
4. Repeat until all gates pass

## References

- [Full workflow details](references/workflow.md)
- `docs/PRE_COMMIT_CHECKLIST.md` - Comprehensive checklist
- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit philosophy
- `docs/STATIC_ANALYSIS_STANDARDS.md` - Static analysis configuration
- `docs/CODING_PRACTICES.md` - Code quality standards

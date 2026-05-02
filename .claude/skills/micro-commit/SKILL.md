---
name: micro-commit
description: Create one production-ready micro-commit following repository standards. Use when the user asks "commit my changes", "micro-commit", "help me commit", "ready to commit", or "create commit".
---

# Micro-Commit Workflow

Guide creation of production-ready commits containing exactly one logical change.

## Trigger Conditions

- User requests help with committing changes
- Before any commit operation
- When analyzing current changes for commit readiness
- Phrases: "commit my changes", "micro-commit", "help me commit", "ready to commit", "create commit"

## Hard Gates

**Single Logical Change Rule:**
- One logical change per commit (never bundle multiple changes)
- Each commit must represent exactly one of: refactor step, feature implementation, test update, or documentation update
- If multiple logical changes detected → output `SPLIT REQUIRED` with specific breakdown

**Production-Ready Requirements:**
1. All unit tests MUST pass (when project test command exists)
2. Build MUST succeed (when project build command exists)
3. No lint errors (when project lint command exists)
4. Conventional Commits format required for all commit messages

**Blocking rules:**
- If any quality gate fails → output `NOT READY` and list blockers
- If multiple logical changes detected → output `SPLIT REQUIRED` with commit breakdown
- If commit message doesn't follow Conventional Commits → output `MESSAGE INVALID`
- Never create commits during analysis phase
- Never bypass failing tests or build

## Workflow

1. **Change Analysis**: Review staged (`git diff --cached --stat`) and unstaged changes (`git diff --stat`)
2. **Change Classification**: Determine if changes represent one or multiple logical changes
3. **Commit Ordering** (when multiple commits needed):
   - Refactor commits first (structure improvements)
   - Feature commits second (new functionality)
   - Test commits third
   - Documentation commits last
4. **Message Crafting**: Use Conventional Commits format `<type>(<scope>): <description>`
   - Types: feat, fix, refactor, test, docs, perf, chore
   - Scope: Optional but recommended (component/module name)
   - Description: Clear, imperative mood, explain WHAT changed
   - Body: Optional, explain WHY (not what)
5. **Quality Gate Verification**: Run unit tests, build, and lint

## Status Vocabulary

**Required output format:**
1. **Status**: `READY`, `NOT READY`, `SPLIT REQUIRED`, or `MESSAGE INVALID`
2. **Change summary**: What logical changes were detected
3. **Commit plan**: Specific commits to create (if split needed)
4. **Quality gates**: Results of test/build/lint execution
5. **Next actions**: Specific steps to proceed

**Status indicators:**
- `READY`: Single logical change, all quality gates pass, proper message format
- `NOT READY`: Quality gates failed, must fix before committing
- `SPLIT REQUIRED`: Multiple logical changes detected, must separate into individual commits
- `MESSAGE INVALID`: Commit message doesn't follow Conventional Commits format

## Fail/Fix/Rerun Loop

**When quality gates fail:**
1. Stop immediately - do not proceed to commit
2. Fix blockers: Address test failures, build errors, or lint issues
3. Rerun verification: Execute quality gates again after fixes
4. Repeat until all gates pass

**When split required:**
1. Stage selectively using `git add -p` or file-by-file staging
2. Create first commit with one logical change
3. Stage next change and repeat

**Common fix actions:**
- Test failures → fix code or update tests
- Build failures → resolve compilation/syntax errors
- Lint failures → fix code style and formatting issues
- Multiple changes → use selective staging to separate logical changes
- Message format → rewrite to follow Conventional Commits specification

## Tool Adapter Requirements

**All adapters MUST preserve:**
- Single logical change enforcement
- Production-ready quality gates
- Conventional Commits message format
- Status vocabulary and output ordering
- References to canonical documentation

**Adapters MUST NOT:**
- Automatically create commits without explicit user confirmation
- Skip quality gate verification
- Allow multiple logical changes in single commit
- Bypass production-ready requirements

## Token Budget

- **Category**: On-demand workflow
- **Estimated usage**: 600-1000 tokens per invocation
- **Frequency**: Per commit (typically 5-20 times per development session)
- **Optimization**: Keep content minimal, reference canonical docs for detail

## References

- [Full workflow details](references/workflow.md)
- `docs/AI_AGENT_WORKFLOW.md` - Micro-commit philosophy
- `docs/PRE_COMMIT_CHECKLIST.md` - Quality gates checklist
- `docs/CODING_PRACTICES.md` - Production-ready requirements
- `docs/CODING_STANDARDS.md` - Conventional Commits format
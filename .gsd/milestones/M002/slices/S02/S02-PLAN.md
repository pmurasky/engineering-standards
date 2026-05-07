# S02: Update SKILL.md Files

**Goal:** Update all 9 SKILL.md files across both .claude/skills/ and .opencode/skills/ surfaces to be fully Agent Skills spec-compliant: correct frontmatter only (name + description + disable-model-invocation), Use when/Not for within first 30 lines, concrete example, anti-patterns section, no CSO violations, under 500 lines. Priority focus on the 3 thin/non-compliant skills: spec-compliance, commit-review, refactoring-gate.
**Demo:** After this: all 9 SKILL.md files are fully spec-compliant — correct frontmatter, Use when/Not for within 30 lines, examples, anti-patterns, under 500 lines, no external doc redirects.

## Must-Haves

- All 9 skills pass test_enforcement_gates.py. spec-compliance, commit-review, refactoring-gate have Use when/Not for in first 30 lines, examples, anti-patterns, no ## References pointing to docs/. No SKILL.md exceeds 500 lines. disable-model-invocation: true present where appropriate.

## Proof Level

- This slice proves: Automated: python3 -m pytest test_enforcement_gates.py. Manual: spot-check spec-compliance, commit-review, refactoring-gate for Use when/Not for placement.

## Integration Closure

S03 (Archive Canonical Contracts) can only safely run once these files no longer reference docs/workflows/ as live sources.

## Verification

- None — skill content changes. Enforcement test suite validates compliance automatically.

## Tasks

- [ ] **T01: Fix spec-compliance, commit-review, refactoring-gate** `est:45 min`
  Fix the 3 most non-compliant skills first (highest ROI).

For each of spec-compliance, commit-review, refactoring-gate in BOTH .claude/skills/ and .opencode/skills/:
1. Remove legacy frontmatter fields (version, category)
2. Add `disable-model-invocation: true` after name/description
3. Add `## Use when` section within first 30 lines with 3-5 concrete trigger phrases
4. Add `## Not for` section immediately after with 2-3 exclusion cases
5. Remove any `## References` section that points to docs/ paths (CSO fix)
6. Add a `## Example` section with a short realistic scenario
7. Add an `## Anti-patterns` section with 2-3 common misuses

Commit per skill: `fix(skills): bring spec-compliance into Agent Skills compliance`
  - Files: `.claude/skills/spec-compliance/SKILL.md`, `.opencode/skills/spec-compliance/SKILL.md`, `.claude/skills/commit-review/SKILL.md`, `.opencode/skills/commit-review/SKILL.md`, `.claude/skills/refactoring-gate/SKILL.md`, `.opencode/skills/refactoring-gate/SKILL.md`
  - Verify: python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -k 'spec_compliance or commit_review or refactoring_gate' -v OR full suite run — all 3 skills pass

- [x] **T02: Audit remaining 6 skills for compliance gaps** `est:20 min`
  Audit the remaining 6 skills (code-quality, micro-commit, pre-commit, tdd-enforcement, static-analysis-gate, test-coverage) for compliance:
- Check frontmatter has only name + description (+ disable-model-invocation)
- Confirm Use when / Not for present within first 30 lines
- Confirm no ## References pointing to external docs/ paths
- Confirm line count under 500
Document any gaps found.
  - Files: `.claude/skills/code-quality/SKILL.md`, `.claude/skills/micro-commit/SKILL.md`, `.claude/skills/pre-commit/SKILL.md`, `.claude/skills/tdd-enforcement/SKILL.md`, `.claude/skills/static-analysis-gate/SKILL.md`, `.claude/skills/test-coverage/SKILL.md`
  - Verify: Gap document written; no skill silently skipped

- [x] **T03: Apply fixes to remaining 6 skills** `est:30 min`
  Apply any fixes identified in T02 to the remaining 6 skills (both .claude/ and .opencode/ surfaces). If a skill is already fully compliant, mark it PASS and skip. Commit each skill fix individually following micro-commit workflow.
Example commit: `fix(skills): add Use when/Not for to static-analysis-gate`
  - Files: `.claude/skills/code-quality/SKILL.md`, `.opencode/skills/code-quality/SKILL.md`, `.claude/skills/micro-commit/SKILL.md`, `.opencode/skills/micro-commit/SKILL.md`, `.claude/skills/pre-commit/SKILL.md`, `.opencode/skills/pre-commit/SKILL.md`, `.claude/skills/tdd-enforcement/SKILL.md`, `.opencode/skills/tdd-enforcement/SKILL.md`, `.claude/skills/static-analysis-gate/SKILL.md`, `.opencode/skills/static-analysis-gate/SKILL.md`, `.claude/skills/test-coverage/SKILL.md`, `.opencode/skills/test-coverage/SKILL.md`
  - Verify: python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v — all 9 skills pass

- [ ] **T04: Full enforcement test suite green** `est:5 min`
  Full test suite run to confirm all skills pass enforcement gates after all SKILL.md edits.
python3 -m pytest tests/enforcement_integration/ -v
If any skill fails, fix immediately before proceeding to S03.
  - Files: `tests/enforcement_integration/test_enforcement_gates.py`
  - Verify: python3 -m pytest tests/enforcement_integration/ -v — exit code 0, zero failures

## Files Likely Touched

- .claude/skills/spec-compliance/SKILL.md
- .opencode/skills/spec-compliance/SKILL.md
- .claude/skills/commit-review/SKILL.md
- .opencode/skills/commit-review/SKILL.md
- .claude/skills/refactoring-gate/SKILL.md
- .opencode/skills/refactoring-gate/SKILL.md
- .claude/skills/code-quality/SKILL.md
- .claude/skills/micro-commit/SKILL.md
- .claude/skills/pre-commit/SKILL.md
- .claude/skills/tdd-enforcement/SKILL.md
- .claude/skills/static-analysis-gate/SKILL.md
- .claude/skills/test-coverage/SKILL.md
- .opencode/skills/code-quality/SKILL.md
- .opencode/skills/micro-commit/SKILL.md
- .opencode/skills/pre-commit/SKILL.md
- .opencode/skills/tdd-enforcement/SKILL.md
- .opencode/skills/static-analysis-gate/SKILL.md
- .opencode/skills/test-coverage/SKILL.md
- tests/enforcement_integration/test_enforcement_gates.py

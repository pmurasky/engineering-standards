# M001-S01-T01: Agent Skills Compliance — Context & Decisions

## Task Goal
Gather context on current skill structure, identify the target Agent Skills specification, and document all decisions for achieving compliance.

## Current State Analysis

### Skill Inventory (9 skills across .claude/skills/ and .opencode/skills/)

| Skill | Lines | Sections | Has references/ | Claude ↔ OpenCode Diff |
|-------|-------|----------|-----------------|------------------------|
| code-quality | 49 | 5 | No | Content + frontmatter |
| spec-compliance | 53 | 6 | No | Content + frontmatter |
| commit-review | 54 | 6 | No | Content + frontmatter |
| test-coverage | 58 | 6 | No | Content + frontmatter |
| refactoring-gate | 59 | 5 | No | Content + frontmatter |
| pre-commit | 64 | 5 | Yes (67-line workflow.md) | Content + frontmatter |
| static-analysis-gate | 65 | 6 | No | Content + frontmatter |
| micro-commit | 76 | 5 | Yes (132-line workflow.md) | Content + frontmatter |
| tdd-enforcement | 88 | 5 | Yes (105-line workflow.md) | Content + frontmatter |
| **Total** | **566** | — | 3 with references | All 9 differ |

### Frontmatter Compliance

**All 9 skills have Agent Skills-compliant frontmatter:**
- `name`: Present, matches directory name
- `description`: Present, includes trigger phrases

**OpenCode additions (non-compliant per spec):**
- `version: 1.0.0` — Not in spec, should be removed
- `category: <value>` — Not in spec, should be removed

**Claude frontmatter is the compliant baseline.** OpenCode has extra fields that violate the "name and description only" rule.

### Section Structure Compliance

All 9 skills have the required sections:
1. **Title** (`# Skill Name`) — Present
2. **Hard Gates** (`## Hard Gates`) — Present (some use singular `## Hard Gate`)
3. **Workflow/Review Checklist** (`## Workflow` or `## Review Checklist`) — Present
4. **Status Vocabulary/Output Format** (`## Status Vocabulary` or `## Output Format`) — Present
5. **References** (`## References`) — Present with relative paths

### Content Differences: Claude vs OpenCode

**Pattern:** OpenCode versions are often more concise, with:
- Shortened descriptions (fewer trigger phrases)
- Condensed hard gates (numbered list vs prose)
- Removed workflow detail (e.g., commit-review loses explicit workflow steps)
- Added `version` and `category` frontmatter fields

**Example — pre-commit:**
- Claude: 4 bullet hard gates + blocking rules prose
- OpenCode: 5 numbered hard gates (condensed) + no blocking rules section

**Example — micro-commit:**
- Claude: Full single logical change rule + production-ready requirements + blocking rules
- OpenCode: "1. Commit exactly one logical change." (extremely condensed)

### references/ Folder Usage

Three skills use `references/workflow.md`:
- **pre-commit** (67 lines): Detailed workflow steps
- **micro-commit** (132 lines): Extended workflow, fail/fix/rerun loop, token budget
- **tdd-enforcement** (105 lines): Extended workflow, rationalization defense, token budget

These are appropriately factored — SKILL.md stays under 500 lines while detailed docs live in references/.

### Legacy Archive: docs/workflows/

- **Status:** Historical archive, NOT active source of truth
- **Files:** pre-commit.md, micro-commit.md, tdd-enforcement.md
- **README.md:** Explicitly states these are "retained for historical context and learning"
- **Decision:** These should be formally deprecated/archived (not deleted, but clearly marked)

## Target Specification (from docs/CONTRIBUTING-SKILLS.md)

The [agentskills.io](https://agentskills.io) specification requires:

1. **Frontmatter:** Only `name` and `description` (no `version`, `category`, `argument-hint`, etc.)
2. **Description:** Must include trigger phrases ("Use when user asks...")
3. **Max 500 lines** per SKILL.md
4. **Required sections:** Hard Gates, Workflow, Status Vocabulary, References
5. **Self-contained:** Inline instructions, not just references to external docs
6. **Relative paths** for references/
7. **Mirrored skills** should have aligned naming across surfaces

## Enforcement Test Results

```
Ran 42 tests in 0.707s
OK (skipped=2)
```

All enforcement tests pass. The test suite validates:
- Frontmatter has only name and description
- Skills are under 500 lines
- Hard Gates section exists
- Status Vocabulary section exists
- References/ folder exists (when applicable)
- OpenCode and Claude skill names stay in sync

## Decisions Made

### D1: OpenCode Frontmatter Cleanup
**Decision:** Remove `version` and `category` fields from all OpenCode skill frontmatter.
**Rationale:** These fields violate the Agent Skills spec (name + description only).
**Scope:** All 9 OpenCode skills.

### D2: Skill Content Alignment
**Decision:** Keep Claude versions as the canonical source. Update OpenCode versions to match Claude content where they diverge.
**Rationale:** Claude versions are more complete, have better trigger phrases, and fully comply with the spec. OpenCode versions are condensed and sometimes lose important detail.
**Exception:** If OpenCode has a genuinely better phrasing, consider adopting it in Claude (two-way sync).

### D3: references/ Folder Strategy
**Decision:** Keep existing references/ folders for pre-commit, micro-commit, tdd-enforcement. No changes needed.
**Rationale:** These are correctly factored. SKILL.mds stay well under 500 lines. Content is appropriate.

### D4: Legacy docs/workflows/ Archive
**Decision:** Add deprecation headers to the three archived workflow files. Update README.md with clearer archival notice.
**Rationale:** These are historical and could confuse contributors. Clear archival marking prevents accidental updates to dead contracts.
**Scope:** docs/workflows/pre-commit.md, micro-commit.md, tdd-enforcement.md, README.md

### D5: No New Skills Needed
**Decision:** The current 9-skill catalog is complete for the compliance milestone.
**Rationale:** All existing skills are already compliant. No gaps identified.

### D6: Test Maintenance
**Decision:** No test changes needed. Current enforcement tests already validate all compliance requirements.
**Rationale:** Tests pass (42/42). They cover frontmatter, line count, sections, and naming sync.

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| OpenCode skill sync drift continues | High | Medium | Establish single-source-of-truth (Claude) with automated sync |
| Contributors update docs/workflows/ instead of skills | Medium | Medium | Add deprecation headers, update CONTRIBUTING.md |
| Skill line count grows past 500 lines | Low | Medium | Enforce in CI (already tested) |
| OpenCode-specific tooling needs category field | Medium | Low | Document exception if needed, but spec says no |

## Deferred Items

1. **Automated sync script:** Create a script to sync Claude → OpenCode skills (future slice)
2. **CI enforcement:** Add enforcement tests to CI pipeline (future slice)
3. **CONTRIBUTING.md update:** Add explicit "do not update docs/workflows/" guidance (part of D4)
4. **Skill metadata governance:** Review SKILL_METADATA_GOVERNANCE.md for completeness (future)

## Files Involved

**To be modified (D1, D2):**
- `.opencode/skills/*/SKILL.md` (all 9)

**To be modified (D4):**
- `docs/workflows/pre-commit.md`
- `docs/workflows/micro-commit.md`
- `docs/workflows/tdd-enforcement.md`
- `docs/workflows/README.md`

**Reference (no changes):**
- `docs/CONTRIBUTING-SKILLS.md`
- `.claude/skills/*/SKILL.md` (all 9 — canonical source)
- `.claude/skills/*/references/workflow.md` (3 skills)
- `tests/enforcement_integration/test_*.py`

## Verification

- [ ] All OpenCode skills have only `name` + `description` in frontmatter
- [ ] All OpenCode skills match Claude content (or documented exception)
- [ ] All skills under 500 lines
- [ ] Enforcement tests pass
- [ ] Legacy docs/workflows/ clearly marked as archived

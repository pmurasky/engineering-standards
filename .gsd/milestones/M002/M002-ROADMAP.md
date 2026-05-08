# M002: Skills Restructuring

**Vision:** Migrate all 9 project skills from hybrid canonical-contract architecture to strict Agent Skills spec compliance: self-contained SKILL.md files with references/ folders, standard-only frontmatter, Use when/Not for sections, examples, anti-patterns, and no CSO-violating external doc references.

## Success Criteria

- All 9 skills fully Agent Skills spec-compliant on both .claude/skills/ and .opencode/skills/ surfaces
- No legacy frontmatter (version, category) remaining in any skill
- spec-compliance, commit-review, refactoring-gate have Use when/Not for, examples, anti-patterns, and no CSO violations
- docs/workflows/ archived or removed; zero active references remain
- All enforcement tests pass

## Slices

- [x] **S01: S01** `risk:low` `depends:[]`
  > After this: After this: each of the 3 workflow-heavy skills has a references/ directory with workflow.md content; other 6 skills directories are clean and ready for SKILL.md updates.

- [ ] **S02: Update SKILL.md Files** `risk:medium` `depends:[S01]`
  > After this: After this: all 9 SKILL.md files are fully spec-compliant — correct frontmatter, Use when/Not for within 30 lines, examples, anti-patterns, under 500 lines, no external doc redirects.

- [ ] **S03: Archive Legacy Canonical Contracts** `risk:low` `depends:[S02]`
  > After this: After this: docs/workflows/ is either removed or clearly marked as a historical archive; no active skill, agent, or command references it as a live source of truth.

## Boundary Map

Not provided.

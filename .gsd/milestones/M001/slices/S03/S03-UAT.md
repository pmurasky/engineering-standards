# S03: Skills 2.0 Implementation — Fix .opencode skills, update governance docs, complete archival — UAT

**Milestone:** M001
**Written:** 2026-05-02T00:54:57.772Z

## UAT: Skills 2.0 Implementation

### Acceptance Criteria
- [x] All 9 skills migrated to Agent Skills compliance
- [x] All skills have strict frontmatter (name + description only)
- [x] All skills are self-contained with inline instructions
- [x] All skills under 500 lines
- [x] references/ folders exist where applicable
- [x] Canonical contracts preserved in references/
- [x] Enforcement tests validate Agent Skills structure
- [x] CONTRIBUTING-SKILLS.md reflects new architecture
- [x] README.md reflects new architecture
- [x] Old canonical contracts archived in docs/workflows/

### Test Results
```
24 passed, 60 subtests passed in 0.05s
```

### Commits
- 45507b6 refactor(skills): migrate pre-commit skill
- 8d74b84 refactor(skills): migrate micro-commit skill
- 8950a38 refactor(skills): migrate tdd-enforcement skill
- 90ad448 refactor(skills): migrate code-quality skill
- 09eb778 refactor(skills): migrate commit-review skill
- 86b98b1 refactor(skills): migrate refactoring-gate skill
- 09390c6 refactor(skills): migrate spec-compliance skill
- f09946b refactor(skills): migrate static-analysis-gate skill
- 11a1894 refactor(skills): migrate test-coverage skill

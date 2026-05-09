# S02: Update Documentation

**Goal:** Update README.md, CONTRIBUTING-SKILLS.md, and SKILL_AUTHORING_STANDARDS.md to reflect the post-M002 clean architecture and the new CI and scenario test requirements added in S01.
**Demo:** After this: README.md, CONTRIBUTING-SKILLS.md, and SKILL_AUTHORING_STANDARDS.md accurately describe the post-M002 architecture with CI enforcement, scenario tests, and .opencode/ compliance requirements.

## Must-Haves

- README Agent Skills Matrix accurate. CONTRIBUTING-SKILLS.md PR checklist includes scenario tests and CI. SKILL_AUTHORING_STANDARDS.md \u00a78 has example basic.yaml. All docs reference post-M002 architecture only.

## Proof Level

- This slice proves: Manual review of updated docs. Link-check for no broken references. Enforcement tests still green.

## Integration Closure

Closes M003. M009 and M010 proceed on a documented, tested foundation.

## Verification

- None at runtime. Documentation accuracy is the deliverable.

## Tasks

- [ ] **T01: Update README.md** `est:20 min`
  Update README.md:
1. Agent Skills Matrix section: verify all 9 skills listed; update 'references' column if any skills now have references/ folders
2. Remove or annotate any mention of docs/workflows/ as active source of truth; update to 'historical archive'
3. Add a 'Testing' or 'CI' section noting that push/PR triggers enforcement tests via GitHub Actions
4. Verify the Plugin Architecture section still accurate after M002

Commit: `docs(readme): update post-M002 Agent Skills Matrix and CI section`
  - Files: `README.md`
  - Verify: Manual review: all 9 skills in matrix, CI section present, docs/workflows/ not referenced as active

- [ ] **T02: Update CONTRIBUTING-SKILLS.md** `est:20 min`
  Update CONTRIBUTING-SKILLS.md (or CONTRIBUTING.md if that is where skill contribution guidance lives):
1. Add scenario test requirement: every new skill must include tests/skills/scenarios/<name>/basic.yaml
2. Add CI requirement: PRs must pass the CI workflow
3. Add the post-M002 frontmatter requirement (name + description + disable-model-invocation only)
4. Add Use when/Not for placement rule (within first 30 lines)
5. Remove references to canonical contract workflow

Commit: `docs(contributing): add scenario test, CI, and frontmatter requirements to contribution guide`
  - Files: `CONTRIBUTING-SKILLS.md`, `CONTRIBUTING.md`
  - Verify: Manual review: all 4 new requirements present. No mention of docs/workflows/ as active source.

- [ ] **T03: Update SKILL_AUTHORING_STANDARDS.md §8** `est:15 min`
  Update docs/SKILL_AUTHORING_STANDARDS.md §8:
1. Add or update the scenario test section with the exact basic.yaml format/template
2. Note that tests/skills/scenarios/<skill-name>/basic.yaml is mandatory for every skill (PR checklist item)
3. Add that CI enforces this on every push/PR via .github/workflows/ci.yml

Commit: `docs(standards): add scenario test template and CI enforcement notes to SKILL_AUTHORING_STANDARDS`
  - Files: `docs/SKILL_AUTHORING_STANDARDS.md`
  - Verify: Manual review: §8 has YAML example, mandatory requirement stated, CI reference present. File under 500 lines.

- [ ] **T04: Final verification and clean-up** `est:10 min`
  Final check: run enforcement tests, validate no broken links to docs/workflows/ remain in updated docs, confirm all files updated are under size limits.

python3 -m pytest tests/enforcement_integration/ -v
grep -r 'docs/workflows' . --include='*.md' (should only appear in archive or historical context)

Commit any final touch-ups.
  - Files: `tests/enforcement_integration/`
  - Verify: pytest exit code 0, grep shows no active docs/workflows/ references in updated docs

## Files Likely Touched

- README.md
- CONTRIBUTING-SKILLS.md
- CONTRIBUTING.md
- docs/SKILL_AUTHORING_STANDARDS.md
- tests/enforcement_integration/

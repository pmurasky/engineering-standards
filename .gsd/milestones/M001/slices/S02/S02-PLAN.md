# S02: GSD Research Phase

**Goal:** Produce a comprehensive research findings document that validates the decisions from S01 and identifies any gaps, risks, or additional considerations before planning execution.
**Demo:** Research findings document complete

## Must-Haves

- 02-RESEARCH.md produced with all findings
- S01 decisions validated or updated with new evidence
- Gap analysis provides clear scope for S03 planning
- No blockers identified for execution

## Proof Level

- This slice proves: Research-only slice. Findings documented in 02-RESEARCH.md. No code changes.

## Integration Closure

Research findings feed directly into S03 plan phase. All decisions from S01 are either validated or amended with evidence.

## Verification

- Research document serves as audit trail for why the execution plan was structured the way it is.

## Tasks

- [x] **T01: Research Agent Skills spec compliance edge cases** `est:45 min`
  Research the Agent Skills specification (agentskills.io) for any edge cases or requirements not covered in S01 context:
1. Verify the exact frontmatter requirements (are there any optional fields?)
2. Check if there are any section ordering requirements
3. Verify the 500-line limit is strict or recommended
4. Check if there are any content formatting requirements (e.g., trigger phrase format)
5. Research how other projects handle multi-tool skill distribution

Read CONTRIBUTING-SKILLS.md thoroughly and any other spec references.
  - Files: `docs/CONTRIBUTING-SKILLS.md`
  - Verify: Document any new findings that contradict or extend S01 decisions. If no new findings, document that S01 decisions are validated.

- [x] **T02: Analyze OpenCode skill content gaps vs Claude** `est:1 hour`
  Do a detailed line-by-line comparison of OpenCode vs Claude skills to identify specific content gaps:
1. For each of the 9 skills, identify exactly what content is missing in OpenCode
2. Categorize gaps: missing trigger phrases, missing hard gate detail, missing workflow steps, missing blocking rules
3. Estimate the scope of each alignment (lines to add/remove)
4. Identify any OpenCode content that is BETTER than Claude (for potential two-way sync)

This informs the execution plan in S03.
  - Files: `.opencode/skills/*/SKILL.md`, `.claude/skills/*/SKILL.md`
  - Verify: Produce a detailed gap analysis table showing per-skill differences and estimated effort to align.

- [x] **T03: Research legacy docs/workflows/ archival strategy** `est:30 min`
  Research best practices for archiving legacy documentation:
1. Check if docs/workflows/ is referenced anywhere in the codebase (links, imports, scripts)
2. Verify no build or test processes depend on these files
3. Research best practices for marking files as archived/deprecated in Markdown
4. Check if any external documentation links to these files

This validates D4 from S01.
  - Files: `docs/workflows/*.md`
  - Verify: Confirm docs/workflows/ can be safely archived with headers only. Document any dependencies found.

## Files Likely Touched

- docs/CONTRIBUTING-SKILLS.md
- .opencode/skills/*/SKILL.md
- .claude/skills/*/SKILL.md
- docs/workflows/*.md

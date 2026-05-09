# S03: Archive Legacy Canonical Contracts

**Goal:** Archive the legacy docs/workflows/ directory by finding all active references, updating them to point to new skill locations, then removing the old directory.
**Demo:** After this: docs/workflows/ is either removed or clearly marked as a historical archive; no active skill, agent, or command references it as a live source of truth.

## Must-Haves

- Not provided.

## Threat Surface

- **Verdict:** pass
- **Rationale:** Slice S03 has clear scope: archive legacy docs/workflows/ directory after skills were restructured to .claude/skills and .opencode/skills. No ambiguity.

## Requirement Impact

- **Verdict:** pass
- **Rationale:** All dependencies satisfied: S01 and S02 are complete. No blockers. Ready to execute.

## Proof Level

- This slice proves: Not provided.

## Integration Closure

Not provided.

## Verification

- Not provided.

## Tasks

- [x] **T01: Grep all active references to docs/workflows/** `est:10 min`
  Search the entire codebase for any active references to docs/workflows/ or files within it. This includes imports, links in markdown, path references in code, and any documentation. Record every hit with file path and line number.
  - Files: `docs/workflows/`
  - Verify: Run grep/search and produce a complete list of all references. No references should be missed.

- [x] **T02: Update or remove active docs/workflows/ references** `est:20 min`
  For each reference found in T01: if it's a documentation link, update it to point to the new skill location (.claude/skills/ or .opencode/skills/). If it's a code reference, update the path. If it's obsolete, remove it. Commit each logical change separately.
  - Files: `Various files across codebase`
  - Verify: Re-run grep from T01 — zero active references to docs/workflows/ should remain.

- [x] **T03: Archive or delete docs/workflows/** `est:5 min`
  Once zero active references remain, delete the docs/workflows/ directory. If any files have historical value, move them to an archive location (e.g., .archive/workflows/) with a README explaining why they were archived.
  - Files: `docs/workflows/`
  - Verify: Directory no longer exists at docs/workflows/. git status shows it as deleted.

- [x] **T04: Final verification — tests green, zero active references** `est:10 min`
  Run the full test suite to ensure nothing broke. Re-run the grep from T01 to confirm zero references. Verify build succeeds.
  - Files: `Various`
  - Verify: All tests pass. Zero grep hits for docs/workflows/. Build succeeds.

## Files Likely Touched

- docs/workflows/
- Various files across codebase
- Various

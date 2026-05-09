---
estimated_steps: 1
estimated_files: 2
skills_used: []
---

# T03: Verify Skill Loading and Update Enforcement Tests

Run the existing enforcement test suite (tests/enforcement_integration/) to confirm all tests pass with the updated manifest and skill registrations. Then write a plugin skill loading integration test: install the plugin in a temp consuming project (or simulate with a local path install) and verify at least 2 skills are discoverable by OpenCode. Add an enforcement check that verifies every skill registered in the manifest has a valid SKILL.md.

## Inputs

- `S02 manifest + S04/T02 skills section`
- `S01 research doc on skill loading`
- `Existing tests/enforcement_integration/ structure`

## Expected Output

- `All existing enforcement tests passing`
- `New plugin skill loading integration test`
- `Enforcement check for manifest-registered skill SKILL.md existence`

## Verification

All existing enforcement tests green; new integration test passes for ≥2 skills; SKILL.md existence check added to enforcement suite and passing.

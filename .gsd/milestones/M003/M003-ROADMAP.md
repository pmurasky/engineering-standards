# M003: Testing and Documentation

**Vision:** Establish a complete, automated quality gate for the engineering-standards repo: CI pipeline running on every push/PR, skill scenario tests for all 9 skills, enforcement test coverage extended to .opencode/skills/, and updated documentation reflecting the post-M002 clean architecture.

## Success Criteria

- CI pipeline running on push/PR via .github/workflows/ci.yml
- Scenario tests exist for all 9 skills in tests/skills/scenarios/
- test_enforcement_gates.py validates both .claude/ and .opencode/ surfaces
- README, CONTRIBUTING-SKILLS.md, SKILL_AUTHORING_STANDARDS.md all updated and accurate

## Slices

- [ ] **S01: CI Pipeline, Skill Scenario Tests, and Enforcement Coverage** `risk:medium` `depends:[]`
  > After this: After this: every push/PR triggers a CI run that validates all skills via test_enforcement_gates.py; scenario tests exist for all 9 skills; .opencode/skills/ surface is also tested for compliance.

- [ ] **S02: Update Documentation** `risk:low` `depends:[S01]`
  > After this: After this: README.md, CONTRIBUTING-SKILLS.md, and SKILL_AUTHORING_STANDARDS.md accurately describe the post-M002 architecture with CI enforcement, scenario tests, and .opencode/ compliance requirements.

## Boundary Map

Not provided.

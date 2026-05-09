# S01: CI Pipeline, Skill Scenario Tests, and Enforcement Coverage

**Goal:** Close the 3 critical audit gaps: CI pipeline, skill scenario tests for all 9 skills, and extend enforcement tests to cover .opencode/skills/.
**Demo:** After this: every push/PR triggers a CI run that validates all skills via test_enforcement_gates.py; scenario tests exist for all 9 skills; .opencode/skills/ surface is also tested for compliance.

## Must-Haves

- CI runs on push/PR and passes. 9 scenario test YAML files exist. test_enforcement_gates.py covers .opencode/skills/. All local tests green.

## Proof Level

- This slice proves: CI green run on GitHub + local pytest exit code 0 + YAML lint on scenario files.

## Integration Closure

S02 (documentation) uses the completed CI config and scenario test format as input. M009/M010 proceed on a tested foundation.

## Verification

- Primary observability surface: GitHub Actions run output visible in the PR/push timeline. Local test output via pytest -v. Scenario test validation surfaced via test_enforcement_gates.py extension.

## Tasks

- [ ] **T01: Extend test_enforcement_gates.py to cover .opencode/skills/** `est:30 min`
  Extend tests/enforcement_integration/test_enforcement_gates.py to also validate .opencode/skills/ alongside .claude/skills/. The existing tests only check .claude/skills/; both surfaces should have the same compliance requirements.

Changes:
1. Read existing test structure to understand how .claude/skills/ path is parameterized
2. Add .opencode/skills/ as a second surface to all compliance checks (frontmatter, line count, hard gates, status vocabulary, metadata)
3. Run tests locally to confirm both surfaces pass

Commit: `test(enforcement): extend gates to also validate .opencode/skills/ surface`
  - Files: `tests/enforcement_integration/test_enforcement_gates.py`, `tests/enforcement_integration/helpers.py`
  - Verify: python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v -- shows test cases for both .claude/skills/ and .opencode/skills/, all passing

- [ ] **T02: Create scenario tests for all 9 skills** `est:30 min`
  Create tests/skills/scenarios/ directory and a basic.yaml scenario file for each of the 9 skills. Per SKILL_AUTHORING_STANDARDS.md §8 and the PR checklist §9.

Scenario file format (derive from standard or establish if unspecified):
```yaml
skill_name: <skill>
trigger: "<example user phrase that should invoke this skill>"
expected_behavior: "<what the skill should produce>"
not_for: "<example phrase that should NOT invoke this skill>"
```

Create for: code-quality, commit-review, micro-commit, pre-commit, refactoring-gate, spec-compliance, static-analysis-gate, tdd-enforcement, test-coverage.

Commit: `test(skills): add scenario tests for all 9 skills per authoring standard §8`
  - Files: `tests/skills/scenarios/`
  - Verify: ls tests/skills/scenarios/ shows 9 directories, each with basic.yaml. yamllint tests/skills/scenarios/**/*.yaml (or python3 -c 'import yaml; yaml.safe_load(open(...))') validates all files are valid YAML

- [ ] **T03: Add .github/workflows/ci.yml and fix npm test** `est:20 min`
  Create .github/workflows/ci.yml that:
- Triggers on: push to main, pull_request to main
- Checks out code
- Sets up Python (3.11 or 3.12)
- Installs dependencies (pip install pytest pyyaml)
- Runs: python3 -m pytest tests/enforcement_integration/ -v
- Runs: yamllint or python YAML validation on tests/skills/scenarios/**/*.yaml

Also fix the root package.json npm test placeholder to run the Python tests (via npx or a shell command).

Commit: `ci: add CI workflow to run enforcement tests on push and PR`
  - Files: `.github/workflows/ci.yml`, `package.json`
  - Verify: Push branch to GitHub and confirm CI workflow appears in Actions tab and passes. Locally: cat .github/workflows/ci.yml and npm test both work.

- [ ] **T04: Add dependabot.yml and SECURITY.md** `est:15 min`
  Add .github/dependabot.yml to auto-update GitHub Actions versions (fixes CODEOWNERS reference to missing file). Add SECURITY.md with minimal security policy (vulnerability reporting email/process), fixing the second CODEOWNERS broken reference.

Commit: `chore(github): add dependabot.yml and SECURITY.md`
  - Files: `.github/dependabot.yml`, `SECURITY.md`
  - Verify: cat .github/dependabot.yml shows valid config. cat SECURITY.md has reporting instructions. .github/CODEOWNERS references no longer broken.

## Files Likely Touched

- tests/enforcement_integration/test_enforcement_gates.py
- tests/enforcement_integration/helpers.py
- tests/skills/scenarios/
- .github/workflows/ci.yml
- package.json
- .github/dependabot.yml
- SECURITY.md

---
estimated_steps: 6
estimated_files: 2
skills_used: []
---

# T01: Extend test_enforcement_gates.py to cover .opencode/skills/

Extend tests/enforcement_integration/test_enforcement_gates.py to also validate .opencode/skills/ alongside .claude/skills/. The existing tests only check .claude/skills/; both surfaces should have the same compliance requirements.

Changes:
1. Read existing test structure to understand how .claude/skills/ path is parameterized
2. Add .opencode/skills/ as a second surface to all compliance checks (frontmatter, line count, hard gates, status vocabulary, metadata)
3. Run tests locally to confirm both surfaces pass

Commit: `test(enforcement): extend gates to also validate .opencode/skills/ surface`

## Inputs

- `.opencode/skills/`
- `.claude/skills/`
- `tests/enforcement_integration/test_enforcement_gates.py`

## Expected Output

- `tests/enforcement_integration/test_enforcement_gates.py updated`
- `Tests pass for both .claude/skills/ and .opencode/skills/`

## Verification

python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v -- shows test cases for both .claude/skills/ and .opencode/skills/, all passing

## Observability Impact

Test output now shows compliance results for both surfaces side by side

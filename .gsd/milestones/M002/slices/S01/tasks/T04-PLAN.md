---
estimated_steps: 3
estimated_files: 1
skills_used: []
---

# T04: Verify enforcement tests still pass

Run the enforcement integration test suite to confirm no regressions from directory additions.
python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v
Fix any regressions before moving to S02.

## Inputs

- `.claude/skills/`
- `.opencode/skills/`

## Expected Output

- `All tests pass with exit code 0`

## Verification

python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v — exit code 0, all green

# Enforcement Integration Tests

This suite validates enforcement behavior for Claude workflow controls:

- Session bootstrap hook behavior (normal and fallback)
- Hard-gate skills (pre-commit, TDD enforcement, refactoring gate)
- Token-budget reporting for skill invocation context size

## Run all enforcement integration tests

```bash
python3 -m unittest discover -s tests/enforcement_integration -p "test_*.py"
```

## Run token usage report only

```bash
python3 scripts/report-token-usage.py --max-tokens 1000 --fail-on-exceed
```

## Fixtures

- `tests/fixtures/claude-project-with-bootstrap/`: fixture project with bootstrap context file
- `tests/fixtures/invalid-skills/missing-hard-gate/`: pressure fixture for invalid skill structure

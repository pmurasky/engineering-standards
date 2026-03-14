# Enforcement Integration Tests

This suite validates enforcement behavior for Skills 2.0 canonical workflow contracts and adapters:

- **Session bootstrap hook** behavior (normal and fallback)
- **Legacy phrase-based validation** (pre-commit, TDD enforcement, refactoring gate)
- **Contract parity validation** (Skills 2.0 canonical contracts vs tool adapters)
- **Contract drift detection** (pressure tests with invalid adapters)
- **Token-budget reporting** for skill invocation context size

## Test Categories

### Legacy Enforcement Tests
- `EnforcementGateSkillIntegrationTests` - Original phrase-based validation (preserved for backward compatibility)
- Validates hard-gate presence and required phrases in Claude skills

### Skills 2.0 Contract Parity Tests
- `ContractParityIntegrationTests` - Validates adapter alignment with canonical contracts
- Tests contract references, hard-gate semantics, and status vocabulary consistency
- Validates cross-surface parity between Claude skills and OpenCode commands

### Contract Drift Pressure Tests
- `ContractDriftPressureTests` - Negative tests that verify validation functions catch drift
- Uses pressure fixtures designed to fail validation
- Ensures contract parity validation has high signal detection

## Run Tests

### Run all enforcement integration tests
```bash
python3 -m unittest discover -s tests/enforcement_integration -p "test_*.py"
```

### Run specific test categories
```bash
# Legacy phrase-based tests only
python3 -m unittest tests.enforcement_integration.test_enforcement_gates.EnforcementGateSkillIntegrationTests

# Skills 2.0 contract parity tests only  
python3 -m unittest tests.enforcement_integration.test_enforcement_gates.ContractParityIntegrationTests

# Contract drift pressure tests only
python3 -m unittest tests.enforcement_integration.test_enforcement_gates.ContractDriftPressureTests
```

### Run individual contract parity tests
```bash
# Test pre-commit workflow parity across Claude and OpenCode
python3 -m unittest tests.enforcement_integration.test_enforcement_gates.ContractParityIntegrationTests.test_pre_commit_workflow_parity

# Test that adapters reference canonical contracts
python3 -m unittest tests.enforcement_integration.test_enforcement_gates.ContractParityIntegrationTests.test_claude_pre_commit_references_canonical_contract
```

### Run token usage report
```bash
python3 scripts/report-token-usage.py --max-tokens 1000 --fail-on-exceed
```

## CI Integration

Contract parity tests are designed to be CI-ready and should be included in build pipelines:

```bash
# Fail build if any contract parity issues detected
python3 -m unittest tests.enforcement_integration.test_enforcement_gates.ContractParityIntegrationTests
```

## Test Fixtures

### Positive Fixtures
- `tests/fixtures/claude-project-with-bootstrap/` - Bootstrap hook fixture project

### Pressure Fixtures (Designed to Fail)
- `tests/fixtures/invalid-skills/missing-hard-gate/` - Missing hard-gate section
- `tests/fixtures/invalid-skills/missing-contract-reference/` - No canonical contract reference
- `tests/fixtures/invalid-skills/wrong-status-vocabulary/` - Uses incorrect status terms
- `tests/fixtures/invalid-skills/incomplete-hard-gates/` - Missing required hard-gate semantics

## Skills 2.0 Contract Validation

The contract parity tests validate:

1. **Contract References** - Adapters reference valid canonical contracts in `docs/workflows/`
2. **Hard-Gate Semantics** - Adapters implement canonical hard gates with proper blocking semantics
3. **Status Vocabulary** - Adapters use canonical status terms (`READY`, `NOT READY`, `NOT CONFIGURED`)
4. **Cross-Surface Parity** - Claude skills and OpenCode commands implement same workflow logic
5. **Drift Detection** - Changes that break contract compliance are caught by tests

## Adding New Contract Validation

When adding new workflows to Skills 2.0:

1. Create canonical contract in `docs/workflows/[workflow-name].md`
2. Add contract parity test in `ContractParityIntegrationTests` 
3. Create pressure fixtures for common failure modes
4. Add pressure tests in `ContractDriftPressureTests`
5. Update this README with new test documentation

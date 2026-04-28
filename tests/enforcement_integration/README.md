# Enforcement Integration Tests

This suite validates enforcement behavior for Skills 2.0 canonical workflow contracts and adapters:

- **Session bootstrap hook** behavior (normal and fallback)
- **Legacy phrase-based validation** (pre-commit, TDD enforcement, refactoring gate)
- **Contract parity validation** (Skills 2.0 canonical contracts vs tool adapters)
- **Contract drift detection** (pressure tests with invalid adapters)
- **Token-budget reporting** for skill invocation context size
- **Upstream lock tooling** validation and sync behavior

## Test Categories

### Legacy Enforcement Tests
- `EnforcementGateSkillIntegrationTests` - Original phrase-based validation (preserved for backward compatibility)
- Validates hard-gate presence and required phrases in Claude skills

### Skills 2.0 Contract Parity Tests
- `ContractParityIntegrationTests` - Validates adapter alignment with canonical contracts
- Tests contract references, hard-gate semantics, and status vocabulary consistency
- Validates cross-surface parity between Claude skills and OpenCode commands

### Contract Structure Validation Tests
- `ContractStructureValidationTests` - Validates that all discovered contracts have required sections
- Uses `discover_contracts()` to auto-detect all `docs/workflows/*.md` files
- Checks for H1 title and all eight required H2 sections from the contract template

### Contract Structure Pressure Tests
- `ContractStructurePressureTests` - Negative tests verifying `validate_contract_structure` catches malformed contracts
- Uses contract fixtures: missing-sections, empty-contract, nonexistent file

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

### Run token usage reports

#### Legacy Claude skills report (backward compatibility)
```bash
python3 scripts/report-token-usage.py --max-tokens 1000 --fail-on-exceed
```

#### Skills 2.0 multi-category report
```bash
# Human-readable format with default thresholds
python3 scripts/report-token-usage.py --always-on-threshold 2000 --skills-threshold 1000 --commands-threshold 800 --contracts-threshold 1200

# JSON output for machine processing  
python3 scripts/report-token-usage.py --json-output

# CI-ready with threshold enforcement
python3 scripts/report-token-usage.py --always-on-threshold 2000 --skills-threshold 1000 --commands-threshold 800 --contracts-threshold 1200 --fail-on-exceed
```

#### Baseline capture and comparison
```bash
# Capture current state as baseline
python3 scripts/report-token-usage.py --capture-baseline baseline.json

# Compare current state against baseline
python3 scripts/report-token-usage.py --compare-baseline baseline.json --fail-on-exceed
```

### Run upstream lock tooling checks

```bash
# Validate lockfile against schema and checksum paths
python3 scripts/validate_upstream_lock.py

# Refresh lockfile metadata from upstream and local mirror
python3 scripts/sync_superpowers_lock.py

# Integration tests for lock scripts
python3 -m unittest tests.enforcement_integration.test_upstream_lock_tools
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
- `tests/fixtures/invalid-contracts/missing-sections/` - Contract missing most required sections
- `tests/fixtures/invalid-contracts/empty-contract/` - Empty contract file

## Skills 2.0 Contract Validation

The contract parity tests validate:

1. **Contract References** - Adapters reference valid canonical contracts in `docs/workflows/`
2. **Hard-Gate Semantics** - Adapters implement canonical hard gates with proper blocking semantics
3. **Status Vocabulary** - Adapters use canonical status terms (`READY`, `NOT READY`, `NOT CONFIGURED`)
4. **Cross-Surface Parity** - Claude skills and OpenCode commands implement same workflow logic
5. **Drift Detection** - Changes that break contract compliance are caught by tests

## Skills 2.0 Token Governance

The multi-category token reporting validates:

1. **Always-on Budget** - CLAUDE.md and key rules stay within always-on context limits
2. **Adapter Efficiency** - Skills and commands remain concise with canonical contract references
3. **Category Thresholds** - Each category (always-on, skills, commands, contracts) has appropriate limits
4. **Token Efficiency** - Canonical contracts reduce duplication vs duplicated adapter content
5. **Baseline Tracking** - Token usage changes are tracked and compared over time

**Current baseline (Skills 2.0 implementation):**
- **Total**: 9,750 tokens across all surfaces
- **Always-on**: 1,453/2,000 tokens (72.7%) - CLAUDE.md + key rules
- **Claude skills**: 3,155 tokens (avg 351 per skill) - On-demand adapters
- **OpenCode commands**: 3,688 tokens (avg 369 per command) - Cross-surface parity
- **Canonical contracts**: 1,454 tokens (avg 727 per contract) - Single source of truth

## Adding New Contract Validation

When adding new workflows to Skills 2.0:

1. Create canonical contract in `docs/workflows/[workflow-name].md`
2. Add contract parity test in `ContractParityIntegrationTests` 
3. Create pressure fixtures for common failure modes
4. Add pressure tests in `ContractDriftPressureTests`
5. Update this README with new test documentation

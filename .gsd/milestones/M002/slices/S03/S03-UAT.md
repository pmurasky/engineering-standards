# S03: Archive Legacy Canonical Contracts — UAT

**Milestone:** M002
**Written:** 2026-05-09T00:32:02.544Z

## UAT: Archive Legacy Canonical Contracts

### Verification Steps
1. Confirm docs/workflows/ no longer exists: `ls docs/workflows/` → should fail
2. Confirm docs/archived-workflows/ exists with files: `ls docs/archived-workflows/` → shows README.md, CONTRIBUTING.md, contracts.registry.json, pre-commit.md, micro-commit.md, tdd-enforcement.md
3. Run tests: `python3 -m pytest tests/enforcement_integration/ -q` → 44 passed, 2 skipped
4. Check for active references: `grep -r "docs/workflows" --include="*.py" --include="*.md" --include="*.json" --include="*.yml" . | grep -v ".planning" | grep -v "docs/adr" | grep -v "backward"` → only backward-compatibility code in report_contract_adapter_impact.py

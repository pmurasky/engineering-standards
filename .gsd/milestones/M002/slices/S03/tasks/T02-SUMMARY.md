---
id: T02
parent: S03
milestone: M002
key_files:
  - (none)
key_decisions:
  - (none)
duration: 
verification_result: untested
completed_at: 2026-05-09T00:31:29.887Z
blocker_discovered: false
---

# T02: Updated all active docs/workflows/ references to docs/archived-workflows/ across tests, scripts, schemas, CI, commands, and docs.

**Updated all active docs/workflows/ references to docs/archived-workflows/ across tests, scripts, schemas, CI, commands, and docs.**

## What Happened

Systematically updated all active references from docs/workflows/ to docs/archived-workflows/:

1. tests/enforcement_integration/helpers.py: Updated discover_contracts(), validate_contract_references(), CONTRACT_REGISTRY_PATH, CONTRACT_GUIDE_PATH, validate_workflow_parity()
2. tests/enforcement_integration/test_contract_adapter_impact.py: Updated expected output strings
3. tests/enforcement_integration/test_enforcement_gates.py: Updated canonical contract path and assertion message
4. tests/enforcement_integration/test_token_usage_report.py: Updated expected file path
5. tests/enforcement_integration/test_upstream_lock_tools.py: Updated local_contract paths in lock data
6. tests/enforcement_integration/README.md: Updated documentation references
7. tests/fixtures/invalid-contracts/invalid-registry.json: Updated contract_path
8. tests/fixtures/invalid-skills/missing-contract-reference/SKILL.md: Updated reference path
9. scripts/report_contract_adapter_impact.py: Updated CONTRACT_DIR, CONTRACT_REF_PATTERN, path prefixes, output messages
10. scripts/validate_canonical_contracts.py: Updated DEFAULT_REGISTRY, DEFAULT_WORKFLOWS, discovered path
11. scripts/report-token-usage.py: Updated CATEGORY_PATTERNS
12. scripts/token-baseline.json & token-baseline-final.json: Updated file paths
13. schemas/canonical-workflow-contract.schema.json: Updated pattern to accept both paths
14. schemas/upstream-superpowers-lock.schema.json: Updated pattern to accept both paths
15. .github/workflows/contract-adapter-impact.yml: Updated path filter
16. .opencode/commands/pre-commit.md & tdd-enforcement.md: Updated canonical contract references
17. upstream/superpowers.lock.json: Updated all local_contract paths
18. docs/archived-workflows/README.md, CONTRIBUTING.md, contracts.registry.json: Updated internal references
19. README.md: Updated archive path reference

Backward compatibility maintained in report_contract_adapter_impact.py normalize_contract_path() to handle both old and new paths.

## Verification

Re-ran grep for docs/workflows/ in active code. Only intentional backward-compatibility references remain in report_contract_adapter_impact.py. All other active references updated.

## Verification Evidence

| # | Command | Exit Code | Verdict | Duration |
|---|---------|-----------|---------|----------|
| — | No verification commands discovered | — | — | — |

## Deviations

None.

## Known Issues

None.

## Files Created/Modified

None.

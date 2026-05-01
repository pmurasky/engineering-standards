---
estimated_steps: 9
estimated_files: 1
skills_used: []
---

# T10: Update Enforcement Tests

Update test suite to validate Agent Skills compliance:
1. Review `tests/enforcement_integration/test_enforcement_gates.py`
2. Update `validate_contract_references()` - remove or modify
3. Update `validate_hard_gate_semantics()` - adapt for inline content
4. Add `validate_agent_skills_structure()` - check frontmatter compliance
5. Add `validate_skill_references()` - verify references/ folder files exist
6. Update test fixtures if needed
7. Run full test suite
8. Commit changes

## Inputs

- `tests/enforcement_integration/test_enforcement_gates.py`

## Expected Output

- `Updated test file`
- `All tests passing`

## Verification

Tests validate Agent Skills frontmatter, references/ folder structure, SKILL.md line count; all tests pass

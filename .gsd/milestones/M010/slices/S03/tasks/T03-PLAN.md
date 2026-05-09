---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T03: Verify Resource Loading and Add Enforcement Tests

Write and run a resource loading test. Create a minimal test consuming project (or use a temp directory) that installs the plugin and attempts to access at least 3 resources by their plugin resource IDs. Document the access pattern in docs/resource-inventory.md. Add a resource reference integrity check to the enforcement test suite (tests/enforcement_integration/ or tests/validation/) that verifies every registered resource file actually exists on disk.

## Inputs

- `Plugin manifest with resources (T02 output)`
- `S01 research doc on resource loading API`
- `Existing tests/enforcement_integration/ structure`

## Expected Output

- `Resource loading test script or test case`
- `Enforcement test for resource file existence`
- `Passing test run output`

## Verification

Resource loading test passes; enforcement test for resource existence added and green; at least 3 resources verified accessible via plugin API.

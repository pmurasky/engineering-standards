---
name: test-coverage
description: Assess test completeness and identify missing unit-test coverage for changed behavior. Verify minimum 80% coverage for changed code.
---

# Test Coverage Assessment

Assess test coverage quality for targeted changes.

## Trigger Conditions

- User requests coverage assessment for changes
- Before commit when coverage verification is needed
- Phrases: "test coverage", "coverage check", "missing tests", "coverage assessment"

## Checks

1. **Identify changed behavior** and existing unit tests
2. **Flag missing coverage**:
   - Happy path scenarios
   - Edge cases
   - Error paths
3. **Verify test quality**:
   - Naming clarity
   - Given-When-Then structure where relevant
4. **Recommend minimal additional tests** to satisfy standards

## Coverage Requirements

**Minimum Thresholds:**
- 80% unit test coverage overall for changed code
- 100% coverage for critical paths
- Unit tests only — integration and E2E tests do not count toward coverage

## What to Look For

**Missing Test Scenarios:**
- Happy path not tested
- Edge cases (null, empty, boundary values)
- Error conditions and exceptions
- Branch coverage (all code paths)

**Test Quality Issues:**
- Unclear test names
- Missing Given-When-Then structure
- Tests that don't verify behavior
- Overly complex test setup

## Output Format

Provide:
1. **Coverage summary** for changed code
2. **Missing test scenarios** identified
3. **Specific recommendations** for additional tests
4. **Test quality observations**

## Important

If no automated unit test command is configured, note that explicitly in the report.

## Token Budget

- **Category**: On-demand workflow
- **Estimated usage**: 700-1000 tokens per invocation
- **Frequency**: Per commit (typically 5-20 times per development session)
- **Optimization**: Focus on missing coverage first

## References

- `docs/CODING_PRACTICES.md` - Testing standards and coverage requirements
- `docs/PRE_COMMIT_CHECKLIST.md` - Quality checklist
---
description: Testing standards enforcement when editing test files
globs: "**/*{Test,test,Spec,spec,_test}*.{kt,java,ts,js,py,go,rs,cs,cpp,c,swift,rb}"
---

# Testing Standards

Use this rule as a compact test-quality checklist.

## Quick Checks
- Given-When-Then structure and clear scenario names
- Coverage intent includes happy path, edge cases, and error paths
- Tests verify behavior (not private implementation details)
- No skipped/disabled tests without a tracked reason
- No failing tests in committed changes

Canonical references:
- `docs/CODING_PRACTICES.md`
- `docs/PRE_COMMIT_CHECKLIST.md`

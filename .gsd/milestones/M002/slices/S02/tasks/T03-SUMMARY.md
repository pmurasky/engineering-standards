# T03 Summary — Apply fixes to remaining 6 skills

## Scope

Applied compliance fixes for the remaining six skills across both surfaces:

- code-quality
- micro-commit
- pre-commit
- tdd-enforcement
- static-analysis-gate
- test-coverage

Files updated: 12 SKILL.md files under `.claude/skills/*` and `.opencode/skills/*`.

## Fixes applied

- Normalized frontmatter to required contract:
  - `name`
  - `description`
  - `disable-model-invocation: true`
- Added explicit `## Use when` and `## Not for` near the top.
- Removed external `docs/...` reference redirects.
- Added concrete `## Example` and `## Anti-patterns` sections.

## Verification

Executed required gates:

- `python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v`
  - Result: `26 passed, 79 subtests passed`
- `ruff check tests/enforcement_integration`
  - Result: `All checks passed`
- `python3 -m compileall -q .`
  - Result: pass

## Outcome

T03 objective met: remaining six skills were brought to compliance across both surfaces, with enforcement tests green.

---
estimated_steps: 2
estimated_files: 12
skills_used: []
---

# T03: Apply fixes to remaining 6 skills

Apply any fixes identified in T02 to the remaining 6 skills (both .claude/ and .opencode/ surfaces). If a skill is already fully compliant, mark it PASS and skip. Commit each skill fix individually following micro-commit workflow.
Example commit: `fix(skills): add Use when/Not for to static-analysis-gate`

## Inputs

- `Gap list from T02`
- `docs/SKILL_AUTHORING_STANDARDS.md`

## Expected Output

- `All 6 remaining skills updated in both surfaces`
- `Each fix committed individually`

## Verification

python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v — all 9 skills pass

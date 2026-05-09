# S01: Restructure Skill Directories — UAT

**Milestone:** M002
**Written:** 2026-05-08T10:31:44.518Z

## UAT for S01

1. Confirm directories exist:
   - `.claude/skills/pre-commit/references/workflow.md`
   - `.claude/skills/micro-commit/references/workflow.md`
   - `.claude/skills/tdd-enforcement/references/workflow.md`
   - `.opencode/skills/pre-commit/references/workflow.md`
   - `.opencode/skills/micro-commit/references/workflow.md`
   - `.opencode/skills/tdd-enforcement/references/workflow.md`
2. Confirm enforcement tests pass:
   - `python3 -m pytest tests/enforcement_integration/test_enforcement_gates.py -v`
3. Expected result:
   - All listed workflow reference files exist.
   - Test command exits 0 with all tests green.

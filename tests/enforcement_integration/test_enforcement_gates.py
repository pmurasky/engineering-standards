from __future__ import annotations

import unittest
from pathlib import Path

from helpers import REPO_ROOT, validate_skill


class EnforcementGateSkillIntegrationTests(unittest.TestCase):
    def test_pre_commit_skill_requires_static_analysis_gate(self) -> None:
        skill_path = REPO_ROOT / ".claude" / "skills" / "pre-commit" / "SKILL.md"
        problems = validate_skill(
            skill_path,
            [
                "Do NOT recommend commit readiness",
                "Static analysis passes",
                "static-analysis-gate",
                "docs/STATIC_ANALYSIS_STANDARDS.md",
            ],
        )
        self.assertEqual(problems, [])

    def test_tdd_enforcement_skill_blocks_without_red_evidence(self) -> None:
        skill_path = REPO_ROOT / ".claude" / "skills" / "tdd-enforcement" / "SKILL.md"
        problems = validate_skill(
            skill_path,
            [
                "Never allow production code changes before a failing test",
                "If no failing test evidence is shown, output BLOCKED",
            ],
        )
        self.assertEqual(problems, [])

    def test_refactoring_gate_skill_requires_coverage_thresholds(self) -> None:
        skill_path = REPO_ROOT / ".claude" / "skills" / "refactoring-gate" / "SKILL.md"
        problems = validate_skill(
            skill_path,
            [
                "Unit-test coverage for the target code is >= 80%",
                "Coverage for critical paths is 100%",
                "If target coverage is < 80%, output BLOCKED",
            ],
        )
        self.assertEqual(problems, [])

    def test_pressure_fixture_detects_missing_hard_gate(self) -> None:
        fixture_skill = (
            REPO_ROOT
            / "tests"
            / "fixtures"
            / "invalid-skills"
            / "missing-hard-gate"
            / "SKILL.md"
        )
        problems = validate_skill(fixture_skill, ["Do NOT recommend commit readiness"])

        self.assertNotEqual(problems, [])
        self.assertIn("missing hard-gate section", problems[0])


if __name__ == "__main__":
    unittest.main()

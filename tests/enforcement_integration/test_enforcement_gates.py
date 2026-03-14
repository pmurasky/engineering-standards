from __future__ import annotations

import unittest
from pathlib import Path

from helpers import (
    REPO_ROOT,
    validate_skill,
    validate_contract_references,
    validate_hard_gate_semantics,
    validate_status_vocabulary,
    validate_workflow_parity,
)


class EnforcementGateSkillIntegrationTests(unittest.TestCase):
    """Legacy phrase-based validation tests (preserved for backward compatibility)."""
    
    def test_pre_commit_skill_requires_static_analysis_gate(self) -> None:
        skill_path = REPO_ROOT / ".claude" / "skills" / "pre-commit" / "SKILL.md"
        problems = validate_skill(
            skill_path,
            [
                "Static analysis MUST pass",
                "static-analysis-gate",
                "canonical contract",
                "docs/workflows/pre-commit.md",
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


class ContractParityIntegrationTests(unittest.TestCase):
    """Skills 2.0 contract parity validation tests."""
    
    def test_pre_commit_workflow_parity(self) -> None:
        problems = validate_workflow_parity("pre-commit")
        self.assertEqual(problems, [], f"Pre-commit workflow parity issues: {problems}")
    
    def test_claude_pre_commit_references_canonical_contract(self) -> None:
        skill_path = REPO_ROOT / ".claude" / "skills" / "pre-commit" / "SKILL.md"
        problems = validate_contract_references(skill_path)
        self.assertEqual(problems, [], f"Claude pre-commit contract reference issues: {problems}")
    
    def test_opencode_pre_commit_references_canonical_contract(self) -> None:
        command_path = REPO_ROOT / ".opencode" / "commands" / "pre-commit.md"
        problems = validate_contract_references(command_path)
        self.assertEqual(problems, [], f"OpenCode pre-commit contract reference issues: {problems}")
    
    def test_claude_pre_commit_implements_canonical_hard_gates(self) -> None:
        canonical_contract = REPO_ROOT / "docs" / "workflows" / "pre-commit.md"
        skill_path = REPO_ROOT / ".claude" / "skills" / "pre-commit" / "SKILL.md"
        problems = validate_hard_gate_semantics(canonical_contract, skill_path)
        self.assertEqual(problems, [], f"Claude pre-commit hard gate issues: {problems}")
    
    def test_opencode_pre_commit_implements_canonical_hard_gates(self) -> None:
        canonical_contract = REPO_ROOT / "docs" / "workflows" / "pre-commit.md"
        command_path = REPO_ROOT / ".opencode" / "commands" / "pre-commit.md"
        problems = validate_hard_gate_semantics(canonical_contract, command_path)
        self.assertEqual(problems, [], f"OpenCode pre-commit hard gate issues: {problems}")
    
    def test_claude_pre_commit_uses_canonical_status_vocabulary(self) -> None:
        canonical_contract = REPO_ROOT / "docs" / "workflows" / "pre-commit.md"
        skill_path = REPO_ROOT / ".claude" / "skills" / "pre-commit" / "SKILL.md"
        problems = validate_status_vocabulary(canonical_contract, skill_path)
        self.assertEqual(problems, [], f"Claude pre-commit status vocabulary issues: {problems}")
    
    def test_opencode_pre_commit_uses_canonical_status_vocabulary(self) -> None:
        canonical_contract = REPO_ROOT / "docs" / "workflows" / "pre-commit.md"
        command_path = REPO_ROOT / ".opencode" / "commands" / "pre-commit.md"
        problems = validate_status_vocabulary(canonical_contract, command_path)
        self.assertEqual(problems, [], f"OpenCode pre-commit status vocabulary issues: {problems}")


class ContractDriftPressureTests(unittest.TestCase):
    """Pressure tests that verify contract parity validation catches drift issues."""
    
    def test_missing_contract_reference_detected(self) -> None:
        fixture_skill = (
            REPO_ROOT / "tests" / "fixtures" / "invalid-skills" 
            / "missing-contract-reference" / "SKILL.md"
        )
        problems = validate_contract_references(fixture_skill)
        self.assertNotEqual(problems, [])
        self.assertIn("missing canonical contract reference", problems[0])
    
    def test_wrong_status_vocabulary_detected(self) -> None:
        canonical_contract = REPO_ROOT / "docs" / "workflows" / "pre-commit.md"
        fixture_skill = (
            REPO_ROOT / "tests" / "fixtures" / "invalid-skills"
            / "wrong-status-vocabulary" / "SKILL.md"
        )
        problems = validate_status_vocabulary(canonical_contract, fixture_skill)
        self.assertNotEqual(problems, [])
        self.assertTrue(any("missing required status vocabulary" in problem for problem in problems))
    
    def test_incomplete_hard_gates_detected(self) -> None:
        canonical_contract = REPO_ROOT / "docs" / "workflows" / "pre-commit.md"
        fixture_skill = (
            REPO_ROOT / "tests" / "fixtures" / "invalid-skills"
            / "incomplete-hard-gates" / "SKILL.md"
        )
        problems = validate_hard_gate_semantics(canonical_contract, fixture_skill)
        self.assertNotEqual(problems, [])
        self.assertTrue(any("missing hard-gate semantic" in problem for problem in problems))


if __name__ == "__main__":
    unittest.main()

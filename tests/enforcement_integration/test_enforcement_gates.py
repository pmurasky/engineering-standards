from __future__ import annotations

import unittest

from helpers import (
    REPO_ROOT,
    validate_skill,
    validate_contract_references,
    validate_contract_structure,
    validate_hard_gate_semantics,
    discover_contracts,
    validate_skill_metadata,
    validate_metadata_dependencies,
    validate_metadata_budget,
    discover_skills,
    parse_frontmatter,
    validate_contract_registry,
    validate_contract_contributor_guide,
)


class EnforcementGateSkillIntegrationTests(unittest.TestCase):
    """Legacy phrase-based validation tests (preserved for backward compatibility)."""

    def test_pre_commit_skill_requires_static_analysis_gate(self) -> None:
        skill_path = REPO_ROOT / ".claude" / "skills" / "pre-commit" / "SKILL.md"
        problems = validate_skill(
            skill_path,
            [
                "Static analysis MUST pass",
                "references/workflow.md",
            ],
        )
        self.assertEqual(problems, [])

    def test_tdd_enforcement_skill_blocks_without_red_evidence(self) -> None:
        skill_path = REPO_ROOT / ".claude" / "skills" / "tdd-enforcement" / "SKILL.md"
        problems = validate_skill(
            skill_path,
            [
                "Never allow production code changes before a failing test",
                "If no failing test evidence is shown",
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
                "If target coverage is < 80%",
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


class AgentSkillsComplianceTests(unittest.TestCase):
    def _check_skill_hard_gates(self, surface: str, skill_name: str) -> None:
        skill_path = REPO_ROOT / f".{surface}" / "skills" / skill_name / "SKILL.md"
        problems = validate_skill(skill_path, ["Hard Gates"])
        self.assertEqual(problems, [], f"{surface}/{skill_name} hard gate issues: {problems}")

    def _check_skill_status_vocabulary(self, surface: str, skill_name: str) -> None:
        skill_path = REPO_ROOT / f".{surface}" / "skills" / skill_name / "SKILL.md"
        problems = validate_skill(skill_path, ["Status Vocabulary"])
        self.assertEqual(
            problems, [], f"{surface}/{skill_name} status vocabulary issues: {problems}"
        )

    def _check_skill_under_500_lines(self, surface: str, skill_name: str) -> None:
        skill_path = REPO_ROOT / f".{surface}" / "skills" / skill_name / "SKILL.md"
        content = skill_path.read_text(encoding="utf-8")
        line_count = len(content.splitlines())
        self.assertLess(
            line_count,
            500,
            f"{surface}/{skill_name} skill has {line_count} lines, must be under 500",
        )

    def _check_skill_has_references_folder(self, surface: str, skill_name: str) -> None:
        references_path = REPO_ROOT / f".{surface}" / "skills" / skill_name / "references"
        self.assertTrue(
            references_path.exists(), f"{surface}/{skill_name} skill missing references/ folder"
        )

    def test_pre_commit_skill_has_hard_gates_claude(self) -> None:
        self._check_skill_hard_gates("claude", "pre-commit")

    def test_pre_commit_skill_has_hard_gates_opencode(self) -> None:
        self._check_skill_hard_gates("opencode", "pre-commit")

    def test_pre_commit_skill_has_status_vocabulary_claude(self) -> None:
        self._check_skill_status_vocabulary("claude", "pre-commit")

    def test_pre_commit_skill_has_status_vocabulary_opencode(self) -> None:
        self._check_skill_status_vocabulary("opencode", "pre-commit")

    def test_pre_commit_skill_under_500_lines_claude(self) -> None:
        self._check_skill_under_500_lines("claude", "pre-commit")

    def test_pre_commit_skill_under_500_lines_opencode(self) -> None:
        self._check_skill_under_500_lines("opencode", "pre-commit")

    def test_pre_commit_skill_has_references_folder_claude(self) -> None:
        self._check_skill_has_references_folder("claude", "pre-commit")

    def test_pre_commit_skill_has_references_folder_opencode(self) -> None:
        self._check_skill_has_references_folder("opencode", "pre-commit")

    def test_all_claude_skills_have_name_and_description_in_frontmatter(self) -> None:
        skills_dir = REPO_ROOT / ".claude" / "skills"
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_path = skill_dir / "SKILL.md"
                if skill_path.exists():
                    content = skill_path.read_text(encoding="utf-8")
                    self.assertIn(
                        "name:",
                        content,
                        f"{skill_dir.name} missing 'name' in frontmatter",
                    )
                    self.assertIn(
                        "description:",
                        content,
                        f"{skill_dir.name} missing 'description' in frontmatter",
                    )

    def test_all_opencode_skills_have_name_and_description_in_frontmatter(self) -> None:
        skills_dir = REPO_ROOT / ".opencode" / "skills"
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_path = skill_dir / "SKILL.md"
                if skill_path.exists():
                    content = skill_path.read_text(encoding="utf-8")
                    self.assertIn(
                        "name:",
                        content,
                        f"{skill_dir.name} missing 'name' in frontmatter",
                    )
                    self.assertIn(
                        "description:",
                        content,
                        f"{skill_dir.name} missing 'description' in frontmatter",
                    )


class SkillMetadataValidationTests(unittest.TestCase):

    def test_all_claude_skills_have_required_metadata(self) -> None:
        for skill_path in discover_skills("claude"):
            with self.subTest(skill=skill_path.parent.name):
                problems = validate_skill_metadata(skill_path)
                self.assertEqual(
                    problems,
                    [],
                    f"{skill_path.parent.name} metadata issues: {problems}",
                )

    def test_all_opencode_skills_have_required_metadata(self) -> None:
        for skill_path in discover_skills("opencode"):
            with self.subTest(skill=skill_path.parent.name):
                problems = validate_skill_metadata(skill_path)
                self.assertEqual(
                    problems,
                    [],
                    f"{skill_path.parent.name} metadata issues: {problems}",
                )

    def test_claude_skills_do_not_require_legacy_metadata_fields(self) -> None:
        for skill_path in discover_skills("claude"):
            with self.subTest(skill=skill_path.parent.name):
                problems = validate_skill_metadata(skill_path)
                self.assertFalse(
                    any("version" in problem or "category" in problem for problem in problems),
                    f"{skill_path.parent.name} should not require legacy fields: {problems}",
                )

    def test_claude_skill_name_matches_directory_name(self) -> None:
        for skill_path in discover_skills("claude"):
            with self.subTest(skill=skill_path.parent.name):
                metadata = parse_frontmatter(skill_path)
                self.assertEqual(
                    metadata.get("name"),
                    skill_path.parent.name,
                    f"Claude skill name must match directory: {skill_path.parent.name}",
                )

    def test_opencode_skill_name_matches_directory_name(self) -> None:
        for skill_path in discover_skills("opencode"):
            with self.subTest(skill=skill_path.parent.name):
                metadata = parse_frontmatter(skill_path)
                self.assertEqual(
                    metadata.get("name"),
                    skill_path.parent.name,
                    f"OpenCode skill name must match directory: {skill_path.parent.name}",
                )

    def test_claude_skill_dependencies_are_valid(self) -> None:
        claude_skills = discover_skills("claude")
        all_skill_names = {p.parent.name for p in claude_skills}

        for skill_path in claude_skills:
            with self.subTest(skill=skill_path.parent.name):
                problems = validate_metadata_dependencies(skill_path, all_skill_names)
                self.assertEqual(
                    problems,
                    [],
                    f"{skill_path.parent.name} dependency issues: {problems}",
                )

    def test_opencode_skill_dependencies_are_valid(self) -> None:
        opencode_skills = discover_skills("opencode")
        all_skill_names = {p.parent.name for p in opencode_skills}

        for skill_path in opencode_skills:
            with self.subTest(skill=skill_path.parent.name):
                problems = validate_metadata_dependencies(skill_path, all_skill_names)
                self.assertEqual(
                    problems,
                    [],
                    f"{skill_path.parent.name} dependency issues: {problems}",
                )

    def test_claude_skill_budget_format_is_valid(self) -> None:
        for skill_path in discover_skills("claude"):
            with self.subTest(skill=skill_path.parent.name):
                problems = validate_metadata_budget(skill_path)
                self.assertEqual(
                    problems,
                    [],
                    f"{skill_path.parent.name} budget issues: {problems}",
                )

    def test_opencode_skill_budget_format_is_valid(self) -> None:
        for skill_path in discover_skills("opencode"):
            with self.subTest(skill=skill_path.parent.name):
                problems = validate_metadata_budget(skill_path)
                self.assertEqual(
                    problems,
                    [],
                    f"{skill_path.parent.name} budget issues: {problems}",
                )


class ContractDriftPressureTests(unittest.TestCase):
    """Pressure tests that verify contract parity validation catches drift issues."""

    def test_missing_contract_reference_detected(self) -> None:
        fixture_skill = (
            REPO_ROOT
            / "tests"
            / "fixtures"
            / "invalid-skills"
            / "missing-contract-reference"
            / "SKILL.md"
        )
        problems = validate_contract_references(fixture_skill)
        self.assertNotEqual(problems, [])
        self.assertIn("missing canonical contract reference", problems[0])

    def test_wrong_status_vocabulary_detected(self) -> None:
        fixture_skill = (
            REPO_ROOT
            / "tests"
            / "fixtures"
            / "invalid-skills"
            / "wrong-status-vocabulary"
            / "SKILL.md"
        )
        content = fixture_skill.read_text(encoding="utf-8")
        self.assertIn("FAILED", content)
        self.assertIn("MISSING", content)

    def test_incomplete_hard_gates_detected(self) -> None:
        canonical_contract = REPO_ROOT / "docs" / "archived-workflows" / "pre-commit.md"
        fixture_skill = (
            REPO_ROOT
            / "tests"
            / "fixtures"
            / "invalid-skills"
            / "incomplete-hard-gates"
            / "SKILL.md"
        )
        problems = validate_hard_gate_semantics(canonical_contract, fixture_skill)
        self.assertNotEqual(problems, [])
        self.assertTrue(
            any("missing hard-gate semantic" in problem for problem in problems)
        )


class ContractStructureValidationTests(unittest.TestCase):
    """Validate that all canonical contracts conform to the required section template."""

    def test_at_least_one_contract_discovered(self) -> None:
        contracts = discover_contracts()
        self.assertGreater(
            len(contracts), 0, "No canonical contracts found in docs/archived-workflows/"
        )

    def test_all_contracts_have_required_sections(self) -> None:
        for contract in discover_contracts():
            with self.subTest(contract=contract.name):
                problems = validate_contract_structure(contract)
                self.assertEqual(
                    problems,
                    [],
                    f"{contract.name} structure issues: {problems}",
                )

    def test_all_contracts_have_h1_title(self) -> None:
        for contract in discover_contracts():
            with self.subTest(contract=contract.name):
                content = contract.read_text(encoding="utf-8")
                self.assertRegex(
                    content,
                    r"^# .+",
                    f"{contract.name} missing H1 title",
                )


class ContractStructurePressureTests(unittest.TestCase):
    """Pressure tests verifying validate_contract_structure catches malformed contracts."""

    def test_missing_sections_detected(self) -> None:
        fixture = (
            REPO_ROOT
            / "tests"
            / "fixtures"
            / "invalid-contracts"
            / "missing-sections"
            / "contract.md"
        )
        problems = validate_contract_structure(fixture)
        self.assertNotEqual(problems, [])
        self.assertTrue(
            any("missing required sections" in p for p in problems),
            f"Expected 'missing required sections' in {problems}",
        )

    def test_empty_contract_detected(self) -> None:
        fixture = (
            REPO_ROOT
            / "tests"
            / "fixtures"
            / "invalid-contracts"
            / "empty-contract"
            / "contract.md"
        )
        problems = validate_contract_structure(fixture)
        self.assertNotEqual(problems, [])
        self.assertIn("contract file is empty", problems)

    def test_nonexistent_contract_detected(self) -> None:
        fixture = REPO_ROOT / "tests" / "fixtures" / "nonexistent-contract.md"
        problems = validate_contract_structure(fixture)
        self.assertNotEqual(problems, [])
        self.assertTrue(
            any("does not exist" in p for p in problems),
            f"Expected 'does not exist' in {problems}",
        )


class CanonicalContractGovernanceTests(unittest.TestCase):
    """Validate canonical contract schema/registry and contributor guidance."""

    def test_contract_registry_is_valid(self) -> None:
        problems = validate_contract_registry()
        self.assertEqual(problems, [], f"Contract registry issues: {problems}")

    def test_contract_contributor_guide_is_discoverable_and_complete(self) -> None:
        problems = validate_contract_contributor_guide()
        self.assertEqual(
            problems,
            [],
            f"Contract contributor guide issues: {problems}",
        )


if __name__ == "__main__":
    unittest.main()

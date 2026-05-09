from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SESSION_START_HOOK = REPO_ROOT / ".claude" / "hooks" / "session-start.sh"


def run_session_start(project_dir: Path) -> dict[str, object]:
    env = os.environ.copy()
    env["CLAUDE_PROJECT_DIR"] = str(project_dir)
    result = subprocess.run(
        ["bash", str(SESSION_START_HOOK)],
        check=True,
        capture_output=True,
        text=True,
        env=env,
        cwd=REPO_ROOT,
    )
    return json.loads(result.stdout)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_skill(skill_path: Path, required_phrases: list[str]) -> list[str]:
    content = read_text(skill_path)
    problems: list[str] = []
    if "## Hard Gate" not in content and "## Hard Gates" not in content:
        problems.append("missing hard-gate section")
    missing_phrases = [phrase for phrase in required_phrases if phrase not in content]
    if missing_phrases:
        problems.append(f"missing phrases: {', '.join(missing_phrases)}")
    return problems


def parse_canonical_contract(contract_path: Path) -> dict[str, list[str]]:
    """Parse canonical contract to extract requirements."""
    if not contract_path.exists():
        return {}

    content = read_text(contract_path)
    requirements = {
        "hard_gates": [],
        "status_vocabulary": [],
        "required_references": [],
    }

    # Extract hard gates from ## Hard Gates section
    hard_gates_match = re.search(
        r"## Hard Gates\s*\n(.*?)(?=\n##|\nz)", content, re.DOTALL
    )
    if hard_gates_match:
        hard_gates_section = hard_gates_match.group(1)
        # Find MUST requirements
        must_gates = re.findall(r"\*\*(.*?MUST.*?)\*\*", hard_gates_section)
        requirements["hard_gates"] = must_gates

    # Extract status vocabulary
    status_match = re.search(
        r"## Status Vocabulary\s*\n(.*?)(?=\n##|\nz)", content, re.DOTALL
    )
    if status_match:
        status_section = status_match.group(1)
        # Find status indicators
        status_indicators = re.findall(r"- `([^`]+)`:", status_section)
        requirements["status_vocabulary"] = status_indicators

    # Extract required references
    ref_match = re.search(
        r"## Required References\s*\n(.*?)(?=\n##|\nz)", content, re.DOTALL
    )
    if ref_match:
        ref_section = ref_match.group(1)
        # Find markdown links and file paths
        refs = re.findall(r"- `([^`]+\.md)`", ref_section)
        requirements["required_references"] = refs

    return requirements


def validate_contract_references(adapter_path: Path) -> list[str]:
    """Verify adapter references valid canonical contract."""
    problems: list[str] = []
    content = read_text(adapter_path)

    # Check for canonical contract reference
    contract_refs = re.findall(r"`docs/(?:workflows|archived-workflows)/([^`]+\.md)`", content)
    if not contract_refs:
        problems.append("missing canonical contract reference (docs/archived-workflows/*.md)")
        return problems

    # Validate referenced contract files exist
    for contract_ref in contract_refs:
        contract_path = REPO_ROOT / "docs" / "archived-workflows" / contract_ref
        if not contract_path.exists():
            problems.append(
                f"referenced contract does not exist: docs/archived-workflows/{contract_ref}"
            )

    return problems


def validate_hard_gate_semantics(
    canonical_contract: Path, adapter_path: Path
) -> list[str]:
    problems: list[str] = []

    if not canonical_contract.exists():
        problems.append(f"canonical contract not found: {canonical_contract}")
        return problems

    adapter_content = read_text(adapter_path)

    if "## Hard Gate" not in adapter_content and "## Hard Gates" not in adapter_content:
        problems.append("missing hard-gate section")
        return problems

    hard_gate_match = re.search(
        r"## Hard Gates?\s*\n(.*?)(?=\n## |\n\Z)", adapter_content, re.DOTALL
    )
    if not hard_gate_match:
        problems.append("malformed hard-gate section")
        return problems

    hard_gate_content = hard_gate_match.group(1)

    expected_semantics = [
        "Unit tests MUST pass",
        "Build MUST succeed",
        "Lint MUST pass",
        "NOT READY",
        "NOT CONFIGURED",
    ]

    for semantic in expected_semantics:
        if semantic not in hard_gate_content and semantic not in adapter_content:
            problems.append(f"missing hard-gate semantic: {semantic}")

    return problems


def validate_status_vocabulary(
    canonical_contract: Path, adapter_path: Path
) -> list[str]:
    problems: list[str] = []

    if not canonical_contract.exists():
        problems.append(f"canonical contract not found: {canonical_contract}")
        return problems

    adapter_content = read_text(adapter_path)

    hard_gate_match = re.search(
        r"## Hard Gates?\s*\n(.*?)(?=\n## |\n\Z)", adapter_content, re.DOTALL
    )
    output_format_match = re.search(
        r"## Status Vocabulary\s*\n(.*?)(?=\n## |\n\Z)",
        adapter_content,
        re.DOTALL | re.IGNORECASE,
    )

    relevant_sections = ""
    if hard_gate_match:
        relevant_sections += hard_gate_match.group(1)
    if output_format_match:
        relevant_sections += output_format_match.group(1)

    if not relevant_sections.strip():
        relevant_sections = adapter_content

    required_status = ["READY", "NOT READY", "NOT CONFIGURED"]
    for status in required_status:
        if (
            f"`{status}`" not in relevant_sections
            and f"'{status}'" not in relevant_sections
            and status not in relevant_sections
        ):
            problems.append(f"missing required status vocabulary: {status}")

    return problems


# Required top-level sections for every canonical workflow contract.
# Derived from the template in docs/workflows/README.md.
REQUIRED_CONTRACT_SECTIONS: list[str] = [
    "Purpose",
    "Trigger Conditions",
    "Hard Gates",
    "Workflow Steps",
    "Status Vocabulary",
    "Fail/Fix/Rerun Loop",
    "Token Budget Intent",
    "Required References",
]

CONTRACT_SCHEMA_PATH = REPO_ROOT / "schemas" / "canonical-workflow-contract.schema.json"
CONTRACT_REGISTRY_PATH = REPO_ROOT / "docs" / "archived-workflows" / "contracts.registry.json"
CONTRACT_GUIDE_PATH = REPO_ROOT / "docs" / "archived-workflows" / "CONTRIBUTING.md"


def load_contract_schema() -> dict[str, object]:
    if not CONTRACT_SCHEMA_PATH.exists():
        return {}
    try:
        return json.loads(read_text(CONTRACT_SCHEMA_PATH))
    except json.JSONDecodeError:
        return {}


def schema_required_sections() -> list[str]:
    schema = load_contract_schema()
    sections = schema.get("required_sections") if isinstance(schema, dict) else None
    if isinstance(sections, list) and all(isinstance(item, str) for item in sections):
        return list(sections)
    return REQUIRED_CONTRACT_SECTIONS


def discover_contracts() -> list[Path]:
    """Return all canonical contract files in docs/archived-workflows/ (excludes README)."""
    workflows_dir = REPO_ROOT / "docs" / "archived-workflows"
    if not workflows_dir.is_dir():
        return []
    excluded = {"readme.md", "template.md", "contributing.md"}
    return sorted(
        p
        for p in workflows_dir.glob("*.md")
        if p.name.lower() not in excluded
    )


def validate_contract_structure(contract_path: Path) -> list[str]:
    """Validate that a canonical contract contains all required sections."""
    problems: list[str] = []

    if not contract_path.exists():
        problems.append(f"contract file does not exist: {contract_path}")
        return problems

    content = read_text(contract_path)

    if not content.strip():
        problems.append("contract file is empty")
        return problems

    if not re.search(r"^# .+", content, re.MULTILINE):
        problems.append("missing H1 title")

    present_sections = re.findall(r"^## (.+)$", content, re.MULTILINE)
    present_set = {s.strip() for s in present_sections}

    missing = [s for s in schema_required_sections() if s not in present_set]
    if missing:
        problems.append(f"missing required sections: {', '.join(missing)}")

    return problems


def validate_contract_registry() -> list[str]:
    problems: list[str] = []

    schema = load_contract_schema()
    if not schema:
        problems.append("missing or invalid canonical contract schema")
        return problems

    if not CONTRACT_REGISTRY_PATH.exists():
        problems.append(f"missing contract registry: {CONTRACT_REGISTRY_PATH}")
        return problems

    try:
        registry = json.loads(read_text(CONTRACT_REGISTRY_PATH))
    except json.JSONDecodeError as exc:
        problems.append(f"invalid registry JSON: {exc}")
        return problems

    if not isinstance(registry, dict):
        problems.append("registry root must be an object")
        return problems

    contracts = registry.get("contracts")
    if not isinstance(contracts, list):
        problems.append("registry must include a contracts array")
        return problems

    required_fields = {"id", "contract_path", "adapter_paths", "status"}
    for entry in contracts:
        if not isinstance(entry, dict):
            problems.append("registry contracts entries must be objects")
            continue

        missing = sorted(field for field in required_fields if field not in entry)
        if missing:
            problems.append(f"registry entry missing fields: {', '.join(missing)}")
            continue

        contract_value = entry.get("contract_path")
        if not isinstance(contract_value, str) or not contract_value.endswith(".md"):
            problems.append("registry contract_path must be a markdown path")
            continue

        contract_path = REPO_ROOT / contract_value
        problems.extend(validate_contract_structure(contract_path))

    discovered = {
        f"docs/archived-workflows/{path.name}"
        for path in discover_contracts()
    }
    indexed = {
        item.get("contract_path")
        for item in contracts
        if isinstance(item, dict) and isinstance(item.get("contract_path"), str)
    }

    missing_in_registry = sorted(discovered - indexed)
    if missing_in_registry:
        problems.append(
            "registry missing discovered contracts: " + ", ".join(missing_in_registry)
        )

    return problems


def validate_contract_contributor_guide() -> list[str]:
    problems: list[str] = []

    if not CONTRACT_GUIDE_PATH.exists():
        return [f"missing contributor guide: {CONTRACT_GUIDE_PATH}"]

    content = read_text(CONTRACT_GUIDE_PATH)
    required_phrases = [
        "when to create contracts",
        "adapter update process",
        "versioning strategy",
        "discovery mechanism",
    ]

    missing_phrases = [phrase for phrase in required_phrases if phrase not in content.lower()]
    if missing_phrases:
        problems.append(
            "contributor guide missing required topics: " + ", ".join(missing_phrases)
        )

    return problems


def validate_workflow_parity(workflow_name: str) -> list[str]:
    """Compare Claude skill vs OpenCode command for same workflow."""
    problems: list[str] = []

    # Paths for adapters
    claude_skill = REPO_ROOT / ".claude" / "skills" / workflow_name / "SKILL.md"
    opencode_command = REPO_ROOT / ".opencode" / "commands" / f"{workflow_name}.md"
    canonical_contract = REPO_ROOT / "docs" / "archived-workflows" / f"{workflow_name}.md"

    # Check if both adapters exist
    if not claude_skill.exists():
        problems.append(f"Claude skill missing: {claude_skill}")
    if not opencode_command.exists():
        problems.append(f"OpenCode command missing: {opencode_command}")

    if problems:  # Can't compare if adapters don't exist
        return problems

    # Validate both adapters against canonical contract
    if canonical_contract.exists():
        claude_problems = validate_hard_gate_semantics(canonical_contract, claude_skill)
        opencode_problems = validate_hard_gate_semantics(
            canonical_contract, opencode_command
        )

        for problem in claude_problems:
            problems.append(f"Claude adapter: {problem}")
        for problem in opencode_problems:
            problems.append(f"OpenCode adapter: {problem}")

        # Check both use same status vocabulary
        claude_status_problems = validate_status_vocabulary(
            canonical_contract, claude_skill
        )
        opencode_status_problems = validate_status_vocabulary(
            canonical_contract, opencode_command
        )

        for problem in claude_status_problems:
            problems.append(f"Claude status vocabulary: {problem}")
        for problem in opencode_status_problems:
            problems.append(f"OpenCode status vocabulary: {problem}")

    return problems


VALID_BUDGET_FREQUENCIES: list[str] = [
    "per-commit",
    "per-session",
    "on-demand",
]


def parse_frontmatter(skill_path: Path) -> dict[str, object]:
    content = read_text(skill_path)
    frontmatter_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not frontmatter_match:
        return {}

    import yaml

    try:
        return yaml.safe_load(frontmatter_match.group(1)) or {}
    except Exception:
        return {}


def validate_skill_metadata(skill_path: Path) -> list[str]:
    problems: list[str] = []
    metadata = parse_frontmatter(skill_path)

    if not metadata:
        problems.append("missing or malformed frontmatter")
        return problems

    required_fields = ["name", "description"]
    for field in required_fields:
        value = metadata.get(field)
        if value is None or str(value).strip() == "":
            problems.append(f"missing required metadata field: {field}")

    name = str(metadata.get("name", "")).strip()
    if name and not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", name):
        problems.append(
            "invalid name format: expected lowercase letters, numbers, and hyphens"
        )
    if name and len(name) > 64:
        problems.append("invalid name length: must be <= 64 characters")

    description = str(metadata.get("description", "")).strip()
    if description and len(description) > 1024:
        problems.append("invalid description length: must be <= 1024 characters")

    # Forbidden fields per Agent Skills spec compliance
    forbidden_fields = ["disable-model-invocation", "argument-hint", "user-invocable"]
    for field in forbidden_fields:
        if field in metadata:
            problems.append(f"forbidden field in frontmatter: {field}")

    return problems


def validate_metadata_dependencies(
    skill_path: Path, all_skill_names: set[str]
) -> list[str]:
    problems: list[str] = []
    metadata = parse_frontmatter(skill_path)

    dependencies = metadata.get("dependencies", [])
    if not dependencies:
        return problems

    if not isinstance(dependencies, list):
        problems.append("dependencies must be a list")
        return problems

    for dep in dependencies:
        if dep not in all_skill_names:
            problems.append(f"dependency '{dep}' does not exist")

    return problems


def validate_metadata_budget(skill_path: Path) -> list[str]:
    problems: list[str] = []
    metadata = parse_frontmatter(skill_path)

    budget = metadata.get("budget")
    if not budget:
        return problems

    if not isinstance(budget, dict):
        problems.append("budget must be an object")
        return problems

    tokens = budget.get("tokens")
    if tokens is not None and (not isinstance(tokens, int) or tokens <= 0):
        problems.append("budget.tokens must be a positive integer")

    frequency = budget.get("frequency")
    if frequency is not None and frequency not in VALID_BUDGET_FREQUENCIES:
        problems.append(
            f"budget.frequency '{frequency}' must be one of {', '.join(VALID_BUDGET_FREQUENCIES)}"
        )

    return problems


def discover_skills(surface: str) -> list[Path]:
    skills_dir = REPO_ROOT / f".{surface}" / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(p for p in skills_dir.rglob("SKILL.md"))

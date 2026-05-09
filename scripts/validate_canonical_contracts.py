#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = REPO_ROOT / "schemas" / "canonical-workflow-contract.schema.json"
DEFAULT_REGISTRY = REPO_ROOT / "docs" / "archived-workflows" / "contracts.registry.json"
DEFAULT_WORKFLOWS = REPO_ROOT / "docs" / "archived-workflows"
DEFAULT_REQUIRED_SECTIONS: tuple[str, ...] = (
    "Purpose",
    "Trigger Conditions",
    "Hard Gates",
    "Workflow Steps",
    "Status Vocabulary",
    "Fail/Fix/Rerun Loop",
    "Token Budget Intent",
    "Required References",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate canonical workflow contracts using schema + registry."
    )
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    parser.add_argument("--workflows-dir", default=str(DEFAULT_WORKFLOWS))
    return parser.parse_args()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def required_sections_from_schema(schema: dict[str, object]) -> list[str]:
    sections = schema.get("required_sections")
    if isinstance(sections, list) and all(isinstance(item, str) for item in sections):
        return list(sections)
    return list(DEFAULT_REQUIRED_SECTIONS)


def discover_contracts(workflows_dir: Path) -> list[Path]:
    excluded = {"readme.md", "template.md", "contributing.md"}
    return sorted(
        path
        for path in workflows_dir.glob("*.md")
        if path.name.lower() not in excluded
    )


def validate_contract_content(contract_path: Path, required_sections: list[str]) -> list[str]:
    issues: list[str] = []
    content = contract_path.read_text(encoding="utf-8")
    if not content.strip():
        return [f"{contract_path}: contract file is empty"]
    if not re.search(r"^# .+", content, re.MULTILINE):
        issues.append(f"{contract_path}: missing H1 title")

    present = {value.strip() for value in re.findall(r"^## (.+)$", content, re.MULTILINE)}
    missing = [section for section in required_sections if section not in present]
    if missing:
        issues.append(
            f"{contract_path}: missing required sections: {', '.join(missing)}"
        )
    return issues


def validate_registry_entries(registry: dict[str, object]) -> list[str]:
    issues: list[str] = []
    contracts = registry.get("contracts")
    if not isinstance(contracts, list):
        return ["registry must include a contracts array"]

    required = {"id", "contract_path", "adapter_paths", "status"}
    for entry in contracts:
        if not isinstance(entry, dict):
            issues.append("registry contracts entries must be objects")
            continue
        missing = sorted(field for field in required if field not in entry)
        if missing:
            issues.append(f"registry entry missing fields: {', '.join(missing)}")
        adapters = entry.get("adapter_paths")
        if not isinstance(adapters, list) or not adapters:
            issues.append("registry entry adapter_paths must be a non-empty array")
    return issues


def validate_registry_coverage(
    contracts: list[Path], registry: dict[str, object], workflows_dir: Path
) -> list[str]:
    issues: list[str] = []
    entries = registry.get("contracts") if isinstance(registry, dict) else None
    if not isinstance(entries, list):
        return ["registry must include a contracts array"]

    discovered = {
        f"docs/archived-workflows/{path.name}" for path in contracts
    }
    indexed = {
        value.get("contract_path")
        for value in entries
        if isinstance(value, dict) and isinstance(value.get("contract_path"), str)
    }
    missing = sorted(discovered - indexed)
    if missing:
        issues.append("registry missing discovered contracts: " + ", ".join(missing))

    for path in indexed:
        if not isinstance(path, str):
            continue
        absolute = REPO_ROOT / path
        if not absolute.exists():
            issues.append(f"registry references missing contract: {path}")

    return issues


def main() -> int:
    args = parse_args()
    schema_path = Path(args.schema)
    registry_path = Path(args.registry)
    workflows_dir = Path(args.workflows_dir)

    issues: list[str] = []
    if not schema_path.exists():
        issues.append(f"missing schema: {schema_path}")
    if not registry_path.exists():
        issues.append(f"missing registry: {registry_path}")
    if not workflows_dir.exists():
        issues.append(f"missing workflows directory: {workflows_dir}")

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}", file=sys.stderr)
        return 1

    try:
        schema = read_json(schema_path)
        registry = read_json(registry_path)
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 1

    required_sections = required_sections_from_schema(schema)
    contracts = discover_contracts(workflows_dir)

    issues.extend(validate_registry_entries(registry))
    issues.extend(validate_registry_coverage(contracts, registry, workflows_dir))

    for contract in contracts:
        issues.extend(validate_contract_content(contract, required_sections))

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}", file=sys.stderr)
        return 1

    print(f"Validated {len(contracts)} canonical contracts against schema + registry")
    return 0


if __name__ == "__main__":
    sys.exit(main())

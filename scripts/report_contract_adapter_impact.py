#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTRACT_DIR = REPO_ROOT / "docs" / "workflows"
CONTRACT_REF_PATTERN = re.compile(r"`docs/workflows/([^`]+\.md)`")

ADAPTER_GLOBS: tuple[str, ...] = (
    ".claude/skills/**/SKILL.md",
    ".opencode/commands/*.md",
    ".cursor/rules/*.md",
    ".github/copilot-instructions.md",
    ".github/instructions/*.md",
)


@dataclass(frozen=True)
class Impact:
    contract: str
    adapter: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Report adapters that reference changed canonical workflow contracts. "
            "Notification-only: exits 0 and emits warnings."
        )
    )
    parser.add_argument(
        "--base",
        help="Base git ref/sha for diff detection (used with --head).",
    )
    parser.add_argument(
        "--head",
        help="Head git ref/sha for diff detection (used with --base).",
    )
    parser.add_argument(
        "--changed-contract",
        action="append",
        default=[],
        help=(
            "Relative contract path under docs/workflows/, for example pre-commit.md. "
            "Can be passed multiple times."
        ),
    )
    return parser.parse_args()


def resolve_changed_contracts(args: argparse.Namespace) -> list[str]:
    manual = [
        normalize_contract_path(value)
        for value in args.changed_contract
        if normalize_contract_path(value)
    ]
    if manual:
        return sorted(set(manual))

    if not args.base or not args.head:
        return []

    changed_files = git_diff_names(args.base, args.head)
    contracts: list[str] = []
    for file_path in changed_files:
        if not file_path.startswith("docs/workflows/"):
            continue
        leaf = file_path.removeprefix("docs/workflows/")
        if not leaf.endswith(".md"):
            continue
        if leaf.lower() == "readme.md":
            continue
        contracts.append(leaf)
    return sorted(set(contracts))


def normalize_contract_path(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    if not normalized:
        return ""
    if normalized.startswith("docs/workflows/"):
        normalized = normalized.removeprefix("docs/workflows/")
    if normalized.lower() == "readme.md":
        return ""
    if not normalized.endswith(".md"):
        return ""
    return normalized


def git_diff_names(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", base, head],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or "unknown git diff failure"
        raise RuntimeError(f"git diff failed: {message}")

    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def discover_adapter_files() -> list[Path]:
    files: set[Path] = set()
    for pattern in ADAPTER_GLOBS:
        files.update(REPO_ROOT.glob(pattern))
    return sorted(path for path in files if path.is_file())


def extract_contract_refs(adapter_file: Path) -> set[str]:
    content = adapter_file.read_text(encoding="utf-8")
    refs = {match for match in CONTRACT_REF_PATTERN.findall(content)}
    return {ref for ref in refs if normalize_contract_path(ref)}


def build_impacts(changed_contracts: list[str], adapter_files: list[Path]) -> list[Impact]:
    changed = set(changed_contracts)
    impacts: list[Impact] = []

    for adapter_file in adapter_files:
        refs = extract_contract_refs(adapter_file)
        matching = sorted(changed.intersection(refs))
        for contract in matching:
            impacts.append(
                Impact(
                    contract=contract,
                    adapter=adapter_file.relative_to(REPO_ROOT).as_posix(),
                )
            )

    return sorted(impacts, key=lambda item: (item.contract, item.adapter))


def emit_results(changed_contracts: list[str], impacts: list[Impact]) -> None:
    print("Contract Adapter Impact Analysis")
    print(f"Changed contracts: {len(changed_contracts)}")
    print(f"Impacted adapters: {len(impacts)}")

    if not changed_contracts:
        print("No canonical contract changes detected under docs/workflows/*.md")
        return

    print("")
    print("Changed canonical contracts:")
    for contract in changed_contracts:
        print(f"- docs/workflows/{contract}")

    print("")
    if not impacts:
        print("No adapter references found for changed contracts.")
        print("::notice title=Contract impact::No adapter references found")
        return

    print("Potentially affected adapters:")
    for impact in impacts:
        print(f"- {impact.adapter} (references docs/workflows/{impact.contract})")
        print(
            "::warning title=Contract adapter may need update::"
            f"{impact.adapter} references docs/workflows/{impact.contract}"
        )


def main() -> int:
    args = parse_args()

    try:
        changed_contracts = resolve_changed_contracts(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    adapter_files = discover_adapter_files()
    impacts = build_impacts(changed_contracts, adapter_files)
    emit_results(changed_contracts, impacts)
    return 0


if __name__ == "__main__":
    sys.exit(main())

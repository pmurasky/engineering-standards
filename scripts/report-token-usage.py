#!/usr/bin/env python3

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def estimate_tokens(text: str) -> int:
    return max(1, math.ceil(len(text) / 4))


def collect_skill_files() -> list[Path]:
    return sorted((REPO_ROOT / ".claude" / "skills").glob("*/SKILL.md"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report approximate token usage for Claude skill files."
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1000,
        help="Maximum allowed token estimate per skill (default: 1000).",
    )
    parser.add_argument(
        "--fail-on-exceed",
        action="store_true",
        help="Exit non-zero when any skill exceeds --max-tokens.",
    )
    args = parser.parse_args()

    skill_files = collect_skill_files()
    if not skill_files:
        print("No skill files found under .claude/skills")
        return 0

    exceeded = []
    print("skill,tokens,status")
    for skill_file in skill_files:
        text = skill_file.read_text(encoding="utf-8")
        tokens = estimate_tokens(text)
        status = "OK"
        if tokens > args.max_tokens:
            status = "EXCEEDS"
            exceeded.append((skill_file, tokens))
        relative = skill_file.relative_to(REPO_ROOT)
        print(f"{relative},{tokens},{status}")

    if exceeded:
        print("\nExceeded token budget:")
        for skill_file, tokens in exceeded:
            relative = skill_file.relative_to(REPO_ROOT)
            print(f"- {relative}: {tokens} > {args.max_tokens}")

    if args.fail_on_exceed and exceeded:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

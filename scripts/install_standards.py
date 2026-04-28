#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from standards_distribution import (
    classify_install_changes,
    copy_managed_files,
    expand_profile_sources,
    format_conflicts,
    read_install_manifest,
    resolve_profiles,
    summarize_changes,
    utc_now,
    write_install_manifest,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install engineering-standards into a downstream project.",
    )
    parser.add_argument(
        "--target",
        default=".",
        help="Target project root (default: current directory).",
    )
    parser.add_argument(
        "--profile",
        action="append",
        dest="profiles",
        help="Additional tool profile to install (opencode, claude, cursor, copilot).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite conflicting existing files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_root = Path(args.target).resolve()
    target_root.mkdir(parents=True, exist_ok=True)

    existing_manifest = read_install_manifest(target_root)
    if existing_manifest is not None:
        print(
            "engineering-standards is already installed in this target. "
            "Use scripts/update_standards.py instead.",
            file=sys.stderr,
        )
        return 1

    profile_names = resolve_profiles(args.profiles)
    managed_files = expand_profile_sources(profile_names)
    changes, conflicts = classify_install_changes(target_root, managed_files, args.force)
    if conflicts:
        print(format_conflicts(conflicts), file=sys.stderr)
        print("Re-run with --force to overwrite conflicting files.", file=sys.stderr)
        return 1

    summary = summarize_changes(changes)
    print(f"Profiles: {', '.join(profile_names)}")
    print(
        f"Planned changes: create={summary['create']} overwrite={summary['overwrite']} keep={summary['keep']}"
    )

    if args.dry_run:
        print("Dry run only; no files were written.")
        return 0

    managed_entries = copy_managed_files(target_root, managed_files)
    write_install_manifest(target_root, profile_names, managed_entries, utc_now())
    print("engineering-standards installed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from standards_distribution import (
    classify_update_changes,
    copy_managed_files,
    expand_profile_sources,
    format_conflicts,
    prune_empty_directories,
    read_install_manifest,
    remove_stale_files,
    resolve_profiles,
    summarize_changes,
    write_install_manifest,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update an existing engineering-standards installation.",
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
        help="Override installed profiles for this update.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite locally modified managed files.",
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

    manifest = read_install_manifest(target_root)
    if manifest is None:
        print(
            "No engineering-standards installation manifest found in target. "
            "Run scripts/install_standards.py first.",
            file=sys.stderr,
        )
        return 1

    requested_profiles = args.profiles or manifest.get("profiles")
    profile_names = resolve_profiles(requested_profiles)
    managed_files = expand_profile_sources(profile_names)
    changes, conflicts, removals = classify_update_changes(
        target_root,
        manifest,
        managed_files,
        args.force,
    )
    if conflicts:
        print("Local changes detected in managed files.", file=sys.stderr)
        print(format_conflicts(conflicts), file=sys.stderr)
        print("Re-run with --force to overwrite managed local changes.", file=sys.stderr)
        return 1

    summary = summarize_changes(changes)
    print(f"Profiles: {', '.join(profile_names)}")
    print(
        f"Planned changes: create={summary['create']} overwrite={summary['overwrite']} keep={summary['keep']} remove={len(removals)}"
    )

    if args.dry_run:
        print("Dry run only; no files were written.")
        return 0

    remove_stale_files(target_root, removals)
    prune_empty_directories(target_root, removals)
    managed_entries = copy_managed_files(target_root, managed_files)
    write_install_manifest(
        target_root,
        profile_names,
        managed_entries,
        manifest.get("installed_at"),
    )
    print("engineering-standards updated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

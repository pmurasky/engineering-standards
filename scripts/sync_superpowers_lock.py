#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCK_FILE = REPO_ROOT / "upstream" / "superpowers.lock.json"
DEFAULT_MIRROR_DIR = REPO_ROOT / "upstream" / "superpowers"


def load_lock(lock_path: Path) -> Dict[str, Any]:
    with lock_path.open(encoding="utf-8") as handle:
        return json.load(handle)


def resolve_commit(repo: str, branch: str) -> str:
    result = subprocess.run(
        ["git", "ls-remote", repo, f"refs/heads/{branch}"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to resolve upstream commit: {result.stderr.strip()}")

    first_line = result.stdout.strip().splitlines()
    if not first_line:
        raise RuntimeError("Upstream branch lookup returned no commit")

    commit = first_line[0].split()[0].strip()
    if len(commit) != 40:
        raise RuntimeError(f"Unexpected commit hash format: {commit}")
    return commit


def iter_tracked_files(mirror_dir: Path, source_paths: List[str]) -> List[Path]:
    files: List[Path] = []
    for source_path in source_paths:
        target = mirror_dir / source_path
        if target.is_file():
            files.append(target)
            continue
        if target.is_dir():
            files.extend(path for path in target.rglob("*") if path.is_file())
    return sorted(files)


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def build_checksums(mirror_dir: Path, source_paths: List[str]) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    for file_path in iter_tracked_files(mirror_dir, source_paths):
        relative = file_path.relative_to(mirror_dir).as_posix()
        entries.append({"path": relative, "sha256": sha256_file(file_path)})
    return entries


def write_lock(lock_path: Path, data: Dict[str, Any]) -> None:
    with lock_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def sync_lock(lock_path: Path, mirror_dir: Path, pinned_commit: str | None, dry_run: bool) -> int:
    lock = load_lock(lock_path)
    upstream = lock.get("upstream", {})

    repo = upstream.get("repo")
    branch = upstream.get("branch")
    if not repo or not branch:
        raise RuntimeError("Lockfile upstream.repo and upstream.branch are required")

    commit = pinned_commit if pinned_commit else resolve_commit(repo, branch)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    source_paths = lock.get("source_paths", [])
    if not isinstance(source_paths, list):
        raise RuntimeError("Lockfile source_paths must be an array")

    checksums = build_checksums(mirror_dir, source_paths)

    lock["generated_at"] = generated_at
    lock.setdefault("upstream", {})["pinned_commit"] = commit
    lock["checksums"] = checksums

    if dry_run:
        print(f"[dry-run] upstream commit: {commit}")
        print(f"[dry-run] checksum entries: {len(checksums)}")
        return 0

    write_lock(lock_path, lock)
    try:
        display_path = str(lock_path.relative_to(REPO_ROOT))
    except ValueError:
        display_path = str(lock_path)

    print(f"Updated {display_path}")
    print(f"- upstream commit: {commit}")
    print(f"- checksum entries: {len(checksums)}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync upstream/superpowers.lock.json with latest upstream commit and local mirror checksums."
    )
    parser.add_argument(
        "--lockfile",
        default=str(DEFAULT_LOCK_FILE),
        help="Path to lockfile (default: upstream/superpowers.lock.json).",
    )
    parser.add_argument(
        "--mirror-dir",
        default=str(DEFAULT_MIRROR_DIR),
        help="Path to mirrored upstream files (default: upstream/superpowers).",
    )
    parser.add_argument(
        "--pinned-commit",
        help="Optional explicit commit hash (skips network lookup).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute and print updates without writing lockfile.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    lock_path = Path(args.lockfile).resolve()
    mirror_dir = Path(args.mirror_dir).resolve()

    if not lock_path.exists():
        print(f"Lockfile not found: {lock_path}", file=sys.stderr)
        return 2

    if not mirror_dir.exists():
        print(f"Mirror directory not found: {mirror_dir}", file=sys.stderr)
        return 2

    try:
        return sync_lock(lock_path, mirror_dir, args.pinned_commit, args.dry_run)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

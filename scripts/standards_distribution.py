#!/usr/bin/env python3

from __future__ import annotations

import json
import hashlib
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_MANIFEST = REPO_ROOT / "distribution" / "standards-package.json"
INSTALL_STATE = Path(".engineering-standards") / "manifest.json"
SOURCE_REPO = "https://github.com/pmurasky/engineering-standards"


@dataclass(frozen=True)
class ManagedFile:
    relative_path: str
    source_path: Path


@dataclass(frozen=True)
class PlannedChange:
    relative_path: str
    action: str


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def git_output(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return "unknown"
    return result.stdout.strip() or "unknown"


def source_revision() -> str:
    return git_output("rev-parse", "HEAD")


def source_version() -> str:
    return git_output("describe", "--tags", "--always")


def load_package_manifest() -> dict[str, Any]:
    return load_json(PACKAGE_MANIFEST)


def ensure_known_profiles(profile_names: list[str], package: dict[str, Any]) -> list[str]:
    known_profiles = package["profiles"]
    unknown = [name for name in profile_names if name not in known_profiles]
    if unknown:
        supported = ", ".join(sorted(known_profiles))
        missing = ", ".join(sorted(unknown))
        raise ValueError(f"Unknown profiles: {missing}. Supported profiles: {supported}")
    return profile_names


def resolve_profiles(requested_profiles: list[str] | None) -> list[str]:
    package = load_package_manifest()
    if requested_profiles:
        profiles = list(dict.fromkeys(["core", *requested_profiles]))
        return ensure_known_profiles(profiles, package)

    defaults = package.get("default_profiles", ["core", "opencode"])
    return ensure_known_profiles(list(dict.fromkeys(defaults)), package)


def expand_profile_sources(profile_names: list[str]) -> list[ManagedFile]:
    package = load_package_manifest()
    sources: list[ManagedFile] = []
    seen: set[str] = set()

    for profile_name in profile_names:
        for source_rel in package["profiles"][profile_name]:
            source_path = REPO_ROOT / source_rel
            if source_path.is_dir():
                for file_path in sorted(path for path in source_path.rglob("*") if path.is_file()):
                    relative_path = file_path.relative_to(REPO_ROOT).as_posix()
                    if relative_path not in seen:
                        seen.add(relative_path)
                        sources.append(ManagedFile(relative_path, file_path))
                continue

            if not source_path.exists():
                raise FileNotFoundError(f"Packaged source missing: {source_rel}")

            relative_path = source_path.relative_to(REPO_ROOT).as_posix()
            if relative_path not in seen:
                seen.add(relative_path)
                sources.append(ManagedFile(relative_path, source_path))

    return sources


def read_install_manifest(target_root: Path) -> dict[str, Any] | None:
    manifest_path = target_root / INSTALL_STATE
    if not manifest_path.exists():
        return None
    return load_json(manifest_path)


def target_checksum(target_root: Path, relative_path: str) -> str | None:
    target_path = target_root / relative_path
    if not target_path.exists() or not target_path.is_file():
        return None
    return sha256_file(target_path)


def manifest_checksums(manifest: dict[str, Any]) -> dict[str, str]:
    managed_files = manifest.get("managed_files", [])
    return {entry["path"]: entry["sha256"] for entry in managed_files}


def classify_install_changes(
    target_root: Path,
    managed_files: list[ManagedFile],
    force: bool,
) -> tuple[list[PlannedChange], list[str]]:
    changes: list[PlannedChange] = []
    conflicts: list[str] = []

    for managed_file in managed_files:
        target_path = target_root / managed_file.relative_path
        if not target_path.exists():
            changes.append(PlannedChange(managed_file.relative_path, "create"))
            continue

        source_hash = sha256_file(managed_file.source_path)
        current_hash = sha256_file(target_path)
        if source_hash == current_hash:
            changes.append(PlannedChange(managed_file.relative_path, "keep"))
            continue

        if force:
            changes.append(PlannedChange(managed_file.relative_path, "overwrite"))
            continue

        conflicts.append(managed_file.relative_path)

    return changes, conflicts


def classify_update_changes(
    target_root: Path,
    manifest: dict[str, Any],
    managed_files: list[ManagedFile],
    force: bool,
) -> tuple[list[PlannedChange], list[str], list[str]]:
    previous_checksums = manifest_checksums(manifest)
    desired_paths = {file.relative_path for file in managed_files}
    changes: list[PlannedChange] = []
    conflicts: list[str] = []
    removals: list[str] = []

    for relative_path, installed_hash in previous_checksums.items():
        current_hash = target_checksum(target_root, relative_path)
        if current_hash is None:
            continue
        if current_hash != installed_hash and not force:
            conflicts.append(relative_path)

    for managed_file in managed_files:
        source_hash = sha256_file(managed_file.source_path)
        current_hash = target_checksum(target_root, managed_file.relative_path)

        if current_hash is None:
            changes.append(PlannedChange(managed_file.relative_path, "create"))
            continue
        if current_hash == source_hash:
            changes.append(PlannedChange(managed_file.relative_path, "keep"))
            continue
        if managed_file.relative_path in previous_checksums or force:
            changes.append(PlannedChange(managed_file.relative_path, "overwrite"))
            continue
        conflicts.append(managed_file.relative_path)

    for relative_path in previous_checksums:
        if relative_path not in desired_paths:
            removals.append(relative_path)

    return changes, conflicts, removals


def copy_managed_files(target_root: Path, managed_files: list[ManagedFile]) -> list[dict[str, str]]:
    manifest_entries: list[dict[str, str]] = []

    for managed_file in managed_files:
        target_path = target_root / managed_file.relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(managed_file.source_path, target_path)
        manifest_entries.append(
            {
                "path": managed_file.relative_path,
                "sha256": sha256_file(target_path),
            }
        )

    return manifest_entries


def remove_stale_files(target_root: Path, relative_paths: list[str]) -> None:
    for relative_path in relative_paths:
        target_path = target_root / relative_path
        if target_path.exists() and target_path.is_file():
            target_path.unlink()


def prune_empty_directories(target_root: Path, relative_paths: list[str]) -> None:
    candidate_dirs: set[Path] = set()
    for relative_path in relative_paths:
        path = (target_root / relative_path).parent
        while path != target_root and path not in candidate_dirs:
            candidate_dirs.add(path)
            path = path.parent

    for directory in sorted(candidate_dirs, reverse=True):
        if directory.exists() and directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()


def write_install_manifest(
    target_root: Path,
    profile_names: list[str],
    managed_entries: list[dict[str, str]],
    installed_at: str | None,
) -> None:
    manifest_path = target_root / INSTALL_STATE
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    existing_manifest = read_install_manifest(target_root)
    first_installed = installed_at
    if existing_manifest is not None:
        first_installed = existing_manifest.get("installed_at")

    manifest = {
        "schema_version": 1,
        "package_manifest": PACKAGE_MANIFEST.relative_to(REPO_ROOT).as_posix(),
        "source_repo": SOURCE_REPO,
        "source_revision": source_revision(),
        "source_version": source_version(),
        "profiles": profile_names,
        "installed_at": first_installed or utc_now(),
        "updated_at": utc_now(),
        "managed_files": managed_entries,
    }

    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")


def summarize_changes(changes: list[PlannedChange]) -> dict[str, int]:
    summary = {"create": 0, "overwrite": 0, "keep": 0}
    for change in changes:
        summary[change.action] = summary.get(change.action, 0) + 1
    return summary


def format_conflicts(conflicts: list[str]) -> str:
    items = "\n".join(f"- {path}" for path in conflicts)
    return f"Conflicting files detected:\n{items}"

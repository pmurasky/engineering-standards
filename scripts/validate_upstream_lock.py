#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = REPO_ROOT / "schemas" / "upstream-superpowers-lock.schema.json"
DEFAULT_LOCKFILE = REPO_ROOT / "upstream" / "superpowers.lock.json"
DEFAULT_MIRROR_DIR = REPO_ROOT / "upstream" / "superpowers"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate superpowers lockfile against JSON schema and mirror checksum entries."
    )
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA), help="Path to lock schema file.")
    parser.add_argument("--lockfile", default=str(DEFAULT_LOCKFILE), help="Path to lockfile.")
    parser.add_argument(
        "--mirror-dir",
        default=str(DEFAULT_MIRROR_DIR),
        help="Path to mirrored upstream content for checksum path verification.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_schema(lock_data: dict, schema_data: dict) -> None:
    try:
        import jsonschema  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "jsonschema is required. Install with: python3 -m pip install jsonschema"
        ) from exc

    jsonschema.validate(instance=lock_data, schema=schema_data)


def validate_checksum_paths(lock_data: dict, mirror_dir: Path) -> list[str]:
    problems: list[str] = []
    checksums = lock_data.get("checksums", [])
    
    # Check for empty checksums array (governance gap)
    if not checksums:
        problems.append("checksums array is empty - run 'make sync-lock' to populate")
        return problems
    
    for entry in checksums:
        relative = entry.get("path")
        expected_sha256 = entry.get("sha256")
        
        if not isinstance(relative, str):
            continue
            
        target = mirror_dir / relative
        if not target.exists():
            problems.append(f"checksum path missing in mirror: {relative}")
            continue
            
        # Content integrity verification beyond path existence
        if expected_sha256:
            try:
                import hashlib
                actual_sha256 = hashlib.sha256(target.read_bytes()).hexdigest()
                if actual_sha256 != expected_sha256:
                    problems.append(f"checksum mismatch for {relative}: expected {expected_sha256}, got {actual_sha256}")
            except Exception as e:
                problems.append(f"failed to verify checksum for {relative}: {e}")
                
    return problems


def main() -> int:
    args = parse_args()
    schema_path = Path(args.schema).resolve()
    lock_path = Path(args.lockfile).resolve()
    mirror_dir = Path(args.mirror_dir).resolve()

    if not schema_path.exists():
        print(f"Schema not found: {schema_path}", file=sys.stderr)
        return 2
    if not lock_path.exists():
        print(f"Lockfile not found: {lock_path}", file=sys.stderr)
        return 2
    if not mirror_dir.exists():
        print(f"Mirror directory not found: {mirror_dir}", file=sys.stderr)
        return 2

    try:
        schema_data = load_json(schema_path)
        lock_data = load_json(lock_path)
        validate_schema(lock_data, schema_data)
        path_problems = validate_checksum_paths(lock_data, mirror_dir)
        if path_problems:
            for problem in path_problems:
                print(problem, file=sys.stderr)
            return 1
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print("Lockfile validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

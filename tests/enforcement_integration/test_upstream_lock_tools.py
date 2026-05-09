from __future__ import annotations

import importlib.util
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    from helpers import REPO_ROOT
except ModuleNotFoundError:
    from tests.enforcement_integration.helpers import REPO_ROOT


def has_jsonschema() -> bool:
    return importlib.util.find_spec("jsonschema") is not None


class UpstreamLockToolIntegrationTests(unittest.TestCase):
    def test_sync_script_updates_pinned_commit_and_checksums(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            mirror_dir = base / "upstream" / "superpowers"
            source_file = mirror_dir / "skills" / "sample.txt"
            source_file.parent.mkdir(parents=True, exist_ok=True)
            source_file.write_text("sample", encoding="utf-8")

            lockfile = base / "superpowers.lock.json"
            lock_data = {
                "schema_version": 1,
                "generated_at": "2026-03-14T00:00:00Z",
                "upstream": {
                    "repo": "https://github.com/obra/superpowers",
                    "branch": "main",
                    "pinned_commit": "0" * 40,
                },
                "source_paths": ["skills/"],
                "workflows": [],
                "checksums": [],
                "policy": {
                    "mirror_read_only": True,
                    "require_divergence_tag": True,
                    "consumer_paths_stable": True,
                },
            }
            lockfile.write_text(json.dumps(lock_data, indent=2) + "\n", encoding="utf-8")

            pinned_commit = "1" * 40
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/sync_superpowers_lock.py",
                    "--lockfile",
                    str(lockfile),
                    "--mirror-dir",
                    str(mirror_dir),
                    "--pinned-commit",
                    pinned_commit,
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            updated = json.loads(lockfile.read_text(encoding="utf-8"))
            self.assertEqual(updated["upstream"]["pinned_commit"], pinned_commit)
            self.assertEqual(len(updated["checksums"]), 1)
            self.assertEqual(updated["checksums"][0]["path"], "skills/sample.txt")
            expected_hash = hashlib.sha256(b"sample").hexdigest()
            self.assertEqual(updated["checksums"][0]["sha256"], expected_hash)

    def test_validate_script_passes_for_valid_lockfile(self) -> None:
        if not has_jsonschema():
            self.skipTest("jsonschema is not installed")

        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            schema_path = REPO_ROOT / "schemas" / "upstream-superpowers-lock.schema.json"
            mirror_dir = base / "upstream" / "superpowers"
            source_file = mirror_dir / "skills" / "sample.txt"
            source_file.parent.mkdir(parents=True, exist_ok=True)
            source_file.write_text("sample", encoding="utf-8")

            lockfile = base / "superpowers.lock.json"
            checksum = hashlib.sha256(b"sample").hexdigest()
            lock_data = {
                "$schema": "../schemas/upstream-superpowers-lock.schema.json",
                "schema_version": 1,
                "generated_at": "2026-03-14T00:00:00Z",
                "upstream": {
                    "repo": "https://github.com/obra/superpowers",
                    "branch": "main",
                    "pinned_commit": "2" * 40,
                },
                "source_paths": ["skills/"],
                "workflows": [
                    {
                        "workflow": "pre-commit",
                        "upstream_path": "skills",
                        "local_contract": "docs/archived-workflows/pre-commit.md",
                        "divergence": "extend",
                        "owner": "@maintainers/standards",
                        "adapters": {
                            "claude_skill": ".claude/skills/pre-commit/SKILL.md",
                            "opencode_command": ".opencode/commands/pre-commit.md",
                            "cursor_rule": ".cursor/rules/engineering-standards.md",
                            "copilot_instruction": ".github/instructions/micro-commit.instructions.md",
                        },
                    }
                ],
                "checksums": [{"path": "skills/sample.txt", "sha256": checksum}],
                "policy": {
                    "mirror_read_only": True,
                    "require_divergence_tag": True,
                    "consumer_paths_stable": True,
                },
            }
            lockfile.write_text(json.dumps(lock_data, indent=2) + "\n", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_upstream_lock.py",
                    "--schema",
                    str(schema_path),
                    "--lockfile",
                    str(lockfile),
                    "--mirror-dir",
                    str(mirror_dir),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Lockfile validation passed", result.stdout)

    def test_validate_script_fails_when_checksum_path_missing(self) -> None:
        if not has_jsonschema():
            self.skipTest("jsonschema is not installed")

        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            schema_path = REPO_ROOT / "schemas" / "upstream-superpowers-lock.schema.json"
            mirror_dir = base / "upstream" / "superpowers"
            mirror_dir.mkdir(parents=True, exist_ok=True)

            lockfile = base / "superpowers.lock.json"
            lock_data = {
                "$schema": "../schemas/upstream-superpowers-lock.schema.json",
                "schema_version": 1,
                "generated_at": "2026-03-14T00:00:00Z",
                "upstream": {
                    "repo": "https://github.com/obra/superpowers",
                    "branch": "main",
                    "pinned_commit": "3" * 40,
                },
                "source_paths": ["skills/"],
                "workflows": [
                    {
                        "workflow": "pre-commit",
                        "upstream_path": "skills",
                        "local_contract": "docs/archived-workflows/pre-commit.md",
                        "divergence": "extend",
                        "owner": "@maintainers/standards",
                        "adapters": {
                            "claude_skill": ".claude/skills/pre-commit/SKILL.md",
                            "opencode_command": ".opencode/commands/pre-commit.md",
                            "cursor_rule": ".cursor/rules/engineering-standards.md",
                            "copilot_instruction": ".github/instructions/micro-commit.instructions.md",
                        },
                    }
                ],
                "checksums": [
                    {
                        "path": "skills/missing.txt",
                        "sha256": "a" * 64,
                    }
                ],
                "policy": {
                    "mirror_read_only": True,
                    "require_divergence_tag": True,
                    "consumer_paths_stable": True,
                },
            }
            lockfile.write_text(json.dumps(lock_data, indent=2) + "\n", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_upstream_lock.py",
                    "--schema",
                    str(schema_path),
                    "--lockfile",
                    str(lockfile),
                    "--mirror-dir",
                    str(mirror_dir),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("checksum path missing in mirror: skills/missing.txt", result.stderr)


if __name__ == "__main__":
    unittest.main()

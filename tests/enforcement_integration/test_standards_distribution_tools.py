from __future__ import annotations

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


class StandardsDistributionToolTests(unittest.TestCase):
    def test_distribution_manifest_paths_exist(self) -> None:
        manifest_path = REPO_ROOT / "distribution" / "standards-package.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

        for profile_paths in manifest["profiles"].values():
            for relative_path in profile_paths:
                with self.subTest(path=relative_path):
                    self.assertTrue(
                        (REPO_ROOT / relative_path).exists(),
                        f"Packaged path missing: {relative_path}",
                    )

    def test_opencode_skills_mirror_claude_skill_names(self) -> None:
        claude_skills = {
            path.parent.name
            for path in (REPO_ROOT / ".claude" / "skills").glob("*/SKILL.md")
        }
        opencode_skills = {
            path.parent.name
            for path in (REPO_ROOT / ".opencode" / "skills").glob("*/SKILL.md")
        }

        self.assertEqual(opencode_skills, claude_skills)

    def test_install_script_installs_default_profiles(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target_root = Path(temp_dir)
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/install_standards.py",
                    "--target",
                    str(target_root),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target_root / "docs" / "CODING_PRACTICES.md").exists())
            self.assertTrue((target_root / "AGENTS.md").exists())
            self.assertTrue((target_root / "opencode.json").exists())
            self.assertTrue(
                (target_root / ".opencode" / "skills" / "pre-commit" / "SKILL.md").exists()
            )

            install_manifest = target_root / ".engineering-standards" / "manifest.json"
            self.assertTrue(install_manifest.exists())
            manifest = json.loads(install_manifest.read_text(encoding="utf-8"))
            self.assertEqual(manifest["profiles"], ["core", "opencode"])

    def test_update_script_blocks_local_managed_edits_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target_root = Path(temp_dir)
            install = subprocess.run(
                [
                    sys.executable,
                    "scripts/install_standards.py",
                    "--target",
                    str(target_root),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(install.returncode, 0, install.stderr)

            managed_file = target_root / "AGENTS.md"
            managed_file.write_text("locally modified\n", encoding="utf-8")

            update = subprocess.run(
                [
                    sys.executable,
                    "scripts/update_standards.py",
                    "--target",
                    str(target_root),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(update.returncode, 1)
            self.assertIn("Local changes detected in managed files.", update.stderr)


if __name__ == "__main__":
    unittest.main()

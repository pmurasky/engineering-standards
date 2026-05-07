from __future__ import annotations

import subprocess
import sys
import unittest

try:
    from helpers import REPO_ROOT
except ModuleNotFoundError:
    from tests.enforcement_integration.helpers import REPO_ROOT


class CanonicalContractValidationScriptTests(unittest.TestCase):
    def run_script(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/validate_canonical_contracts.py", *args],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_validation_passes_for_repository_contracts(self) -> None:
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validated", result.stdout)

    def test_validation_fails_for_invalid_registry_fixture(self) -> None:
        result = self.run_script(
            "--registry",
            "tests/fixtures/invalid-contracts/invalid-registry.json",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("registry entry missing fields", result.stderr)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import subprocess
import sys
import unittest

try:
    from helpers import REPO_ROOT
except ModuleNotFoundError:
    from tests.enforcement_integration.helpers import REPO_ROOT


class ContractAdapterImpactIntegrationTests(unittest.TestCase):
    def run_script(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/report_contract_adapter_impact.py", *args],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_reports_warning_for_referencing_adapter(self) -> None:
        result = self.run_script("--changed-contract", "pre-commit.md")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Changed contracts: 1", result.stdout)
        self.assertIn("Impacted adapters:", result.stdout)
        self.assertIn(
            ".opencode/commands/pre-commit.md (references docs/archived-workflows/pre-commit.md)",
            result.stdout,
        )
        self.assertIn("::warning title=Contract adapter may need update::", result.stdout)

    def test_ignores_non_contract_inputs(self) -> None:
        result = self.run_script("--changed-contract", "README.md")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Changed contracts: 0", result.stdout)
        self.assertIn(
            "No canonical contract changes detected under docs/archived-workflows/*.md",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()

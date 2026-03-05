from __future__ import annotations

import subprocess
import unittest

from helpers import REPO_ROOT


class TokenUsageReportIntegrationTests(unittest.TestCase):
    def test_report_script_succeeds_for_reasonable_budget(self) -> None:
        result = subprocess.run(
            ["python3", "scripts/report-token-usage.py", "--max-tokens", "5000", "--fail-on-exceed"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("skill,tokens,status", result.stdout)
        self.assertIn(".claude/skills/pre-commit/SKILL.md", result.stdout)

    def test_report_script_fails_for_tiny_budget(self) -> None:
        result = subprocess.run(
            ["python3", "scripts/report-token-usage.py", "--max-tokens", "10", "--fail-on-exceed"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Exceeded token budget", result.stdout)


if __name__ == "__main__":
    unittest.main()

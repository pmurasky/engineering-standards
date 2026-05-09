from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from helpers import REPO_ROOT


class TokenUsageReportIntegrationTests(unittest.TestCase):
    """Legacy token usage report tests (preserved for backward compatibility)."""
    
    def test_legacy_report_script_succeeds_for_reasonable_budget(self) -> None:
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

    def test_legacy_report_script_fails_for_tiny_budget(self) -> None:
        result = subprocess.run(
            ["python3", "scripts/report-token-usage.py", "--max-tokens", "10", "--fail-on-exceed"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Exceeded token budget", result.stdout)


class MultiCategoryTokenReportTests(unittest.TestCase):
    """Skills 2.0 multi-category token reporting tests."""
    
    def test_multi_category_report_with_default_thresholds(self) -> None:
        result = subprocess.run(
            [
                "python3", "scripts/report-token-usage.py",
                "--always-on-threshold", "2000",
                "--skills-threshold", "1000", 
                "--commands-threshold", "800",
                "--contracts-threshold", "1200"
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("=== TOKEN USAGE REPORT ===", result.stdout)
        self.assertIn("=== CATEGORY TOTALS ===", result.stdout)
        self.assertIn("always-on:", result.stdout)
        self.assertIn("claude-skills:", result.stdout) 
        self.assertIn("opencode-commands:", result.stdout)
        self.assertIn("canonical-contracts:", result.stdout)
    
    def test_multi_category_json_output(self) -> None:
        result = subprocess.run(
            [
                "python3", "scripts/report-token-usage.py",
                "--json-output"
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        
        self.assertEqual(result.returncode, 0)
        
        try:
            data = json.loads(result.stdout)
            self.assertIn("categories", data)
            self.assertIn("summary", data)
            self.assertIn("timestamp", data)
            
            categories = data["categories"]
            self.assertIn("always-on", categories)
            self.assertIn("claude-skills", categories)
            self.assertIn("opencode-commands", categories)
            self.assertIn("canonical-contracts", categories)
            
            for category in categories.values():
                self.assertIn("total_tokens", category)
                self.assertIn("file_count", category)
                self.assertIn("threshold", category)
                self.assertIn("files", category)
                
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
    
    def test_threshold_exceedance_detection(self) -> None:
        result = subprocess.run(
            [
                "python3", "scripts/report-token-usage.py",
                "--always-on-threshold", "10",  # Unreasonably low
                "--fail-on-exceed"
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("=== THRESHOLD VIOLATIONS ===", result.stdout)
        self.assertIn("CLAUDE.md:", result.stdout)
    
    def test_baseline_capture_and_comparison(self) -> None:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            baseline_path = f.name
        
        try:
            # Capture baseline
            result = subprocess.run(
                ["python3", "scripts/report-token-usage.py", "--capture-baseline", baseline_path],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            
            self.assertEqual(result.returncode, 0)
            self.assertIn("Baseline captured", result.stdout)
            
            # Verify baseline file exists and has correct structure
            baseline_file = Path(baseline_path)
            self.assertTrue(baseline_file.exists())
            
            with open(baseline_file) as f:
                baseline_data = json.load(f)
            
            self.assertIn("timestamp", baseline_data)
            self.assertIn("version", baseline_data)
            self.assertIn("categories", baseline_data)
            
            categories = baseline_data["categories"]
            self.assertIn("always-on", categories)
            self.assertIn("claude-skills", categories)
            self.assertIn("opencode-commands", categories)
            self.assertIn("canonical-contracts", categories)
            
            # Compare against baseline
            result = subprocess.run(
                ["python3", "scripts/report-token-usage.py", "--compare-baseline", baseline_path],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            
            self.assertEqual(result.returncode, 0)
            
        finally:
            Path(baseline_path).unlink(missing_ok=True)
    
    def test_category_file_detection(self) -> None:
        result = subprocess.run(
            [
                "python3", "scripts/report-token-usage.py",
                "--json-output"
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        categories = data["categories"]
        
        # Check always-on files are detected
        always_on = categories["always-on"]
        self.assertGreater(always_on["file_count"], 0)
        self.assertIn("CLAUDE.md", str(always_on["files"]))
        
        # Check claude-skills files are detected  
        claude_skills = categories["claude-skills"]
        self.assertGreater(claude_skills["file_count"], 0)
        self.assertIn(".claude/skills/pre-commit/SKILL.md", str(claude_skills["files"]))
        
        # Check opencode-commands files are detected
        opencode_commands = categories["opencode-commands"]
        self.assertGreater(opencode_commands["file_count"], 0)
        self.assertIn(".opencode/commands/pre-commit.md", str(opencode_commands["files"]))
        
        # Check canonical contracts are detected
        canonical_contracts = categories["canonical-contracts"] 
        self.assertGreater(canonical_contracts["file_count"], 0)
        self.assertIn("docs/archived-workflows/pre-commit.md", str(canonical_contracts["files"]))


if __name__ == "__main__":
    unittest.main()

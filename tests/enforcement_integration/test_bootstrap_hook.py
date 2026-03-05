from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from helpers import REPO_ROOT, run_session_start


class SessionStartHookIntegrationTests(unittest.TestCase):
    def test_loads_bootstrap_context_from_project_file(self) -> None:
        project_dir = REPO_ROOT / "tests" / "fixtures" / "claude-project-with-bootstrap"

        output = run_session_start(project_dir)
        context = str(output["additional_context"])

        self.assertIn("Fixture Bootstrap", context)
        self.assertIn("docs/AI_AGENT_WORKFLOW.md", context)
        self.assertEqual(output["hookSpecificOutput"]["hookEventName"], "SessionStart")

    def test_uses_fallback_context_when_bootstrap_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = run_session_start(Path(temp_dir))
            context = str(output["additional_context"])

        self.assertIn("bootstrap is unavailable", context)
        self.assertIn("docs/PRE_COMMIT_CHECKLIST.md", context)


if __name__ == "__main__":
    unittest.main()

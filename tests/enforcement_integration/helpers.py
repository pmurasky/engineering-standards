from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SESSION_START_HOOK = REPO_ROOT / ".claude" / "hooks" / "session-start.sh"


def run_session_start(project_dir: Path) -> dict[str, object]:
    env = os.environ.copy()
    env["CLAUDE_PROJECT_DIR"] = str(project_dir)
    result = subprocess.run(
        ["bash", str(SESSION_START_HOOK)],
        check=True,
        capture_output=True,
        text=True,
        env=env,
        cwd=REPO_ROOT,
    )
    return json.loads(result.stdout)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_skill(skill_path: Path, required_phrases: list[str]) -> list[str]:
    content = read_text(skill_path)
    problems: list[str] = []
    if "<HARD-GATE>" not in content or "</HARD-GATE>" not in content:
        problems.append("missing hard-gate section")
    missing_phrases = [phrase for phrase in required_phrases if phrase not in content]
    if missing_phrases:
        problems.append(f"missing phrases: {', '.join(missing_phrases)}")
    return problems

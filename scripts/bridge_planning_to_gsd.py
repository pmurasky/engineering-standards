#!/usr/bin/env python3
"""
Bridge: planning-with-files → GSD v2

Reads planning files from .planning/ and creates/updates GSD milestones/slices/tasks.
This script provides a reusable way to sync planning content into the GSD database.

Usage:
    python bridge_planning_to_gsd.py [--dry-run] [--milestone M001]

Requirements:
    - Python 3.8+
    - GSD CLI installed and configured
    - .planning/ directory with phase files
    - .gsd/ directory with existing milestone structure
"""

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class Task:
    """Represents a task parsed from a planning file."""
    task_id: str
    title: str
    description: str
    estimate: str = "1h"
    files: List[str] = field(default_factory=list)
    verify: str = ""
    inputs: List[str] = field(default_factory=list)
    expected_output: List[str] = field(default_factory=list)


@dataclass
class Slice:
    """Represents a slice (phase) with its tasks."""
    slice_id: str
    title: str
    goal: str
    tasks: List[Task] = field(default_factory=list)
    risk: str = "medium"
    depends: List[str] = field(default_factory=list)
    demo: str = ""
    success_criteria: str = ""
    proof_level: str = "demo"
    integration_closure: str = ""
    observability_impact: str = ""


@dataclass
class Milestone:
    """Represents a milestone with its slices."""
    milestone_id: str
    title: str
    vision: str
    slices: List[Slice] = field(default_factory=list)


class PlanningParser:
    """Parses planning markdown files into structured data."""

    def __init__(self, planning_dir: Path):
        self.planning_dir = Path(planning_dir)

    def parse_plan_file(self, plan_file: Path) -> List[Task]:
        """Parse a plan markdown file and extract tasks."""
        content = plan_file.read_text()
        tasks = []

        # Find all task sections (### Task N: Title)
        task_pattern = r'###\s+Task\s+(\d+)\s*:\s*(.+?)\n\n\*\*Objective:\*\*\s*(.+?)\n\n\*\*Steps:\*\*(.+?)(?=\n\n\*\*Success Criteria:|\n\n---|\Z)'

        for match in re.finditer(task_pattern, content, re.DOTALL):
            task_num = match.group(1)
            title = match.group(2).strip()
            objective = match.group(3).strip()
            steps_text = match.group(4).strip()

            # Build description from objective + steps
            description = f"**Objective:** {objective}\n\n**Steps:**\n{steps_text}"

            # Extract files mentioned in steps
            files = self._extract_files(steps_text)

            # Extract verification from success criteria
            verify = self._extract_verification(content, match.end())

            task = Task(
                task_id=f"T{int(task_num):02d}",
                title=title,
                description=description,
                files=files,
                verify=verify,
                inputs=files,  # Inputs are typically the same as files
                expected_output=[f"Completed: {title}"]
            )
            tasks.append(task)

        return tasks

    def _extract_files(self, steps_text: str) -> List[str]:
        """Extract file paths mentioned in steps."""
        files = set()
        # Match backtick-quoted paths and explicit file mentions
        patterns = [
            r'`([^`]+\.(?:md|json|py|js|ts|sh|yml|yaml))`',
            r'(?:file|path|directory|folder)\s*:?\s*`?([^`\n]+\.(?:md|json|py|js|ts|sh|yml|yaml))`?',
        ]
        for pattern in patterns:
            for match in re.finditer(pattern, steps_text, re.IGNORECASE):
                files.add(match.group(1))
        return sorted(list(files)) if files else ["docs/"]

    def _extract_verification(self, content: str, after_pos: int) -> str:
        """Extract success criteria after a task section."""
        # Look for success criteria section after the task
        remaining = content[after_pos:after_pos + 500]
        match = re.search(r'\*\*Success Criteria:\*\*\s*(.+?)(?=\n\n---|\Z)', remaining, re.DOTALL)
        if match:
            criteria = match.group(1).strip()
            # Convert checklist items to verification steps
            lines = [line.strip('- []').strip() for line in criteria.split('\n') if line.strip().startswith('-')]
            return '\n'.join(f"- [ ] {line}" for line in lines)
        return "- [ ] Task completed successfully"

    def parse_phase_directory(self, phase_dir: Path) -> Slice:
        """Parse a phase directory and create a slice."""
        phase_name = phase_dir.name

        # Determine slice ID from directory name (e.g., 03-agent-skills-plan -> S03)
        match = re.match(r'(\d+)', phase_name)
        slice_num = match.group(1) if match else "01"
        slice_id = f"S{int(slice_num):02d}"

        # Find plan file
        plan_files = list(phase_dir.glob("*PLAN.md")) + list(phase_dir.glob("*plan.md"))
        context_files = list(phase_dir.glob("*CONTEXT.md")) + list(phase_dir.glob("*context.md"))
        research_files = list(phase_dir.glob("*RESEARCH.md")) + list(phase_dir.glob("*research.md"))

        # Read title from first heading
        title = "Execute Phase"
        goal = "Complete phase tasks"

        if plan_files:
            content = plan_files[0].read_text()
            title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
                # Extract goal from overview
                overview_match = re.search(r'## Overview\s*\n\n(.+?)(?=\n\n|\Z)', content, re.DOTALL)
                if overview_match:
                    goal = overview_match.group(1).strip()

            tasks = self.parse_plan_file(plan_files[0])
        elif context_files:
            content = context_files[0].read_text()
            title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
            tasks = [Task(
                task_id="T01",
                title="Gather context and requirements",
                description=content[:1000],
                files=[str(context_files[0])]
            )]
        elif research_files:
            content = research_files[0].read_text()
            title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
            tasks = [Task(
                task_id="T01",
                title="Research and document findings",
                description=content[:1000],
                files=[str(research_files[0])]
            )]
        else:
            tasks = []

        return Slice(
            slice_id=slice_id,
            title=title,
            goal=goal,
            tasks=tasks,
            demo=f"After this: {title} is complete"
        )

    def discover_phases(self) -> List[Slice]:
        """Discover all phase directories and parse them."""
        phases_dir = self.planning_dir / "phases"
        if not phases_dir.exists():
            print(f"No phases directory found at {phases_dir}")
            return []

        slices = []
        for phase_dir in sorted(phases_dir.iterdir()):
            if phase_dir.is_dir():
                slice_data = self.parse_phase_directory(phase_dir)
                slices.append(slice_data)
                print(f"  Parsed phase: {phase_dir.name} -> {slice_data.slice_id} ({len(slice_data.tasks)} tasks)")

        return slices


class GSDBridge:
    """Bridge to GSD v2 database and APIs."""

    def __init__(self, project_dir: Path):
        self.project_dir = Path(project_dir)
        self.gsd_dir = self.project_dir / ".gsd"
        self.db_path = self.gsd_dir / "gsd.db"

    def get_milestone_id(self, phase_prefix: str) -> Optional[str]:
        """Map phase prefix to milestone ID."""
        # Query the database for milestone mapping
        if not self.db_path.exists():
            return None

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, title FROM milestones WHERE status != 'closed'")
            milestones = cursor.fetchall()
            conn.close()

            # Simple heuristic: match by number or title
            for mid, title in milestones:
                if phase_prefix in title.lower() or phase_prefix.replace('-', ' ') in title.lower():
                    return mid

            # Return first active milestone as fallback
            if milestones:
                return milestones[0][0]
        except Exception as e:
            print(f"Error querying database: {e}")

        return None

    def list_milestones(self) -> List[Tuple[str, str]]:
        """List all active milestones."""
        if not self.db_path.exists():
            return []

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, title FROM milestones WHERE status != 'closed'")
            milestones = cursor.fetchall()
            conn.close()
            return milestones
        except Exception as e:
            print(f"Error querying database: {e}")
            return []

    def update_slice(self, milestone_id: str, slice_data: Slice, dry_run: bool = False) -> bool:
        """Update a slice with tasks using GSD MCP tools or direct DB writes."""
        print(f"\n  Updating {milestone_id}/{slice_data.slice_id}: {slice_data.title}")
        print(f"  Tasks: {len(slice_data.tasks)}")

        if dry_run:
            for task in slice_data.tasks:
                print(f"    - {task.task_id}: {task.title}")
            return True

        # Try using GSD CLI first
        try:
            # Build tasks array for gsd_plan_slice
            tasks_json = []
            for task in slice_data.tasks:
                tasks_json.append({
                    "taskId": task.task_id,
                    "title": task.title,
                    "description": task.description,
                    "estimate": task.estimate,
                    "files": task.files if task.files else ["docs/"],
                    "verify": task.verify,
                    "inputs": task.inputs if task.inputs else ["docs/"],
                    "expectedOutput": task.expected_output if task.expected_output else ["Task completed"]
                })

            # Use gsd CLI to update slice
            cmd = [
                "gsd", "plan-slice",
                "--milestone", milestone_id,
                "--slice", slice_data.slice_id,
                "--goal", slice_data.goal,
                "--tasks", json.dumps(tasks_json)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_dir)
            if result.returncode == 0:
                print(f"  ✓ Updated successfully")
                return True
            else:
                print(f"  ✗ CLI failed: {result.stderr}")
                # Fallback: direct DB update
                return self._update_slice_db(milestone_id, slice_data)

        except FileNotFoundError:
            print(f"  gsd CLI not found, falling back to direct DB update")
            return self._update_slice_db(milestone_id, slice_data)
        except Exception as e:
            print(f"  ✗ Error: {e}")
            return False

    def _update_slice_db(self, milestone_id: str, slice_data: Slice) -> bool:
        """Fallback: Update slice directly in SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Update slice record
            cursor.execute("""
                UPDATE slices SET
                    title = ?,
                    goal = ?,
                    task_count = ?,
                    updated_at = datetime('now')
                WHERE milestone_id = ? AND id = ?
            """, (slice_data.title, slice_data.goal, len(slice_data.tasks), milestone_id, slice_data.slice_id))

            # Delete existing tasks for this slice
            cursor.execute("""
                DELETE FROM tasks WHERE milestone_id = ? AND slice_id = ?
            """, (milestone_id, slice_data.slice_id))

            # Insert new tasks
            for task in slice_data.tasks:
                cursor.execute("""
                    INSERT INTO tasks (milestone_id, slice_id, id, title, description, status, estimate, verify, files, inputs, expected_output)
                    VALUES (?, ?, ?, ?, ?, 'pending', ?, ?, ?, ?, ?)
                """, (
                    milestone_id, slice_data.slice_id, task.task_id, task.title, task.description,
                    task.estimate, task.verify,
                    json.dumps(task.files if task.files else ["docs/"]),
                    json.dumps(task.inputs if task.inputs else ["docs/"]),
                    json.dumps(task.expected_output if task.expected_output else ["Task completed"])
                ))

            conn.commit()
            conn.close()
            print(f"  ✓ Updated via direct DB write")
            return True

        except Exception as e:
            print(f"  ✗ DB update failed: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Bridge planning-with-files to GSD v2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Bridge all phases to GSD
  %(prog)s --dry-run               # Show what would be done
  %(prog)s --milestone M001        # Only bridge M001
  %(prog)s --phase 03              # Only bridge phase 03
        """
    )
    parser.add_argument("--dry-run", action="store_true", help="Show changes without applying")
    parser.add_argument("--milestone", help="Only process specific milestone (e.g., M001)")
    parser.add_argument("--phase", help="Only process specific phase (e.g., 03)")
    parser.add_argument("--project-dir", default=".", help="Project directory (default: current)")
    parser.add_argument("--planning-dir", default=".planning", help="Planning directory (default: .planning)")

    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()
    planning_dir = project_dir / args.planning_dir

    print(f"Planning → GSD Bridge")
    print(f"=" * 50)
    print(f"Project: {project_dir}")
    print(f"Planning: {planning_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()

    # Initialize parser and bridge
    parser = PlanningParser(planning_dir)
    bridge = GSDBridge(project_dir)

    # List active milestones
    print("Active milestones:")
    milestones = bridge.list_milestones()
    if milestones:
        for mid, title in milestones:
            print(f"  {mid}: {title}")
    else:
        print("  No active milestones found")
    print()

    # Discover phases
    print("Discovering phases...")
    slices = parser.discover_phases()
    if not slices:
        print("No phases found!")
        sys.exit(1)

    print(f"\nFound {len(slices)} phase(s)")
    print()

    # Map and update
    print("Bridging to GSD...")
    print("=" * 50)

    # Simple mapping: phase number → milestone
    # In practice, you'd want a more sophisticated mapping
    phase_to_milestone = {
        "01": "M001", "02": "M001", "03": "M001",  # Agent skills
        "09": "M009",  # Distribution
    }

    success_count = 0
    for slice_data in slices:
        # Filter by phase if specified
        if args.phase and not slice_data.slice_id.endswith(args.phase):
            continue

        # Determine milestone
        phase_num = slice_data.slice_id.replace("S", "")
        milestone_id = phase_to_milestone.get(phase_num)

        if not milestone_id:
            # Try to find matching milestone
            milestone_id = bridge.get_milestone_id(phase_num)

        if not milestone_id:
            print(f"  ⚠ No milestone mapping for {slice_data.slice_id}, skipping")
            continue

        # Filter by milestone if specified
        if args.milestone and milestone_id != args.milestone:
            continue

        # Update slice
        if bridge.update_slice(milestone_id, slice_data, dry_run=args.dry_run):
            success_count += 1

    print()
    print("=" * 50)
    print(f"Bridge complete: {success_count}/{len(slices)} slices updated")

    if args.dry_run:
        print("\nThis was a dry run. Use without --dry-run to apply changes.")


if __name__ == "__main__":
    main()

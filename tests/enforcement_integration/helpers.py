from __future__ import annotations

import json
import os
import re
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
    """Legacy phrase-based validation (preserved for backward compatibility)."""
    content = read_text(skill_path)
    problems: list[str] = []
    if "<HARD-GATE>" not in content or "</HARD-GATE>" not in content:
        problems.append("missing hard-gate section")
    missing_phrases = [phrase for phrase in required_phrases if phrase not in content]
    if missing_phrases:
        problems.append(f"missing phrases: {', '.join(missing_phrases)}")
    return problems


def parse_canonical_contract(contract_path: Path) -> dict[str, list[str]]:
    """Parse canonical contract to extract requirements."""
    if not contract_path.exists():
        return {}
    
    content = read_text(contract_path)
    requirements = {
        "hard_gates": [],
        "status_vocabulary": [],
        "required_references": []
    }
    
    # Extract hard gates from ## Hard Gates section
    hard_gates_match = re.search(r'## Hard Gates\s*\n(.*?)(?=\n##|\nz)', content, re.DOTALL)
    if hard_gates_match:
        hard_gates_section = hard_gates_match.group(1)
        # Find MUST requirements
        must_gates = re.findall(r'\*\*(.*?MUST.*?)\*\*', hard_gates_section)
        requirements["hard_gates"] = must_gates
    
    # Extract status vocabulary
    status_match = re.search(r'## Status Vocabulary\s*\n(.*?)(?=\n##|\nz)', content, re.DOTALL)
    if status_match:
        status_section = status_match.group(1)
        # Find status indicators
        status_indicators = re.findall(r'- `([^`]+)`:', status_section)
        requirements["status_vocabulary"] = status_indicators
    
    # Extract required references
    ref_match = re.search(r'## Required References\s*\n(.*?)(?=\n##|\nz)', content, re.DOTALL)
    if ref_match:
        ref_section = ref_match.group(1)
        # Find markdown links and file paths
        refs = re.findall(r'- `([^`]+\.md)`', ref_section)
        requirements["required_references"] = refs
    
    return requirements


def validate_contract_references(adapter_path: Path) -> list[str]:
    """Verify adapter references valid canonical contract."""
    problems: list[str] = []
    content = read_text(adapter_path)
    
    # Check for canonical contract reference
    contract_refs = re.findall(r'`docs/workflows/([^`]+\.md)`', content)
    if not contract_refs:
        problems.append("missing canonical contract reference (docs/workflows/*.md)")
        return problems
    
    # Validate referenced contract files exist
    for contract_ref in contract_refs:
        contract_path = REPO_ROOT / "docs" / "workflows" / contract_ref
        if not contract_path.exists():
            problems.append(f"referenced contract does not exist: docs/workflows/{contract_ref}")
    
    return problems


def validate_hard_gate_semantics(canonical_contract: Path, adapter_path: Path) -> list[str]:
    """Verify adapter implements canonical hard gates."""
    problems: list[str] = []
    
    if not canonical_contract.exists():
        problems.append(f"canonical contract not found: {canonical_contract}")
        return problems
    
    contract_reqs = parse_canonical_contract(canonical_contract)
    adapter_content = read_text(adapter_path)
    
    # Check hard-gate section exists
    if "<HARD-GATE>" not in adapter_content or "</HARD-GATE>" not in adapter_content:
        problems.append("missing hard-gate section")
        return problems
    
    # Extract adapter hard-gate content
    hard_gate_match = re.search(r'<HARD-GATE>(.*?)</HARD-GATE>', adapter_content, re.DOTALL)
    if not hard_gate_match:
        problems.append("malformed hard-gate section")
        return problems
    
    hard_gate_content = hard_gate_match.group(1)
    
    # Check key hard-gate semantics from canonical contract
    expected_semantics = [
        "Unit tests MUST pass",
        "Build MUST succeed", 
        "Lint MUST pass",
        "NOT READY",
        "NOT CONFIGURED"
    ]
    
    for semantic in expected_semantics:
        if semantic not in hard_gate_content and semantic not in adapter_content:
            problems.append(f"missing hard-gate semantic: {semantic}")
    
    return problems


def validate_status_vocabulary(canonical_contract: Path, adapter_path: Path) -> list[str]:
    """Verify adapter uses canonical status vocabulary."""
    problems: list[str] = []
    
    if not canonical_contract.exists():
        problems.append(f"canonical contract not found: {canonical_contract}")
        return problems
    
    contract_reqs = parse_canonical_contract(canonical_contract)
    adapter_content = read_text(adapter_path)
    
    # Extract hard-gate and output format sections for focused validation
    hard_gate_match = re.search(r'<HARD-GATE>(.*?)</HARD-GATE>', adapter_content, re.DOTALL)
    output_format_match = re.search(r'Output.*?format[:\s]+(.*?)(?=\n\n|\n[A-Z]|\nz)', adapter_content, re.DOTALL | re.IGNORECASE)
    
    relevant_sections = ""
    if hard_gate_match:
        relevant_sections += hard_gate_match.group(1)
    if output_format_match:
        relevant_sections += output_format_match.group(1)
    
    # If no relevant sections found, check whole document (fallback)
    if not relevant_sections.strip():
        relevant_sections = adapter_content
    
    # Check for canonical status vocabulary in relevant sections
    required_status = ["READY", "NOT READY", "NOT CONFIGURED"]
    for status in required_status:
        if (f"`{status}`" not in relevant_sections and 
            f"'{status}'" not in relevant_sections and 
            status not in relevant_sections):
            problems.append(f"missing required status vocabulary: {status}")
    
    return problems


def validate_workflow_parity(workflow_name: str) -> list[str]:
    """Compare Claude skill vs OpenCode command for same workflow."""
    problems: list[str] = []
    
    # Paths for adapters
    claude_skill = REPO_ROOT / ".claude" / "skills" / workflow_name / "SKILL.md"
    opencode_command = REPO_ROOT / ".opencode" / "commands" / f"{workflow_name}.md"
    canonical_contract = REPO_ROOT / "docs" / "workflows" / f"{workflow_name}.md"
    
    # Check if both adapters exist
    if not claude_skill.exists():
        problems.append(f"Claude skill missing: {claude_skill}")
    if not opencode_command.exists():
        problems.append(f"OpenCode command missing: {opencode_command}")
    
    if problems:  # Can't compare if adapters don't exist
        return problems
    
    # Validate both adapters against canonical contract
    if canonical_contract.exists():
        claude_problems = validate_hard_gate_semantics(canonical_contract, claude_skill)
        opencode_problems = validate_hard_gate_semantics(canonical_contract, opencode_command)
        
        for problem in claude_problems:
            problems.append(f"Claude adapter: {problem}")
        for problem in opencode_problems:
            problems.append(f"OpenCode adapter: {problem}")
            
        # Check both use same status vocabulary
        claude_status_problems = validate_status_vocabulary(canonical_contract, claude_skill)
        opencode_status_problems = validate_status_vocabulary(canonical_contract, opencode_command)
        
        for problem in claude_status_problems:
            problems.append(f"Claude status vocabulary: {problem}")
        for problem in opencode_status_problems:
            problems.append(f"OpenCode status vocabulary: {problem}")
    
    return problems

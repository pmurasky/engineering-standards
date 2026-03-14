#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]

# Default thresholds per category
DEFAULT_THRESHOLDS = {
    "always-on": 2000,
    "claude-skills": 1000,
    "opencode-commands": 800,
    "canonical-contracts": 1200,
}

# File patterns for each category
CATEGORY_PATTERNS = {
    "always-on": [
        "CLAUDE.md",
        ".claude/rules/micro-commit-workflow.md",
        ".claude/rules/testing.md",
        ".claude/rules/code-review.md",
        ".claude/rules/refactoring.md",
    ],
    "claude-skills": [".claude/skills/*/SKILL.md"],
    "opencode-commands": [".opencode/commands/*.md"],
    "canonical-contracts": ["docs/workflows/*.md"],
}


def estimate_tokens(text: str) -> int:
    return max(1, math.ceil(len(text) / 4))


def collect_category_files(category: str) -> List[Path]:
    patterns = CATEGORY_PATTERNS[category]
    files = []
    
    for pattern in patterns:
        if "*" in pattern:
            files.extend(REPO_ROOT.glob(pattern))
        else:
            file_path = REPO_ROOT / pattern
            if file_path.exists():
                files.append(file_path)
    
    return sorted(files)


def collect_skill_files() -> List[Path]:
    """Legacy function for backward compatibility."""
    return collect_category_files("claude-skills")


def measure_category(category: str, threshold: int) -> Tuple[Dict, List]:
    files = collect_category_files(category)
    category_data = {"files": {}, "total": 0, "threshold": threshold}
    exceeded = []
    
    for file_path in files:
        if not file_path.exists():
            continue
            
        text = file_path.read_text(encoding="utf-8")
        tokens = estimate_tokens(text)
        relative_path = str(file_path.relative_to(REPO_ROOT))
        
        category_data["files"][relative_path] = tokens
        category_data["total"] += tokens
        
        if tokens > threshold:
            exceeded.append((relative_path, tokens, threshold))
    
    return category_data, exceeded


def capture_baseline(baseline_path: Path) -> Dict:
    baseline = {
        "timestamp": datetime.now().isoformat(),
        "version": "Skills 2.0 token governance",
        "categories": {}
    }
    
    for category, threshold in DEFAULT_THRESHOLDS.items():
        category_data, _ = measure_category(category, threshold)
        baseline["categories"][category] = category_data
    
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    with open(baseline_path, "w") as f:
        json.dump(baseline, f, indent=2)
    
    return baseline


def compare_baseline(baseline_path: Path, current_data: Dict) -> List[str]:
    if not baseline_path.exists():
        return [f"Baseline file not found: {baseline_path}"]
    
    with open(baseline_path) as f:
        baseline = json.load(f)
    
    warnings = []
    
    for category, current_cat in current_data.items():
        if category not in baseline["categories"]:
            warnings.append(f"New category: {category}")
            continue
            
        baseline_cat = baseline["categories"][category]
        current_total = current_cat["total"]
        baseline_total = baseline_cat["total"]
        
        if current_total > baseline_total * 1.1:  # 10% increase threshold
            increase = current_total - baseline_total
            pct = (increase / baseline_total) * 100
            warnings.append(f"{category}: {increase:+} tokens ({pct:+.1f}%) vs baseline")
    
    return warnings


def report_legacy_format(args) -> int:
    """Legacy CLI compatibility for Claude skills only."""
    skill_files = collect_skill_files()
    if not skill_files:
        print("No skill files found under .claude/skills")
        return 0

    exceeded = []
    print("skill,tokens,status")
    for skill_file in skill_files:
        text = skill_file.read_text(encoding="utf-8")
        tokens = estimate_tokens(text)
        status = "OK"
        if tokens > args.max_tokens:
            status = "EXCEEDS"
            exceeded.append((skill_file, tokens))
        relative = skill_file.relative_to(REPO_ROOT)
        print(f"{relative},{tokens},{status}")

    if exceeded:
        print("\nExceeded token budget:")
        for skill_file, tokens in exceeded:
            relative = skill_file.relative_to(REPO_ROOT)
            print(f"- {relative}: {tokens} > {args.max_tokens}")

    if args.fail_on_exceed and exceeded:
        return 1
    return 0


def report_multi_category(args) -> int:
    """Multi-category token reporting with threshold validation."""
    thresholds = {
        "always-on": args.always_on_threshold,
        "claude-skills": args.skills_threshold,
        "opencode-commands": args.commands_threshold,
        "canonical-contracts": args.contracts_threshold,
    }
    
    all_data = {}
    all_exceeded = []
    
    if args.json_output:
        # JSON format
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "categories": {},
            "summary": {}
        }
        
        for category, threshold in thresholds.items():
            category_data, exceeded = measure_category(category, threshold)
            all_data[category] = category_data
            all_exceeded.extend(exceeded)
            
            report_data["categories"][category] = {
                "total_tokens": category_data["total"],
                "file_count": len(category_data["files"]),
                "threshold": threshold,
                "files": category_data["files"]
            }
        
        report_data["summary"]["total_exceeded"] = len(all_exceeded)
        report_data["summary"]["total_tokens"] = sum(data["total"] for data in all_data.values())
        
        print(json.dumps(report_data, indent=2))
        
    else:
        # Human-readable format
        print("=== TOKEN USAGE REPORT ===")
        print("category,file,tokens,threshold,status")
        
        for category, threshold in thresholds.items():
            category_data, exceeded = measure_category(category, threshold)
            all_data[category] = category_data
            all_exceeded.extend(exceeded)
            
            for file_path, tokens in category_data["files"].items():
                status = "EXCEEDS" if tokens > threshold else "OK"
                print(f"{category},{file_path},{tokens},{threshold},{status}")
        
        print("\n=== CATEGORY TOTALS ===")
        for category, data in all_data.items():
            threshold = thresholds[category]
            total = data["total"]
            count = len(data["files"])
            pct = (total / threshold) * 100 if threshold > 0 else 0
            print(f"{category}: {total}/{threshold} tokens ({pct:.1f}%) - {count} files")
        
        if all_exceeded:
            print("\n=== THRESHOLD VIOLATIONS ===")
            for file_path, tokens, threshold in all_exceeded:
                excess = tokens - threshold
                print(f"- {file_path}: {tokens} > {threshold} (+{excess})")
    
    # Baseline comparison
    if args.compare_baseline:
        baseline_warnings = compare_baseline(Path(args.compare_baseline), all_data)
        if baseline_warnings:
            print("\n=== BASELINE COMPARISON ===")
            for warning in baseline_warnings:
                print(f"WARNING: {warning}")
    
    # Return non-zero if thresholds exceeded and fail-on-exceed is set
    if args.fail_on_exceed and all_exceeded:
        return 1
    
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report token usage across Skills 2.0 file categories."
    )
    
    # Legacy compatibility
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1000,
        help="Maximum allowed tokens per Claude skill (legacy mode)."
    )
    
    # Multi-category thresholds
    parser.add_argument(
        "--always-on-threshold",
        type=int,
        default=DEFAULT_THRESHOLDS["always-on"],
        help=f"Threshold for always-on files (default: {DEFAULT_THRESHOLDS['always-on']})."
    )
    parser.add_argument(
        "--skills-threshold", 
        type=int,
        default=DEFAULT_THRESHOLDS["claude-skills"],
        help=f"Threshold for Claude skills (default: {DEFAULT_THRESHOLDS['claude-skills']})."
    )
    parser.add_argument(
        "--commands-threshold",
        type=int,
        default=DEFAULT_THRESHOLDS["opencode-commands"], 
        help=f"Threshold for OpenCode commands (default: {DEFAULT_THRESHOLDS['opencode-commands']})."
    )
    parser.add_argument(
        "--contracts-threshold",
        type=int,
        default=DEFAULT_THRESHOLDS["canonical-contracts"],
        help=f"Threshold for canonical contracts (default: {DEFAULT_THRESHOLDS['canonical-contracts']})."
    )
    
    # Output and baseline options
    parser.add_argument(
        "--fail-on-exceed",
        action="store_true",
        help="Exit non-zero when any file exceeds its threshold."
    )
    parser.add_argument(
        "--json-output",
        action="store_true",
        help="Output in JSON format for machine processing."
    )
    parser.add_argument(
        "--capture-baseline",
        help="Capture current measurements to baseline file."
    )
    parser.add_argument(
        "--compare-baseline",
        help="Compare current measurements against baseline file."
    )
    
    args = parser.parse_args()
    
    # Baseline capture mode
    if args.capture_baseline:
        baseline = capture_baseline(Path(args.capture_baseline))
        total_tokens = sum(cat["total"] for cat in baseline["categories"].values())
        print(f"Baseline captured: {total_tokens} tokens across {len(baseline['categories'])} categories")
        return 0
    
    # Determine if using legacy or multi-category mode
    is_legacy_mode = (
        args.always_on_threshold == DEFAULT_THRESHOLDS["always-on"] and
        args.skills_threshold == DEFAULT_THRESHOLDS["claude-skills"] and  
        args.commands_threshold == DEFAULT_THRESHOLDS["opencode-commands"] and
        args.contracts_threshold == DEFAULT_THRESHOLDS["canonical-contracts"] and
        not args.json_output and
        not args.compare_baseline
    )
    
    # Check if user explicitly used only legacy arguments
    used_legacy_only = (
        "--max-tokens" in sys.argv or 
        len(sys.argv) == 1  # No arguments at all
    )
    
    used_multicategory = (
        "--always-on-threshold" in sys.argv or
        "--skills-threshold" in sys.argv or
        "--commands-threshold" in sys.argv or  
        "--contracts-threshold" in sys.argv or
        "--json-output" in sys.argv or
        "--capture-baseline" in sys.argv or
        "--compare-baseline" in sys.argv
    )
    
    if used_legacy_only and not used_multicategory:
        # Legacy compatibility mode
        return report_legacy_format(args)
    else:
        # Multi-category mode
        return report_multi_category(args)


if __name__ == "__main__":
    sys.exit(main())

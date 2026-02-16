# Team-Tunable Defaults

Use this file as the active quality profile for the team.

## Default Thresholds

- `line_coverage_min`: 80%
- `critical_path_coverage_target`: 100% (where practical)
- `method_length_soft_limit`: 15 lines
- `class_size_soft_limit`: 300 lines
- `cyclomatic_complexity_soft_limit`: 10 per method
- `max_private_methods_guideline`: 2 per class

## Tuning Rules

- These values are defaults, not universal absolutes.
- Teams may tune thresholds based on domain risk, legacy constraints, and delivery stage.
- Any override should include rationale and scope (repo-wide, module, or temporary).

## Override Template

- `key`:
- `new_value`:
- `scope`:
- `rationale`:
- `expiry_or_review_date`:

## Agent Behavior

- If overrides are present, use them as the source of truth.
- If no overrides are defined, enforce defaults.
- If thresholds are ambiguous, ask for clarification and proceed with defaults meanwhile.

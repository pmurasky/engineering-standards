#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
BOOTSTRAP_FILE="$PROJECT_DIR/docs/AGENT_BOOTSTRAP.md"

fallback_context() {
  cat <<'EOF'
Engineering standards bootstrap is unavailable.

Load these references before implementing code changes:
- AGENTS.md
- docs/AI_AGENT_WORKFLOW.md
- docs/PRE_COMMIT_CHECKLIST.md
- docs/CODING_PRACTICES.md
EOF
}

if [ -f "$BOOTSTRAP_FILE" ]; then
  context="$(cat "$BOOTSTRAP_FILE")"
else
  context="$(fallback_context)"
fi

escape_json() {
  python3 -c 'import json, sys; print(json.dumps(sys.stdin.read()), end="")'
}

escaped_context="$(printf '%s' "$context" | escape_json)"

cat <<EOF
{
  "additional_context": $escaped_context,
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": $escaped_context
  }
}
EOF

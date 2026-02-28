#!/usr/bin/env bash
set -euo pipefail

INPUT_JSON="$(cat)"

IS_BLOCKED="$(printf '%s' "$INPUT_JSON" | python3 -c 'import json, re, sys
try:
    payload = json.load(sys.stdin)
except Exception:
    print(0)
    raise SystemExit(0)

command = payload.get("tool_input", {}).get("command", "")
pattern = re.compile(r"(?:^|[;&|\s])rm\s+-[\w-]*r[\w-]*f[\w-]*\s+(?:/|~|\.|\$PWD)(?:$|[\s;&|/])")
print(1 if pattern.search(command) else 0)
')"

if [ "$IS_BLOCKED" = "1" ]; then
  cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Blocked by conservative policy: destructive rm -rf target"
  }
}
EOF
fi

exit 0

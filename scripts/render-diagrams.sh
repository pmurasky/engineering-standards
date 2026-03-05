#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
DIAGRAM_DIR="${REPO_ROOT}/docs/diagrams"

if ! command -v dot >/dev/null 2>&1; then
  echo "Error: GraphViz 'dot' command not found." >&2
  echo "Install GraphViz, then re-run this script." >&2
  exit 1
fi

shopt -s nullglob
dot_files=("${DIAGRAM_DIR}"/*.dot)

if [ ${#dot_files[@]} -eq 0 ]; then
  echo "No DOT files found in ${DIAGRAM_DIR}"
  exit 0
fi

for dot_file in "${dot_files[@]}"; do
  svg_file="${dot_file%.dot}.svg"
  dot -Tsvg "${dot_file}" -o "${svg_file}"
  echo "Rendered ${svg_file}"
done

echo "Diagram rendering complete."

---
estimated_steps: 1
estimated_files: 3
skills_used: []
---

# T01: Define Supported Consumer Installation Modes

Identify every realistic way a downstream project can consume engineering-standards (git submodule, sparse-checkout, script-based copy, npm install, manual copy). For each mode, document: installation steps, update mechanism, tooling requirements, tradeoffs, and which consumer types (CI-only, developer workstation, agent-only) it suits. Write an ADR capturing the recommended mode with alternatives considered. Include support tiers: Recommended (first-class, documented, tested), Advanced (supported but not hand-held), Legacy (documented, not maintained).

## Inputs

- `Existing README install section`
- `Current .opencode/, .claude/, scripts/ structure`
- `M010 plugin context for comparison`

## Expected Output

- `docs/adr/ADR-XXX-distribution-modes.md with Recommended/Advanced/Legacy tiers`
- `docs/distribution/installation-modes.md listing all modes with tradeoffs`

## Verification

ADR file exists with status:Accepted; installation-modes.md lists ≥2 modes with tradeoffs; README references the canonical mode.

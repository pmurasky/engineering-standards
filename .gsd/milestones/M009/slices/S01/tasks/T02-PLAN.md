---
estimated_steps: 11
estimated_files: 3
skills_used: []
---

# T02: Design One-Command Init Workflow

Specify the bootstrap command that installs standards into a downstream repo with minimal manual work.

Steps:
1. Define command surface, expected arguments, and target repo assumptions.
2. Decide which files are copied, generated, or linked during init.
3. Define behavior for empty repo vs existing repo.
4. Define idempotency rules and safe re-run behavior.
5. Define conflict handling for existing AGENTS.md, opencode.json, .opencode/, and .claude/ content.

Success Criteria:
- Init command contract is explicit
- Existing-project merge behavior is defined
- Idempotency and conflict rules are documented

## Inputs

- `.planning/phases/09-standards-distribution-opencode-alignment/09-PLAN.md`

## Expected Output

- `Init workflow specification document`

## Verification

Init workflow documented with command contract and conflict handling

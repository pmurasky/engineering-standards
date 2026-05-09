---
estimated_steps: 1
estimated_files: 2
skills_used: []
---

# T01: Inventory Standards Documents for Resource Registration

Enumerate every file in docs/ that should be exposed as a plugin resource. For each file, determine: (1) whether it should be exposed as a named resource or glob-included, (2) what the consumer-facing resource identifier should be (e.g. `engineering-standards/CODING_PRACTICES`), (3) whether any docs/ files should be excluded (drafts, templates that aren't consumer-facing). Produce a resource manifest inventory as a markdown table.

## Inputs

- `ls docs/ recursive output`
- `S01 research doc resource loading section`
- `S02 manifest file`

## Expected Output

- `docs/resource-inventory.md with table of all docs/ files, their resource IDs, and include/exclude decisions`

## Verification

docs/resource-inventory.md exists; all docs/ files accounted for; each file has a resource ID or an explicit exclusion reason.

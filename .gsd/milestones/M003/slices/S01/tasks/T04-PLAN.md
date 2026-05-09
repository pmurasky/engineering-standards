---
estimated_steps: 1
estimated_files: 2
skills_used: []
---

# T04: Add dependabot.yml and SECURITY.md

Add .github/dependabot.yml to auto-update GitHub Actions versions (fixes CODEOWNERS reference to missing file). Add SECURITY.md with minimal security policy (vulnerability reporting email/process), fixing the second CODEOWNERS broken reference.

## Inputs

- `.github/CODEOWNERS`

## Expected Output

- `.github/dependabot.yml`
- `SECURITY.md`

## Verification

cat .github/dependabot.yml shows valid config. cat SECURITY.md has reporting instructions. .github/CODEOWNERS references no longer broken.

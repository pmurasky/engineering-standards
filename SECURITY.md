# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it by opening a private security advisory via GitHub:

1. Go to **Security → Advisories → New draft security advisory**
2. Describe the vulnerability, affected versions, and reproduction steps
3. Submit the draft; the maintainers will respond within 7 days

For sensitive issues that cannot be reported via GitHub, email the maintainer directly (see repository owner profile).

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |
| < latest | :x:                |

## Security Practices

- No hardcoded secrets or credentials in source code
- Dependencies are monitored via Dependabot
- CI/CD workflows use least-privilege permissions

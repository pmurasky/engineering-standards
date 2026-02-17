---
description: Next.js framework standards for App Router projects
globs: "**/{app,pages,src/app,src/pages}/**/*.{ts,tsx,js,jsx}"
---

# Next.js Standards

When working with Next.js app routes, pages, layouts, route handlers, and framework code, follow `docs/NEXTJS_STANDARDS.md`.

Focus on:
- Server Components by default; minimal `"use client"`
- Correct server-side auth, validation, and data boundaries
- Intentional caching and revalidation strategy
- Route handler input validation and stable error responses
- Performance, accessibility, and observability requirements

For TypeScript language rules, also apply `docs/TYPESCRIPT_STANDARDS.md`.


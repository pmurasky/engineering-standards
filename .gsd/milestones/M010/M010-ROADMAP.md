# M010: OpenCode Plugin Packaging

**Vision:** Transform this project into an installable OpenCode plugin exposing standards docs, skills, and workflows to consuming repos.

## Success Criteria

- Plugin manifest is valid and accepted by OpenCode
- Standards docs accessible as plugin resources
- Skills load correctly in consuming projects without manual copying
- Installation documentation complete and accurate
- Existing enforcement tests remain green

## Slices

- [ ] **S01: Research OpenCode Plugin Architecture** `risk:Low` `depends:[]`
  > After this: Research doc exists at docs/research/opencode-plugin-architecture.md covering manifest format, directory structure, skill/agent/command discovery, resource loading, and installation mechanism.

- [ ] **S02: Create Plugin Manifest and Structure** `risk:Low` `depends:[S01]`
  > After this: opencode.json or equivalent manifest file exists and validates against the OpenCode plugin schema; directory structure matches plugin conventions.

- [ ] **S03: Package Standards Documents as Plugin Resources** `risk:Medium` `depends:[S02]`
  > After this: At least one standards doc (e.g. CODING_PRACTICES.md) is accessible via the plugin resource API in a consuming project.

- [ ] **S04: Expose Skills via Plugin** `risk:Medium` `depends:[S02]`
  > After this: At least one skill (e.g. code-quality) is available in a consuming project without manual file copying after plugin install.

- [ ] **S05: Create Installation and Usage Documentation** `risk:Low` `depends:[S03,S04]`
  > After this: New developer can follow README to install plugin and access a skill and a standards doc within 5 minutes.

## Boundary Map

Not provided.

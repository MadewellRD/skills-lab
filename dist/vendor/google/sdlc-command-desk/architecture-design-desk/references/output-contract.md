# Output Contract

## Default artifact wrapper

When creating a downloadable design artifact, use:

```markdown
# [Artifact title]

## How to use this file

Use this architecture artifact as source material for planning, security review, verification, and implementation handoff. Resolve blocking assumptions and open questions before implementation.

## Artifact

[Design artifact]

## Source facts used

- [Source fact]

## Unverified assumptions

- [Assumption or `None`]
```

## Artifact modes

- `architecture-design.md` for solution or system design.
- `adr-<topic>.md` for a single decision record.
- `interface-contract-<name>.md` for APIs, schemas, events, or module contracts.
- `migration-plan-<topic>.md` for phased changes.
- `architecture-diagnostic.md` when required inputs or connectors are missing.

## Quality requirements

Every artifact must explicitly mark:

- facts from sources;
- design judgments;
- assumptions;
- risks;
- open questions;
- downstream handoff notes.

# Output Contract

## Default Markdown wrapper

For downloadable artifacts, use:

```markdown
# <artifact title>

## How to use this file

<One paragraph explaining who should use it and what to do next.>

## Source facts

<Grounding sources, refs, file paths, issue/PR numbers, and unverified assumptions.>

## Artifact

<The report, map, plan, index, or handoff note.>
```

## Required source facts

Include source facts unless the user explicitly requests a draft only:

- Repositories and refs.
- Relevant docs and sections.
- Issues, PRs, commits, and tests.
- Known missing sources.
- Unverified assumptions.

## File names

Use descriptive slugs:

- `proof-map-<topic>.md`
- `claim-map-<topic>.md`
- `doc-code-consistency-<topic>.md`
- `knowledge-index-<project>.md`
- `audit-evidence-<scope>.md`
- `docs-handoff-<scope>.md`
- `connector-diagnostic.md`

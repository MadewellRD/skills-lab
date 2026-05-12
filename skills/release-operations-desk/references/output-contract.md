# Output Contract

Use Markdown for all release artifacts.

## Artifact types

- `release-readiness-report.md`
- `release-notes.md`
- `version-tag-plan.md`
- `rollback-plan.md`
- `post-release-verification-plan.md`
- `release-handoff-notes.md`
- `connector-diagnostic.md`

## Required sections

Every release artifact must include:

- title
- scope or release identity
- source facts
- assumptions and unknowns
- risks or blockers
- downstream handoff notes when relevant

When the artifact will be pasted into another agent, wrap it with:

```markdown
# <artifact title>

## How to use this file

Paste the relevant handoff section into the target execution agent. Keep halt conditions and evidence requirements intact.

## Artifact

<content>
```

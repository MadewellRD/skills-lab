# Evidence Blocks and Source Notes

Every generated implementation handoff must be traceable to the facts used to produce it.

## Default behavior

If the source facts are short and useful to the implementation agent, include them at the end of the prompt file under `## Source facts used`.

If the prompt must remain clean for direct agent execution, create a companion file named `<prompt-slug>-sources.md` and link it in the chat response.

## Inline source facts format

```markdown
## Source facts used

- Mode: connector-grounded | user-facts-only | mixed | diagnostic
- GitHub repo: <owner/name or unavailable>
- Base branch: <branch or unverified>
- Baseline commit: <sha or unverified>
- Target branch/PR: <branch/pr or n/a>
- Issue/project source: <issue id or unavailable>
- Canonical docs used: <docs or n/a>
- Communication sources used: <messages/threads or n/a>
- Uploaded exemplars used: <canonical exemplar filenames>
- Unverified assumptions: <none or list>
```

## Companion source-notes format

```markdown
# Source notes: <prompt title>

## Grounding mode

<connector-grounded | user-facts-only | mixed | diagnostic>

## Sources checked

- <source>: <facts found>

## Conflicts or gaps

- <none or gap>

## Facts copied into prompt

- <fact>

## Facts intentionally not copied

- <fact and reason>
```

## Citation handling

When the environment supports citations, cite internal files or connector results in the chat response or source-notes file. Do not put tool-specific citation tokens inside a prompt intended to be pasted into Codex or Claude Code unless the user explicitly wants citations in the execution prompt.

## Evidence discipline

- Treat evidence as an audit trail, not a verbose appendix.
- Keep source facts factual; do not include reasoning chains.
- Prefer explicit `unverified` labels over vague wording.
- If no connectors were used, say `Mode: user-facts-only`.

# Downloadable Markdown Output Rules

Use this file with `evidence-blocks.md` and `connector-failure-modes.md`.

Every generated implementation handoff must be returned as a downloadable `.md` file.

## Output modes

Use one of these modes for every generated artifact:

- `grounded-pr-prompt.md`: implementation prompt grounded in GitHub and any required project/doc sources.
- `halt-resume-prompt.md`: continuation prompt for an existing halted branch, grounded in branch/PR/commit state and a halt report.
- `merge-train-prompt.md`: branch landing/rebase/push/PR opening runbook.
- `post-merge-rerank-prompt.md`: diagnostic prompt that should not edit code.
- `docs-proof-prompt.md`: docs/proof/parity amendment prompt.
- `connector-diagnostic.md`: missing-source diagnostic, not an implementation prompt.

## Filename rules

Use a descriptive lowercase slug:

- `pr-prompt-<theme>.md` for implementation PRs.
- `pr-halt-resume-<theme>.md` for halt-resume prompts.
- `merge-train-<branch>.md` for branch landing or merge-train prompts.
- `post-merge-rerank-<theme>.md` for diagnostic prompts.
- `repo-hygiene-<theme>.md` for cleanup/runbook prompts.
- `connector-diagnostic-<theme>.md` when required connector facts are unavailable.
- `<prompt-slug>-sources.md` for companion source notes when evidence should not be embedded in the execution prompt.

Avoid spaces. Use hyphens. Do not include timestamps unless the user asks for versioned files.

## Required file structure

```markdown
# <prompt title>

## How to use this file

Paste everything under `## Prompt` into Claude Code, Codex, or the target implementation agent. Keep the guardrails, halt conditions, commit instructions, PR title, PR body requirements, and final stop line intact.

## Prompt

<copy-paste-ready prompt>
```

## Chat response

Return only:

1. A link to the markdown file.
2. A companion source-notes link when generated.
3. One direct usage sentence.

Example:

```markdown
Created the downloadable prompt: [pr-prompt-corpus-catalog.md](sandbox:/mnt/data/pr-prompt-corpus-catalog.md). Paste everything under `## Prompt` into Claude Code or Codex.
```

Do not paste the full prompt in chat unless the user explicitly asks for inline text.

## Content requirements

The `## Prompt` section must be self-contained. It must include all facts needed by the implementation agent: repo path, GitHub repo, branch/worktree instructions, PR/issue/commit state when available, scope, commits, validation gates, guardrails, PR title/body, stop line, and halt conditions. The implementation agent should not need the surrounding chat to execute the task.

## Evidence requirements

Every prompt must have a grounding mode: `connector-grounded`, `mixed`, `user-facts-only`, or `diagnostic`. Include source facts inline when concise, or generate a companion `<prompt-slug>-sources.md` file using `evidence-blocks.md`. Do not put environment-specific citation tokens inside the paste-ready prompt unless the user explicitly requests them.

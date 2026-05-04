# PR Command Desk

Connector-grounded PR, repo-operations, halt-resume, merge-train, docs/proof, and implementation-agent handoff prompt generator.

## Internal skill name

`pr-command-desk`

## What it produces

The skill produces downloadable Markdown prompt files for implementation agents such as Codex, Claude Code, or equivalent coding agents.

Primary output modes:

- `grounded-pr-prompt.md`
- `halt-resume-prompt.md`
- `merge-train-prompt.md`
- `docs-proof-prompt.md`
- `connector-diagnostic.md`

## Operating model

The skill routes through connected sources before drafting. GitHub is treated as the source of truth for repo state, files, branches, commits, PRs, issues, and CI/check status. Docs and communication connectors are used for policy, product context, audit context, and recent decisions.

## Canonical style

Canonical prompts are operational handoff memos. They include baseline, setup/worktree instructions, scope, commit structure or sequence, validation gates, out-of-scope constraints, halt conditions, PR title/body instructions, and an exact stop line.

## Packaging

The packaged ChatGPT artifact should be named exactly:

```text
skill.zip
```

Keep source files under this directory and publish packaged artifacts through GitHub Releases or release notes under `releases/pr-command-desk/`.

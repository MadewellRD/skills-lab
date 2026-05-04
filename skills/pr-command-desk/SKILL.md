---
name: pr-command-desk
description: create, review, refine, and package connector-grounded pull request, repo-operations, halt-resume, merge-train, docs/proof, and agent handoff prompts as downloadable markdown files. use when the user asks for a pr prompt, next codex/claude handoff, halt resume prompt, repo cleanup prompt, merge-train runbook, post-merge re-rank, audit-to-pr plan, connector-grounded implementation instructions, or operational prompt file backed by github, issues, docs, and communication context.
---

# PR Command Desk

Produce connector-grounded implementation-agent handoff prompts in downloadable Markdown form.

## Core behavior

Use this skill to create operational prompt files for PR builds, halt resumes, merge trains, repo hygiene, docs/proof amendments, post-merge diagnostics, audit-to-PR plans, and connector diagnostics.

Default to the canonical PR Command Desk handoff style: exact operating context, repo/worktree facts, bounded job statement, numbered execution sequence or commit plan, validation gates, out-of-scope constraints, hard halt conditions, PR title/body instructions, and exact stop line.

## Connector preflight

Before drafting, route the request through available connectors.

- Use GitHub as the source of truth for repository files, branches, commits, PRs, issues, changed files, tests, and CI/check state.
- Use issue/project connectors for tickets, labels, priority, acceptance criteria, linked PRs, and blockers.
- Use docs connectors for parity scoreboards, proof maps, architecture docs, completion packs, audit packs, and canonical specs.
- Use communication connectors for decision-bearing conversations, halt reports, and user/team policy decisions.

If load-bearing connector context is unavailable, stale, contradictory, or unverified, produce a connector diagnostic instead of inventing repo state.

## Source hierarchy

Apply this truth order:

1. Current user instruction in the active conversation.
2. Live GitHub repository state.
3. Live issue/project state.
4. Canonical repo/internal docs.
5. Decision-bearing communication sources.
6. Uploaded canonical prompt exemplars.
7. Public web sources for external APIs/tools only.
8. Model inference, clearly labeled as unverified.

## Required output

Every generated prompt must be returned as a downloadable `.md` file. Include a concise usage instruction telling the user which agent/tool should receive the file.

Use one of these output modes:

- `grounded-pr-prompt.md`
- `halt-resume-prompt.md`
- `merge-train-prompt.md`
- `docs-proof-prompt.md`
- `connector-diagnostic.md`

## Evidence

Every generated prompt must be traceable. Include a `Source facts used` block when useful to the implementation agent, or generate a companion source file when the execution prompt should remain clean.

Do not invent branch names, commit SHAs, PR numbers, issue IDs, test names, file paths, CI state, or repo facts.

## Halt discipline

A halt condition is mandatory. If a halt condition triggers, the next prompt must diagnose, narrow, or resume. It must not continue blindly.

Prefer hard operational language: `halt and report`, `do not merge`, `do not push`, `stop at`, `do not touch`, and `do not invent`.

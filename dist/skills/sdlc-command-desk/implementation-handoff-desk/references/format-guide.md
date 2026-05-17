# Implementation Handoff Format Guide

## Canonical style signature

The current canonical style is an operational handoff memo for an implementation agent. It is not a generic PR template. It starts with the exact operating context, states the job in one bounded sentence, pins branch/worktree/base facts, gives a concrete sequence or commit plan, defines validation gates, lists forbidden work, specifies the PR title/body, and ends with an exact stop line.

Use the files in `references/canonical/` as the source of truth for wording and section order.

## Preferred opening forms

Use one of these forms when applicable:

```text
You are operating on [repo path]. Your job is to [bounded job].
```

```text
You are operating on [repo path]. Job: [bounded job].
```

```text
Continue work on branch [branch] in worktree [path]. [narrow continuation instruction].
```

Avoid generic openings such as `PR N: [theme]` unless the user specifically wants a compact prompt-pack item.

## Common canonical sections

Do not force every section into every prompt. Select the sections used by the closest canonical exemplar.

- `State summary:` for base commit, branch, worktree, dirty state, prior PR state, and critical constraints.
- `Current state:` for branch landing/rebase prompts.
- `Working directory:`, `Branch target:`, and `Branch to land:` for merge-train prompts.
- `Sequence:` for linear operational runbooks.
- `What needs testing:`, `What changes:`, or `What to build:` for scoped implementation prompts.
- `Commit 1`, `Commit 2`, `Commit 3` when the PR must have a specific history.
- `Per-PR guardrails:` or `Guardrails:` for hard constraints.
- `Commit message:` when a single exact commit message is required.
- `PR title:`, `PR base:`, and `PR body:` for pull request creation instructions.
- `Stop at "...". Do not merge.` for final stop behavior.

## Section rules

### State summary / Current state

Include facts the agent must verify before editing:

- repository and exact base commit or branch;
- target branch and worktree path;
- expected dirty state or stash/isolation instruction;
- prior PR/merge state;
- expected metrics, row counts, test counts, file counts, corpus counts, or runtime diagnostics;
- known external CI caveats only when the user has allowed local verification to stand in.

### Sequence

Use numbered steps for branch landing, merge-train, repo hygiene, and other operational tasks where order matters.

Every step that can fail should include the required stop behavior immediately after the command block. Use `STOP`, `halt and report`, and `Do not continue to step N` language.

### What needs testing / What changes / What to build

Use the label from the closest exemplar.

- Use `What needs testing:` for test-module PRs.
- Use `What changes:` for docs/proof amendments.
- Use `What to build:` for implementation or tooling PRs.
- Use explicit output schemas for tools that generate artifacts.

### Commit plan

When the prompt prescribes commit history, name each commit and state the exact validation state required before moving to the next commit.

Canonical examples:

- `Commit 1 - failing corpus regressions (RED)`
- `Commit 2 - fix recursive ternary rewrite (GREEN for test 1)`
- `Commit 3 - fix tex2D multiply operand preservation (GREEN for test 2)`

Do not silently combine commits when the prompt requires separation. If combining may be necessary, state the allowed condition explicitly.

### Validation and guardrails

Validation commands must be exact. Guardrails must be prohibitive, not advisory.

Recurring gates:

- `cargo build ... must exit zero`
- `cargo test ... must exit zero`
- `cargo clippy ... -- -D warnings must exit zero`
- `cargo fmt ... -- --check must exit zero`
- docs sync scripts must exit zero;
- row counts or generated artifacts must match expectation;
- deterministic output must be verified when the PR generates snapshots;
- PR must be opened, not merged.

### PR title and body

When known, provide the exact PR title. For PR body, specify the exact content groups the implementation agent must include. Do not leave PR-body quality to the agent's discretion when the exemplar gives required bullets.

### Stop line

End with an exact stop line. Preserve the user's requested wording when present.

Examples:

- `Stop at "PR opened, CI running." Do not merge.`
- `Stop at "PR opened, sync checks green locally." Do not merge.`
- `Stop at "PR opened, all md-render-wgpu tests pass locally including the two new corpus regressions." Do not merge.`
- `Stop at "PR opened, all md-compat-harness tests pass locally, snapshot committed." Do not merge.`

## Connector-grounding rules

### Connector preflight rule

Before writing the prompt, identify the required connector route. GitHub is required for repo facts. Issue/project connectors are required for ticket facts. Docs connectors are required for parity/spec/audit facts. Communication connectors are required only for decisions or halt reports that are not in the active chat.

### Evidence block rule

A prompt must declare whether it is connector-grounded, mixed, user-facts-only, or diagnostic. Add a concise source-facts block or companion source-notes file. Do not mix audit citations into the copy-paste prompt if they will confuse the implementation agent.

### Connector failure rule

If a required connector is missing and the missing facts are load-bearing, generate a connector diagnostic instead of a confident implementation prompt. If the prompt can safely delegate verification, include an explicit pre-flight gate and halt-on-drift language.

## Decision rules

### Canonical exemplar rule

Before drafting, select the closest canonical file and mirror its structure. If multiple files apply, use the one with the closest operational risk profile, then borrow only the relevant section pattern from the secondary exemplar.

### Chained-work rule

Never draft the next implementation PR against an unmerged predecessor. If the prior PR is open, draft only a merge/verification prompt, a post-merge re-rank prompt, or a resume-from-halt prompt for the current branch.

### First-anomaly halt rule

If the work contains rebases, force-pushes, worktree creation, fixture updates, generated baselines, or regression tests, include first-anomaly halt behavior. The agent must stop rather than improvise through conflicts, red gates, or rejected pushes.

### Reproduction-before-fix rule

For bug-fix prompts, require a failing reproduction before implementation. If the expected reproduction does not fail on the unfixed code, the agent must stop and report rather than weaken assertions.

### No-invention proof rule

For docs/proof prompts, require grep or equivalent verification before citing test names, modules, row counts, or status values. Do not invent proof artifacts.

### Local-CI evidence rule

If hosted CI is unavailable for an external reason, local gates can be sufficient only when the prompt explicitly says so. Do not generalize this exception.

### Worktree isolation rule

Use worktrees for parallel work and dirty primary checkouts. Use stash only when the exemplar or user explicitly says to stash named paths.

### GitHub grounding rule

For repo-aware prompts, use GitHub access to verify baseline, branches, PR state, commits, files, and named tests before drafting whenever the connector is available. If GitHub data conflicts with pasted facts, the prompt must halt at pre-flight and report drift. If GitHub is unavailable, state that the prompt is based on user-provided facts only and require the implementation agent to verify live state before editing.

### Downloadable output rule

Generated prompts must be written to markdown files using the wrapper in `references/output-files.md`. The chat reply should link the file and give one direct use instruction.

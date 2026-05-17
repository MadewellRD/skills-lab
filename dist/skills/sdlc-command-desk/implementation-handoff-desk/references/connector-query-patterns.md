# Connector Query Patterns

Use these query patterns when the environment exposes the relevant connector. Adapt to the available tool syntax instead of copying these literally when the tool has different operators.

## GitHub code

Use for files, functions, tests, configs, scripts, and docs.

- Exact test/function: `"translator_recursively_rewrites_nested_ternaries_inside_select_arguments"`
- File path: `path:engine/crates/md-render-wgpu/src/legacy_shader.rs`
- Docs/proof file: `filename:parity-scoreboard.md` or exact path when known
- Validation commands: search for package manifests, CI workflows, README docs, and scripts

## GitHub PRs

Use for predecessor state, merge state, changed files, comments, checks, and compare URLs.

- Open predecessor: `base:main is:pr is:open <branch or theme>`
- Merged predecessor: `is:pr is:merged <title/theme>`
- Author branch: `<branch-name>`

## GitHub commits

Use for baseline SHAs, branch history, and merge commits.

- Recent main history: sort by date descending when supported
- Specific SHA: exact SHA lookup
- Commit message: quoted title when known

## GitHub Issues / Linear

Use for scope, acceptance criteria, blockers, labels, owner, and linked PRs.

- Exact issue ID/title if known
- Component label plus failure term
- Sprint/milestone plus branch/theme

## Docs connectors

Use for parity scoreboards, completion packs, architecture docs, audit packs, prompt packs, and specs.

- Search exact document title first.
- Then search the most distinctive row ID, acceptance criterion, or section title.
- Open the document before relying on a snippet, especially for long-running docs with recent metadata.

## Communication connectors

Use for decision-bearing messages and halt reports.

- Search exact branch, PR number, error shape, or stop line.
- Prefer the newest relevant thread with concrete commands/errors.
- Copy decisions only when speaker/date/context are clear.

## Calendar/email

Use only when timing, ownership, release windows, or stakeholder communication affects the prompt.

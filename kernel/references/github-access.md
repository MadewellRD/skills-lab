# GitHub Access and Repo Grounding

Use GitHub access as the repository source of truth for implementation handoffs. GitHub is required for prompts that depend on real code, branches, commits, pull requests, issues, changed files, tests, validation scripts, or CI/check state.

Read this file together with:

- `connector-routing.md` for when GitHub is required;
- `source-hierarchy.md` for conflict resolution;
- `connector-failure-modes.md` for missing GitHub behavior;
- `connector-query-patterns.md` for search patterns.

## What to inspect

Inspect the available GitHub connector or GitHub-backed search source for:

- repository owner/name and selected repo scope;
- default branch, base branch, target branch, and branch existence;
- open, merged, draft, or halted PR state;
- PR changed files, comments, checks, and mergeability when available;
- issue or bug report context when requested work references tickets;
- commit SHAs, merge commits, and branch history;
- code paths, function names, test names, modules, manifests, workflow files, and docs named in the request;
- existing validation conventions, scripts, package commands, and CI status when available.

## Required GitHub facts by prompt family

### New implementation handoff

- repo owner/name;
- base branch and baseline SHA;
- target branch name and whether it exists;
- predecessor PR state if the next PR depends on it;
- files/modules/tests relevant to scope;
- validation commands from repo conventions;
- PR title/base/body requirements.

### Halt resume prompt

- branch and worktree path if known;
- commits already in place;
- changed files;
- failing check/test/log source;
- current PR state;
- whether it is safe to preserve existing commits.

### Merge train prompt

- main HEAD;
- target branch tip;
- rebase/merge conflict state if available;
- push policy;
- PR or compare URL;
- checks and validation requirements.

### Docs/proof prompt

- exact doc files to edit;
- named tests verified in source;
- row IDs and row counts when available;
- sync/check scripts;
- files forbidden by guardrails.

## Grounding rules

1. Prefer live GitHub facts over memory or stale prompt text when both are available.
2. Do not invent repo facts. If a fact cannot be verified, leave a placeholder, instruct the implementation agent to verify it before editing, or produce a connector diagnostic.
3. If pasted facts conflict with GitHub state, make the generated prompt halt at pre-flight verification and report the drift.
4. If GitHub access is unavailable, explicitly mark the prompt as based on user-provided facts only.
5. If the selected GitHub repo does not match the requested repo, tell the user to select the correct repository before using the prompt as fully grounded.

## Prompt content to carry forward

When verified, include these GitHub-derived facts in the downloadable markdown prompt or source-notes file:

- repo and local path;
- base branch and baseline commit SHA;
- target branch and worktree path;
- PR number, title, base, head, and merge state;
- relevant issue numbers;
- exact files and modules to touch;
- exact files and modules forbidden by the request;
- named tests found in code;
- relevant commit messages or commit count;
- validation commands used by the repo;
- hosted CI status or known CI limitation.

## Connector fallback language

Use this sentence when GitHub context was expected but not available:

`GitHub state was not available to verify live repo facts; this prompt is grounded only in the provided conversation context and requires the implementation agent to verify branch, PR, commit, file, test, and CI state before editing.`

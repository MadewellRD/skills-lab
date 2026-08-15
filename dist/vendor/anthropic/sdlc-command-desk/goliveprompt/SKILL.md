---
name: goliveprompt
description: generate and run the go-live protocol for a software project, covering total repo reconnaissance, status assessment, engineering spec, a full sdlc-command-desk audit hard gate, a sprint-split roadmap with GL ids and acceptance gates, a pinned live tracker artifact, and by-the-book github execution. use whenever the user types /goliveprompt, asks for a go-live prompt, plan, roadmap, or tracker, wants a repo taken to production, wants a project scanned end to end before implementation begins, wants work split into sprints, or wants lifecycle discipline retrofitted onto a project already in flight.
---

# Go-Live Prompt

## Role

Produce and execute the go-live protocol for a named project. The protocol is a fixed six-phase sequence held in `references/protocol-template.md`. This skill resolves the project variables, fills the template, and either hands back the filled prompt or runs it.

The protocol exists to stop implementation from starting before the repo is fully known and audited. Phase 3 is a hard gate. Treat it as one.

## Modes

Pick the mode from the request, do not ask which mode.

1. `emit`: the request names no project, or explicitly asks for the prompt text. Fill the template, write it to a file, present it.
2. `run`: the request names a project or a reachable repo. Fill the template and begin executing Phase 0 in the same turn.
3. `resume`: an engineering spec, a `tracker.json`, or a prior tracker artifact already exists. Reconcile with existing state, then continue from the earliest incomplete phase.

`resume` outranks `run`. A project that already has a tracker is never restarted.

## Variable resolution

Resolve these before filling the template:

```
PROJECT   = project name
REPO      = repo root and github remote
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = {project}-golive-tracker
```

Resolution order: the current request, then `references/presets.md`, then the repo itself (resolve the root through the local filesystem connector's root listing, read the github remote from git config), then the conversation history. Only after all four come up empty, ask, and ask for everything missing in one batch. Never ask for a value a preset already supplies.

The defaults for `SPRINTS`, `TIMELINE`, `SPEC_DIR`, and `TRACKER` stand unless the user overrides them. Do not confirm defaults.

## Execution

Read `references/protocol-template.md` and run the phases in order. The template is the contract; do not paraphrase its requirements away.

Three references carry the detail the phases depend on:

- `references/audit-coverage.md` for Phase 3. It lists every suite and holds the coverage table. "Every suite" means the enumerated list, not a judgment call.
- `references/tracker-contract.md` for Phase 5. It holds the `tracker.json` schema and the artifact requirements. A tracker built off-schema breaks the next session's artifact, so build to the schema even when improvising the visual design.
- `references/presets.md` for known projects and their standing constraints.
- `references/capability-baseline.md` for what the executing model may assume about context, self-verification, long-horizon work, and parallel fan-out.
- `references/halt-taxonomy.md` for when to stop. Phase 3 is a hard gate, so treat a failed audit as a release-integrity halt rather than a note to carry forward. Everything short of the six consequence classes is a soft gap: record it against the GL id and keep moving.

## Parallel surface

Phase 0 reconnaissance is parallel-safe per folder or module: independent subtrees can be read concurrently. Phase 3 audit suites are parallel-safe per suite. The status assessment, the GL backlog, and `tracker.json` are aggregate passes that run once over the collected results, never per item.

## Mid-flight reconciliation

Most runs land on a project already in motion. These rules prevent a run from trampling prior work, and they apply in every mode:

1. Phase 0 captures git state alongside code: current branch, uncommitted work, unpushed commits, open PRs. Uncommitted work found at scan time gets committed or discarded deliberately before new work starts. Nothing rides along in an unrelated commit.
2. GL ids already present in `tracker.json` are canonical. Extend the sequence. Never renumber, never reuse an id, never resequence to make a new plan look tidy.
3. One tracker per project, keyed to the `TRACKER` name. If it exists, refresh it. If the artifact is gone but `tracker.json` survives, rebuild the artifact under the same name against the same file. Never create a second tracker.
4. Existing audit artifacts in `SPEC_DIR` get verified for coverage against the current code rather than re-run from zero. Stale or missing suites get run fresh.
5. Existing specs get reconciled against the scan, and every point of drift gets flagged rather than silently overwritten.

## Status discipline

A task is `done` when its acceptance gate passes, not when it compiles and not when the code is written. Code complete with an unverified gate stays `in_progress` and says so.

When a task is blocked on something only the user can do, such as credentials, a production flag flip, or a browser verify, mark it `blocked`, record the exact human action in `blocked_on`, stage everything that can be staged, and keep working the unblocked queue. Do not idle waiting for a human.

Report status by GL id against repo state. Never report progress from chat memory.

## Output contract

In `emit` mode, write `{project}-golive-prompt.md` containing the filled template and present it.

In `run` and `resume` mode, the outputs are the artifacts the phases produce: the recon record, the status assessment, the populated `SPEC_DIR`, the audit coverage table, the GL backlog, `tracker.json`, the tracker artifact, and the merged PRs. That is one set from one protocol run, not a menu. The mode chooses between emitting the prompt and running it; nothing inside the run list is optional.

Each artifact is finished at the depth the next phase needs. The recon record covers the repo, not a sample of it. The status assessment states what is done, what is claimed done, and the difference. The audit coverage table has a row per suite in `references/audit-coverage.md` with a real result, and a suite that was not run says so. Every GL id carries an acceptance gate specific enough to pass or fail. `tracker.json` matches the schema in `references/tracker-contract.md`, because the next session's artifact is built from it. A phase output that exists as a heading has not been produced.

Phase 0 subtrees and Phase 3 suites are parallel-safe, so those artifacts come out of concurrent work. The aggregate passes named under Parallel surface still run once.

The set being fixed is what makes invention tempting here. An audit suite that could not run is recorded as not run, never as passed. A GL id with no repo evidence behind it does not go in the backlog. A task whose gate has not been checked stays `in_progress`, and one blocked on a human stays `blocked` with the exact action written down. A complete-looking tracker built on unverified status is the single failure this protocol exists to prevent.

Written artifacts follow the user's house style: no em dashes, plain direct prose, no corporate filler. Files written into the repo match the line ending convention already used in that file.

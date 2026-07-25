# Protocol Template

Fill the variables, then execute the phases in order. In `emit` mode this whole block is the deliverable.

```
PROJECT   =
REPO      =
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = {PROJECT}-golive-tracker
```

---

You are running the {PROJECT} go-live protocol. Execute the phases in order. Phase 3 is a hard gate: zero implementation work until it completes. {PROJECT} may already be mid-flight, so reconcile with existing state at every phase and never restart or duplicate what exists.

## Phase 0: Total Repo Reconnaissance

Scan every folder and every file in {REPO}. Read contents, not filenames. No sampling. Skip nothing without noting what was skipped and why. Token budget is not a constraint; completeness is the requirement.

Record as you go:

- stack, languages, and versions
- entry points and runtime topology
- build, test, and lint commands, and whether they currently pass
- CI configuration and current pipeline state
- environment and secrets surface
- dead code, duplicated code, and anything half finished
- existing docs and specs
- git state: current branch, uncommitted work, unpushed commits, open PRs

## Phase 1: Status Assessment

From the scan only, no assumptions:

1. Where are we? What exists, what works, what is partial, what is missing.
2. What needs completed to ship? Every gap, ranked by blocking severity.

Name the things that are broken plainly. A status assessment that reads like a status report is useless.

## Phase 2: Engineering Spec

Create {SPEC_DIR} if absent. It drives end-to-end development from here forward: requirements, architecture decisions, the roadmap, audit output, and `tracker.json` live in it and get committed.

If specs already exist, reconcile them against the scan and flag every point of drift rather than overwriting.

## Phase 3: SDLC Audit (Hard Gate)

Run the entire app through /sdlc-command-desk using every suite listed in `audit-coverage.md`. A suite may be marked N/A only with a one line justification recorded in the coverage table.

Every finding from every suite becomes a backlog item. Nothing gets summarized away, merged into a vaguer parent, or dropped for being small.

Run this even mid-project. Retrofitting the audit beats skipping it. Implementation may begin only when the audit is complete, and everything it surfaced must appear in the action plan.

## Phase 4: Go-Live Roadmap

Produce the complete task list. Every item gets:

- a GL id (GL-01..GL-nn), extending any existing sequence and never renumbering
- an acceptance criterion stated as a verifiable gate, not a description of the work
- dependency ordering
- a source, either the recon scan or the specific audit suite that raised it

Split the backlog across {SPRINTS} sprints with named milestones. Phase 3 findings are non-negotiable entries.

## Phase 5: Live Tracker

Create a pinned artifact named {TRACKER} that reads from {SPEC_DIR}/tracker.json so it reflects repo truth rather than chat memory. Build `tracker.json` to the schema in `tracker-contract.md`.

The artifact shows overall progress, per-milestone bars, the full backlog with status, and the PR and commit feed. It is updated after every merged PR, no exceptions.

## Phase 6: Execution

By the book on GitHub:

1. CI first. If CI is missing or red, fixing it is task one. Nothing merges on red.
2. Branch per task, named to the GL id. PR per change, with a description that links the task and states the acceptance evidence.
3. No direct commits to main.
4. You decide when to push, open PRs, and merge. Merge continually as work completes, never batch at the end.
5. Hook-safe conventional commit messages.
6. Update `tracker.json` in the merge or immediately after, then refresh the tracker.
7. Uncommitted work found in Phase 0 gets committed or discarded deliberately before new work starts.

## Operating Rules

Continuous operation, target {TIMELINE}.

Report status by GL id against repo state, not vibes. A task is done when its acceptance gate passes, not when it compiles.

When blocked on something only the user can do, such as credentials, a production flag flip, or a browser verify, stage everything, state exactly what is needed, and keep working the unblocked queue.

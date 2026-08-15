# Presets

Known projects and their standing values. Never ask for a value a preset supplies. Values in the current request override the preset.

`REPO` is an absolute path. Resolution by search is a fallback for a project that has never been run, never a step in a `resume`. A project that has been run before and still carries an unpinned `REPO` line is a defect in this file: pin it from the session that discovers it, and name any sibling directory a search could confuse it with. `list_roots` returns overlapping roots, so a search that finds one match has not established that it found the only one.

## MrdOS

```
PROJECT   = MrdOS
REPO      = D:\projects\mrdOS  (remote github.com/MadewellRD/mrdOS)
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = aitsm-golive-tracker
```

Standing notes:

- The working clone is `D:\projects\mrdOS` and it is the only one. Do not resolve it by search. `list_roots` returns both `D:\dev` and `D:\projects`, both contain a directory named `mrdOS`, and a search resolves to whichever is walked first.
- `D:\dev\mrdOS` is a dormant pre-Gate-6 clone. Last commit 2026-08-02, last fetch 2026-08-04, roughly seventy stale July feature branches, HEAD sitting on a fast-forward of `origin/main` under a feature branch name. Verified 2026-08-14 to hold zero commits absent from the remote, so nothing is lost by leaving it alone. Never work in it, never fetch it to catch it up, never delete it. A session that finds itself there has resolved the root wrongly and should stop and re-read this file.
- The tracker artifact name is `aitsm-golive-tracker`, not the `{PROJECT}-golive-tracker` default. It is already pinned and already carries GL ids. Refresh it, never replace it.
- Repo access runs through SignalDesk MCP against the local machine. The tracker reads `docs/engineering-spec/tracker.json` and recent commits through that connector.
- Has a browser-facing surface, so the web suites in `audit-coverage.md` apply on top of the core SDLC suites.
- Repo files use per-file line ending conventions that have been deliberately normalized. Match the existing convention in each file rather than imposing one.
- Commit hooks are active, so commit messages must be hook-safe conventional commits.

## PROMETHEUS

```
PROJECT   = PROMETHEUS
REPO      = resolve root via SignalDesk list_roots, remote from git config
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = prometheus-golive-tracker
```

TypeScript multi-agent orchestration platform. Web suites apply only if it ships a browser surface; confirm from the scan rather than assuming.

## SOCIETY

```
PROJECT   = SOCIETY
REPO      = resolve root via SignalDesk list_roots, remote from git config
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = society-golive-tracker
```

Rust event-sourced simulation on GCP. Expect the deployment, observability, and release suites to carry more weight than usual, and expect infrastructure state to matter as much as repo state during Phase 0.

## ROGUE:OPS

```
PROJECT   = ROGUE-OPS
REPO      = resolve root via SignalDesk list_roots, remote from git config
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = rogue-ops-golive-tracker
```

Governance-first AI execution framework. The colon in the project name is dropped in ids, branch names, and file paths. Security and verification findings are first-class here rather than a late gate.

## Adding a project

PROMETHEUS, SOCIETY and ROGUE-OPS still carry unpinned `REPO` lines and are not pinned here because no session has established their roots against ground truth. SOCIETY is ambiguous today: `D:\dev\society` and `D:\dev\society-platform` both exist. Pin each from the next session that works it, from the reflog and the remote rather than from a guess.

A new project needs only `PROJECT` and a reachable `REPO`. Everything else takes the defaults. Add a preset block once the project has been run through the protocol and its tracker name is fixed, since the tracker name is the value most likely to drift from the default.

<!-- UNPINNED_ALLOWANCE: PROMETHEUS -- no session has established the working clone against reflog and remote; pin from the next session that works it -->
<!-- UNPINNED_ALLOWANCE: SOCIETY -- ambiguous today: D:\dev\society and D:\dev\society-platform both exist and neither has been checked against its reflog -->
<!-- UNPINNED_ALLOWANCE: ROGUE-OPS -- D:\dev\ROGUE-OPS is the likely root but D:\dev\ROGUE-GPT sits beside it and the working clone has not been confirmed -->

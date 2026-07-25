# Presets

Known projects and their standing values. Never ask for a value a preset supplies. Values in the current request override the preset.

## MrdOS

```
PROJECT   = MrdOS
REPO      = resolve root via SignalDesk list_roots, remote from git config
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = aitsm-golive-tracker
```

Standing notes:

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

A new project needs only `PROJECT` and a reachable `REPO`. Everything else takes the defaults. Add a preset block once the project has been run through the protocol and its tracker name is fixed, since the tracker name is the value most likely to drift from the default.

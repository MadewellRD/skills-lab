# Presets

Standing values for projects this protocol has already been run against. Never ask for a
value a preset supplies. Values in the current request override the preset.

This file ships inside a public skill package. **Keep it free of real project names,
absolute paths, repository URLs, machine layout, and operational history.** Those belong
in a local override that is never committed. The example below is illustrative and names
no real project.

## Where your presets actually live

Put real presets in a file outside this package and point the run at it:

```
PRESETS = <path to your local presets file>
```

Anything the run does not find there falls back to the defaults below. A local presets
file is untracked by design: it carries paths and project facts that are yours, and a
skill package is the wrong place for either.

## Preset shape

```
PROJECT   = <short name, used for ids, branches, and the tracker name>
REPO      = <absolute path to the working clone>
SPRINTS   = 8
TIMELINE  = 3-4 days continuous
SPEC_DIR  = docs/engineering-spec
TRACKER   = {PROJECT}-golive-tracker
```

Only `PROJECT` and a reachable `REPO` are required. Everything else takes the default.
Add a block once a project has been run through the protocol and its tracker name is
fixed, since the tracker name is the value most likely to drift from the default.

## REPO must be an absolute path

This is the rule the whole file exists for, and it was learned the expensive way.

Resolution by search is a fallback for a project that has never been run. It is never a
step in a `resume`. A root resolver can return overlapping roots, and more than one of
them can contain a directory with your project's name, so a search that finds one match
has not established that it found the only one. The root then gets re-decided every
session, and some fraction of the time it lands on a dormant clone: work happens, looks
successful, and goes nowhere anyone will find it.

So:

- Pin `REPO` to an absolute path from the session that first establishes it.
- Establish it from evidence, not preference: the reflog date of the last real commit,
  which branches have live upstreams, whether the cached remote ref is current, and
  whether any candidate holds commits absent from the remote.
- Record the sibling directory a search could confuse it with, so the next session
  recognises a wrong resolution instead of repeating it.
- A project that has been run before and still carries an unpinned `REPO` is a defect in
  your presets file, not a pending task.

`tools/validate_presets.py` enforces this. A non-absolute `REPO` fails the check unless
the project carries an explicit allowance naming the reason:

```
<!-- UNPINNED_ALLOWANCE: PROJECT_NAME -- why it cannot be pinned yet -->
```

An allowance with no reason does not count, and an allowance naming a project with no
preset block is an error, so allowances cannot outlive what they excuse.

## Example

Illustrative only. Replace with your own, in your local presets file.

```
PROJECT   = EXAMPLE-APP
REPO      = /srv/work/example-app
SPRINTS   = 8
SPEC_DIR  = docs/engineering-spec
TRACKER   = example-app-golive-tracker
```

Standing notes worth recording per project, when they apply:

- Whether a second clone of the same name exists, where it is, and that it is dormant.
- Whether the tracker artifact name differs from the `{PROJECT}-golive-tracker` default,
  and whether it is already pinned and carrying ids. Refresh a pinned tracker, never
  replace it.
- Whether the project ships a browser surface, which decides whether the web suites in
  `audit-coverage.md` apply on top of the core SDLC suites.
- Whether commit hooks are active, which constrains commit message format.
- Whether the repository uses per-file line ending conventions that have been deliberately
  normalized, in which case match each file rather than imposing one.

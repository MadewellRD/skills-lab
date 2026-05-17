# Refactor Plan Template

## Refactor target

Name the modules, files, classes, functions, packages, or boundaries.

## Goal

Define the maintainability objective without adding feature scope.

## Non-goals

List feature work, unrelated cleanup, and behavior changes that are out of scope.

## Proposed sequence

1. Characterization tests or baseline verification.
2. Mechanical extraction, rename, move, or consolidation.
3. Compile/test cleanup.
4. Documentation or proof-map update if needed.

## Files likely affected

List known files and mark uncertain files separately.

## Regression controls

Name tests, commands, snapshots, CI checks, or manual checks.

## Rollback/revert considerations

Describe revert safety and any migration implications.

## Downstream handoff

State what `implementation-handoff-desk` needs to generate a safe PR prompt.

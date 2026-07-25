# Connector Routing

## Required GitHub facts

Use GitHub for:

- Repository name and selected branch.
- Target files, modules, package manifests, lockfiles, CI config, test tree, and build scripts.
- Open issues, PRs, labels, milestones, ownership signals, and recent related commits.
- CI checks, workflow failures, test failures, and build matrix when relevant.

## Required document facts

Use docs or uploaded files for:

- Architecture and component-boundary decisions.
- Migration or deprecation policy.
- Release compatibility requirements.
- Existing technical-debt audits.
- Runbooks and operational constraints.

## Required issue/project facts

Use issue/project connectors when maintenance work depends on:

- Acceptance criteria.
- Severity or priority.
- Owners and blockers.
- Release/milestone target.
- Linked PRs or incidents.

## Optional sources

Use public web only for external package release notes, framework migration docs, CVE/vendor advisories, or public API compatibility information not available in repo docs.

## Missing connector behavior

When a required source is unavailable, produce a scoped artifact based only on user-provided facts or a connector diagnostic. Do not invent dependency versions, affected files, CI status, test names, package compatibility, or dead-code proof.

# Connector Routing

## GitHub

Required when the artifact depends on:

- Source files, paths, modules, tests, fixtures, or generated artifacts.
- Pull requests, changed files, review comments, commits, branches, or CI status.
- GitHub issues, labels, milestones, or acceptance criteria.

Retrieve: repo owner/name, branch or commit, relevant files, named tests, PR/issue numbers, check status, and changed-file scope.

## Document sources

Required when the artifact depends on:

- PRDs, SRS/SDS, architecture docs, roadmap docs, parity docs, status docs, audit packs, completion packs, release notes, or policy docs.

Retrieve: title, date, section, exact claim text, source location, and whether content appears current.

## Communication sources

Optional unless the user asks for decision history or recent team context. Use Slack, Teams, email, or pasted halt reports only for decisions, rationale, and current intent. Do not treat chat as repo truth.

## Public web

Use only for external standards, public APIs, public vendor docs, or public repository research not available through connected sources.

## Missing connector behavior

If a required connector is unavailable, produce `connector-diagnostic.md` with:

- Missing source.
- Facts that cannot be verified.
- Safe partial output possible, if any.
- Exact user action needed to continue.

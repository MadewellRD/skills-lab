# Connector Routing

## V&V report
Required sources:
- requirements source: PRD, SRS, issue body, design spec, or user-provided acceptance criteria
- GitHub source: PRs, commits, changed files, checks, and tests when repo work is involved
- evidence source: CI logs, test output, artifacts, or QA notes

Halt if requirement source or implementation evidence is missing.

## RTM
Required sources:
- stable requirement source
- implementation evidence
- validation evidence

Halt if requirements cannot be enumerated.

## Acceptance-gate review
Required sources:
- expected gates or acceptance criteria
- observed gate results

Halt if expected gates are unknown.

## Release-blocker report
Required sources:
- release scope
- acceptance gates
- failed checks, missing evidence, or risk notes

Halt if release scope is ambiguous.

## Downstream implementation handoff
Required sources:
- verified gap or blocker
- affected files, PRs, issues, or tests

Continue into implementation handoff after the gap is concrete and implementation-readiness facts are present.

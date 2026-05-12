# Risk and Unknowns Classification

Classify each risk or unknown with one type and one severity.

## Types

- `technical`: architecture, code, dependency, scalability, compatibility, or migration concern.
- `product`: unclear requirement, user value, scope, or acceptance criteria.
- `integration`: external API, service, contract, auth, rate-limit, or failure-mode concern.
- `security`: auth, authorization, secrets, dependency vulnerability, abuse, privacy, or compliance concern.
- `delivery`: timeline, staffing, CI, release, rollout, or operational concern.
- `evidence`: missing source, stale fact, unverified assumption, or connector gap.

## Severity

- `blocker`: cannot proceed safely without resolution.
- `high`: can plan, but implementation should not start without mitigation.
- `medium`: acceptable with explicit mitigation or spike.
- `low`: document and monitor.

## Unknown handling

A useful unknown has:

- A concrete question
- The source or command needed to answer it
- The owner or next skill that should resolve it
- A stop condition if unresolved

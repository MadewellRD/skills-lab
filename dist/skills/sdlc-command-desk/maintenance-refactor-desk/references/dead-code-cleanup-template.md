# Dead-Code Cleanup Template

## Candidate item

Name candidate file, symbol, dependency, config, route, feature flag, test, or doc.

## Evidence

Record all evidence: search results, import graph, runtime references, build config, routing, telemetry, feature flags, public APIs, and docs.

## Proof status

Classify as:

- proven unused
- likely unused
- unclear
- actively used

Only proven unused items should proceed to removal without additional investigation.

## Removal plan

List files to delete or update, expected compile/test impact, and docs changes.

## Safety checks

Include search, build, tests, runtime smoke checks, and release/deployment considerations.

## Halt conditions

Halt on dynamic loading, reflection, plugin references, external API consumers, config-only usage, or incomplete search coverage.

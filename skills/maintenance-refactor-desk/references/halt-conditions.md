# Halt Conditions

Halt and report when:

- Required GitHub repo state is unavailable.
- Dependency version, lockfile, or compatibility facts are missing.
- Static search cannot prove a dead-code candidate is unused.
- Dynamic loading, plugins, reflection, generated code, or external consumers may reference the target.
- The refactor includes feature behavior or product scope.
- A migration changes data, public APIs, auth, deployment, or release behavior without downstream plans.
- CI/test gates cannot be identified.
- Source facts conflict across repo, docs, tickets, and CI.
- The user asks for a broad cleanup with no bounded target.

When halting, provide missing facts, conflicting sources, safest narrowed scope, and the SDLC desk that should handle the next step.

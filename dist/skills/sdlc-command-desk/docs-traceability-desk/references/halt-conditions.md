# Halt Conditions

Halt or produce a connector diagnostic when:

- A claim depends on GitHub state but no repo/source facts are available.
- A claim depends on a canonical doc that cannot be accessed.
- A doc cites a file, test, issue, PR, or commit that cannot be found.
- Two trusted sources conflict and the current user has not resolved the conflict.
- The requested artifact would require inventing evidence.
- The user asks for audit/compliance proof without sufficient source facts.
- The requested scope is too broad to verify in one pass; produce a scoped plan instead.

When halting, report:

- The missing or conflicting source.
- The claims affected.
- The safest partial artifact, if any.
- The exact next source or connector needed.

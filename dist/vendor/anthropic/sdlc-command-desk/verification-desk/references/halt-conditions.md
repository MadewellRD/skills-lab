# Halt Conditions

Halt or produce a connector diagnostic when:

- Requirement sources are missing or contradictory.
- Requirement IDs cannot be assigned or mapped.
- GitHub PR, commit, branch, check, or changed-file state is required but unavailable.
- CI/test status is required but logs or run status cannot be accessed.
- Evidence conflicts with claimed completion.
- A release decision is requested without release scope.
- Security, compliance, or privacy evidence is required but absent.
- The user asks for a definitive pass/fail decision but required gates are unknown.

When halting, report:

1. Missing or conflicting source.
2. Why it blocks verification.
3. Exact information needed to continue.
4. Whether a partial report can still be produced.

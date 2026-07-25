# Halt Conditions

Halt or produce a connector diagnostic when:

- Required requirements or acceptance criteria are missing.
- The repo/test tree cannot be inspected but the user expects repo-grounded coverage analysis.
- The requested plan depends on CI status that is unavailable.
- Source facts conflict and the conflict changes test scope or release risk.
- The user asks for coverage claims without enough evidence to inspect tests or assertions.
- Sensitive production data would be needed for fixtures and no approved sanitized source exists.
- A regression cannot be reproduced and no baseline behavior is documented.
- The plan would require broad implementation work outside test strategy.

When halting, return:

1. Missing or conflicting facts.
2. Sources checked.
3. Why the artifact would be unsafe or misleading.
4. The minimum information needed to proceed.

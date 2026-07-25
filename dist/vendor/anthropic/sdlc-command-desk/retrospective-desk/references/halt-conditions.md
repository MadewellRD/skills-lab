# Halt Conditions

Halt, downgrade confidence, or produce a connector diagnostic when:

- The requested retrospective depends on GitHub facts but GitHub is unavailable.
- PR, issue, commit, release, or CI state cannot be verified.
- Timeline evidence conflicts and cannot be resolved.
- Incident impact or severity is asserted but not supported by evidence.
- Required docs are missing, stale, or contradictory.
- Metrics are requested but cannot be computed from available sources.
- Action owners or due dates are requested but not present in source material.
- The user asks for blame assignment unsupported by evidence.
- The retrospective would expose private or unavailable source details not accessible to the current user.

When halting, list the missing evidence and the connector or source needed.

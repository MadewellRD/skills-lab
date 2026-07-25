# Halt Conditions

Halt or produce a connector diagnostic when:

- target version, tag, branch, commit, or release range is unknown
- GitHub facts conflict with user-provided release scope
- merged PR list is incomplete or unverified
- CI/check status is unavailable for a gated release
- verification evidence is missing or stale
- security, privacy, or compliance review is required but unavailable
- rollback path is requested but deployment surface or data migration state is unknown
- release notes require customer-facing claims that are not supported by source facts
- the user asks to deploy, tag, publish, or merge and the current environment cannot do it safely

When halted, report:

- missing or conflicting facts
- affected release gate
- source queried
- safest next action

# Halt Conditions

Halt or produce a connector diagnostic when:

- Required GitHub repo, PR, issue, branch, commit, check, workflow, run, job, log, artifact, or changed-file facts are unavailable.
- Logs are truncated or missing the failing command and error signature.
- GitHub check state conflicts with pasted agent or user reports.
- A rerun would hide a possible deterministic failure or release blocker.
- The action requires changing secrets, credentials, billing, repository settings, required checks, or branch protection.
- A failure may be security-sensitive, such as leaked secrets, excessive token permissions, or unauthorized deployment access.
- Release or deployment is requested while required checks are red or unverified.
- Scope expands from diagnosis into implementation without bounded handoff.

When halting, report:

- missing source
- why it is required
- safest partial output available
- next connector or evidence needed
- whether `implementation-handoff-desk`, `verification-desk`, or `release-operations-desk` should receive the handoff

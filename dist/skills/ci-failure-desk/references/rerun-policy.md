# Rerun Policy

Use this policy to decide whether to rerun, fix, halt, or escalate.

## Rerun is appropriate when

- Same commit has passed the same check before.
- Failure signature indicates runner outage, network timeout, package registry outage, external service transient, quota/billing interruption, or known flaky test behavior.
- Logs show no deterministic assertion failure and the error is infrastructure-level.
- The user or release policy allows rerun with evidence retained.

## Fix is required when

- A deterministic test assertion fails.
- Compile, typecheck, lint, formatting, migration, dependency, or security scan failure points to repository content.
- A required secret, permission, or workflow config is missing or wrong.
- The failure reproduces locally or across repeated runs on the same commit.
- The failed check aligns with files changed in the PR.

## Halt is required when

- Logs or workflow run facts are missing.
- GitHub check state conflicts with pasted reports.
- Rerun would hide a possible release blocker.
- Credentials, secrets, billing, permissions, or branch protection changes are required.
- The requested action would merge or deploy while required gates are red.

## Escalate when

- The failure depends on repository settings or branch protections not visible through connectors.
- A live secret or permission issue is suspected.
- External vendor incident evidence is needed but unavailable.
- Required checks appear misconfigured at repository settings level.

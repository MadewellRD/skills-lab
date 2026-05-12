# Connector Routing

## Incident triage

Required:
- Incident report or alert context.
- Telemetry source when available.
- GitHub when code, deploy, release, or CI state is implicated.

Retrieve:
- Current status, start time, affected systems, symptoms, known impact, mitigation attempts, recent deploys, active incidents, related issues or PRs.

Halt when:
- User asks for live status but no current incident or telemetry source is available.
- Customer impact or recovery status is asserted without source evidence.

## RCA or post-incident review

Required:
- Incident timeline evidence.
- Mitigation and recovery evidence.
- Root-cause evidence or explicitly labeled root-cause hypothesis.

Retrieve:
- Timeline, trigger, contributing factors, detection path, response actions, owner notes, verification evidence, follow-up work.

Halt when:
- The incident is not resolved but the user asks for a final RCA.
- Recovery cannot be verified.

## Bug or regression triage

Required:
- Reproduction details or issue report.
- GitHub issue/PR/commit context when linked to code.

Retrieve:
- Expected/actual behavior, environment, recent changes, logs, test failures, suspected owners, duplicate issues.

Halt when:
- No reproduction path or affected environment can be identified and the user needs implementation instructions.

## Hotfix handoff

Required:
- GitHub repo state.
- A bounded remediation target.
- Validation and rollback expectations.

Retrieve:
- Base branch, recent commits, candidate files, failing tests/checks, release/rollback constraints, linked issue or incident ID.

Halt when:
- Hotfix scope is ambiguous, blast radius is unknown, or rollback authority is unclear.

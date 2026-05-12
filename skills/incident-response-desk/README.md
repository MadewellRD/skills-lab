# Incident Response Desk

`incident-response-desk` creates connector-grounded incident response, RCA, bug triage, hotfix handoff, and follow-up remediation artifacts for SDLC production-support workflows.

## Lifecycle coverage

Covers SDLC stage 20: incident response, bug triage, and production support. It also composes with release, deployment, observability, CI failure triage, verification, and documentation traceability.

## Intended inputs

- Incident reports, alert summaries, status updates, or support escalations.
- GitHub issues, PRs, commits, CI/checks, release tags, and changed files.
- Logs, metrics, traces, dashboards, SLO/SLA summaries, and alert timelines when available.
- Release notes, deployment plans, feature-flag state, rollback plans, and runbooks.
- Slack, Teams, email, or status-page updates for timeline and decision context.

## Intended outputs

- Incident triage brief.
- Severity classification.
- RCA or post-incident review.
- Bug triage and reproduction plan.
- Hotfix handoff for `implementation-handoff-desk`.
- Follow-up issue plan and verification gates.
- Connector diagnostic when required evidence is missing.

## Required connectors

GitHub is required for code, PR, issue, commit, release, and CI evidence. Observability, deployment, docs, and communication connectors are required when claims depend on runtime status, rollout state, runbooks, stakeholder decisions, or timeline facts.

## Composition

Use this skill to stabilize and analyze incidents. Use `implementation-handoff-desk` for implementation-agent hotfix prompts, `ci-failure-desk` for failing pipeline diagnosis, `deployment-desk` for rollback/rollout control, `observability-readiness-desk` for telemetry gaps, and `docs-traceability-desk` for runbook or evidence updates.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.

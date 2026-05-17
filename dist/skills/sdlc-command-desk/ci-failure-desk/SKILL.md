---
name: ci-failure-desk
description: create connector-grounded ci/cd failure triage and pipeline-health artifacts for software delivery. use when chatgpt needs to diagnose github actions or build failures, classify flaky tests, inspect logs and workflow runs, decide rerun versus fix, identify failing checks, map ci failures to code changes or infrastructure, or prepare downstream handoff notes for review-quality-desk, verification-desk, release-operations-desk, incident-response-desk, issue-planning-desk, or implementation-handoff-desk workflows.
---

# CI Failure Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to turn CI, build, workflow, test, and deployment-check failures into traceable diagnostics, rerun decisions, fix scopes, and downstream handoff notes.

## Core workflow

1. Classify the request.
   - CI failure diagnosis: use `references/ci-diagnostic-template.md`.
   - Flaky-test classification: use `references/flake-triage-template.md`.
   - Pipeline health or workflow review: use `references/pipeline-health-template.md`.
   - Rerun or escalation decision: use `references/rerun-policy.md`.
   - Downstream implementation handoff: use `references/handoff-rules.md`.

2. Run connector preflight.
   Use `references/connector-routing.md` before making claims about workflow runs, jobs, logs, checks, commits, changed files, tests, branches, PRs, or deployment gates. GitHub is source of truth for repository workflow files, checks, Actions runs, jobs, logs, commit status, branches, PR metadata, and changed files. Docs define release policy, required checks, test strategy, and deployment expectations.

3. Establish the source hierarchy.
   Apply `references/source-hierarchy.md`. Current user instruction defines scope. GitHub controls CI facts. Requirement, test, release, and operations docs control expected gates. Communication sources provide halt reports and decision context, not check-state truth.

4. Produce the smallest sufficient artifact.
   Choose a CI diagnostic, flake triage report, pipeline-health report, rerun decision, fix-scope note, or downstream handoff. Include source facts, failing run/job/check identifiers, observed error signatures, suspected root cause, confidence, reproduction or rerun recommendation, and next gate.

5. Halt rather than invent.
   If required GitHub or log facts are unavailable, produce a connector-needed diagnostic or explicitly mark the artifact as user-fact-only. Do not invent workflow names, check statuses, job IDs, log lines, branch state, failure history, or flake evidence.

## CI triage rules

- Separate confirmed failures from suspected causes.
- Prefer exact error signatures, job names, failing commands, and file paths over broad explanations.
- Distinguish code regression, test regression, environment failure, dependency outage, permission/configuration failure, quota/billing failure, and flaky behavior.
- A failed check is not automatically a code defect. Confirm whether the same commit, same test, or same workflow has failed previously.
- Recommend rerun only when the failure pattern supports flake, infrastructure, external-service, or transient classification.
- When a fix is required, prepare bounded notes for `issue-planning-desk` or `implementation-handoff-desk`; do not broaden into unrelated cleanup.
- When a CI failure blocks release, prepare evidence for `verification-desk` and `release-operations-desk`.

## Output requirements

Default to downloadable Markdown artifacts when producing diagnostics, pipeline reports, rerun decisions, handoffs, or connector diagnostics. Include a `How to use this file` section when the artifact is intended for another agent, reviewer, or release operator.

For deterministic file wrapping, use `scripts/write_ci_failure_markdown.py` when a local artifact file is requested.

## References

- `references/ci-diagnostic-template.md`: CI failure diagnostic structure.
- `references/flake-triage-template.md`: flaky-test classification structure.
- `references/pipeline-health-template.md`: workflow and pipeline-health review structure.
- `references/rerun-policy.md`: rerun, fix, halt, and escalation rules.
- `references/root-cause-rubric.md`: failure taxonomy and confidence rubric.
- `references/connector-routing.md`: connector requirements by task.
- `references/source-hierarchy.md`: source precedence and conflict handling.
- `references/output-contract.md`: artifact names and output rules.
- `references/handoff-rules.md`: downstream SDLC handoffs.
- `references/halt-conditions.md`: mandatory stop conditions.
- `references/suite-workflow-contract.md`: shared workflow packet, continuation, and halt contract for SDLC Command Desk suite orchestration.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/codex-conservation-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `CODEX_BLOCKER` when implementation handoff facts are insufficient for a coding agent.

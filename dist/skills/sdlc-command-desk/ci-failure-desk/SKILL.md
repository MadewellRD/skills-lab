---
name: ci-failure-desk
description: create connector-grounded ci/cd failure triage and pipeline-health artifacts for software delivery. use when the assistant needs to diagnose github actions or build failures, classify flaky tests, inspect logs and workflow runs, decide rerun versus fix, identify failing checks, map ci failures to code changes or infrastructure, or prepare downstream handoff notes for review-quality-desk, verification-desk, release-operations-desk, incident-response-desk, issue-planning-desk, or implementation-handoff-desk workflows.
---

# CI Failure Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to turn CI, build, workflow, test, and deployment-check failures into traceable diagnostics, rerun decisions, fix scopes, and downstream handoff notes.

## Core workflow

**Outcome.** The smallest sufficient artifact that answers the request: a CI diagnostic, flake triage report, pipeline-health report, rerun decision, fix-scope note, or downstream handoff.

**Artifact selection.** CI failure diagnosis uses `references/ci-diagnostic-template.md`. Flaky-test classification uses `references/flake-triage-template.md`. Pipeline health or workflow review uses `references/pipeline-health-template.md`. Rerun or escalation decisions use `references/rerun-policy.md`. Downstream implementation handoff uses `references/handoff-rules.md`.

**Grounding.** Run connector preflight per `references/connector-routing.md` before making claims about workflow runs, jobs, logs, checks, commits, changed files, tests, branches, PRs, or deployment gates. GitHub is source of truth for repository workflow files, checks, Actions runs, jobs, logs, commit status, branches, PR metadata, and changed files. Docs define release policy, required checks, test strategy, and deployment expectations.

**Source hierarchy.** Apply `references/source-hierarchy.md`. Current user instruction defines scope. GitHub controls CI facts. Requirement, test, release, and operations docs control expected gates. Communication sources provide halt reports and decision context, not check-state truth.

**Parallel surface.** Failing checks, jobs, workflow runs, and log files are independent of one another. Retrieve and triage them in parallel rather than looping serially, then merge the findings into one artifact.

**Acceptance bar.** The artifact is done when every failing run, job, and check is named by its identifier; each error signature is quoted from retrieved logs rather than paraphrased; confirmed failures are separated from suspected causes and each suspected cause carries a confidence level; and the rerun-versus-fix recommendation and next gate are stated explicitly. Do not invent workflow names, check statuses, job IDs, log lines, branch state, failure history, or flake evidence. When GitHub or log facts are simply absent, mark the artifact user-fact-only and continue.

## CI triage rules

- Separate confirmed failures from suspected causes.
- Prefer exact error signatures, job names, failing commands, and file paths over broad explanations.
- Distinguish code regression, test regression, environment failure, dependency outage, permission/configuration failure, quota/billing failure, and flaky behavior.
- A failed check is not automatically a code defect. Confirm whether the same commit, same test, or same workflow has failed previously.
- Recommend rerun only when the failure pattern supports flake, infrastructure, external-service, or transient classification.
- When a fix is required, prepare bounded notes for `issue-planning-desk` or `implementation-handoff-desk`; do not broaden into unrelated cleanup.
- When a CI failure blocks release, prepare evidence for `verification-desk` and `release-operations-desk`.

## Halt policy

Proceed by default. When a CI fact is missing or ambiguous, take the most defensible reading, label it inline as an assumption, and continue the diagnosis. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — a rerun, escalation, or permission change needs human authorization.
- **Production or destructive** — the recommended action re-triggers a deployment job or deletes branches, caches, or artifacts.
- **Security or privacy** — logs expose secrets, tokens, or personal data, or the failure is itself a credential or permission leak.
- **Source conflict** — live check state and user-supplied facts genuinely disagree on a load-bearing fact.
- **Release integrity** — a gate would be reported as passing when its result cannot be established.
- **Connector unreachable** — GitHub or the log source exists but cannot be read. Evidence that is merely absent is a soft gap: produce a connector-needed diagnostic or a user-fact-only artifact and continue.

## Output requirements

A triage run on a failing pipeline delivers the set, not the first useful piece of it: the diagnostic covering every failing check by identifier, the flake classification for any test with intermittent history in the retrieved evidence, the rerun-versus-fix decision with the reasoning that produced it, and the fix-scope handoff for whichever desk picks the work up next. Pipeline-health review is a different scope — a read across recent runs rather than one failure — and stays its own artifact rather than being folded in.

Depth is measured against the person who has to act. A diagnostic is finished when someone can go straight to the failing job and the failing line without re-reading logs: exact run and job identifiers, the quoted error signature, the commit and changed files in play, and the classification with its confidence. "Tests are failing in CI" restates the input.

Failing checks and jobs are independent, so the pieces of the set are produced concurrently on the parallel surface described in the core workflow.

Delivering the whole set never means completing it by inference. A check whose logs could not be retrieved is reported as unretrieved rather than diagnosed, a flake claim with no failure history behind it is stated as a hypothesis, and a rerun recommendation with no supporting pattern is not made at all. When GitHub or log facts are simply absent, the artifact is marked user-fact-only and stays short.

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

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.

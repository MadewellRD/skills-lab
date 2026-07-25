---
name: runbook-engineering-desk
description: write and review operational runbooks keyed to the alert or failure mode that triggers them, with the first mitigating action stated before diagnosis, diagnostic decision trees carrying exact queries and dashboards, escalation and rollback branches, access and permission preconditions for the responder, freshness state per runbook, and the alerts left with no runbook at all.
---

# Runbook Engineering Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the runbook artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent commands, query text, dashboard names, service endpoints, flag names, role names, escalation contacts, or the date a runbook was last validated.

## Role

Own what a responder does in the first ten minutes. A runbook here is not documentation about a service; it is an executable response to a specific trigger, written for someone woken at three in the morning who did not build the system, may never have touched it, and is reading on a phone before reaching a laptop.

That reader constrains everything. The trigger has to match the alert text they just received, the first action has to stop user harm before anyone understands the cause, every command and query has to be copy-runnable rather than described, and the access it assumes has to be access the responder actually has at that hour rather than access they can request on Monday. A runbook that requires understanding before acting is a design document that happens to be linked from a page.

The recurring defect in this domain is not the missing runbook; it is the stale one. A step pointing at a decommissioned dashboard, a command for a deployment tool replaced last quarter, or a rollback procedure for a service that now runs behind a different gateway all fail at the worst possible moment, and they fail while looking authoritative.

## Use when

- Alerts route to a page and need the response that makes the page actionable.
- A failure mode from dependency analysis, a chaos result, or a postmortem has a known mitigation that nobody has written down.
- Existing runbooks need a freshness review: which have been used in a real incident, which reference resources that no longer exist, which have never been exercised.
- A postmortem action item calls for a runbook, or an incident showed the runbook was wrong in a specific step.
- A degradation mode from resilience design needs an operator procedure: how to shed load, flip to the cached path, drain a zone, or turn a feature off.
- A responder onboarding gap is really an access gap, and the preconditions need naming before the next shift starts.

## Do not use when

- The alert itself is wrong, noisy, or missing: that is `alerting-quality-desk`, which sets the trigger this desk answers.
- The mitigation does not exist yet as a system capability, such as a shed policy or a fallback path that has to be built: that is `resilience-architecture-desk`.
- The question is who is reachable and how escalation proceeds: that is `oncall-escalation-desk`, which owns the tiers this desk branches to.
- The procedure is a recovery of last resort, involving failover, restore, or regional evacuation: those belong to `disaster-recovery-desk` and `backup-restore-desk`, which own the ordered recovery sequences a runbook may reference.
- An incident is running now and the runbook is missing: that is `incident-command-desk`, which continues without it and files the gap.

## Required evidence

- The alert set with routing, expressions, and the failure mode each alert corresponds to.
- The failure mode inventory with trigger, propagation, and the mitigation believed to stop user impact.
- Resilience control values and degradation modes, so the runbook can state the flag, the shed threshold, or the fallback that exists rather than a generic instruction to reduce load.
- The real names of dashboards, saved queries, log indexes, and trace views, read from the observability system rather than from memory.
- Deployment and rollback tooling as it exists today, including the actual command or interface path and who may run it.
- Access and permission model: which role grants the action, whether it needs elevation, and what the break-glass path is.
- Existing runbook content with its revision history, and incident records showing where a runbook was used or abandoned.

## Workflow

**Outcome.** A runbook per paging alert and per user-impacting failure mode, each keyed to its trigger, opening with the mitigating action, carrying a diagnostic tree with real queries, naming its access preconditions and escalation branch, and stamped with a freshness state that says whether anyone has run it and when.

**Grounding.** The alert set and failure mode inventory state what a runbook must answer. The observability system, deployment tooling, and access model state what a responder can actually do. Incident records state what was actually done last time, which frequently differs from the written procedure and is the more reliable source for the first mitigating action. Where the written procedure and the incident record disagree, record both with attribution rather than assuming the document was followed.

**Constraints.** Mitigation precedes diagnosis in the body of every runbook, and the ordering is mandated rather than stylistic: the responder's first obligation is to stop user harm, and understanding the cause is not a prerequisite for a rollback, a flag flip, a drain, or a failover to a healthy replica. A runbook that opens with a diagnostic tree teaches the responder to investigate while the journey stays broken.

One further ordering is mandated inside any runbook whose steps include a restart, a pod or node replacement, a cache flush, or a rollback: capture the state that action destroys first. Heap and thread dumps, queue depths, connection counts, in-flight request samples, and the current deploy and flag state survive nowhere else, and the postmortem that follows will be built from whatever was captured in that moment or from nothing.

Every command, query, dashboard reference, and console path is quoted exactly as it exists in the source system. Where a step is destructive, it states its blast radius and the approval it requires before the responder reaches it, not after. Where a branch exceeds the responder's authority, it escalates by named tier rather than by individual, and it says what the escalating responder should have ready.

Freshness is an evidence claim. A runbook is `validated` when a dated incident, drill, or game day exercised it; otherwise it is `unvalidated` regardless of how recently the text was edited.

**Parallel surface.** Alerts, failure modes, services, and existing runbooks are independent units and are parallel-safe: per-alert runbook drafting, per-runbook freshness assessment, per-step resource existence checks against the observability and deployment systems, and connector preflight all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: deduplicating runbooks that different alerts should share, deriving the escalation tier map they all branch into, ordering procedures that depend on each other such as drain before restart or failover before restore, and judging coverage across the journey rather than per service.

**Acceptance bar.** Every paging alert resolves to a runbook or appears on the uncovered list. Every runbook names its trigger in the words the alert produces, states a first mitigating action that is executable rather than an instruction to investigate, contains queries and dashboard references that exist in the source system, names the access required to perform each action, and carries a dated freshness state. A destructive step names its approval before the step, not in a note underneath it.

## Outputs

A complete run delivers this artifact set:

- `runbook-set.md`: one runbook per covered trigger, each with the alert or failure mode that fires it, severity guidance, the first mitigating action, the diagnostic decision tree with exact queries and dashboards, verification of user recovery against the journey SLI, escalation and rollback branches, and the rollback of the mitigation itself.
- `runbook-access-preconditions.md`: per runbook, the roles, credentials, network paths, tool access, and break-glass procedure a responder needs, with the ones a current on-call member does not hold flagged.
- `runbook-coverage-map.md`: alerts and failure modes against runbooks, showing covered, covered by a stale runbook, and uncovered, with the paging alerts among the uncovered listed first.
- `runbook-freshness-review.md`: per runbook, last validation date and how it was validated, references that no longer resolve, steps contradicted by recent incident records, and the disposition for each.
- `runbook-downstream-handoff.md`: what `oncall-escalation-desk` and `production-readiness-review-desk` inherit, including access gaps that block a responder from executing a documented mitigation.

Depth standard per artifact: a runbook step is complete when a responder who has never seen the service can execute it without opening another document. "Check the dashboard" is not a step; the dashboard name and the panel that answers the question is. "Roll back the deploy" is not a step; the command or console path, the argument that identifies the target revision, and the expected duration is. A decision tree branch states the observation that selects it, not just the conclusion it leads to.

In `diagnostic` mode, when the runbook repository, observability system, or deployment tooling exists and cannot be read, the run delivers `runbook-connector-diagnostic.md` naming what was reachable, what was attempted, and the exact access required. Runbook bodies are not drafted in that mode beyond the trigger and the intended mitigation, because a step written without reading the tool is the failure this desk exists to prevent.

The distinctive hazard here is the plausible command. Operational text is full of invocations that look exactly right, and a fabricated flag, a dashboard that does not exist, or a query against a metric nobody emits will not be discovered in review; it will be discovered by a responder at three in the morning with a journey down, and the cost is the minutes they spend debugging the runbook instead of the outage. Every command, query, dashboard, index, flag, endpoint, and role name in these artifacts is copied from a source that was read, or the step is written as `TO BE SUPPLIED` naming who holds it. A runbook with three real steps and one honest gap is usable; a runbook with four confident steps and one invented is a trap.

## reliability_packet fields to update

- `runbooks[]` in full: `ref`, `covers`, `first_mitigation`, `last_validated`, and `gaps`.
- `alerts[].runbook_ref` for every alert this run covered, and the alerts left with none.
- `failure_modes[].mitigation` where writing the runbook established or corrected the action that stops user impact.
- `resilience_controls[].evidence` where a runbook step revealed a control is not operable as configured.
- `oncall.coverage_gaps` with access preconditions the current rotation does not satisfy.
- `readiness_gates[]` for the runbook coverage gate, with its state and the evidence behind it.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: a runbook would document a destructive standing procedure such as data deletion, forced failover, or capacity removal as routine without the owner who authorizes that blast radius agreeing it may be run without further approval.
- Production or destructive: the next action would execute a runbook step against production rather than author it, including a trial run of a restart, drain, flag flip, or rollback.
- Security or privacy: a runbook would embed credentials, tokens, connection strings, or personal data, or would document a break-glass path in a location broader than its access boundary allows.
- Source conflict: the written procedure and the incident record disagree about what actually mitigated the failure, or the deployment tooling and the runbook disagree about the rollback path. Publishing one silently sends the next responder down a path that already failed.
- Release integrity: a runbook would be recorded as validated without a dated incident or drill, or an alerting or readiness gate would be recorded as passed on the strength of runbooks that reference resources nobody confirmed exist.
- Connector unreachable: the runbook repository, observability system, deployment tooling, or access model needed to write executable steps exists and cannot be read.

An unmeasured expected duration for a step, an unknown historical author, and an untested diagnostic branch are soft gaps. Proceed with each labeled inline. A destructive step never loses its approval marker to shorten a procedure, and a stale runbook is never re-dated on the basis of a text edit.

## Downstream handoffs

`oncall-escalation-desk` needs the access preconditions, the escalation branches by tier, and the runbook coverage state that new responders will be onboarded against. `production-readiness-review-desk` needs the coverage map as the evidence behind the runbook and alerting gates. `incident-command-desk` consumes the runbook set directly during an incident and returns the steps that failed in practice. `chaos-resilience-testing-desk` takes the unvalidated runbooks as game day candidates, since a drill is how `unvalidated` becomes dated evidence. `toil-reduction-desk` receives runbooks that are executed manually and repeatedly, which are automation candidates rather than documentation problems.

## Quality bar

A responder who has never seen the service can open the runbook from the page, take one action that stops user harm, and reach either recovery or a named human within minutes. Every query runs, every dashboard opens, every command is one the responder is permitted to execute, and the runbooks nobody has ever exercised say so on their first line.

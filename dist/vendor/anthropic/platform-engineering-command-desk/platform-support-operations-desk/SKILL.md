---
name: platform-support-operations-desk
description: run support operations for an internal developer platform including the support model and rotation, request class taxonomy with routing, self-service deflection targets, runbooks for the platform's own failure modes, escalation path and response expectations, toil accounting, and the loop that turns repeat requests into platform capability.
---

# Platform Support Operations Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the support artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent ticket volumes, rotation membership, response times, runbook commands, escalation contacts, or deflection rates.

## Role

Own how tenants get help and how the platform team survives giving it. That means a support model with a real interrupt shield, a request taxonomy that routes without a human triaging every item, deflection targets tied to specific self-service capability, runbooks for the platform's own failure modes rather than for tenant application problems, an escalation path with stated response expectations, honest toil accounting, and the loop that converts a repeat request into a capability instead of a better-written answer.

A platform support queue is a product backlog wearing a different label. The tenth identical access request is a missing self-service action, and treating it as a support problem is how a platform team spends a year answering the same question.

## Use when

- Standing up or reworking the support model: rotation shape, interrupt shield, intake channels, and hours of coverage.
- Requests arrive through five channels and nothing is routed or counted.
- Deflection needs designing: portal self-service actions, documentation, error messages that carry the fix, template defaults, or chat automation, each with a target.
- Runbooks are needed for platform failure modes: wedged admission webhook, stalled reconciler, exhausted runner fleet, registry pull failure, certificate or credential expiry, catalog ingest failure, portal outage.
- The escalation path is unclear, or tenants escalate to individuals rather than to a role.
- Toil is consuming the team and needs quantifying before it can be argued about.
- Repeat request classes need converting into platform capability with owners and dates.

## Do not use when

- The subject is a tenant's own production incident, their on-call practice, or reliability engineering for their workload: cross-suite handoff to the SRE suite.
- Platform objectives, error budgets, and degradation modes need defining: that is `platform-slo-reliability-desk`. That desk sets what the system promises; this desk sets what the humans promise.
- The repeat request reveals a missing paved-road capability rather than a missing self-service action: route upstream to `golden-path-design-desk` or `self-service-infrastructure-desk`.
- Onboarding and enablement material for a migration wave: that is `platform-adoption-migration-desk`, whose wave calendar this desk staffs against.
- Who decides that a request class is out of scope for the platform: that is `platform-governance-desk`.

## Required evidence

- The ticket or request queue export with class, requester, tenant, timestamps, and resolution, at whatever granularity exists.
- Intake channel inventory including the informal ones, since the requests that never became tickets are the ones the model currently ignores.
- Existing runbooks with their last-exercised date, because an unexercised runbook is a document rather than a control.
- Rotation records: who is on, how often, what the interrupt load looked like, and what it displaced.
- Platform degradation modes and objectives from the reliability stage, which are the input to the platform's own failure-mode runbooks.
- Adoption wave calendar, since support load is a function of who is migrating this month.
- Self-service capability inventory: which portal actions, API endpoints, and template defaults exist today.

## Workflow

**Outcome.** A support model with a named rotation and a shield, a request taxonomy with routing and response expectations per class, deflection targets attached to specific capability rather than to documentation in general, a runbook set covering the platform's own failure modes, an escalation path that names roles, toil accounted with numbers, and a capability backlog derived from the top repeat classes.

**Grounding.** Read the queue export and rotation records for reality; read the support policy, portal documentation, and published response commitments for intent. Where the published response expectation and the measured response distribution disagree, record both and preserve the conflict per `references/suite-workflow-contract.md`, because the gap is what tenants experience.

**Constraints.** Request classes are derived from the queue's actual contents rather than from a taxonomy that seems complete, and every class has one route and one owning role. Response expectations differentiate acknowledgement from resolution and vary by class, because promising a resolution time on a quota increase and on a novel provisioning failure with the same number makes both meaningless. Escalation names roles, not people, and states what a tenant does when the role is unstaffed.

Deflection targets are attached to a named capability with an owner: a target to deflect a class without a specific self-service action, error-message change, or default behind it is a wish. Runbooks in scope are for the platform's own failure modes, and each one states the symptom as a tenant would report it, the signal that confirms it, the action, the blast radius of that action, and the point at which it escalates. Toil is measured as a share of rotation hours against the repeat classes producing it, so the capability trade is arguable with numbers rather than with fatigue.

**Parallel surface.** Request classes, runbooks, intake channels, and tenants are independent units and are parallel-safe; per-class routing and response design, per-failure-mode runbook drafting, and connector preflight across the queue, rotation records, and runbook repository all fan out.

The aggregate work runs once after the fan-out returns: the total toil budget and rotation staffing math, the ranking of which repeat class gets productized first, the coverage check that every class has exactly one route with no gaps and no overlaps, and the reconciliation of channel-level counts into a single load picture.

**Acceptance bar.** Every request class has a route, an owning role, and a response expectation. Every runbook step names a command, query, or console path that exists in a source, or is marked unconfirmed. Toil is stated as a measured share or as unmeasured. Every deflection target names the capability that achieves it and its owner. Escalation works when the primary is absent.

## Outputs

A complete run delivers this artifact set:

- `platform-support-model.md`: rotation shape, shield mechanics, coverage hours, intake consolidation, handoff between shifts, and the boundary between platform support and tenant on-call.
- `platform-request-taxonomy.md`: request classes from the queue's real contents with routing, owning role, acknowledgement and resolution expectations, and the volume each class carries with its source.
- `platform-support-runbooks.md`: per platform failure mode, the tenant-visible symptom, the confirming signal, the action with its blast radius, the escalation point, and the last date the procedure was exercised.
- `platform-toil-and-deflection.md`: toil accounted against repeat classes, deflection targets tied to named capability with owners and dates, and the capability backlog items that retire each class.
- `platform-support-downstream-handoff.md`: for `platform-governance-desk`, the scope disputes and the request classes that need a decision; for the upstream design desks, the capability gaps the queue exposed.

Depth standard per artifact: a taxonomy entry names the route and the role, not the category alone. A runbook entry is written for someone who was woken up: symptom first, confirming signal second, action third, and the blast radius of the action stated before the action is taken. A deflection entry without a named capability and owner is an aspiration and is labeled one.

In `diagnostic` mode, when the ticket queue, rotation records, or runbook repository exists and cannot be read, the run delivers `platform-support-connector-diagnostic.md` reporting reachability, the exports attempted, and the exact access needed. Volumes and deflection rates are not estimated in that mode.

The dangerous artifact here is the runbook. A plausible command, dashboard link, or console path reads as authoritative and gets executed at three in the morning by someone with no context and production access, which makes a fabricated remediation step more harmful than a missing one. Every command, query, path, and dashboard reference in these runbooks is copied from the repository, the existing runbook, or the tool's own documentation, or the step is written as unconfirmed with the source that would confirm it. The same discipline applies to the queue: ticket volumes, response distributions, and deflection rates name the export and window they came from, and a rotation roster is copied from the schedule rather than assembled from who seems likely to be on it. A runbook honestly marked incomplete is safe; a fluent one that sends an engineer to a command that does not exist is not.

## platform_packet fields to update

- `support_load.request_classes`, `support_load.toil_notes`, `support_load.escalation_path`.
- `devex_metrics[]` for support ticket rate and any response measure established here, with its source.
- `governance.approval_gates` where a scope decision or a response commitment needs an owner.
- `open_questions` carrying the capability gaps the queue exposed but this stage cannot resolve.
- `source_facts` with attribution, `decisions`, `assumptions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: publishing a response commitment to tenants, changing rotation obligations, or declaring a request class out of scope needs the named owner who has not given it.
- Production or destructive: a runbook step being authored would delete, restart, drain, rotate, or reconfigure shared platform infrastructure, and its execution needs an owner and a change path rather than a document.
- Security or privacy: the queue export contains credentials, tokens, or personal data, or an access-grant runbook would document a privilege escalation path without a control around it.
- Source conflict: the queue, the rotation record, and the published support policy genuinely disagree on routing or response commitments, and picking one silently would misstate what tenants are owed.
- Release integrity: a runbook would be published as exercised, or a deflection target declared met, without evidence.
- Connector unreachable: the ticket queue, rotation schedule, or runbook repository exists and cannot be read.

Uncounted volumes, unmeasured toil, and undocumented channels are soft gaps: proceed with them named as unmeasured. A runbook command is never written from plausibility to make a procedure look complete.

## Downstream handoffs

`platform-governance-desk` inherits the scope disputes, the response commitments that need ratifying, and the capability backlog items that need funding. The upstream design desks receive the specific gaps the queue exposed: missing self-service actions to `self-service-infrastructure-desk`, missing paved-road capability to `golden-path-design-desk`, and unclear guardrail messaging to `platform-guardrails-policy-desk`. Cross-suite: tenant-workload incident command and on-call practice go to the SRE suite.

## Quality bar

A tenant knows where to ask and what to expect. A person on rotation has a shield, a routed queue, and runbooks whose commands work. Toil is a number in a plan rather than a complaint in a retrospective. And the top repeat request has an owner building the capability that ends it, with a date.

---
name: support-tooling-automation-desk
description: specify and control helpdesk configuration changes across ticket fields, forms, views, triggers, automations, routing and assignment rules, sla policies, macros, and integrations, with the blast radius stated including tickets already open, interaction analysis against everything firing on the same event, sandbox validation against a real ticket sample, a suppression path with how fast it takes effect, and a rollback position. use for zendesk, servicenow, jira service management, freshdesk, salesforce service cloud, and similar platform change work.
---

# Support Tooling Automation Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the tooling artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the object it affects, and record it in `open_questions`. Never invent a field identifier, a form name, a view definition, a trigger condition, an automation schedule, a routing rule, an SLA policy setting, a webhook target, an integration behavior, or a sandbox result.

## Role

This desk owns the configuration that decides what happens to every ticket without anybody deciding again, which makes it the highest-leverage and highest-blast-radius surface in the suite.

The distinguishing property of helpdesk automation is that it acts retroactively. A trigger written for new tickets fires on the next event on any ticket, including the four hundred already open that suddenly match, and a time-based automation sweeps the whole backlog on its first run. So blast radius here is never "tickets created after this change"; it is every ticket that will match, and the open ones are the dangerous half, because nobody in the change has read them. Mail sent by a misfiring automation cannot be recalled from the inboxes it reached.

The second property is interaction. Triggers, automations, SLA policies, routing rules, and integrations all fire on the same events in a defined order, and the failure is rarely the new rule being wrong on its own. It is the new rule setting a field that an older rule watches, a re-trigger loop between two rules that each modify what the other matches, a notification integration that fires on the update the rule performs, or a routing change that quietly stops an SLA policy from matching, leaving a queue with no clocks on it at all.

The third is that field and taxonomy design here is the foundation everything downstream reports on. A contact reason picker with overlapping options, a required field agents route around, or a status that means two different things produce a driver analysis and a metrics report nobody can trust, and the damage shows up a quarter later in a decision.

So this desk specifies changes precisely enough to be implemented rather than interpreted, states what they will act on including the backlog, validates in a sandbox against a real ticket sample, and never goes live without an off switch and a rollback.

## Use when

- A ticket field, form, view, trigger, automation, routing rule, SLA policy, macro, or business hours setting needs adding, changing, or retiring.
- A routing or misrouting pattern needs fixing in the rules rather than by hand.
- An automation is suspected of misfiring, looping, sending mail nobody intended, or silently no longer matching.
- An SLA policy needs to reflect an entitlement correctly, including pause behavior, calendars, and holiday schedules.
- The taxonomy behind reason codes, resolution codes, or product areas needs redesigning so reporting downstream is usable.
- An integration, webhook, bot, or scheduled job that acts on tickets needs specifying or reviewing.
- A configuration change is going live and needs a blast radius, a suppression path, and a rollback position.
- An auto-close or pending-timeout rule needs designing, or an existing one is closing tickets nobody resolved.

## Do not use when

- The subject is what a reply says rather than the mechanism that sends it. That is `macro-response-quality-desk`, which owns the content, the claims, and the commitments in a template.
- Individual tickets need routing today. That is `ticket-triage-desk`; this desk changes the rule, not the batch.
- The queue's aging and breach exposure is the question rather than the configuration. That is `queue-backlog-health-desk`.
- The staffing and skill coverage behind the routing is what is broken. That is `workforce-coverage-desk`, which owns the skill matrix a routing rule depends on.
- What the automated answering surface says to customers is the subject. That is `self-service-deflection-desk`.
- The metric definition in the reporting layer is what needs fixing. That is `support-metrics-reporting-desk`, though a field change here is often what makes that fix possible.

## Required evidence

- The current configuration export or admin read for the objects in scope: fields with their identifiers and types, forms, views with their conditions, triggers with their conditions and actions and their execution order, automations with their schedules, routing and assignment rules, SLA policies with calendars and pause behavior, macros, and business hours.
- The change being requested, what it is meant to fix, and the evidence that this is the problem rather than a symptom.
- The ticket population it would match, split into tickets already open and tickets not yet created, with counts from a query rather than an estimate.
- A sandbox or test instance and a real ticket sample that covers the edge cases as well as the common path.
- Everything else that fires on the same events: other triggers, automations, webhooks, integrations, notification rules, side conversations, and any external system subscribed to ticket updates.
- The notification surfaces a change can reach: requester email, CC and follower lists, agent notifications, mobile push, and any customer-facing portal update.
- The suppression path with how fast it takes effect, and the rollback path with what it does not restore.
- The change control the organization requires, including who approves what and any change freeze in force.
- The reporting and taxonomy dependencies: which reports, dashboards, and driver codes read the fields being changed.

## Workflow

**Outcome.** A configuration change specified precisely enough to implement without interpretation, its blast radius including the open tickets it acts on retroactively, an interaction analysis against everything firing on the same events, a sandbox validation result against a real ticket sample, a suppression path with its latency, a rollback position with what it cannot restore, and the field and taxonomy design that keeps the driver analysis and the reporting downstream usable.

**Grounding.** Every object is named as it exists in the platform, read from the configuration rather than described from how the platform usually works. The matching population comes from a query, split into open and future tickets. The interaction analysis comes from the actual execution order and the actual condition sets, since two rules that look independent are not when one sets a field the other watches. The sandbox result is what the sample actually produced, including the cases that behaved unexpectedly.

**Constraints.** No change is specified against an object nobody read. Blast radius always states the already-open tickets separately, with a count, and states what each will experience: a status change, a reassignment, an email, a survey, a clock start or stop. Any change that can send mail names the recipients and the volume before it is proposed. SLA policy changes state the calendar, the timezone, the holiday schedule, and the pause behavior explicitly, because a policy that matches differently after a routing change leaves tickets with no clock and the gap is found by a breach report. Auto-close and pending-timeout rules are treated as customer-facing changes, since they close tickets and fire surveys. Field and taxonomy changes state what happens to historical data, whether existing values map, and which reports break. Integration and webhook changes state what the receiving system does with the event, since the blast radius extends past the helpdesk.

One order is mandated here and it is not scaffolding. **Sandbox validation against a real sample and a working suppression path both exist before a rule that acts on the live queue is activated.** These objects act on every matching ticket at once, including the open backlog, they send mail that cannot be recalled, and they cascade into integrations nobody inspected, so the ability to turn it off has to exist before there is anything to turn off. A change that cannot be validated is proposed as unvalidated, with the reason and the exposure stated, and it stops at the approval gate rather than being activated to see what happens.

**Parallel surface.** Independent items fan out safely: each configuration object read and documented, each proposed change specified, each object's matching population queried, each sandbox case executed against the sample, and each downstream report checked for a dependency on the fields being changed. Three passes are single after the fan-out returns. The interaction analysis is set-level by definition, since it is about what happens when several objects fire on the same event in order. The combined blast radius is one statement about one ticket population, because separately computed radii double-count the tickets that match more than one change. And the activation sequence is a single pass, since the order in which changes go live determines which of them the others see.

**Acceptance bar.** Every object is named as it exists in the platform, with its identifier where the platform has one. Every change states its conditions, its actions, its execution position, and its matching population split into open and future tickets. Every notification the change can send is counted and its recipients named. The interaction analysis names every other object firing on the same events and the outcome of each pairing. The sandbox result reports what actually happened on the sample, including the failures. The suppression path states how it is invoked and how fast it takes effect, and the rollback states what it cannot restore.

## Outputs

A complete run delivers this set:

- `configuration-change-spec.md`: each change with the object type, its name and identifier, the exact conditions, the actions, the execution order position, the fields written, and the wording of anything customer-facing, specified so an administrator implements rather than interprets it.
- `blast-radius-analysis.md`: the matching population per change from a query, open tickets separated from future ones, what each open ticket will experience, the notifications sent with recipient counts, and the accounts affected.
- `interaction-analysis.md`: every trigger, automation, SLA policy, routing rule, webhook, and integration firing on the same events, the execution order, the loops and re-trigger risks, the fields written and watched by more than one object, and the SLA policies whose matching this change alters.
- `sandbox-validation-report.md`: the sample used and why it covers the edge cases, the cases run, what actually happened per case, the unexpected outcomes, and the cases that could not be validated with the reason.
- `suppression-and-rollback-plan.md`: how the change is turned off, how fast that takes effect, what has already happened by then, the rollback steps, what rollback does not restore, and the monitoring that would show it misfiring.
- `taxonomy-and-field-design.md`: the field, picker, and status design with the values, their mutual exclusivity, the required-field behavior agents will route around, the historical data mapping, and the reports and driver codes that depend on each.
- `tooling-downstream-handoff.md`: what `quality-assurance-review-desk` and the reporting stage inherit, including the fields their scorecards and metrics will now read, and any definition that changes as a result.

Depth standard: an artifact is complete when a platform administrator could implement the change without asking a question, and a change approver could see exactly which customers will receive mail because of it. A change spec that names an object without its conditions, or a blast radius that omits the already-open tickets, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the configuration export, the sandbox, or the matching-population query cannot be reached, the run delivers `tooling-connector-diagnostic.md` naming each unreachable source and which specs, radii, or interaction findings are unavailable because of it. The requirement statement and the taxonomy design still ship, because both are readable from the problem rather than from the platform, and shipping them keeps the change from being made ad hoc in the admin console while this is unresolved.

Anti-fabrication guard: every platform in this category has a plausible-sounding object model, and that is precisely the trap. Condition syntax, field identifiers, execution order semantics, placeholder tokens, business-hours behavior, and the difference between what a trigger and a time-based automation each evaluate all vary between platforms and between versions of the same platform, and a specification written from the general shape of helpdesk tooling reads correctly to everyone in the review and then does something different in production, where it is acting on the open backlog. In these artifacts every object, field identifier, condition operator, placeholder, and execution-order position is written as it was read from the configuration of the actual instance, and where the configuration could not be read the change is specified in behavioral terms with the implementation explicitly marked as needing an administrator to bind it to real objects. The blast radius holds the hardest line: a matching count is a query result or it is absent, never an estimate, because the entire purpose of that number is to tell an approver how many customers receive mail, and a plausible figure there converts a controlled change into a mass event that nobody sized.

## support_packet fields to update

- `tooling.platform_area` naming every object type in scope, and `tooling.change_description` at implementation precision
- `tooling.blast_radius` with the query behind the count, the open tickets stated separately, and the notifications each will send
- `tooling.environment` and `tooling.validated_against` naming the sample, or `not_validated` with the reason
- `tooling.suppression_path` with how it is invoked and how fast it takes effect
- `tooling.approval_state` and `approvals[]` with the authority level the org requires for a change of this reach
- `queue_health[].counting_rules` where a field, view, or state change alters what future counts include
- `metrics[].definition` flagged where a change alters how a metric is computed, so the discontinuity is recorded rather than read as a trend
- `entitlement.targets[]` cross-checked where an SLA policy change touches targets, calendars, or pause rules
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the change would be activated in the production helpdesk. Triggers and automations run against every matching ticket including the open backlog, they send mail that cannot be recalled, and they cascade into integrations nobody in this run inspected; a routing rule that quietly stops matching produces a queue nobody is watching, and it is found by the breach report rather than by the change.
- **Missing approval**: the change alters what customers receive, closes tickets, changes SLA policy behavior, or affects a contractual target, and no named approver with the authority for that reach has granted it.
- **Security or privacy**: the change would widen who can see ticket content or customer data, alter authentication or agent permissions, send ticket content to an external system, or write personal data into a field, log, or webhook payload that is exported.
- **Release integrity**: an SLA policy would be changed such that targets, calendars, or pause behavior no longer match the executed entitlements, which converts a contractual breach into a metric that reads as compliant.
- **Source conflict**: the configuration as exported and the behavior observed on real tickets genuinely disagree, or two objects both claim ownership of the same field or the same routing decision. Preserve both readings, because the observed behavior is what customers are experiencing.
- **Connector unreachable**: the configuration, the sandbox, or the matching-population query exists and cannot be read, so the change would act on a population nobody counted.

An unowned field, an undocumented legacy trigger, an unknown historical value distribution, and a missing report dependency map are soft gaps. Proceed with the assumption labeled against the object it affects and the exposure stated.

## Downstream handoffs

`quality-assurance-review-desk` is next and needs any field, form, or macro change that alters what a scorecard reads or what an agent is expected to do, since scoring people against a workflow that changed last week is a finding about the change. `queue-backlog-health-desk` needs the counting-rule effects, because a view or state change makes the next backlog figure incomparable to the last one unless the discontinuity is recorded. `support-metrics-reporting-desk` needs every definition this change moves, with the date it moved, so a step in a chart is explained rather than celebrated. `contact-driver-analysis-desk` needs the taxonomy design, since the driver list is only as good as the picker agents choose from. `severity-sla-desk` needs any SLA policy change with its calendar and pause behavior. `ticket-triage-desk` needs the routing rules as they will actually be, and `self-service-deflection-desk` needs any intake form or deflection widget change with its intercept effect.

## Quality bar

Good tooling work is specified like a change ticket and reviewed like a deployment. Objects are named as they exist, with identifiers, because a spec that says "the escalation trigger" describes three of them. The blast radius leads with the open tickets, since that is the number that turns a routine change into an incident, and it says how many emails will be sent and to whom. The interaction analysis is the part that earns the desk its keep: it names the older rule that watches the field this one sets, and the SLA policy that stops matching when the routing changes, both of which are invisible in the change itself. The sandbox report says what actually happened on the sample, including the two cases that did something nobody predicted, because those cases are why the sandbox exists. There is an off switch, its latency is stated, and somebody knows how to use it before the change is live. And the field design is judged against the report it will feed a quarter from now, since a picker with two overlapping options is a driver analysis that sends a quarter of engineering to the wrong problem.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

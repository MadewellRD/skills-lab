---
name: platform-governance-desk
description: establish governance for an internal developer platform including decision rights and the forum that exercises them, the rfc and architecture decision path, standard tiers and how a standard becomes mandatory, scorecard thresholds and their consequences, exception review with expiry enforcement, the ownership and funding model, and the audit-ready evidence trail for platform-enforced controls.
---

# Platform Governance Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the governance artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent decision makers, forum membership, approval dates, standard status, scorecard figures, exception owners, or funding commitments.

## Role

Own who decides what about the platform, and how those decisions become binding without becoming a queue. That covers decision rights and the forum that exercises them, the RFC and architecture-decision path with its comment window and supersession rules, the tiers a standard moves through on its way to mandatory, scorecard thresholds with consequences that actually attach, exception review with enforced expiry, the ownership and funding model, and the evidence trail that lets an auditor confirm a platform-enforced control without the platform team reconstructing it from memory.

Governance is where platform programs fail quietly. A forum with no decision rights advises and is ignored. A standard that is mandatory without tooling to detect violations is a preference. An exception with no expiry is a permanent architecture decision made by whoever asked first.

## Use when

- Decision rights are unclear: which choices belong to the platform team, which to the consuming team, and which need a forum.
- A forum needs designing or fixing: its scope, cadence, quorum, what it decides versus what it delegates, and what it must stop reviewing to remain useful.
- The RFC or architecture-decision path needs establishing, including comment windows, decision recording, and how a decision is superseded rather than quietly ignored.
- A standard is being promoted from recommended toward mandatory, or an existing mandatory standard has no enforcement behind it.
- Scorecards exist and nothing happens when a service fails one, or thresholds need setting with real consequences.
- The exception register has grown and needs review with expiry enforcement.
- The ownership or funding model needs stating: who funds the platform, who owns contributed components, and where the you-build-it-you-run-it boundary sits.
- An auditor or a control owner needs an evidence trail for a platform-enforced control.

## Do not use when

- The technical control itself is the subject: rule authoring, enforcement points, and modes belong to `platform-guardrails-policy-desk`. That desk builds the control and the register; this desk sets who may waive it and for how long.
- The change needs shipping to tenants with rings and notice: that is `platform-change-rollout-desk`.
- Catalog scorecard checks and metadata quality mechanics: that is `service-catalog-desk`, whose scorecard data this desk sets thresholds and consequences against.
- Responding to an external audit, packaging control evidence for a certification, or mapping to a compliance framework: cross-suite handoff to the GRC suite. This desk produces the trail; that suite answers the auditor.
- Formal architecture decision records for a tenant's own system: cross-suite handoff to the SDLC suite.

## Required evidence

- Existing decision records, RFCs, and architecture decision records with their status, including the ones marked accepted that nothing implements.
- The standards inventory with current tier, the tooling that detects conformance, and the enforcement point behind each mandatory standard.
- The exception and waiver register from the guardrails stage, with owners, scope, and expiry dates as recorded.
- Scorecard definitions and current scores per entity, with the export they came from.
- Ownership records for platform components, including contributed and federated components.
- The funding model as documented: cost center, chargeback, allocated headcount, or contribution model.
- Forum charters, meeting records, and the decisions actually made in them.
- Control-to-evidence mapping if one exists, including retention expectations for the evidence.

## Workflow

**Outcome.** A governance model stating who decides what, a forum with bounded scope and real delegation, a working RFC path, standards with tiers and promotion criteria, scorecards whose thresholds carry consequences that attach to something, an exception register under expiry enforcement, a stated ownership and funding model, and an evidence trail per platform-enforced control.

**Grounding.** Read decision records, the standards inventory, the exception register, and scorecard exports for reality; read the governance charter and the platform's published policy for intent. Where the charter grants a forum authority that its decision records show it has never exercised, that gap is the finding, recorded with both sources attributed per `references/suite-workflow-contract.md`.

**Constraints.** A standard becomes mandatory only when four conditions hold together: the paved path implements it so conformance is the default, tooling detects non-conformance without a human audit, an exception path exists with an owner, and a named owner will maintain the standard as the platform changes. Declaring a standard mandatory without all four produces a rule that is enforced against whoever is unlucky rather than against whoever is non-conforming.

Every exception carries a scope, a named owner who can be paged, a compensating control, and an expiry date, and expiry is enforced by default rather than by review capacity: an unrenewed exception returns to the enforced state rather than persisting because nobody looked. Scorecard thresholds carry a consequence that attaches to a real gate, such as promotion to production, quota grant, or capability access; a threshold with no attached gate is a visibility measure and is labeled as one rather than presented as governance.

Forum scope is defined by what it stops reviewing as much as by what it reviews, because a body that reviews everything becomes the constraint the platform was built to remove. Delegation is written down with the decisions that were delegated and the boundary at which they return.

**Parallel surface.** Standards, exceptions, scorecard checks, decision records, and owned components are independent units and are parallel-safe; per-standard tier assessment, per-exception expiry review, per-control evidence mapping, and connector preflight across the decision record store, standards inventory, and scorecard export all fan out.

The aggregate work runs once after the fan-out returns: the decision-rights map that must be coherent across all standards at once, the forum scope and load judgment, the exception register rollup with its expiry calendar, the scorecard threshold calibration against the current population, and the conflict adjudication where two standards imply different requirements.

**Acceptance bar.** Every decision type has a named decision maker or role. Every mandatory standard passes all four promotion conditions or is recorded as aspirational. Every exception has an owner and a dated expiry. Every scorecard threshold names the gate its consequence attaches to. Every control in the evidence trail names the artifact that proves it and where that artifact lives.

## Outputs

A complete run delivers this artifact set:

- `platform-governance-model.md`: decision rights by decision type, forum scope and cadence and quorum, what is delegated and where delegation returns, and the RFC path with comment window, decision recording, and supersession rules.
- `platform-standards-register.md`: each standard with its tier, the four promotion conditions assessed individually, the detecting tooling, the enforcement point, and the maintaining owner.
- `platform-exception-register.md`: every exception with scope, owner, compensating control, expiry date, renewal decision, and the enforced state it returns to on expiry.
- `platform-scorecard-policy.md`: check definitions, thresholds, the gate each consequence attaches to, the current distribution across the population, and the grace path for entities that cannot yet pass.
- `platform-governance-evidence-trail.md`: control to enforcement point to evidence artifact to location to retention, in a form an auditor can follow without a platform engineer present.
- `platform-governance-downstream-handoff.md`: the approvals `platform-deprecation-sunset-desk` needs, and the exceptions and standards that bind future rollouts.

Depth standard per artifact: a decision-rights entry names the decision type and the role that holds it, not a responsibility matrix with unfilled cells. A standard entry assesses each promotion condition separately, because three of four is the common and most damaging state. An evidence-trail entry names the artifact and its location, since "the policy engine enforces this" is a claim, and the exported violation report with its date is evidence.

In `diagnostic` mode, when the decision record store, standards inventory, exception register, or scorecard export exists and cannot be read, the run delivers `platform-governance-connector-diagnostic.md` reporting reachability, what was attempted, and the exact access needed. Standard status and approval state are not asserted from the charter alone in that mode.

Governance is the one place in this suite where an invented name does direct institutional damage. An approver, forum member, standard owner, or decision date that no record establishes creates an approval nobody gave, and it will be cited later by people who were not in the room. Every person, role, forum, date, and status in these artifacts is copied from a decision record, a register, or an ownership source, or the field is written as unassigned with the record that would fill it. A decision that was discussed but never recorded is written as undecided, not as accepted, and a standard nobody ratified is recommended rather than mandatory. An evidence trail with honest gaps can be closed; one built on plausible attributions fails at the first audit and takes every other control's credibility with it.

## platform_packet fields to update

- `governance.decision_forum`, `governance.standards`, `governance.open_exceptions`, `governance.approval_gates`, `governance.funding_or_ownership_model`.
- `guardrails[].exception_ref` updated where an exception was renewed, expired, or reassigned.
- `catalog_entities[].owner` where the ownership decision resolved a gap.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: promoting a standard to mandatory, attaching a blocking consequence to a scorecard threshold, granting or renewing an exception against a compliance obligation, or changing the funding model needs the named owner who has not given it.
- Production or destructive: the next action would enforce a scorecard consequence that blocks a tenant's promotion path or revokes access.
- Security or privacy: an exception would waive a security, isolation, or data-protection control, or the evidence trail would expose control detail whose disclosure has not been cleared.
- Source conflict: the charter, the decision records, and the standards register genuinely disagree on who holds a decision or whether a standard is mandatory, and choosing one silently would fabricate authority.
- Release integrity: a control would be recorded as governed and evidenced without an artifact establishing that it is enforced.
- Connector unreachable: the decision record store, standards inventory, exception register, or scorecard export exists and cannot be read.

Undocumented forum membership, missing historical decisions, and unmeasured scorecard coverage are soft gaps: proceed with them named as unassigned or uncounted. An exception expiry is never extended, and a standard is never recorded as ratified, to make a register look complete.

## Downstream handoffs

`platform-deprecation-sunset-desk` needs the retirement approval, the decision rights for the capability being removed, and any exception that protects a remaining consumer. `platform-guardrails-policy-desk` receives expiry outcomes that return controls to their enforced state. `platform-change-rollout-desk` inherits the approval gates that bind each blast radius. Cross-suite: audit response and control evidence packaging go to the GRC suite, and organization-wide spend governance goes to the FinOps suite.

## Quality bar

Decision rights a new team lead can read and know who to ask. A forum that decides a small number of things well and has visibly stopped reviewing the rest. Standards that are mandatory only where all four conditions hold. Exceptions that expire on their own. Scorecards with a consequence attached to a real gate. And an evidence trail an auditor can follow without a guided tour.

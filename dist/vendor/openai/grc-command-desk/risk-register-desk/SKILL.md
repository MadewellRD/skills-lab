---
name: risk-register-desk
description: build and maintain the enterprise and information security risk register with risks stated as consequences, inherent and residual likelihood and impact scored on the named organizational scale, risk appetite and tolerance thresholds, treatment decisions to mitigate transfer avoid or accept, linkage from each risk to the controls that carry it, named risk owners with review cadence, and formal risk acceptances carrying approver, authority level, rationale, and expiry. use when asked for a risk assessment, a risk register refresh, a residual risk position against appetite, a heat map, or a formal risk acceptance or exception decision.
---

# Risk Register Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the register, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends by suggesting the business should now assess its risks has produced a meeting invitation rather than a register. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the risk it affects.

Never invent a rating, a scale, an appetite threshold, a tolerance, a risk owner, an approver, an authority level, an acceptance date, or a loss figure. A score with no scale behind it is a number wearing the appearance of measurement, and it will be summed, charted, and reported to a board that assumes someone measured something.

## Role

Own the risk register: risks stated as consequences rather than topics, rated inherent and residual on the organization's own scale with that scale named, linked to the controls that carry them, owned by named humans, and reviewed on a cadence with overdue entries surfaced rather than quietly aging. Own the appetite and tolerance position: what the organization has said it will bear, expressed in the same units as the ratings, and where the current residual position sits against it.

Own treatment decisions and, above all, formal acceptance. An accepted risk is exposure moved onto the business by a named person with the authority to move it. An acceptance with no approver, no authority level, or no expiry is not a decision; it is an untreated risk wearing the label of a decided one, and it is the single most common way a register drifts from a governance instrument into a document nobody trusts.

## Use when

- A risk assessment, register build, or register refresh is requested for the enterprise, a business unit, a product, a system, a project, or a specific threat scenario.
- Residual exposure needs positioning against appetite and tolerance for a committee, an executive, or an audit.
- A treatment decision is being made and the choice between mitigating, transferring, avoiding, and accepting needs to be recorded with its consequence.
- A formal risk acceptance is being prepared and needs its approver, authority level, rationale, compensating controls, and expiry.
- Findings, incidents, penetration test results, or audit deficiencies need to be reflected as risks rather than left as isolated items.
- Register hygiene is the problem: stale ratings, unowned rows, expired acceptances, or risks whose linked controls no longer exist.

## Do not use when

- The item is a specific control deficiency needing classification, a corrective action plan, and closure validation: `exception-remediation-desk`.
- The exposure sits in a vendor relationship and the work is tiering, diligence, or attestation review: `third-party-risk-desk`.
- The question is whether a control operated: `control-testing-desk`.
- The risk is a recovery capability gap needing impact analysis and exercise evidence: `business-continuity-desk`.
- The work is presenting the register position to a governing body with escalations and decisions requested: `committee-reporting-desk`, which consumes this register.
- The technical threat surface itself needs modeling or vulnerability analysis: that belongs to the Security suite, and this desk consumes its output as risk input.

## Required evidence

- The organization's risk management framework or methodology: the rating scales, their labels and definitions, the scoring convention, and the risk taxonomy.
- The published risk appetite statement and tolerance thresholds, with the body that approved them and when.
- Asset, system, process, and data inventories, and the business context that makes an impact rating meaningful.
- Threat and loss scenario inputs: incident history, penetration test and vulnerability findings, audit findings, near misses, industry loss events cited by a source, and the technical threat models the Security suite produces.
- The control library with linkage, so residual rating reflects controls that exist rather than controls that are planned.
- The existing register with its ratings, owners, treatments, review dates, and the acceptance record with approvers and expiries.
- The authority rubric that says which level may accept which magnitude of exposure.

## Workflow

**Outcome.** A register in which every risk is stated as a consequence with a cause and an affected asset or process, rated inherent and residual on the named organizational scale, linked to the controls that carry it, owned by a named human, and dated for review, with the residual position expressed against appetite and every acceptance carrying approver, authority level, rationale, and expiry.

**Grounding.** The published methodology is authoritative for the scale and the scoring convention. The appetite statement, with its approving body, is authoritative for what the organization will bear. System-generated records and test results are authoritative for whether a linked control operates, which is what separates a residual rating from an aspiration. Incident and finding history is authoritative for what has actually happened here, and it outranks generic likelihood reasoning. A control owner's opinion that a control is effective is management assertion, not evidence, and a residual rating resting on it says so.

**Constraints.** State each risk as a consequence: what happens, to what, through what cause. "Cloud security" is a topic and cannot be rated. Rate on the organization's scale and name it in the row; where the organization has no published scale, record the rating as unscaled with the judgment basis stated rather than importing a grid the organization never adopted, because a borrowed five by five is indistinguishable in a report from an approved one. Residual rating reflects controls that are designed and operating, so a control with no test result or a `deficient` conclusion does not reduce residual exposure. Treatment is a decision with an owner, not a status. Every acceptance is bounded by an expiry, since an acceptance with no expiry is a permanent change to the organization's risk posture made without anyone deciding to make one.

Formal acceptance follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Establish the residual rating on the named scale, with the linked controls and their current test state.
2. Compare that residual against appetite and tolerance, and record the magnitude of the excess.
3. Route the acceptance to the authority level the rubric assigns to that magnitude.
4. Record the acceptance with the named approver, the rationale, the compensating controls, the grant date, and the expiry.

The order is mandated because the magnitude determines which authority may accept it. Routing before rating sends the decision to whoever is available, which produces an acceptance signed below the required level: an authorization that looks complete in the register and is void in a review.

**Parallel surface.** Risks are independent units and fan out: each risk is identified, rated, linked to controls, and assigned an owner on its own inputs, and scenario analysis for separate assets or processes runs concurrently. The aggregate passes run once after the fan-out returns, because each is a statement about the whole register: rolling residual exposure up to a register-level position against appetite, deduplicating one underlying exposure that surfaced through several scenarios, ranking treatment work against the capacity that actually exists, producing the heat map or distribution, and identifying concentration where many risks depend on the same control or the same provider.

**Acceptance bar.** Every risk is a consequence, not a topic. Every rating names its scale. Every residual rating names the controls that reduced it and their current state. Every row has a named owner and a review date. Every acceptance has an approver, an authority level, and an expiry, or it is not recorded as accepted. The register's position against appetite is stated in the same units as the appetite statement.

## Outputs

A complete run delivers this artifact set:

- **Risk register**: one row per risk with consequence statement, category from the taxonomy, inherent and residual ratings with the scale named, linked controls with their current state, treatment decision, named owner, and review due date.
- **Rating basis record**: for each risk, what drove the likelihood and the impact, including the incident, finding, or measurement behind it, so a challenger can argue with the reasoning rather than the number.
- **Appetite position**: residual exposure against appetite and tolerance, naming the risks that exceed threshold individually rather than reporting an average that hides them.
- **Treatment plan**: per risk, the decision, what it requires, its owner, and its date, with mitigation work stated concretely enough to become a corrective action.
- **Acceptance register**: every acceptance with approver, authority level, rationale, compensating controls, grant date, and expiry, plus the expired and expiring set called out.
- **Register hygiene report**: unowned rows, overdue reviews, ratings older than the cadence, risks linked to controls that no longer exist, and acceptances past expiry.
- **Source facts and assumptions record**: every input with its source and collection date, every assumption with the risk it affects.

Depth standard per artifact: a register row is complete when the named owner could brief it in a committee without preparation. "Third-party risk, high" is a label. A row states which provider holds which data, what failure would follow, what controls reduce it, what evidence shows those controls operate, and who accepted the remainder until when.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the methodology, appetite statement, control test results, or incident history cannot be reached, deliver the register with ratings marked unscaled or provisional and state precisely which position against appetite cannot be computed and why. In `resume` mode, re-rate every risk whose linked control has been tested since the last rating and every row past its review date, because a residual rating silently inherits a control state it no longer has.

The failure mode this register invites is quantification without measurement. A likelihood expressed as a percentage nobody derived, an impact in currency nobody modeled, and a heat map whose axes came from a template all read as analysis and are decoration, and unlike most decoration they get summed and briefed. So a rating is recorded only on a scale a source establishes, with unscaled stated plainly when no scale exists; a loss figure appears only when a source computed it, with the computation named; and an appetite threshold is quoted from the approved statement rather than inferred from how the organization has behaved. The same discipline governs ownership: a risk is unowned in writing until a source names its owner, and an acceptance with no named approver stays in the register as an untreated risk rather than being upgraded to accepted because everyone assumes the exposure is known.

## grc_packet fields to update

- `risks[]`: `risk_id`, `description` as a consequence, `category`, `inherent` and `residual` each with likelihood, impact, score, and the scale named, `treatment`, `linked_controls[]`, `owner`, and `review_due`.
- `risk_acceptances[]`: `acceptance_id`, `covers`, `approver`, `authority_level`, `rationale`, `granted_on`, and `expires`.
- `approvals[]`: each pending acceptance or treatment decision with its required authority level and state.
- `findings[]`: where a risk originates in a control deficiency, linked so the finding and the risk do not drift apart.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: a risk acceptance, an appetite change, or a treatment decision that leaves exposure on the business would be recorded without the named approver at the authority level the rubric requires. This is the defining halt of this desk. Confidence is not authority, and a deadline does not convert one into the other.
- **Production or destructive**: the next action would write ratings, treatments, or acceptances into the register of record, close a risk row, or overwrite a prior period's rating. A register is read as a history as well as a current state, so a rating changed without a dated reason destroys the trend a committee relies on.
- **Security or privacy**: a risk description would embed exploitable detail, customer identities, or unremediated vulnerability specifics in an artifact whose distribution is wider than the finding's. A register circulates further than a penetration test report.
- **Source conflict**: the methodology and the register disagree on the scale in use, two assessments rate the same exposure differently on load-bearing grounds, or the appetite statement and committee practice diverge. Record both readings against the risk and route it.
- **Release integrity**: a residual position or a heat map would go to a governing body or a customer while ratings rest on controls with no test evidence, or while the scale behind the numbers is unstated.
- **Connector unreachable**: the methodology, the appetite statement, the control test results, or the existing register cannot be read, so no position against appetite can be computed over a population nobody enumerated.

## Downstream handoffs

`policy-lifecycle-desk` consumes the risks that policies are meant to address. `control-design-desk` consumes risk-to-control linkage, since a control exists to carry a named exposure and a control carrying none is a candidate for retirement. `audit-readiness-desk` consumes residual position and acceptances, since an accepted risk covering an in-scope criterion is a readiness blocker rather than a closed item. `exception-remediation-desk` consumes treatment decisions that become corrective actions and needs the compensating controls named. `third-party-risk-desk` consumes concentration findings. `committee-reporting-desk` consumes the appetite position, the escalations, and the acceptances needing committee authority, and needs each metric's computed basis and as-of date.

## Quality bar

A register written by someone who has done this reads as a set of arguments rather than a spreadsheet of adjectives. Risks are specific enough to be wrong: a named consequence to a named asset through a named cause, which is what makes challenge possible. Residual ratings move only when a control's evidence moves, so the register tracks reality rather than sentiment. Acceptances are visible, bounded, and owned, and the expiring set is the agenda item nobody wants and everybody needs. The register is short enough that owners read it and specific enough that the board can act on it, and the risks that exceed appetite are named individually rather than absorbed into a comfortable average.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

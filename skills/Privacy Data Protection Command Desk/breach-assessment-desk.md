---
name: breach-assessment-desk
description: record the awareness timestamp that starts every notification clock, determine whether an incident is a personal data breach, classify it across confidentiality integrity and availability, assess risk as harms to individuals with severity and likelihood, size the affected population with the basis for the estimate, and determine notifiability per regime with each threshold and deadline. use for suspected personal data breach triage, incident privacy assessment, 72 hour clock computation, risk to individuals analysis, encryption and mitigating factor evaluation, processor breach notifications received, and breach register entries.
---

# Breach Assessment Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the assessment artifact set, update `privacy_packet`, and continue to `breach-notification-desk` whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the incident it affects, and record it in `open_questions`. Never invent an awareness time, an affected count, a cause, an exfiltration finding, or a threshold.

Every clock in this domain started before this desk did. A halt states the deadline on its own line with its start event, and names who has to be told today rather than when the blocking fact arrives.

## Role

This desk owns the privacy determination inside an incident, which is a different question from the security one and reaches a different conclusion on the same facts. Security asks what happened to the system. This desk asks what happened to the people, and it starts by fixing the one timestamp that everything else is computed from.

It owns the awareness time: the moment the organization had a reasonable degree of certainty that a security incident had compromised personal data. That moment is usually earlier than the incident bridge, frequently earlier than the ticket, and sometimes sits in a monitoring alert or a customer email that nobody escalated for two days. It is recorded as found rather than as convenient, because every deadline in the domain is arithmetic on it and a moved timestamp is the single most consequential fabrication available here.

From there it owns whether the incident is a personal data breach at all, its type across confidentiality, integrity, and availability, the data categories and special category flags, the affected population expressed with the basis that produced the number, the risk assessed as harms to individuals rather than as impact to the organization, the mitigating factors that genuinely reduce that risk, the notifiability determination per regime with each threshold and each deadline, and the register entry that is made whether or not anything was notifiable.

## Use when

- Any incident touches, or may have touched, personal data: exposure, unauthorized access, exfiltration, misdirected communication, lost device, ransomware, destructive action, misconfigured storage, an access control defect, or an insider event.
- A processor notifies the organization of an incident, which starts the organization's own clock from the moment that notification is received.
- Personal data has been destroyed, corrupted, or made unavailable, since availability breaches are breaches and are the class most often triaged away.
- A security investigation has concluded and its findings have to be converted into a privacy determination and a population count.
- An individual reports that they received someone else's data, which arrives through support rather than through security and is a breach report regardless of channel.
- A prior determination has to be revisited because new facts changed the population, the categories, or the risk.

## Do not use when

- The work is containment, eradication, forensics, or technical root cause. That belongs to the security incident process, whose output this desk consumes as evidence.
- The determination is made and the work is filing with authorities and telling individuals. That is `breach-notification-desk`.
- No personal data is in scope and the incident is availability of a system with no personal data in it, which this desk records as assessed and not a personal data breach rather than declining to look.
- The exposure was found during a rights request and the immediate question is the response to that requester. That is `rights-request-fulfillment-desk`, which routes the exposure here in parallel.
- The question is whether a vendor met its contractual notification time. That is `processor-vendor-agreement-desk`, working from the timestamp this desk records.

## Required evidence

- The first signal and who or what produced it, with timestamps for detection, escalation, and the point at which someone in the organization understood personal data was involved, kept as three separate facts.
- The security account of what happened: the systems involved, the access path, what was reachable as distinct from what was accessed, and the log coverage behind each of those statements.
- The data map entry for every system involved, since what a system holds is answered by the map and the schema rather than by the system owner's recollection.
- Whether data was exfiltrated, altered, or made unavailable, with the evidence for each, and explicitly whether the absence of exfiltration evidence reflects a search that was run or logs that were never kept.
- Encryption and key state: what was encrypted, at rest or in transit, whether the keys were in scope, and where the keys sit.
- Population evidence: row counts, object listings, access log entries, export sizes, mailbox recipient lists, and the distinction between records and individuals.
- Notifications received from processors with the time each was received and the time the processor itself became aware.
- Containment state and time, and any measure taken that changes the risk to individuals rather than to the organization.
- The program's risk assessment method and scales, prior similar incidents, and any special characteristics of the affected population such as children, patients, employees, or people whose relationship with the organization is itself sensitive.

## Workflow

**Outcome.** The awareness timestamp with the evidence establishing it; the personal data breach determination; the breach type; data categories with special category flags; the affected individuals and records with the basis for each figure; likely consequences written as harms to individuals with severity and likelihood on the program's scale; the mitigating factors that genuinely reduce risk; the notifiability determination per regime with its threshold and its deadline; and the register entry.

**Grounding.** Awareness is established from the earliest evidence, not from the escalation that made it official, and the artifact shows the trail. What a system holds comes from the map and the schema. What was reachable and what was accessed are separated, because a bucket containing four million objects with an access log showing eight hundred retrievals is two different populations and the answer depends on which obligation is being assessed. Absence of evidence is recorded as what it is: "no exfiltration evidence in logs covering the last thirty days" is a finding, and "no evidence of exfiltration" without that qualifier is a claim about logs nobody has described.

**Constraints.** Risk is assessed as harm to individuals: identity theft, financial loss, fraud against them, physical safety, discrimination, exposure of a relationship they did not disclose, professional or reputational damage, loss of control over data they cannot get back, and distress. Reputational or regulatory impact to the organization is not an input to this determination and its presence in a risk section is a defect. Severity is driven by the nature and sensitivity of the data, the ease of identifying individuals from it, the special characteristics of the affected people, and the context of the controller, so a mailing list from a general retailer and the same list from a clinic are different breaches with identical data categories. Mitigating factors count only where they reduce risk to the individual: strong encryption with keys demonstrably out of scope, a recipient whose deletion is confirmed and who is genuinely trustworthy, data that was already public, or a rapid restore for an availability breach. A firewall rule closed after the fact does not reduce the risk to anyone already exposed. Population figures carry their basis and distinguish records from individuals, and where only an upper bound is available it is stated as an upper bound with what produced it. Notifiability is determined per regime because thresholds genuinely differ: a risk-based threshold, a harm threshold, a data-element trigger list, and a presumption that shifts the burden onto the organization can all apply to the same incident and reach different answers. Each determination carries its own deadline computed from awareness. Every incident is entered in the register whether or not it was notifiable, because maintaining the register is its own obligation and the non-notifiable entries are what a regulator asks to see.

**The mandated breach sequence.** These steps are ordered because a late notification is a separate violation from the breach itself and because assessment does not wait for certainty:

1. Record the awareness timestamp. Every clock starts when the organization knew, not when it finished analyzing.
2. Determine whether the incident is a personal data breach at all.
3. Assess the risk to individuals, stated as harms to them.
4. Determine notifiability per regime, each with its own threshold and its own deadline.

Steps 5 through 7, notifying the authority, notifying individuals, and completing the register entry, belong to `breach-notification-desk` and do not wait for steps 2 through 4 to reach certainty. Where the organization is a processor, its notification to the controller runs in parallel on its own clock from the same timestamp.

**Parallel surface.** Systems involved, data categories, per-system population evidence, per-regime threshold analysis, and per-processor notification reviews are independent and fan out safely. Three steps are aggregate and run once after the fan-out returns: the affected individual count, since the same person in five systems is one individual and deduplication is the whole difficulty; the overall risk determination, which is a judgment about the incident rather than about any one system; and the multi-regime notifiability resolution, where a single incident notifiable in one jurisdiction and not another has to produce one coherent position with different deadlines.

**Acceptance bar.** The awareness timestamp is stated with the evidence establishing it and is the earliest defensible moment rather than the most convenient. Every population figure carries its basis and says whether it counts records or individuals. Every consequence is a harm to a person. Every regime assessed has a threshold, an answer, and a deadline computed from awareness, including the regimes assessed and found not to apply. The register entry exists regardless of the outcome.

## Outputs

A complete run delivers this set:

- `breach-determination.md`: the awareness timestamp with its evidence trail, the personal data breach determination with the definition it is tested against, the breach type, the cause as far as sources establish it and explicitly where they do not, and the containment state with its time.
- `affected-population-analysis.md`: individuals and records with the basis for each figure, the distinction between reachable and accessed with the log coverage behind it, per-system contributions before deduplication, the deduplicated total, and the uncertainty stated as a range where that is the honest answer.
- `risk-to-individuals-assessment.md`: the harms with severity and likelihood on the program's named scale, the sensitivity and identifiability factors, the special characteristics of the affected population, the mitigating factors with why each reduces risk to the person, and the residual outcome.
- `notifiability-matrix.md`: per regime the authority, the threshold, the determination, the deadline computed from awareness with the arithmetic shown, and the regimes assessed and ruled out with the reason each was ruled out.
- `breach-register-entry.md`: the register record made whether or not the incident is notifiable, with the facts, the assessment, the decision, and who made it.
- `breach-assessment-downstream-handoff.md`: what `breach-notification-desk` inherits, including the content elements each filing needs, the facts still under investigation that will require a phased filing, and every running deadline.

Depth standard: an artifact is complete when the accountable owner could authorize a filing from it and a regulator could follow the reasoning from the first signal to the deadline. A population figure without a basis, or a notifiability answer without the threshold it turns on, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where logs, the data map, or the affected systems cannot be read, the run delivers `breach-connector-diagnostic.md` naming each unreachable source, the determinations it blocks, and every deadline still running. The clock is stated in that mode with the same precision as in any other, because the connector's state has no effect on it.

Anti-fabrication guard: this desk has two numbers that will be quoted back to the organization for years, and both round toward comfort if nobody stops them. The awareness timestamp drifts later, from the alert to the bridge to the moment the assessment began, and each hour of drift buys a deadline the organization did not have. The affected count drifts toward whatever was easy to query, so a row count becomes a person count and an upper bound becomes a finding. Both are recorded with the evidence that produced them and with the direction of their uncertainty stated. The third temptation is the sentence that closes an incident early: "no evidence of exfiltration" written where the truth is that retention on those logs was seven days and the access happened on day twelve. Log coverage is stated alongside every negative finding, because a filing built on an unqualified negative is the one a forensic report will contradict later, in public.

## privacy_packet fields to update

- `breaches[]` created or updated with `incident_id`, `awareness_at`, `discovered_by`, `breach_type`, `personal_data_involved`, `data_categories`, `special_category`, `affected_subjects` and `affected_records` each with their basis, `cause`, `containment_state`, and `mitigating_factors`
- `breaches[].risk_to_individuals` with `likely_consequences` stated as harms, `severity`, `likelihood`, `method`, and `outcome`
- `breaches[].notifiability[]` per regime with `authority`, `notifiable`, `deadline` computed from `awareness_at`, and `basis` naming the threshold
- `breaches[].register_entry` recorded whether or not the incident is notifiable, and `processor_notified_controller_at` where the organization is a processor
- `active_clocks[]` for every notification deadline, each with the awareness event as its start and the regime that set the period
- `data_inventory[]` corrected where the incident revealed a system holding categories the map did not carry, with both readings preserved
- `source_facts` separating the security account from the map and from log evidence with collection dates, `assumptions` with the direction of each uncertainty, `open_questions`, `approvals`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the security account and the data map genuinely disagree about what the affected system holds. Both the population and the duty to notify derive from this one fact, so both readings are preserved and neither the smaller number nor the safer one is adopted silently while the clock runs.
- **Missing approval**: the risk determination, the decision that an incident is not a personal data breach, and the decision not to notify are each positions the organization defends to a regulator and need the accountable owner with counsel. Preparation continues while approval is sought, because the deadline does not pause.
- **Security or privacy**: continuing would require handling exposed personal data in a way that widens the exposure, such as copying affected records into a working artifact or an incident channel with a broader audience than the data had.
- **Release integrity**: an affected-population figure or a risk conclusion would go into a filing with no computed basis under it, or an unqualified negative finding would rest on logs whose coverage nobody established.
- **Production or destructive**: the next action would alter or destroy evidence, close an access path in a way that removes the record of what happened, or write into the breach register before the determination is authorized.
- **Connector unreachable**: logs, the affected system, or the data map exists and cannot be read, so the population would describe something nobody observed. The deadline is stated on the halt and escalated immediately.

An unconfirmed root cause, an unknown attacker motive, and a missing timeline detail are soft gaps. They do not delay the notifiability determination, which is made on what is known with the uncertainty labeled, because a filing on incomplete facts is provided for and a late filing is not.

## Downstream handoffs

`breach-notification-desk` is next and needs the notifiability determination per regime, the deadline each computes from awareness, the content elements each filing requires, the population figure with its basis and its uncertainty, the harms as they will be described to individuals, and the facts still under investigation that make a phased filing necessary. `retention-deletion-desk` receives the over-retention finding where historic data widened the population. `processor-vendor-agreement-desk` receives the vendor notification timing against the contractual clock. `data-inventory-mapping-desk` receives corrections where the incident showed a system holding what the map did not record. `privacy-program-metrics-desk` needs the awareness-to-notification interval and the register completeness.

## Quality bar

Good breach assessment is recognizable in its first paragraph, which gives an awareness time earlier than anyone would like along with the evidence for it. After that, the marks are a population figure with arithmetic behind it and an explicit statement of whether it counts people or rows, a risk section that never mentions the organization's exposure, and a notifiability matrix that includes the regimes assessed and ruled out, because "we considered it and here is why not" is a defensible position while silence is not. The mitigating factors section is short and specific, since most claimed mitigations do nothing for the individual. And the register entry is made even when the answer is that nothing was notifiable, because the incidents an organization decided not to report are exactly the ones a regulator will ask to see the reasoning for.

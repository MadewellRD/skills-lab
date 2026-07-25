---
name: vendor-security-review-desk
description: run third-party security review across vendor tiering and inherent risk rating by data shared and integration depth, attestation and certification review bounded to the stated scope period and exceptions, questionnaire gap analysis against evidence, required contractual and technical controls, integration and access review of tokens keys and subprocessors, continuous monitoring by tier, and offboarding with access revocation and data deletion. use for vendor security assessment, saas onboarding, attestation review, subprocessor risk, and third-party offboarding.
---

# Vendor Security Review Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the vendor artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent attestation types, report scopes, audit periods, exception counts, certification identifiers, subprocessor lists, contractual terms, or a control the vendor did not state.

## Role

Own the risk that sits in someone else's environment. This desk produces the vendor tier and inherent risk rating derived from the data shared and the depth of the integration, an attestation review bounded strictly to the scope and period the report names, a questionnaire gap analysis that separates self-attestation from evidence, the contractual and technical controls required at that tier, an integration access review covering the tokens, keys, and identities the vendor actually holds, continuous monitoring requirements by tier, and offboarding requirements that end access and data retention rather than assuming they end themselves.

The residual risk of a vendor relationship is set at onboarding by two decisions: what data crosses and how deeply the integration reaches. Everything else is mitigation on top of those two facts.

## Use when

- A vendor or service is being onboarded and needs a security assessment before data or access is granted.
- An attestation, certification, or audit report has arrived and needs reading for scope, period, exceptions, and the obligations it passes back.
- A questionnaire has been returned and its answers need testing against evidence rather than filing.
- Tiering or risk rating is being defined or applied, or a vendor's tier needs revisiting after a change in data or integration.
- Contractual security terms need drafting, reviewing, or enforcing: breach notification, subprocessor notification, audit rights, deletion on termination.
- An integration's access needs review: OAuth grants and scopes, API keys, service accounts, webhook endpoints, and network access into the environment.
- A vendor is being offboarded, or a vendor incident or breach disclosure needs assessing for impact here.

## Do not use when

- The subject is the organization's own controls and their evidence. That is `compliance-evidence-desk`, which supplies the boundary this vendor may sit inside.
- The subject is the identity provider configuration that federates the vendor's application. That is `identity-access-management-desk`; this desk states the requirement, that desk implements it.
- The subject is a software dependency, package, or library rather than a service relationship. That is `software-supply-chain-desk`.
- The subject is commercial terms, pricing, or vendor selection. Route that to the procurement suite as a labeled cross-suite handoff, with the security requirements attached.
- The subject is a confirmed incident at a vendor affecting this organization's data. That is `security-incident-response-desk`, with this desk supplying the data and access picture.

## Required evidence

- What the vendor does for the organization, described concretely rather than by product category, and the business owner who sponsors it.
- The data shared with its classification, volume, residency, and whether it is transferred, accessed in place, or processed on the vendor's infrastructure.
- The integration and access model: authentication method, OAuth scopes granted, API keys and service accounts issued, network paths opened, callbacks and webhooks, and any agent or code running inside the environment.
- Attestations, certifications, and audit reports as the actual documents, with their scope section, period, opinion, exceptions, and subservice organization treatment.
- Questionnaire responses with the respondent named, plus any supporting evidence attached to the answers.
- Contractual security terms in force: the security addendum, data processing terms, breach notification window, subprocessor notification and objection rights, audit or assessment rights, deletion on termination, and liability and insurance where relevant.
- The subprocessor list the vendor publishes, and the notification mechanism for changes to it.
- The organization's tier rubric, and the control requirements attached to each tier.

## Workflow

**Outcome.** A tier and inherent risk rating with the factors that produced it, an attestation review bounded to the scope and period actually named in the report, a questionnaire gap analysis separating stated from evidenced, the required contractual and technical controls with their current state, an integration access review, monitoring requirements by tier, and offboarding requirements ready to execute.

**Grounding.** An attestation is authoritative only for the systems named in its scope section, during the period it covers, subject to the exceptions it lists. Every one of those four is a fact to read from the document rather than from a badge, a trust page, or a summary email. Where the report period ended some time ago, the gap between its end and today is uncovered by that report, and a bridge letter covering the gap is either present or it is not. Questionnaire answers are the vendor's statements about itself and are recorded as such; an answer supported by an attached artifact is a different fact from an answer that is not. What the vendor actually holds is read from the integration itself, since granted scopes and issued keys are observable here and are frequently broader than the questionnaire describes.

**Constraints.** Tier is derived from stated factors, at minimum the data classification shared, the depth of access into the environment, the availability dependence, and whether the vendor sits inside a regulated or audited boundary; the derivation is shown so a tier can be argued with. Attestation findings record the report type, its scope, its period, its opinion, and its exceptions, and the obligations the report passes back to the organization as a user entity are extracted and assigned an owner here rather than left in an appendix nobody reads. Subprocessors are treated as part of the assessment, since data reaching a fourth party is still the organization's data. Required controls are stated with the enforcement point and whether they are contractual, technical, or both, and a control that exists only in a contract is recorded as contractual with no technical enforcement, which is a real and different state. Integration access is reviewed against least privilege at the scope level rather than at the vendor level. Continuous monitoring is set by tier with a cadence and a trigger set, because a point-in-time assessment ages the day it is signed.

**Parallel surface.** Individual vendors, individual attestation documents, individual integrations, individual questionnaire domains, and per-vendor subprocessor reviews fan out and are parallel-safe. The tier assignment relative to the rest of the portfolio, the aggregate concentration view where several vendors depend on one underlying provider, the monitoring cadence allocation against available capacity, and the portfolio risk record are single passes that run after the fan-out returns.

**Ordered gate for granting a vendor access to data.** This order is mandated because access and data, once granted, are outside the organization's environment and cannot be recalled by revoking a token; copies made during the window remain made. Step 4 is the point of no return.

1. Establish the data classification and the integration depth, and set the tier from them.
2. Complete the assurance review at that tier, with the attestation scope, period, and exceptions read from the document, and the residual gaps recorded.
3. Put the contractual controls in force for the tier, including breach notification, subprocessor notification, and deletion on termination.
4. Obtain the data owner's approval, plus privacy or legal review where the data class or jurisdiction requires it, and only then provision access at the minimum scope with monitoring and an offboarding path already defined.

**Acceptance bar.** A risk owner can accept or reject the vendor from the artifact, and an engineer can provision the integration at the right scope from it. The attestation review states scope, period, opinion, and exceptions as read from the report, the required controls each name their enforcement point and current state, and offboarding is specific enough to execute on the day it is needed.

## Outputs

A complete run delivers this set:

- `vendor-tier-and-risk-rating.md`: the tier with the factors that produced it, inherent risk before controls, residual risk after them, and the concentration or availability dependence the relationship creates.
- `attestation-review.md`: report type, scope as named in the document, period, opinion, exceptions carried forward, subservice organizations and their treatment, the coverage gap between period end and today, and the user entity obligations the report passes back with an owner for each.
- `questionnaire-gap-analysis.md`: answers grouped by domain, which are supported by evidence and which are self-attested, the gaps against the tier's requirements, and the follow-up questions worth asking.
- `required-controls.md`: contractual and technical controls required at the tier, each with its enforcement point, current state, and the gap where it is required and absent.
- `integration-access-review.md`: the identities, scopes, keys, network paths, and callbacks the vendor holds, what each reaches, least-privilege findings, and the credentials whose rotation and expiry nobody owns.
- `continuous-monitoring-plan.md`: reassessment cadence by tier, the triggers that force an off-cycle review, attestation renewal dates to watch, subprocessor change notification handling, and the owner of each.
- `offboarding-requirements.md`: access revocation across every path identified, key and token revocation, data deletion or return with the evidence expected, retention obligations that survive termination, and the confirmation the vendor must provide.
- `vendor-downstream-handoff.md`: what the aggregate risk record and `compliance-evidence-desk` inherit, including vendors inside an audit boundary and their subservice treatment.

Depth standard: an artifact is complete when the data owner can make the accept-or-reject call and the engineer can provision or revoke from the same set. An attestation review that says a report exists without its scope, period, and exceptions is a filing note rather than a review.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the attestation document, the vendor portal, the questionnaire response, or the integration configuration cannot be reached, the run delivers `vendor-connector-diagnostic.md` naming what is unreachable and which assurance conclusions are unavailable as a result. Assurance is never inferred from a trust page, a certification badge, or a vendor's own summary of its report.

Anti-fabrication guard: third-party assurance fails in one specific direction, and it is scope. A certification badge and a report title look like coverage, and the sentence that writes itself is that the vendor holds a clean report with no exceptions, when the report may cover a different product line, a period that ended eleven months ago, or carry exceptions on exactly the control the integration depends on. Every attestation statement in these artifacts therefore quotes the scope section, the period dates, the opinion, and the exception list from the document, and where the document itself was not read the review says the assurance is unverified and names what is needed, rather than describing a report that was summarized to us. Report types, certification identifiers, and audit periods are never reconstructed from the vendor's marketing surface. Subprocessor lists are copied from the published list on its retrieval date, since data flowing to a fourth party nobody enumerated is the exposure that turns up during someone else's breach. Contractual terms are quoted from the executed agreement, because a breach notification window that was assumed rather than negotiated is discovered in the worst week of the relationship. Where a questionnaire answer is the only source, the artifact says so plainly: the vendor stated it, and nobody tested it.

## security_packet fields to update

- `vendors[]` with the vendor name, `tier` from the org rubric, `attestation` recording report type, scope, and period, and `open_issues[]` for gaps carried forward
- `data_classification[]` for the data shared, with residency and the basis for the classification
- `controls[]` for contractual and technical controls, each with `enforcement_point`, `state`, `evidence`, and the named owner, including the user entity obligations inherited from an attestation
- `identities[]` for vendor service accounts, OAuth grants, and API keys, with `privilege_tier` and `review_state`
- `findings[]` for control gaps and least-privilege issues in the integration, with an owner and a due date
- `exceptions[]` where a vendor is onboarded with a known gap, carrying the compensating control, the named approver, and the expiry
- `approvals[]` for onboarding, data sharing, and any privacy or legal review, with the approver and state
- `source_facts[]` with `collected` times per document read, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: onboarding a vendor that will hold regulated, personal, or otherwise sensitive data needs the data owner, plus privacy or legal review where the jurisdiction requires it. A completed assessment is not an approval.
- **Security or privacy**: the integration would send regulated or personal data outside an approved jurisdiction or to an unenumerated subprocessor, or the review has surfaced a live exposure in the vendor's access into the environment.
- **Production or destructive**: the next action would revoke vendor access, disable an integration, or trigger data deletion at the vendor, each of which breaks a live business process and, in the deletion case, cannot be undone.
- **Source conflict**: the questionnaire, the attestation, and the observed integration genuinely disagree about what the vendor holds or can reach, so no risk rating can be stated without choosing a story.
- **Release integrity**: a vendor assurance statement would go to an auditor, a customer, or a risk committee based on a report whose scope or period does not cover the service in use.
- **Connector unreachable**: the attestation, the questionnaire, or the integration configuration exists and cannot be read, so the assurance conclusion would describe a document nobody opened.

An unnamed subprocessor, a missing internal owner, or an unstated retention period is a soft gap: name it, label the assumption inline against the affected rating, and continue with the tier set from what is known. Tier requirements are never lowered to unblock a procurement date.

## Downstream handoffs

`security-command-desk` receives the vendor entry for the aggregate risk record, including the concentration view where several vendors rest on one underlying provider. `compliance-evidence-desk` receives vendors sitting inside an audit boundary, with the subservice treatment and the user entity obligations that the organization must now evidence as its own controls. `identity-access-management-desk` receives the federation, provisioning, and access requirements the tier demands. `network-security-desk` receives any inbound path or allowlisting the integration needs. `security-incident-response-desk` receives the notification obligations and contacts, so a vendor breach disclosure has a defined path rather than arriving at a shared mailbox. Commercial negotiation and vendor selection go to the procurement suite as a labeled cross-suite handoff.

## Quality bar

Good vendor review is a scope-reading exercise before it is anything else. The attestation section states what the report covers, over what period, with what exceptions, and what obligations it hands back; the questionnaire section separates what the vendor said from what anyone checked; and the access section describes the tokens and scopes actually granted rather than the ones requested. Tiering is derived from stated factors so it can be argued with. Offboarding is written at onboarding, while there is still leverage and while somebody still remembers every path the integration opened.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

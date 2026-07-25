---
name: vendor-onboarding-provisioning-desk
description: onboard an executed supplier by requesting the vendor master record with tax and compliance forms, verifying bank details out of band through a channel the requester did not supply, granting access only at the level the review authorized with the approval recorded per system, capturing the security configuration as actually built including identity federation provisioning logging retention and admin roles, setting up invoicing and purchase order handling, and naming an internal owner. use for vendor master setup, supplier bank detail verification and payment fraud controls, access provisioning and sso scim configuration, tenant security settings, invoicing and coding setup, supplier owner assignment, and go-live readiness after contract signature.
---

# Vendor Onboarding Provisioning Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, prepare the onboarding, record what was actually configured, update `procurement_packet`, and continue into `supplier-performance-sla-desk` so the relationship starts with a measurement baseline rather than acquiring one after the first dispute. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the action boundary that keeps bank changes and access grants behind named human authorization.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the record, grant, or setting it affects.

Never invent a bank account, a beneficiary name, a verification call, a verifier, a tax form, a vendor master identifier, an approver, an access grant, a configuration setting, a retention period, a log destination, an entitlement count, an invoicing contact, or an internal owner.

## Role

Own the gap between what the agreement says and what actually exists in the systems. An executed contract is a set of promises; onboarding is where those promises become a vendor record that can be paid, a tenant that is configured, accounts that exist at a defined level of privilege, an invoice route that can be reconciled, and a named person who owns the relationship. Every one of those can be built correctly, and every one of them is routinely built to whatever the go-live date allowed.

Two acts here are different in kind from everything else in this suite. Adding or changing a supplier's bank details sends money, and it is the single most productive fraud pattern aimed at any company: an urgent request, a familiar name, a new account, and an approval chain shortened by a deadline. Granting a supplier access to systems or data converts a reviewable decision into an exposure, and access granted for a go-live is rarely revisited. Everything else in onboarding is administration; these two are controls, and they are the controls that fail under exactly the conditions onboarding creates.

The third quiet failure is ownership. A supplier with no named internal owner is the one nobody renegotiates, nobody measures, and nobody notices auto-renewing.

## Use when

- An agreement has been executed and the supplier has to be set up to be paid, accessed, and operated.
- A vendor master record has to be requested with the correct legal entity, tax residency and withholding forms, and compliance documentation.
- Bank details have arrived, or a request to change existing details has arrived, and the verification the policy requires has to be performed and recorded.
- Access has to be granted across systems and each grant needs its level, its requester, its approver, and the review that authorized it recorded.
- The tenant or service has to be configured to the security requirements the review produced, and what was actually built has to be captured.
- Invoicing needs setting up: billing contact, invoice format, purchase order requirement, and the coding that will let this spend be attributed later.
- An internal owner has to be named and handed the obligations, dates, service levels, and conditions they now carry.
- A go-live is imminent and the onboarding steps being skipped to meet it need recording with what each one leaves exposed.

## Do not use when

- The contract is not executed and the dates and obligations have not been extracted: `contract-execution-routing-desk`.
- The security or privacy review has not closed and the required configuration is not yet defined: `security-privacy-review-desk`.
- The entity, ownership, or insurance position is unresolved: `supplier-integrity-screening-desk`, whose verified entity is what the vendor master record has to match.
- The question is ongoing scorecards, service level measurement, or credits: `supplier-performance-sla-desk`.
- Access is being removed rather than granted, or the relationship is ending: `vendor-offboarding-desk`.
- The identity platform, provisioning pipeline, or integration itself has to be built rather than configured and recorded: route the engineering work to the SDLC suite with the control it has to preserve and the acceptance criteria attached.

## Required evidence

- The executed agreement with the entity, the entitlements, the commercial terms, the security terms, and the service levels.
- The vendor master requirements: legal entity details, tax residency and withholding forms, remit-to information, and any compliance documentation the policy requires.
- The banking details as supplied, and the verification method the policy mandates including the independent channel and the dual authorization requirement.
- The access the supplier needs per system, the level requested, the business justification, and the approval behind each grant.
- The security configuration the review obliges: identity federation, automated provisioning and deprovisioning, multi-factor enforcement, administrative role assignment, session policy, log delivery and its destination, retention settings, data residency or tenant region, network restrictions, and service account and token handling.
- The invoicing setup: billing contact, invoice format, purchase order requirement, payment terms as executed, and the cost center and ledger coding.
- The named internal owner, the technical owner, and the users in scope.
- The adoption plan and the usage the business case assumed, so consumption can later be measured against it.
- The conditions attached to any conditional approval, each with its owner and date.

## Workflow

**Outcome.** A vendor master request against the verified entity, a bank detail verification record naming the method, the independent channel, and the person who performed it, an access provisioning record with an approval per grant, the security configuration as actually built rather than as required, an invoicing setup that will let spend be attributed later, a named internal owner with the obligations handed to them, an adoption plan measured against the business case, and an explicit record of what was skipped to meet the date.

**Grounding.** The executed agreement and the closed review define what should exist. The systems define what does exist, and the record here is of the second one. A configuration recorded because the contract requires it, rather than because somebody looked at the setting, is the defect this stage most reliably produces, and it is discovered during an incident.

**Constraints.**

- The vendor master record matches the entity on the signature block. An entity mismatch between the contract and the payee is how a company ends up paying a party it has no agreement with.
- Bank details are verified against a channel the requester did not supply, using contact details obtained independently of the request, by a named person, with the result recorded. An emailed change request, a letterhead, and an attached bank letter are all the same evidence: the requester's own assertion.
- Every access grant records the system, the level, the requester, the approver, and the review that authorized it. Administrative access, service accounts, and API tokens are grants and are recorded as such.
- Record the configuration as built, setting by setting, with who confirmed it and when. Where a required setting is unavailable on the purchased tier, that is a finding rather than a footnote, because the review approved a control the product does not offer at the price paid.
- Set the invoicing coding so this spend is attributable later. Spend that arrives uncoded is exactly the spend that shows up as unattributed in the next analysis and cannot be consolidated or renegotiated.
- Name one internal owner, not a team. Hand them the notice deadline, the service levels, the entitlement count, the open conditions, and the dates.
- Record every step skipped to meet the go-live date, with what it leaves exposed and who accepted that. Skipped onboarding steps are never revisited by the calendar; they are revisited by an audit or an incident.

**Mandated order.** The provisioning sequence below is set by the mechanics of the systems involved rather than by preference, and each step destroys evidence or forecloses a choice for the one before it, so it is kept as an order:

1. The security configuration is built and confirmed in the tenant.
2. Access is granted, at the level the review authorized and no higher.
3. Company data is loaded or connected.

Retention, residency, encryption, and logging settings apply from the moment they are set and not retroactively, so data placed into a tenant before its configuration exists is data the configuration never covered, and no later change to the setting reaches it. Access granted ahead of the configuration is access to an unconfigured system, and access granted ahead of the review that governs it is the review made irrelevant.

**Parallel surface.** Independent items fan out and are parallel safe: each access grant with its own approval, each configuration domain such as identity, logging, retention, network restriction, and administrative roles, the tax and compliance form collection, the invoicing setup, and the adoption and training preparation. Two items sit outside the fan-out. Bank detail verification is performed once by a named human through an independent channel and is never parallelized, batched, or delegated to whoever is processing the queue, because the control is the human and the channel. The go-live readiness position is a single pass after everything returns, since it is a judgment across the whole set and a partially onboarded supplier that is live is simply live.

**Acceptance bar.** The vendor master request names the entity that signed. The bank verification names the method, the independently obtained channel, the person, and the date. Every access grant names its system, level, requester, approver, and authorizing review. The configuration record states each required setting with its actual value and who confirmed it, including the ones that could not be set. Invoicing setup includes the coding. One person is named as owner and has received the dates and obligations. Skipped steps are listed with their exposure and the person who accepted it.

## Outputs

A complete run delivers the set:

- `vendor-master-request.md`: the legal entity as executed, registration details, remit-to, tax residency and withholding forms received and outstanding, payment terms as executed, and the compliance documentation the policy requires.
- `bank-detail-verification-record.md`: the details as supplied, the verification method, the channel used and how it was obtained independently, the named person who performed it, the second authorizer where policy requires dual control, the date, and the outcome.
- `access-provisioning-record.md`: a line per system with the access level, the requester, the approver, the authorizing review, the date, and whether the grant is standing or time-bound, including administrative accounts, service accounts, and API tokens.
- `security-configuration-as-built.md`: each required control with its actual configured value, who confirmed it, the date, and an explicit entry for every control that could not be configured on the purchased tier.
- `invoicing-and-coding-setup.md`: billing contact, invoice format and delivery route, purchase order requirement, payment terms, cost center and ledger coding, and the entitlement the invoice should reflect.
- `supplier-owner-handover.md`: the named internal owner, the obligations they now carry, the notice deadline and its date, the service levels and credit claim windows, the entitlement count, and the open conditions with their dates.
- `adoption-plan.md`: rollout, training, the population in scope, and the usage the business case assumed, expressed so consumption can be measured against it later.
- `onboarding-exceptions-record.md`: every step skipped or shortened to meet the date, what it leaves exposed, the person who accepted it, and the date it is to be closed.
- `vendor-onboarding-downstream-handoff.md`: the baseline the performance, spend, and renewal stages inherit, including entitlement, coding, owner, and measurement sources.

Depth standard: an artifact is complete when someone who was not present could reproduce the state of the account from it. "SSO configured" is a claim; "identity federation enabled against the named identity provider with automated provisioning and deprovisioning active, multi-factor enforced at the identity provider, three administrative roles assigned to named people, audit logs delivered to the named destination, retention set to a stated period, and tenant region set to a stated region, each confirmed by a named person on a stated date" is a configuration record.

Where a control the review required is unavailable at the tier purchased, the artifact records it as unavailable with the compensating control and the owner rather than omitting the line. Where the vendor master, the identity platform, or the supplier's administration console cannot be reached, `vendor-onboarding-diagnostic.md` names the system and states which configuration facts are unestablished, and no setting is recorded as configured on the basis of what the contract requires.

This is the only desk in the suite whose output can be contradicted by opening a screen, which is precisely why it drifts. The contract says what should be true, the review says what has to be true, and the fastest way to fill an onboarding record under a go-live deadline is to copy those into it. The result reads as an implementation report and is actually a restatement of the requirements, and nobody notices until an incident, an access review, or an audit asks where the logs go and finds that the answer was written by someone reading an exhibit. So a setting is recorded only with the person who looked at it and the date they did; a control nobody confirmed is written as unconfirmed with who has the console; an access grant with no approver named is written as unauthorized and pending rather than as granted; and a bank verification with no independent channel and no named verifier is written as not performed, because in this one case an unperformed control that reads as performed is how the money leaves.

## procurement_packet fields to update

- `onboarding.vendor_master_state`, `bank_detail_verification`, `tax_and_compliance_forms`, `access_provisioning`, `security_configuration`, `invoicing_setup`, `internal_owner`, `adoption_plan`, `kickoff_state`.
- `engagement.technical_owner` and the named relationship owner, since this is the stage where an unowned supplier becomes permanent.
- `contract.key_obligations` updated with the company-side obligations now assigned to the owner with dates.
- `diligence.security.conditions` where a condition became a configuration item, closed with evidence or carried forward with its owner and date intact.
- `performance.measurement_source` and the entitlement baseline that `consumption_versus_entitlement` will later be read against.
- `spend` coding references so this supplier's spend is attributable in the next baseline.
- `approvals` for the bank detail action, each access grant, and any onboarding exception accepted to meet a date.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Security or privacy**: creating or changing bank details on an instruction that has not been verified through a channel the requester did not supply, and granting a supplier access to systems or data before the review governing that access has closed. Both are irreversible in the way that matters: money that has left, and data that has been reached. The correct response to an urgent bank change from a familiar name is verification through an independently obtained channel, not careful processing.
- **Approval**: creating the vendor master record, granting any access, accepting an onboarding exception to meet a go-live date, and raising the purchase order. Each has a named authority and none of them is implied by the contract having been signed.
- **Production or destructive**: connecting an integration, loading company or customer data into the supplier's environment, or enabling an automated provisioning link. These change production state and are performed by the system owner, not by the onboarding record.
- **Source conflict**: the entity on the executed agreement, the entity on the invoice, and the entity in the vendor master do not match, or the entitlement in the order form and the entitlement provisioned in the tenant disagree. Record both readings; an entity mismatch at the payment step is the pattern this control exists to catch.
- **Release integrity**: a security configuration would be reported as implemented, to a reviewer, an auditor, or a customer questionnaire, on the basis of what the contract requires rather than what the system shows.
- **Connector unreachable**: the vendor master, the identity platform, the supplier's administration console, or the approval record exists and cannot be read, so grants and settings would be recorded as facts without anyone having seen them.

An outstanding tax form, a billing contact the supplier has not yet named, a training date not yet scheduled, and an adoption plan awaiting a rollout decision are soft gaps. Record them against the item, name who is chasing, and continue the rest of the onboarding.

## Downstream handoffs

`supplier-performance-sla-desk` inherits the entitlement baseline, the measurement sources, the service levels with their credit claim windows, and the adoption assumptions, which together are what make a first scorecard possible rather than aspirational. `spend-analysis-desk` inherits the coding and the vendor master identifier, without which this supplier's spend arrives unattributed and invisible to consolidation. `supplier-relationship-governance-desk` inherits the named owner, the access footprint, and the integration depth as built, which is the real measure of dependency. `renewal-consolidation-desk` inherits the owner and the notice deadline. `vendor-offboarding-desk` inherits the access provisioning record and the configuration record, and it is the only reason an exit can deprovision completely, because the accounts nobody recorded are the accounts nobody removes.

## Quality bar

A good onboarding record is an inventory of reality. Someone reading it two years later, during an access review or an incident, finds every account that exists, every setting as it was actually configured, the person who confirmed each one, and the date. The bank verification is a short entry with a person's name in it, and it exists even when the supplier is well known, because familiarity is the condition the fraud pattern relies on. The supplier has one owner, and that owner has the dates. The exceptions record is unflattering and complete, because a go-live never closes the steps it skipped and the only thing that will is a document that says which ones they were.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

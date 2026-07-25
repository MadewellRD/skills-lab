---
name: attack-surface-inventory-desk
description: build the asset and exposure baseline for a security engagement, covering internet-facing surface enumeration, dns and certificate transparency discovery, cloud account and subdomain inventory, dangling records and subdomain takeover risk, shadow it and unmanaged systems, data classification per store, data residency, crown-jewel designation, ownership mapping, and scope exclusions attributed to whoever set them. use for estate discovery, external attack surface review, asset inventory gaps, data location questions, and establishing what an assessment actually covered.
---

# Attack Surface Inventory Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the inventory artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent hostnames, IP ranges, account identifiers, storage buckets, data classes, residency regions, owner names, or the existence of an asset that no source returned.

## Role

Own the denominator. Every later stage in this suite makes a statement about a population, and this desk decides what that population is: which systems exist, which of them face the internet, what data each one holds, which are crown jewels, who owns them, and what was deliberately left out of scope by whom.

An inventory is a claim about absence as much as presence. The valuable output is rarely the tidy asset table; it is the set of assets that appear in one discovery source and not another, the hosts with no owner, the storage with no classification, and the honest statement of which discovery methods could not have seen a given class of asset at all.

## Use when

- An engagement is starting and the scope is described in business terms rather than in named systems, accounts, or repositories.
- The estate is suspected of holding systems nobody is tracking: acquired infrastructure, decommissioned-in-name-only services, developer-provisioned accounts, or unsanctioned software-as-a-service holding company data.
- External exposure is the question: what answers on the internet, on which ports, behind which certificates, and under whose name.
- Data location is the question, whether for a residency obligation, a regulated boundary, or an audit scope statement.
- Crown jewels have never been designated, or the existing designation predates a material change to the business.
- A prior assessment reported a clean result and its coverage was never stated.

## Do not use when

- The question is where controls should sit in a design that is being drawn now. That is `security-architecture-review-desk`; this desk supplies the asset and classification input it consumes.
- The question is which of the discovered exposures an attacker would actually use, and how. That is `threat-modeling-desk`.
- The question is cloud misconfiguration detail on discovered accounts, such as public buckets, permissive security groups, or guardrail gaps. Hand the account list to `cloud-security-posture-desk`.
- The question is segmentation, ingress and egress paths, or edge protection on the discovered surface. That is `network-security-desk`.
- The question is endpoint and workload agent coverage across a device population. That is `endpoint-hardening-desk`.
- The subject is a third party holding company data rather than an owned asset. That is `vendor-security-review-desk`.

## Required evidence

- Configuration management database, asset register, or service catalog export, with its last reconciliation date.
- Cloud organization, account, subscription, and project enumeration, plus tag or label conventions used for ownership.
- DNS zones under the organization's control, registrar records, certificate transparency results for owned domains, and the autonomous system numbers and address ranges attributable to the organization.
- External surface scan or attack surface management output, with its scan window and the ranges it covered.
- Identity provider application catalog and single sign-on assignments, which is usually the most complete record of software-as-a-service in use.
- Data store inventory: databases, object storage, data warehouse and lake locations, message queues, backups, and analytics copies.
- Existing data classification scheme, records of processing, and any residency or sovereignty obligations named by a source.
- Ownership sources: service catalog owners, on-call rotations, cost center or billing tags, and repository code owners.
- Prior scope statements, exclusion lists, and the audit or authorization boundary definitions already in force.

## Workflow

**Outcome.** An asset and exposure baseline that later stages can trust as their population: internet-facing surface with what answers on it, data classification per store with the source that established it, crown-jewel designation with the reason, an ownership map with unowned assets named as unowned, and a scope statement whose exclusions each carry the person or document that set them.

**Grounding.** Cross-source reconciliation is the method, because no single discovery source is complete. Cloud enumeration finds what is provisioned, DNS and certificate transparency find what is named, external scanning finds what answers, and the identity provider catalog finds what people log into. Assets present in one source and absent from another are the finding, not a data quality nuisance to smooth over. Attribution matters as much as discovery: an address range or certificate is attributed to the organization only where a source establishes the link, because a wrongly claimed asset invites testing against someone else's system.

**Constraints.** Every asset entry carries its discovery source and collection time, since exposure changes between readings. Data classification records the basis that established it, and a store whose contents were never examined is classified as unknown rather than as internal. Crown jewels are designated by consequence of compromise rather than by traffic volume or team seniority, and each designation names the consequence. Ownership is recorded as found: an unowned asset with a real ownership gap is more useful than a plausible team name, and orphaned assets are the ones that go unpatched. Coverage is stated as part of the result, naming the ranges, accounts, and domains the discovery methods reached and the classes of asset they structurally could not see, such as workloads behind a partner network or systems in an account nobody enumerated. Dangling DNS records pointing at deprovisioned infrastructure are recorded as a takeover exposure at discovery time rather than deferred, because that window is measured in hours.

**Parallel surface.** Independent domains, cloud accounts, address ranges, business units, repositories, and data stores fan out safely and are evaluated concurrently. Reconciliation across discovery sources, deduplication of assets that appear under several names, crown-jewel designation relative to the rest of the estate, and the coverage statement itself run once after the fan-out returns, because each is a judgment about the whole set rather than about any one asset.

**Acceptance bar.** A reviewer could take the scope statement into the next stage and know exactly what was and was not looked at. Every internet-facing entry names what answers and how that was established, every data store carries a classification with its basis or an explicit unknown, every crown jewel names the consequence that earned the designation, and every exclusion names who set it.

## Outputs

A complete run delivers this set:

- `asset-inventory.md`: the reconciled asset register with discovery source, collection time, environment, and the per-source presence that produced each row.
- `external-exposure.md`: internet-facing hosts, endpoints, and services with the port, protocol, certificate subject, and responding banner or behavior that establishes the exposure, plus dangling records and takeover candidates.
- `data-classification-map.md`: one row per data store with data classes held, residency, the basis of the classification, and stores whose contents were not examined marked unknown.
- `crown-jewels.md`: designated assets with the compromise consequence, the data classes involved, and the dependencies that reach them.
- `ownership-map.md`: asset to owner with the ownership source, and a separate unowned register that is the actionable half of the artifact.
- `scope-statement.md`: in-scope systems, environments, and boundaries; exclusions with the named person or document that set each; and the coverage the discovery methods achieved against the classes they could not see.
- `inventory-downstream-handoff.md`: what `security-architecture-review-desk` and any directly targeted desk inherit, including the assets whose classification is still unknown.

Depth standard: an artifact is complete when the next desk can act on it without re-running discovery. An asset row without a discovery source, an exposure without what answers on it, or an exclusion without an attributed setter is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the configuration database, cloud organization, DNS control plane, or scan output exists and cannot be read, the run delivers `inventory-connector-diagnostic.md` naming each unreachable source, the asset classes it would have covered, and the downstream claims that consequently cannot be made.

Anti-fabrication guard: the characteristic failure here is the complete-looking asset table. Inventories are consumed as populations, so a row invented to make a region, environment, or business unit look covered silently corrupts every coverage percentage, severity ranking, and audit boundary computed downstream. Assets are listed only where a discovery source returned them, and an asset is attributed to this organization only where a source establishes ownership of the domain, range, or account, because testing an address that merely resembles the estate is testing somebody else's system. A store whose contents were not examined is classified unknown, never internal-by-default; unknown and empty are different findings. The right shape for a partial run is a short register plus an explicit list of what the discovery methods could not reach, and that is a correct result rather than a thin one.

## security_packet fields to update

- `scope.systems`, `scope.environments`, `scope.boundaries`
- `scope.out_of_scope` with the setter recorded per exclusion
- `data_classification[]` with `asset`, `classes`, `residency`, and `basis`
- `crown_jewels[]`
- `controls[]` only where discovery established an enforcement point, otherwise left for later stages
- `source_facts[]` with `source` and `collected` per fact
- `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: the asset register, cloud organization, DNS control plane, identity provider catalog, or scan output exists and cannot be read. This is the stage-specific halt, because "nothing is exposed" would otherwise be a claim about assets nobody enumerated.
- **Security or privacy**: discovery surfaces live personal or regulated data in an unexpected location, an open store, or an exposed management interface, and continuing to publish the locator broadly would widen the exposure before the owner can close it.
- **Production or destructive**: the next action would probe, authenticate to, or otherwise touch a discovered system rather than read inventory sources. Active interrogation of a live target belongs to `offensive-security-desk` behind its authorization gate.
- **Missing approval**: an exclusion that removes a crown jewel or a regulated system from scope needs a named human owner rather than a silent narrowing.
- **Source conflict**: the asset register, cloud enumeration, and scan output genuinely disagree about whether a system exists, which environment it is in, or which data it holds.
- **Release integrity**: a coverage or completeness statement would go into an audit or assurance artifact without the discovery evidence to carry it.

An asset with no owner, a store with no classification, and a stale reconciliation date are soft gaps. Record them, label the assumption inline, and continue; they are the findings this desk exists to produce.

## Downstream handoffs

`security-architecture-review-desk` is next and needs the crown jewels, data classification, and environment boundaries to judge where controls belong. `threat-modeling-desk` needs the external exposure list and crown jewels as its asset set. `cloud-security-posture-desk` needs the account and subscription enumeration. `network-security-desk` needs the internet-facing surface and address ranges. `compliance-evidence-desk` needs the scope statement and its exclusions verbatim, because an audit boundary that drifts between stages is itself a finding. Every desk inherits the coverage statement, since none of them can report on assets this stage never saw.

## Quality bar

Good inventory work is judged by what it admits. It states the discovery methods used and the asset classes each one is blind to, keeps the unowned and unclassified registers in front rather than in an appendix, and attributes every exclusion to a person or a document so a narrowed scope stays visible instead of becoming an assumption. Crown jewels are designated by consequence, and the reasoning survives on the page so the next reviewer can disagree with it. The register is structured so that a newly discovered account or domain obviously requires a new row, which is the property that keeps the baseline usable after this engagement ends.

---
name: data-governance-access-desk
description: design data classification and access control covering pii phi and pci classification of physical columns, roles groups and actual grants, row-level security predicates, column masking and tokenization, enforcement points, purpose limitation per audience, access reviews and the joiners movers leavers path, export and egress controls, non-production copies of production data, audit logging of restricted access, and enforcement evidence separated from policy documents. use for access reviews, masking design, and restricted dataset exposure.
---

# Data Governance Access Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the classification and access artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. This desk sits closest to the privacy boundary in the suite, so the distinction is sharp: an undocumented business justification for an old grant is a soft gap, while describing a masking policy as enforced without applied evidence is a security halt, because a false control is worse than a missing one. Never invent role names, group memberships, grant statements, predicate expressions, masking rules, classification labels, or the enablement state of any control.

## Role

Own who may see what, proven from applied grants rather than from policy text. This desk holds the classification of physical assets and columns, the access model with its actual grants, row-level predicates, column masks and tokenization rules, the enforcement point for each, purpose limitation per audience, the review cadence and the joiners-movers-leavers path, export and egress controls including non-production copies of production data, audit logging of access to restricted assets, and the enforcement evidence that separates a live control from a documented one.

Two properties make access control in a warehouse different from access control in an application. Permissions compose across objects, so a masked column on a base table is unmasked the moment a view, a materialized aggregate, or a BI extract copies it into an object the policy does not follow, and each copy is a new enforcement point nobody granted. And access is transitive through derivation, so classification is a property that propagates: a column classified as personal at the source stays personal in every mart, feature table, and export downstream of it, whether or not the derived object's name suggests it.

## Use when

- Restricted columns need classifying against the physical assets, or a classification recorded at profiling needs propagating to everything derived from it.
- Access needs designing, tightening, or reviewing for a dataset, a domain, or an audience, including standing grants nobody re-approves.
- Row-level security predicates, column masking, tokenization, or pseudonymization need designing, and the enforcement point for each needs establishing.
- An access review or recertification cycle is due and the reviewer set, the evidence each reviewer must see, and the revocation path need defining.
- Joiners, movers, and leavers are not reliably reflected in warehouse access, particularly movers, whose old access typically persists alongside their new access.
- Data is leaving the platform through exports, downloads, external shares, or partner deliveries, and egress controls need designing.
- A non-production environment holds a copy of production data and the policy that applies to it needs establishing or is known to be absent.
- Audit logging of access to restricted assets needs designing, or an audit is asking for evidence that a control was live during a period.

## Do not use when

- The subject is which audience needs which dataset for their work. That is `analytics-enablement-desk`; this desk decides what that audience may actually reach.
- The subject is how long data may be kept or how it is erased. That is `data-retention-lifecycle-desk`, which inherits classification from here.
- The subject is the classification of a source column during profiling. That is `source-system-profiling-desk`, which records the original label this desk applies and propagates.
- The subject is the privacy program itself: lawful basis, consent, cross-border transfer, or the data subject request process. That is a labeled cross-suite handoff to the Privacy suite; this desk implements the access consequences.
- The subject is audit response, control evidence packaging, or framework mapping. That is a labeled cross-suite handoff to the GRC suite, which consumes the enforcement evidence produced here.

## Required evidence

- The column classifications from profiling, and the information schema and catalog so classification can be applied to objects that actually exist.
- The applied grant inventory at live values: roles, groups, users, service accounts, and what each can read, at the object, schema, and database level.
- Existing row-level policies, column masking policies, tokenization mappings, and secure view definitions, with the objects they are attached to.
- The lineage graph, since classification propagates along it and a derived object outside the policy's attachment is the recurring exposure in this domain.
- Identity source data: group membership, the joiners-movers-leavers feed, and the role assignment path from a person to a warehouse grant.
- Access logs for restricted assets: who actually read what and when, which is what distinguishes a needed grant from an inherited one.
- The export, share, and download inventory: scheduled file deliveries, external shares, BI extracts, reverse-ETL destinations, and non-production environments holding production copies.
- The regulatory and contractual obligations that bind the data, and the purposes each audience has been approved for.

## Workflow

**Outcome.** A classification applied to physical assets and columns with propagation traced through derivation, an access model stating the actual grants, predicates, masks, and tokenization rules with the enforcement point of each, purpose limitation per audience, a review cadence with named reviewers and the joiners-movers-leavers path, egress controls covering exports and non-production copies, an audit logging design for restricted access, and an enforcement evidence record separating controls confirmed live from controls asserted in a document.

**Grounding.** Every access claim is read from applied state: the grant as the platform reports it, the policy as it is attached, the group membership as the identity source holds it. A policy in a repository, a design document, or a ticket is intent, and where intent and applied state disagree, both are recorded and the conflict is preserved. Need is assessed against access logs, so a standing grant with no read in the observation window is a finding rather than a fact of life, and a read by a principal no grant document mentions is a larger one.

**Constraints.** Every policy entry names the asset, the rule as an actual predicate, mask, or grant rather than a description of one, the subjects it applies to, the enforcement point that rejects a violation, and how that enforcement was confirmed. Classification propagates along lineage, and every derived object holding a classified column is listed with whether the control follows it; the objects where it does not follow are exposures with a reachable path, named individually. Non-production copies of production data are treated as production for classification purposes or recorded as a named exception with an owner and an expiry, because a development environment holding unmasked personal data is the same disclosure risk with fewer controls and more readers. Purpose limitation states the approved use per audience rather than only the objects, since the same table serves an approved analytical purpose and an unapproved operational one. Review cadence names reviewers as people, states the evidence each must see, and includes the revocation path, because a recertification performed without last-read data is a signature rather than a review. Service accounts and shared credentials are inventoried separately from human principals, since they are the population that never appears in a leavers feed.

**Parallel surface.** Assets, individual policies, roles, audiences, export destinations, and non-production environments are independent assessment units and fan out safely, as does the per-object read of applied grants and attached policies. The aggregate work runs once after the fan-out returns: composing effective access per principal across object, schema, and inherited grants, tracing classification propagation along the lineage graph, computing the exposure set for each restricted column across every derived copy, and reconciling the identity feed against warehouse grants for the movers and leavers. A per-table access review assembled in parallel and never composed across derivation is how a masked column is reported as protected while an aggregate built on it, in a different schema, serves the same values to a wider audience.

**Ordered gate for widening access to a restricted dataset.** Granting new access to personal, health, cardholder, or otherwise restricted data runs in this order, because access granted is access exercised, and a read that has already happened cannot be revoked:

1. Establish the classification of every column in scope and whether the request needs the restricted columns at all, since a masked or aggregated alternative frequently answers the question.
2. Establish the purpose and its approval basis, recorded against the specific audience rather than against the requesting individual.
3. Obtain the named approval from the data owner, and where the classification requires it, from the privacy or compliance owner.
4. Grant at the narrowest scope that serves the purpose, through a group rather than to an individual, with an expiry or a review date attached.
5. Confirm the applied state and that access logging is capturing reads on the object, and record the grant, its approver, its purpose, and its expiry in the review register.

Step 1 precedes everything because the cheapest control is not granting the column, and step 5 exists because a grant whose reads are not logged cannot be reviewed later and cannot support an audit answer about who saw what.

**Acceptance bar.** A reviewer could state, from these artifacts alone, which principals can read each restricted column and by which path, where each control is enforced and how that was confirmed, which derived copies fall outside the control, what leaves the platform and to whom, and which grants are due for review with the evidence the reviewer will see. Every control carries an honest state, including unverified.

## Outputs

A complete run delivers this set:

- `classification-map.md`: classification per asset and column, its basis, and the propagation through derived models, extracts, feature tables, and exports, with the derived objects where the classification is not currently carried.
- `access-model.md`: roles, groups, and service accounts with their actual grants, the path from a person to a permission, and effective access per principal composed across object and inherited grants.
- `policy-expressions.md`: row-level predicates, column masks, tokenization and pseudonymization rules written out, each with its attachment point, the objects it covers, and the objects deriving from those that it does not.
- `purpose-and-egress.md`: approved purpose per audience, and the export, download, external share, reverse-ETL, and non-production copy inventory with the control applying to each and the exceptions with owners and expiries.
- `access-review-plan.md`: the cadence, named reviewers, the evidence each must see including last-read data, the joiners-movers-leavers path with the mover case stated explicitly, and the revocation procedure.
- `audit-logging-design.md`: what is logged for restricted asset access, where the log is held, its retention, who reviews it, and the assets whose reads are currently not logged.
- `enforcement-evidence.md`: per control, whether it was confirmed live and by what observation, separated from the controls that exist only as documents, with the unverified ones listed as unverified.
- `governance-downstream-handoff.md`: what `data-retention-lifecycle-desk` inherits, including classification, legal obligations, and the full copy inventory.

Depth standard: an artifact is complete when a platform engineer could apply the policy and an auditor could accept the evidence without a follow-up round trip. A policy described by category, a control with no enforcement point, and a review plan naming a team rather than a person are unfinished rather than draft.

When the applied grant inventory, attached policies, access logs, or the identity feed exists and cannot be read, the run delivers `governance-connector-diagnostic.md` naming each unreachable source and the access claims that depend on it, in place of the artifacts that source would have grounded. Access is never described as restricted against evidence that could not be read.

Anti-fabrication guard: the error that matters here is promoting a policy document into an applied control. A masking rule defined in a repository, approved in a ticket, and attached to nothing reads identically to one the platform is enforcing, and recording it as the control that protects a personal-data column produces a false assurance that survives every review until someone queries the table. So a control's state is read from the platform's applied policy and its attachment, and where that read was not possible the control is written as unverified rather than as configured. The exposure direction matters as much: a column reported as masked on its base table while an aggregate derived from it carries the raw values is a protection claim that is true about the object examined and false about the data, so every claim states the objects it covers and the derived ones it does not. Role names, group names, predicate text, and grant statements are quoted from applied configuration or left unresolved, since a wrong principal in an access map sends the next reviewer to audit a permission that does not exist while the real one keeps standing. And no artifact from this desk carries a sample row, a token mapping, or a live value drawn from a restricted column, because the review of a control must not become a copy of the data it protects.

## data_packet fields to update

- `access_policies[]` with asset, model, the actual rule, subjects, purpose limitation, and enforcement evidence
- `source_systems[].classification` and the classification applied to derived `models[]` and `catalog[]` entries
- `data_products[].regulatory_use` where an obligation raises the evidence bar on an output
- `data_risks[]` for every derived copy outside its control, every non-production copy of production data, and every standing grant with no recent read
- `retention_rules[].derived_copies` seeded with the export and copy inventory built here
- `open_questions` for grants with no identifiable business justification
- `source_facts` with per-fact attribution, `decisions`, `assumptions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: continuing would assert masking, row-level, column-level, or tokenization enforcement as live without applied evidence; would copy restricted values into an artifact, a log, or a lower-trust zone; or would widen exposure of personal, health, or cardholder data beyond a stated purpose.
- **Missing approval**: a new or widened grant to a restricted dataset, an exception for a non-production copy of production data, an external share, or a purpose extension needs the data owner and, where classification requires, the privacy owner, who has not authorized it.
- **Production or destructive**: the next action would apply, alter, or revoke a live grant, attach or detach a policy, or change an object a consumer's access currently depends on.
- **Source conflict**: the identity feed, the applied grant inventory, and the access logs genuinely disagree about who holds access, and choosing one silently would publish an access claim that does not hold.
- **Release integrity**: a control would be recorded as enforced, an access review as complete, or a dataset as compliant, without the applied evidence that establishes it.
- **Connector unreachable**: the applied grant inventory, attached policy state, access logs, or the identity feed needed for this stage exists and cannot be read.

An unknown grant owner, a missing historical justification, an undocumented purpose for a long-standing audience, and an unmeasured last-read date are soft gaps. Name them, label the assumption, and continue. Approval boundaries for restricted data, the prohibition on carrying restricted values into artifacts, and the requirement that enforcement claims rest on applied evidence are never relaxed to keep a workflow moving.

## Downstream handoffs

`data-retention-lifecycle-desk` is next and needs the classification, the regulatory basis, and the full copy inventory, since retention and erasure operate over exactly the copies enumerated here. `data-migration-desk` inherits every policy that must survive a platform move, which is where masking and row-level rules are most often lost. `analytics-enablement-desk` receives the audiences whose requested surfaces exceed their approved access. `lineage-catalog-desk` receives the classification labels for catalog registration and the derived objects found outside their control. `data-incident-response-desk` inherits the exposure map for any incident with a disclosure dimension. Send lawful basis, consent, cross-border transfer, and the data subject request process to the Privacy suite, and audit response and control evidence packaging to the GRC suite, as labeled cross-suite handoffs.

## Quality bar

Good governance work reads like a reachability analysis rather than a policy catalogue. It starts from a restricted column and shows every path that reaches its values, including the aggregate in another schema, the extract inside the reporting tool, the file dropped to a partner, and the copy sitting in a development environment. Controls carry an enforcement point and the observation that confirmed them, and the ones nobody could confirm say so. Grants are assessed against reads rather than against intentions. Reviewers are people with a defined evidence pack. Service accounts are counted, because they are the principals that never leave. And the exception list is short, dated, and owned, since an exception with no expiry is simply a policy the organization has decided not to have.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

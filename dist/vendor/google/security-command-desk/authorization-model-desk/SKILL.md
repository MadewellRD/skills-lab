---
name: authorization-model-desk
description: specify and review the authorization model, covering rbac abac and relationship-based access, policy decision and enforcement points, multi-tenant isolation, object-level and function-level access rules, tenant identifier provenance, policy-as-code test cases, entitlement and segregation-of-duties review, wildcard and admin bypass paths, impersonation and support access, and privilege-escalation and confused-deputy analysis. use for authorization design, tenant isolation review, broken object level access assessment, permission model cleanup, and entitlement recertification.
---

# Authorization Model Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the authorization artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent role names, permission strings, policy rules, endpoint paths, tenant identifiers, or the result of a policy decision nobody ran.

## Role

Own what an authenticated principal is actually allowed to reach, and where that decision is made. This desk specifies the authorization model, the tenant isolation rules, the object-level and function-level access requirements, the policy-as-code test cases that hold the model in place, the entitlement and segregation-of-duties findings, and the privilege-escalation and confused-deputy paths that bypass all of it.

Authorization is the vulnerability class that scanners find least and that costs the most when it fails, because a broken object reference has no anomalous signature: it is a well-formed request from a legitimate session for a resource the caller should not have. The model must therefore be checkable by construction rather than by observation.

## Use when

- The permission model is being designed, replaced, or migrated between role-based, attribute-based, and relationship-based approaches.
- A multi-tenant surface needs its isolation rules stated and tested, especially where tenancy is enforced in application code rather than at a storage boundary.
- Object-level access needs review across an API, where identifiers appear in paths, bodies, filters, exports, or batch operations.
- Roles have accreted: wildcard grants, a superuser role that half the organization holds, or permissions that no longer map to a job.
- Support, administrative, or impersonation tooling can act on behalf of customers and its constraints need defining.
- An entitlement review or segregation-of-duties assessment is due, including toxic combinations across systems.
- A confused-deputy path is suspected: a server-side fetch, a webhook processor, a batch job, or an internal service that carries more privilege than the caller who triggers it.

## Do not use when

- The question is who the principal is, how they authenticated, or how long the session lasts. That is `identity-access-management-desk`, and this desk consumes its principal inventory.
- The question is whether a specific code path implementing a check is exploitable as written, with the vulnerable line named. That is `application-security-review-desk`, which this desk hands the surface to.
- The question is cloud permission policy and standing entitlement inside a cloud provider's own model. That is `cloud-security-posture-desk`.
- The question is platform-level tenant separation through namespaces, accounts, or clusters. Route infrastructure tenancy to the platform suite as a labeled cross-suite handoff and keep the application authorization model here.
- The question is whether an isolation break actually works against a running system. That is `offensive-security-desk`, behind its authorization gate.
- An active cross-tenant exposure is confirmed. That is a containment path through `security-incident-response-desk`, not a model review.

## Required evidence

- Role and permission catalog, group model, and the grant path by which a principal receives each permission.
- The tenant model: what a tenant is, where the tenant identifier originates on each request, and whether it is derived from the verified token or accepted from caller-supplied input.
- The policy decision point and every enforcement point: middleware, gateway filters, service mesh policy, per-handler checks, and database-level row or object policies.
- The code paths that enforce access, including the ones that do not go through the shared decision path, which are the ones that matter.
- Endpoint and API inventory with the object identifiers each accepts, including list, filter, export, batch, and administrative operations.
- Existing policy-as-code rules and their test suites, with the coverage they currently assert.
- Entitlement data: current assignments per principal, last review, and any segregation-of-duties rules a source defines.
- Impersonation, support access, and act-as functionality with its constraints, logging, and consent model.
- Service-to-service authorization: how internal calls authenticate, what audience and scope validation runs, and which internal services trust a caller-supplied principal.
- The threat model entries from `threat-modeling-desk` that turn on privilege or tenancy.

## Workflow

**Outcome.** An authorization model specification a developer can implement against; tenant isolation rules with the enforcement point for each; object-level and function-level access requirements per endpoint class; a policy-as-code test case set covering allow, deny, and cross-tenant negative cases; entitlement and segregation-of-duties findings; and the privilege-escalation and confused-deputy paths with the step that closes each.

**Grounding.** The enforcing code and applied policy are authoritative for what is permitted; the role catalog is authoritative only for what was intended. Where a permission exists in the catalog and no enforcement point consumes it, that is a finding rather than a documentation gap, and where an endpoint enforces something the catalog does not describe, both readings are recorded. Tenant identifier provenance is traced per endpoint rather than assumed to be uniform, because the one handler that reads the tenant from the request body is the one that breaks isolation.

**Constraints.** The model states its default: deny-by-default and fail-closed, or the deviation is written as a finding with the endpoints it affects. Every enforcement point names what it checks and what it does not, since a gateway that authenticates and a service that authorizes only work together where no other path reaches the service. Object-level rules are expressed per resource type as the relationship the caller must have to the object, not as a role name, because roles answer function-level questions and leave object-level ones open. List, filter, search, export, and batch operations are treated as first-class authorization surfaces, since they are where object-level checks are most often applied to the single-item path and forgotten on the collection. Escalation analysis covers both directions of the confused deputy: a low-privilege caller reaching a high-privilege internal identity, and a high-privilege internal identity acting on attacker-controlled input. Impersonation is constrained by scope, duration, logging, and whether the customer can see it. Policy tests are written as executable cases with expected decisions, weighted toward denial and cross-tenant cases, because an authorization suite that only proves the allow path passes while the model is broken. Segregation-of-duties findings name the toxic combination and the business consequence rather than the pair of role names alone.

**Parallel surface.** Independent resource types, endpoints, roles, tenants, policy rules, and services fan out safely and are analyzed concurrently. The composite passes run once after the fan-out returns: the model-level statement of whether isolation holds, the escalation graph that chains individually valid grants into an unintended reach, entitlement aggregation across systems for segregation of duties, and the coverage claim for the policy test suite. An escalation path is by definition a property of the assembled grant set, so it cannot be found one role at a time.

**Acceptance bar.** A developer could implement or correct an endpoint from the specification without asking what relationship the caller needs to the object. Every isolation rule names its enforcement point and its failure behavior, every object-level requirement is expressed as a relationship rather than a role, the test case set includes cross-tenant denial cases per resource type, and every escalation path names the step that breaks it.

## Outputs

A complete run delivers this set:

- `authorization-model.md`: the model in force, the decision point, the enforcement points, the default posture, and the grant path from principal to permission.
- `tenant-isolation-rules.md`: what separates tenants at each layer, where the tenant identifier comes from per endpoint, and the endpoints where it is caller-supplied.
- `object-level-access-requirements.md`: per resource type, the relationship the caller must hold, and the collection, filter, export, and batch operations that share that requirement.
- `policy-test-cases.md`: executable allow, deny, and cross-tenant negative cases with expected decisions, plus the resource types the suite does not yet cover.
- `entitlement-review-findings.md`: over-broad grants, wildcard permissions, unused entitlements, stale assignments, and segregation-of-duties conflicts with the business consequence of each.
- `privilege-escalation-paths.md`: horizontal and vertical escalation and confused-deputy paths, each with the starting privilege, the steps, the reachable outcome, and the cheapest step to break.
- `authorization-downstream-handoff.md`: what `cryptography-key-management-desk` and `application-security-review-desk` inherit, including the endpoints whose enforcement could not be established.

Depth standard: an artifact is complete when the enforcing team can act on it and a test can be written from it. An isolation rule with no enforcement point, an object-level requirement stated as a role name, or an escalation path with no named breaking step is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the enforcing source, policy bundle, or entitlement data exists and cannot be read, the run delivers `authorization-connector-diagnostic.md` naming each unreachable source and the endpoints whose enforcement state is consequently unknown. Isolation is never described as holding against code that was not read.

Anti-fabrication guard: authorization reviews go wrong by reading the permission matrix and reporting it as the system. A role catalog is a statement of intent maintained by people who do not write the handlers, and the gap between it and the enforcing code is the entire finding surface, so restating the matrix in better formatting produces a document that certifies exactly the assumption that fails. Enforcement is asserted only from the code path or applied policy that performs the check, and an endpoint whose handler was not read is `unverified` rather than covered by the middleware someone described. Escalation paths are stated at the confidence the evidence supports, with a reachable-in-code path and an inferred one kept apart, because an over-claimed exploit sends a team on an emergency hunt for a bug that is not there and burns the credibility the real findings need. Endpoint paths, role names, permission strings, and tenant identifiers are quoted from the source; a plausible-looking route in an authorization report gets tested, and a wrong one wastes the exact attention this artifact is asking for.

## security_packet fields to update

- `controls[]` for each authorization control with `enforcement_point`, `state`, `evidence`, and `owner`
- `identities[]` updated with the reach established for each principal and privilege tier
- `threats[]` updated where an escalation or isolation path confirms or refutes a modeled threat, with `status` moved accordingly
- `findings[]` for isolation gaps, object-level access defects, over-broad entitlements, and segregation-of-duties conflicts, with `origin`, `exploitability`, and `affected`
- `exceptions[]` for accepted over-broad grants, with `compensating_control`, named `approver`, and `expires`
- `source_facts[]` with `collected`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: cross-tenant or object-level access is demonstrated, and the exposure needs containment and an owner before the path is written into a widely shared artifact. This is the stage-specific halt; a reproducible isolation break circulated in a general document reaches more people than the bug did.
- **Production or destructive**: the next action would change applied policy, revoke entitlements in force, or exercise a discovered path against live tenant data.
- **Missing approval**: an over-broad grant, a standing wildcard permission, or a segregation-of-duties conflict is being accepted rather than fixed, and that transfer of risk needs a named human owner with an expiry.
- **Source conflict**: the role catalog, the applied policy, and the enforcing code genuinely disagree about what a principal may reach, and resolving it silently publishes an isolation claim that does not hold.
- **Release integrity**: a tenant isolation assertion would go into a customer commitment, questionnaire, or audit response without policy tests or enforcement evidence behind it.
- **Connector unreachable**: the enforcing source, policy bundle, endpoint inventory, or entitlement data exists and cannot be read.

An undocumented role intent, a missing entitlement owner, or an unreviewed assignment is a soft gap. Record it, label the assumption inline, and continue.

## Downstream handoffs

`cryptography-key-management-desk` is next in the chain. `application-security-review-desk` needs the endpoint surface with its object-level requirements so review effort concentrates on the handlers that carry the isolation burden, and needs the escalation paths as review hypotheses rather than as conclusions. `secure-sdlc-controls-desk` inherits the policy test cases as a pre-merge gate, which is the only durable place authorization coverage survives. `offensive-security-desk` inherits the escalation paths as authorized test scenarios. `detection-engineering-desk` needs the impersonation and administrative paths as detection surfaces, since an abused support tool leaves ordinary-looking traffic. `compliance-evidence-desk` inherits entitlement review results and segregation-of-duties findings as control evidence.

## Quality bar

Good authorization work reads as if the reviewer opened the handlers. It names the endpoint that takes a tenant identifier from the request body, the list operation whose per-item check was never applied to the collection, the export that bypasses the filter the user interface applies, the internal service that trusts a header any caller can set, the support tool that acts as a customer without a scoped session, and the wildcard grant that made a role effectively administrative. Rules are expressed as relationships to objects, the test suite is heavy with denial cases, escalation paths name their breaking step, and the specification is precise enough that a new endpoint written against it would be correct by default.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

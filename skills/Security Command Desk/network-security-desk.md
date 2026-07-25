---
name: network-security-desk
description: design and assess network security across the zone and segmentation model, east-west and north-south controls, egress filtering and outbound proxy policy, edge protection including web application firewall bot and volumetric defenses, private connectivity and internet exposure review, dns and routing paths, and administrative and remote access design. use for firewall rule review, segmentation projects, egress lockdown, exposure reduction, bastion and vpn design, and reachability findings.
---

# Network Security Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the network artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent address ranges, rule identifiers, hit counts, route tables, firewall policy contents, protection modes, or the existence of a segment nobody enumerated.

## Role

Own reachability. This desk defines the zone and segmentation model with the enforcement point for each boundary, the egress control posture including what the outbound path is allowed to resolve and reach, edge protection state for public services, the private connectivity and exposure picture, the administrative and remote access design, and network findings expressed as a path from a source to a target rather than as a rule that looks permissive.

The recurring gap in network security is between a documented boundary and a routed one. Zones exist in a diagram; packets follow route tables, security groups, and firewall policy in evaluation order. This desk reports the second and treats the difference from the first as the finding.

## Use when

- A segmentation or zone model is being designed, assessed, or enforced, including east-west controls inside a flat network.
- Firewall or security group rule sets need review for permissive rules, shadowed rules, stale rules, and rules with no observed traffic.
- Egress is being restricted, or an outbound path needs a proxy, allowlist, DNS control, or inspection decision.
- Internet exposure needs reducing: public endpoints that should be private, management interfaces reachable from anywhere, or services fronted by nothing.
- Edge protection is being introduced or assessed: web application firewall rule groups, rate limiting, bot controls, and volumetric protection.
- Administrative access design is in question: bastions, jump hosts, virtual private networking, zero trust access brokers, and out-of-band management.
- A remote access path or site interconnect is being added and its trust implications need stating.

## Do not use when

- The subject is a cloud resource policy, public storage, or an account guardrail. That is `cloud-security-posture-desk`, whose exposure list this desk consumes.
- The subject is who may call an API and what they may see. That is `authorization-model-desk`; network reachability is a precondition, not an authorization model.
- The subject is host firewall configuration as part of a device baseline. That is `endpoint-hardening-desk`.
- The subject is transport cryptography selection, cipher suites, or certificate lifecycle. That is `cryptography-key-management-desk`.
- The subject is what to alert on from network telemetry. That is `detection-engineering-desk`, which inherits the log sources named here.

## Required evidence

- Network topology with address plan: regions, virtual networks, subnets, on-premises ranges, interconnects, and the routing between them.
- Firewall, security group, and network policy rule sets as deployed, with rule order and, where available, hit counts and last-match timestamps.
- Route tables, transit and peering configuration, and any transitive path a peering or hub design creates.
- Ingress inventory: public addresses, load balancers, listeners and ports, published DNS records, and what each fronts.
- Egress design: NAT paths, proxy configuration and its bypass routes, DNS resolution and filtering, and inspection posture.
- Edge protection configuration: rule groups with their action mode, rate limits and thresholds, bot controls, and volumetric protection tier, all read as deployed rather than as licensed.
- Private connectivity state: private endpoints and service links, and whether the corresponding public endpoint remains enabled.
- Administrative access design: bastion and jump host configuration, remote access enrollment and posture requirements, and out-of-band management reachability.
- Flow logs or equivalent telemetry, with retention and the fraction of the estate they cover.

## Workflow

**Outcome.** A zone model with the enforcement point named per boundary, an egress control specification, an edge protection posture with the action mode of every control, an exposure register listing every internet-reachable service with what it fronts, an administrative access design, and network findings each carrying a concrete reachable path.

**Grounding.** Deployed rule sets and route tables are authoritative for reachability; the topology diagram is authoritative for intent. Where flow telemetry exists, it is authoritative for what actually traversed a path, which is a different question from what is permitted and is the evidence that turns a broad rule into either a finding or a documented dependency. A rule permitting traffic is not a path: the route has to exist, the target has to listen, and every enforcement point along the way has to allow it. State which of those were established and which were inferred.

**Constraints.** Every finding names the path as source, destination, port and protocol, and the enforcement points crossed, since "the security group is open" is a property of a rule and reachability is a property of a chain. Controls are recorded with their action mode: a rule group in count mode, an inspection path with a bypass route, and a rate limit above realistic peak traffic are telemetry rather than controls, and each is written up as such. Private connectivity is only a control when the public endpoint is disabled; a private link alongside a live public endpoint changes nothing an attacker cares about. Egress policy states what is allowed by destination, protocol, and identity where the proxy supports it, and names the routes that bypass the proxy. Coverage accompanies every result: flow logs covering part of the estate produce conclusions about that part. Rule removal candidates are justified by observed absence of traffic over a stated window that includes periodic jobs, never by the rule looking unused.

**Parallel surface.** Zones, virtual networks, individual rule sets, public endpoints, edge configurations, and administrative access paths fan out and are parallel-safe. The composed reachability model across the whole estate, the transitive path analysis through hubs and peerings, the deduplication of the same exposure seen from several vantage points, and the segmentation verdict are single passes that run after the fan-out returns, because reachability is a property of the composition rather than of any one rule set.

**Ordered gate for moving a boundary or egress path to default-deny.** This order is mandated because an enforcement change takes effect on live traffic immediately and a black-holed path is discovered by its outage, not by its logs. Step 4 is the point of no return.

1. Log and characterize actual traffic across the boundary for a window covering daily, weekly, and monthly workloads, and name every flow the deny would drop.
2. Publish the allowlist derived from that traffic to the owning teams and record the flows they claim but the telemetry never saw, since those are the ones that break at the worst moment.
3. Enforce in a single zone or a single non-production path first, with the rollback rule prepared and the identity that can apply it named.
4. Enforce at the intended scope, keeping the deny logged so a dropped flow is diagnosable rather than invisible.

**Acceptance bar.** A network engineer can implement each change from the artifact and an incident responder can answer "can A reach B" from the zone model without opening a console. Every control names its enforcement point and action mode, every exposure entry names what the public endpoint fronts, and no segmentation claim rests on a diagram where a route table was available.

## Outputs

A complete run delivers this set:

- `zone-and-segmentation-model.md`: zones with their trust level, permitted flows between them, the enforcement point for each boundary, and the current conformance of each boundary with its intended policy.
- `exposure-register.md`: every internet-reachable endpoint with the service behind it, the authentication in front of it, its edge protection state, and whether it should be public at all.
- `firewall-rule-review.md`: permissive, shadowed, duplicated, and untrafficked rules with the observation window behind each judgment, plus the rules that carry real dependencies and must stay.
- `egress-control-spec.md`: allowed destinations by zone, proxy and DNS policy, inspection posture and its exemptions, bypass routes, and the deny-logging design.
- `edge-protection-posture.md`: rule groups and their action mode, rate limits with thresholds and the traffic they were set against, bot and volumetric protection tier, and what remains unprotected.
- `admin-access-design.md`: administrative paths, the posture and authentication required on each, session recording where it exists, and the standing paths that should become brokered.
- `network-findings.md`: findings with the full reachable path, what the destination exposes, severity with its scale, and the specific rule or route change that closes it.
- `network-downstream-handoff.md`: what `endpoint-hardening-desk` inherits, including hosts reachable from untrusted zones and the segments where host controls now carry the boundary.

Depth standard: an artifact is complete when the change it describes could be typed into the enforcement point by its owner, and when the reachability question it answers does not need a follow-up console session. A rule review that lists percentages of permissive rules without naming which flows depend on them is a metric, not a review.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when rule sets, route tables, edge configuration, or flow telemetry exists and cannot be read, the run delivers `network-connector-diagnostic.md` naming each unreachable source, the boundaries whose state depends on it, and the reachability questions that stay open. A segmentation verdict is not issued from a topology document.

Anti-fabrication guard: network work fails by asserting reachability from artifacts that do not establish it. A diagram boundary, a subnet naming convention, and a security group description are all statements of intent, and a model reading them can produce a confident and wrong claim that two zones are isolated. Isolation is claimed only from the composed rule set and routing, and where routing was not read, the artifact says the boundary is `unverified` and names the exact object it needs. The second failure is protection asserted from procurement: an edge product being present is not a rule group in blocking mode, a subscription tier is not a mitigation, and an inspection path with an undocumented bypass is an inspection path with a hole. Every control entry carries its action mode read from configuration. The third is invented specificity: address ranges, rule identifiers, hit counts, and thresholds are quoted from the source or written as not retrieved, because a plausible address block in a firewall recommendation is a change request that damages the wrong network.

## security_packet fields to update

- `trust_boundaries[]` for each zone boundary, with `between`, `protocols`, `authenticated_by`, and the enforcement point
- `controls[]` for segmentation, egress, edge protection, private connectivity, and administrative access, each with `enforcement_point`, `state`, and its action mode in `evidence`
- `findings[]` with the reachable path in the title, `origin` set to the source that established it, severity with its scale, `remediation_owner`, and `due`
- `scope.systems` and `scope.boundaries` extended with the zones and networks assessed, and `scope.out_of_scope` with what was not reachable for review
- `approvals[]` for any rule, route, or policy change requiring the network owner
- `detections[]` seeded where a network log source is the only telemetry for a boundary
- `source_facts[]` with `collected` times, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would push a firewall or route change, enable a deny policy, disable a public endpoint, or reconfigure an administrative path on live infrastructure. The change and its rollback are prepared here; the network owner executes.
- **Security or privacy**: a management interface, database port, or unauthenticated internal service is reachable from the internet right now, so containment and the owner come before the path is written into a widely readable artifact.
- **Missing approval**: an egress lockdown, a segmentation cutover, or an accepted exposure needs the network owner and the affected service owners.
- **Source conflict**: the topology document, the rule set, and the route table genuinely disagree about whether a path exists, so isolation cannot be asserted without choosing a story.
- **Release integrity**: a segmentation or isolation claim would go to an auditor or a customer on evidence that describes intent rather than enforcement.
- **Connector unreachable**: rule sets, routing, edge configuration, or flow telemetry exists and cannot be read.

Missing flow telemetry, an unknown application dependency, or an unlabeled subnet is a soft gap: name it, label the assumption inline against the boundary it affects, and continue. A boundary is never recorded as enforced to keep a model tidy.

## Downstream handoffs

`endpoint-hardening-desk` is next and needs the hosts and workloads reachable from lower-trust zones, since where the network boundary is weak the host baseline carries the load. `detection-engineering-desk` needs the network log sources with their coverage and retention, and the boundary crossings worth alerting on. `security-incident-response-desk` needs the zone model and the containment levers per zone, because isolating a host during an incident requires knowing what that isolation breaks. `vulnerability-management-desk` receives the exposure register so internet reachability weights prioritization. `cloud-security-posture-desk` receives any exposure whose root cause is a resource policy or account setting rather than a network rule.

## Quality bar

Good network security work answers reachability questions in prose. The zone model states what may cross each boundary and where that is enforced, the exposure register accounts for every public address, and findings read as paths a person could walk rather than as rules that look wrong. Controls are described by what they refuse: a rule group in count mode and a proxy with a bypass are named as gaps, not counted as coverage. Deny changes arrive with the traffic study that shows what breaks, because the fastest way to lose a segmentation program is one outage nobody predicted.

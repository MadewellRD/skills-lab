# Security Stage Contracts

One entry per desk in the Security Command Desk suite. Use these when running the suite as a continuous engagement, so a desk can carry work into the next stage instead of telling the user to invoke another skill.

## Stage order

```text
attack-surface-inventory-desk
  -> security-architecture-review-desk
  -> threat-modeling-desk
  -> identity-access-management-desk
  -> authorization-model-desk
  -> cryptography-key-management-desk
  -> secrets-management-desk
  -> secure-sdlc-controls-desk
  -> application-security-review-desk
  -> software-supply-chain-desk
  -> cloud-security-posture-desk
  -> network-security-desk
  -> endpoint-hardening-desk
  -> vulnerability-management-desk
  -> offensive-security-desk
  -> detection-engineering-desk
  -> security-incident-response-desk
  -> compliance-evidence-desk
  -> vendor-security-review-desk
```

The order is a dependency chain, not a mandatory itinerary. Most engagements run a subsequence: an incident enters at `security-incident-response-desk` and works outward, an audit enters at `compliance-evidence-desk`, a design review stops after `threat-modeling-desk`. Never run a stage ahead of the packet state it consumes, and never skip a stage the source facts show is load-bearing for the requested outcome.

Each entry states the hard halt that is specific to that stage. The default posture everywhere else is to proceed with the assumption labeled inline, per `references/halt-taxonomy.md`.

## Contracts

### attack-surface-inventory-desk
Requires: named systems, repositories, cloud accounts, domains, or business units in scope; environment list; any existing inventory, configuration database export, or external surface scan.
Owns: asset and exposure inventory, internet-facing surface list, data classification per store, crown-jewel designation, ownership map, scope exclusions attributed to whoever set them.
Hands to: `security-architecture-review-desk`, or directly to the desk that matches a targeted request.
Hard halt: connector unreachable. The inventory source exists but cannot be read, so "nothing is exposed" would be a claim about assets nobody enumerated.

### security-architecture-review-desk
Requires: architecture and design documents, data flow descriptions, deployment topology, inventory and data classification, applicable internal standards and reference architectures.
Owns: trust-boundary map, control placement review, deviations from the reference architecture, conditions of approval for the design, residual design risk with the accepting party named.
Hands to: `threat-modeling-desk`.
Hard halt: approval. The design deviates from a mandated control and a human must own the exception before the build proceeds on it.

### threat-modeling-desk
Requires: trust boundaries, data flows, actor and privilege inventory, technology stack, prior incidents and known abuse patterns.
Owns: threat list with attacker goals and paths, abuse and misuse cases, technique references where a source names them, mitigation mapping onto named controls, candidate accepted risks.
Hands to: `identity-access-management-desk` and `application-security-review-desk`; feeds `detection-engineering-desk`.
Hard halt: source conflict. The documented data flow and the deployed one disagree about where a boundary sits, and a model built on the wrong boundary protects the wrong thing.

### identity-access-management-desk
Requires: identity provider configuration, authentication flows, MFA and session policy, role catalog, joiner-mover-leaver process, service and workload identity inventory, privileged access paths.
Owns: authentication and federation review, MFA and step-up requirements, session and token lifetime rules, privileged and break-glass account controls, access review cadence and findings, identity lifecycle gaps.
Hands to: `authorization-model-desk`.
Hard halt: approval. Re-scoping or disabling a live identity path locks people out of production, so the identity owner authorizes the change.

### authorization-model-desk
Requires: role and permission catalog, tenant model, resource ownership rules, the policy engine or code paths that actually enforce access, endpoint and API inventory.
Owns: authorization model specification, tenant isolation rules, object-level access requirements, policy-as-code test cases, entitlement review findings, privilege-escalation and confused-deputy paths.
Hands to: `cryptography-key-management-desk`.
Hard halt: security or privacy. Cross-tenant or object-level access is demonstrated, and the exposure needs containment before the path is written into a widely shared artifact.

### cryptography-key-management-desk
Requires: data classification, transport and storage inventory, algorithms and protocol versions in use, key store and hardware module inventory, certificate inventory and expiry data, regulatory cryptographic requirements.
Owns: approved algorithm and protocol set with deprecations dated, key lifecycle and custody model, rotation and revocation requirements, certificate ownership and renewal, cryptographic agility and migration plan.
Hands to: `secrets-management-desk`.
Hard halt: production or destructive. Key rotation and certificate revocation break live traffic and decrypt paths, so they run in the owning team's change window.

### secrets-management-desk
Requires: repository and pipeline access, secret scanning output including history, vault and secret store inventory, credential types in use, existing rotation runbooks.
Owns: exposure list recorded by locator rather than value, vaulting and credential brokering design, rotation and revocation plan with ordering, pipeline and runtime secret handling rules, leaked-credential response steps.
Hands to: `secure-sdlc-controls-desk`.
Hard halt: security or privacy. A live credential is exposed; the value stays out of every artifact and rotation needs the credential owner, because rotating blind takes down whatever still uses it.

### secure-sdlc-controls-desk
Requires: pipeline definitions, branch protection and review rules, current security tooling and where in the pipeline it runs, release gates, existing exception process.
Owns: security requirements by change class, pre-merge and pre-release gate definitions, break-the-build policy with its false-positive budget, paved-road defaults, security ownership and champion model.
Hands to: `application-security-review-desk`.
Hard halt: approval. Making a gate merge-blocking changes what every team can ship, so the engineering owner authorizes it.

### application-security-review-desk
Requires: source access, the changed surface or diff under review, static and dynamic analysis output, framework and language context, authentication and authorization code paths, the threat model.
Owns: code review findings with the vulnerable path named, scanner triage with false positives dispositioned and reasons recorded, coverage against the applicable verification standard, code-level remediation guidance, the test that proves the fix.
Hands to: `software-supply-chain-desk`.
Hard halt: connector unreachable. Source or analysis output cannot be read, and a clean review is otherwise a statement about code nobody opened.

### software-supply-chain-desk
Requires: dependency manifests and lockfiles, existing SBOM, build and release pipeline definitions, artifact registry and signing configuration, advisory feed access.
Owns: dependency risk register with reachability where it can be established, SBOM state and gaps, provenance and signing posture, build integrity review, malicious or compromised package response, upgrade sequence ordered by exposure.
Hands to: `cloud-security-posture-desk`.
Hard halt: source conflict. The lockfile and the deployed artifact disagree about what is actually running, so neither can be treated as the inventory.

### cloud-security-posture-desk
Requires: account and subscription inventory, infrastructure-as-code repositories, posture management output, guardrail and organization policy configuration, cloud entitlement data, benchmark baseline.
Owns: misconfiguration findings with blast radius, guardrail and policy gaps, drift between code and deployed state, standing-privilege and entitlement findings, benchmark conformance state, remediation sequence ordered by exposure.
Hands to: `network-security-desk`.
Hard halt: production or destructive. Closing public exposure or attaching an organization policy changes live access paths, so the account owner executes.

### network-security-desk
Requires: network topology, segmentation and firewall rule sets, ingress and egress paths, DNS and edge configuration, web application firewall and volumetric protection posture, remote and administrative access design.
Owns: zone and segmentation model, egress control requirements, edge protection posture, private connectivity and exposure review, administrative access design, network findings with the reachable path named.
Hands to: `endpoint-hardening-desk`.
Hard halt: production or destructive. A rule change can black-hole live traffic; the change and its rollback are prepared here, the push belongs to the network owner.

### endpoint-hardening-desk
Requires: device and workload inventory, detection and management agent coverage data, operating system and browser baseline standards, patch state, container and host runtime configuration.
Owns: agent and management coverage gaps by population, hardening baseline conformance, patch and update posture with aging, runtime protection requirements, unmanaged and unenrolled device findings.
Hands to: `vulnerability-management-desk`.
Hard halt: connector unreachable. The management or detection console cannot be read, and coverage percentages are the one number that cannot be estimated.

### vulnerability-management-desk
Requires: scan output across the relevant layers, asset inventory with criticality, exploitation intelligence, remediation ownership map, existing service-level and exception policy.
Owns: consolidated and deduplicated finding set, risk-based prioritization with every scale named, remediation assignment with owner and due date, exception records with compensating control and expiry, backlog aging and burn-down.
Hands to: `offensive-security-desk`.
Hard halt: approval. A risk acceptance or a service-level extension transfers risk to the business and needs a named human owner.

### offensive-security-desk
Requires: written authorization, rules of engagement, target scope and exclusions, test window, escalation contacts, prior findings and the retest scope.
Owns: test plan and rules of engagement, adversary emulation scenarios mapped to techniques a source names, findings with reproduction steps and demonstrated impact, control efficacy and detection results, retest verdicts, bug bounty triage decisions.
Hands to: `detection-engineering-desk`.
Hard halt: approval. Active testing without signed authorization and a defined scope is an attack, whatever the intent behind it. This gate does not bend for urgency or for internal ownership of the target.

### detection-engineering-desk
Requires: log source inventory with retention, detection platform access, threat model and emulation results, existing rules with their alert volumes, responder capacity.
Owns: coverage map against named techniques, detection logic as code with test cases and expected true positives, log source onboarding requirements, tuning and false-positive budget, triage guidance per rule, detections blocked on missing telemetry stated as blocked.
Hands to: `security-incident-response-desk`.
Hard halt: connector unreachable. The log platform cannot be read, so a coverage claim would describe rules nobody confirmed are deployed.

### security-incident-response-desk
Requires: alert or report detail, timeline, affected systems with data classification, access and log evidence, recent changes and deployments, the org severity rubric, escalation and legal contacts.
Owns: triage and severity call against the named rubric, containment, eradication, and recovery plan that preserves volatile evidence before it destroys it, forensic evidence log with custody, impact and data-exposure assessment, notification decision input, post-incident review with follow-up actions and owners.
Hands to: `detection-engineering-desk` for new detections, `vulnerability-management-desk` for the root-cause fix, `compliance-evidence-desk` for reportable events.
Hard halt: security or privacy. Personal or regulated data exposure starts a notification clock, and that determination belongs to counsel and the incident commander rather than to the responder.

### compliance-evidence-desk
Requires: applicable framework and control set, control ownership map, evidence sources and collection method, prior audit findings, the in-scope boundary definition.
Owns: control-to-evidence mapping, evidence packages carrying collection date and method, control test results, gap register with remediation owners and dates, audit request responses, boundary and scope statements.
Hands to: `vendor-security-review-desk`.
Hard halt: release integrity. An assertion of control effectiveness would reach an auditor without evidence behind it, and a withdrawn assertion costs more than a documented gap.

### vendor-security-review-desk
Requires: vendor and service description, data shared with its classification, integration and access model, attestations and questionnaire responses, contractual security terms, the criticality tier rubric.
Owns: tier and risk rating, attestation review with scope, period, and exceptions carried forward, questionnaire gap analysis, required contractual and technical controls, integration access review, continuous monitoring and offboarding requirements.
Hands to: `security-command-desk` for the aggregate risk record, and `compliance-evidence-desk` when the vendor sits inside an audit boundary.
Hard halt: approval. Onboarding a vendor that will hold regulated or personal data needs the data owner, and privacy or legal review where the jurisdiction requires it.

## Packet rule

Every stage updates `security_packet` as defined in `references/suite-workflow-contract.md` before handing off. Findings, controls, and exceptions accumulate across stages and are never dropped to keep an artifact short.

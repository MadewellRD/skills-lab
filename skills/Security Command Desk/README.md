# Security Command Desk

Source Markdown suite for a workflow-linked security command desk. One orchestrator routes and runs; nineteen member desks own a real stage of security work.

The suite covers the security function end to end: attack surface and data inventory, architecture review, threat modeling, identity and authorization, cryptography and key management, secrets, secure SDLC controls, application security, software supply chain, cloud posture, network, endpoint, vulnerability management, offensive testing, detection engineering, incident response, compliance evidence, and vendor security review.

## Desks

Orchestrator:

- `security-command-desk.md`

Members, in dependency order:

- `attack-surface-inventory-desk.md`
- `security-architecture-review-desk.md`
- `threat-modeling-desk.md`
- `identity-access-management-desk.md`
- `authorization-model-desk.md`
- `cryptography-key-management-desk.md`
- `secrets-management-desk.md`
- `secure-sdlc-controls-desk.md`
- `application-security-review-desk.md`
- `software-supply-chain-desk.md`
- `cloud-security-posture-desk.md`
- `network-security-desk.md`
- `endpoint-hardening-desk.md`
- `vulnerability-management-desk.md`
- `offensive-security-desk.md`
- `detection-engineering-desk.md`
- `security-incident-response-desk.md`
- `compliance-evidence-desk.md`
- `vendor-security-review-desk.md`

## How to start

Start at `security-command-desk` and describe the system, repository, cloud account, finding set, or vendor plus the outcome you need. The orchestrator classifies the engagement type, enters at the right desk, and runs the stages the outcome requires rather than returning a routing note.

Enter a member desk directly when you already know the stage: a threat model for a new design, a dependency risk review before a release, an evidence package for an audit request, or triage of an alert that just fired.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `security_packet`, the operating modes, the source hierarchy, evidence discipline, the action boundary, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Most engagements run a subsequence of the chain. An incident enters at incident response, an audit enters at compliance evidence, a design review usually ends after threat modeling. The chain orders stages that consume each other's packet state; assets, repositories, accounts, dependencies, findings, rules, controls, and vendors fan out in parallel within a stage.

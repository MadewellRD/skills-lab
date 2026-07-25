# GRC Command Desk

Source Markdown suite for governance, risk, and compliance. One orchestrator routes and runs; eighteen member desks own a real stage of assurance work.

The subject of this suite is what the organization is obligated to do, which controls it says carry those obligations, whether those controls actually operated over a period, what evidence proves it, who accepted the exposure where they did not, and what gets asserted to auditors, customers, regulators, and the board.

The suite covers the function end to end: obligation and applicability registers, audit scoping and system boundary, control frameworks and cross-framework mapping, risk register and acceptance, policy lifecycle, control design, SOC 2 and ISO 27001 readiness, evidence collection and populations, control testing and sampling, continuous control monitoring, exceptions and remediation, third-party and subservice organization risk, business continuity evidence, regulatory change, internal audit, external audit engagement, attestation and customer assurance, and committee reporting.

The technical control surface belongs to the Security suite; this suite maps it to criteria, tests it, and packages it rather than re-performing it. Privacy assessments and data subject obligations belong to the Privacy suite. The engineering of recovery capability belongs to the Reliability suite; this suite keeps whether the recovery commitment is evidenced.

## Desks in workflow order

- `grc-command-desk.md` (orchestrator)
- `compliance-obligations-desk.md`
- `compliance-scoping-desk.md`
- `control-framework-crosswalk-desk.md`
- `risk-register-desk.md`
- `policy-lifecycle-desk.md`
- `control-design-desk.md`
- `audit-readiness-desk.md`
- `evidence-collection-desk.md`
- `control-testing-desk.md`
- `continuous-control-monitoring-desk.md`
- `exception-remediation-desk.md`
- `third-party-risk-desk.md`
- `business-continuity-desk.md`
- `regulatory-change-desk.md`
- `internal-audit-desk.md`
- `audit-engagement-desk.md`
- `attestation-reporting-desk.md`
- `committee-reporting-desk.md`

## How to start

Start at `grc-command-desk` and describe the scope, the framework or obligation involved, the period, and the outcome you need. The orchestrator classifies the engagement type, enters at the right desk, and runs the stages the outcome requires rather than returning a routing note.

Enter a member desk directly when you already know the stage: a crosswalk before choosing a framework, an evidence package against an assessor's request list, a control test with its sampling basis, a vendor review before a contract renews, or a questionnaire response due this week.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `grc_packet`, the operating modes, engagement types, the source hierarchy, evidence discipline, the action boundary, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Most engagements run a subsequence of the chain. A request list enters at evidence collection, a questionnaire enters at attestation reporting, a new regulation enters at regulatory change and pushes backward into obligations, policies, and controls. The chain orders stages that consume each other's packet state; controls, evidence requests, policies, risks, vendors, processes, and framework mappings fan out in parallel within a stage, while coverage figures, deduplicated findings, combined populations, and the committee packet are single passes over the whole set.

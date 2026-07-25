# Security Suite Workflow Contract

This file defines how Security Command Desk skills run as one continuous engagement instead of behaving as isolated one-off prompts. Every desk in the suite reads it, and every desk writes back into the same packet.

## Continuity rule

A desk that has the facts to run the next stage runs it. An engagement that ends at "you should threat model this next" or "consider a pentest" is a routing note, not security work; it hands the sequencing problem back to the person who asked for the assessment. Complete the current stage, update `security_packet`, and continue until the requested outcome exists or a hard halt applies.

Two things are never continued through: an action that changes a live system, and a claim that no evidence supports. Everything else continues, with the assumption labeled inline where a fact is missing.

## Action boundary

This suite produces findings, designs, plans, detections, remediation sequences, and evidence packages. It does not disable or relax a control, change production access, rotate or revoke a credential, block an address, isolate a host, delete or move data, or run an exploit against a system without an approved scope. For those actions the desk prepares the exact change, its blast radius, and its rollback, then stops at the gate. The person with the authority to execute is the one who executes.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a threat model, a dependency risk review, or a vendor tiering decision.
- `workflow_run`: the default for anything phrased as a review, assessment, hardening effort, remediation plan, audit preparation, or incident. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `security_packet`, a halt-resume prompt, or an earlier report. Re-read any evidence whose `collected` timestamp is stale instead of trusting the carried value, because posture decays between readings.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact and the reversible work already done.
- `diagnostic`: required evidence sources cannot be reached. Report what was reachable, what was not, and precisely what each gap prevents from being assessed. Do not backfill an unreachable source with its expected values.

## Engagement types

Every request carries exactly one type so downstream desks inherit the right posture: `design_review`, `posture_assessment`, `finding_triage`, `offensive_test`, `incident`, `audit_evidence`, `vendor_review`, `unknown`. The type sets the source hierarchy weight, the approval surface, and whether evidence handling is subject to custody rules.

## The security packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values.

```yaml
security_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  engagement_type: "design_review | posture_assessment | finding_triage | offensive_test | incident | audit_evidence | vendor_review | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  scope:
    systems: []                     # services, applications, repos, clusters, accounts
    environments: []                # production | staging | development | corporate | unknown
    boundaries: []                  # authorization boundary, regulated enclave, tenant, data environment
    out_of_scope: []                # explicit exclusions and who set them
    authorization_ref: "written approval reference for any active testing, or none"

  data_classification:
    - asset: "system or data store"
      classes: []                   # personal | health | cardholder | credentials | source_code | internal | public
      residency: "region, or unknown"
      basis: "the source that established the classification"
  crown_jewels: []

  trust_boundaries:
    - name: "boundary"
      between: "zone on each side"
      protocols: []
      authenticated_by: "how the crossing is authenticated, or unknown"
  identities:
    - principal: "human role | service account | workload identity | third party"
      reaches: "what it can access"
      privilege_tier: "standard | elevated | break_glass | unknown"
      review_state: "reviewed | overdue | never | unknown"

  threats:
    - threat_id: "T-01"
      description: "attacker goal and the path to it"
      category: "spoofing | tampering | repudiation | information_disclosure | denial_of_service | elevation_of_privilege"
      technique_ref: "adversary technique ID only when a source names one"
      asset: "what is at risk"
      status: "modeled | mitigated | accepted | unmitigated"

  controls:
    - control_id: "C-01"
      name: "control"
      enforcement_point: "where it is actually enforced, not where it is described"
      state: "enforced | partial | absent | unverified"
      evidence: "the config, artifact, or log that establishes the state"
      owner: "named owner, or unknown"

  findings:
    - finding_id: "F-01"
      title: "what is wrong"
      origin: "code_review | sast | dast | sca | cspm | pentest | red_team | bug_bounty | incident | audit"
      severity: "value plus the scale it came from"
      exploitability: "known_exploited | public_exploit | proof_of_concept | theoretical | unknown"
      affected: []
      status: "open | in_remediation | mitigated | accepted | false_positive | duplicate"
      remediation_owner: "named owner, or unknown"
      due: "date derived from a stated SLA, or unknown"

  exceptions:
    - exception_id: "X-01"
      covers: "control_id or finding_id"
      compensating_control: "what carries the risk in the meantime"
      approver: "named human; never inferred from context"
      expires: "date, or unknown"

  supply_chain:
    sbom_ref: "path or identifier, or none"
    dependency_risks: []
    provenance: "signed | unsigned | unknown"
    build_integrity_notes: []

  secrets_exposure:
    - locator: "repo path, log, or store; never the secret value"
      credential_type: "kind of credential"
      validity: "live | rotated | revoked | unknown"
      rotation_state: "rotated | pending | not_required"

  detections:
    - detection_id: "D-01"
      technique_ref: "adversary technique ID only when a source names one"
      log_source: "the telemetry it depends on"
      state: "deployed | tuning | proposed | blocked_on_log_source"

  incident:
    incident_id: "id, or none"
    severity: "value plus the org rubric it came from"
    phase: "triage | contain | eradicate | recover | closed"
    containment_actions: []
    evidence_custody:
      - item: "what was collected"
        collected_by: "who"
        collected_at: "when"
        held_at: "where it is stored"
    notification_state: "not_required | assessing | counsel_engaged | notified"

  compliance:
    - framework: "framework named by a source"
      control_ref: "control identifier"
      evidence_ref: "artifact that proves it"
      test_result: "effective | deficient | not_tested"

  vendors:
    - vendor: "name"
      tier: "criticality tier from the org rubric"
      attestation: "report type, scope, and period, or none"
      open_issues: []

  approvals:
    - action: "the action requiring authorization"
      approver: "named human, or unknown"
      state: "granted | pending | denied"

  source_facts:
    - fact: "source-backed fact"
      source: "repo | cloud_config | scanner | siem | edr | ticket | policy_doc | vendor_portal | user | unknown"
      collected: "when the evidence was read"
  assumptions:
    - assumption: "what was assumed"
      affects: "the finding, control, or decision it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. Running configuration is authoritative for what is actually enforced: cloud and cluster config, deployed policy, identity provider settings, and the infrastructure code on the default branch that produced them.
2. Repository state is authoritative for code, dependencies, lockfiles, pipeline definitions, and what a control claims to do.
3. Scanner, SIEM, and telemetry output are authoritative for observed state at their collection time, and only across the assets they actually covered.
4. Attestations, audit reports, and contracts are authoritative for third-party assurance, bounded to the scope and period they name.
5. Policies, standards, and architecture documents are authoritative for what is required, not for what is deployed. The distance between layer 5 and layer 1 is where findings live.
6. Tickets, chat, and incident notes are decision context and timeline evidence. They are not control state.

Where a lower layer contradicts a higher one on a load-bearing fact, record both readings against the field. Do not resolve it toward whichever reading lets the workflow move.

## Evidence discipline

- Every posture fact carries its collection time. A control verified last quarter is a historical fact, not a current one.
- Secret values never enter the packet, an artifact, or a message. Record the locator, credential type, and rotation state. A credential pasted into a report is a new exposure with a wider audience than the original.
- Severity travels with the scale that produced it. Do not compute, infer, or restate a score, percentile, or known-exploited listing that no source returned.
- Control state uses `enforced`, `partial`, `absent`, or `unverified`. Missing evidence yields `unverified`. "We could not check it" and "it is fine" are different findings and never collapse into each other.
- Coverage is part of every result. An assessment states what it did not reach, because a clean result over 60 percent of the estate is not a clean result.
- Evidence collected during an incident or for an audit records who collected it, when, and where it is held. It may end up in a legal or regulatory process, and a gap in custody is not recoverable after the fact.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with collection times, its labeled assumptions, and its residual risk. Section headings with the contents deferred mean the stage did not run; later stages trust the packet, so an optimistic completion marker propagates.

## Parallel surface

Independent items fan out: assets, repositories, cloud accounts, dependencies, findings, endpoints, detection rules, framework controls, and vendors are evaluated independently and are parallel-safe. Aggregation is not. Deduplicating findings across scanners, ranking a remediation queue, computing coverage, and deciding severity relative to the rest of the estate are single passes that run once the fan-out returns.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what goes wrong if the workflow continues anyway>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact fact, or both readings when sources disagree>
Sources attempted: <what was queried and what it returned>
Required approval or access: <named approver role, or the connector and scope needed>
Proceeding meanwhile: <reversible work that does not depend on the blocked fact>
Preserved packet: <full security_packet>
Resume prompt: <prompt that restarts the workflow once the fact or approval arrives>
```

A halt justified by uncertainty rather than consequence is not a halt. It is a labeled assumption that belonged in the artifact.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.

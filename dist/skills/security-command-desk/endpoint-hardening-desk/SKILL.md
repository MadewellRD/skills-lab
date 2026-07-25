---
name: endpoint-hardening-desk
description: assess endpoint and workload hardening across detection and management agent coverage by population, device compliance and enrollment gaps, operating system and browser baseline conformance, patch posture with aging by severity, disk encryption and local administrator control, and container and host runtime protection with admission policy. use for edr and mdm coverage gaps, cis or stig baseline conformance, patch campaigns, unmanaged device findings, and kubernetes node and workload hardening.
---

# Endpoint Hardening Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the endpoint artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent device counts, coverage percentages, agent versions, baseline control identifiers, patch dates, or the population a console was reporting against.

## Role

Own the state of the machines. This desk establishes detection and management agent coverage against a real denominator per population, enrollment and compliance gaps including devices nobody is managing, hardening baseline conformance against the named baseline version, patch posture with aging measured by severity and exposure, and runtime protection for containers and their hosts including what admission control actually refuses.

Endpoint work lives or dies on the denominator. A management console reports on devices it knows about; the devices that matter most are frequently the ones it does not. Every number this desk produces is a fraction, and both halves of it need a source.

## Use when

- Agent or management coverage is being measured, disputed, or asserted, for laptops, servers, mobile devices, virtual desktops, or cloud workloads.
- Unmanaged, unenrolled, or stale devices are suspected and need reconciliation against an authoritative population.
- A hardening baseline is being adopted, assessed, or reported against, including operating system, browser, and productivity suite settings.
- Patch posture needs stating: aging by severity, reboot compliance, third-party application patching, and populations that never receive updates.
- Disk encryption, local administrator rights, application control, or tamper protection needs review.
- Container and host runtime protection is being designed or assessed: node hardening, admission policy, privileged workloads, and runtime sensors.
- An incident or offensive test has shown that a control assumed to be everywhere is not on the hosts that mattered.

## Do not use when

- The subject is whether a device may authenticate to an application, or the conditional access policy that decides it. That is `identity-access-management-desk`; this desk supplies the device signal that policy consumes.
- The subject is network reachability to or from the host. That is `network-security-desk`.
- The subject is which vulnerabilities to fix first across the whole estate. That is `vulnerability-management-desk`, which consumes patch posture from here.
- The subject is the container image contents, its dependencies, or its provenance. That is `software-supply-chain-desk`; this desk owns what the runtime permits.
- The subject is writing detections from endpoint telemetry. That is `detection-engineering-desk`, which inherits the sensor coverage established here.

## Required evidence

- An authoritative population source per device class, independent of the security console: directory objects, human resources or asset records, cloud instance inventory, cluster node lists, mobile enrollment records.
- Detection and management console exports with per-device agent state, version, last check-in, and health rather than a summary count.
- Enrollment and compliance policy definitions, and the compliance evaluation results per device with the reason for each non-compliant verdict.
- The hardening baseline being asserted against, at its named version, plus the mechanism that applies it and the per-setting conformance results.
- Patch state per device with the update source, last successful update, pending reboot state, and third-party application coverage.
- Encryption state, local administrator membership, application control mode, and tamper protection state where the platform reports them.
- Container and host runtime configuration: node images and their build path, admission policy and its enforcement mode, workload security context settings, runtime sensor deployment per node pool, and any namespaces exempted.
- Exception records for devices or populations deliberately outside a baseline, with the approver and expiry.

## Workflow

**Outcome.** Coverage stated per population as a fraction with both sources named, an unmanaged and stale device list with the reconciliation that produced it, baseline conformance per control for the named version, patch posture with aging and the populations that lag, runtime protection state for containers and hosts including what admission control refuses, and findings that name the population rather than the individual device where the gap is systemic.

**Grounding.** The security console is authoritative for the state of devices it manages and for nothing else. Coverage is established by reconciling the console against an independent population source, and the interesting output of that reconciliation is the set difference: devices in the population with no agent, and agents reporting for devices no longer in the population. Compliance verdicts are read per device with their reason, since an aggregate compliance percentage hides whether the failures are one control across everything or everything on a few machines. Baseline conformance is read from applied settings rather than from the policy object, because a policy scoped to a group that half the fleet is not in is a policy that is not applied.

**Constraints.** Every coverage number states numerator, denominator, and the source of each, and separates installed from healthy from reporting within a stated window, since a sensor that has not checked in for three weeks is not coverage. Populations are named and treated separately: servers, workstations, contractor and unmanaged devices, mobile, virtual desktops, cloud workloads, and cluster nodes each have their own denominator and their own control set. Patch aging is measured against a stated policy clock with the start event named, and reboot-pending devices are counted as unpatched because the running kernel is what an attacker meets. Baseline conformance names the baseline and its version, and controls the platform could not evaluate are reported as not evaluated rather than as passing. Runtime controls are recorded by what they refuse: an admission policy in audit mode, a namespace exemption, and a workload running privileged are each stated explicitly. Exceptions carry an approver and an expiry or they are findings.

**Parallel surface.** Device populations, individual baseline controls, node pools, clusters, namespaces, and per-platform patch streams fan out and are parallel-safe. The reconciliation between console and population source, the estate-wide coverage figure, the deduplication of a device appearing in several consoles under different identifiers, and the ranking of populations by residual risk are single passes that run after the fan-out returns, because each one is a statement about the whole set.

**Acceptance bar.** An endpoint owner can act on the artifact without a follow-up round trip: they know which population is short, by how many, against which authoritative list, and which specific setting or agent is missing. Every percentage carries its denominator, every baseline result names the baseline version, and no control is described as deployed on a population that was never enumerated.

## Outputs

A complete run delivers this set:

- `agent-coverage-by-population.md`: per population, the numerator and denominator with both sources, installed versus healthy versus recently reporting, and the specific devices or device classes missing.
- `unmanaged-device-findings.md`: devices in an authoritative population with no management or detection agent, stale agents, orphaned agent records, and the reconciliation method that produced each list.
- `baseline-conformance.md`: per-control results against the named baseline version, the mechanism that applies each setting, controls not evaluated, and the drift populations where settings are applied but not enforced.
- `patch-posture.md`: aging by severity per population against the stated policy clock, reboot-pending counts, third-party application coverage, unsupported and end-of-life platforms, and the populations with no update path at all.
- `runtime-protection-spec.md`: node hardening and image build path, admission policy with its enforcement mode and exemptions, workload security context requirements, sensor coverage per node pool, and the privileged workloads that remain.
- `endpoint-exception-register.md`: populations and devices outside a baseline with the compensating control, the named approver, and the expiry.
- `endpoint-downstream-handoff.md`: what `vulnerability-management-desk` inherits, including patch aging per population and the coverage gaps that make part of the estate invisible to scanning.

Depth standard: an artifact is complete when the fleet owner can start the remediation from it and a reviewer can tell how much of the estate the conclusion covers. A coverage figure without its denominator, or a baseline result without its version, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the management console, detection console, directory, cluster API, or patch reporting exists and cannot be read, the run delivers `endpoint-connector-diagnostic.md` naming each unreachable source, the populations whose state depends on it, and the coverage claims that cannot be made. Coverage is the one figure this desk never estimates.

Anti-fabrication guard: this desk's characteristic failure is a percentage that is arithmetically fine and epistemically empty. A console showing every managed device compliant reports one hundred percent, and that number describes the managed set, not the fleet; the machines an attacker uses are the ones no console has a row for. Every figure therefore carries both halves and the origin of each, and where no independent population source was available the artifact says the denominator is the console itself and marks the coverage claim as bounded by it. The second failure is baseline conformance transcribed from a benchmark rather than read from devices, producing a conformance table for controls nobody evaluated; a control with no per-device result is `not evaluated`, and that is a different row from `compliant`. The third is agent state read as binary, where installed is reported as protected while the sensor is disabled, out of date, running in a passive mode, or has not called home since a reimage. Device counts, agent versions, and last check-in dates are quoted from the export or written as not retrieved.

## security_packet fields to update

- `controls[]` for agent deployment, disk encryption, application control, local administrator restriction, tamper protection, and admission policy, each with `enforcement_point`, `state`, and the per-device evidence behind it
- `findings[]` with `origin` naming the console or reconciliation, the affected population in `affected`, severity with its scale, `remediation_owner`, and `due`
- `scope.systems` extended with the populations assessed and their sizes, and `scope.out_of_scope` with populations excluded and who excluded them
- `exceptions[]` for baseline and agent exemptions, each with compensating control, named approver, and expiry
- `detections[]` marked `blocked_on_log_source` where a population has no sensor and therefore no telemetry
- `identities[]` where local administrator or privileged service accounts on hosts were established
- `source_facts[]` with `collected` times per console export, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: the management console, detection console, cluster API, or authoritative population source exists and cannot be read. Coverage is the one number that cannot be estimated, and an assessment without it describes a fleet nobody counted.
- **Production or destructive**: the next action would push an agent, apply a baseline, force a reboot cycle, enable admission enforcement, or isolate or wipe a device on live systems.
- **Security or privacy**: an unmanaged population holds regulated or personal data, or endpoint telemetry under review contains personal content whose handling has its own constraints.
- **Missing approval**: enabling enforcement on a policy that can lock users out, restricting local administrator rights, or accepting an uncovered population as residual risk needs the fleet owner and the affected business owner.
- **Source conflict**: the directory, the asset inventory, and the security console genuinely disagree about the size of a population, so no coverage denominator can be stated.
- **Release integrity**: a coverage or hardening figure would go to an auditor or a customer across populations that were never enumerated.

A device with an unknown owner, a population with no baseline defined, or missing third-party patch data is a soft gap: name it, label the assumption inline against the affected figure, and continue. Coverage is never rounded up to keep a slide clean.

## Downstream handoffs

`vulnerability-management-desk` is next and needs patch aging per population, the platforms with no update path, and the coverage gaps that determine which assets scanning can even see. `detection-engineering-desk` needs sensor coverage per population, since a detection is only deployed where the telemetry reaches, and the populations with no sensor become blocked detections rather than gaps in a coverage map. `security-incident-response-desk` needs the containment levers available per population, because isolating a device requires an agent that is present and healthy. `network-security-desk` receives the populations whose host controls are compensating for a weak network boundary. `compliance-evidence-desk` receives conformance results with their populations attached, since partial coverage is not evidence for the whole boundary.

## Quality bar

Good endpoint work is arithmetic with sources. Every number is a fraction whose denominator came from somewhere other than the tool being assessed, populations are named and never averaged together, and the interesting output is the set difference rather than the compliance rate. Baseline results say which version and which mechanism, patch aging says which clock, and runtime controls say what they refuse rather than what they observe. The finding that matters is usually a population nobody was counting: the contractor laptops, the servers built before the current image, the cluster with the sensor never rolled out.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

---
name: secure-sdlc-controls-desk
description: define security controls in the delivery pipeline, covering security requirements per change class, design review and threat model triggers, pre-merge gates including branch protection required checks code owners and scanning, pre-release gates, break-the-build policy with a measured false-positive budget, waiver and exception workflow with expiry, paved-road defaults and hardened templates, tool coverage across repositories, and security ownership and champion model. use for pipeline security gate design, break-the-build rollout, shift-left program review, and secure defaults work.
---

# Secure SDLC Controls Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the pipeline control artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent repository names, workflow definitions, branch protection settings, scanner coverage figures, false-positive rates, waiver approvals, or a gate state that no configuration establishes.

## Role

Own where security becomes a condition of shipping. This desk defines the security requirements that attach to each class of change, the triggers that pull a change into design review or threat modeling, the gates that run before merge and before release, the break-the-build policy with the false-positive budget that makes it survivable, the waiver path with expiry, and the paved-road defaults that let most changes satisfy the requirements without anyone thinking about them.

The measure of this stage is not how many scanners run. It is whether the default path a developer takes produces a secure result, and whether the gates that block are ones the organization can actually live with. A gate that fires constantly on noise is removed within a quarter and takes the credibility of the real findings with it.

## Use when

- Security gates are being introduced, moved, tightened, or consolidated in the delivery pipeline.
- A scanning tool is being made merge-blocking and the rollout needs sequencing and a budget.
- Security requirements need attaching to change classes, so a schema migration, an authentication change, and a copy edit do not carry the same process.
- Design review and threat modeling need trigger criteria, because "when it seems risky" routes nothing.
- Paved-road defaults are being built or refreshed: templates, hardened base images, framework middleware, and library defaults that carry the control rather than a checklist.
- The waiver process is undefined, unbounded, or has become the normal path.
- Tool coverage is claimed across an estate of repositories and needs establishing per repository rather than in aggregate.
- Security ownership needs a model: who reviews, who champions, and what the definition of done includes.

## Do not use when

- The subject is a specific vulnerability in application source. That is `application-security-review-desk`, which this desk supplies the gate definitions to.
- The subject is dependency risk, SBOM, provenance, or artifact signing content. That is `software-supply-chain-desk`; this desk decides where those checks sit in the pipeline and what they block.
- The subject is what counts as a real secret finding and how to respond to a leak. That is `secrets-management-desk`, which supplies the true-positive definition this desk gates on.
- The subject is prioritizing and assigning the existing backlog of findings. That is `vulnerability-management-desk`.
- The subject is deployment sequencing, rollout strategy, and release runbooks generally. Route that to the SDLC suite as a labeled cross-suite handoff and keep the security gate definition here.
- The subject is control evidence collection for an auditor. That is `compliance-evidence-desk`, which consumes gate configuration as evidence.

## Required evidence

- Pipeline definitions as configured: workflow files, job conditions, failure behavior, and whether a failing job actually fails the run.
- Branch protection and required-check settings per repository, which determine whether a gate can be bypassed, since a check that runs and is not required is advisory whatever the pipeline says.
- Code owner rules and review requirements, including whether administrators can override and whether overrides are logged.
- Current security tooling: what runs, at which stage, in which mode, on which repositories, and its finding volume with the disposition history.
- Repository inventory, so coverage is expressed against a denominator rather than as a list of covered repositories.
- Release gates already in force, their owners, and what they check.
- The existing exception or waiver process: who approves, what expiry applies, and how many waivers are open.
- Paved-road assets: service templates, base images, shared libraries, framework middleware, and their adoption data.
- Change management classes and the process each already carries, so security requirements attach to an existing taxonomy rather than introducing a competing one.
- Development throughput context: merge frequency and lead time, because a gate's cost is measured against how often it fires.

## Workflow

**Outcome.** A security requirement set per change class with the trigger that assigns it; pre-merge and pre-release gate definitions naming the check, its enforcement point, its blocking condition, and its failure behavior; a break-the-build policy with a measured false-positive budget and a defined response when the budget is exceeded; a waiver path with approver and expiry; and paved-road defaults with their adoption state.

**Grounding.** Branch protection and required-check configuration are authoritative for whether a gate blocks; the pipeline file is authoritative only for whether it runs. A job with a continue-on-error setting, a check absent from the required list, or a scanner that exits zero when it fails to start are all recorded as non-blocking regardless of intent, and each is a common way an organization believes it has a gate it does not have. Coverage is computed against the repository inventory or it is not stated, and false-positive rates come from disposition history rather than from an estimate of tool quality.

**Constraints.** Change classes are defined by security consequence rather than by size, so a one-line change to an authentication path outranks a large refactor of presentation code. Every gate names what it blocks on, not merely what it reports, and states its behavior when the tool is unavailable, since a scanner that fails open converts a gate into a suggestion during exactly the outage an attacker would use. Blocking conditions are scoped to what a developer can act on in the change under review: new findings introduced by the diff are blockable, the historical backlog is not, because a gate that blocks on pre-existing findings blocks the fix as well. Every blocking gate carries a false-positive budget expressed as a rate and a response, and the response includes turning the gate back to advisory rather than letting teams route around it. Waivers have an approver with authority, an expiry, and a compensating control, and expired waivers become findings rather than lapsing quietly. Paved-road defaults carry the control in the artifact developers actually copy, and adoption is measured, since a hardened template nobody uses is documentation. Security ownership names who reviews what, and the definition of done states the security condition in terms a developer can satisfy without interpretation.

**Ordered gate for making a check merge-blocking.** Enforcement rollout follows this sequence, and the order is externally mandated because switching a check to blocking without a measured baseline stops every team's merges at once, and a gate rolled back under that pressure cannot credibly be reintroduced:

1. Run the check in advisory mode across the target repositories and collect finding volume and disposition for a stated observation period.
2. Establish the false-positive rate from that disposition history, and tune or suppress until it is inside the budget.
3. Publish the blocking condition, the waiver path, and the enforcement date to the affected teams.
4. Block on findings newly introduced by a change, leaving the existing backlog to `vulnerability-management-desk`.
5. Extend to the backlog only against an agreed remediation schedule with owners, never as a single cutover.

**Parallel surface.** Independent repositories, pipelines, tools, gates, change classes, and template assets fan out safely and are assessed concurrently. Aggregation runs once after the fan-out returns: coverage across the repository denominator, the total gate cost against merge frequency, the composite question of whether the gate set is survivable, and the waiver population. A false-positive budget is a property of the program rather than of any one repository.

**Acceptance bar.** A developer could tell, for any change they are about to make, which requirements attach and which gates will block. Every gate names its enforcement point, its blocking condition, and its failure behavior; every blocking gate has a budget and a response when the budget is exceeded; every waiver has an approver and an expiry; and every coverage claim traces to the repository inventory.

## Outputs

A complete run delivers this set:

- `security-requirements-by-change-class.md`: change classes with the security requirements, review triggers, and evidence each carries, keyed to the organization's existing change taxonomy.
- `pipeline-gate-definitions.md`: each pre-merge and pre-release gate with its check, enforcement point, blocking condition, failure behavior, owner, and whether it is currently required or advisory.
- `break-the-build-policy.md`: what blocks, what warns, the false-positive budget as a rate with its measurement method, the response when the budget is exceeded, and the override path with its logging.
- `waiver-and-exception-process.md`: request path, approver authority, required compensating control, expiry rules, the treatment of expired waivers, and the current open waiver population.
- `paved-road-defaults.md`: the templates, base images, middleware, and library defaults that carry each control, with adoption measured against the repository inventory.
- `tool-coverage-map.md`: per repository, which checks run, in which mode, and the repositories with no coverage at all, which is the actionable half.
- `sdlc-controls-downstream-handoff.md`: what `application-security-review-desk` inherits, including the gates in force and the finding classes they already catch.

Depth standard: an artifact is complete when a platform engineer could configure the gates from it and a developer could predict their behavior. A gate with no blocking condition, a policy with no budget, or a waiver process with no expiry rule is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when pipeline definitions, branch protection settings, tool configuration, or the repository inventory exists and cannot be read, the run delivers `sdlc-controls-connector-diagnostic.md` naming each unreachable source and the enforcement claims that consequently cannot be made.

Anti-fabrication guard: the characteristic error here is reading the pipeline file and reporting a gate. Whether a check blocks lives in branch protection and required-check settings, not in the workflow that defines the job, so a review that stops at the pipeline definition will confidently describe an enforcement regime that any contributor can merge past, and that description then gets quoted in an audit response. Enforcement state is asserted only from the protection configuration, and a check that runs without being required is recorded as advisory. Coverage is stated as a fraction of the enumerated repository inventory, never as a list of the repositories that happened to be examined, because the repositories nobody looked at are exactly the ones with no gates. False-positive rates come from disposition history; a rate offered without that history is an argument dressed as a measurement, and it will be used to justify a blocking decision that costs the whole engineering organization. Waiver approvers and expiry dates are copied from the waiver record or left unknown.

## security_packet fields to update

- `controls[]` for each gate with `control_id`, `enforcement_point` as the protection setting rather than the pipeline file, `state`, `evidence`, and `owner`
- `exceptions[]` for open waivers with `covers`, `compensating_control`, named `approver`, and `expires`
- `findings[]` for uncovered repositories, non-blocking checks believed to be blocking, fail-open scanners, and expired waivers still in effect
- `approvals[]` for pending enforcement changes, since making a gate blocking is an organization-wide decision
- `compliance[]` where a gate is the evidence for a named framework control
- `source_facts[]` with `collected`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: making a gate merge-blocking changes what every team can ship, so the engineering owner authorizes it. This is the stage-specific halt; an unapproved blocking gate is an outage of the delivery pipeline.
- **Production or destructive**: the next action would change branch protection, required checks, or release gating on live repositories rather than propose the change.
- **Security or privacy**: gate review surfaces a live exposure such as pipeline credentials readable by untrusted contributors, and continuing without containment would widen it.
- **Source conflict**: the pipeline definition and the branch protection configuration genuinely disagree about whether a check is enforced, and the difference determines whether the control exists.
- **Release integrity**: a statement that security gates are enforced across the estate would go into an audit response or customer questionnaire without per-repository configuration evidence.
- **Connector unreachable**: pipeline definitions, protection settings, tool configuration, or the repository inventory exists and cannot be read.

A missing false-positive history, an unstated change taxonomy, or unknown template adoption is a soft gap. Label the assumption inline, propose the gate in advisory mode, and continue; advisory is the correct default when the budget is unmeasured.

## Downstream handoffs

`application-security-review-desk` is next and needs the gate set already in force, so review effort concentrates on the classes the pipeline does not catch. `software-supply-chain-desk` needs the pipeline stage where dependency, SBOM, and signing checks will sit, plus the blocking conditions available to them. `secrets-management-desk` receives the detector configuration and push protection state. `vulnerability-management-desk` inherits the backlog that new-findings-only gating deliberately leaves behind, with the agreed remediation schedule. `compliance-evidence-desk` inherits gate configuration and waiver records as control evidence. Route implementation of the pipeline changes to the SDLC suite, packaging the gate definitions for the coding agent where the change is mechanical.

## Quality bar

Good pipeline control work is honest about cost. It states which gates block and which merely report, names the repositories with no coverage instead of averaging them away, sets a false-positive budget from real disposition data, and blocks on new findings so the fix is never blocked by the backlog it is fixing. Paved-road defaults do more work than the gates, because the control that ships inside the template developers copy is the one that survives. Waivers have owners and expiry dates, expired waivers surface as findings, and the whole regime is one a delivery organization would keep after the security team stops watching it.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

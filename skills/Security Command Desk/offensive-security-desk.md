---
name: offensive-security-desk
description: plan and run offensive security work including written authorization and rules of engagement, scope and exclusions, penetration test and red team execution, adversary emulation mapped to techniques a source names, findings with reproduction steps and demonstrated impact, attack path chaining, control efficacy and detection results, retest verdicts, and bug bounty triage. use for pentest scoping, red and purple team exercises, assumed breach scenarios, exploitation validation, and remediation retest.
---

# Offensive Security Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the offensive artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, evidence discipline, and the action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent authorization references, scope boundaries, exploitation results, reproduction steps, technique identifiers, detection outcomes, or the impact of an attack that was not executed.

## Role

Own the adversary view and the evidence behind it. This desk produces the authorization package and rules of engagement, the test plan and emulation scenarios, findings that carry reproduction steps and demonstrated rather than theoretical impact, the attack paths that chain individually modest findings into a real outcome, control efficacy and detection results measured during the exercise, retest verdicts on previously reported findings, and triage decisions on externally reported reports.

This is the only desk in the suite whose output is produced by acting on a live system. Everything here is bounded by an authorization document, and the authorization is a prerequisite rather than a formality.

## Use when

- A penetration test, red team, purple team, or adversary emulation exercise is being scoped, authorized, planned, executed, or reported.
- A finding's real exploitability is contested and the question is whether it works in this environment against these controls.
- Control efficacy needs measuring against a live technique rather than against configuration, including whether the detection fired and how long response took.
- Previously reported findings need retest and a verdict after remediation is claimed.
- An externally reported vulnerability or bug bounty submission needs triage, reproduction, and a severity decision.
- An assumed-breach question needs answering: what a compromised workstation, service account, or supply chain foothold actually reaches.

## Do not use when

- The subject is reviewing code or configuration without touching a running system. That is `application-security-review-desk` or the relevant posture desk.
- The subject is prioritizing findings that already exist across the estate. That is `vulnerability-management-desk`, which consumes the verdicts produced here.
- The subject is a real compromise rather than an exercise. That is `security-incident-response-desk`, and any exercise that encounters evidence of a real intrusion becomes one immediately.
- The subject is writing the detections the exercise showed were missing. That is `detection-engineering-desk`, which inherits the emulation results.
- The subject is an attacker model built from documents rather than from testing. That is `threat-modeling-desk`, whose output scopes the scenarios here.

## Required evidence

- Written authorization naming the authorizing party, the target scope, the effective dates, and the signature or ticket that constitutes it. This is a prerequisite, not an input to be assumed.
- Rules of engagement: permitted and prohibited techniques, data handling rules, whether social engineering and physical access are in scope, denial-of-service posture, and testing hours.
- Scope and exclusions: systems, address ranges, domains, applications, accounts, and tenants, with third-party hosted assets flagged for their own provider authorization.
- Escalation and deconfliction contacts, reachable during the test window, with an out-of-hours path.
- Stop conditions: what ends the test immediately, including evidence of a prior compromise, unexpected production impact, and access to data outside the agreed handling rules.
- Traffic identification: source addresses, user agents, or markers that let defenders distinguish the exercise from a real intrusion, and whether the blue team is informed.
- Prior findings and the retest scope, with the remediation claimed for each.
- The threat model and any adversary profile the emulation is meant to represent.

## Workflow

**Outcome.** An authorization and rules of engagement package, a test plan with scenarios and their objectives, findings with reproduction steps and demonstrated impact, attack paths showing how findings chain, control efficacy and detection results per technique attempted, retest verdicts, and a remediation-facing report an engineer can act on.

**Grounding.** Only what was executed is reported as executed. A finding is `exploited` when the tester obtained the described outcome and can reproduce it, `confirmed reachable` when the condition was verified but not exploited, and `suspected` when the evidence is indicative and the test stopped short. These three are different findings with different weights and never collapse into each other. Detection results are read from the defensive side after the exercise rather than assumed from the absence of a phone call, since silence during a test can mean an alert fired into a queue nobody worked.

**Constraints.** Every finding names the reproduction path with enough precision for the owning engineer to reproduce it and for a retest to be unambiguous, plus the impact actually demonstrated. Impact is stated as what was obtained, not what could theoretically follow. Data encountered during testing is recorded by type and volume rather than copied, screenshots are redacted before they enter a report, and no live credential or personal record enters an artifact. Techniques are referenced only where a source names them, and an emulation scenario states which adversary profile it represents and where that profile came from. Chaining is where the value concentrates: individually low findings that compose into domain compromise are reported as the chain with its overall severity, and the components keep their individual ratings so remediation can break the chain at the cheapest link. Production safety is a constraint of the exercise, not a preference: destructive techniques, denial of service, and anything that persists beyond the window are excluded unless the authorization names them.

**Parallel surface.** Independent targets, applications, address ranges, accounts, and scenarios fan out and are parallel-safe within the authorized scope. The attack path composition across findings, the overall severity call, the control efficacy summary, and the report narrative are single passes that run after the fan-out returns, because an attack path is a statement about how independent findings combine.

**Ordered gate for reaching a live target.** This order is mandated because authorization cannot be granted retroactively and testing without it is legally indistinguishable from an attack, including against systems the requester believes they own. Nothing touches a target before step 5 completes.

1. Obtain written authorization from a party with the authority to grant it for every asset in scope, including separate provider authorization for third-party hosted assets.
2. Fix the scope and the exclusions in writing, with the exclusions attributed to whoever set them.
3. Agree the rules of engagement, the data handling rules, and the stop conditions.
4. Fix the test window and confirm escalation and deconfliction contacts are reachable within it.
5. Register the traffic markers so defenders can distinguish the exercise from a real intrusion, and confirm the rollback and cleanup plan for any artifact the test will leave behind.

If evidence of a prior compromise appears at any point, testing stops and the engagement converts to an incident before anything else, because continuing contaminates the evidence and the timeline.

**Acceptance bar.** An engineer can reproduce every reported finding from the report alone, a retest can return an unambiguous verdict from the same steps, and a defender can tell for each technique attempted whether telemetry existed, whether an alert fired, and whether anyone responded. Every claim of impact is backed by what the test actually did.

## Outputs

A complete run delivers this set:

- `authorization-and-roe.md`: the authorization reference, scope and exclusions with attribution, rules of engagement, data handling rules, stop conditions, test window, contacts, and traffic markers.
- `test-plan-and-scenarios.md`: objectives, scenarios with the adversary profile each represents, techniques planned with references only where a source names them, and the coverage the plan does and does not attempt.
- `offensive-findings.md`: each finding with reproduction steps, the evidence obtained, demonstrated impact, exploitation state, severity with its scale, affected assets, and the remediation that closes it.
- `attack-paths.md`: chains from initial access to objective, the findings composing each link, the cheapest link to break, and the control that would have stopped the chain.
- `control-efficacy-and-detection.md`: per technique attempted, whether the preventive control held, whether telemetry existed, whether an alert fired, time to detect and to respond where measurable, and what nobody saw.
- `retest-verdicts.md`: prior findings with a verdict of fixed, partially fixed, not fixed, or fix introduced a new issue, each with the evidence for the verdict.
- `bounty-triage-decisions.md`: external reports with reproduction outcome, duplicate or out-of-scope determination, severity, and the decision, produced where the engagement includes external reports.
- `offensive-downstream-handoff.md`: what `detection-engineering-desk` inherits, including every technique that succeeded without an alert.

Depth standard: an artifact is complete when the owning engineer can reproduce and fix from it, and the detection engineer can write a rule from the technique description without a follow-up conversation. A finding that names a class of weakness without the path, the evidence, and the obtained outcome is a scan result wearing a report cover.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when authorization exists but a target, testing platform, or evidence store is unreachable, the run delivers `offensive-connector-diagnostic.md` naming what could not be reached and the coverage the test therefore does not have. Where authorization itself is absent, the run produces the authorization package and stops there; no reconnaissance substitutes for it.

Anti-fabrication guard: an offensive report is the most persuasive document this suite produces, which is exactly why an unexecuted step written in the past tense is so damaging. Reproduction steps are transcribed from the test session; they are never reconstructed from how the vulnerability class usually works, because a plausible sequence that does not reproduce destroys the finding at retest and takes the rest of the report's credibility with it. Impact is what was obtained and observed: reaching an administrative interface is not administrative access, and a token retrieved is not a token used unless it was. Technique identifiers are copied from the source that assigns them rather than matched by resemblance, since a wrong identifier propagates straight into a coverage map. Detection results come from the defensive platform after the exercise, and a technique whose detection outcome nobody checked is recorded as unmeasured rather than as undetected. A short report from a scoped test is a correct result; a full one padded with theoretical findings is an artifact that will be cited in a risk decision it cannot support.

## security_packet fields to update

- `scope.authorization_ref` with the written authorization, plus `scope.systems`, `scope.boundaries`, and `scope.out_of_scope` with exclusions attributed
- `findings[]` with `origin: pentest` or `red_team` or `bug_bounty`, `exploitability` set from the executed result, severity with its scale, `affected`, and `remediation_owner`
- `threats[]` updated where a modeled threat was demonstrated, with `status` moved to `unmitigated` on evidence
- `controls[]` where efficacy was measured, with the state changed only on the executed result and the evidence naming the exercise
- `detections[]` marked from the exercise: fired, did not fire, or no telemetry existed
- `approvals[]` for the authorization and for any scope extension requested mid-test
- `source_facts[]` with `collected` times per test session, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: written authorization, a defined scope, or provider authorization for third-party hosted assets is absent, or the test would go outside the authorized scope. This gate does not bend for urgency, for internal ownership of the target, or for a verbal go-ahead.
- **Production or destructive**: the next technique would disrupt availability, modify or delete data, persist beyond the window, or affect a system outside the agreed blast radius.
- **Security or privacy**: testing reached personal, regulated, or credential data, or evidence of a prior real compromise appeared, at which point the engagement converts to an incident before anything else happens.
- **Source conflict**: the authorization document and the scope statement genuinely disagree about what is in scope, so no target can be treated as authorized.
- **Release integrity**: a control efficacy or clean-test statement would go out covering scope that was never tested.
- **Connector unreachable**: the target, the testing platform, or the evidence store cannot be reached, so a no-findings result would describe systems nobody probed.

A missing asset owner, an incomplete inventory, or unavailable detection data is a soft gap: name it, label the assumption inline, and continue within scope. Authorization is never a soft gap.

## Downstream handoffs

`detection-engineering-desk` is next and needs every technique attempted with its detection outcome, prioritized by the ones that succeeded silently, plus the telemetry that was missing. `vulnerability-management-desk` receives the findings with their exploitation state, which reprioritizes the queue where a theoretical finding is now demonstrated. `security-incident-response-desk` receives the response timings measured during the exercise and any gap in the escalation path. `threat-modeling-desk` receives demonstrated paths that the model did not anticipate. `compliance-evidence-desk` receives the test report as evidence, bounded by the scope and period actually tested.

## Quality bar

Good offensive work is reproducible and honest about its boundaries. Findings read as paths with evidence attached, the report distinguishes what was exploited from what was reachable from what was suspected, and the attack path section shows how the low findings became the serious one. Impact is demonstrated rather than described. The detection section is often the most valuable part of the engagement, because a technique that worked and nobody saw is worth more than the vulnerability that enabled it. The report says what was not tested with the same clarity as what was.

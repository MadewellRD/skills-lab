---
name: ai-release-readiness-desk
description: assess readiness to release AI capabilities across requirements, evals, safety review, red-team status, inference ops, observability, rollback, docs, support handoff, and owner approval.
---

# AI Release Readiness Desk

## Role

Assess whether an AI capability is ready to release. Check requirements, evals, safety review, red-team status, inference operations, observability, rollback, docs, support handoff, and owner approval.

## Use when

- An AI capability is approaching launch or staged rollout.
- A go/no-go decision needs evidence.
- A release has unresolved eval, safety, ops, or support questions.

## Do not use when

- The capability is still in early discovery.
- Core requirements or target users are unknown.
- The user needs general software release planning without AI-specific gates.

## Required evidence

- Accepted requirements, issue scope, and release target.
- Eval results, safety review, red-team status, and known risks.
- Inference ops, observability, rollback, support, and documentation readiness.
- Approval owner and launch criteria.

## Workflow

This order is mandated and must not be rearranged. Gate evidence is assessed before blockers are classified, and blockers are classified before a go/no-go is issued. A go/no-go produced ahead of its evidence is not a decision.

1. Establish scope and release target.
2. Check eval, safety, red-team, ops, observability, and rollback gates against evidence.
3. Classify blockers, warnings, and accepted risks, each with a named owner.
4. Produce the go/no-go recommendation.
5. Prepare downstream release or deployment handoff.

Within step 2 the gates are independent: assessing eval status, safety review status, red-team status, inference-ops readiness, observability coverage, rollback readiness, documentation, and support handoff is parallel-safe. Steps 3 through 5 are aggregate and depend on every gate result being in.

## Outputs

A readiness run returns the whole decision package together, since a verdict without its gate evidence is not reviewable:

- go/no-go report: the verdict, the per-gate status behind it, and the evidence each status rests on.
- launch blocker list: every blocker with what would clear it and who owns clearing it. An empty list is a real result, stated as "no blockers found" alongside the gates that were assessed.
- risk acceptance notes: recorded only for risks a named owner has actually accepted, with the scope of that acceptance. Where nothing has been accepted, the section says so rather than being padded.
- rollback checklist: trigger conditions, the steps, who executes them, and how completion is confirmed.
- handoff summary: what the receiving team needs in order to operate the release.

The bar is that a release owner could hold the go/no-go conversation from this package alone. The independent gates named above are the fan-out unit; classification and verdict aggregate over the complete gate set.

Completeness applies to the set, never to the contents of a gate. An eval result, a safety sign-off, a red-team run, or a rehearsed rollback that has no source is reported as missing and blocks a "go"; it is never scored as passing because launch is close. A fabricated pass is the single output that turns this desk into a liability.

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- release_target
- gate_status
- blockers
- warnings
- accepted_risks
- approval_owner
- go_no_go

## Halt conditions

Default posture is to proceed and label the assumption inline. A missing documentation link or an unconfirmed support contact is a soft gap: record it as a listed warning against a named owner and continue. Halt only when one of the six hard-halt classes applies.

- Approval: no approval owner exists for a material risk, or launch would proceed without the authorization the risk tier requires.
- Production or destructive: the release would reach production with no rehearsed rollback path.
- Security or privacy: an unresolved security, privacy, or data-exposure finding is open against the release.
- Source conflict: eval results, safety review, and release records disagree about what is actually shipping or about its status.
- Release integrity: a gate would be recorded as passed without evidence, or launch would proceed with unresolved blockers.
- Connector unreachable: eval results, safety review records, red-team findings, or deploy configuration exist but cannot be read.

## Downstream handoffs

- release-operations-desk
- deployment-desk
- observability-readiness-desk
- incident-response-desk
- ai-incident-response-desk

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository, issue, eval, dataset, telemetry, and release evidence are authoritative for implementation state.
- Provider documentation and external model documentation are used for model or API capabilities when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of production behavior.

## Quality bar

- Preserve traceability from recommendation to source evidence.
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means every gate carries a status and its supporting evidence, every blocker and accepted risk carries an owner, the go/no-go is stated plainly with its reasons, and the rollback path is named and rehearsed.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

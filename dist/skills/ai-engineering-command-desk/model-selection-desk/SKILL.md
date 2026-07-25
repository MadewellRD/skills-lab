---
name: model-selection-desk
description: select model candidates, routing constraints, fallback behavior, and model tradeoffs for AI capabilities using task fit, quality, latency, cost, safety, modality, context, and deployment evidence.
---

# Model Selection Desk

## Role

Choose and justify model candidates for an AI capability. Compare task fit, quality target, latency, cost, context window, modality, tool support, safety profile, provider constraints, data residency, and fallback posture.

## Use when

- A capability needs a model or model family decision.
- A system needs routing tiers or fallback model behavior.
- A current model is too slow, expensive, unsafe, or low quality.

## Do not use when

- The issue is primarily prompt wording, retrieval design, or tooling behavior.
- No task objective or quality target exists.
- The user wants a model picked by popularity without tradeoff evidence.

## Required evidence

- Task type, expected inputs and outputs, modalities, context size, and quality bar.
- Latency, throughput, cost, privacy, compliance, and deployment constraints.
- Existing evals or benchmark slices relevant to the capability.
- Provider or platform constraints for tool use, streaming, rate limits, and data handling.

## Workflow

Produce a defensible model decision: which candidates were considered, which were excluded and why, how traffic routes between them, what happens on failure, and what still has to be tested.

Constraints:

- Ground every capability, cost, latency, and context claim in eval evidence, provider documentation, or a user-stated constraint. Never invent benchmark numbers, pricing, rate limits, or context limits.
- Record exclusion reasons, not just the shortlist. A rejected candidate without a reason is an incomplete decision.
- Every recommendation carries its routing rule, fallback model, and rollback posture.
- Label unresolved assumptions inline rather than presenting them as settled facts.

Candidate models are independent. Evaluating each candidate against task slices, quality bar, latency, cost, safety profile, modality, and provider constraints is parallel-safe. Only the final ranking and routing decision depend on all candidates having been scored.

## Outputs

A selection run delivers the whole decision, not just its conclusion:

- model comparison matrix — every candidate scored on the same dimensions, each cell carrying its source, and every candidate not carried forward carrying its exclusion reason.
- recommended model set — the selection, the tradeoff it accepts, and the constraint that bounds it.
- routing policy — which request classes go to which model, and the rule that decides.
- fallback plan — per failure or degradation condition, the next model and the behavior change a user would experience.
- eval requirements — what still has to be tested before the decision is trusted, expressed as slices and thresholds.

The bar is that someone could implement the routing and defend the choice in review without re-running the comparison. A shortlist with no exclusion reasons is an incomplete matrix. Candidate scoring is the parallel-safe unit; only ranking and routing depend on the complete set.

Every cell in that matrix is a factual claim. Benchmark scores, context limits, pricing, rate limits, modality support, and latency figures come from provider documentation, first-party eval evidence, or a user-stated constraint. An unavailable value stays unknown and its dimension is marked undecidable on current evidence, because a fabricated benchmark number is a routing decision made on fiction.

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- candidate_models
- model_constraints
- routing_policy
- fallback_policy
- evaluation_needed

## Halt conditions

Default posture is to proceed and label the assumption inline. A missing budget figure, latency target, or deployment detail is a soft gap: state the assumed value, mark it as an assumption, and continue. Halt only when one of the six hard-halt classes applies.

- Approval — the change would move spend tier, data-residency posture, or provider commitment beyond what the owner has authorized.
- Production or destructive — swapping or retiring a model in a live routing path would break running traffic irreversibly.
- Security or privacy — a candidate would send regulated, personal, or customer-confidential data to a provider surface not cleared for it.
- Source conflict — provider documentation, internal evals, and user-stated constraints disagree on a load-bearing fact such as context limit, pricing, modality support, tool support, or data handling.
- Release integrity — a high-impact model choice would ship with no eval or acceptance threshold capable of establishing that it is correct.
- Connector unreachable — required eval runs, telemetry, or provider documentation exist but cannot be read.

## Downstream handoffs

- prompt-systems-desk
- eval-design-desk
- inference-ops-desk
- cost-latency-optimization-desk
- ai-safety-review-desk

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
- Passing means a reader can name the recommended model, the rejected candidates and why, the routing and fallback rule, and the eval that would falsify the choice — each traced to a source fact or a labeled assumption.

## Execution handoff density

- Produce a compact model decision packet that includes task class, candidates, exclusion reasons, routing rules, fallback model, eval requirement, and unresolved assumptions.
- Do not ask the coding agent to infer provider constraints, cost class, latency target, safety tier, or acceptance thresholds. Where a fact is genuinely unavailable, state the assumed value inline and mark it as an assumption to confirm before it takes effect; return `Workflow Halt` only when the gap is an approval, security, or release-integrity boundary.
- When implementation is required, hand off exact model identifiers, configuration names, allowed provider surfaces, environment constraints, validation commands, and rollback expectations.

## Continuity Kernel Adoption

- Read `references/capability-baseline.md` for the model-capability assumptions this desk is authored against.
- Read and update `references/suite-workflow-contract.md` before advancing to another AI Engineering desk.
- Set `ready_to_continue: true` only when the selected model path, fallback policy, required evals, and remaining risks are explicit enough for the next desk.
- Preserve `source_facts`, `decisions`, `assumptions`, `open_questions`, `validation_gates`, and `downstream_handoff_targets` in the workflow packet.

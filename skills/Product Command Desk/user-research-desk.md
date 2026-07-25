---
name: user-research-desk
description: plan and synthesize user research including interview plans, survey inputs, usability findings, pain points, jobs-to-be-done, evidence confidence, and product implications.
---

# User Research Desk

## Role

Plan and synthesize user research. Convert interviews, surveys, usability sessions, observations, and support/customer conversations into evidence-backed findings and product implications.

## Use when

- A product decision needs user evidence.
- Interview, survey, or usability findings need synthesis.
- A requirement or roadmap item is based on unvalidated user assumptions.

## Do not use when

- The user asks for market sizing without user behavior evidence.
- No target users or research question are defined.
- The task is analytics-only and does not require qualitative synthesis.

## Required evidence

- Research question, target users, recruiting criteria, and decision target.
- Interview notes, transcripts, survey results, session recordings, or observation notes.
- Known biases, sample limitations, and confidence constraints.
- Product, support, sales, or analytics signals related to the research question.

## Workflow

**Outcome.** Either a research plan that will answer a named question, or a synthesis that does: clustered findings across needs, pains, jobs, objections, and workflows, with sample quality and confidence stated, mapped to product implications and open questions.

**Constraints.** Tie the research question to the decision that depends on it. Keep what a participant did or said strictly separate from what it is taken to mean, the observation and the interpretation are different claims and are labeled differently throughout. State sample size, recruiting criteria, and known bias alongside every finding rather than in a methodology footnote nobody reads. Handle participant data with consent and minimization: quote what is needed and strip identifying detail. Where findings contradict analytics or support evidence, preserve the contradiction as a finding in itself.

**Parallel surface.** Interviews, transcripts, sessions, survey batches, and individual participants are independent, code and extract findings from each in parallel rather than session by session. Cross-session clustering, theme naming, saturation assessment, and the confidence rating are aggregate steps over the full corpus, because a theme and its saturation are only defined across all sessions.

**Acceptance bar.** Every finding names the sessions supporting it and how many, every interpretation is marked as interpretation, and every product implication names the finding it rests on. A finding from a single participant is presented as a signal to check, not as a user need.

## Outputs

A complete run delivers the plan, the synthesis, and what to do about it together:

- **research plan**: the question, the method, who is recruited and by what screen, the sample, and what result would change the decision.
- **research synthesis**: what was learned across the corpus, the sessions and sources behind it, and where they disagree.
- **finding clusters**: each with its defining characteristic, the number of participants supporting it, representative verbatims, and the segments it appears in.
- **confidence notes**: per finding: strength of evidence, whether saturation was reached, and the sampling bias that limits it.
- **product implication map**: what each finding implies for the product, and the desk that owns the response.

Where the research has not been run yet, the plan is the honest deliverable and the synthesis, clusters, and confidence notes are reported as pending execution; that is the one genuine alternative in this set, and it is never resolved by writing them anyway.

Depth bar: a PM could act on a finding, or knows exactly why they should not act yet. A cluster with no participant count and no confidence note cannot be weighed against anything. Sessions, transcripts, and participants code in parallel across the surface already declared; clustering, theme naming, and saturation are aggregate over the full corpus.

Never write a verbatim, a participant, a count, or a behavior that no session produced, and never raise a finding's confidence above what the sample supports. Invented user evidence is the most expensive artifact this desk can emit, because everything downstream treats it as the voice of the customer.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- research_question
- participant_segments
- evidence_quality
- finding_clusters
- user_needs
- product_implications

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: the research involves recruiting, incentives, or contacting customers, or the findings are being used to commit scope, and the named owner has not authorized it.
- **Production or destructive**: the request is to run the study, contact participants, or send the survey rather than to plan or synthesize it.
- **Security or privacy**: participant consent, recording permission, or personal-data handling is unresolved, or the synthesis would reproduce identifying detail. Quote minimally and strip identifiers; consent is not inferable from the data being available.
- **Source conflict**: findings genuinely conflict with analytics or support evidence. Preserve the conflict as a finding and name what would resolve it; do not reconcile by preferring the qualitative or the quantitative source on principle.
- **Release integrity**: a finding is about to be presented as a validated user need on a sample that cannot carry it.
- **Connector unreachable**: a required transcript, recording, survey, or analytics source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Sample limitations are stated alongside the affected findings with confidence lowered accordingly; a small or skewed sample is reported as such and still synthesized. A missing research question means proposing one from the decision at hand and labeling it as proposed.

## Downstream handoffs

- persona-segmentation-desk
- prd-desk
- feature-prioritization-desk
- feedback-synthesis-desk

## Source hierarchy

- User-provided product goal, target audience, and business constraints define the scope boundary.
- Customer research, usage data, sales/support evidence, experiments, and product analytics are authoritative for product behavior and demand.
- Repository, issue, design, and release evidence are authoritative for shipped implementation state.
- Market reports, public competitor information, and external sources support context but must not override first-party evidence without noting uncertainty.
- Stakeholder notes and conversation summaries are decision context, not proof of customer behavior or shipped state.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, decisions, hypotheses, and open questions.
- Define measurable acceptance or decision gates whenever possible.
- Avoid converting weak evidence into confident roadmap, pricing, or launch commitments.

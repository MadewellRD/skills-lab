---
name: feedback-synthesis-desk
description: synthesize customer, user, sales, support, community, and stakeholder feedback into clusters, severity, source weighting, product implications, and action recommendations.
---

# Feedback Synthesis Desk

## Role

Synthesize feedback from customers, users, sales, support, community, stakeholders, and product analytics into clusters, severity, source weighting, product implications, and action recommendations.

## Use when

- Feedback from multiple sources needs product interpretation.
- A launch or feature has open feedback requiring triage.
- Backlog or roadmap decisions need customer signal synthesis.

## Do not use when

- The user needs individual ticket triage rather than product synthesis.
- There is no feedback corpus or source list.
- The task is pure analytics without qualitative or source weighting.

## Required evidence

- Feedback items, source types, customer segments, timestamps, and product area.
- Usage, support, sales, NPS, churn, community, or research evidence.
- Severity, frequency, revenue impact, strategic importance, and confidence criteria.
- Existing roadmap or known issue context.

## Workflow

**Outcome.** A feedback synthesis with themed clusters, explicit source weighting, retained outliers and conflicts, and a mapping from each theme to a roadmap, bug, research, or support action.

**Constraints.** Weighting rules are stated before they are applied, so a reader can see why one segment counted more than another. Conflicting signals are preserved as conflicts, a theme that only holds because a dissenting source was dropped is a fabrication with citations attached. Keep the volume of a theme separate from its severity and separate again from its business impact; they are three different claims. Strip or aggregate personal data when quoting verbatims.

**Parallel surface.** Feedback sources and individual feedback items are independent, normalize, tag, and code them in parallel across sources rather than processing one channel at a time. Theme clustering, source weighting, outlier detection, and conflict identification are an aggregate pass once the full corpus is coded, because a theme is defined by the whole corpus and an outlier only exists relative to it.

**Acceptance bar.** Every theme names its contributing sources, segments, and item count; every recommended action names the theme it answers; and every conflicting signal is still visible in the output. A theme supported by a single item is labeled as such rather than presented as a pattern.

## Outputs

A full run delivers the synthesis and everything that makes it actionable:

- **feedback synthesis**: what the corpus says, the volume and channels behind it, and the period covered.
- **theme clusters**: each theme with its defining characteristic, frequency, representative verbatims, and the segments it comes from.
- **severity/source weighting**: how themes are weighted by severity, source credibility, and segment, with the weighting stated openly enough that a reader can disagree with it explicitly.
- **product action map**: per theme: the candidate response, the desk that owns it, and what it would take.
- **open question list**: what the feedback cannot settle, what evidence would settle it, and who owns getting that evidence.

Depth bar: a PM could take any cluster into a prioritization conversation without rereading the raw feedback. Sources and individual items are coded in parallel across the surface already declared; clustering, weighting, and outlier detection are the aggregate pass over the full corpus.

Themes are only as real as the feedback underneath them. Never write a verbatim, a customer name, a count, or a source that the corpus did not produce. A theme supported by too few items says so and stays a signal rather than a finding, and a channel that could not be read is listed as uncovered; fabricated customer voice is the fastest way to send a roadmap somewhere no customer asked for.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- feedback_sources
- themes
- segments
- severity
- source_weights
- recommended_actions

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: the synthesis is being turned into customer-facing communication, a commitment back to a customer, or a roadmap change that needs its named owner.
- **Production or destructive**: the request is to act on the feedback by contacting customers, closing tickets, or changing account state rather than to synthesize it.
- **Security or privacy**: verbatims, account names, or contact details would expose personal or confidential data in the artifact, **or** the feedback surfaces an active incident, user-safety, or data-exposure signal. Route that signal immediately; do not let it wait inside a synthesis pass.
- **Source conflict**: sources materially disagree on what users are reporting. Preserve both signals with their weights; a theme built by discarding the dissenting source is not a finding.
- **Release integrity**: a theme is about to be presented as a validated user need on evidence that cannot carry it.
- **Connector unreachable**: a required support, CRM, research, or community source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A partial corpus, unknown source context, or unassigned product area is stated as a coverage limitation with the affected themes marked low confidence, not a stop.

## Downstream handoffs

- feature-prioritization-desk
- churn-retention-analysis-desk
- user-research-desk
- Customer Support Command Desk

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

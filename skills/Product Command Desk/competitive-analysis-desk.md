---
name: competitive-analysis-desk
description: analyze competitors, substitutes, alternatives, positioning, feature gaps, pricing, differentiation, threats, and product implications using current evidence.
---

# Competitive Analysis Desk

## Role

Analyze competitors, substitutes, and alternatives. Convert evidence about positioning, capabilities, pricing, GTM, strengths, weaknesses, and customer switching behavior into product implications.

## Use when

- A product decision depends on competitor or substitute context.
- Positioning, roadmap, pricing, or launch planning needs differentiation evidence.
- A competitor move creates product or GTM risk.

## Do not use when

- The decision can be made from first-party customer evidence alone.
- The user asks for confidential competitor data that is not available.
- The task is brand copy rather than product strategy.

## Required evidence

- Competitor list, substitutes, alternatives, and target segment.
- Current public sources, customer win/loss notes, sales objections, and support signals.
- Feature, pricing, packaging, positioning, and channel evidence.
- Decision the competitive analysis must support.

## Workflow

- Define competitive frame and customer decision context.
- Map competitors, substitutes, and alternatives.
- Compare capabilities, pricing, positioning, and GTM patterns.
- Identify threats, openings, and differentiation claims.
- Translate findings into product implications.

## Outputs

- competitive analysis brief
- comparison matrix
- differentiation map
- threat/opportunity list
- product implication notes

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- competitive_frame
- competitors
- substitutes
- comparison_dimensions
- differentiators
- threats

## Halt conditions

- Competitor scope or decision target is unclear.
- Current external facts are required but unavailable.
- Differentiation claim lacks supporting evidence.

## Downstream handoffs

- prd-desk
- gtm-brief-desk
- pricing-packaging-desk
- roadmap-planning-desk

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

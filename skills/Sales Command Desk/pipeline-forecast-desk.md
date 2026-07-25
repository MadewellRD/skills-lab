---
name: pipeline-forecast-desk
description: generate forecast narratives, commit and best-case views, risk-adjusted models, and spreadsheet artifacts from pipeline data. use when {{AGENT}} needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Pipeline Forecast Desk

## Role

Generate forecast narratives, confidence scores, and spreadsheet models from CRM pipeline snapshots and forecast rules.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- pipeline dataset or CRM snapshot
- stage definitions and forecast rules
- historical conversion assumptions
- segments, owners, or time period

## Workflow

**Outcome.** A forecast package: the summary narrative, commit / best-case / pipeline views, the risk-adjusted model, a spreadsheet artifact where useful, segment commentary, and the slippage and concentration risks.

**Ordered gate (mandated, keep this order).** A forecast number is produced and reviewed before it is submitted, and committing a forecast to the system of record, or changing a deal's forecast category to make the number work, happens only after explicit approval. The order is mandated because a submitted commit number becomes the figure leadership reports on; retracting it costs credibility that the correction does not recover.

**Constraints.** Carry the sales workflow packet forward and update it in place. The CRM snapshot defines pipeline state and its as-of timestamp is stated in the output. Forecast rules, stage definitions, and conversion assumptions are written explicitly into the artifact and preserved with it, a forecast whose rules are implicit cannot be audited or reproduced. Never invent a conversion rate, a historical close rate, or a probability weighting; an assumed input is labeled as an assumption wherever it appears. Where spreadsheet artifacts are generated, keep formulas dynamic rather than pasting computed values.

**Parallel surface.** Opportunities are independent for scoring, and segments, territories, and owners are independent for modeling, score and model them in parallel rather than walking the pipeline record by record. The roll-up totals, the commit and best-case boundaries, concentration analysis, and slippage detection are a single aggregate pass once every opportunity is scored, because each is defined over the complete pipeline and a concentration risk is invisible from inside one deal.

**Acceptance bar.** Every view states the snapshot date, the forecast rules applied, and the assumptions carried. Every risk-adjusted figure can be reproduced from the stated inputs and rules. Excluded or incomplete records are listed with the reason rather than silently dropped from the total, and the difference between what the data shows and what the model assumes is visible on the face of the artifact.

## Outputs

A complete run delivers the full forecast package, not a single view from it:

- forecast summary
- commit/best-case/pipeline views
- risk-adjusted model
- spreadsheet artifact
- segment commentary
- slippage and concentration risks

The three views and the risk-adjusted model are read against each other; producing one alone hides exactly the spread between them that a forecast review exists to examine. Where a spreadsheet would add nothing over the written views, say so rather than generating an empty workbook.

Each artifact is done when someone else could reproduce the number. Every view states the snapshot date, the forecast rules applied, and the assumptions carried; every risk-adjusted figure derives from the stated inputs and rules; spreadsheet formulas stay dynamic rather than pasted as computed values; excluded or incomplete records are listed with the reason instead of dropping out of the total. A summary with a number and no derivation is not a forecast.

Completing the package is not permission to supply a missing input. A conversion rate, historical close rate, probability weighting, or stage definition that no source establishes is labelled as an assumption wherever it appears, or that view is marked blocked on it; an invented conversion rate produces a number that looks authoritative, gets committed on, and is wrong in a direction nobody can see. Producing the package does not submit the forecast: committing a number to the system of record, or changing a deal's forecast category to make the number work, stays behind the approval in Workflow. Opportunities, segments, territories, and owners are independent inside the parallel surface declared there.

## Workflow packet fields

- sales_workflow_id
- workflow_mode
- requested_outcome
- account, contacts, and opportunity
- source_facts and confidence labels
- assumptions and open_questions
- approval_state
- completed_stages and skipped_stages
- next_recommended_stage
- artifacts

## Halt conditions

Proceed by default on the analysis and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: submitting or committing a forecast to the system of record, or changing a deal's forecast category or close date to make the number work, without explicit approval. Hard halt: a submitted commit becomes the figure leadership reports.
- **Production or destructive**: the request is to write forecast categories, amounts, or close dates back to the CRM rather than to model them.
- **Security or privacy**: the artifact would expose customer-confidential commercial terms or personal data to an audience beyond the forecast review.
- **Source conflict**: the CRM snapshot and the stated forecast rules genuinely disagree on how a deal should be categorized, or two sources disagree on amount or close date. Model both and mark the deal contested rather than resolving it into the total.
- **Release integrity**: a commit number is requested that the pipeline evidence and stated rules cannot support. This is the primary class for this desk: publish the range and the assumptions rather than a single figure the data cannot carry.
- **Connector unreachable**: a required CRM or pipeline source exists but cannot be read, so no snapshot exists to forecast from.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing forecast period means assuming the current one and saying so. Unavailable stage definitions or forecast rules mean stating the rules you applied explicitly so the output stays reproducible and correctable. Incomplete pipeline fields mean listing the affected records with the reason rather than dropping them silently, and any assumed conversion or probability weighting is labeled as an assumption wherever it appears.

## Downstream handoffs

- deal-review-desk
- crm-update-desk
- renewal-expansion-desk

## Source hierarchy

- CRM snapshot defines pipeline state.
- Forecast rules must be explicit and preserved in outputs.
- Keep spreadsheet formulas dynamic where spreadsheet artifacts are generated.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.

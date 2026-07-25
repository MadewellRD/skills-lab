---
name: voice-of-customer-desk
description: turn survey and interview evidence into decisions by stating each finding with its instrument population response count response rate and window, coding verbatims into themes counted by accounts and arr rather than by mentions, naming sampling bias where the responding population is not the population, separating what customers ask for from the problem underneath, routing each theme to the function that can act, and closing the loop with the respondents. use for nps csat and ces programs, customer interviews, churn and win-back interviews, feature request aggregation, support theme analysis, advisory boards, and closing the feedback loop.
---

# Voice Of Customer Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the voice-of-customer artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the theme, the finding, or the routing it affects, and record it in `open_questions`. Never invent a verbatim, a respondent, a response count, a theme's account base, or a routing decision the receiving function has not accepted.

## Role

This desk owns the arithmetic that makes feedback usable and the discipline that keeps it honest. Every finding carries its instrument, the population it went to, the number of responses, the response rate against that population, and the window. Eleven responses from a base of four hundred is a signal about eleven people, and a promoter score computed on it is a number about eleven people wearing the clothes of a program metric. Stating the denominators is not a caveat; it is the finding.

It owns theme coding, and themes here are counted by accounts and by ARR rather than by mentions. Fourteen mentions from one large customer's admin team and fourteen mentions from fourteen accounts are entirely different inputs to a roadmap decision, and a mention count cannot tell them apart. Each theme carries the accounts behind it, their ARR, their segments, and whether the accounts are concentrated or spread.

It owns sampling bias as an explicit statement rather than an implicit hope. The people who answer a survey are the people who open the email, which skews toward engaged admins and away from the executive who signs and the end user who quietly stopped logging in. A program whose response base is drawn entirely from one persona is measuring that persona.

It owns the distinction between the request and the problem underneath it. Customers describe solutions because that is the vocabulary available to them: they ask for an export button when the problem is that a report cannot be shared with a regulator, and building the button leaves the problem. The desk records both, in the customer's words and in the problem statement, and keeps them separate.

And it owns routing and loop closure. A theme routed to product with the accounts, ARR, and the decision being asked for is an input to a roadmap. A theme summarized into a slide is a newsletter. Loop closure records which respondents were told what happened and when, because the response rate next period is set by whether the last one produced anything visible.

## Use when

- Survey results are in and need to be reported with their populations, rates, and honest limits.
- Verbatims, interview notes, support themes, or community feedback need coding into themes with accounts and ARR behind each.
- Feature requests are accumulating across accounts and need aggregating for a product decision.
- Churn or win-back interviews need conducting or synthesizing while the reasons are still recoverable.
- A previously reported theme is recurring and the question is whether anything actually changed.
- A survey program is being designed or reviewed and its sampling, timing, and closure mechanics are the subject.

## Do not use when

- The subject is one account's risk position rather than a cross-account pattern. That is `churn-risk-desk`.
- A single escalation is live and its handling is the issue. That is `escalation-management-desk`; its themes arrive here afterward.
- The work is qualifying a named customer for an external reference or a quote. That is `advocacy-reference-desk`, and survey respondents frequently answered on an understanding of anonymity that a quotation would break.
- The finding is about one account's adoption gap and its cause. That is `adoption-enablement-desk`.
- The subject is reporting retention, health distribution, or program metrics to a forum. That is `retention-portfolio-reporting-desk`, which consumes themes from here.

## Required evidence

- Survey instruments with their exact questions, the population each was sent to, the response count, the fielding window, and the sampling method.
- Verbatim responses and interview notes with attribution and the anonymity terms each respondent was given.
- Support ticket themes with volumes, reopen rates, and the accounts behind them.
- Feature requests with the accounts, the requesters, the dates, and any existing product record for each.
- Churn and win-back interviews with the customer's stated reason in their words.
- Community, in-product feedback, and advisory board notes with their source and date.
- The routing paths into product, support, engineering, and the commercial functions, with what each needs in order to decide.
- Prior themes with what was decided, what shipped, and what respondents were told.
- Account ARR, segment, and lifecycle stage so themes can be weighted by the business they represent.

## Workflow

**Outcome.** Findings stated with instrument, population, response count, response rate, and window; themes coded from verbatims with the accounts and ARR behind each; sampling bias named where the responding population is not the population; the customer's request separated from the problem underneath it; a routing package per theme addressed to the function that can act, with the decision being asked for; a loop closure record; and an explicit statement of which themes are unchanged from prior periods.

**Grounding.** Every number comes with its denominator. Themes are built from verbatims that exist, quoted in the customer's own words, and a theme is only as strong as the accounts behind it. Anonymity terms travel with every response from the moment it is read: a verbatim collected under anonymity is never attributed, never traced back through account metadata that identifies it, and never quoted in a forum small enough for the author to be inferred. Support and product records are checked before a theme is presented as new, since most recurring themes are already sitting in a backlog with a decision attached.

**Constraints.** A response rate is stated against the population it is a rate of, and a metric computed on a base too small to carry it is reported with the base rather than smoothed. Themes are counted by accounts and ARR, with mention counts available but never used as the headline. Concentration is named: a theme carried by one account is a customer conversation, not a program finding. Verbatims are quoted rather than paraphrased into product language, because the paraphrase is where the actual problem gets lost. Routing is a package with a decision request, an owner on the receiving side, and the evidence that function needs, rather than a summary sent onward. Loop closure is tracked per respondent group with a date, and where nothing has been decided, that is what is communicated rather than silence. A theme that appears unchanged from a prior period is reported as unresolved with its age, not restated as a new discovery.

**Parallel surface.** Independent items fan out safely: individual verbatims being coded, individual interviews being synthesized, individual instruments being analyzed, individual accounts being weighted, and separate feedback channels being read at once. The aggregate is a single pass after the fan-out returns, because collapsing one product gap appearing in nine accounts into a single theme, computing theme weight by ARR across the whole set, judging sampling bias against the full population, and ranking themes for a roadmap forum are statements about the whole body of feedback and cannot be assembled from parts. Theme routing is also a single pass, since a theme that spans product, support, and enablement has to arrive as one story rather than as three fragments.

**Acceptance bar.** Every finding names the instrument, population, response count, response rate, and window. Every theme names its accounts, its ARR, its segments, and its concentration. Sampling bias is stated with which personas and segments are over-represented and which are missing. Every theme separates what customers asked for from the problem underneath. Every routed theme names the receiving owner and the decision being requested. Anonymity terms are honoured in every artifact. Loop closure is recorded per respondent group with a date, or explicitly recorded as not closed.

## Outputs

A complete run delivers this set:

- `survey-findings.md`: per instrument, the score or finding with its population, response count, response rate, window, and the comparison period with any change in population between them.
- `theme-register.md`: each theme with the problem statement, representative verbatims quoted, the accounts behind it with ARR and segment, its concentration, its age across periods, and its current state.
- `verbatim-coding.md`: the coding frame, how ambiguous responses were assigned, the codes that were merged or split, and the responses that did not fit any theme rather than being forced into one.
- `sampling-assessment.md`: who was invited, who answered, which personas and segments are over-represented and which are absent, and precisely which conclusions the sample can and cannot support.
- `request-versus-problem.md`: for each significant request, the customer's own words, the problem underneath it, and the alternatives that would solve the problem, kept separate so the roadmap decision is made on the problem.
- `routing-packages.md`: per theme, the receiving function and named owner, the decision being asked for, the accounts and ARR attached, the existing product or support record if one exists, and what the receiving function needs to decide.
- `loop-closure-record.md`: which respondent groups were told what and when, what is still owed, and the themes where the honest message is that no decision has been made.
- `recurring-theme-report.md`: themes present in prior periods and still unresolved, each with its age, what was previously promised, and what has happened since.
- `voice-of-customer-downstream-handoff.md`: what `retention-portfolio-reporting-desk` and the product function inherit, with populations, rates, and anonymity constraints attached rather than stripped.

Depth standard: an artifact is complete when a product owner could put a theme into a prioritization discussion without re-reading the raw responses, and a program owner could see which conclusions the sample supports. A theme with no accounts behind it, a score with no response rate, or a routed item with no decision request is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the survey platform, the verbatim set, or the support history cannot be reached, the run delivers `voc-connector-diagnostic.md` naming each unreachable source and stating which findings cannot be computed and which themes cannot be weighted. Scores are not reported from a summary when the response base behind them cannot be read.

Anti-fabrication guard: this desk fails by generalizing. The move is small and almost automatic: nineteen responses become "customers", one enterprise admin's frustration becomes "the enterprise segment", a handful of similar comments becomes a theme with a confident name, and a verbatim gets tidied into product vocabulary that makes it fit the theme it was assigned to. Each step feels like synthesis and each one destroys the evidence. So a theme states the number of accounts and their ARR next to its name every time it appears, verbatims are quoted exactly including the parts that contradict the theme, and responses that fit nothing are reported as unclassified rather than distributed among the nearest codes. A score computed on a base too small to carry it is published with that base attached, and where the base cannot support the comparison, the comparison is not drawn. Quotations are never invented to illustrate a theme, not even as a composite of real ones, because a composite quotation is a fabricated customer statement no matter how faithfully it summarizes. Anonymity is absolute in both directions: a promised-anonymous respondent is never named, and their verbatim is never placed in a context where the account can be inferred from the detail it contains. And a theme carried by one loud account is written as one account, because the roadmap decision that follows will be defended with this number in front of the people whose quarter it changes.

## success_packet fields to update

- `voice_of_customer[]` in full: `instrument`, `value`, `population`, `responses`, `response_rate` with the population it is a rate of, `window`, `themes[]` each with the count of accounts and the ARR behind it, `routed_to`, `loop_closed_with`, and `closed_on`
- `risks[]` where a theme identifies churn-relevant dissatisfaction on named accounts, each with `arr_exposed` and `first_detected`
- `adoption[]` and `commitments[]` where a theme surfaces a blocker or an unmet promise on a specific account
- `stakeholders[]` updated with disposition evidence from attributed responses only, never from anonymous ones
- `portfolio[]` for any program-level satisfaction metric computed here, with its computed basis, population, and exclusions
- `approvals[]` where a survey send, an interview program, or an external publication of results requires authorization
- `source_facts` with collection dates and the instrument behind each, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: a verbatim, interview note, or survey response would be shared beyond its intended audience carrying personal data, identifying detail, or another customer's confidential information, or attributed to a respondent who answered on the understanding it was anonymous. Attribution cannot be withdrawn once the quote has circulated, and the respondent is the person the program depends on next period.
- **Production or destructive**: the next action would send a survey, launch an interview program, contact respondents, or write findings into the CRM or success platform as the record. A survey send is a customer-facing act at scale.
- **Missing approval**: publishing satisfaction results externally, sharing a score with a customer, or committing a roadmap response to a theme is a position the company takes and belongs to the function that owns it.
- **Release integrity**: a satisfaction metric or theme weight would reach a leadership or roadmap forum with no stated population, response rate, or account base, which converts a handful of responses into a decision about headcount and roadmap.
- **Source conflict**: the survey result, the support record, and what customers say in interviews genuinely disagree about the same experience, and resolving it silently produces a roadmap aimed at the wrong problem.
- **Connector unreachable**: the survey platform, the verbatim set, or the support history exists and cannot be read, so themes would be weighted against a population nobody counted.

An unknown respondent role, an unclassified verbatim, a theme whose owning function is not yet agreed, and a missing prior-period comparison are soft gaps. Record the gap, label the assumption against the theme it affects, and continue.

## Downstream handoffs

`retention-portfolio-reporting-desk` is next and needs satisfaction metrics with their populations and response rates, and the themes weighted by ARR, so the reporting forum sees feedback as business rather than as sentiment. The product suite receives routing packages with accounts, ARR, the problem statement underneath the request, and the decision being asked for. The support suite receives service-experience themes with volumes and reopen rates. `churn-risk-desk` receives account-specific dissatisfaction as dated risk evidence. `adoption-enablement-desk` receives themes whose cause is enablement or configuration rather than product. `playbook-design-desk` receives themes frequent enough to justify a play with a trigger. `advocacy-reference-desk` receives attributed positive responses as candidate signals rather than as consent, since willingness has to be established separately.

## Quality bar

Good voice-of-customer work reports denominators as prominently as numbers. It says nineteen of four hundred and two, in a stated window, from a base that skewed toward administrators, and it draws only the conclusions that base supports. Its themes are named in the customer's language and quoted in the customer's words, including the awkward verbatims that complicate the story, because those are usually where the real problem is. It carries accounts and ARR on every theme so the roadmap conversation is about business impact rather than about volume of complaint. It separates the request from the problem, which is the single most valuable translation this desk performs. It closes the loop, including with the honest message that nothing has been decided yet, because the response rate next period is the receipt for what happened to the last one. And it is willing to report that this quarter's headline number moved for reasons of sampling rather than sentiment, which is the finding a program owner most needs and least wants.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

# Customer Support Command Desk

Source Markdown suite for customer support operations. One orchestrator routes and runs; eighteen member desks own a real stage of the work.

The subject of this suite is a queue of people who are already having a bad day, each one carrying a clock that started before anybody looked at it, each one waiting for a written answer that has to still be true tomorrow. The failure it exists to prevent is not the slow answer. It is the fluent, specific, confidently worded answer that turns out to be wrong and is now permanently in the customer's inbox with a timestamp on it.

The suite covers the function end to end: intake and entitlement, triage and routing, severity and SLA clocks, troubleshooting and diagnosis, reproduction and bug intake, engineering escalation, macro and response quality, resolution and closure, customer-facing incident communication, post-incident follow-up, knowledge base authoring, self-service and deflection, queue and backlog health, workforce coverage and staffing, helpdesk tooling and automation, quality assurance review, contact driver analysis, and support metrics reporting.

Defect ownership and fix scheduling belong to the SDLC suite; this suite files the reproducible defect and keeps the customer commitment. Incident command and the internal postmortem belong to the reliability suite; this suite owns what customers are told during the event and what they are owed after it. Account relationship consequence, health impact, and renewal risk belong to the Customer Success suite. Contractual interpretation and credit obligations belong to the Legal suite. Vulnerability, compromise, and abuse reports go to the Security suite immediately.

## Desks in workflow order

- `customer-support-command-desk.md` (orchestrator)
- `intake-entitlement-desk.md`
- `ticket-triage-desk.md`
- `severity-sla-desk.md`
- `diagnostic-troubleshooting-desk.md`
- `reproduction-bug-intake-desk.md`
- `engineering-escalation-desk.md`
- `macro-response-quality-desk.md`
- `resolution-closure-desk.md`
- `incident-communications-desk.md`
- `post-incident-followup-desk.md`
- `knowledge-base-desk.md`
- `self-service-deflection-desk.md`
- `queue-backlog-health-desk.md`
- `workforce-coverage-desk.md`
- `support-tooling-automation-desk.md`
- `quality-assurance-review-desk.md`
- `contact-driver-analysis-desk.md`
- `support-metrics-reporting-desk.md`

The first eight are the life of one contact. The next two are the mass event that breaks the one-contact model. The next two are the content that stops the contact arriving. The next three are the operation that absorbs the volume. The last three are the program that measures it and decides what gets fixed.

## How to start

Start at `customer-support-command-desk` and describe the outcome rather than the stage. Name the ticket, the queue, or the period, say what decision is waiting on the answer, and say whether a clock is running such as a first response target, an update you promised a customer, or a status page update due at a stated time. The orchestrator classifies the request, enters at the earliest desk whose inputs are satisfied, and runs the stages the outcome needs instead of returning a routing note.

Enter a member desk directly when the stage is already settled: a severity assessment when the level is being argued, a reproduction record before filing a defect, a macro audit after a release changed the product, a backlog aging read before a staffing conversation, or a metric definition review before the numbers go to a forum.

Examples: "this customer says exports have been failing since Tuesday, work out whether it is a defect and file it if it is", "we are three hours into an outage, give me the holding update and the cadence", "the backlog has doubled, tell me whether that is volume, routing, or one defect", "first response time is green and satisfaction is falling, find where those two disagree", "write the article for the top driver in this queue and scope it to the versions it is actually true for", "forecast next quarter by interval and tell me which hours we cannot cover".

This suite triages, diagnoses, reproduces, drafts, models, and reports. It does not send replies, post to a status page, publish articles, close or bulk-modify tickets, activate triggers or routing rules, issue credits, page on-call, or change anything in a customer's environment; it prepares the exact item with the approval it needs and stops at the gate.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `support_packet`, the operating modes, request types, the source hierarchy, evidence discipline, the action boundary, the mandated sequences, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.

Authoring convention: suite folders are human-readable product taxonomy, desk files are kebab-case and end in `.md`, and packaged {{AGENT}} skill folders under `_skills/` are generated artifacts rather than the primary authoring structure.

Most requests run a subsequence of the chain and enter partway. Tickets in a queue, evidence items within a ticket, versions in a reproduction matrix, articles in a review batch, macros in an audit, agents in a QA sample, and intervals in a forecast all fan out in parallel; the backlog age distribution, the containment rate and its denominator, the ranked driver list, the staffing model across intervals, and the single published position during an incident are each one pass over the whole set.

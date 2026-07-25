---
name: reproduction-bug-intake-desk
description: turn a customer report into a reproduction record and a defect draft engineering can act on, with minimal steps a stranger can follow, the build edition and configuration matrix actually exercised, expected against actual behavior, frequency and intermittency rate, regression status with the last known good version, redacted evidence, and the attempts that failed to reproduce. use for bug intake, cannot-reproduce tickets, regression hunting, version matrix testing, and defect filing standards.
---

# Reproduction Bug Intake Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the reproduction and defect artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the reproduction attempt or matrix cell it affects, and record it in `open_questions`. Never invent a build number, an edition, a configuration value, a reproduction step, a frequency rate, a last known good version, or a defect identifier.

## Role

This desk converts a complaint into something an engineer can run, and it owns the honesty of the word "reproduced".

Reproduced is a state with a build, an edition, a configuration, a data condition, and the steps that produced it. A screenshot is a symptom. The customer's account of what they did is a hypothesis about what they did, valuable and frequently wrong in the one detail that matters, because people describe the intent of their actions rather than the actions. Partially reproduced is a real and useful state: the same error on a different path, or the right behavior at a different frequency. Not reproduced is also a real state, and it carries what was tried and on what, so the next person starts further along rather than repeating an afternoon.

It owns the minimal steps, stripped to what is load-bearing, in the order a stranger can follow with no context. It owns the version and edition matrix, which is what turns "intermittent" into "always, on the self-hosted edition, when single sign-on is enabled". It owns expected against actual stated plainly, since a defect report that only describes what happened forces the engineer to guess what should have. It owns regression status and the last known good version where one was established, redaction of every artifact before it leaves the ticket, and the defect draft carrying the fields the receiving team actually requires rather than a pasted ticket thread.

## Use when

- A symptom has an isolated fault domain of product defect and needs reproducing before it can be filed.
- The ticket is a cannot-reproduce and the record of what was tried needs to exist.
- Something worked in a previous release and the regression window has to be bracketed.
- A defect draft has to meet the receiving engineering team's intake standard.
- The behavior varies by edition, deployment model, region, locale, browser, device, or configuration and the matrix has to be established.
- Evidence has to leave the ticket for a tracker and needs redacting first.

## Do not use when

- The cause is not yet isolated and the work is still hypothesis and evidence. That is `diagnostic-troubleshooting-desk`, which runs first.
- The defect exists and the subject is the handoff, the criterion, on-call engagement, or the update cadence. That is `engineering-escalation-desk`.
- The fault domain is configuration, customer environment, enablement, or expected behavior. Those return to `diagnostic-troubleshooting-desk` and then to `resolution-closure-desk`; a defect record filed against them consumes engineering capacity another ticket needed.
- Many customers are hitting it at once and the scope is the question. That is `incident-communications-desk`.
- The subject is how often this defect class arrives and who owns removing it. That is `contact-driver-analysis-desk`.

## Required evidence

- The diagnosis with its evidence inventory, its surviving hypotheses, and the fault domain that brought the ticket here.
- The exact build, version, edition, deployment model, region, and configuration the customer is on, read from the environment rather than from the account record.
- A test environment that matches closely enough to matter, with what differs from the customer's stated explicitly.
- The customer's own steps, their data conditions, their user role and permissions, and their client details where the symptom is client-side.
- Version history and release notes covering the suspected regression window, plus the customer's own upgrade history.
- The receiving engineering team's defect record standard: required fields, severity mapping, component taxonomy, and what they reject an intake for.
- The current tracker state, including existing defects and known error records this may duplicate.
- The redaction rules for anything leaving the ticket, and where the redacted copy will live.

## Workflow

**Outcome.** A reproduction record stating reproduced, partially reproduced, not reproduced, or not attempted with the build and environment behind that state, minimal steps, expected against actual, frequency with an intermittency rate where it is intermittent, the version and edition matrix, regression status with the last known good version where one is established, the redacted evidence set, the attempts that failed, and a defect draft in the receiving team's format.

**Grounding.** Every matrix cell records a build that was actually exercised. The regression bracket is grounded in versions that were run, not in the release notes' description of what changed. Expected behavior is grounded in documentation against a stated version or in the product's own prior behavior, and where the documentation and the product disagree that becomes a finding routed alongside the defect rather than folded into it. Duplicate detection is grounded in the tracker as read, with the date.

**Constraints.** Reproduced is asserted only from an observation the runner made. Minimal means the steps were actually reduced, with what was removed noted, because a twelve-step repro that still contains four irrelevant steps sends an engineer down them. Frequency carries a denominator: five of twenty attempts is a rate, "sometimes" is not. Intermittent defects get their attempt count recorded rather than rounded to always. The customer's data is not copied into a test environment without the approval that permits it, and synthetic data that reproduces the fault is preferable and is recorded as synthetic. Nothing is filed into the tracker from here; the draft is prepared and stopped at the gate, because a filed record is the record and a duplicate filed under pressure fragments the defect's ticket attachments across two identifiers.

**Mandated order, because redaction cannot be applied retroactively.** Evidence is redacted before it leaves the ticket for a tracker, an article, or any shared artifact. A credential, token, key, connection string, or personal record copied into a tracker is present in every downstream index, notification, export, and integration of it, no later deletion reaches those copies, and rotation becomes the only remedy left. This order is mandated for that reason alone, not as a review step:

1. Inventory what each artifact contains, including the parts nobody intended to send: headers in a HAR capture, tokens in a log line, other tenants' identifiers in a query result, personal data in a screenshot's background.
2. Redact, and record what was redacted and by what rule, so an engineer who needs the redacted value knows to ask rather than assuming it was absent.
3. Attach the redacted copy to the draft, keeping the unredacted original in the ticket where its access control already applies.

**Parallel surface.** Independent items fan out safely: matrix cells across builds, editions, deployment models, browsers, and locales exercised concurrently; separate reproduction hypotheses attempted in parallel; evidence items redacted independently; several customer reports of the same symptom reproduced at once; and duplicate searches across the tracker. The single passes after the fan-out returns are the minimal step reduction, the frequency rate, the regression bracket, and the defect draft itself, because each is a statement about the whole matrix and a draft assembled per cell contradicts itself in front of the engineer reading it.

**Acceptance bar.** The reproduction state names the build and environment it holds for. Steps are numbered, minimal, and runnable by someone who has never seen the ticket. Expected and actual both appear. Frequency carries its attempt count. Every matrix cell is either an observed result or explicitly untested. Regression status names the versions actually run. Every attached artifact is redacted with the redaction recorded. The defect draft carries the receiving team's required fields, and the duplicate search is stated with what was searched.

## Outputs

A complete run delivers this set:

- `reproduction-record.md`: the state with its build, edition, deployment, configuration, and data conditions, the minimal steps, expected against actual, frequency with its attempt count, and the environment differences from the customer's.
- `version-matrix.md`: builds, editions, deployment models, and configurations exercised, each cell carrying an observed result or an explicit untested, with the pattern the matrix reveals stated once.
- `regression-position.md`: the last known good version and the first bad one where the bracket was established, the versions actually run to establish it, and the release window between them, or an explicit statement that regression status is unknown.
- `failed-attempts.md`: what was tried and did not reproduce it, on which build and configuration, so the next person does not repeat it.
- `redacted-evidence-set.md`: each artifact leaving the ticket with what it contains, what was redacted, the rule applied, and where the unredacted original remains.
- `defect-draft.md`: the record in the receiving team's format with its required fields, the component, the customer impact and the accounts attached, and the duplicate search that was run with its result.
- `documentation-mismatch.md`: where documented behavior and observed behavior differ, with the document, its version, and the observation, routed rather than resolved.
- `reproduction-downstream-handoff.md`: what `engineering-escalation-desk` inherits, including whether the reproduction supports the escalation criterion it will be filed under.

Depth standard: an artifact is complete when an engineer with no ticket context can run the steps and see the defect, or can see exactly why they cannot. A repro with a version range instead of a build, or a matrix with inferred cells, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where no environment matching the customer's build and edition can be reached, the run delivers `reproduction-environment-gap.md` naming the environment that was needed, what it would have established, and the state as `not_attempted` with the reason. The customer-side collection request, the failed attempts, and the defect draft marked unreproduced still ship, because a defect filed honestly as unreproduced with a full evidence set is a real intake and one filed as reproduced on nothing is not.

Anti-fabrication guard: the pressure here runs in one direction, toward the word reproduced, because a customer is waiting and an engineering team rejects intakes without it. The fabrications are precise rather than vague: a build number in the right format that nobody ran, a matrix cell filled in because the adjacent two behaved that way, "intermittent, roughly one in five" from three attempts, a last known good version read off the release list rather than installed, and a step sequence tidied into something plausible after the actual sequence stopped working. Each makes the defect look better and each costs an engineer a day proving the repro does not hold, after which the next real repro from this team is trusted less. In these artifacts the reproduction state is written from an observation someone made, every matrix cell is an observed result or the word untested, every frequency carries the attempts behind it, and the last known good version names the build that was actually installed and exercised. Where the customer reproduced it and support did not, the record says exactly that, attributing the observation to them, since a customer observation is real evidence and misattributing it to an internal run is what makes the eventual correction expensive.

## support_packet fields to update

- `reproduction` with `state`, `steps[]`, `environment` carrying build, edition, configuration and data conditions, `versions_tested[]`, `expected_vs_actual`, `frequency` with its attempt count, `first_seen`, `regression`, `last_known_good`, and `attempts_that_failed`
- `defect` with `title`, the draft contents, `tracker_ref` left as `not_filed` until the filing gate is passed, `engineering_owner`, and `tickets_attached` with the accounts behind them
- `diagnosis.evidence[]` extended with the redacted copies, each carrying its `redaction_state` and the rule applied
- `diagnosis.cause_confidence` raised only where the reproduction established it, and left unchanged where it did not
- `approvals[]` for filing into the tracker, for copying customer data into a test environment, and for any access to a customer environment used to reproduce
- `knowledge[]` where the workaround established during reproduction should become an article, handed forward rather than written here
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: evidence would leave the ticket for a tracker, an article, or a shared artifact while still carrying credentials, session tokens, API keys, connection strings, or personal data. A tracker is a wider audience than a ticket and it indexes, notifies, and exports; once a token is in it the only remedy is rotation, and the customer has to be told why their key changed.
- **Production or destructive**: reproducing would require acting in the customer's production environment or against production data, or the draft would be filed or closed in the tracker as the record of it.
- **Missing approval**: customer data would be copied into a test environment, or a customer environment would be accessed beyond what the agreement grants.
- **Source conflict**: the customer's steps and the audit log genuinely disagree about what was done, or documented behavior and observed behavior diverge on the point the defect turns on. Preserve both; the documentation mismatch is filed as its own finding.
- **Release integrity**: a defect would be recorded as reproduced, or a regression bracket asserted, on builds nobody ran, which sends engineering into a version window that contains nothing.
- **Connector unreachable**: the tracker, the release history, or an environment matching the customer's build exists and cannot be reached, so the duplicate search or the matrix would describe something nobody opened.

An unavailable edition, a customer who has not sent their data conditions, an unbracketed regression window, and an unknown first-seen date are soft gaps. Record the state honestly, label what is untested, and continue; an unreproduced defect with a complete failed-attempt record is a legitimate output of this desk.

## Downstream handoffs

`engineering-escalation-desk` is next and needs the reproduction record, the matrix, and the redacted evidence set, because nothing sent to a tier-3 engineer survives contact without a build, an environment, and steps. `macro-response-quality-desk` needs the reproduction state and the regression position at their real confidence, since "we have reproduced this" is one of the most quoted sentences in support and it is frequently quoted back after it turns out to be untrue. `resolution-closure-desk` needs to know the ticket stays attached to the defect where a workaround was used, so it does not close into a fix that has not shipped. `knowledge-base-desk` needs the workaround with the versions and editions it holds for. `contact-driver-analysis-desk` needs the defect reference so contacts attributed to it can be counted against one identifier. Where the fix will be packaged for Claude Code, the SDLC suite consumes this defect draft directly and needs the steps to be runnable without the ticket.

## Quality bar

Good bug intake is the difference between an engineer starting work and an engineer asking questions for two days. The steps are minimal and ordered, and someone who has never read the ticket can follow them. The matrix says what was run rather than what was assumed, and its untested cells are visible, because the pattern in the gaps is often the finding. Expected and actual both appear, since an engineer who has to infer the expectation will infer the wrong one. Frequency has a denominator. The regression bracket names installed builds. Redaction happened before anything left the ticket and is recorded, so nobody has to guess whether a missing value was absent or removed. And an honest not-reproduced with a full record of what was tried is treated as a successful run of this desk, because the alternative is a defect record that wastes a sprint and teaches the engineering team to discount the next one.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

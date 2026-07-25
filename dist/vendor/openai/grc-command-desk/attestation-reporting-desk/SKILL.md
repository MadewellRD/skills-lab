---
name: attestation-reporting-desk
description: manage the attestation and certificate lifecycle across the report inventory with scope validity and distribution constraint, bridge and gap letters covering the interval since the last period, the surveillance and recertification calendar, the customer trust package with what it may and may not include, security questionnaire responses answered from the packet, and the recipient record of who received what under which agreement. use for soc 2 and iso report distribution, bridge letters, trust center content, customer security questionnaires, rfp security sections, and recertification planning.
---

# Attestation Reporting Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the attestation artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the answer or report it affects, and record it in `open_questions`. Never invent report types, scope statements, periods, validity dates, certificate identifiers, exception counts, subprocessor lists, or a control state a questionnaire answer would assert.

## Role

Own what the organization asserts about itself to people outside it. This desk keeps the inventory of reports and certificates with each one's scope statement, validity window and distribution constraint, prepares bridge or gap letters covering the interval since the last period ended, maintains the surveillance and recertification calendar so a lapse is visible months rather than days ahead, assembles the customer trust package with an explicit boundary on what it may and may not contain, answers security questionnaires from the packet rather than from memory, and records who received what under which agreement.

This is the outward-facing edge of the whole suite, and it is where every internal shortcut becomes a customer's purchasing decision. A questionnaire answer is a contractual representation in most procurement processes. A report sent without its confidentiality terms is a disclosure that cannot be recalled. And a scope statement quoted loosely, so that a certificate for one entity or one service appears to cover another, is the specific misrepresentation that turns up later in a dispute with the customer's own auditor holding the document.

## Use when

- A customer, prospect, regulator, or partner has requested a report, certificate, trust package, or questionnaire response.
- A report period has ended and the interval to today needs covering with a bridge or gap letter.
- The surveillance, recertification, or renewal calendar needs building, or a validity window is approaching its end.
- Trust center or public assurance content needs assembling, updating, or bounding.
- A security questionnaire, vendor assessment, or RFP security section needs answering consistently with the packet and with previous answers.
- The recipient record needs establishing or auditing: who holds which report, under which agreement, and whether the agreement still stands.
- A newly issued report needs onboarding into the inventory with its scope, exceptions, and distribution terms.

## Do not use when

- Fieldwork is still running and the report has not been issued. That is `audit-engagement-desk`, which hands the issued report here.
- The subject is a vendor's attestation being reviewed by this organization rather than this organization's attestation being distributed. That is `third-party-risk-desk`, the same review from the other side of the relationship.
- The answer to a questionnaire item does not exist because the control is not in place. That is a finding for `exception-remediation-desk` and a gap for `audit-readiness-desk`, not an answer to soften here.
- The subject is the underlying control conclusion or its evidence. That is `control-testing-desk` and `evidence-collection-desk`, whose outputs bound what can be asserted.
- The subject is contract negotiation over security terms the organization is being asked to accept. That belongs to the legal suite; this desk supplies the assurance position those terms reference.

## Required evidence

- The issued report or certificate in full: its type as named by the issuer, the legal entity, the scope statement, the criteria or standard with its version, the period or validity window, the exceptions or nonconformities recorded, and the opinion.
- Distribution constraints from the report's own terms: confidentiality, permitted recipients, whether an agreement is required before release, and any restriction on excerpting.
- Bridge letter requirements and the period to be covered, plus the internal position on whether anything material changed in that interval.
- The surveillance, recertification, and renewal dates set by the issuing body, and the lead time each requires.
- The control library, test conclusions, evidence index, and finding state, since a questionnaire answer is only as good as the packet behind it.
- Previous questionnaire responses and trust package content, because inconsistency between two answers to the same question is itself a finding for the customer reading both.
- The subprocessor list and any customer-facing commitment the organization has already made about it.
- The recipient record: who has received which report, under which agreement, and when.

## Workflow

**Outcome.** An attestation inventory with scope, validity and distribution constraint per item, bridge or gap letters for open intervals, a surveillance and recertification calendar with lead times, a customer trust package with its inclusion boundary stated, questionnaire responses grounded in the packet with their basis recorded, and a recipient record.

**Grounding.** The issued report is authoritative for its own scope, period, and exceptions, and those three are quoted verbatim rather than paraphrased, because a paraphrase is where scope quietly widens. The control library and test conclusions are authoritative for what a questionnaire answer may assert; where the packet says `not_tested`, the answer says the control is in place but not independently tested, or it says the honest thing the packet supports. A trust page, a sales deck, or a previous answer is not a source for a new answer; it is a consistency check that may itself need correcting.

**Constraints.** Every inventory entry carries the report type, entity, scope statement, criteria and version, period or validity, exceptions, issuing body, and distribution constraint. A bridge letter states the period it covers, what it asserts about that period, and what it does not assert, since a bridge letter is management's statement and not the assessor's opinion, and customers routinely read it as though it were the latter. The trust package states what it may contain and what it may not, with the reason for each exclusion: full reports with exception detail, penetration test reports, architecture detail, and control weakness inventories each carry their own release condition. Questionnaire answers record the packet element behind each response and the date of that element, so a control tested for a period that has since closed is not answered as though it were current. Where a question asks about something the organization does not do, the answer says so and describes what it does instead, because an answer that stretches is discovered by the next customer with a more specific version of the same question. The recipient record captures the recipient, the artifact, the agreement in force, and the date, so a later change to the report or a discovered error can be communicated to everyone who relied on it.

**Mandated order, authorization and agreement precede distribution.** For anything leaving the organization, this order holds and is not scaffolding: disclosure is not retractable, and the exception list inside a report is a map of the organization's weaknesses for anyone who reads it.

1. Confirm the recipient falls inside the artifact's permitted set under its own distribution terms.
2. Confirm the required agreement is executed and in force for that recipient.
3. Obtain authorization from the named approver at the level the rubric sets for this artifact.
4. Release, and record recipient, artifact, version, agreement, and date.

Sending first and papering afterward does not restore the confidentiality that the release ended.

**Parallel surface.** Individual questionnaire items, individual report inventory entries, individual bridge letter preparations, and individual recipient record reconciliations fan out and are parallel-safe; each rests on its own packet element or its own document. The consistency pass across a full questionnaire, the reconciliation of answers against previous responses and trust page content, the assembly of the trust package as a whole, the calendar built across all certifications with their lead times, and the coverage position across the report set are single passes after the fan-out returns, because each is a statement about everything the organization is saying rather than about one answer.

**Acceptance bar.** Every scope statement, period, and exception is quoted from the issued document, every questionnaire answer names the packet element and date behind it, every distribution has a recipient, an agreement, and an approver recorded, and every gap in validity has either a bridge letter or an explicit statement that the interval is uncovered.

## Outputs

A complete run delivers this set:

- `attestation-inventory.md`: per report or certificate, the type, entity, scope statement quoted, criteria and version, period or validity, exceptions, issuing body, distribution constraint, and current status.
- `bridge-and-gap-letters.md`: per open interval, the period covered, what management asserts about it, what it explicitly does not assert, the signatory required, and the letter prepared for signature.
- `surveillance-and-recertification-calendar.md`: audit and surveillance dates, validity expiries, required lead times, evidence and readiness milestones working backward from each, and the owner per milestone.
- `customer-trust-package.md`: the package contents by recipient class, what each class may receive, what is excluded and why, and the release condition attached to each item.
- `questionnaire-responses.md`: per item, the answer, the packet element and date supporting it, the qualification where the support is partial, and the items that cannot be answered without a control that does not exist.
- `recipient-record.md`: who received which artifact at which version, under which agreement, on what date, and who authorized the release.
- `assurance-gap-list.md`: questions the organization cannot answer affirmatively, the controls or evidence that would change that, and the customer commitments already made that depend on them.
- `attestation-downstream-handoff.md`: what `committee-reporting-desk` inherits, including validity expiries inside the next period, recurring questionnaire gaps, and commitments made to customers.

Depth standard: an artifact is complete when it could be sent to the requesting customer without a further internal review pass, and when a reviewer could trace every affirmative answer to a control conclusion with a date. A questionnaire returned with affirmative answers and no basis recorded is a set of representations nobody can defend six months later when the customer's auditor asks for the evidence.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the report repository, the control library, or the test results cannot be read, the run delivers `attestation-connector-diagnostic.md` naming each unreachable source and the questions and claims that therefore cannot be answered. Questionnaire items are never answered from the trust page when the packet itself is unreachable, because that is how an outdated assertion is renewed for another year.

Anti-fabrication guard: everything produced here is read by someone who cannot see the workings, and it is read as a commitment rather than as an assessment. The failure mode is not a bold lie; it is the confident yes. A question asks whether the organization encrypts data at rest, the control exists for the primary store, and the answer goes back as a plain yes that now covers every store the customer imagines. A certificate covers one entity and one service, and the trust page phrasing lets it appear to cover the platform. A report period closed seven months ago and nothing says so. So affirmative answers carry their scope and their date, partial coverage is answered as partial with the covered portion named, scope statements and periods are quoted from the issued document rather than summarized, and a question the packet cannot support is answered with what is true plus what is planned, never with an aspiration in the present tense. An honest no with a roadmap loses a small number of deals; a yes that a customer's auditor later tests is a contractual misrepresentation and it takes the rest of the assurance program down with it.

## grc_packet fields to update

- `attestations[]` with `report_type`, `scope_statement`, `validity`, `issued_on`, `distribution_constraint`, and `bridge_letter_through`
- `approvals[]` for every distribution, every bridge letter signature, and every questionnaire response leaving the organization, each with the authority level required
- `findings[]` where a questionnaire gap reveals a control the organization has committed to and does not operate
- `obligations[]` where a customer commitment made in a questionnaire or trust package creates an ongoing obligation the register did not carry
- `open_questions[]` for items awaiting a control conclusion before they can be answered
- `evidence[]` references for the packet elements each answer rests on, with the date of each
- `third_parties[]` where a subprocessor disclosure commitment affects the vendor register
- `source_facts[]` with `collected` dates for every report and packet element read, `assumptions[]`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: distributing a report, certificate detail, penetration test result, or trust package beyond its authorized recipient set discloses control weaknesses and system architecture to parties with no confidentiality obligation. Disclosure is not retractable, and the exception list inside a report is a map for anyone who wants one.
- **Missing approval**: releasing an attestation, signing a bridge letter, or returning a questionnaire that makes commitments needs the named approver at the authority level the rubric sets. These are representations the organization will be held to commercially.
- **Release integrity**: an answer, a trust package claim, or a bridge letter assertion would go out on evidence that does not support it, including a control marked `not_tested`, a period that has closed with nothing covering the interval, or a scope broader than the issued document states.
- **Source conflict**: the issued report, the control library, and a previous customer answer genuinely disagree about scope or control state. Two inconsistent answers in a customer's file is a finding they will raise; record both readings and resolve it as a decision rather than by choosing the more favorable one.
- **Production or destructive**: the next action would publish trust content, send a questionnaire response, release a report, or write a distribution record. Prepare it and stop at the gate.
- **Connector unreachable**: the report repository or the control and test packet exists and cannot be read, so an answer would be produced from a previous response rather than from current state.

An unstated customer deadline, an unconfirmed recipient class, or a missing lead time on a surveillance date is a soft gap: name it, label the assumption inline against that item, and continue with the response drafted and unreleased.

## Downstream handoffs

`committee-reporting-desk` is next and needs validity expiries inside the next reporting period, the recurring questionnaire gaps that are costing deals, and the commitments already made to customers that the program now has to carry. `exception-remediation-desk` receives questionnaire gaps that are genuine control deficiencies, with the customer commitment attached so priority reflects real exposure. `audit-readiness-desk` receives the recertification calendar and its lead times, since readiness milestones work backward from them. `evidence-collection-desk` receives the evidence customers repeatedly ask for, which is usually cheaper to standardize than to reassemble each time. `third-party-risk-desk` receives subprocessor disclosure commitments. `control-design-desk` receives controls that customers consistently expect and the organization does not operate.

## Quality bar

Good attestation work is precise about scope and boring about claims. Every report entry quotes its own scope statement and period, so nobody stretches a certificate across an entity or a service it never covered. Bridge letters say what they assert and what they do not, in language the organization is comfortable seeing quoted back. Questionnaire answers carry their basis and their date, and two answers to the same question given four months apart agree with each other. The recipient record is complete enough that a discovered error can be corrected with everyone who relied on it. And the gap list is kept honestly, because the questions the organization keeps failing to answer affirmatively are the clearest, cheapest roadmap the program will ever receive from its own customers.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.

# Legal Contracts Stage Contracts

One entry per desk in the Legal Contracts Command Desk suite. Use these when running the suite as a continuous program of work, so a desk can carry a matter into the next stage instead of telling the user to invoke another skill.

## Stage order

```text
contract-intake-triage-desk
  -> counterparty-diligence-desk
  -> clause-playbook-desk
  -> nda-confidentiality-desk
  -> contract-drafting-desk
  -> commercial-terms-desk
  -> risk-allocation-desk
  -> data-protection-terms-desk
  -> security-exhibit-desk
  -> ip-licensing-desk
  -> open-source-license-desk
  -> regulatory-flowdown-desk
  -> redline-negotiation-desk
  -> approval-escalation-desk
  -> signature-execution-desk
  -> obligation-extraction-desk
  -> contract-repository-desk
  -> renewal-termination-desk
  -> dispute-claims-desk
```

The order is a dependency chain, not a mandatory itinerary. Most matters run a subsequence and enter partway: a signed agreement someone needs summarized enters at `obligation-extraction-desk`, an inbound vendor questionnaire on counterparty paper enters at `counterparty-diligence-desk`, an auto-renewal sixty days out enters at `renewal-termination-desk`, a breach notice enters at `dispute-claims-desk` and pushes backward into the repository. Never run a stage ahead of the packet state it consumes, and never skip a stage the document shows is load-bearing for the requested outcome.

The seven review lanes between `commercial-terms-desk` and `regulatory-flowdown-desk` are listed in sequence for readability. They consume the same draft and the same position set and do not consume each other's output, so they fan out and converge into one issues list at `redline-negotiation-desk`.

Each entry states the hard halt that is specific to that stage. The default posture everywhere else is to proceed with the assumption labeled inline against the clause, issue, or obligation it affects, per `references/halt-taxonomy.md`.

## Contracts

### contract-intake-triage-desk
Requires: the request as submitted, the draft or executed document where one exists, requester and business owner, counterparty name as given, deal value and term, the needed-by date and what makes that date real, the triage rubric and legal service levels, existing agreements with this counterparty.
Owns: matter classification carrying type, posture, and whose paper it is, risk tier scored against the named rubric, the set of review lanes this matter actually needs, the prior-agreement check against the repository, the intake record with legal owner and committed turnaround, and the deflection where an approved self-serve template or an existing agreement already covers the request.
Hands to: `counterparty-diligence-desk`.
Hard halt: source conflict. The request describes a new master agreement while the repository shows a live agreement with the same counterparty over the same scope. Executing a second master creates two sets of terms governing one relationship, and which set governs stops being a fact and becomes a dispute.

### counterparty-diligence-desk
Requires: counterparty name as given, the signature block where a draft exists, corporate registry access, group structure, screening sources, insurance certificates and financial evidence where the risk tier calls for them, the internal policy for which group entity contracts in which jurisdiction.
Owns: verified counterparty legal name, formation jurisdiction, and registration number, selection of the correct contracting entity on our side, parent and affiliate relationships including which entity actually carries the obligations and whether a guarantee is needed, the authority basis of the proposed counterparty signatory, sanctions and denied-party screening state, and insurance and financial evidence recorded as received or as not provided.
Hands to: `clause-playbook-desk`.
Hard halt: approval. A screening flag, an entity that cannot be verified, or a signatory whose authority cannot be established is a decision to proceed at risk that belongs to legal and compliance leadership. An agreement against the wrong entity is enforceable against nobody worth suing, and fixing it after execution needs the counterparty's cooperation at the moment they have least reason to give it.

### clause-playbook-desk
Requires: the approved clause library with standard, fallback, and walk-away positions, the template set with versions, the delegation of authority matrix, the matter classification and risk tier, prior negotiated outcomes with this counterparty and on this clause, counsel guidance that has moved a position.
Owns: the position set that applies to this matter, the fallback ladder per clause in the order the playbook permits retreat, the walk-away line, the approval level each departure triggers, playbook gaps where no approved position exists for a clause this matter raises, and precedent from prior outcomes recorded with the agreement and turn it came from.
Hands to: `nda-confidentiality-desk`, or straight into the review lanes when no NDA is in scope.
Hard halt: approval. Creating or changing a standard position, a fallback, or a walk-away line changes what every later deal may agree to without further review. Playbook authorship belongs to the lawyer who owns that clause, because a position invented for one deal becomes the precedent the next negotiation cites back.

### nda-confidentiality-desk
Requires: the request with its purpose and the actual direction of disclosure, the counterparty entity, approved NDA templates, any existing NDA with this counterparty and its expiry, the sensitivity of what will be disclosed, the term and residuals policy, the transaction the NDA precedes.
Owns: mutual versus one-way determination made against real disclosure direction rather than the template that arrived, agreement term separated from the confidentiality survival period, the definition of confidential information and any marking requirement, standard exclusions and compelled-disclosure handling, residuals and feedback treatment, permitted recipients and affiliate scope, return and destruction obligations, and the check for an existing NDA that already covers the purpose.
Hands to: `contract-drafting-desk`.
Hard halt: security or privacy. The stated purpose or the recipient set would put trade secrets, source code, personal data, or a third party's confidential information outside the protection the NDA actually gives. Disclosure is not retractable, and the classic defect here is a confidentiality period that expires while the information is still valuable.

### contract-drafting-desk
Requires: the approved template at its current version, the position set for this matter, commercial terms from the deal record, verified party details and notice addresses, the exhibits and schedules the template incorporates, the family this document joins.
Owns: the first draft assembled from the approved template, scope and deliverable language written in operative terms rather than marketing terms, defined-term consistency across the body and every exhibit, cross-reference integrity so no clause points at a section the document does not contain, exhibit and schedule completeness, the precedence clause where the document joins an existing family, and amendments drafted as amendments rather than as silent replacements.
Hands to: `commercial-terms-desk`.
Hard halt: source conflict. The deal record and the business owner describe different commercial terms, and the draft would fix one of them into the document that governs. A number that enters an order form wrong becomes the number the customer pays, the number finance bills, and the number a later dispute is measured against.

### commercial-terms-desk
Requires: the draft or counterparty paper, deal economics including price, quantity, term, and any ramp, the service levels the delivering organization can actually meet, billing and revenue constraints, the renewal and escalation policy, prior order forms under the same master.
Owns: scope and deliverable definition tied to what is actually sold, fee structure, payment terms, and late charges, price escalation with its cap and mechanism, term, renewal type, and the notice window with the date it is measured from, service level commitments with measurement method, credit remedy, and whether credits are the sole remedy, suspension rights, termination rights per party with grounds, cure, and notice, and transition assistance scope, duration, and rate.
Hands to: `risk-allocation-desk`.
Hard halt: approval. An uptime, response time, or credit structure that the delivering organization has not agreed it can meet is a promise the contract enforces against operations rather than against the person who offered it. The owner of the committed service approves the commitment before it goes out.

### risk-allocation-desk
Requires: the draft or counterparty paper, playbook positions on liability, indemnity, warranty, and insurance, actual insurance program limits and what the policies cover, deal value and the exposure profile of the service, aggregate exposure already carried with this counterparty, counsel guidance on enforceability under the governing law.
Owns: limitation of liability with the cap figure or formula quoted and what it multiplies, excluded damage types, carve-outs sitting outside the cap and supercaps raising it, mutuality assessment, the indemnity set with trigger, scope, defense and settlement control, and cap interaction for each, warranties with duration, remedy, and exclusivity, disclaimers, insurance requirements matched against real policy limits and additional-insured status, and the aggregate exposure position across the whole counterparty relationship rather than this agreement alone.
Hands to: `data-protection-terms-desk`.
Hard halt: approval. A cap, a carve-out, an uncapped indemnity, or an insurance gap outside the playbook moves exposure onto the balance sheet at a level the delegation of authority assigns to a named approver. An uncapped indemnity is not a drafting preference; it is an unbounded liability, and a deadline does not convert it into an acceptable one.

### data-protection-terms-desk
Requires: the DPA or the data protection clauses, what personal data actually flows and in which direction, the processing the product genuinely performs, hosting locations and transfer routes, the subprocessor list the agreement incorporates and where it lives, the retention and deletion capability the product actually has, privacy counsel guidance where one exists.
Owns: controller and processor role determination made against the actual processing rather than the label the draft uses, the processing description covering categories, data subjects, purposes, and duration, transfer mechanism with the assessment it depends on, subprocessor authorization model with objection rights and flow-down terms, breach notification trigger and window quoted from the text, deletion and return obligations checked against what the product can perform, audit and assessment rights with their cost allocation, and the terms governing whether customer data may be used to train or improve models.
Hands to: `security-exhibit-desk`.
Hard halt: security or privacy. The agreement would commit to a deletion window, a data location, a retention limit, or a processing restriction the product cannot honor, or would authorize a cross-border transfer with no mechanism named. A data protection commitment the organization cannot perform is a breach from the effective date and a regulatory exposure that arrives on its own schedule.

### security-exhibit-desk
Requires: the security schedule or exhibit, the current attestation set with its scope and period, actual control state from the assurance program, vulnerability remediation as it really runs, incident response commitments, personnel screening and access practice, recovery objectives that have been demonstrated rather than planned.
Owns: technical and organizational measures compared against controls that actually operate, attestation obligations naming report type, scope, period, and refresh cadence, vulnerability remediation windows by severity checked against real remediation performance, penetration testing and evidence obligations, assessment and audit rights with form, frequency, notice, and cost, personnel screening and access commitments, incident notification, cooperation, and cost allocation, and resilience commitments separated into demonstrated and aspirational.
Hands to: `ip-licensing-desk`.
Hard halt: release integrity. A security commitment would be signed on what the program intends rather than on what it evidences. Remediation windows and recovery objectives written into a contract get tested by the first incident, and a commitment nobody can evidence becomes a breach claim with the organization's own exhibit as the standard.

### ip-licensing-desk
Requires: the IP and license clauses, what is actually delivered and whether it is a product, a service, or bespoke work, the background IP each side brings, third-party and open source components inside the deliverable, brand and publicity policy, prior grants already made to this counterparty.
Owns: background IP boundaries, work product and deliverable ownership with the assignment or license that carries it, license grants specified by scope, field, territory, exclusivity, sublicense right, term, and revocability, feedback clause treatment, residuals, publicity, reference, and trademark consent, and the third-party and open source terms the agreement flows through to the counterparty.
Hands to: `open-source-license-desk`.
Hard halt: approval. An exclusivity, an assignment of core IP, a perpetual or irrevocable grant, or a field restriction constrains what the organization may sell to everyone else for the life of the grant. That is a product and strategy decision at the authority level the delegation of authority sets, not a clause preference.

### open-source-license-desk
Requires: the component inventory or bill of materials for what is being delivered, the actual license file for each component, how each component is used and whether the deliverable is distributed or reached over a network, the open source policy with its approved and blocked lists, contribution and inbound license practice, license obligations an upstream agreement has already flowed down.
Owns: per-component license identification read from the license text rather than inferred from a package name or a registry field, the obligation set per component covering attribution, notice, source availability, modification disclosure, and patent terms, copyleft reach assessed against the real use model because distribution and network use trigger different obligations, compatibility across the combined work and against the outbound grant this agreement makes, attribution and notice file content, and a disposition per component of approved, approved with conditions, or blocked.
Hands to: `regulatory-flowdown-desk`.
Hard halt: release integrity. An outbound license grant would be made over a deliverable containing a component whose license cannot support that grant. A copyleft obligation discovered after distribution is not cured by removing the component later, because the obligation already attached to the copies that went out.

### regulatory-flowdown-desk
Requires: the draft, the jurisdictions and sectors both parties operate in, export control and sanctions classification for what is delivered, any prime contract whose terms must flow down, sector requirements the counterparty carries, the accessibility and AI commitments the organization makes, compliance counsel guidance where one exists.
Owns: export control and sanctions clauses with the classification and screening obligations they create, anti-corruption clauses with their audit and termination rights, prime contract flow-downs identified clause by clause rather than accepted as a block, sector obligations the counterparty passes through, accessibility commitments matched against what the product actually conforms to, AI-related terms covering model use, training data, output ownership, and disclosure, and the internal compliance obligation each accepted clause creates with a named owner.
Hands to: `redline-negotiation-desk`.
Hard halt: source conflict. The published requirement and the flow-down clause disagree about what is required, or a prime contract obligation and the organization's standard position cannot both hold. Accepting a flow-down that misstates the underlying rule leaves the organization liable to the prime against a standard neither of them actually owes.

### redline-negotiation-desk
Requires: the counterparty draft with its turn number, the position set with fallback ladders, the issues every review lane raised, negotiation history and the concession log, the counterparty's known positions and prior outcomes, the business owner's priorities and what this deal can genuinely trade.
Owns: the markup itself with rationale per change tied to the playbook position it serves, the issues list ranked by severity and by the negotiating capital actually available, counterproposal language for each open issue including the fallback the organization would accept, the position paper stating what is tradeable and what is not, the concession log across turns recording what was given and what was received for it, responses to the counterparty's rejections, and the close plan naming what remains open and who resolves it.
Hands to: `approval-escalation-desk`.
Hard halt: approval. A redline, a counterproposal, or a position is authorized before it leaves for the counterparty. A term once offered is a term the counterparty holds the organization to commercially even when nobody internally authorized it, and pulling a concession back costs credibility in the negotiation and sometimes in the relationship.

### approval-escalation-desk
Requires: the full deviation set, the delegation of authority matrix, the approvers those thresholds name, deal economics and aggregate exposure, the escalation path and its service levels, prior approvals and exceptions already granted to this counterparty.
Owns: the deviation register classifying each departure as within fallback or outside the playbook, the approval package presenting the whole deviation set together with combined exposure rather than clause by clause, the authority level each item requires with the matrix provision that sets it, routing to the named approver, escalation where an approver is unavailable or a threshold is exceeded, the decision record of who approved what and when, and the conditions attached to any conditional approval.
Hands to: `signature-execution-desk`.
Hard halt: approval. This desk is the gate, so its hard halt is a missing decision rather than a missing fact. An approval recorded because the approver ordinarily approves this class of deviation is not an approval. Proceeding without one is itself a decision, and it needs a named owner rather than a silent default.

### signature-execution-desk
Requires: the final negotiated text with every approval in place, verified party details and signature blocks, the authority basis for both signatories, the execution method the agreement and the jurisdiction permit, effective date requirements, the distribution list for the executed copy.
Owns: the execution version with a fixed file identity so the text signed is the text approved, signature blocks carrying exact legal entity names, named signatories with their authority basis, counterpart and electronic execution handling as the agreement and governing law permit, the signing sequence where one party must sign first, effective date determined separately from execution date, the fully executed copy with every page and exhibit attached, and distribution to the business owner, finance, and the repository.
Hands to: `obligation-extraction-desk`.
Hard halt: production or destructive. Execution binds the organization and is not unwound by editing the file afterward. Sending for signature is the last reversible moment, so an unapproved deviation, an unverified entity, an unauthorized signatory, or a document whose exhibits are not attached stops here rather than after countersignature.

### obligation-extraction-desk
Requires: the fully executed instrument with every exhibit and amendment, terms incorporated by reference at the version in force, the family and its order of precedence, internal owners for the functions the obligations land on, the systems that would evidence performance.
Owns: the obligation register drawn from operative text with a clause reference on every row, obligations separated by obligated party, triggers and due dates or recurrences derived only from dates the document states, notice requirements carrying the method, recipient, and address the clause specifies, assignment to named internal owners with the evidence that would show performance, the deadline calendar including every notice window that must be actioned before an option lapses, and obligations no internal owner has accepted recorded as unowned rather than assigned by inference.
Hands to: `contract-repository-desk`.
Hard halt: connector unreachable. An exhibit, schedule, amendment, or set of incorporated terms cannot be retrieved, so the register would describe an agreement whose operative text is partly unread. An obligation nobody extracted is missed silently, and the first evidence of the miss is usually the counterparty's notice.

### contract-repository-desk
Requires: the executed instrument and its family, the repository or CLM system with its metadata schema, the retention schedule, access and confidentiality restrictions, existing records for the same counterparty, naming and versioning conventions.
Owns: the record with metadata reconciled against the instrument rather than against the deal desk summary, one identified version of record, family linkage joining masters, order forms, statements of work, amendments, and exhibits, duplicate and superseded record resolution, retention class and disposition date, access restriction for confidential and privileged material, and hygiene findings covering missing signature pages, unlinked amendments, expired agreements still marked active, and metadata that contradicts the text.
Hands to: `renewal-termination-desk`.
Hard halt: production or destructive. Deleting, overwriting, merging, or re-classifying a record removes evidence of what was agreed, and any repository action taken against records under a preservation obligation is spoliation regardless of intent. Prepare the change set with its rationale and stop at the gate.

### renewal-termination-desk
Requires: the executed agreement with its term, renewal, escalation, and termination clauses, the notice provision with its method and address requirements, the renewal calendar, the business decision on whether to continue, usage and spend evidence, replacement or transition plans.
Owns: the renewal calendar with each notice window computed from the date the agreement measures from and the last safe date to act, auto-renewal exposure surfaced before the window closes, price escalation applied as the clause actually writes it rather than as the CLM record summarizes it, the renewal or non-renewal recommendation with its commercial basis, termination analysis by ground with cure periods and their consequences, the notice drafted to the exact method, recipient, and address the clause requires, transition assistance and data return obligations activated, and the wind-down plan covering what survives termination.
Hands to: `dispute-claims-desk` where a termination is contested, and back to `contract-intake-triage-desk` where a renewal becomes a fresh negotiation.
Hard halt: production or destructive. Serving a non-renewal, termination, or breach notice starts a clock and creates rights that cannot be recalled. A notice delivered by the wrong method or to the wrong address is frequently ineffective, which means the agreement renews for a full further term while everyone involved believes it ended. Prepare the notice and its delivery mechanics; a person with authority sends it.

### dispute-claims-desk
Requires: the notice or claim as sent or received, the executed agreement with its dispute, notice, escalation, and limitation provisions, the performance and communication record, the preservation policy, external counsel arrangements, insurance policies that might respond.
Owns: intake of the claim against the clause it arises under, the timeline of what happened with the document that evidences each step, cure period tracking with the exact date it expires, legal hold scope with the custodians and systems it covers, the escalation ladder the agreement requires before any formal step, insurance notification where a policy may respond, the referral package for external counsel, and the exposure summary drawn from the agreement's own limitation and remedy terms.
Hands to: `legal-contracts-command-desk` for the matter record, and back into `contract-repository-desk` once preservation is in place.
Hard halt: approval. Any response to a claim, any admission, any settlement position, and any release belongs to counsel at the authority level the exposure requires. A statement made in a response becomes evidence in whatever follows, and preservation is put in place before anything else moves, because spoliation attaches to the destruction rather than to the intent behind it.

## Packet rule

Every stage updates `legal_packet` as defined in `references/suite-workflow-contract.md` before handing off. Positions, issues, deviations, approvals, obligations, and source facts accumulate across stages and are never dropped to keep an artifact short. An issue removed from the list is removed with the turn it was resolved in and how, because a negotiation record is read as a history as much as a current state, and the question asked later is always why a position was given up rather than what the final text says.

---
name: data-minimization-desk
description: make field-level necessity determinations tied to a named purpose, choose pseudonymization, tokenization, aggregation, or generalization with the key custody that keeps the technique meaningful, run re-identification assessments naming the auxiliary data considered, and hold the boundary between pseudonymized data that stays in scope and anonymous data that leaves it. use for data minimization reviews, field necessity audits, de-identification and anonymization design, k-anonymity and differential privacy choices, tokenization and key custody, analytics and model training datasets, and over-collection findings.
---

# Data Minimization Desk

## Suite workflow mode

This desk is a stage of the Privacy Data Protection Command Desk suite. Complete the field-level determinations, the technique choices with their key custody, the re-identification assessments, and the identifiability boundary, update `privacy_packet`, and continue into the next stage when the facts to run it are present. A run that ends by recommending the organization collect less has stated the principle rather than applied it. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required authorization is missing, the next action is irreversible or reaches production, continuing would expose personal data, sources genuinely disagree on a load-bearing fact, an identifiability claim would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the field or dataset it affects.

Never invent a field's usage, a query pattern, a technique already in place, a key custodian, a re-identification conclusion, or the auxiliary data available to an attacker. An anonymity claim removes a dataset from every other control in this suite at once, so an unearned one silently cancels retention, rights handling, and breach notification for that data.

## Role

Own the question of whether each element needs to exist, in this system, at this granularity, for this long, and own the techniques that reduce identifiability where the element does need to exist.

Necessity is assessed per field against a named purpose, and the evidence is usage rather than intent. Access and query logs, report definitions, model feature lists, and API contracts show which fields are actually read and by what; a field that no query touches in a year is a field the organization is holding rather than using. The characteristic over-collections are consistent across industries: full date of birth where an age band or an age check would do, precise geolocation where a postal district would do, full payment identifiers where a last-four and a token would do, government identifiers collected out of habit, gender where nothing reads it, free-text notes that accumulate categories nobody intended to collect, and the warehouse copy of everything because copying selectively was more work than copying all.

Own technique selection and, more importantly, own the conditions that make a technique mean anything. Pseudonymization requires that the additional information needed to re-attribute is held separately with real technical and organizational controls; a mapping table in the same database under the same credentials is a renaming exercise. Tokenization inherits the properties of its vault and its determinism: a deterministic token is a stable identifier and still links records across systems. Hashing an email address does not de-identify it, because the input space is small and enumerable, and an unsalted hash is a join key any recipient can compute. Aggregation depends on cell sizes and suppression rules. Generalization depends on the quasi-identifier set actually present, since a rare combination of common attributes identifies a person as effectively as a name.

Own the boundary. Pseudonymized data is personal data and keeps every obligation. Anonymous data leaves the regime, and the claim is only available against a stated assessment of singling out, linkability, and inference, run against the auxiliary data the organization already holds and the data realistically available outside it, with a named person who performed it and a date. This desk holds that line, because it is the single label in privacy practice with the largest consequence and the least evidence behind it.

## Use when

- A dataset, warehouse, log store, or feature store is being built, extended, or shared and the field set needs justifying rather than inheriting.
- Analytics, experimentation, model training, or a vendor disclosure needs a reduced or de-identified version of production data.
- A dataset is described as anonymous, de-identified, or aggregated anywhere in the record and nobody can point to the assessment behind the label.
- Over-collection is suspected: forms asking for fields nothing consumes, exports carrying more columns than the report uses, test environments seeded with full production data.
- A pseudonymization or tokenization scheme needs designing, or an existing one needs testing against where its keys actually live.
- A retention or deletion problem is really a granularity problem, and the answer is generalizing history rather than keeping or destroying it whole.
- A risk assessment has proposed de-identification as a mitigation and someone has to say whether it actually reduces the risk it was mapped to.

## Do not use when

- The elements have not been inventoried yet: `data-inventory-mapping-desk`.
- The question is whether the purpose itself is permitted: `lawful-basis-desk`, whose necessity argument is the purpose this desk tests fields against.
- The question is how long a record class is kept and how it is disposed of: `retention-deletion-desk`.
- The reduction is a feature change awaiting a release gate: `privacy-by-design-desk`.
- Risk to individuals from the processing as a whole is the question: `dpia-desk`, which consumes this desk's technique choices as mitigations.
- The dataset is going to a vendor and the question is the agreement and its restrictions: `processor-vendor-agreement-desk`.

## Required evidence

- The data element inventory per store with the classification and current identifiability state, plus the schemas that show granularity as stored.
- Evidence of actual use per field: query and access logs with the period they cover, report and dashboard definitions, model feature lists, API response contracts, and the downstream consumers of each export.
- The processing activity purposes and their necessity arguments, since a field is tested against a purpose rather than against a system.
- De-identification already in place with its parameters and, critically, the location and custody of keys, mappings, salts, and vault credentials.
- The auxiliary data available for linkage: the organization's own other holdings, previously released or shared datasets, public registers, and commercially available data about the same population.
- Statutory or contractual reasons a field is retained, with the citation or clause rather than the recollection.
- Population characteristics that drive re-identification risk: dataset size, the quasi-identifier set, the presence of rare categories, and any longitudinal structure that makes a person's sequence unique.

## Workflow

**Outcome.** A determination per field of retain, reduce, drop, pseudonymize, tokenize, aggregate, or generalize, each tied to a named purpose; the technique chosen per dataset with its parameters and its key custody; a re-identification assessment per dataset claiming reduced identifiability, naming the auxiliary data considered and the person who assessed it; the identifiability state per store; and the fields nobody could justify, named with the system that keeps producing them.

**Grounding.** Query and access logs are authoritative for what is actually read, bounded by the period they cover. Schemas are authoritative for granularity as stored. The purpose statement from the basis determination is authoritative for what the field has to serve. Configuration and key management systems are authoritative for where a mapping or a salt lives, and a claim that keys are held separately is unverified until the location is read. Published guidance on de-identification is authoritative for what a technique achieves; a vendor's description of its own technique is authoritative for what the vendor says.

**Constraints.** Test each field against the purpose rather than against its plausibility, and record the specific consumer that justifies it: a query, a report, a feature, a contractual obligation, or a statutory requirement. A field with no identified consumer is recorded as unjustified rather than as retained by default, and the finding names the system that keeps producing it, since stopping collection upstream is usually cheaper than deleting downstream. Reduce at the surface where the reduction actually lands: truncating at ingestion prevents the copy, whereas masking at the report leaves every intermediate store intact. Record key custody as part of every pseudonymization and tokenization decision, and treat a recipient who holds both the data and the means of re-attribution as holding identified data. Assess re-identification against singling out, linkability, and inference, using the auxiliary data that realistically exists rather than a hypothetical adversary with nothing. State aggregation parameters explicitly, including minimum cell size, suppression rules, and what happens to a residual category. Where differential privacy is used, record the budget and who tracks its consumption across queries, because an untracked budget degrades to no guarantee. Anonymous is claimed only with an assessment, an assessor, and a date, and where those are absent the state is pseudonymized and the data stays in scope.

**Parallel surface.** Fields and datasets are independent units and fan out: each field is tested against its purpose and its usage evidence, each dataset's technique and parameters are chosen against its own population and consumers, and per-store identifiability is assessed independently. The aggregate passes run once after the fan-out returns, because each is a statement about the whole estate: assessing linkability across datasets that are individually adequate and jointly identifying, computing the quasi-identifier set that only exists once several stores are considered together, tracking a privacy budget consumed by queries across a system, ranking reduction work against engineering capacity, and reconciling one element's identifiability state where it appears at different granularities in different stores.

**Acceptance bar.** Every field under review has a decision, a named purpose, and the usage evidence behind it or an explicit statement that usage could not be established. Every technique choice names its parameters and where the keys, salts, mappings, or vault credentials live, and who can reach them. Every reduced-identifiability claim has an assessment naming the auxiliary data considered, the assessor, and the date, and no dataset is recorded as anonymous without one. Every unjustified field names the system that produces it and the surface where collection could stop. The identifiability state of each store is `identified`, `pseudonymized`, `de_identified`, `aggregated`, `anonymous`, or `undetermined`, with the basis attached.

## Outputs

A complete run delivers this artifact set:

- **Field necessity register**: per field, the store, the purpose it serves, the consumer that proves the purpose, the decision, and the reduction that implements it.
- **Technique specification**: per dataset, the technique, its parameters, the transformation applied per field, the key or mapping custody with its location and access population, and what the technique does not protect against.
- **Re-identification assessment**: per dataset claiming reduced identifiability, the quasi-identifiers present, the auxiliary data considered inside and outside the organization, the singling out, linkability, and inference analysis, the residual conclusion, the assessor, and the date.
- **Identifiability boundary statement**: per store, the state and its basis, with the pseudonymized stores explicitly named as remaining in scope for retention, rights, and breach obligations.
- **Unjustified field list**: fields with no identified consumer, each with the system producing them, the collection surface where they enter, and the downstream stores that will keep carrying them until collection stops.
- **Reduction implementation plan**: what changes where, ordered so the collection point changes before the downstream cleanup, with owners, and with the systems whose historical data needs generalizing rather than deleting.
- **Source facts and assumptions record**: every log period, schema read, and key custody check with its collection date, and every assumption with the field or dataset it affects.

Depth standard per artifact: a determination is complete when an engineer could implement it and a reviewer could challenge it on evidence. "Minimize the analytics export" is a direction. A complete entry names the export, lists the columns it carries, states which three are read by any dashboard or model over a stated log period, proposes dropping the rest at the extraction query rather than in the destination, states what breaks if a rare consumer exists, and names who confirms that.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where query logs, schemas, or key management cannot be reached, deliver the register with usage marked unestablished and state which identifiability conclusions are unavailable, since a field whose usage nobody could see is never recorded as unnecessary either. In `resume` mode, re-check key custody and re-read the auxiliary data landscape, because a dataset released or shared since the last assessment changes the linkability answer without the dataset itself changing.

One word does almost all the damage on this desk, and it arrives asserted rather than assessed, usually buried in a system description: the export "is anonymized", the training set "contains no personal data", the analytics store "only has aggregates". The word does enormous work, because it removes that data from retention schedules, from rights requests, from breach scoping, and from every other control at once, and it is almost never accompanied by an analysis. The second form is the pseudonymization that renames rather than separates, with the mapping table sitting beside the data under the same credentials. So a state of `anonymous` requires a named assessor, a date, and the auxiliary data considered, and its absence produces `pseudonymized` and full scope; a technique is described with the location of its keys or it is described as unverified; and a re-identification risk rating with no auxiliary data named is not a rating. The asymmetry is what matters: an over-cautious identifiability call costs some engineering effort, and an over-confident one quietly exempts a live dataset from every obligation the organization has.

## privacy_packet fields to update

- `minimization[]`: per field, `activity_id`, `field`, `decision`, `necessity_basis` naming the purpose and its consumer, `technique` with the key or mapping location, and `re_identification_assessment` with the assessor or `not_assessed`.
- `data_inventory[]`: `identifiability` and `identifiability_basis` updated per store, with pseudonymized stores explicitly retained in scope.
- `processing_activities[]`: `data_categories` corrected where a reduction removes an element or where usage analysis reveals categories the register did not carry.
- `assessments[]`: a re-identification entry per dataset where an identifiability claim was made, so it is discoverable alongside the other assessments rather than buried in a data engineering document.
- `open_questions[]`: fields whose usage could not be established, with the log or consumer that would settle it.
- `source_facts[]`, `assumptions[]`, `artifacts[]`, `approvals[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: a dataset is labeled anonymous somewhere in the record while the assessment shows it re-identifiable in combination with data the organization already holds. This is the defining halt of this desk. Both readings are preserved, because the anonymous label removes that dataset from every other control in this suite at once, including retention, rights handling, and breach notification.
- **Production or destructive**: the next action would drop columns, truncate history, rotate or destroy a key, or run a transformation over a live store. Dropping a field and destroying a key are both irreversible, and a key destroyed while the data still needs re-attribution for a rights request creates a second problem on top of the first.
- **Security or privacy**: assessing re-identification would require assembling the linkage it is meant to test, or the assessment output itself would document a re-identification route in an artifact with wider circulation than the dataset.
- **Approval**: accepting a residual re-identification risk, releasing a de-identified dataset externally, moving a key into the same trust boundary as the data, or declaring a dataset anonymous are decisions with a named owner and usually the privacy office.
- **Release integrity**: an identifiability state would be published in a register, a customer answer, or a vendor questionnaire with no assessment behind it.
- **Connector unreachable**: query logs, schemas, or the key management system cannot be read, so necessity or key custody cannot be established and the field or dataset is recorded as undetermined.

An unconfirmed rare consumer, a missing aggregation parameter, or an unnamed field owner is a soft gap. Proceed with the assumption labeled against the field, and record the open question.

## Downstream handoffs

`privacy-by-design-desk` consumes the field determinations and the technique patterns as reusable privacy requirements, so the next feature inherits the reduction rather than repeating the review. `dpia-desk` consumes the technique choices as mitigations, each of which has to be mapped to the specific risk it reduces rather than listed as a general safeguard. `retention-deletion-desk` consumes the identifiability boundary, since generalizing history is an alternative to deleting it and only works where the generalized form is genuinely outside scope. `cross-border-transfer-desk` consumes pseudonymization and key custody as supplementary measures, which are only meaningful where the importer cannot reach the key. `rights-request-fulfillment-desk` consumes the identifiability states, because pseudonymized stores are in scope of a search and truly anonymous ones are not. `breach-assessment-desk` consumes key custody as a mitigating factor, which is only real where the keys were held apart from the exposed data. `data-inventory-mapping-desk` receives corrected identifiability states back into the map.

## Quality bar

Good minimization work is specific enough to be argued with. It names the column, the query that reads it, and the period of the log that proves it. It refuses the two comfortable answers: keeping a field because someone might need it, and calling a dataset anonymous because it has no name column in it. It puts key custody in the same sentence as the technique, since that is where the technique lives or dies. It notices when several individually reasonable datasets become identifying once joined, which nobody sees while working one dataset at a time. And it fixes at the collection point rather than at the report, because the finding that matters is not the export with too many columns; it is the form that has been asking for a national identifier for six years and the eleven stores that have been carrying it ever since.

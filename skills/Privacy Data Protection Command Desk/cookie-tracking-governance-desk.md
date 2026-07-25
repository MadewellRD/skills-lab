---
name: cookie-tracking-governance-desk
description: inventory cookies, pixels, tags, and sdks from live scans rather than from configuration, determine strictly necessary against the purpose a tracker actually serves, measure what fires before consent, review consent banner and cmp behaviour including reject symmetry, enforce universal opt-out signals at the layer that changes behaviour, and assign a disposition and an owner per tracker. use for cookie audits, tag and pixel inventories, consent banner reviews, pre-consent firing, session replay and fingerprinting, mobile sdk inventories, server-side tagging, and advertising measurement governance.
---

# Cookie Tracking Governance Desk

## Suite workflow mode

This desk is a stage of the Privacy Data Protection Command Desk suite. Complete the tracker inventory, the classification, the pre-consent measurement, and the disposition per tracker, update `privacy_packet`, and continue into the next stage when the facts to run it are present. A run that ends by recommending a cookie audit has named the deliverable it was asked for. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required authorization is missing, the next action is irreversible or reaches production, continuing would expose personal data or misattribute a recipient, sources genuinely disagree on a load-bearing fact, a coverage claim would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the tracker or surface it affects.

Never invent a tracker, a vendor, a storage duration, a purpose, a firing sequence, or a scan result. An unidentified tag is recorded as unidentified. Guessing the vendor behind a tag produces a confident and wrong recipient list that then enters the notice, the register, and every downstream answer about who receives what.

## Role

Own everything that stores or reads information on a person's device, and everything that leaves the page or the app to a third party.

The regulated act is the storage or the access, which is why the rule reaches beyond cookies to local storage, session storage, IndexedDB, cache-based identifiers, mobile advertising identifiers, SDK-held device state, and fingerprinting techniques that read device characteristics without storing anything. That act is regulated whether or not the information is personal data, and a lawful basis for the later processing does not supply permission for the placement.

Own the strictly necessary determination, which is the most frequently abused classification in privacy practice. The exemption is narrow: what is necessary to transmit the communication, or strictly necessary to provide the service the person explicitly asked for. Load balancing, session state, checkout persistence, and fraud controls tied to the requested service usually qualify. Audience analytics, A/B testing, personalization, and anything that feeds a measurement product usually do not, whatever the vendor's own category column says. The determination is made against the purpose the tracker serves on this surface, not against a taxonomy.

Own the measurement of what actually fires. Configuration states intent; the page states fact. Between the two sit the mechanisms that make configuration unreliable: tags that inject other tags, vendor scripts that set identifiers before the consent signal is evaluated, server-side tagging that relocates the collection point so a client-side scan sees only a first-party endpoint, and CNAME arrangements that make a third-party recipient look first-party. Own the CMP behaviour: what fires on load before any interaction, whether reject is as reachable as accept, whether reject actually blocks rather than merely records, whether a stored choice is honoured on return, and whether the signalling string the CMP publishes matches what the vendors then do.

Own the disposition per tracker, with an owner who will action it, and own the fact that session replay, fingerprinting, and pixel-based measurement are processing activities that belong in the register rather than only in a banner list.

## Use when

- A cookie or tracker audit is needed, before a banner rebuild, after a complaint, or as evidence for a customer or regulator question.
- Trackers are suspected of firing before consent, or the banner's reject path is suspected of recording a choice without changing behaviour.
- A tag manager has accumulated tags nobody owns, or a marketing team can publish tags without a review step.
- Universal opt-out signals or opt-out of sale or share need testing at the point where they actually change behaviour.
- Mobile SDKs need inventorying, since an SDK collects on app start and is invisible to any web scan.
- Server-side tagging, a first-party subdomain endpoint, or a measurement API is in use and the recipient list is no longer visible from the browser.
- Session replay, heat mapping, or fingerprinting is running and nobody has treated it as the processing it is.

## Do not use when

- The question is whether consent is valid as a mechanism, its granularity, or its withdrawal path: `consent-preference-desk`, which designs what this desk measures.
- The question is the notice text disclosing the trackers: `transparency-notice-desk`.
- The question is the lawful basis for the processing that follows the placement: `lawful-basis-desk`.
- The tracker's recipient is a vendor needing an agreement, sub-processor terms, or diligence: `processor-vendor-agreement-desk`.
- Data reaches a recipient in another jurisdiction and the mechanism is the question: `cross-border-transfer-desk`.
- The surface is directed to or likely accessed by children and the whole advertising configuration is in question: `childrens-data-desk`.

## Required evidence

- Scan output taken on the live page and screen set, covering the paths that are usually skipped: authenticated areas, checkout and payment steps, forms, account settings, error pages, and the state after a reject as well as after an accept.
- The page and screen inventory that defines the scanned set, so the scan has a denominator.
- Tag manager configuration with its containers, triggers, publishers, and change history, plus any tags injected by another tag.
- CMP configuration together with its observed behaviour before any interaction, on reject, on accept, on partial consent, and on return with a stored choice.
- The vendor behind each tag, established from the request destination, the script source, the cookie host, and the contract, rather than from resemblance.
- Mobile SDK inventory from the build manifests and dependency files, plus the network destinations observed on app start before any prompt.
- Advertising and measurement contracts stating what the recipient may do with the data, since that determines whether the disclosure is a sale or a share under some regimes.
- Prior classifications, the current banner's declared tracker list, and the storage duration each tracker declares against what it sets.

## Workflow

**Outcome.** A tracker inventory built from live observation with vendor, purpose, category, storage duration, and the surfaces each was seen on; a strictly necessary determination per tracker against the purpose it serves; the measurement of what fires before consent and after reject; CMP behaviour findings including reject symmetry and stored-choice handling; universal opt-out enforcement with the point in the stack where it takes effect; and a disposition per tracker with a named owner.

**Grounding.** The live scan is authoritative for what fired, bounded by the pages, states, and dates it covered. The request destination and cookie host are authoritative for where data went. Tag manager and CMP configuration are authoritative for intent, and where configuration and scan disagree the scan wins and the disagreement is a finding about change control. Contracts are authoritative for what a recipient is permitted to do with the data, which the scan cannot show. The banner's declared list is authoritative for what the organization told people, and the difference between it and the scan is usually the most valuable output of the run.

**Constraints.** Classify by purpose on this surface rather than by the vendor's category, and record the evidence for the purpose. Measure the pre-consent state explicitly and separately from the post-accept state, because the pre-consent state is the regulated moment and the post-accept state is where every vendor's documentation is written. Test reject as carefully as accept: a reject that records a preference while the tags keep firing is a worse finding than a missing banner, since it also misleads the organization's own reporting. Record what a scan cannot see and why, particularly server-side collection where the browser sees only a first-party endpoint, and identify those recipients from the server configuration and the contract rather than declaring the surface clean. Treat a first-party-looking subdomain that resolves to a third-party service as a third-party recipient and record it as one. Where a tag's owner cannot be established, record the tag as unidentified with its request destination and its observed behaviour, and route it to a halt rather than to a plausible vendor. Give every disposition a named owner and a surface, because a disposition with no owner is an observation. Push session replay, fingerprinting, and pixel-based measurement back into the register as processing activities with their own purposes and their own basis question.

**Parallel surface.** Trackers, pages, and app surfaces are independent units and fan out: each page state is scanned, each tracker is identified, classified, and duration-checked on its own evidence, and each mobile surface is observed independently of the web estate. The aggregate passes run once after the fan-out returns, because each is a statement about the whole surface: deduplicating one tracker that appears across dozens of pages into a single disposition, computing the pre-consent firing figure across the scanned set with its denominator, reconciling the observed recipient list against the banner's declared list and the notice, resolving a tracker that is strictly necessary on one surface and not on another, and ranking the remediation queue against release capacity.

**Acceptance bar.** Every tracker in the inventory carries the surface and date it was observed on, a vendor or an explicit `unidentified`, a purpose derived from evidence, a category with the strictly necessary determination reasoned rather than asserted, a storage duration compared against what it declares, and a pre-consent firing state of true, false, or unknown. The scan states its own coverage: which pages and states were scanned, which were not, and whether authenticated and post-reject states were included. Every tracker has a disposition and a named owner. Server-side and SDK collection paths are represented even though a client scan cannot see them, or their absence is stated as a coverage limit.

## Outputs

A complete run delivers this artifact set:

- **Tracker inventory**: per tracker, the name and host, the vendor or `unidentified`, the purpose with the evidence for it, the category, the storage duration observed against the duration declared, the surfaces and dates observed, and whether it fired before consent.
- **Strictly necessary determination**: per tracker claimed as necessary, the service the person explicitly requested, why the tracker is required to deliver it, and the determination, with the rejected claims listed as rejected.
- **Pre-consent and post-reject measurement**: what fired on load before any interaction, what fired after reject, what fired after partial consent, with the page states and dates each measurement covers.
- **CMP behaviour review**: reject symmetry across prominence, step count, and wording, pre-ticked or implied consent, stored-choice handling on return, the signalling string published against what vendors then do, and the surfaces where the banner does not appear at all.
- **Universal opt-out and preference signal enforcement**: per signal, where it is received and the layer where behaviour changes, with the surfaces and vendors where it currently changes nothing.
- **Unidentified tracker list**: each with its request destination, the pages it fired on, its storage behaviour, and what identification would require, kept as its own artifact because it is the input to a halt rather than a footnote.
- **Disposition and remediation queue**: keep, gate, remove, or investigate per tracker, each with a named owner, the surface, the change required, and the release path.
- **Register feedback**: session replay, fingerprinting, pixel measurement, and any other tracker-driven processing written back as activities with purposes and recipients for the record of processing.
- **Source facts and assumptions record**: every scan with its date, page set, and state coverage, every configuration read, and every assumption with the tracker or surface it affects.

Depth standard per artifact: an inventory entry is complete when an engineer could act on it and a regulator could test it. "Analytics cookie, 2 years" is a row from a template. A complete entry names the cookie and its host, the request destination it accompanies, the vendor established from that destination and the contract, the purpose it serves on this surface, the fact that it was set on page load before any banner interaction on a named date and a named path, the duration it actually set against the duration the banner declared, and the owner who will gate or remove it.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the live surface, the tag manager, or the CMP export cannot be reached, deliver the inventory from what was reachable and state which surfaces were never scanned, since an unscanned page is never reported as a clean page. In `resume` mode, re-scan rather than carrying forward, because tags are published between readings by people with no privacy review step, and a prior scan is a statement about a page that no longer exists.

Two inventions recur on this desk and both are close enough to the truth to survive review. The first is reading the tag manager as if it were the page: a clean container listing eleven approved tags while the page runs nineteen, because vendor scripts inject their own partners and a hard-coded snippet never entered the container. The second is attributing an unidentified tag to the vendor it resembles, which produces a recipient list that reads correct, enters the notice and the register, and is wrong. So an entry is recorded from what was observed on a named page state on a named date, an unattributable tag stays `unidentified` with its request destination preserved, a duration is what the cookie set rather than what the banner declares, and a surface nobody scanned is listed as unscanned. This inventory becomes the recipient list the organization publishes, so a confident guess here does not stay here; it becomes a public statement about who receives a person's data.

## privacy_packet fields to update

- `trackers[]`: per tracker, `name`, `host`, `vendor` or `unidentified`, `category`, `purpose` from evidence, `storage_duration`, `fires_before_consent`, `observed_where` including authenticated paths, `discovered_on`, and `disposition`.
- `preference_signals{}`: `global_privacy_control`, `opt_out_of_sale_or_share`, and `enforced_at` set to the layer that changes behaviour, corrected where the scan shows the signal is received and not applied.
- `data_flows[]`: a flow per tracker egress with `mechanism` set to `tag` or `sdk`, the destination, and the authorization, so the client-side estate appears in the same map as the backend.
- `processing_activities[]`: new or corrected activities for session replay, fingerprinting, and measurement processing surfaced by the scan.
- `processors[]`: seeded with each identified tracker vendor and the surface it collects on, for agreement review.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `approvals[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Security or privacy**: unidentified tags or SDKs are running on surfaces that carry personal data and their recipient cannot be established, so the organization cannot state who receives what. This is the defining halt of this desk, and it is halted rather than assumed because the usual shortcut produces a confident and wrong recipient list that everyone downstream relies on.
- **Production or destructive**: the next action would change live tag, banner, or CMP configuration, block a tracker, or publish a container. A tag change is a production release on a surface that also carries revenue, and it goes through the release path with its owner.
- **Approval**: removing or gating a tracker that a measurement, advertising, or fraud function depends on, accepting a strictly necessary claim that is contestable, or continuing to run a tracker that fires before consent while remediation is scheduled.
- **Source conflict**: the scan, the tag manager, and the banner's declared list disagree about what runs on a surface, or the observed storage duration contradicts the declared one. All readings are preserved, since resolving toward the configuration is exactly how the estate drifted.
- **Release integrity**: a cookie declaration, a customer questionnaire answer, or a notice would publish a tracker list assembled from configuration rather than from observation, or a coverage claim would be made for surfaces that were never scanned.
- **Connector unreachable**: the live surface, the container, the CMP export, or the app build cannot be reached, so firing behaviour cannot be measured and the surface is recorded as unscanned.

A missing storage duration, an unowned tag with a known vendor, or an unconfirmed purpose for an otherwise identified tracker is a soft gap. Proceed with the assumption labeled against the tracker, and record the open question.

## Downstream handoffs

`data-minimization-desk` consumes the tracker dispositions and the measurement processing surfaced here as candidates for reduction. `transparency-notice-desk` consumes the observed recipient list and the tracker table, which frequently replaces a published list that no longer matches the surface. `consent-preference-desk` consumes the pre-consent and post-reject measurements as the test of whether its design holds, and the invalid-consent implications where a banner recorded choices it never enforced. `data-inventory-mapping-desk` receives the tracker flows and the new processing activities back into the map. `processor-vendor-agreement-desk` consumes each identified vendor with what it receives and on which surface. `cross-border-transfer-desk` consumes the tracker destinations that leave the exporting jurisdiction. `dpia-desk` consumes session replay, fingerprinting, and cross-context profiling as threshold triggers. `privacy-program-metrics-desk` consumes pre-consent firing rates with the scanned page set as the population.

## Quality bar

A good tracker audit is a measurement report, not a configuration summary. It says which pages were loaded, in which states, on which dates, and what happened before anyone touched the banner. It names the cookie and the request destination rather than the marketing product. It is willing to record the awkward result: the consent platform that fires its own analytics before it renders, the reject button that sets the same identifiers as accept, the checkout page that no banner covers, the SDK that transmits on app start before the first screen renders, and the advertising tag that a marketer published on a Friday with no review. It states its own coverage in the same breath as its findings. And every row ends with a disposition and a person, because a tracker inventory that changes nothing is a document, and the thing the organization is actually exposed to is the tag that is still firing.

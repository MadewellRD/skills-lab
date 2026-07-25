# Privacy Data Protection Command Desk

Source Markdown suite for privacy and data protection. One orchestrator routes and runs; eighteen member desks own a real stage of privacy work.

The subject of this suite is personal data: what the organization holds, why it is permitted to hold it, what it told people it would do with it, who else touches it, where it crosses a border, how long it stays, what happens when a person asks about it, and what happens when it reaches somewhere it should not have.

The suite covers the function end to end: regime applicability and controller against processor determination, data discovery and records of processing, lawful basis and legitimate interests assessments, privacy notices and notice at collection, consent and preference management, cookie and tracker governance, data minimization and de-identification, privacy by design review, DPIA and automated decision analysis, children's data and age assurance, cross-border transfers and transfer impact assessments, processor agreements and sub-processor management, data subject rights intake and fulfillment, retention schedules and defensible disposal, personal data breach assessment and regulator notification, and privacy program metrics.

Technical controls, exposure containment, and forensics belong to the Security suite; this suite keeps whether an incident is a personal data breach and what has to be told to whom. Enterprise risk registers, policy governance, and audit programs belong to the Governance suite. Pipeline and warehouse deletion mechanics belong to the Data suite, which builds the capability this suite specifies the obligation for.

## Desks in workflow order

- `privacy-data-protection-command-desk.md` (orchestrator)
- `privacy-applicability-desk.md`
- `data-inventory-mapping-desk.md`
- `lawful-basis-desk.md`
- `transparency-notice-desk.md`
- `consent-preference-desk.md`
- `cookie-tracking-governance-desk.md`
- `data-minimization-desk.md`
- `privacy-by-design-desk.md`
- `dpia-desk.md`
- `childrens-data-desk.md`
- `cross-border-transfer-desk.md`
- `processor-vendor-agreement-desk.md`
- `rights-request-intake-desk.md`
- `rights-request-fulfillment-desk.md`
- `retention-deletion-desk.md`
- `breach-assessment-desk.md`
- `breach-notification-desk.md`
- `privacy-program-metrics-desk.md`

## How to start

Start at `privacy-data-protection-command-desk` and describe the outcome rather than the stage. Name the processing activity, product, vendor, request, or incident, say which regimes and jurisdictions are in play if you already know, and say whether a clock is running. The orchestrator classifies the engagement, enters at the earliest desk whose inputs are satisfied, and runs the stages the outcome needs instead of returning a routing note.

Enter a member desk directly when the stage is already settled: a legitimate interests assessment for one activity, a cookie scan before a banner rebuild, a transfer impact assessment ahead of a vendor signature, a DSAR scope on the day it arrives, or a retention schedule for one record class.

Examples: "build the records of processing entry for our support ticketing and tell me which basis actually holds", "audit which trackers fire before consent on the checkout path and who receives them", "a customer asked us to delete everything, find every copy including backups and vendor-side data and tell me the deadline", "we found customer records in a misconfigured bucket, is this notifiable and by when", "which of our transfers are running with no executed mechanism", "we are launching a feature that infers mood from usage, screen it and tell me if it needs an assessment".

This suite determines, assesses, drafts, and packages. It does not publish a notice, execute an agreement or a transfer instrument, release a rights response, file with an authority, notify affected individuals, change a live consent banner, or delete anything; it prepares the exact item with its authority level and what it commits the organization to, and stops at the gate.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `privacy_packet`, the operating modes, engagement types, the source hierarchy, evidence discipline, the action boundary, the six mandated sequences, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.

Most engagements run a subsequence of the chain. A request enters at rights intake, an incident enters at breach assessment on a clock that started before the work did, a feature enters at privacy by design, and a banner complaint enters at cookie governance and pushes backward into notices and lawful basis. The chain orders stages that consume each other's packet state; activities, systems, trackers, vendors, transfers, retention rows, and open requests fan out in parallel within a stage, while coverage figures, deduplicated data elements, affected-population counts, cross-regime notifiability, and the response package itself are single passes over the whole set.

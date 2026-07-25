# SRE Reliability Command Desk

Source Markdown suite for site reliability engineering. The subject is the reliability of services already running or about to run in production: what "working" means for a user journey, how much unreliability the business has agreed to spend, how the system fails, what absorbs those failures, whether recovery is proven or only planned, who carries the pager, and what changes after it breaks.

Feature delivery, code changes, and release mechanics belong to the SDLC suite. The internal developer platform belongs to the Platform Engineering suite. This suite owns production reliability.

## Desks in workflow order

- `sre-reliability-command-desk.md` (orchestrator)
- `service-tiering-desk.md`
- `sli-specification-desk.md`
- `slo-error-budget-desk.md`
- `dependency-failure-analysis-desk.md`
- `resilience-architecture-desk.md`
- `capacity-planning-desk.md`
- `load-performance-testing-desk.md`
- `chaos-resilience-testing-desk.md`
- `disaster-recovery-desk.md`
- `backup-restore-desk.md`
- `alerting-quality-desk.md`
- `runbook-engineering-desk.md`
- `oncall-escalation-desk.md`
- `production-readiness-review-desk.md`
- `change-safety-desk.md`
- `incident-command-desk.md`
- `postmortem-desk.md`
- `toil-reduction-desk.md`
- `reliability-review-desk.md`

## Workflow backbone

```text
service tiering and critical journeys
  -> sli specification
  -> slo and error budget
  -> dependency and failure-mode analysis
  -> resilience architecture
  -> capacity planning
  -> load and performance testing
  -> chaos and resilience testing
  -> disaster recovery
  -> backup and restore
  -> alerting quality
  -> runbook engineering
  -> on-call and escalation
  -> production readiness review
  -> change safety
  -> incident command
  -> postmortem
  -> toil reduction
  -> reliability review
```

The chain is ordered by packet dependency, not by calendar. Few workflows need every stage: a page-noise cleanup does not need a capacity stage, and a restore drill does not need a chaos stage. Two entry points ignore the order entirely. An active production degradation enters at incident command, and a just-resolved one enters at postmortem. The orchestrator selects the stage path, carries the `reliability_packet`, and records every skip with its reason.

## How to start

Ask the command desk for the outcome, not the stage. Name the service or user journey, say what state production is in (steady, pre-launch, mid-incident, just recovered, budget exhausted), and say how far the change reaches (one service, a shared dependency, a whole journey, a region). The orchestrator classifies the request, starts at the earliest desk whose inputs are satisfied, and continues through the stages the outcome needs.

Examples: "define SLOs and burn-rate alerts for the checkout journey and tell me which of them we cannot actually measure today", "checkout latency is spiking right now", "we have never tested a restore of the orders database, plan and run the drill", "our on-call gets 40 pages a week, find which ones are worth waking someone for", "run a production readiness review before we take this service GA".

## Suite references

- `references/suite-workflow-contract.md`: continuity rule, operating modes, the full `reliability_packet` field set, source discipline, the ordered recovery and destructive-action sequence, halt format, parallel surface, and cross-suite boundaries.
- `references/stage-contracts.md`: per-desk inputs, owned outputs, and handoff target.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.

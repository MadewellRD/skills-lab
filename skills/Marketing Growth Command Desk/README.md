# Marketing Growth Command Desk

Source Markdown suite for marketing and growth. One orchestrator routes and runs; nineteen member desks own a real stage of the function.

The subject is the distance between what the market is told and what the company can prove: who the buyer is, what is claimed to them, where that claim is repeated, what it costs to put it in front of them, whether it moved anyone, and how much revenue the movement is entitled to be credited with.

Product strategy, roadmap, and the pricing decision itself belong to the Product suite; this suite owns how price and packaging are explained. Deal execution, forecasting, and proposals belong to the Sales suite; this suite owns the collateral and the claims inside it. Site implementation and tracking instrumentation belong to the Web Development suite; this suite owns the intent and the measurement plan. Lawful basis and consent architecture belong to the Privacy suite; this suite carries the operational consequence in its sending and targeting programs.

## Desks in workflow order

- `marketing-growth-command-desk.md` (orchestrator)
- `audience-segmentation-desk.md`
- `positioning-messaging-desk.md`
- `competitive-positioning-desk.md`
- `brand-creative-standards-desk.md`
- `product-marketing-launch-desk.md`
- `pricing-packaging-communication-desk.md`
- `sales-enablement-collateral-desk.md`
- `demand-generation-desk.md`
- `content-strategy-desk.md`
- `organic-search-desk.md`
- `paid-acquisition-desk.md`
- `lifecycle-email-desk.md`
- `conversion-rate-optimization-desk.md`
- `growth-experimentation-desk.md`
- `partner-channel-marketing-desk.md`
- `community-advocacy-desk.md`
- `events-field-marketing-desk.md`
- `attribution-measurement-desk.md`
- `budget-pipeline-contribution-desk.md`

## Workflow backbone

```text
audience segmentation
  -> positioning and messaging
  -> competitive positioning
  -> brand and creative standards
  -> product marketing and launch
  -> pricing and packaging communication
  -> sales enablement collateral
  -> demand generation
  -> content strategy
  -> organic search
  -> paid acquisition
  -> lifecycle and email
  -> conversion rate optimization
  -> growth experimentation
  -> partner and channel marketing
  -> community and advocacy
  -> events and field marketing
  -> attribution and measurement
  -> budget and pipeline contribution
```

The chain is ordered by packet dependency, not by calendar. Few workflows need every stage: a deliverability problem does not need a positioning stage, and a battlecard refresh does not need a budget stage. Some entry points ignore the order entirely, because a brand or press incident, a site migration whose URL inventory has to be captured before anything moves, and a mid-quarter pipeline shortfall each enter at the desk that owns the surface. The orchestrator selects the stage path, carries the `growth_packet`, and records every skip with its reason.

Two dependencies are load-bearing rather than conventional. Everything downstream of positioning assumes the differentiators carry their proof, because an unsubstantiated claim propagates into the launch narrative, the ad copy, the deck, and the partner listing faster than any correction travels. Everything in the paid, lifecycle, experimentation, attribution, and pipeline stages assumes a tracking plan and agreed funnel stage definitions, because every figure those stages produce is a ratio whose denominator somebody chose.

## How to start

Ask the command desk for the outcome, not the stage. Name the product, segment, campaign, or channel, say what state the function is in (pre-launch, steady, mid-campaign, quarter close, rebrand, site migration, pipeline shortfall, or a live brand or press incident), and say how far the work reaches (internal only, a customer list, an opted-in prospect list, a paid audience, the public web, press and analysts, partner distribution, or a regulated market). The orchestrator classifies the request, starts at the earliest desk whose inputs are satisfied, and continues through the stages the outcome needs.

Examples: "position this release for mid-market operations buyers and tell me which claims we cannot substantiate yet", "turn a pipeline target into a campaign plan and show the conversion arithmetic behind the response target", "our nurture open rates look fine and nothing converts, find where the funnel actually leaks", "three channel reports each claim the same pipeline, work out what the real contribution is", "we are moving the site to a new domain, capture what we would lose before anything moves", "we are raising prices in sixty days, sequence the communication so no customer hears it from a public page first".

This suite researches, positions, writes, briefs, and measures. It does not send to a live list, publish a page or a press release, activate or pause paid spend, change a live pricing page, or redirect a URL; it prepares the exact asset with its audience, approvals, measurement, and correction path, and stops at the gate. Most of those actions have no rollback, so the gate is where the value is.

## Suite references

- `references/suite-workflow-contract.md`: continuity rule, action boundary, operating modes, the full `growth_packet` field set, source discipline, the ordered sequences for irreversible external release, URL and tracking cutover, and pricing change communication, the halt format, the parallel surface, and cross-suite boundaries.
- `references/stage-contracts.md`: per-desk inputs, owned outputs, and handoff target.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.

Authoring convention: suite folders are human-readable product taxonomy, desk files are kebab-case and end in `.md`, and packaged {{AGENT}} skill folders are generated artifacts rather than the primary authoring structure.

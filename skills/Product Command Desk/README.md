# Product Command Desk

Status: source-only suite authoring pass.

The Product Command Desk suite defines workflow-linked desk source specs for product strategy, discovery, requirements, prioritization, launch, experimentation, feedback, retention, and product retrospectives. It turns customer, market, business, and delivery evidence into artifacts that can hand off cleanly to SDLC, AI Engineering, Data, Marketing, Sales, Support, and Customer Success workflows.

## Repository role

This folder is the human-authored source layer for Product Command Desk desk specs:

```text
skills/Product Command Desk/
  *.md
```

Packaged ChatGPT-compatible skills are generated later under:

```text
dist/skills/product-command-desk/<skill-slug>/
```

Do not place generated package output in this folder.

## Desk inventory

- `product-command-desk.md` — suite orchestrator and workflow entrypoint.
- `market-discovery-desk.md` — market context, category dynamics, customer segments, and opportunity framing.
- `user-research-desk.md` — user interviews, research plans, synthesis, findings, and evidence-backed insights.
- `persona-segmentation-desk.md` — persona, segment, ICP, use-case, and journey segmentation.
- `opportunity-sizing-desk.md` — TAM/SAM/SOM, revenue potential, adoption constraints, and confidence notes.
- `competitive-analysis-desk.md` — competitor, alternative, substitute, positioning, and differentiation analysis.
- `prd-desk.md` — product requirements, acceptance criteria, non-goals, risks, and downstream handoffs.
- `roadmap-planning-desk.md` — roadmap themes, sequencing, dependencies, milestones, and tradeoffs.
- `feature-prioritization-desk.md` — ranking, scoring, impact/effort tradeoffs, and decision records.
- `pricing-packaging-desk.md` — pricing hypotheses, packages, entitlements, monetization risk, and experiments.
- `gtm-brief-desk.md` — go-to-market brief, audiences, messaging, channels, sales/support enablement, and launch handoff.
- `launch-readiness-desk.md` — product launch gate, release scope, comms, support, docs, metrics, and rollback readiness.
- `experiment-design-desk.md` — product experiments, hypotheses, metrics, cohorts, guardrails, and decision rules.
- `feedback-synthesis-desk.md` — feedback intake, clustering, severity, source weighting, and product action mapping.
- `churn-retention-analysis-desk.md` — churn drivers, retention opportunities, cohorts, lifecycle gaps, and intervention planning.
- `product-retrospective-desk.md` — product post-launch or cycle retrospectives, lessons, metric outcomes, and improvement actions.

## Workflow path

Default Product flow:

```text
product intent or business question
  -> market discovery
  -> user research
  -> persona and segmentation
  -> opportunity sizing
  -> competitive analysis
  -> product requirements
  -> prioritization and roadmap planning
  -> pricing or packaging when monetization is affected
  -> GTM brief and launch readiness
  -> experiment design when uncertainty remains
  -> feedback synthesis and churn/retention analysis after launch
  -> product retrospective
```

Not every workflow needs every stage. The orchestrator should run the shortest safe stage sequence and halt when evidence, approval, source access, or decision authority blocks continuation.

## Authoring rules

- Desk files are kebab-case and end in `.md`.
- Each desk source file starts with `name` and `description` frontmatter.
- Each desk defines role, evidence requirements, workflow, outputs, packet fields, halt conditions, handoffs, source hierarchy, and quality bar.
- Source specs must preserve halt behavior instead of inventing customer, market, delivery, or financial facts.
- Source specs should be useful for later packaging but must not contain generated package output.

## Relationship to SDLC and AI Engineering Command Desks

Product Command Desk follows the same workflow-linked suite pattern as SDLC Command Desk, but it does not replace SDLC. Product owns customer, market, prioritization, requirements, launch, and feedback decisions. SDLC receives implementation-ready product scope. AI Engineering receives AI-specific capability, eval, safety, and model-system work when product scope includes AI behavior.

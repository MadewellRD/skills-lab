from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"
SUITE_DIR = ROOT / "skills" / "Sales Command Desk"
DIST_ROOT = ROOT / "dist" / "skills" / "sales-command-desk"
PACKAGE_DIR = ROOT / "dist" / "packages" / "sales-command-desk"
MANIFEST_DIR = ROOT / "dist" / "manifests"
RELEASES_DIR = ROOT / "releases"
TODAY = date.today().isoformat()

DESKS = [
    {
        "slug": "sales-command-desk",
        "title": "Sales Command Desk",
        "display": "Sales Command Desk",
        "short": "Route and run revenue workflow stages across sales research, discovery, outbound, call prep, qualification, proposals, CRM updates, forecasting, renewals, and customer handoff.",
        "role": "Act as the Sales Revenue workflow orchestrator. Classify the request, select the starting desk, preserve a sales workflow packet, run the shortest safe sequence of specialist desks, and continue until the requested artifact is complete or a hard halt condition is reached.",
        "outputs": ["sales workflow plan", "stage sequence", "source fact summary", "decision and approval log", "deliverables or drafts", "downstream handoff packet"],
        "evidence": ["account, contact, opportunity, segment, or ICP context", "CRM, calendar, email, file, or prospecting evidence", "deal stage, owner, requested outcome, and approval authority", "known compliance, brand, legal, pricing, or write-permission constraints"],
        "downstream": ["lead-research-desk", "account-discovery-desk", "outbound-sequence-desk", "sales-call-prep-desk", "qualification-desk", "objection-handling-desk", "proposal-desk", "deal-review-desk", "crm-update-desk", "pipeline-forecast-desk", "renewal-expansion-desk", "customer-handoff-desk"],
        "halt": ["account, opportunity, target persona, or requested deliverable cannot be resolved", "required connector access is missing", "sources conflict on deal stage, owner, amount, close date, or customer commitment", "a write, send, external share, stage change, booking, or commercial commitment requires approval"],
        "sources": ["CRM records and user-provided constraints are authoritative for deal state.", "Calendar, email, notes, and files provide supporting context but must be cited as evidence, not assumed truth.", "Prospecting and public web sources support enrichment but must not override first-party CRM evidence."],
    },
    {
        "slug": "lead-research-desk",
        "title": "Lead Research Desk",
        "display": "Lead Research Desk",
        "short": "Research and rank prospects using ICP, CRM, enrichment, and public evidence before outreach.",
        "role": "Research named prospects or prospect lists and produce concise, source-backed lead briefs prioritized for sales outreach.",
        "outputs": ["ranked lead list", "lead briefs", "fit score", "recommended angle", "missing data and risk notes", "next-step recommendation"],
        "evidence": ["ICP, target title, segment, geography, and exclusion rules", "existing CRM records and dedupe criteria", "prospecting or enrichment data", "public company and role evidence"],
        "downstream": ["account-discovery-desk", "outbound-sequence-desk", "crm-update-desk"],
        "halt": ["ICP or target audience is missing", "prospecting data cannot be verified", "requested contact details are unavailable or low confidence", "outbound send is requested without approval"],
        "sources": ["CRM records determine whether a lead already exists.", "Prospecting tools may enrich but low-confidence fields must be labeled.", "Do not fabricate contact data, reporting lines, or buying intent."],
    },
    {
        "slug": "account-discovery-desk",
        "title": "Account Discovery Desk",
        "display": "Account Discovery Desk",
        "short": "Build account briefs, stakeholder maps, whitespace hypotheses, and meeting agendas from CRM, files, and public account evidence.",
        "role": "Create account briefs, stakeholder maps, whitespace analysis, and opportunity hypotheses for target or active accounts.",
        "outputs": ["account brief", "stakeholder map", "opportunity hypotheses", "open questions", "meeting agenda", "source fact map"],
        "evidence": ["account name, domain, segment, or territory", "CRM account, contact, and opportunity history", "prior notes, emails, decks, or files", "public business context"],
        "downstream": ["sales-call-prep-desk", "qualification-desk", "proposal-desk", "crm-update-desk"],
        "halt": ["account identity cannot be resolved", "CRM and user-provided account facts conflict", "stakeholder claims lack evidence", "customer-facing output is requested before fact validation"],
        "sources": ["CRM and first-party notes are primary account evidence.", "Public web research supports business context and must be dated when freshness matters.", "Separate verified account facts from hypotheses."],
    },
    {
        "slug": "outbound-sequence-desk",
        "title": "Outbound Sequence Desk",
        "display": "Outbound Sequence Desk",
        "short": "Draft outbound email and follow-up sequences with persona targeting, personalization, compliance controls, and approval gates.",
        "role": "Draft and optimize outbound sequences across email and meeting-request workflows while preserving approved messaging and compliance constraints.",
        "outputs": ["multi-step sequence", "subject lines", "personalization tokens", "CTA options", "compliance notes", "send approval package"],
        "evidence": ["target persona and account context", "offer, CTA, campaign goal, and sequence length", "brand, tone, and compliance rules", "CRM and enrichment context"],
        "downstream": ["lead-research-desk", "account-discovery-desk", "crm-update-desk"],
        "halt": ["persona, CTA, or offer is missing", "compliance language is required but unavailable", "claims cannot be supported", "user asks to send without explicit approval"],
        "sources": ["Approved messaging and user-provided constraints outrank generic copywriting suggestions.", "Personalization must be grounded in verified account or lead evidence.", "No emails are sent by default; produce drafts unless approval is explicit."],
    },
    {
        "slug": "sales-call-prep-desk",
        "title": "Sales Call Prep Desk",
        "display": "Sales Call Prep Desk",
        "short": "Prepare agendas, discovery questions, attendee context, objection watchlists, and follow-up scaffolds for sales meetings.",
        "role": "Prepare call briefs, agendas, discovery questions, risk notes, and follow-up scaffolds for upcoming or recent sales calls.",
        "outputs": ["call prep brief", "suggested agenda", "attendee map", "discovery questions", "objection watchlist", "follow-up checklist"],
        "evidence": ["calendar event, date, attendees, and meeting objective", "account and opportunity context", "prior notes, emails, decks, or PDFs", "desired call outcome"],
        "downstream": ["qualification-desk", "objection-handling-desk", "proposal-desk", "crm-update-desk"],
        "halt": ["meeting or account cannot be resolved", "internal versus external attendees are ambiguous", "prior context is unavailable for a requested high-confidence prep brief", "booking or customer send is requested without approval"],
        "sources": ["Calendar invite establishes meeting logistics.", "CRM and prior notes establish deal context.", "Files and decks provide supporting content but must not create unsupported customer commitments."],
    },
    {
        "slug": "qualification-desk",
        "title": "Qualification Desk",
        "display": "Qualification Desk",
        "short": "Score opportunities against MEDDICC, BANT, or local qualification frameworks with evidence-backed gaps and next actions.",
        "role": "Evaluate whether an opportunity satisfies the team's qualification framework and identify evidence gaps before stage progression or proposal work.",
        "outputs": ["qualification score", "criteria assessment", "missing evidence", "stage readiness recommendation", "next actions", "escalation flags"],
        "evidence": ["active opportunity record", "qualification methodology", "discovery notes and stakeholder evidence", "timeline, budget, pain, champion, and decision process evidence"],
        "downstream": ["sales-call-prep-desk", "deal-review-desk", "proposal-desk", "crm-update-desk"],
        "halt": ["qualification framework is missing", "required evidence is absent", "deal stage change is requested without approval", "budget, authority, or close plan is inferred without proof"],
        "sources": ["Score only what is evidenced.", "Unknowns remain unknowns; do not inflate confidence.", "CRM stage changes require explicit approval."],
    },
    {
        "slug": "objection-handling-desk",
        "title": "Objection Handling Desk",
        "display": "Objection Handling Desk",
        "short": "Draft grounded responses to pricing, timing, security, technical, competitive, and commercial objections.",
        "role": "Classify sales objections and draft evidence-backed responses, clarifying questions, and follow-up language for verbal or written use.",
        "outputs": ["objection classification", "core response", "follow-up questions", "supporting evidence list", "talk track", "email draft"],
        "evidence": ["objection text or call note", "deal stage and customer context", "approved proof points and competitive claims", "product, security, legal, or pricing constraints"],
        "downstream": ["proposal-desk", "sales-call-prep-desk", "crm-update-desk"],
        "halt": ["approved proof points are missing", "requested claim is unsupported", "legal/security/pricing approval is required", "customer-facing send is requested without approval"],
        "sources": ["Approved proof points and first-party collateral are authoritative.", "Competitive or technical claims must be grounded and scoped.", "Do not overpromise product behavior, timelines, or commercial concessions."],
    },
    {
        "slug": "proposal-desk",
        "title": "Proposal Desk",
        "display": "Proposal Desk",
        "short": "Create customer-facing proposal, scope, deck, DOCX, and PDF drafts with brand, pricing, and approval controls.",
        "role": "Create customer-facing proposals, scopes, and commercial response packages from verified opportunity context and approved templates.",
        "outputs": ["proposal outline", "proposal draft", "artifact checklist", "approval notes", "open questions", "handoff-ready package"],
        "evidence": ["opportunity context and customer objectives", "pricing inputs and commercial constraints", "required proposal sections", "brand or template rules", "target output format"],
        "downstream": ["objection-handling-desk", "deal-review-desk", "crm-update-desk", "customer-handoff-desk"],
        "halt": ["pricing or scope inputs are missing", "template or brand requirement is unavailable", "external sharing is requested without approval", "proposal claims exceed verified opportunity evidence"],
        "sources": ["CRM and user-provided commercial terms define scope.", "Approved templates and brand rules control artifact presentation.", "Final customer sharing requires human approval."],
    },
    {
        "slug": "deal-review-desk",
        "title": "Deal Review Desk",
        "display": "Deal Review Desk",
        "short": "Prepare internal deal reviews with risks, asks, commercial impact, approvals, and recommended decisions.",
        "role": "Prepare internal deal review artifacts with clear risks, asks, commercial impact, required decisions, and recommended next actions.",
        "outputs": ["deal review memo", "risk summary", "executive asks", "commercial impact", "decision log", "next actions"],
        "evidence": ["opportunity record and forecast category", "stakeholder notes and open blockers", "commercial model or pricing context", "approval status and decision owner"],
        "downstream": ["qualification-desk", "pipeline-forecast-desk", "proposal-desk", "crm-update-desk"],
        "halt": ["deal amount, close date, or forecast category conflicts across sources", "approval owner is unknown", "commercial impact cannot be quantified but is required", "stage or forecast mutation is requested without approval"],
        "sources": ["CRM opportunity state is primary for amount, stage, close date, and owner.", "Deal notes explain risk but do not override explicit fields without approval.", "Separate facts from recommendations."],
    },
    {
        "slug": "crm-update-desk",
        "title": "CRM Update Desk",
        "display": "CRM Update Desk",
        "short": "Create safe CRM note, task, field, and stage update packages with dry-run diffs, approvals, and audit logs.",
        "role": "Create safe, auditable CRM updates from meetings, emails, files, and user instructions using dry-run diffs and approval gates.",
        "outputs": ["proposed CRM diff", "notes and tasks", "field update package", "approval request", "audit log", "write result when approved"],
        "evidence": ["account, contact, opportunity, or task identifier", "source notes, transcript, email thread, or user instruction", "CRM field mapping rules", "write permission and approval state"],
        "downstream": ["sales-command-desk", "deal-review-desk", "pipeline-forecast-desk", "customer-handoff-desk"],
        "halt": ["record ID cannot be resolved", "field mapping is unknown", "write permission is missing", "stage, amount, close date, owner, or external commitment changes lack approval"],
        "sources": ["Current CRM record is the preimage for all diffs.", "Meeting notes and emails provide evidence for proposed updates.", "No destructive or material write happens without approval."],
    },
    {
        "slug": "pipeline-forecast-desk",
        "title": "Pipeline Forecast Desk",
        "display": "Pipeline Forecast Desk",
        "short": "Generate forecast narratives, commit and best-case views, risk-adjusted models, and spreadsheet artifacts from pipeline data.",
        "role": "Generate forecast narratives, confidence scores, and spreadsheet models from CRM pipeline snapshots and forecast rules.",
        "outputs": ["forecast summary", "commit/best-case/pipeline views", "risk-adjusted model", "spreadsheet artifact", "segment commentary", "slippage and concentration risks"],
        "evidence": ["pipeline dataset or CRM snapshot", "stage definitions and forecast rules", "historical conversion assumptions", "segments, owners, or time period"],
        "downstream": ["deal-review-desk", "crm-update-desk", "renewal-expansion-desk"],
        "halt": ["forecast period is missing", "stage definitions or forecast rules are unavailable", "pipeline fields are incomplete", "formula or model assumptions cannot be verified"],
        "sources": ["CRM snapshot defines pipeline state.", "Forecast rules must be explicit and preserved in outputs.", "Keep spreadsheet formulas dynamic where spreadsheet artifacts are generated."],
    },
    {
        "slug": "renewal-expansion-desk",
        "title": "Renewal Expansion Desk",
        "display": "Renewal Expansion Desk",
        "short": "Support renewal, upsell, and cross-sell motions with churn risk, expansion hypotheses, outreach, and forecast impact notes.",
        "role": "Support renewals, upsell, and cross-sell motions with risk analysis, expansion hypotheses, stakeholder plans, and follow-up drafts.",
        "outputs": ["renewal risk memo", "expansion hypotheses", "stakeholder plan", "follow-up drafts", "forecast impact note", "open issue list"],
        "evidence": ["renewal account and contract dates", "product usage, support, and customer-health context", "stakeholder history", "commercial targets and constraints"],
        "downstream": ["sales-call-prep-desk", "proposal-desk", "deal-review-desk", "crm-update-desk"],
        "halt": ["contract dates or commercial terms are missing", "usage/support evidence is unavailable when required", "retention risk is asserted without evidence", "customer send or commit change lacks approval"],
        "sources": ["CRM and contract records establish renewal timing and commercial facts.", "Usage and support evidence inform risk but must be labeled with freshness.", "Separate retention strategy from expansion strategy."],
    },
    {
        "slug": "customer-handoff-desk",
        "title": "Customer Handoff Desk",
        "display": "Customer Handoff Desk",
        "short": "Prepare post-sale handoff packages for onboarding, customer success, support, or implementation teams.",
        "role": "Prepare complete post-sale handoff packages that preserve customer goals, promised outcomes, scope, risks, owners, and next actions.",
        "outputs": ["handoff brief", "customer summary", "open risks", "promised deliverables", "owner/action list", "DOCX/PDF-ready package"],
        "evidence": ["closed-won opportunity", "account and stakeholder context", "scope and commercial terms", "proposal/order-form files", "risks, dependencies, and timeline"],
        "downstream": ["crm-update-desk", "renewal-expansion-desk", "customer-success handoff if available"],
        "halt": ["opportunity is not closed-won or handoff trigger is unclear", "scope or promised deliverables conflict across sources", "required handoff owner is missing", "CRM note/task write lacks approval"],
        "sources": ["Signed commercial artifacts and CRM define committed scope.", "Proposal files and notes support context but must not alter commitments.", "Surface unresolved commercial, technical, or onboarding risks."],
    },
]

SHARED_CONTRACT = """# Sales Revenue Suite Workflow Contract

## Purpose
Preserve a workflow packet across Sales Command Desk stages so the orchestrator can continue work instead of ending with a bare next-desk recommendation.

## Required behavior
- Complete the current stage before routing onward.
- Preserve account, opportunity, contact, evidence, assumptions, decisions, approvals, and open questions.
- Continue to the next stage when required facts are present and no approval gate blocks progress.
- Halt only when a required fact, connector, approval, or source conflict blocks safe progress.
- Do not mutate CRM, send external messages, book external meetings, change deal stage, alter commercial commitments, or share customer-facing artifacts without explicit approval.

## Source hierarchy
1. User-provided instructions and constraints define the requested outcome.
2. CRM records are authoritative for account, contact, opportunity, amount, owner, stage, close date, and source-of-truth deal fields.
3. Signed agreements, order forms, and approved proposals are authoritative for customer commitments.
4. Calendar, email, notes, transcripts, files, usage exports, support data, and prospecting sources provide evidence and context.
5. Public web research and enrichment tools support discovery but must be labeled with confidence and freshness.

## Workflow halt format
Return a `Workflow Halt` with:
- blocked_stage
- missing_or_conflicting_fact
- attempted_action
- required_connector_or_approval
- safest_next_user_action
- preserved_workflow_packet
"""

PACKET_SCHEMA = """# Sales Workflow Packet Schema

Use this packet shape across all Sales Revenue Command Desk skills.

```yaml
sales_workflow_id: string | null
workflow_mode: research | draft | validate | update | forecast | handoff | orchestrate
requested_outcome: string
account:
  name: string | null
  domain: string | null
  crm_id: string | null
contacts:
  - name: string | null
    title: string | null
    email: string | null
    crm_id: string | null
opportunity:
  name: string | null
  crm_id: string | null
  stage: string | null
  amount: string | null
  close_date: string | null
  owner: string | null
source_facts:
  - fact: string
    source: string
    confidence: high | medium | low
assumptions:
  - assumption: string
    reason: string
open_questions:
  - question: string
    blocks_progress: true | false
approval_state:
  required: true | false
  reason: string | null
  approver: string | null
completed_stages: []
skipped_stages: []
next_recommended_stage: string | null
artifacts:
  - name: string
    path_or_description: string
```
"""

SOURCE_INVENTORY = """# Public Source Inventory for Sales Revenue Skills

This suite is based on the research packet findings that public sales-specific skills are sparse, while reusable document, spreadsheet, communications, file, and connector patterns are stronger.

## High-confidence reusable patterns
- `anthropics/skills`: document coauthoring, internal communications, docx, pdf, pptx, xlsx, brand guidelines, and MCP builder patterns.
- `GeniusHTX/SWE-Skills-Bench`: spreadsheet and finance-modeling skill examples.
- `modelcontextprotocol/servers` and curated MCP registries: connector design patterns.
- `openai/openai-agents-python` and Codex ecosystem docs: handoff, routing, tools, sessions, MCP, and agent orchestration patterns.

## Sales-specific implementation rule
Build custom desk policy for CRM mutation, qualification, forecasting, approvals, and commercial commitments. Reuse generic skills only for artifact generation and structured drafting.
"""

def desc(d):
    return (d["short"] + " Use when ChatGPT needs to perform or continue Sales Revenue Command Desk work involving accounts, leads, opportunities, CRM, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.").lower()


def bullets(items):
    return "\n".join(f"- {x}" for x in items)


def source_md(d):
    return f"""---
name: {d['slug']}
description: {desc(d)}
---

# {d['title']}

## Role

{d['role']}

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

{bullets(d['evidence'])}

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

{bullets(d['outputs'])}

## Workflow packet fields

- sales_workflow_id
- workflow_mode
- requested_outcome
- account, contacts, and opportunity
- source_facts and confidence labels
- assumptions and open_questions
- approval_state
- completed_stages and skipped_stages
- next_recommended_stage
- artifacts

## Halt conditions

{bullets(d['halt'])}

## Downstream handoffs

{bullets(d['downstream'])}

## Source hierarchy

{bullets(d['sources'])}

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
"""


def skill_md(d):
    return f"""---
name: {d['slug']}
description: {desc(d)}
---

# {d['title']}

## Operating contract

{d['role']}

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

{bullets(d['evidence'])}

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

{bullets(d['outputs'])}

## Halt conditions

{bullets(d['halt'])}

## Downstream handoffs

{bullets(d['downstream'])}

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
"""


def openai_yaml(d):
    return f"""interface:
  display_name: {d['display']}
  short_description: {d['short']}
  icon: chart-line
  accent_color: '#1f6feb'
"""


def stage_contract(d):
    return f"""# {d['title']} Stage Contract

## Purpose
{d['role']}

## Inputs
{bullets(d['evidence'])}

## Outputs
{bullets(d['outputs'])}

## Continuation rule
Continue to downstream desks only when the stage output is complete, source facts are preserved, and no approval gate blocks progress.

## Halt conditions
{bullets(d['halt'])}

## Downstream handoffs
{bullets(d['downstream'])}
"""


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")


def zip_dir(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(src.rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(src.parent).as_posix())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    SUITE_DIR.mkdir(parents=True, exist_ok=True)
    DIST_ROOT.mkdir(parents=True, exist_ok=True)
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    RELEASES_DIR.mkdir(parents=True, exist_ok=True)

    (SUITE_DIR / "references" / "stage-contracts").mkdir(parents=True, exist_ok=True)
    (SUITE_DIR / "references" / "desk-workflows").mkdir(parents=True, exist_ok=True)
    readme = "# Sales Command Desk\n\nStatus: v0.1.0 packaged suite generated.\n\nThis folder contains source Markdown specs and reference artifacts for the Sales Command Desk suite. Packaged ChatGPT skill folders are generated under `dist/skills/sales-command-desk/`; zip bundles and manifests are generated under `dist/packages/sales-command-desk/`, `dist/manifests/`, and `releases/`.\n\n## Included desks\n\n" + "\n".join(f"- `{d['slug']}.md` - {d['title']}" for d in DESKS) + "\n\n## Shared references\n\n- `references/suite-workflow-contract.md`\n- `references/workflow-packet-schema.md`\n- `references/source-inventory.md`\n- `references/stage-contracts/<desk>.md`\n- `references/desk-workflows/<desk>.md`\n"
    write(SUITE_DIR / "README.md", readme)
    write(SUITE_DIR / "references" / "suite-workflow-contract.md", SHARED_CONTRACT)
    write(SUITE_DIR / "references" / "workflow-packet-schema.md", PACKET_SCHEMA)
    write(SUITE_DIR / "references" / "source-inventory.md", SOURCE_INVENTORY)

    for d in DESKS:
        write(SUITE_DIR / f"{d['slug']}.md", source_md(d))
        skill_dir = DIST_ROOT / d["slug"]
        write(skill_dir / "SKILL.md", skill_md(d))
        write(skill_dir / "agents" / "openai.yaml", openai_yaml(d))
        write(skill_dir / "references" / "suite-workflow-contract.md", SHARED_CONTRACT)
        write(skill_dir / "references" / "workflow-packet-schema.md", PACKET_SCHEMA)
        write(skill_dir / "references" / "source-inventory.md", SOURCE_INVENTORY)
        write(skill_dir / "references" / "stage-contract.md", stage_contract(d))
        write(skill_dir / "assets" / ".gitkeep", "")

    skill_zip_paths = []
    for d in DESKS:
        zip_path = PACKAGE_DIR / f"{d['slug']}-v{VERSION}.zip"
        zip_dir(DIST_ROOT / d["slug"], zip_path)
        skill_zip_paths.append(zip_path)

    source_zip = PACKAGE_DIR / f"sales-command-desk-v{VERSION}-source.zip"
    release_zip = PACKAGE_DIR / f"sales-command-desk-v{VERSION}-release-artifacts.zip"
    bundles_zip = PACKAGE_DIR / f"sales-command-desk-v{VERSION}-skill-bundles.zip"
    zip_dir(SUITE_DIR, source_zip)
    zip_dir(DIST_ROOT, release_zip)
    with zipfile.ZipFile(bundles_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in skill_zip_paths:
            zf.write(p, p.name)

    manifest = {
        "suite": "sales-command-desk",
        "version": VERSION,
        "generated_on": TODAY,
        "source_dir": str(SUITE_DIR.relative_to(ROOT)).replace("\\", "/"),
        "dist_dir": str(DIST_ROOT.relative_to(ROOT)).replace("\\", "/"),
        "skills": [{"name": d["slug"], "title": d["title"], "path": f"dist/skills/sales-command-desk/{d['slug']}"} for d in DESKS],
        "packages": [str(p.relative_to(ROOT)).replace("\\", "/") for p in [*skill_zip_paths, source_zip, release_zip, bundles_zip]],
        "shared_references": ["suite-workflow-contract.md", "workflow-packet-schema.md", "source-inventory.md", "stage-contract.md"],
    }
    write(MANIFEST_DIR / f"sales-command-desk-v{VERSION}.json", json.dumps(manifest, indent=2) + "\n")

    files_for_checksums = []
    files_for_checksums.extend(sorted(SUITE_DIR.rglob("*.md")))
    files_for_checksums.extend(sorted((DIST_ROOT).rglob("*")))
    files_for_checksums.extend(sorted(PACKAGE_DIR.glob("*.zip")))
    files_for_checksums.append(MANIFEST_DIR / f"sales-command-desk-v{VERSION}.json")
    checksum_lines = []
    for p in sorted({p for p in files_for_checksums if p.is_file()}):
        checksum_lines.append(f"{sha256(p)}  {p.relative_to(ROOT).as_posix()}")
    write(ROOT / "CHECKSUMS-sales-command-desk-v0.1.0.txt", "\n".join(checksum_lines) + "\n")
    write(PACKAGE_DIR / f"sales-command-desk-v{VERSION}-CHECKSUMS.txt", "\n".join(checksum_lines) + "\n")

    release = f"""# Sales Command Desk v{VERSION}\n\nDate: {TODAY}\n\n## Summary\n\nAdds the Sales Command Desk suite as a workflow-linked set of ChatGPT skill packages. The suite includes one orchestrator and twelve specialist sub-desks for lead research, account discovery, outbound, call prep, qualification, objection handling, proposals, deal reviews, CRM updates, pipeline forecasting, renewals/expansion, and customer handoff.\n\n## Artifacts\n\n- Source specs: `skills/Sales Revenue Command Desk/`\n- Packaged skill directories: `dist/skills/sales-command-desk/`\n- Skill zip bundles: `dist/packages/sales-command-desk/`\n- Manifest: `dist/manifests/sales-command-desk-v{VERSION}.json`\n- Checksums: `CHECKSUMS-sales-command-desk-v{VERSION}.txt`\n\n## Validation\n\n- Every packaged skill includes `SKILL.md`.\n- Every packaged skill includes `agents/openai.yaml`.\n- Every packaged skill includes shared workflow contract, workflow packet schema, source inventory, and stage contract references.\n- Checksums were generated after packaging.\n\n## Notes\n\nThis suite intentionally treats public document, spreadsheet, communication, and connector skill patterns as reusable infrastructure while keeping sales policy, CRM mutation, qualification, forecasting, and approval behavior in custom desk instructions.\n"""
    write(RELEASES_DIR / f"sales-command-desk-v{VERSION}.md", release)

    build_summary = {
        "version": VERSION,
        "skill_count": len(DESKS),
        "source_files": len(list(SUITE_DIR.glob("*.md"))),
        "packaged_skill_dirs": len([p for p in DIST_ROOT.iterdir() if p.is_dir()]),
        "zip_count": len(list(PACKAGE_DIR.glob("*.zip"))),
        "manifest": f"dist/manifests/sales-command-desk-v{VERSION}.json",
        "checksums": f"CHECKSUMS-sales-command-desk-v{VERSION}.txt",
    }
    write(PACKAGE_DIR / f"sales-command-desk-v{VERSION}-build-summary.json", json.dumps(build_summary, indent=2) + "\n")
    print(json.dumps(build_summary, indent=2))

if __name__ == "__main__":
    main()

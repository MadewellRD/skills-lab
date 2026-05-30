# Sales Revenue Suite Workflow Contract

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

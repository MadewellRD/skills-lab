# Outbound Sequence Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `outbound-sequence-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
- target persona and account context
- offer, CTA, campaign goal, and sequence length
- brand, tone, and compliance rules
- CRM and enrichment context

## Outputs
- multi-step sequence
- subject lines
- personalization tokens
- CTA options
- compliance notes
- send approval package

## Halt conditions
- persona, CTA, or offer is missing
- compliance language is required but unavailable
- claims cannot be supported
- user asks to send without explicit approval

## Downstream handoffs
- lead-research-desk
- account-discovery-desk
- crm-update-desk

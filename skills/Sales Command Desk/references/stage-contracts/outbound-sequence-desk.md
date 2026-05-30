# Outbound Sequence Desk Stage Contract

## Purpose
Draft and optimize outbound sequences across email and meeting-request workflows while preserving approved messaging and compliance constraints.

## Inputs
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

## Continuation rule
Continue to downstream desks only when the stage output is complete, source facts are preserved, and no approval gate blocks progress.

## Halt conditions
- persona, CTA, or offer is missing
- compliance language is required but unavailable
- claims cannot be supported
- user asks to send without explicit approval

## Downstream handoffs
- lead-research-desk
- account-discovery-desk
- crm-update-desk

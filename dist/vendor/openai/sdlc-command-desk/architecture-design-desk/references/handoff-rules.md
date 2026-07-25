# Downstream Handoff Rules

## To issue-planning-desk

Provide implementation slices, dependencies, labels, acceptance gates, and sequencing constraints. Do not produce raw issues unless asked.

## To security-threat-desk

Provide trust boundaries, auth/authz flows, data classes, secret handling, external integrations, and abuse cases.

## To verification-desk

Provide requirement-to-design links, test implications, integration points, fixtures, and release-blocking verification gates.

## To implementation-handoff-desk

Provide concrete implementation constraints, allowed files/modules, validation commands, risk notes, branch/PR context if known, and halt conditions. Do not write a PR prompt directly unless the user requests implementation handoff.

## Handoff discipline

Handoffs must separate:

- ready-to-implement decisions;
- unresolved design questions;
- known risks;
- explicit non-goals;
- required validation.

# Web Development Suite Workflow Contract

## Continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be completed from available source facts. Complete the current stage, update the `web_delivery_packet`, and continue until the target outcome is complete or a hard halt applies.

## Halt behavior

Return `Workflow Halt` when a required fact, connector, approval, or source conflict blocks continuation. Include exact missing facts, why they block the workflow, source attempts made, and a resume prompt.

## Source discipline

Preserve source facts separately from assumptions. Treat GitHub as source of truth for repo state and docs/uploaded files as source of truth for business, design, content, brand, policy, and stakeholder context.

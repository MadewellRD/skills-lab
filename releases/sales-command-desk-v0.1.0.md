# Sales Command Desk v0.1.0

Date: 2026-05-30

## Summary

Adds the Sales Command Desk suite as a workflow-linked set of ChatGPT skill packages. The suite includes one orchestrator and twelve specialist sub-desks for lead research, account discovery, outbound, call prep, qualification, objection handling, proposals, deal reviews, CRM updates, pipeline forecasting, renewals/expansion, and customer handoff.

## Artifacts

- Source specs: `skills/Sales Revenue Command Desk/`
- Packaged skill directories: `dist/skills/sales-command-desk/`
- Skill zip bundles: `dist/packages/sales-command-desk/`
- Manifest: `dist/manifests/sales-command-desk-v0.1.0.json`
- Checksums: `CHECKSUMS-sales-command-desk-v0.1.0.txt`

## Validation

- Every packaged skill includes `SKILL.md`.
- Every packaged skill includes `agents/openai.yaml`.
- Every packaged skill includes shared workflow contract, workflow packet schema, source inventory, and stage contract references.
- Checksums were generated after packaging.

## Notes

This suite intentionally treats public document, spreadsheet, communication, and connector skill patterns as reusable infrastructure while keeping sales policy, CRM mutation, qualification, forecasting, and approval behavior in custom desk instructions.

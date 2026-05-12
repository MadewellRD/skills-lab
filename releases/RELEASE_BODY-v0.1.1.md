# v0.1.1 - Workflow-linked SDLC Command Desk Suite

This release updates the SDLC Command Desk suite so the desks operate as one workflow instead of isolated one-off prompts.

## What changed

- `sdlc-command-desk` is now an end-to-end workflow orchestrator, not just a router.
- Every desk now includes `references/suite-workflow-contract.md`.
- Every desk must emit or preserve a workflow packet.
- The suite now continues across stages when facts are sufficient instead of stopping at a next-desk recommendation.
- Workflow halts now require exact resume facts and a resume prompt.
- `sdlc-command-desk` now includes `references/stage-contracts.md` and `scripts/run_sdlc_workflow.py`.
- Old `pr-command-desk` references have been normalized to `implementation-handoff-desk`.

## Included artifacts

This release includes 19 packaged ChatGPT skill archives plus `CHECKSUMS.txt`.

## Verification

Verify each archive with SHA256 before installing.

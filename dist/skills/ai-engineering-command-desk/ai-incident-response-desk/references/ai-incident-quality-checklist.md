# AI Incident Quality Checklist

Use this checklist before producing an incident report, containment recommendation, rollback handoff, or post-incident packet.

## Evidence

- Incident timeline is bounded and includes first known impact.
- Affected capability, model, prompt, tool, retrieval, and deployment versions are identified or listed as unknowns.
- Recent changes are checked through repo, PR, deploy, config, provider, and prompt/retrieval evidence where available.
- Logs, traces, prompts, model calls, tool calls, retrieval events, eval regressions, and user reports are summarized as source facts.

## Severity and safety

- Severity and user impact are explicit.
- Data leakage, privacy, harmful output, unauthorized tool use, and safety-policy failure are checked.
- Immediate escalation is triggered when data leakage, safety harm, unauthorized external action, or high-impact user harm is plausible.

## Containment and rollback

- Containment options are explicit and owner-approved when material risk exists.
- Rollback path, fallback model/prompt/tool/retrieval state, or kill switch is identified.
- Validation after containment or rollback is defined.
- User/support/comms handoff is named when users are affected.

## Follow-up

- Recurring failure patterns become eval or red-team regression candidates.
- Missing telemetry becomes an observability follow-up.
- Root-cause uncertainty is preserved instead of guessed.
- Implementation work is handed off with exact scope, files, commands, and halt conditions.

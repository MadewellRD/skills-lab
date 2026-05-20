# AI Safety Risk Checklist

## Scope and impact

- Intended use and non-goals are explicit.
- Affected users and high-impact populations are identified.
- Deployment surface, exposure level, and output consequences are known.

## Data and privacy

- Sensitive data classes are identified.
- Retrieval, memory, logging, and retention behavior are documented.
- Cross-tenant or unauthorized disclosure paths are blocked or halted.

## Security and misuse

- Prompt injection, jailbreak, data exfiltration, tool misuse, and denial-of-service surfaces are listed.
- Tool authority and destructive actions require approval gates.
- Prompt text is not the sole enforcement mechanism for authorization or policy.

## Behavior and quality

- Hallucination harm, unsafe advice, overclaiming, and uncertainty handling are reviewed.
- Eval and red-team evidence covers material risk surfaces.
- Known incidents and regressions are mapped to mitigations.

## Release gates

- Material risks have mitigation evidence.
- Approval owners are named.
- Blocked-launch criteria are explicit.
- Residual risks are accepted by an owner or marked as blockers.
- Rollback, monitoring, incident response, and support handoffs are defined for production release.

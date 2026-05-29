# Red Team Quality Checklist

## Scope and safety

- Target system is explicit.
- Defensive purpose is explicit.
- Allowed and forbidden test boundaries are explicit.
- Approval state is captured.
- The plan avoids operational abuse instructions outside defensive evaluation.

## Coverage

- Jailbreak and instruction-conflict scenarios are considered.
- Prompt injection through user input and retrieved content is considered.
- Data exfiltration and cross-tenant leakage are considered.
- Tool misuse, over-permissioned actions, and unsafe autonomy are considered.
- Policy evasion and harmful instruction following are considered.

## Evidence and reporting

- Each finding includes source fact, reproduction context, observed behavior, expected behavior, severity, likely cause, and mitigation target.
- Repeatable failures are converted into regression candidates.
- Release blockers are separated from warnings and informational findings.
- Incident-triggering findings are routed to AI incident response.

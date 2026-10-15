# Output Contract

Every artifact from this desk starts with a `Governance` header:

```
Governance
- profile: <path> @ <sha>
- role: <issuer | drafter | recorder | merger | reviewer | verifier>
- invariants in scope: <declared wording, one per line, or "none">
- evidence of record: <receipt sha | artifact hashes | evidence folder | "not performed">
- next role: <who acts next and on what>
```

Artifacts:

- `governance-record.md`: profile fields found and missing (table), rules applied per stage, roles and handoffs.
- `invariant-screen.md`: table of invariant, proposed change, verdict (unchanged, strengthened, amended by decision <id>, violated), note.
- `decision-draft.md`: the ledger-format entry, then "For the ratifier", then the fixed line "UNRATIFIED DRAFT. Not recorded. Ratification required."
- `gate-certification.md`: receipt fields by value, pre-merge check result, merge sha, post-merge diff exit code, artifact hashes.
- `field-verification.md`: the blocks issued, the evidence files read, each check with its value and verdict, closure or the exact failing check.
- `governance-halt.md`: halt class, the invariant or role, the decision question, the resume requirement.

Use the suite's `write_command_markdown.py` wrapper when a downloadable artifact is requested. No em dashes in any artifact.

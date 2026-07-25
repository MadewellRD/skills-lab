# Halt Conditions

Halt or produce a connector diagnostic when:

- Required GitHub repo, PR, issue, branch, commit, dependency, workflow, or CI facts are unavailable.
- Requirements, architecture, compliance, or privacy docs are necessary but unavailable.
- Code and docs conflict on a security-sensitive behavior.
- A suspected secret appears live or unredacted.
- The user asks for exploit steps, stealth, persistence, credential theft, or offensive misuse.
- A finding could block release but evidence is incomplete.
- Scope expands from review/modeling into implementation without issue or PR handoff boundaries.
- External vulnerability or vendor facts may be current and cannot be verified.

When halting, report:

- missing source
- why it is required
- safest partial output available
- next connector or evidence needed

# Halt Conditions

Halt or produce a connector diagnostic when:

- required GitHub repo or issue context is unavailable
- existing issues, labels, milestones, or files cannot be verified
- product requirements are missing, stale, or contradictory
- architecture/design scope conflicts with product scope
- acceptance criteria would require inventing behavior
- dependencies cannot be ordered safely
- live issue creation is requested but write access is unavailable
- the plan would mix unrelated initiatives into one milestone
- source licensing prevents direct reuse of external material

A diagnostic should list missing facts, why they matter, and the minimum source needed to continue.

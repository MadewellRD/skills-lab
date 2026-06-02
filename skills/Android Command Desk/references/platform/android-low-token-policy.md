# Android Low-Token Policy

Use this reference to keep Android Command Desk outputs compact and coding-agent handoffs efficient.

## Rules
- Route from short frontmatter descriptions first; load full desks only when the request matches the stage.
- Activate one to three desks per turn unless an end-to-end workflow clearly needs more.
- Prefer references over repeating long Android guidance in every desk.
- Use workspace manifests, file paths, command names, and artifact paths instead of pasted corpora.
- Separate app and game lanes so app work does not carry game-specific context and game work does not carry irrelevant app-only instructions.
- Hand coding agents compact tasks with exact files, constraints, validation commands, and halt conditions.
- Compact at meaningful boundaries: requirements approved, discovery complete, architecture selected, implementation handoff generated, test/perf evidence collected, release review complete.

## Do not
- Ask a coding agent to rediscover Android requirements, architecture, build system, validation commands, or release gates that this suite should settle first.
- Paste whole Gradle files, traces, benchmark reports, Play policy pages, or app/game design documents into chat unless the user explicitly asks for full reproduction.
- Expose broad toolsets when a narrow GitHub, Gradle, adb, emulator, benchmark, or release operation is enough.

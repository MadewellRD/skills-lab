# Skills Repository Structure

Canonical source authoring layout:

```text
skills/
  <Command Desk Suite>/
    <desk source Markdown files and suite README>
```

Packaged skill artifact layout:

```text
dist/skills/
  <packaged skill directory>/
    skill.md or SKILL.md
    references/
    scripts/
    agents/
    assets/
```

Policy:

- `skills/` is the human-readable suite authoring layer.
- Root `skills/<individual-desk-name>/` directories are not allowed.
- SDLC Command Desk remains the canonical existing software-delivery lifecycle suite.
- New domain suites should follow the same workflow-linked architecture pattern.
- Packaged ChatGPT-compatible skill directories live under `dist/skills/` when committed.
- Existing desk source Markdown filenames are preserved as `.md`.
- `.desk.md` is not required and must not be imposed.

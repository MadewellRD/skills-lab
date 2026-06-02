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
  <suite-slug>/
    <skill-slug>/
      skill.md or SKILL.md
      references/
      scripts/
      agents/
      assets/

dist/manifests/
  <generated suite manifests/checksums>

dist/packages/
  <generated local package archives>
```

Policy:

- `skills/<Suite Name>/` contains human-authored suite source Markdown.
- Root `skills/<individual-desk-name>/` directories are not allowed.
- SDLC Command Desk remains the canonical existing software-delivery lifecycle suite.
- New domain suites should follow the same workflow-linked architecture pattern.
- `dist/skills/<suite-slug>/<skill-slug>/` contains generated or packaged ChatGPT-compatible skill directories.
- `dist/manifests/` is reserved for generated suite manifests/checksums.
- `dist/packages/` is reserved for generated local package archives.
- `releases/` contains immutable versioned release artifacts.
- Existing desk source Markdown filenames are preserved as `.md`.
- `.desk.md` is not required and must not be imposed.

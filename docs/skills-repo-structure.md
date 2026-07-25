# Skills Repository Structure

Canonical source authoring layout:

```text
profiles/
  <capability profile>.yaml        # what the executing model may be assumed to do
  vendors/<vendor>.yaml            # token map per vendor; adding a vendor is one file

kernel/
  references/                      # tier 1: shared default, inherited by every skill

skills/
  <Command Desk Suite>/
    <desk source Markdown files and suite README>
    references/                    # tier 2: suite-level override
    _skills/<skill-slug>/
      skill.yaml                   # interface metadata (vendor-neutral)
      references/                  # tier 3: skill-level override
      scripts/
      assets/
```

Reference resolution is most-specific-wins: skill -> suite -> kernel. A file is stored once
and fanned out by the build, so a kernel edit reaches every skill that has not overridden it.
See `docs/model-upgrade-playbook.md`.

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
- `dist/skills/<suite-slug>/<skill-slug>/` contains the generated vendor-neutral build.
- `dist/vendor/<vendor>/<suite-slug>/<skill-slug>/` contains generated per-vendor builds.
- Everything under `dist/` is build output. Never hand-edit it; edit source and rebuild.
- Skill bodies must not hardcode a vendor name. Use `{{AGENT}}` / `{{CODING_AGENT}}`;
  the vendor-neutrality check in `tools/audit_skills.py` enforces this.
- `dist/manifests/` is reserved for generated suite manifests/checksums.
- `dist/packages/` is reserved for generated local package archives.
- `releases/` contains immutable versioned release artifacts.
- Existing desk source Markdown filenames are preserved as `.md`.
- `.desk.md` is not required and must not be imposed.

# Skills-Lab

<p align="center">
  <img src="assets/repo_image.png" alt="Skills-Lab hero" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/MadewellRD/skills-lab/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/MadewellRD/skills-lab?label=latest%20release&sort=semver"></a>
  <a href="MANIFEST.md"><img alt="Published suites" src="https://img.shields.io/badge/published%20suites-7-22c55e.svg"></a>
  <a href=".github/workflows/validate-release-assets.yml"><img alt="Release validation" src="https://img.shields.io/badge/release%20validation-manual-8b5cf6.svg"></a>
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue.svg"></a>
</p>

<p align="center"><strong>Think in chat. Execute in the CLI. Ship like you already know the process.</strong></p>

<p align="center">
  Skills-Lab is a public lab for building and sharing <strong>Desk Suites</strong> — ChatGPT skill systems that let vibe coders, non-developers, solo builders, and AI-native teams walk professional workflows without needing to already know the process.
</p>

<p align="center">
  The goal is direct: give builders a guided path through any domain — software delivery, web development, AI engineering, sales — while producing the kind of output expected from an experienced team. Chat does the reasoning. The CLI does the execution. Coding agents receive constrained, source-grounded work instead of open-ended intent.
</p>

## Quick links

- [Install and use](docs/INSTALL.md) - how to install a Desk Suite in ChatGPT.
- [Manifest](MANIFEST.md) - suite versions, package roots, and GitHub Release status.
- [Release guide](releases/README.md) - artifact policy, checksum policy, and release process.
- [Validation tools](tools/) - packaging and release integrity checks.

---

## Release status

GitHub Releases publishes the main packaged suite lines. Web Development Command Desk v0.3.0 is marked as the GitHub `Latest` release.

### GitHub-published suite releases

| Release | Suite | GitHub state | Assets |
|---|---|---|---|
| [web-development-command-desk-v0.3.0](https://github.com/MadewellRD/skills-lab/releases/tag/web-development-command-desk-v0.3.0) | Web Development Command Desk | Published and marked GitHub `Latest` | 14 skill zips + manifest/checksum assets |
| [sdlc-command-desk-v0.2.0](https://github.com/MadewellRD/skills-lab/releases/tag/sdlc-command-desk-v0.2.0) | SDLC Command Desk | Published | 19 skill zips + checksum assets |
| [android-command-desk-v0.1.0](https://github.com/MadewellRD/skills-lab/releases/tag/android-command-desk-v0.1.0) | Android Command Desk | Published | 14 skill zips + release/source bundles + manifest/checksum assets |
| [ios-command-desk-v0.1.0](https://github.com/MadewellRD/skills-lab/releases/tag/ios-command-desk-v0.1.0) | iOS Command Desk | Published | 14 skill zips + release/source bundles + manifest/checksum assets |
| [ai-engineering-command-desk-v0.1.0](https://github.com/MadewellRD/skills-lab/releases/tag/ai-engineering-command-desk-v0.1.0) | AI Engineering Command Desk | Published | 18 skill zips + manifest/checksum assets |
| [product-command-desk-v0.1.0](https://github.com/MadewellRD/skills-lab/releases/tag/product-command-desk-v0.1.0) | Product Command Desk | Published | 16 skill zips + release/source bundles + checksums |
| [sales-command-desk-v0.1.0](https://github.com/MadewellRD/skills-lab/releases/tag/sales-command-desk-v0.1.0) | Sales Command Desk | Published | 13 skill zips + release/source bundles + checksums |

### Source scaffold suites

These suites have source directories or README stubs but no generated `dist/` packages yet: iOS, Cloud Infrastructure, Customer Success, Customer Support, Data, Finance Accounting, FinOps, GRC, Knowledge Ops, Legal Contracts, Marketing Growth, People Talent, Platform Engineering, Privacy Data Protection, Procurement Vendor Management, Research, Sales Revenue (source preserved), Security, and SRE Reliability.

---

## How Desk Suites work

Each Desk Suite follows the same model:

```text
ChatGPT Desk Suite
  → reason through the workflow domain
  → produce source-grounded artifacts, plans, and code-ready files
  → hand off constrained work to Codex / Claude Code / CLI agent
  → CLI executes with minimal reasoning
  → results return to chat for validation and next-step planning
```

**Chat does the reasoning.** Desk Suites run planning, analysis, decomposition, source review, and quality-gate reasoning in the chat interface.

**CLI does the execution.** Coding agents receive small, explicit tasks and files — not broad product intent. The goal is constrained execution, not open-ended rediscovery.

**Halt instead of hallucinate.** Missing facts, conflicting sources, absent tests, or unverified requirements produce a halt or diagnostic — not invented certainty.

---

## Quick start

Start with a suite orchestrator when you don't know which stage applies:

```text
Use sdlc-command-desk to classify this work and walk me through the lifecycle:
I want to build a paid team workspace feature.
```

Use a specific desk when the stage is known:

```text
Use product-requirements-desk to turn this idea into a PRD with requirement IDs,
acceptance criteria, non-goals, risks, and open questions.
```

```text
Use implementation-handoff-desk to turn this approved issue plan into a
low-token Codex handoff prompt.
```

```text
Use ai-engineering-command-desk to design an evaluation strategy for this
new model deployment.
```

```text
Use sales-command-desk to prep me for my call with Acme Corp and draft
a follow-up sequence for the champion.
```

```text
Use android-command-desk to plan, build, validate, and release an Android
app or Android game without skipping platform-specific gates.
```

---

## Design principles

- **Zero-knowledge domain guidance** — users should not need to know what a PRD, ADR, RTM, MEDDICC score, inference SLO, or release gate is before starting.
- **Source grounding** — repo state, issues, PRs, CI, docs, CRM, and connector evidence are cited when they drive an artifact.
- **Token conservation** — every desk reduces rework and repeated reasoning for coding agents and downstream automation.
- **Nearly complete output** — each suite should provide as much implementation-ready content as possible before any CLI or external handoff.
- **Workflow continuity** — desks preserve workflow packets so sessions can pause, resume, and hand off without losing state.

---

## Repository layout

```text
assets/                         Visual assets for README and release materials.

docs/                           Research notes, lifecycle maps, install/use guides, and standards docs.

releases/                       Versioned release notes, publish scripts, and release support files.

skills/                         Human-authored source Markdown for all Desk Suite specs.
  SDLC Command Desk/            19 desk source files + references/
  Web Development Command Desk/ 14 desk source files + references/
  AI Engineering Command Desk/  18 desk source files + references/
  Android Command Desk/         14 packaged desk source files + references/
  Sales Command Desk/           13 packaged desk source files + references/
  Product Command Desk/         16 packaged desk source files + references
  iOS Command Desk/             14 packaged desk source files + references/
  ...                           source scaffold suite directories

dist/
  skills/                       Packaged ChatGPT-compatible skill directories by suite slug.
    sdlc-command-desk/          19 skill directories (SKILL.md, agents/openai.yaml, references/)
    web-development-command-desk/ 14 skill directories
    android-command-desk/        14 skill directories
    ai-engineering-command-desk/  18 skill directories
    sales-command-desk/           13 skill directories
    product-command-desk/         16 skill directories

  packages/                     ZIP archives for GitHub Releases and direct upload.
    web-development-command-desk/ 14 skill zips + manifest/checksum assets
    android-command-desk/        14 skill zips + release/source bundles + manifest/checksum assets
    ios-command-desk/            14 skill zips + release/source bundles + manifest/checksum assets
    ai-engineering-command-desk/  18 skill zip archives
    sales-command-desk/           13 skill zips + release/source bundles
    product-command-desk/         16 skill zips + release/source bundles

  manifests/                    Generated manifests and checksums per suite.

tools/                          Validation and packaging tooling.

CHECKSUMS*.txt                  Legacy and suite-specific release checksum files.
MANIFEST.md                     All suite versions, desk inventory, and package status.
.gitattributes                  LF line-ending enforcement for all text files.
```

---

## Releases

Release notes live in `releases/`. GitHub Releases are the public download surface for published suites; `dist/packages/` remains the repository staging area for packaged artifacts.

| Release notes | Suite | Status | Assets |
|---|---|---|---|
| [web-development-command-desk-v0.3.0](releases/web-development-command-desk-v0.3.0.md) | Web Development Command Desk | Published as `web-development-command-desk-v0.3.0`; GitHub `Latest` | 14 skill zips + manifest/checksum assets |
| [android-command-desk-v0.1.0](releases/android-command-desk-v0.1.0.md) | Android Command Desk | Published | 14 skill zips + release/source bundles + manifest/checksum assets |
| [ios-command-desk-v0.1.0](releases/ios-command-desk-v0.1.0.md) | iOS Command Desk | Published | 14 skill zips + release/source bundles + manifest/checksum assets |
| [ai-engineering-command-desk-v0.1.0](releases/ai-engineering-command-desk-v0.1.0.md) | AI Engineering Command Desk | Published | 18 skill zips + manifest/checksum assets |
| [product-command-desk-v0.1.0](releases/product-command-desk-v0.1.0.md) | Product Command Desk | Published | 16 skill zips + release/source bundles |
| [sales-command-desk-v0.1.0](releases/sales-command-desk-v0.1.0.md) | Sales Command Desk | Published | 13 skill zips + release/source bundles |
| [sdlc-command-desk-v0.2.0](releases/sdlc-command-desk-v0.2.0.md) | SDLC Command Desk | Published | 19 skill zips + checksum assets |

Verify packaged artifacts before publishing or installing:

```powershell
python tools/validate_release_assets.py
```

---
## From source

```bash
git clone https://github.com/MadewellRD/skills-lab.git
cd skills-lab
python3 tools/validate_sdlc_suite.py
python3 tools/validate_release_assets.py
```

---

## Community

Skills-Lab is built for builders who want AI agents to move faster without losing source truth, reviewability, or operational control.

Issues and pull requests should stay evidence-first: include repo state, affected files, validation commands, source facts, and known halt conditions.

See [MANIFEST.md](MANIFEST.md) for the full suite registry and [docs/INSTALL.md](docs/INSTALL.md) for setup instructions.

# AI Engineering Command Desk v0.1.0

Date: 2026-06-01

## Summary

Publishes the AI Engineering Command Desk packaged skill suite. The suite includes one orchestrator and specialist desks for model selection, prompt systems, tool schema design, agent architecture, RAG/retrieval design, eval design and analysis, dataset curation, synthetic data, fine-tuning, inference operations, observability, cost/latency optimization, release readiness, incident response, safety review, and red-team evaluation.

## Artifacts

- Source specs: `skills/AI Engineering Command Desk/`
- Packaged skill directories: `dist/skills/ai-engineering-command-desk/`
- Skill zip bundles: `dist/packages/ai-engineering-command-desk/`
- Manifest: `dist/manifests/ai-engineering-command-desk-manifest.json`
- Checksums: `dist/manifests/ai-engineering-command-desk-CHECKSUMS.txt`

## Validation

Release assets were validated with:

```powershell
python tools/validate_release_assets.py
```

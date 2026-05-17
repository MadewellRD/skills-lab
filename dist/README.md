# Dist Artifact Layout

`dist/` is the packaged and generated artifact layer.

Contract:

- `dist/skills/<suite-slug>/<skill-slug>/` contains generated or packaged ChatGPT-compatible skill directories.
- `dist/manifests/` is reserved for generated suite manifests/checksums.
- `dist/packages/` is reserved for generated local package archives.

Related repository layers:

- `skills/<Suite Name>/` contains human-authored suite source Markdown.
- `releases/` contains immutable versioned release artifacts.

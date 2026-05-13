---
schema_version: "1.0"
name: BadlyNamedSkill
description: Too short.
version: "not-semver"
desk: test-desk
role: leaf
capability_requirements:
  file_io: none
  script_execution: none
  tool_calling: required
  long_context: none
  multimodal: none
  workflow_packet: required
provenance:
  author: TestAuthor
  license: GPL-3.0
---

## Procedure

This file is intentionally malformed to exercise the validator error reporting.
It is missing required anchors, has an invalid name, version, and license, and
a workflow_packet/file_io capability inconsistency.

## Purpose

Out-of-order on purpose.

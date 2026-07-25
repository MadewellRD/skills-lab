#!/usr/bin/env python3
"""Render a canonical Implementation Handoff implementation prompt from a JSON spec.

This helper is intentionally small. It is useful when the request has enough
structured facts to render a branch/worktree PR handoff, but the canonical files
in references/canonical/ remain the source of truth for final wording.

Usage:
  render_handoff_prompt.py spec.json > prompt.txt

Expected JSON keys are optional unless noted by the caller:
  repo_path, job, grounding_mode, connector_status, github_repo, github_pr,
  github_issue, github_commit, linear_issue, docs_used, communication_sources,
  state_summary, worktree_command, sections, commits, guardrails,
  commit_message, pr_title, pr_base, pr_body, stop_line.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

VALID_MODES = {"connector-grounded", "mixed", "user-facts-only", "diagnostic"}


def as_lines(value: Any, fallback: str = "missing-required-value") -> list[str]:
    if value is None or value == "":
        return [fallback]
    if isinstance(value, list):
        return [str(item) for item in value]
    return str(value).splitlines() or [fallback]


def bullet_block(value: Any, fallback: str = "missing-required-value") -> str:
    return "\n".join(f"- {line}" for line in as_lines(value, fallback))


def render_sections(sections: Any) -> str:
    if not sections:
        return "What to build:\n\nmissing-required-value"
    out: list[str] = []
    if isinstance(sections, dict):
        iterable = sections.items()
    else:
        iterable = []
        for idx, item in enumerate(sections):
            if isinstance(item, dict):
                iterable.append((item.get("title", f"Section {idx + 1}"), item.get("body", "missing-required-value")))
            else:
                iterable.append((f"Section {idx + 1}", str(item)))
    for title, body in iterable:
        out.append(f"{title}:\n\n{body}")
    return "\n\n".join(out)


def render_commits(commits: Any) -> str:
    if not commits:
        return "Commit structure:\n\nmissing-required-value"
    out: list[str] = []
    for idx, commit in enumerate(commits, start=1):
        if isinstance(commit, dict):
            title = commit.get("title", "missing-required-value")
            body = commit.get("body", "missing-required-value")
        else:
            title = str(commit)
            body = "missing-required-value"
        out.append(f"Commit {idx} - {title}:\n  {body}")
    return "\n\n".join(out)


def connector_block(data: dict[str, Any]) -> str:
    mode = str(data.get("grounding_mode", "user-facts-only"))
    if mode not in VALID_MODES:
        mode = "user-facts-only"
    lines = [f"Grounding mode: {mode}"]
    for key, label in [
        ("connector_status", "Connector status"),
        ("github_repo", "GitHub repo"),
        ("github_pr", "GitHub PR"),
        ("github_issue", "GitHub issue"),
        ("github_commit", "GitHub commit"),
        ("linear_issue", "Linear issue"),
        ("docs_used", "Docs used"),
        ("communication_sources", "Communication sources"),
    ]:
        value = data.get(key)
        if value:
            if isinstance(value, list):
                lines.append(f"{label}: {', '.join(str(item) for item in value)}")
            else:
                lines.append(f"{label}: {value}")
    return "\n".join(f"- {line}" for line in lines)


def state_summary_block(data: dict[str, Any]) -> str:
    lines = [connector_block(data)]
    lines.extend(f"- {line}" for line in as_lines(data.get("state_summary")))
    return "\n".join(lines)


def val(data: dict[str, Any], key: str, default: str = "missing-required-value") -> str:
    value = data.get(key, default)
    if value is None or value == "":
        return default
    return str(value)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: render_handoff_prompt.py spec.json", file=sys.stderr)
        return 2

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    prompt = f"""You are operating on {val(data, 'repo_path')}. Job: {val(data, 'job')}.

State summary:
{state_summary_block(data)}

Setup:

{val(data, 'worktree_command')}

{render_sections(data.get('sections'))}

{render_commits(data.get('commits'))}

Per-PR guardrails:
{bullet_block(data.get('guardrails'))}

Commit message:

    {val(data, 'commit_message')}

PR title: "{val(data, 'pr_title')}"
PR base: {val(data, 'pr_base', 'main')}
PR body: {val(data, 'pr_body')}

Stop at "{val(data, 'stop_line', 'PR opened, CI running.')}" Do not merge.
"""
    print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

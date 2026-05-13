import { describe, it, expect } from 'vitest';
import {
  parseSkillContent,
  splitByAnchors,
  missingRequiredAnchors,
  unknownAnchors,
  anchorsOutOfOrder,
} from '../src/parser.js';
import { REQUIRED_ANCHORS } from '../src/types.js';

const MINIMAL_FRONTMATTER = `---
schema_version: "1.0"
name: example-skill
description: A minimal skill used for testing the parser path only.
version: "1.0.0"
desk: test-desk
role: leaf
capability_requirements:
  file_io: required
  script_execution: none
  tool_calling: required
  long_context: none
  multimodal: none
  workflow_packet: required
provenance:
  author: TestAuthor
  license: Apache-2.0
---

## Purpose

Test purpose body.

## Activation

Test activation body.

## Procedure

Test procedure body.

## Output Contract

Test output contract body.

## Halt Conditions

Test halt conditions body.

## Workflow Packet

Test workflow packet body.

## Composition

Test composition body.
`;

describe('parseSkillContent', () => {
  it('parses YAML frontmatter into a typed object', () => {
    const parsed = parseSkillContent(MINIMAL_FRONTMATTER, '/test/SKILL.md');
    expect(parsed.frontmatter.name).toBe('example-skill');
    expect(parsed.frontmatter.version).toBe('1.0.0');
    expect(parsed.frontmatter.role).toBe('leaf');
  });

  it('throws when frontmatter is missing entirely', () => {
    const content = '## Purpose\n\nNo frontmatter here.';
    expect(() => parseSkillContent(content, '/test/SKILL.md')).toThrow(
      /missing YAML frontmatter/i,
    );
  });

  it('captures the source path on the parsed result', () => {
    const parsed = parseSkillContent(MINIMAL_FRONTMATTER, '/some/path/SKILL.md');
    expect(parsed.source_path).toBe('/some/path/SKILL.md');
  });

  it('splits body into anchor-keyed sections', () => {
    const parsed = parseSkillContent(MINIMAL_FRONTMATTER, '/test/SKILL.md');
    for (const anchor of REQUIRED_ANCHORS) {
      expect(parsed.body_sections[anchor]).toBeDefined();
      expect(parsed.body_sections[anchor]).toMatch(/Test .* body\./);
    }
  });
});

describe('splitByAnchors', () => {
  it('returns empty object for a body with no H2 anchors', () => {
    const result = splitByAnchors('Just a paragraph with no headers.');
    expect(Object.keys(result)).toHaveLength(0);
  });

  it('captures content between consecutive anchors', () => {
    const body = '## First\n\nfirst content\n\n## Second\n\nsecond content';
    const result = splitByAnchors(body);
    expect(result['First']).toBe('first content');
    expect(result['Second']).toBe('second content');
  });

  it('captures content for the final anchor up to end of file', () => {
    const body = '## Only\n\nonly content';
    const result = splitByAnchors(body);
    expect(result['Only']).toBe('only content');
  });

  it('does not match H3 or deeper headers', () => {
    const body = '## Real\n\ncontent\n\n### Subsection\n\nsub content';
    const result = splitByAnchors(body);
    expect(result['Real']).toContain('content');
    expect(result['Real']).toContain('### Subsection');
    expect(result['Subsection']).toBeUndefined();
  });
});

describe('missingRequiredAnchors', () => {
  it('returns empty when all required anchors are present', () => {
    const parsed = parseSkillContent(MINIMAL_FRONTMATTER, '/test/SKILL.md');
    expect(missingRequiredAnchors(parsed)).toEqual([]);
  });

  it('reports each missing required anchor', () => {
    const incomplete = MINIMAL_FRONTMATTER.replace(/## Halt Conditions[\s\S]*?(?=## Workflow Packet)/, '');
    const parsed = parseSkillContent(incomplete, '/test/SKILL.md');
    expect(missingRequiredAnchors(parsed)).toContain('Halt Conditions');
  });
});

describe('unknownAnchors', () => {
  it('flags anchors that are neither required nor optional', () => {
    const withExtra = MINIMAL_FRONTMATTER + '\n## Surprise Section\n\nUnexpected content.\n';
    const parsed = parseSkillContent(withExtra, '/test/SKILL.md');
    expect(unknownAnchors(parsed)).toContain('Surprise Section');
  });

  it('does not flag the optional References anchor', () => {
    const withReferences = MINIMAL_FRONTMATTER + '\n## References\n\n- link\n';
    const parsed = parseSkillContent(withReferences, '/test/SKILL.md');
    expect(unknownAnchors(parsed)).not.toContain('References');
  });
});

describe('anchorsOutOfOrder', () => {
  it('returns null when required anchors are in canonical order', () => {
    const parsed = parseSkillContent(MINIMAL_FRONTMATTER, '/test/SKILL.md');
    expect(anchorsOutOfOrder(parsed)).toBeNull();
  });

  it('detects a swapped pair of required anchors', () => {
    // Swap Activation and Purpose: Activation comes before Purpose.
    const swapped = MINIMAL_FRONTMATTER.replace(
      /## Purpose\n\nTest purpose body\.\n\n## Activation\n\nTest activation body\./,
      '## Activation\n\nTest activation body.\n\n## Purpose\n\nTest purpose body.',
    );
    const parsed = parseSkillContent(swapped, '/test/SKILL.md');
    const result = anchorsOutOfOrder(parsed);
    expect(result).not.toBeNull();
    // First out-of-order required anchor encountered is 'Activation' (where 'Purpose' was expected).
    expect(result).toBe('Activation');
  });
});

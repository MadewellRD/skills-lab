/**
 * Skill-Lab SKILL.md Parser
 *
 * Reads a SKILL.md file from disk and produces a ParsedSkill object containing
 * the YAML frontmatter and the body broken into anchor-keyed sections.
 *
 * This parser is deliberately permissive about content within sections; the
 * validator enforces structural rules separately.
 */

import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import matter from 'gray-matter';
import {
  type ParsedSkill,
  type SkillFrontmatter,
  REQUIRED_ANCHORS,
  OPTIONAL_ANCHORS,
} from './types.js';

/**
 * Match an H2 anchor line: "## Anchor Name"
 * Captures the anchor name (without leading hashes/whitespace).
 */
const H2_ANCHOR_RE = /^##[ \t]+(.+?)[ \t]*$/;

/**
 * Match the opening or closing of a triple-backtick fence (with optional info string).
 */
const FENCE_RE = /^```/;

/**
 * Walk the body line-by-line and return the offset range of every H2 anchor
 * that appears outside fenced code blocks. Anchors inside ``` fences are
 * content, not document structure, and must be ignored.
 */
function findRealAnchors(body: string): Array<{ name: string; start: number; contentStart: number }> {
  const lines = body.split('\n');
  const matches: Array<{ name: string; start: number; contentStart: number }> = [];
  let inFence = false;
  let offset = 0;

  for (const line of lines) {
    const lineLength = line.length + 1; // +1 for the newline

    if (FENCE_RE.test(line)) {
      inFence = !inFence;
      offset += lineLength;
      continue;
    }

    if (!inFence) {
      const m = H2_ANCHOR_RE.exec(line);
      if (m) {
        matches.push({
          name: m[1]!,
          start: offset,
          contentStart: offset + m[0].length,
        });
      }
    }

    offset += lineLength;
  }

  return matches;
}

/**
 * Split a markdown body into a map of H2 anchor name to its content.
 *
 * Content under an anchor is everything between that H2 and the next H2 or
 * end of file. Anchors inside fenced code blocks are ignored. Leading and
 * trailing whitespace within a section is trimmed.
 */
export function splitByAnchors(body: string): Record<string, string> {
  const sections: Record<string, string> = {};
  const matches = findRealAnchors(body);

  for (let i = 0; i < matches.length; i++) {
    const current = matches[i]!;
    const next = matches[i + 1];
    const end = next ? next.start : body.length;
    const content = body.slice(current.contentStart, end).trim();
    sections[current.name] = content;
  }

  return sections;
}

/**
 * Parse a SKILL.md string into a ParsedSkill object.
 *
 * Throws if the file lacks YAML frontmatter or has malformed YAML. Structural
 * validation (anchor presence, frontmatter schema) is performed by the
 * validator, not the parser.
 */
export function parseSkillContent(content: string, sourcePath: string): ParsedSkill {
  const parsed = matter(content);

  if (!parsed.data || Object.keys(parsed.data).length === 0) {
    throw new Error(
      `SKILL.md at ${sourcePath} is missing YAML frontmatter. Every IR file must declare its frontmatter between '---' fences.`,
    );
  }

  // Cast: validator will enforce the schema; parser trusts gray-matter's YAML parse.
  const frontmatter = parsed.data as SkillFrontmatter;
  const rawBody = parsed.content.trim();
  const bodySections = splitByAnchors(rawBody);

  return {
    source_path: sourcePath,
    frontmatter,
    body_sections: bodySections,
    raw_body: rawBody,
  };
}

/**
 * Convenience: load a SKILL.md from disk and parse it.
 */
export async function parseSkillFile(path: string): Promise<ParsedSkill> {
  const absolutePath = resolve(path);
  const content = await readFile(absolutePath, 'utf8');
  return parseSkillContent(content, absolutePath);
}

/**
 * Check that all required anchors are present in a parsed skill's body.
 * Returns missing anchor names (empty array if complete).
 */
export function missingRequiredAnchors(parsed: ParsedSkill): string[] {
  return REQUIRED_ANCHORS.filter((anchor) => !(anchor in parsed.body_sections));
}

/**
 * Return any anchors in the body that are neither required nor optional.
 * These are warnings, not errors — Desks may define additional sections.
 */
export function unknownAnchors(parsed: ParsedSkill): string[] {
  const known = new Set<string>([...REQUIRED_ANCHORS, ...OPTIONAL_ANCHORS]);
  return Object.keys(parsed.body_sections).filter((anchor) => !known.has(anchor));
}

/**
 * Check that the anchors appear in the canonical order in the body. Returns
 * the first out-of-order anchor's name, or null if all required anchors are
 * in order. Code-fence-aware: anchors inside ``` blocks are ignored.
 */
export function anchorsOutOfOrder(parsed: ParsedSkill): string | null {
  const foundOrder = findRealAnchors(parsed.raw_body).map((m) => m.name);
  const required = REQUIRED_ANCHORS;
  // Filter foundOrder to just required anchors (ignoring optionals and extras).
  const foundRequired = foundOrder.filter((a) => (required as readonly string[]).includes(a));
  for (let i = 0; i < foundRequired.length; i++) {
    if (foundRequired[i] !== required[i]) {
      return foundRequired[i] ?? null;
    }
  }
  return null;
}

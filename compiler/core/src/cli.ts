#!/usr/bin/env node
/**
 * Skill-Lab Compiler Core CLI
 *
 * Validates a single SKILL.md file. Used for manual verification and as a
 * scriptable check from CI.
 *
 *   tsx src/cli.ts <path-to-SKILL.md>
 *
 * Exit codes:
 *   0 — validation passed
 *   1 — validation failed (errors printed to stderr)
 *   2 — invocation error (bad arguments, file not found)
 */

import { parseSkillFile } from './parser.js';
import { validateSkill, collectWarnings } from './validator.js';

async function main(): Promise<number> {
  const path = process.argv[2];
  if (!path) {
    console.error('Usage: tsx src/cli.ts <path-to-SKILL.md>');
    return 2;
  }

  let parsed;
  try {
    parsed = await parseSkillFile(path);
  } catch (err) {
    console.error(`Parse error: ${(err as Error).message}`);
    return 2;
  }

  const warnings = collectWarnings(parsed);
  for (const w of warnings) console.warn(`WARN: ${w}`);

  const result = await validateSkill(parsed);
  if (result.ok) {
    console.log(`OK ${parsed.frontmatter.name}@${parsed.frontmatter.version}`);
    return 0;
  }

  console.error(`FAIL ${path}`);
  for (const err of result.errors) {
    console.error(`  [${err.scope}] ${err.path} — ${err.message}`);
  }
  return 1;
}

main().then((code) => process.exit(code));

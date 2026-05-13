/**
 * @skill-lab/compiler-core
 *
 * Public entry point. Re-exports the parser, validator, and IR types.
 *
 * Usage:
 *
 *   import { parseSkillFile, validateSkill } from '@skill-lab/compiler-core';
 *
 *   const parsed = await parseSkillFile('./desks/sdlc/skills/verification-desk/SKILL.md');
 *   const result = await validateSkill(parsed);
 *   if (!result.ok) {
 *     for (const err of result.errors) console.error(err);
 *   }
 */

export * from './types.js';
export {
  parseSkillContent,
  parseSkillFile,
  splitByAnchors,
  missingRequiredAnchors,
  unknownAnchors,
  anchorsOutOfOrder,
} from './parser.js';
export {
  validateSkill,
  validateFrontmatter,
  validateBodyStructure,
  validateSemantics,
  collectWarnings,
  isValidSemver,
  isValidSemverRange,
} from './validator.js';

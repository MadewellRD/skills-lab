/**
 * Skill-Lab IR Validator
 *
 * Runs three layers of validation:
 *
 *   1. Schema validation of the frontmatter against skill.schema.json
 *   2. Structural validation of the body (anchor presence and order)
 *   3. Semantic validation (semver range syntax, capability consistency)
 *
 * Cross-reference validation (composes_from / hands_off_to resolvability)
 * requires registry context and is handled by a separate pass in the
 * compiler core's graph resolver — not here.
 */

import { readFile } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import Ajv, { type ValidateFunction } from 'ajv';
import addFormats from 'ajv-formats';
import semver from 'semver';
import {
  type ParsedSkill,
  type ValidationError,
  type ValidationResult,
  type CapabilityRequirements,
} from './types.js';
import {
  anchorsOutOfOrder,
  missingRequiredAnchors,
  unknownAnchors,
} from './parser.js';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Repo root is three levels up from compiler/core/src/.
const REPO_ROOT = resolve(__dirname, '../../..');
const SCHEMA_DIR = resolve(REPO_ROOT, 'ir-schema/v1.0');

let cachedSkillValidator: ValidateFunction | null = null;

/**
 * Lazily compile and cache the Ajv validator for skill.schema.json. The Ajv
 * instance is configured strict (no unknown keywords) with format checking.
 */
async function getSkillValidator(): Promise<ValidateFunction> {
  if (cachedSkillValidator) return cachedSkillValidator;

  const schemaPath = resolve(SCHEMA_DIR, 'skill.schema.json');
  const schemaJson = await readFile(schemaPath, 'utf8');
  const schema = JSON.parse(schemaJson);

  // Ajv v8: the default export is the class constructor.
  // CJS interop quirk — the class lives on .default when imported from ESM.
  const AjvCtor = (Ajv as unknown as { default?: typeof Ajv }).default ?? Ajv;
  const ajv = new AjvCtor({
    strict: true,
    allErrors: true,
    verbose: true,
  });
  const addFormatsFn =
    (addFormats as unknown as { default?: typeof addFormats }).default ?? addFormats;
  addFormatsFn(ajv);

  cachedSkillValidator = ajv.compile(schema);
  return cachedSkillValidator;
}

/**
 * Validate the frontmatter of a parsed skill against skill.schema.json.
 */
export async function validateFrontmatter(
  parsed: ParsedSkill,
): Promise<ValidationError[]> {
  const validator = await getSkillValidator();
  const valid = validator(parsed.frontmatter);
  if (valid) return [];

  return (validator.errors ?? []).map((err) => ({
    scope: 'schema' as const,
    path: err.instancePath || '/',
    message: `${err.keyword}: ${err.message ?? 'schema violation'}`,
    value: err.data,
  }));
}

/**
 * Validate that all required body anchors are present and in order.
 */
export function validateBodyStructure(parsed: ParsedSkill): ValidationError[] {
  const errors: ValidationError[] = [];

  const missing = missingRequiredAnchors(parsed);
  for (const anchor of missing) {
    errors.push({
      scope: 'body',
      path: `## ${anchor}`,
      message: `Required anchor '## ${anchor}' is missing from the SKILL.md body.`,
    });
  }

  const outOfOrder = anchorsOutOfOrder(parsed);
  if (outOfOrder) {
    errors.push({
      scope: 'body',
      path: `## ${outOfOrder}`,
      message: `Required anchor '## ${outOfOrder}' appears out of canonical order. See REQUIRED_ANCHORS in types.ts.`,
    });
  }

  // Unknown anchors are warnings, not errors. We surface them through a
  // separate channel (see validateSkill below) rather than as errors.

  return errors;
}

/**
 * Validate semver string. Returns true if `version` is a valid semver, false otherwise.
 *
 * The underlying `semver.valid` accepts 'v1.0.0' and silently strips the prefix,
 * which is looser than the SemVer 2.0 spec and looser than our skill.schema.json
 * regex. We reject the prefix explicitly so this helper agrees with the schema.
 */
export function isValidSemver(version: string): boolean {
  if (/^[vV]/.test(version)) return false;
  return semver.valid(version) !== null;
}

/**
 * Validate semver range (used by composes_from / hands_off_to version fields).
 */
export function isValidSemverRange(range: string): boolean {
  if (range === '*') return true;
  return semver.validRange(range) !== null;
}

/**
 * Validate semver fields and semantic invariants that aren't expressible in
 * the JSON Schema alone (e.g., capability consistency, semver ranges in
 * composition references).
 */
export function validateSemantics(parsed: ParsedSkill): ValidationError[] {
  const errors: ValidationError[] = [];
  const fm = parsed.frontmatter;

  // Skill version must be valid semver.
  if (fm.version && !isValidSemver(fm.version)) {
    errors.push({
      scope: 'semver',
      path: '/version',
      message: `Skill version '${fm.version}' is not a valid semver string.`,
      value: fm.version,
    });
  }

  // composes_from and hands_off_to versions must be valid semver ranges.
  for (const [field, refs] of [
    ['composes_from', fm.composes_from],
    ['hands_off_to', fm.hands_off_to],
  ] as const) {
    if (!refs) continue;
    for (let i = 0; i < refs.length; i++) {
      const ref = refs[i]!;
      const v = ref.version ?? '*';
      if (!isValidSemverRange(v)) {
        errors.push({
          scope: 'semver',
          path: `/${field}/${i}/version`,
          message: `Version range '${v}' for '${ref.ref}' is not a valid semver range.`,
          value: v,
        });
      }
    }
  }

  // Capability consistency: workflow_packet=required implies file_io is not 'none'.
  const caps: CapabilityRequirements = fm.capability_requirements;
  if (caps && caps.workflow_packet === 'required' && caps.file_io === 'none') {
    errors.push({
      scope: 'frontmatter',
      path: '/capability_requirements',
      message:
        "workflow_packet: required is inconsistent with file_io: none. Workflow packets require file I/O for durable state.",
    });
  }

  // Orchestrator role must have at least one composition link.
  if (
    fm.role === 'orchestrator' &&
    (!fm.composes_from || fm.composes_from.length === 0) &&
    (!fm.hands_off_to || fm.hands_off_to.length === 0)
  ) {
    errors.push({
      scope: 'frontmatter',
      path: '/role',
      message:
        "Skills with role 'orchestrator' must reference at least one leaf via composes_from or hands_off_to.",
    });
  }

  return errors;
}

/**
 * Run the full validation pipeline on a parsed skill.
 *
 * Returns ValidationResult; on failure, errors is non-empty and lists every
 * problem detected across schema, body, and semantic layers.
 */
export async function validateSkill(parsed: ParsedSkill): Promise<ValidationResult> {
  const errors: ValidationError[] = [];

  errors.push(...(await validateFrontmatter(parsed)));
  errors.push(...validateBodyStructure(parsed));
  errors.push(...validateSemantics(parsed));

  if (errors.length === 0) return { ok: true };
  return { ok: false, errors };
}

/**
 * Helper for callers that want to surface non-fatal warnings (unknown anchors).
 */
export function collectWarnings(parsed: ParsedSkill): string[] {
  const warnings: string[] = [];
  for (const anchor of unknownAnchors(parsed)) {
    warnings.push(
      `Unknown anchor '## ${anchor}' in body — neither required nor optional. Allowed but may be removed by some target adapters.`,
    );
  }
  return warnings;
}

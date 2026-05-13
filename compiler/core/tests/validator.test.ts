import { describe, it, expect } from 'vitest';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { dirname } from 'node:path';
import {
  validateSkill,
  validateFrontmatter,
  validateBodyStructure,
  validateSemantics,
  isValidSemver,
  isValidSemverRange,
} from '../src/validator.js';
import { parseSkillContent, parseSkillFile } from '../src/parser.js';
import type { ParsedSkill, SkillFrontmatter } from '../src/types.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../..');

function buildFrontmatter(overrides: Partial<SkillFrontmatter> = {}): SkillFrontmatter {
  return {
    schema_version: '1.0',
    name: 'example-skill',
    description: 'A minimal skill used for validator tests, exceeding twenty characters easily.',
    version: '1.0.0',
    desk: 'test-desk',
    role: 'leaf',
    capability_requirements: {
      file_io: 'required',
      script_execution: 'none',
      tool_calling: 'required',
      long_context: 'none',
      multimodal: 'none',
      workflow_packet: 'required',
    },
    provenance: {
      author: 'TestAuthor',
      license: 'Apache-2.0',
    },
    ...overrides,
  };
}

function buildParsedSkill(overrides: Partial<SkillFrontmatter> = {}): ParsedSkill {
  return {
    source_path: '/test/SKILL.md',
    frontmatter: buildFrontmatter(overrides),
    body_sections: {
      Purpose: 'p',
      Activation: 'a',
      Procedure: 'pr',
      'Output Contract': 'oc',
      'Halt Conditions': 'hc',
      'Workflow Packet': 'wp',
      Composition: 'c',
    },
    raw_body:
      '## Purpose\n\np\n\n## Activation\n\na\n\n## Procedure\n\npr\n\n## Output Contract\n\noc\n\n## Halt Conditions\n\nhc\n\n## Workflow Packet\n\nwp\n\n## Composition\n\nc',
  };
}

describe('semver helpers', () => {
  it('accepts valid semver versions', () => {
    expect(isValidSemver('1.0.0')).toBe(true);
    expect(isValidSemver('0.1.0-alpha.1')).toBe(true);
    expect(isValidSemver('2.3.4+build.5')).toBe(true);
  });

  it('rejects invalid semver versions', () => {
    expect(isValidSemver('1.0')).toBe(false);
    expect(isValidSemver('v1.0.0')).toBe(false);
    expect(isValidSemver('latest')).toBe(false);
  });

  it('accepts valid semver ranges', () => {
    expect(isValidSemverRange('^1.0.0')).toBe(true);
    expect(isValidSemverRange('>=1.2.0 <2.0.0')).toBe(true);
    expect(isValidSemverRange('*')).toBe(true);
    expect(isValidSemverRange('~1.2.3')).toBe(true);
  });

  it('rejects invalid semver ranges', () => {
    expect(isValidSemverRange('latest')).toBe(false);
    expect(isValidSemverRange('not-a-range')).toBe(false);
  });
});

describe('validateFrontmatter', () => {
  it('passes a fully-populated valid frontmatter', async () => {
    const errors = await validateFrontmatter(buildParsedSkill());
    expect(errors).toEqual([]);
  });

  it('rejects an unknown schema_version', async () => {
    const skill = buildParsedSkill();
    (skill.frontmatter as unknown as { schema_version: string }).schema_version = '2.0';
    const errors = await validateFrontmatter(skill);
    expect(errors.length).toBeGreaterThan(0);
  });

  it('rejects a name in PascalCase', async () => {
    const skill = buildParsedSkill({ name: 'PascalCaseName' });
    const errors = await validateFrontmatter(skill);
    expect(errors.some((e) => e.path.includes('name'))).toBe(true);
  });

  it('rejects an unknown role value', async () => {
    const skill = buildParsedSkill();
    (skill.frontmatter as unknown as { role: string }).role = 'mystery';
    const errors = await validateFrontmatter(skill);
    expect(errors.some((e) => e.path.includes('role'))).toBe(true);
  });

  it('rejects an unknown license', async () => {
    const skill = buildParsedSkill();
    (skill.frontmatter as unknown as { provenance: { license: string; author: string } }).provenance = {
      author: 'X',
      license: 'GPL-3.0',
    };
    const errors = await validateFrontmatter(skill);
    expect(errors.some((e) => e.path.includes('license'))).toBe(true);
  });

  it('rejects a missing required field (provenance)', async () => {
    const skill = buildParsedSkill();
    delete (skill.frontmatter as unknown as { provenance?: unknown }).provenance;
    const errors = await validateFrontmatter(skill);
    expect(errors.length).toBeGreaterThan(0);
  });

  it('rejects a missing required capability_requirements key', async () => {
    const skill = buildParsedSkill();
    delete (skill.frontmatter.capability_requirements as unknown as { workflow_packet?: unknown })
      .workflow_packet;
    const errors = await validateFrontmatter(skill);
    expect(errors.some((e) => e.path.includes('capability_requirements'))).toBe(true);
  });
});

describe('validateBodyStructure', () => {
  it('passes when all required anchors are present and in order', () => {
    const errors = validateBodyStructure(buildParsedSkill());
    expect(errors).toEqual([]);
  });

  it('reports a missing required anchor', () => {
    const skill = buildParsedSkill();
    delete skill.body_sections['Halt Conditions'];
    skill.raw_body = skill.raw_body.replace(/## Halt Conditions[\s\S]*?(?=## Workflow Packet)/, '');
    const errors = validateBodyStructure(skill);
    expect(errors.some((e) => e.path.includes('Halt Conditions'))).toBe(true);
  });
});

describe('validateSemantics', () => {
  it('rejects an invalid semver version string', () => {
    const skill = buildParsedSkill({ version: '1.0' });
    const errors = validateSemantics(skill);
    expect(errors.some((e) => e.scope === 'semver' && e.path === '/version')).toBe(true);
  });

  it('rejects an invalid semver range in composes_from', () => {
    const skill = buildParsedSkill({
      composes_from: [{ ref: 'other-skill', version: 'latest' }],
    });
    const errors = validateSemantics(skill);
    expect(errors.some((e) => e.scope === 'semver' && e.path.includes('composes_from'))).toBe(true);
  });

  it('rejects workflow_packet=required combined with file_io=none', () => {
    const skill = buildParsedSkill({
      capability_requirements: {
        file_io: 'none',
        script_execution: 'none',
        tool_calling: 'required',
        long_context: 'none',
        multimodal: 'none',
        workflow_packet: 'required',
      },
    });
    const errors = validateSemantics(skill);
    expect(
      errors.some((e) => e.scope === 'frontmatter' && e.path.includes('capability_requirements')),
    ).toBe(true);
  });

  it('rejects orchestrator role with no composition links', () => {
    const skill = buildParsedSkill({ role: 'orchestrator' });
    const errors = validateSemantics(skill);
    expect(errors.some((e) => e.path === '/role')).toBe(true);
  });

  it('accepts orchestrator role when composes_from is populated', () => {
    const skill = buildParsedSkill({
      role: 'orchestrator',
      composes_from: [{ ref: 'leaf-one', version: '^1.0.0' }],
    });
    const errors = validateSemantics(skill);
    expect(errors.filter((e) => e.path === '/role')).toEqual([]);
  });
});

describe('validateSkill end-to-end', () => {
  it('returns ok for a fully-valid parsed skill', async () => {
    const result = await validateSkill(buildParsedSkill());
    expect(result.ok).toBe(true);
  });

  it('returns errors for a multi-fault skill', async () => {
    const skill = buildParsedSkill({ version: '1.0', name: 'BadName' });
    const result = await validateSkill(skill);
    expect(result.ok).toBe(false);
    if (!result.ok) {
      expect(result.errors.length).toBeGreaterThanOrEqual(2);
    }
  });
});

describe('round-trip: verification-desk', () => {
  it('parses and validates the converted verification-desk SKILL.md', async () => {
    const skillPath = resolve(
      REPO_ROOT,
      'desks/sdlc-command-desk/skills/verification-desk/SKILL.md',
    );
    const parsed = await parseSkillFile(skillPath);
    const result = await validateSkill(parsed);
    if (!result.ok) {
      console.error('verification-desk validation errors:', result.errors);
    }
    expect(result.ok).toBe(true);
  });

  it('verification-desk carries all required body anchors', async () => {
    const skillPath = resolve(
      REPO_ROOT,
      'desks/sdlc-command-desk/skills/verification-desk/SKILL.md',
    );
    const parsed = await parseSkillFile(skillPath);
    expect(parsed.body_sections['Purpose']).toBeDefined();
    expect(parsed.body_sections['Activation']).toBeDefined();
    expect(parsed.body_sections['Procedure']).toBeDefined();
    expect(parsed.body_sections['Output Contract']).toBeDefined();
    expect(parsed.body_sections['Halt Conditions']).toBeDefined();
    expect(parsed.body_sections['Workflow Packet']).toBeDefined();
    expect(parsed.body_sections['Composition']).toBeDefined();
  });

  it('verification-desk declares semver-versioned composition references', async () => {
    const skillPath = resolve(
      REPO_ROOT,
      'desks/sdlc-command-desk/skills/verification-desk/SKILL.md',
    );
    const parsed = await parseSkillFile(skillPath);
    const composes = parsed.frontmatter.composes_from ?? [];
    expect(composes.length).toBeGreaterThan(0);
    for (const ref of composes) {
      expect(ref.version).toMatch(/^[\^~>=<*\d]/);
    }
  });
});

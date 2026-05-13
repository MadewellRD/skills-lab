import { describe, it, expect } from 'vitest';
import { splitByAnchors } from '../src/parser.js';

describe('splitByAnchors — code-fence awareness', () => {
  it('ignores H2-shaped lines inside fenced code blocks', () => {
    const body = [
      '## Real Anchor',
      '',
      'Real content.',
      '',
      '```markdown',
      '## Not An Anchor',
      'Just template content.',
      '```',
      '',
      '## Next Real Anchor',
      '',
      'More real content.',
    ].join('\n');

    const sections = splitByAnchors(body);
    expect(Object.keys(sections).sort()).toEqual(['Next Real Anchor', 'Real Anchor']);
    expect(sections['Real Anchor']).toContain('## Not An Anchor');
  });

  it('handles multiple fenced blocks correctly', () => {
    const body = [
      '## First',
      '```',
      '## Inside One',
      '```',
      'between',
      '```typescript',
      '## Inside Two',
      '```',
      '## Second',
      'second content',
    ].join('\n');

    const sections = splitByAnchors(body);
    expect(Object.keys(sections).sort()).toEqual(['First', 'Second']);
  });

  it('treats unclosed fences as fenced to end of body (conservative)', () => {
    const body = [
      '## Real',
      'real content',
      '```',
      '## Looks Like Anchor',
      'but never closed',
    ].join('\n');

    const sections = splitByAnchors(body);
    expect(Object.keys(sections)).toEqual(['Real']);
  });
});

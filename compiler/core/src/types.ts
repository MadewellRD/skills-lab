/**
 * Skill-Lab IR Type Definitions
 *
 * TypeScript types that mirror the JSON schemas in ir-schema/v1.0/.
 * The schemas remain the source of truth for validation; these types
 * give the compiler core and target adapters typed access to parsed IR.
 */

export type SchemaVersion = '1.0';

export type CapabilityLevel = 'required' | 'preferred' | 'none';

export type ConnectorName =
  | 'filesystem'
  | 'github'
  | 'gitlab'
  | 'drive'
  | 'gmail'
  | 'slack'
  | 'linear'
  | 'jira'
  | 'notion'
  | 'calendar'
  | 'web';

export type SkillRole = 'router' | 'orchestrator' | 'leaf';

export type Target =
  | 'claude'
  | 'openai-custom-gpt'
  | 'openai-apps-sdk'
  | 'gemini-gem'
  | 'copilot-extension'
  | 'anthropic-agent-sdk'
  | 'langchain'
  | 'autogen';

export type License =
  | 'Apache-2.0'
  | 'MIT'
  | 'BSD-3-Clause'
  | 'CC-BY-4.0'
  | 'Proprietary';

export interface IODescriptor {
  id: string;
  type:
    | 'document'
    | 'markdown'
    | 'json'
    | 'yaml'
    | 'github_pr'
    | 'github_issue'
    | 'github_repo'
    | 'ci_artifact'
    | 'code_diff'
    | 'user_text'
    | 'uploaded_file'
    | 'workflow_packet';
  required?: boolean;
  description?: string;
}

export interface OutputDescriptor {
  id: string;
  type: 'markdown' | 'json' | 'yaml' | 'diagnostic';
  filename: string;
  description?: string;
}

export interface SkillReference {
  ref: string;
  version?: string;
  reason?: string;
}

export interface CapabilityRequirements {
  file_io: CapabilityLevel;
  script_execution: CapabilityLevel;
  tool_calling: CapabilityLevel;
  long_context: CapabilityLevel;
  multimodal: CapabilityLevel;
  workflow_packet: CapabilityLevel;
}

export interface Provenance {
  author: string;
  sources?: string[];
  license: License;
}

export interface LifecycleStage {
  number: number;
  name: string;
}

export interface SkillFrontmatter {
  schema_version: SchemaVersion;
  name: string;
  description: string;
  version: string;
  desk: string;
  lifecycle_stage?: LifecycleStage;
  role: SkillRole;
  inputs?: IODescriptor[];
  outputs?: OutputDescriptor[];
  connectors_required?: ConnectorName[];
  connectors_optional?: ConnectorName[];
  composes_from?: SkillReference[];
  hands_off_to?: SkillReference[];
  capability_requirements: CapabilityRequirements;
  activation_hints?: string[];
  provenance: Provenance;
  policy_ref?: string;
}

/**
 * Mandatory body anchors that must appear in every SKILL.md body, in this order.
 * The parser extracts the content under each anchor; the validator ensures all
 * required anchors are present.
 */
export const REQUIRED_ANCHORS = [
  'Purpose',
  'Activation',
  'Procedure',
  'Output Contract',
  'Halt Conditions',
  'Workflow Packet',
  'Composition',
] as const;

export type RequiredAnchor = (typeof REQUIRED_ANCHORS)[number];

export const OPTIONAL_ANCHORS = ['References'] as const;
export type OptionalAnchor = (typeof OPTIONAL_ANCHORS)[number];

export type AnchorName = RequiredAnchor | OptionalAnchor;

/**
 * A parsed SKILL.md file, ready for validation and downstream compilation.
 */
export interface ParsedSkill {
  /** Path the skill was loaded from. */
  source_path: string;
  /** Validated frontmatter object. */
  frontmatter: SkillFrontmatter;
  /** Map of anchor name to body content under that anchor. */
  body_sections: Record<string, string>;
  /** Raw markdown body (everything after the frontmatter fence). */
  raw_body: string;
}

/**
 * Desk-level manifest parsed from desks/<desk>/desk.yaml.
 */
export interface DeskManifest {
  schema_version: SchemaVersion;
  name: string;
  display_name: string;
  description: string;
  version: string;
  namespace?: string;
  capability_tags: string[];
  orchestrator: string;
  leaves: string[];
  workflow_packet_schema?: string;
  policy?: string;
  depends_on?: Array<{
    ref: string;
    version?: string;
    reason?: string;
  }>;
  supported_targets?: Target[];
}

/**
 * Policy definition parsed from policy.yaml. Consumed by ROGUE:OPS-compatible
 * runtimes for governance enforcement.
 */
export interface Policy {
  schema_version: SchemaVersion;
  execution_boundaries: {
    filesystem?: {
      allowed_paths?: string[];
      denied_paths?: string[];
      require_approval_for_writes?: boolean;
    };
    network?: {
      allowed_domains?: string[];
      denied_domains?: string[];
      require_approval?: string[];
    };
    connectors?: {
      require_approval_for_writes?: string[];
      audit_all?: boolean;
      denied?: string[];
    };
  };
  halt_on?: Array<
    | 'missing_required_connector'
    | 'policy_violation'
    | 'schema_validation_failure'
    | 'audit_write_failure'
    | { condition: 'confidence_below_threshold'; threshold: number }
  >;
  audit?: {
    log_all_invocations?: boolean;
    retain_workflow_packets?: boolean;
    retention_days?: number;
    audit_sink?: 'local' | 'rogue-ops' | 'both';
  };
}

/**
 * Result of a validation pass — successful, or carrying structured errors.
 */
export type ValidationResult =
  | { ok: true }
  | { ok: false; errors: ValidationError[] };

export interface ValidationError {
  /** Where the error was detected — 'frontmatter', 'body', or 'cross-reference'. */
  scope: 'frontmatter' | 'body' | 'cross-reference' | 'schema' | 'semver';
  /** JSON pointer or anchor path. */
  path: string;
  /** Human-readable message. */
  message: string;
  /** The offending value, if any. */
  value?: unknown;
}

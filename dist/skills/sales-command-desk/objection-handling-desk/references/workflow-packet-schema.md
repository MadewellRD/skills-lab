# Sales Workflow Packet Schema

Use this packet shape across all Sales Revenue Command Desk skills.

```yaml
sales_workflow_id: string | null
workflow_mode: research | draft | validate | update | forecast | handoff | orchestrate
requested_outcome: string
account:
  name: string | null
  domain: string | null
  crm_id: string | null
contacts:
  - name: string | null
    title: string | null
    email: string | null
    crm_id: string | null
opportunity:
  name: string | null
  crm_id: string | null
  stage: string | null
  amount: string | null
  close_date: string | null
  owner: string | null
source_facts:
  - fact: string
    source: string
    confidence: high | medium | low
assumptions:
  - assumption: string
    reason: string
open_questions:
  - question: string
    blocks_progress: true | false
approval_state:
  required: true | false
  reason: string | null
  approver: string | null
completed_stages: []
skipped_stages: []
next_recommended_stage: string | null
artifacts:
  - name: string
    path_or_description: string
```

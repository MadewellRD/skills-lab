#!/usr/bin/env python3
import json
import sys

ORDER = [
    "site-product-requirements-desk",
    "information-architecture-desk",
    "ux-ui-design-system-desk",
    "backend-integration-desk",
    "frontend-engineering-desk",
    "web-security-secops-desk",
    "accessibility-seo-desk",
    "web-performance-desk",
    "web-testing-qa-desk",
    "web-release-deployment-desk",
    "web-observability-desk",
    "web-maintenance-growth-desk",
]

def sequence(start=None, target=None):
    start = start or ORDER[0]
    target = target or ORDER[-1]
    if start not in ORDER or target not in ORDER:
        raise SystemExit("unknown stage")
    s = ORDER.index(start)
    t = ORDER.index(target)
    if s <= t:
        return ORDER[s:t+1]
    return ORDER[s:] + ORDER[:t+1]

if __name__ == "__main__":
    start = sys.argv[1] if len(sys.argv) > 1 else None
    target = sys.argv[2] if len(sys.argv) > 2 else None
    stages = sequence(start, target)
    print(json.dumps({"stages": stages, "current_stage": stages[0], "target_stage": stages[-1]}, indent=2))

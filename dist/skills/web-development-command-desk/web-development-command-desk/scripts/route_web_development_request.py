#!/usr/bin/env python3
import sys

ROUTES = [
    (("sitemap", "navigation", "url", "route", "taxonomy"), "information-architecture-desk"),
    (("design system", "component", "responsive", "token", "figma", "ui"), "ux-ui-design-system-desk"),
    (("frontend", "react", "next", "vue", "svelte", "rendering", "state"), "frontend-engineering-desk"),
    (("api", "auth", "session", "backend", "integration", "bff"), "backend-integration-desk"),
    (("cms", "content", "editorial", "localization", "publishing"), "cms-content-operations-desk"),
    (("security", "secops", "csp", "headers", "cookie", "secrets"), "web-security-secops-desk"),
    (("performance", "core web vitals", "lcp", "inp", "cls", "bundle", "cache"), "web-performance-desk"),
    (("accessibility", "wcag", "seo", "metadata", "structured data", "crawl"), "accessibility-seo-desk"),
    (("test", "qa", "browser", "device", "visual regression", "smoke"), "web-testing-qa-desk"),
    (("observability", "rum", "synthetic", "dashboard", "alert", "incident"), "web-observability-desk"),
    (("deploy", "release", "rollback", "cdn", "preview", "ci/cd"), "web-release-deployment-desk"),
    (("growth", "experiment", "analytics", "maintenance", "migration", "refresh"), "web-maintenance-growth-desk"),
]

text = " ".join(sys.argv[1:]).lower()
for keys, desk in ROUTES:
    if any(k in text for k in keys):
        print(desk)
        raise SystemExit(0)
print("site-product-requirements-desk")

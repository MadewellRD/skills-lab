#!/usr/bin/env python3
import argparse
from pathlib import Path
import zipfile
import hashlib

ORDER = [
"sdlc-command-desk","product-requirements-desk","technical-discovery-desk","architecture-design-desk","issue-planning-desk","implementation-handoff-desk","review-quality-desk","test-strategy-desk","verification-desk","docs-traceability-desk","security-threat-desk","ci-failure-desk","release-operations-desk","deployment-desk","observability-readiness-desk","incident-response-desk","maintenance-refactor-desk","retrospective-desk","decommissioning-desk"
]

ap = argparse.ArgumentParser()
ap.add_argument("--skills-dir", required=True)
ap.add_argument("--dist-dir", required=True)
args = ap.parse_args()

skills = Path(args.skills_dir)
dist = Path(args.dist_dir)
dist.mkdir(parents=True, exist_ok=True)

rows=[]
for i,name in enumerate(ORDER):
    src = skills / name
    zname = f"{i:03d}-{name}-skill.zip"
    zpath = dist / zname
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in src.rglob("*"):
            if p.is_file():
                zf.write(p, arcname=str(Path(name) / p.relative_to(src)))
    if zpath.stat().st_size > 25*1024*1024:
        raise SystemExit(f"archive too large: {zname}")
    rows.append((zname, zpath.stat().st_size))

chk = dist / "CHECKSUMS.txt"
with chk.open("w", encoding="utf-8") as f:
    for zname,_ in rows:
        data = (dist / zname).read_bytes()
        h = hashlib.sha256(data).hexdigest()
        f.write(f"{h}  {zname}\n")

print("PACKAGED")
for z,s in rows:
    print(f"{z}\t{s}")

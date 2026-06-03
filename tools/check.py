#!/usr/bin/env python3
"""Repository health checks (used by CI alongside `build.py --check`)."""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULLWIDTH = re.compile(r"[０-９Ａ-Ｚａ-ｚ]")
REQUIRED_SPEC_KEYS = {"title", "direction", "meta", "source", "fields"}

errors = []


def rel(p):
    return os.path.relpath(p, ROOT)


def check_specs():
    for p in glob.glob(os.path.join(ROOT, "spec", "*.json")):
        try:
            spec = json.load(open(p, encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{rel(p)}: invalid JSON ({e})")
            continue
        missing = REQUIRED_SPEC_KEYS - spec.keys()
        if missing:
            errors.append(f"{rel(p)}: missing keys {sorted(missing)}")
        if spec.get("direction") not in ("import", "output"):
            errors.append(f"{rel(p)}: direction must be import/output")
        for i, f in enumerate(spec.get("fields", []), 1):
            for k in ("name", "length", "type"):
                if k not in f:
                    errors.append(f"{rel(p)}: field #{i} missing '{k}'")


def check_fullwidth():
    for p in glob.glob(os.path.join(ROOT, "docs", "*.md")) + [os.path.join(ROOT, "README.md")]:
        for n, line in enumerate(open(p, encoding="utf-8"), 1):
            if FULLWIDTH.search(line):
                errors.append(f"{rel(p)}:{n}: full-width alphanumeric found: {line.strip()[:40]}")


def main():
    check_specs()
    check_fullwidth()
    if errors:
        print("Health check FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("repo health checks passed ✓")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the documented standard without network access or third-party dependencies."""
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
SVG = "{http://www.w3.org/2000/svg}"


def check(condition, message):
    if not condition:
        ERRORS.append(message)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def anchor(heading):
    return "".join(ch for ch in heading.lower() if ch in " -_" or
                   unicodedata.category(ch)[0] in {"L", "N"}).replace(" ", "-")


def check_link(link, origin):
    path, _, fragment = unquote(link).partition("#")
    target = ((ROOT / origin).parent / path).resolve() if path else ROOT / origin
    check(target.is_relative_to(ROOT), f"{origin}: link escapes repository: {link}")
    if not target.is_relative_to(ROOT):
        return
    check(target.exists(), f"{origin}: missing {link}")
    if fragment and target.is_file() and target.suffix == ".md":
        headings = re.findall(r"^#{1,6} (.+)$", target.read_text(encoding="utf-8"), re.M)
        check(fragment in {anchor(s) for s in headings}, f"{origin}: missing anchor {link}")


def check_markdown(paths):
    for path in paths:
        for link in re.findall(r"\]\(([^)\s]+)\)", read(path)):
            if not re.match(r"^[a-zA-Z][\w+.-]*:", link):
                check_link(link, path)


def main():
    registry = json.loads(read("maintenance/rules.json"))
    components = json.loads(read("component-catalog/manifest.json"))["components"]
    required = ("id", "status", "scope", "motif", "example", "counterexample",
                "verification", "evidence", "owner", "canonical")
    seen = set()
    check(registry.get("schema_version") == 1 and bool(registry.get("rules")), "Invalid registry")
    for rule in registry["rules"]:
        ident = rule.get("id", "")
        check(bool(re.fullmatch(r"RGL-\d{3,}", ident)) and ident not in seen, f"Rule ID: {ident}")
        seen.add(ident)
        for field in required:
            val = rule.get(field)
            check(isinstance(val, str) and bool(val.strip()), f"{ident}: missing {field}")
        check(rule.get("status") in {"proposed", "active", "deprecated", "retired"}, f"{ident}: status")
        if rule.get("status") in {"deprecated", "retired"}:
            for field in ("retirement_reason", "fallback"):
                check(bool(str(rule.get(field, "")).strip()), f"{ident}: missing {field}")
        if rule.get("canonical"):
            check_link("../" + rule["canonical"], "maintenance/rules.json")
    ids = [x["id"] for x in components]
    check(len(ids) == len(set(ids)) and all(f"N{i:02}" in ids for i in range(1, 29)),
          "Component IDs N01–N28 must exist and remain unique")
    slugs = [x["slug"] for x in components]
    check(len(slugs) == len(set(slugs)), "Duplicate component slugs")
    for comp in components:
        check_link("../" + comp["reference"], "component-catalog/manifest.json")
    cards = read("composition-library/visual-cards.md")
    assets = re.findall(r"\]\((assets/[^)]+\.svg)\)", cards)
    check(len(set(assets)) == len(assets) and len(assets) >= 10, "Missing or repeated composition illustrations")
    for relative in assets:
        target = ROOT / "composition-library" / relative
        try:
            svg = ET.parse(target).getroot()
            check(svg.tag == SVG + "svg" and bool(svg.get("viewBox")), f"{relative}: invalid SVG root")
            check(bool(svg.findtext(SVG + "title")) and bool(svg.findtext(SVG + "desc")),
                  f"{relative}: missing accessible title or description")
        except (OSError, ET.ParseError) as error:
            ERRORS.append(f"{relative}: {error}")
    check_markdown(["composition-library/visual-cards.md", "component-catalog/interaction-cards.md",
                    "composition-library/README.md", "mobile-first/README.md", "mobile-first/patterns.md", "maintenance/README.md",
                    "maintenance/review-template.md"])
    if ERRORS:
        print("\n".join(ERRORS), file=sys.stderr)
        return 1
    print(f"OK: {len(seen)} rules, {len(ids)} components, {len(assets)} illustrated compositions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

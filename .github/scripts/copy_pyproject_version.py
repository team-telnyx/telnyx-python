#!/usr/bin/env python3
# ruff: noqa: T201
"""Copy only ``[project].version`` between Telnyx Python pyproject files.

Release Please owns the release version, while the promoted ``next`` tree owns
all dependencies and build metadata. Overlaying the whole release-branch
``pyproject.toml`` silently reverts newly generated dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SECTION = re.compile(r"^\s*\[([^]]+)]\s*(?:#.*)?$")
VERSION = re.compile(
    r"^(?P<prefix>\s*version\s*=\s*)(?P<quote>['\"])(?P<value>[^'\"]+)(?P=quote)(?P<suffix>\s*(?:#.*)?)(?P<newline>\r?\n?)$"
)


class OverlayError(ValueError):
    pass


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise OverlayError(f"cannot read {path}: {exc}") from exc


def project_scalar(text: str, key: str, path: Path) -> str:
    assignment = re.compile(
        rf"^\s*{re.escape(key)}\s*=\s*(?P<quote>['\"])(?P<value>[^'\"]+)(?P=quote)\s*(?:#.*)?$"
    )
    in_project = False
    matches: list[str] = []
    for line in text.splitlines():
        section = SECTION.match(line)
        if section:
            in_project = section.group(1).strip() == "project"
            continue
        if in_project:
            match = assignment.match(line)
            if match:
                matches.append(match.group("value"))
    if len(matches) != 1:
        raise OverlayError(f"{path}: expected exactly one [project].{key} assignment, found {len(matches)}")
    return matches[0]


def validate(text: str, path: Path) -> str:
    if project_scalar(text, "name", path) != "telnyx":
        raise OverlayError(f"{path}: project.name must be 'telnyx'")
    version = project_scalar(text, "version", path)
    if not SEMVER.fullmatch(version):
        raise OverlayError(f"{path}: project.version must be a valid semantic version (X.Y.Z)")
    return version


def replace_project_version(text: str, version: str, path: Path) -> str:
    lines = text.splitlines(keepends=True)
    in_project = False
    matches: list[int] = []

    for index, line in enumerate(lines):
        section = SECTION.match(line.rstrip("\r\n"))
        if section:
            in_project = section.group(1).strip() == "project"
            continue
        if in_project and VERSION.match(line):
            matches.append(index)

    if len(matches) != 1:
        raise OverlayError(f"{path}: expected exactly one [project].version assignment, found {len(matches)}")

    index = matches[0]
    match = VERSION.match(lines[index])
    if match is None:  # defensive: the index was collected using the same expression
        raise OverlayError(f"{path}: could not parse [project].version assignment")
    lines[index] = (
        f"{match.group('prefix')}{match.group('quote')}{version}{match.group('quote')}"
        f"{match.group('suffix')}{match.group('newline')}"
    )
    return "".join(lines)


def overlay(source: Path, target: Path) -> None:
    source_text = read(source)
    target_text = read(target)
    version = validate(source_text, source)
    validate(target_text, target)
    updated = replace_project_version(target_text, version, target)

    # Validate before replacing the target and require the exact source version.
    if validate(updated, target) != version:
        raise OverlayError(f"overlay did not set {target} project.version to {version}")

    target.write_text(updated, encoding="utf-8")
    print(f"Copied project.version={version} from {source} to {target}; retained target dependencies and metadata")


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(f"usage: {argv[0]} SOURCE_PYPROJECT TARGET_PYPROJECT", file=sys.stderr)
        return 2
    try:
        overlay(Path(argv[1]), Path(argv[2]))
    except OverlayError as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
# ruff: noqa: T201
"""Verify an exact Telnyx Python release is available from PyPI."""
from __future__ import annotations

import re
import sys
import json
import time
import argparse
import urllib.error
import urllib.request
from typing import Dict, Mapping, Optional, Sequence

VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_TYPES = frozenset({"bdist_wheel", "sdist"})


class AvailabilityError(RuntimeError):
    pass


def validate_release(payload: Mapping[str, object], version: str) -> Dict[str, Mapping[str, object]]:
    info = payload.get("info")
    urls = payload.get("urls")
    if not isinstance(info, Mapping) or info.get("version") != version:
        raise AvailabilityError("PyPI metadata version does not match exact release")
    if not isinstance(urls, list):
        raise AvailabilityError("PyPI release file list is missing")
    found: Dict[str, Mapping[str, object]] = {}
    for raw in urls:
        if not isinstance(raw, Mapping):
            continue
        kind = raw.get("packagetype")
        if kind not in REQUIRED_TYPES:
            continue
        if not isinstance(raw.get("filename"), str) or version not in str(raw["filename"]):
            raise AvailabilityError("release filename does not bind exact version")
        digests = raw.get("digests")
        sha = digests.get("sha256") if isinstance(digests, Mapping) else None
        if not isinstance(sha, str) or not SHA256_RE.fullmatch(sha):
            raise AvailabilityError("release file lacks a valid SHA-256 digest")
        if not isinstance(raw.get("size"), int) or int(raw["size"]) <= 0:
            raise AvailabilityError("release file has invalid size")
        if not isinstance(raw.get("url"), str) or not str(raw["url"]).startswith("https://files.pythonhosted.org/"):
            raise AvailabilityError("release file has an untrusted download URL")
        found[str(kind)] = raw
    missing = REQUIRED_TYPES - set(found)
    if missing:
        raise AvailabilityError("missing PyPI distribution types: %s" % ", ".join(sorted(missing)))
    return found


def fetch_json(url: str) -> Mapping[str, object]:
    request = urllib.request.Request(url, headers={"User-Agent": "telnyx-python-release-readiness/1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if not isinstance(payload, Mapping):
        raise AvailabilityError("invalid PyPI response")
    return payload


def verify_download_metadata(files: Mapping[str, Mapping[str, object]]) -> None:
    for kind, data in files.items():
        request = urllib.request.Request(str(data["url"]), method="HEAD", headers={"User-Agent": "telnyx-python-release-readiness/1"})
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise AvailabilityError("%s distribution is not downloadable" % kind)
            length = response.headers.get("Content-Length")
            if length is not None and int(length) != int(data["size"]):
                raise AvailabilityError("%s distribution size differs from PyPI metadata" % kind)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--attempts", type=int, default=20)
    parser.add_argument("--delay", type=int, default=15)
    args = parser.parse_args(argv)
    if not VERSION_RE.fullmatch(args.version) or args.attempts < 1 or args.delay < 0:
        print("invalid release verification arguments", file=sys.stderr)
        return 2
    endpoint = "https://pypi.org/pypi/telnyx/%s/json" % args.version
    last = "not found"
    for attempt in range(args.attempts):
        try:
            files = validate_release(fetch_json(endpoint), args.version)
            verify_download_metadata(files)
            print("verified PyPI telnyx %s (%s)" % (args.version, ", ".join(sorted(files))))
            return 0
        except (AvailabilityError, urllib.error.URLError, TimeoutError, ValueError) as exc:
            last = str(exc)
            if attempt + 1 < args.attempts:
                time.sleep(args.delay)
    print("PyPI release availability failed: %s" % last, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

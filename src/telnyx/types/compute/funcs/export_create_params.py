# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ExportCreateParams"]


class ExportCreateParams(TypedDict, total=False):
    endpoint: Required[str]
    """HTTPS URL to push logs to"""

    headers: Required[Dict[str, str]]
    """Headers attached to every export push, as key-value pairs (e.g.

    an auth token the collector expects). Required even when empty — {} means "no
    headers". Encrypted at rest; never returned.
    """

    invocation_export_enabled: Required[bool]
    """Export invocation records (one per HTTP request) to this destination"""

    runtime_export_enabled: Required[bool]
    """Export runtime logs (function stdout/stderr) to this destination"""

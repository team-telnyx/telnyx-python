# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["KeyListParams"]


class KeyListParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a previous response's `meta.cursor`."""

    limit: int
    """Maximum number of keys to return. Values above 1000 are treated as 1000."""

    prefix: str
    """Return only keys that start with this prefix."""

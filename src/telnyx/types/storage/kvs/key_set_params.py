# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["KeySetParams"]


class KeySetParams(TypedDict, total=False):
    id: Required[str]

    body: Required[FileTypes]
    """Raw value bytes, stored verbatim."""

    ttl_secs: int
    """Time-to-live in seconds.

    When set, the key expires and is deleted after this duration. Requires a
    namespace provisioned with TTL support; namespaces without it return a `409`.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RcsContentInfoParam"]


class RcsContentInfoParam(TypedDict, total=False):
    file_url: Required[str]
    """Publicly reachable URL of the file."""

    force_refresh: bool
    """If set the URL content will not be cached."""

    thumbnail_url: str
    """Publicly reachable URL of the thumbnail. Maximum size of 100 kB."""

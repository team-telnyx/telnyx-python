# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailInboxListParams"]


class EmailInboxListParams(TypedDict, total=False):
    page_cursor: str
    """Opaque cursor returned by the previous inbox page."""

    page_size: int
    """Number of results to return. Defaults to 20; maximum is 250."""

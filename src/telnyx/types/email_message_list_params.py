# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailMessageListParams"]


class EmailMessageListParams(TypedDict, total=False):
    page_cursor: str
    """Opaque URL-safe Base64 cursor returned by a previous list response."""

    page_size: int
    """Number of results to return.

    Defaults to 25; maximum is 100. Invalid values are clamped to the valid range.
    """

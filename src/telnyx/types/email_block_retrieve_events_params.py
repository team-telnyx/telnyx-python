# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailBlockRetrieveEventsParams"]


class EmailBlockRetrieveEventsParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Offset page number (≥1, default 1)."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Page size (default 50, max 100)."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoiceCloneListParams"]


class VoiceCloneListParams(TypedDict, total=False):
    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Case-insensitive substring filter on the name field."""

    filter_provider: Annotated[Literal["telnyx", "minimax"], PropertyInfo(alias="filter[provider]")]
    """Filter by voice synthesis provider. Case-insensitive."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number for pagination (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results per page."""

    sort: Literal["name", "-name", "created_at", "-created_at"]
    """Sort order. Prefix with `-` for descending. Defaults to `-created_at`."""

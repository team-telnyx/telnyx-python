# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PronunciationDictListParams"]


class PronunciationDictListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number (1-based). Defaults to 1."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results per page. Defaults to 20, maximum 250."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["MediaListParams", "Filter"]


class MediaListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[content_type][]
    """


class Filter(TypedDict, total=False):
    content_type: List[str]
    """Filters files by given content types"""

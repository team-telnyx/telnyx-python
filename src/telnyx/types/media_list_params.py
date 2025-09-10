# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["MediaListParams", "Filter"]


class MediaListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[content_type][]
    """


class Filter(TypedDict, total=False):
    content_type: SequenceNotStr[str]
    """Filters files by given content types"""

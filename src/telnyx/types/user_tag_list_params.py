# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserTagListParams", "Filter"]


class UserTagListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[starts_with]
    """


class Filter(TypedDict, total=False):
    starts_with: str
    """Filter tags by prefix"""

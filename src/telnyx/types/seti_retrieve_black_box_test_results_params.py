# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SetiRetrieveBlackBoxTestResultsParams", "Filter"]


class SetiRetrieveBlackBoxTestResultsParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[product]"""


class Filter(TypedDict, total=False):
    product: str
    """Filter results for a specific product."""

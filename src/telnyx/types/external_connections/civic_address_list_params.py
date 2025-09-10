# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["CivicAddressListParams", "Filter"]


class CivicAddressListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for civic addresses (deepObject style).

    Supports filtering by country.
    """


class Filter(TypedDict, total=False):
    country: SequenceNotStr[str]
    """The country (or countries) to filter addresses by."""

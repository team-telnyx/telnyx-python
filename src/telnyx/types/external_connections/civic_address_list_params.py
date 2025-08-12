# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["CivicAddressListParams", "Filter"]


class CivicAddressListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for civic addresses (deepObject style).

    Supports filtering by country.
    """


class Filter(TypedDict, total=False):
    country: List[str]
    """The country (or countries) to filter addresses by."""

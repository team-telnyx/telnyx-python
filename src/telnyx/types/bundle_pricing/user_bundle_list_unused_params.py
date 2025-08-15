# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["UserBundleListUnusedParams", "Filter"]


class UserBundleListUnusedParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Supports filtering by country_iso and resource. Examples: filter[country_iso]=US
    or filter[resource]=+15617819942
    """

    authorization_bearer: str
    """Authenticates the request with your Telnyx API V2 KEY"""


class Filter(TypedDict, total=False):
    country_iso: List[str]
    """Filter by country code."""

    resource: List[str]
    """Filter by resource."""

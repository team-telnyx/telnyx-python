# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BillingBundleListParams", "Filter"]


class BillingBundleListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Supports filtering by country_iso and resource. Examples: filter[country_iso]=US
    or filter[resource]=+15617819942
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    authorization_bearer: str
    """Authenticates the request with your Telnyx API V2 KEY"""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Supports filtering by country_iso and resource. Examples: filter[country_iso]=US or filter[resource]=+15617819942
    """

    country_iso: SequenceNotStr[str]
    """Filter by country code."""

    resource: SequenceNotStr[str]
    """Filter by resource."""

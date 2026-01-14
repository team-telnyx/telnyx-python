# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ShortCodeListParams", "Filter"]


class ShortCodeListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[messaging_profile_id]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[messaging_profile_id]
    """

    messaging_profile_id: str
    """Filter by Messaging Profile ID.

    Use the string `null` for phone numbers without assigned profiles. A synonym for
    the `/messaging_profiles/{id}/short_codes` endpoint when querying about an
    extant profile.
    """
